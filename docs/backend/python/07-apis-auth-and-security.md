---
sidebar_label: "APIs, Auth and Security"
description: "REST design, pagination, idempotency keys, JWT vs sessions, OAuth2 in FastAPI, password hashing, common Python vulnerabilities and 12-factor secrets."
---

# Python APIs, Auth and Security (Q77-Q84)

> **Reviewed:** 2026-09 · **Level:** Senior · **Type:** Foundational

## Q77. REST API design in Python

Good REST design is framework-independent: resource-oriented nouns (`/orders/{id}`), correct methods and status codes (201 with `Location` on create, 204 on delete, 409 on conflict, 422 on validation errors), consistent error bodies, and versioning via path or header. In Python, separate input schemas, output schemas and ORM models so you never accidentally expose internal fields. FastAPI generates OpenAPI from these schemas; in Django, DRF serializers and viewsets play the same role.

- **Trade-offs**:
  - Separate schemas add some duplication but give explicit contracts and safe evolution; exposing ORM models directly is quicker but leaks fields and couples API to schema.

**Example:**

```python
from fastapi import APIRouter, HTTPException, Response, status
from pydantic import BaseModel, Field

router = APIRouter(prefix="/v1/orders", tags=["orders"])

class OrderCreate(BaseModel):
    sku: str
    qty: int = Field(gt=0)

class OrderOut(BaseModel):
    id: int
    sku: str
    qty: int
    status: str

@router.post("", status_code=status.HTTP_201_CREATED, response_model=OrderOut)
async def create_order(body: OrderCreate, response: Response):
    order = {"id": 1, **body.model_dump(), "status": "pending"}
    response.headers["Location"] = f"/v1/orders/{order['id']}"
    return order

@router.get("/{order_id}", response_model=OrderOut)
async def get_order(order_id: int):
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail={"code": "order_not_found"})
```

**Remember:** Nouns, correct status codes, separate in/out schemas, versioned paths.

## Q78. Pagination strategies

Offset pagination (`?limit=20&offset=40`) is simple and supports jumping to page N, but gets slower on deep pages and can skip or duplicate rows when data changes. Cursor (keyset) pagination uses the last seen sort key (`WHERE (created_at, id) < (:ts, :id)`) with an index, giving stable and fast pages for feeds and large tables. Return an opaque cursor and cap `limit` server-side.

- **Trade-offs**:
  - Offset: easy UI with page numbers, poor at scale.
  - Cursor: consistent and index-friendly, but no random page access and needs a unique, ordered key.

**Example:**

```python
import base64, json
from typing import Annotated
from fastapi import Query
from sqlalchemy import select, tuple_

def encode_cursor(ts: str, id_: int) -> str:
    return base64.urlsafe_b64encode(json.dumps([ts, id_]).encode()).decode()

def decode_cursor(c: str) -> tuple[str, int]:
    ts, id_ = json.loads(base64.urlsafe_b64decode(c))
    return ts, id_

@router.get("")
async def list_orders(session: SessionDep, limit: Annotated[int, Query(le=100)] = 20, cursor: str | None = None):
    stmt = select(Order).order_by(Order.created_at.desc(), Order.id.desc()).limit(limit + 1)
    if cursor:
        ts, id_ = decode_cursor(cursor)
        stmt = stmt.where(tuple_(Order.created_at, Order.id) < (ts, id_))
    rows = list(await session.scalars(stmt))
    has_more = len(rows) > limit
    rows = rows[:limit]
    next_cursor = encode_cursor(rows[-1].created_at.isoformat(), rows[-1].id) if has_more else None
    return {"items": rows, "next_cursor": next_cursor}
```

**Remember:** Offset for small admin lists; keyset cursors for anything large or live.

## Q79. Idempotency keys for safe retries

Clients and proxies retry on timeouts, so non-idempotent operations like "create payment" can run twice. An idempotency key (a client-generated UUID in an `Idempotency-Key` header) lets the server store the first result and return it for repeats. Implement it with a unique constraint or an atomic Redis `SET NX`, store the response together with a hash of the request, and reject reuse of the key with a different payload.

- **Trade-offs**:
  - Safe retries and exactly-once effects from the client's view, at the cost of storage, TTL management, and handling concurrent in-flight duplicates (return 409 or wait).

**Example:**

