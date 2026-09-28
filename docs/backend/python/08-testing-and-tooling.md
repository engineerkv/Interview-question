---
sidebar_label: "Testing and Tooling"
description: "pytest fixtures and parametrize, mocking, async tests, endpoint tests, coverage, ruff and black, mypy and pyright, and pre-commit."
---

# Python Testing and Tooling (Q85-Q92)

> **Reviewed:** 2026-09 · **Level:** Senior · **Type:** Foundational

## Q85. pytest fixtures and parametrize

pytest discovers `test_*` functions and uses plain `assert` with rich failure output. Fixtures provide dependencies by name, support setup and teardown via `yield`, have scopes (`function`, `module`, `session`), and live in `conftest.py` to be shared. `@pytest.mark.parametrize` runs one test body over many inputs, which keeps edge cases explicit without copy-paste.

- **Trade-offs**:
  - Fixtures remove boilerplate but deep fixture chains can hide what a test depends on; keep them small and named clearly.
  - Wider scopes (session) are faster but risk shared state between tests.

**Example:**

```python
# conftest.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

@pytest.fixture(scope="session")
def engine():
    eng = create_engine("sqlite+pysqlite:///:memory:")
    Base.metadata.create_all(eng)
    yield eng
    eng.dispose()

@pytest.fixture
def session(engine):
    with engine.connect() as conn:
        trans = conn.begin()
        with Session(bind=conn) as s:
            yield s                  # each test runs inside a transaction
        trans.rollback()             # isolation: nothing persists

# test_pricing.py
@pytest.mark.parametrize(
    ("qty", "expected"),
    [(1, 1000), (10, 9000), (0, 0)],
    ids=["single", "bulk-discount", "zero"],
)
def test_price(qty: int, expected: int) -> None:
    assert price_for(qty) == expected
```

**Remember:** Fixtures inject and clean up; parametrize covers cases without duplication.

## Q86. Mocking with unittest.mock and "patch where it is used"

`unittest.mock` provides `Mock`/`MagicMock`/`AsyncMock` and `patch` to replace objects during a test. The key rule is to patch the name where it is looked up, not where it is defined: if `app.services` does `from app.clients import send_email`, patch `app.services.send_email`. Use `autospec=True` so mocks enforce real signatures, and prefer injecting fakes via dependencies over patching when you control the design.

- **Trade-offs**:
  - Mocks isolate slow or external dependencies, but over-mocking tests implementation details and gives false confidence; mock at system boundaries (HTTP, email, clock) only.

**Example:**

```python
# app/services.py
from app.clients import send_email

def register(email: str) -> None:
    ...
    send_email(email, "Welcome")

# tests/test_services.py
from unittest.mock import patch
from app.services import register

def test_register_sends_welcome() -> None:
    with patch("app.services.send_email", autospec=True) as fake:   # where it is used
        register("a@x.io")
    fake.assert_called_once_with("a@x.io", "Welcome")

# pytest-mock plugin alternative:
def test_register_mocker(mocker) -> None:
    fake = mocker.patch("app.services.send_email", autospec=True)
    register("a@x.io")
    fake.assert_called_once()
```

**Remember:** Patch the lookup location, use autospec, mock only at boundaries.

## Q87. Testing async code

pytest does not run coroutines by itself; use a plugin such as `pytest-asyncio` (mark tests with `@pytest.mark.asyncio` or set `asyncio_mode = "auto"`) or the `anyio` plugin that ships with AnyIO. `AsyncMock` returns awaitables for mocked async functions. Test timeouts, cancellation and concurrency paths explicitly, not just the happy path.

- **Trade-offs**:
  - Async fixtures and event-loop scoping can be confusing (a session-scoped async resource needs a matching loop scope); keep async fixtures function-scoped unless you need otherwise.

**Example:**

```python
import asyncio
import pytest
from unittest.mock import AsyncMock

async def get_price(client, sku: str) -> int:
    async with asyncio.timeout(1):
        return (await client.fetch(sku))["price"]

@pytest.mark.asyncio
async def test_get_price() -> None:
    client = AsyncMock()
    client.fetch.return_value = {"price": 500}
    assert await get_price(client, "A1") == 500
    client.fetch.assert_awaited_once_with("A1")

@pytest.mark.asyncio
async def test_get_price_timeout() -> None:
    async def slow_fetch(sku: str) -> dict:
        await asyncio.sleep(5)
        return {"price": 1}

    client = AsyncMock()
    client.fetch.side_effect = slow_fetch      # async side_effect is awaited
    with pytest.raises(TimeoutError):
        await get_price(client, "A1")
```

**Remember:** Use an async pytest plugin and `AsyncMock`; test timeouts and cancellation too.

## Q88. Testing FastAPI and Django endpoints

FastAPI's `TestClient` (built on httpx) calls the app in-process without a real server; for async tests use `httpx.AsyncClient` with `ASGITransport`. Override dependencies with `app.dependency_overrides` to inject a test DB session or fake user. Django's test `Client` and `TestCase` wrap each test in a transaction, and pytest-django adds fixtures like `client` and the `django_db` marker.

- **Trade-offs**:
  - In-process endpoint tests are fast and cover routing, validation and serialisation; they do not catch server config issues, so keep a few smoke tests against a real container.
  - Prefer a real database (for example Postgres in a container) over SQLite if you rely on Postgres-specific behaviour.

**Example:**