```python
import hashlib, json
from fastapi import Header, HTTPException

async def create_payment(body: dict, idempotency_key: str = Header(alias="Idempotency-Key")) -> dict:
    req_hash = hashlib.sha256(json.dumps(body, sort_keys=True).encode()).hexdigest()
    key = f"idem:{idempotency_key}"

    # Reserve the key atomically; only the first request proceeds
    if not await redis.set(key, json.dumps({"state": "processing", "hash": req_hash}), nx=True, ex=86400):
        saved = json.loads(await redis.get(key))
        if saved["hash"] != req_hash:
            raise HTTPException(422, "idempotency key reused with different payload")
        if saved["state"] == "processing":
            raise HTTPException(409, "request in progress")
        return saved["response"]

    result = await charge_card(body)                  # the side effect
    await redis.set(key, json.dumps({"state": "done", "hash": req_hash, "response": result}), ex=86400)
    return result

async def charge_card(body: dict) -> dict: ...
```

**Remember:** Reserve the key atomically, store the response, compare request hashes.

## Q80. JWT vs server-side sessions

Server-side sessions store state in Redis or the DB and give the browser an opaque cookie ID; revocation is instant and tokens are small, but every request needs a lookup. JWTs are signed, self-contained tokens verified without a lookup, which suits service-to-service calls and distributed APIs, but they cannot be revoked before expiry without a denylist. A common design is short-lived access JWTs (minutes) plus rotating refresh tokens stored server-side; for browsers, keep tokens in `HttpOnly`, `Secure`, `SameSite` cookies rather than `localStorage`.

- **Trade-offs**:
  - Sessions: easy revocation and small cookies, but shared session store required.
  - JWTs: stateless scaling, but revocation, key rotation and token size become your problem; always validate `alg`, `exp`, `aud` and `iss`.

**Example:**

```python
from datetime import datetime, timedelta, timezone
import jwt  # PyJWT

SECRET = "load-from-settings"

def issue_access_token(user_id: int) -> str:
    now = datetime.now(timezone.utc)
    return jwt.encode(
        {"sub": str(user_id), "iat": now, "exp": now + timedelta(minutes=15),
         "aud": "orders-api", "iss": "auth.example.com"},
        SECRET, algorithm="HS256",
    )

def verify(token: str) -> dict:
    return jwt.decode(token, SECRET, algorithms=["HS256"],   # pin the algorithm list
                      audience="orders-api", issuer="auth.example.com")
```

**Remember:** Sessions revoke easily; JWTs scale statelessly; short-lived access plus refresh is the usual compromise.

## Q81. OAuth2 flows in FastAPI

OAuth2 is a delegation framework: the Authorization Code flow with PKCE is the standard for user logins (web and mobile), Client Credentials is for service-to-service, and the Password grant is legacy and discouraged. FastAPI provides security helpers such as `OAuth2PasswordBearer` (which just extracts a bearer token and wires OpenAPI) and `OAuth2AuthorizationCodeBearer`; your dependency then validates the token, usually a JWT from an identity provider verified against its JWKS. Scopes and roles are enforced per route with `Security` or dependencies.

- **Trade-offs**:
  - Delegating to an identity provider (Auth0, Keycloak, Cognito) offloads MFA, password resets and compliance, at the cost of an external dependency and token validation complexity; rolling your own is rarely justified.

**Example:**

```python
from typing import Annotated
import jwt
from fastapi import Depends, FastAPI, HTTPException, Security
from fastapi.security import OAuth2AuthorizationCodeBearer, SecurityScopes

oauth2 = OAuth2AuthorizationCodeBearer(
    authorizationUrl="https://idp.example.com/authorize",
    tokenUrl="https://idp.example.com/oauth/token",
    scopes={"orders:read": "Read orders", "orders:write": "Create orders"},
)
jwks = jwt.PyJWKClient("https://idp.example.com/.well-known/jwks.json")

async def current_user(scopes: SecurityScopes, token: Annotated[str, Depends(oauth2)]) -> dict:
    try:
        key = jwks.get_signing_key_from_jwt(token).key
        claims = jwt.decode(token, key, algorithms=["RS256"], audience="orders-api")
    except jwt.PyJWTError:
        raise HTTPException(401, "invalid token", headers={"WWW-Authenticate": "Bearer"})
    granted = set(claims.get("scope", "").split())
    if not set(scopes.scopes) <= granted:
        raise HTTPException(403, "insufficient scope")
    return claims

app = FastAPI()

@app.post("/orders")
async def create(user: Annotated[dict, Security(current_user, scopes=["orders:write"])]):
    return {"created_by": user["sub"]}
```

**Remember:** Auth Code + PKCE for users, Client Credentials for services; validate tokens in a dependency.

## Q82. Password hashing with bcrypt and Argon2

Never store passwords in plaintext or with fast hashes like SHA-256 or MD5; use a slow, salted, memory-hard or adaptive algorithm. Argon2id is the modern recommendation (via `argon2-cffi`), and bcrypt remains widely acceptable; Django defaults to PBKDF2 and supports Argon2 and bcrypt hashers. Libraries embed the salt and parameters in the hash string, so you can raise cost over time and rehash on login.

- **Trade-offs**:
  - Higher cost slows brute force but also adds login latency and CPU load; run hashing off the event loop in async apps.
  - bcrypt only uses the first 72 bytes of input.

**Example:**

```python
import asyncio
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()   # Argon2id with library defaults

def hash_password(pw: str) -> str:
    return ph.hash(pw)  # salt and params embedded in the string

def verify_password(stored: str, pw: str) -> tuple[bool, str | None]:
    try:
        ph.verify(stored, pw)
    except VerifyMismatchError:
        return False, None
    new_hash = ph.hash(pw) if ph.check_needs_rehash(stored) else None
    return True, new_hash

async def login(stored: str, pw: str) -> bool:
    ok, _ = await asyncio.to_thread(verify_password, stored, pw)   # CPU work off the loop
    return ok
```

**Remember:** Argon2id or bcrypt, never fast hashes; rehash when parameters change.

## Q83. Common vulnerabilities: injection, SSRF and unsafe deserialisation

SQL injection comes from string-formatting queries; always use bound parameters, which ORMs and `text()` do by default. SSRF happens when your server fetches user-supplied URLs and can be tricked into hitting internal services or cloud metadata endpoints; validate schemes and hosts against an allowlist, resolve and block private IP ranges, and disable redirects. `pickle`, `yaml.load` without `SafeLoader`, `eval` and `shelve` can execute arbitrary code on untrusted input; use JSON, `yaml.safe_load` and signed payloads instead. Also watch for command injection (`subprocess` with `shell=True`) and path traversal in file downloads.

- **Trade-offs**:
  - Strict allowlists and safe formats reduce flexibility (no arbitrary objects, fewer URLs) but remove whole classes of remote code execution.

**Example:**

```python
import ipaddress, socket, subprocess
from urllib.parse import urlparse
import yaml

# Injection: bound parameters, never f-strings
session.execute(text("SELECT * FROM users WHERE email = :e"), {"e": email})

# Command injection: pass a list, no shell
subprocess.run(["convert", input_path, output_path], check=True)

# Unsafe deserialisation
data = yaml.safe_load(user_yaml)          # not yaml.load(user_yaml)
# pickle.loads(untrusted_bytes)           # remote code execution risk

# SSRF guard (simplified; also re-check after redirects or disable them)
ALLOWED_HOSTS = {"images.partner.com"}
def safe_url(url: str) -> str:
    u = urlparse(url)
    if u.scheme != "https" or u.hostname not in ALLOWED_HOSTS:
        raise ValueError("url not allowed")
    for info in socket.getaddrinfo(u.hostname, 443):
        if ipaddress.ip_address(info[4][0]).is_private:
            raise ValueError("private address")
    return url
```

**Remember:** Parameterise SQL, allowlist outbound URLs, never unpickle untrusted data.

## Q84. Secrets and configuration (12-factor)

The 12-factor approach stores config in the environment, separate from code, so the same image runs in every environment with different settings. Secrets come from a secrets manager (AWS Secrets Manager, Vault, Kubernetes secrets) injected as env vars or files at runtime, never committed to git or baked into Docker images. Validate config at startup (pydantic-settings), keep secrets out of logs and reprs (`SecretStr`), and support rotation.

- **Trade-offs**:
  - Env vars are universal and simple but visible to anything in the process environment and can leak via debug pages or crash dumps; mounted secret files or SDK fetches with caching add safety at the cost of complexity.

**Example:**

```python
import logging
from pydantic import SecretStr
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: SecretStr
    stripe_api_key: SecretStr
    environment: str = "dev"

settings = Settings()      # fails fast if secrets are missing

logging.info("config loaded: %s", settings)   # SecretStr prints as '**********'
stripe_key = settings.stripe_api_key.get_secret_value()   # explicit unwrap at use site

# .gitignore: .env   |   pre-commit: detect-secrets or gitleaks hook
```

**Remember:** Config from the environment, secrets from a manager, validated at startup, never logged.

## References

- [FastAPI security](https://fastapi.tiangolo.com/tutorial/security/)
- [FastAPI OAuth2 scopes](https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/)
- [Django security overview](https://docs.djangoproject.com/en/stable/topics/security/)
- [Django password management](https://docs.djangoproject.com/en/stable/topics/auth/passwords/)
- [pickle module security warning](https://docs.python.org/3/library/pickle.html)
- [secrets module](https://docs.python.org/3/library/secrets.html)
- [Pydantic settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)
- [SQLAlchemy documentation](https://docs.sqlalchemy.org/)