```python
import pytest
from fastapi.testclient import TestClient
from httpx import ASGITransport, AsyncClient
from app.main import app, current_user

def test_create_order_validation() -> None:
    app.dependency_overrides[current_user] = lambda: {"sub": "42"}
    client = TestClient(app)
    r = client.post("/v1/orders", json={"sku": "A1", "qty": 0})
    assert r.status_code == 422
    app.dependency_overrides.clear()

@pytest.mark.asyncio
async def test_health_async() -> None:
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        r = await ac.get("/health")
    assert r.json() == {"ok": True}

# Django with pytest-django
@pytest.mark.django_db
def test_product_list(client) -> None:
    r = client.get("/api/products/")
    assert r.status_code == 200
```

**Remember:** In-process clients plus dependency overrides; a real DB for realistic tests.

## Q89. Code coverage

`coverage.py` (often via `pytest-cov`) measures which lines and branches ran during tests. Enable branch coverage, report missing lines, and enforce a threshold in CI with `--cov-fail-under` so coverage does not regress. Coverage shows what is untested, not whether tests are good; critical paths still need meaningful assertions.

- **Trade-offs**:
  - A coverage gate prevents neglect but chasing 100% leads to low-value tests; focus on domain logic and error paths.

**Example:**

```python
# pyproject.toml (shown as comments)
# [tool.pytest.ini_options]
# addopts = "--cov=app --cov-branch --cov-report=term-missing --cov-fail-under=85"
#
# [tool.coverage.run]
# omit = ["app/migrations/*"]
#
# [tool.coverage.report]
# exclude_also = ["if TYPE_CHECKING:", "raise NotImplementedError"]

# Run: pytest
```

**Remember:** Branch coverage with a CI floor; coverage finds gaps, not quality.

## Q90. Linting and formatting with ruff and black

`ruff` is a very fast linter (implemented in Rust) that replaces flake8, isort, pyupgrade and many plugins, and `ruff format` is a black-compatible formatter; `black` remains a widely used opinionated formatter. Configure them in `pyproject.toml`, run them in pre-commit and CI, and let formatting be automatic so code review focuses on logic. Select rule sets deliberately (for example pyflakes, bugbear, security rules) rather than enabling everything.

- **Trade-offs**:
  - Consistent style and early bug detection versus noisy rules; start with a curated set and add per-file ignores sparingly.

**Example:**

```python
# pyproject.toml (shown as comments)
# [tool.ruff]
# line-length = 100
# target-version = "py312"
#
# [tool.ruff.lint]
# select = ["E", "F", "I", "B", "UP", "S", "ASYNC"]   # pycodestyle, pyflakes, isort, bugbear, pyupgrade, bandit, async
# ignore = ["E501"]
#
# [tool.ruff.lint.per-file-ignores]
# "tests/*" = ["S101"]      # allow assert in tests

# Commands:
# ruff check . --fix
# ruff format .            (or: black .)
```

**Remember:** ruff for lint and format, configured in pyproject, enforced in CI.

## Q91. Static type checking with mypy and pyright

mypy and pyright analyse type hints without running the code, catching `None` handling errors, wrong argument types and broken refactors. pyright powers Pylance in VS Code and is fast; mypy is the long-standing reference checker with a plugin system (for example for Django and Pydantic). Adopt gradually: start with checking new modules, enable `strict` per package, and avoid scattering `Any` and `# type: ignore`.

- **Trade-offs**:
  - Safer refactors and better editor help versus annotation effort and occasional friction with dynamic libraries lacking stubs.

**Example:**

```python
# pyproject.toml (shown as comments)
# [tool.mypy]
# python_version = "3.12"
# strict = true
# plugins = ["pydantic.mypy"]
#
# [[tool.mypy.overrides]]
# module = "legacy.*"
# ignore_errors = true

def find_user(user_id: int) -> dict | None: ...

def email_of(user_id: int) -> str:
    user = find_user(user_id)
    return user["email"]      # mypy: Value of type "dict | None" is not indexable

def email_of_fixed(user_id: int) -> str:
    user = find_user(user_id)
    if user is None:
        raise LookupError(user_id)
    return user["email"]      # narrowed to dict
```

**Remember:** Type check in CI, adopt strictness gradually, keep `Any` rare.

## Q92. pre-commit hooks

`pre-commit` manages git hooks declared in `.pre-commit-config.yaml`, running tools like ruff, mypy, secret scanners and file checks on staged files before each commit. It gives fast local feedback and consistent tool versions across the team. CI should run the same hooks (`pre-commit run --all-files`) because local hooks can be skipped.

- **Trade-offs**:
  - Catches issues before review, but slow hooks annoy developers; keep heavy checks (full test suite, slow type checks) in CI.

**Example:**

```python
# .pre-commit-config.yaml (YAML shown as comments; pin rev to real release tags)
# repos:
#   - repo: https://github.com/astral-sh/ruff-pre-commit
#     rev: vX.Y.Z
#     hooks:
#       - id: ruff
#         args: [--fix]
#       - id: ruff-format
#   - repo: https://github.com/pre-commit/pre-commit-hooks
#     rev: vX.Y.Z
#     hooks:
#       - id: check-yaml
#       - id: end-of-file-fixer
#       - id: detect-private-key
#
# Setup: pre-commit install
# CI:    pre-commit run --all-files
```

**Remember:** Fast checks at commit time, the same checks again in CI.

## References

- [pytest documentation](https://docs.pytest.org/)
- [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)
- [pytest parametrize](https://docs.pytest.org/en/stable/how-to/parametrize.html)
- [unittest.mock](https://docs.python.org/3/library/unittest.mock.html)
- [unittest.mock: where to patch](https://docs.python.org/3/library/unittest.mock.html#where-to-patch)
- [FastAPI testing](https://fastapi.tiangolo.com/tutorial/testing/)
- [Django testing](https://docs.djangoproject.com/en/stable/topics/testing/)
- [typing module](https://docs.python.org/3/library/typing.html)
