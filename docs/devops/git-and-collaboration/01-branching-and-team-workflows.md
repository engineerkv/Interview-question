---
sidebar_position: 1
sidebar_label: "Branching & Team Workflows"
description: "Branching strategies, trunk-based development, CODEOWNERS, PR hygiene, monorepo vs polyrepo and team-scale conflict handling."
---

# Branching & Team Workflows

> **Reviewed:** 2026-09 · **Level:** Senior / Tech Lead · **Type:** Foundational

Mechanics like merge vs rebase, cherry-pick and resolving a single conflict are covered in [Git, Docker, CI/CD, Tooling](../ci-cd-and-releases/01-git-docker-ci-cd-tooling.md). This page is about the **team-level** decisions a Tech Lead is expected to own.

---

## Q1. How do you choose a branching strategy for a team?

**Short answer:** I choose based on how often we release and how many versions we support. If we deploy a web service continuously, I prefer trunk-based development with short-lived branches and feature flags. If we ship versioned artifacts — mobile apps, on-prem software, SDKs — with several supported versions, a release-branch model (GitFlow-like) is more honest about reality. The strategy should minimise how long code lives away from `main`.

**How it works:** Every branch is a bet that merging later will be cheap. The longer a branch lives, the more `main` drifts and the more expensive integration gets. So the real question is: "What forces us to keep code apart from main?" If the answer is only "it's not finished", feature flags solve that. If the answer is "customers run v2 and v3 at the same time", you genuinely need release branches.

| Strategy | Best fit | Main cost |
| --- | --- | --- |
| Trunk-based (short-lived branches, flags) | SaaS, continuous delivery | Needs strong CI and flag discipline |
| GitHub flow (branch → PR → main → deploy) | Small/medium teams, web apps | Little structure for multiple supported versions |
| GitFlow (develop, release, hotfix branches) | Versioned releases, long QA cycles | Merge overhead, slow feedback, "merge hell" |
| Release branches off trunk | Mobile apps, SDKs with LTS versions | Back-porting fixes (cherry-picks) |

**Example:** A team shipping a web API and a mobile app from one repo: the API uses trunk-based deploys on every merge; the mobile app cuts a `release/5.3` branch from `main` at code freeze, and only cherry-picked fixes land on it.

**Trade-offs and pitfalls:**

- Picking GitFlow "because it's a standard" for a SaaS product adds ceremony with no benefit.
- Trunk-based without feature flags and good tests just moves the pain to production.
- Hybrid is fine — the strategy can differ per deliverable.

<details>
<summary>Follow-up questions</summary>

- How would you migrate a team from GitFlow to trunk-based development?
- How do you handle a hotfix when `main` already contains unreleased work?
- What metrics tell you the branching strategy is hurting you?

</details>

**Remember:** Choose the strategy that keeps code away from `main` for the shortest time your release model allows.

---

## Q2. What is trunk-based development and what does it require to work?

**Short answer:** Everyone integrates into a single trunk (`main`) at least daily, via very short-lived branches or direct commits. Unfinished work is hidden behind feature flags, not branches. It only works with fast, reliable CI, a good automated test suite, and a culture of small changes — otherwise you break trunk constantly.

**How it works:**

- Branches live hours to a couple of days, not weeks.
- `main` is always releasable; a red build is a stop-the-line event.
- Features are merged "dark" behind flags and enabled gradually.
- Large changes use **branch by abstraction**: introduce an interface, move callers over incrementally, then delete the old implementation.

**Example:** Replacing a payment provider: add a `PaymentGateway` interface, implement it for the old provider, migrate callers in small PRs, add the new provider behind a flag, ramp traffic, then delete the old code — all on trunk.

**Trade-offs and pitfalls:**

- Flag debt: stale flags become hidden branches in code. Give each flag an owner and expiry.
- Requires CI that finishes in minutes; a 60-minute pipeline kills the model.
- Reviewers must be responsive — slow reviews create long-lived branches by accident.

<details>
<summary>Follow-up questions</summary>

- How do you keep trunk green with many engineers merging daily? (merge queues, required checks)
- What is branch by abstraction and when do you use it?
- How do you test code paths behind feature flags?

</details>

**Remember:** Trunk-based development is a CI discipline, not just a branching diagram.

---

## Q3. What is CODEOWNERS and how do you use it well?

**Short answer:** CODEOWNERS is a file (supported by GitHub, GitLab and others) that maps paths to the people or teams responsible for them. Combined with branch protection, it automatically requests reviews and can require an owner's approval before merge. Used well, it routes reviews to experts; used badly, it creates bottlenecks.

**How it works:** Patterns are matched top to bottom and the **last matching pattern wins**. Owners are usually teams rather than individuals so that vacations don't block merges.

**Example:**

```text
# .github/CODEOWNERS
# Default owners for everything
*                       @acme/platform-reviewers

# Frontend app
/apps/web/              @acme/web-team

# Infrastructure changes need the platform team
/infra/                 @acme/platform-team
*.tf                    @acme/platform-team

# Security-sensitive code requires security review
/services/auth/         @acme/identity-team @acme/security
```

**Trade-offs and pitfalls:**

- Assigning individuals creates single points of failure.
- Too broad (`* @whole-org`) means nobody feels ownership.
- Keep the file itself owned by leads so ownership changes are reviewed.

<details>
<summary>Follow-up questions</summary>

- How would you stop CODEOWNERS from becoming a review bottleneck?
- How does CODEOWNERS interact with required approvals in branch protection?

</details>

**Remember:** CODEOWNERS encodes ownership; branch protection enforces it.

---

## Q4. What does good PR hygiene look like on a senior team?

**Short answer:** Small, focused PRs with a clear description of *why*, not just *what*; green CI before asking for review; a reviewable size; and a fast review turnaround. As a lead, I set expectations like "one logical change per PR", "describe how you tested it", and "review within the same working day".

**How it works:** Review quality drops as PR size grows — reviewers skim large diffs. Small PRs are faster to review, easier to revert and easier to bisect.

Practical checklist:

- Title and description: problem, approach, risks, how it was tested, screenshots for UI.
- Separate refactors from behaviour changes.
- Stack PRs for large features (PR 1: schema, PR 2: API, PR 3: UI behind a flag).
- Automate the boring parts: lint, format, type-check, tests, preview environments.
- Use draft PRs to get early design feedback.

**Example:** A PR template in `.github/pull_request_template.md` with sections "Why", "What changed", "How tested", "Rollout/rollback plan". The rollback section forces people to think about risky changes before merging.

**Trade-offs and pitfalls:**

- Too many tiny PRs without context can fragment understanding — link them to a tracking issue.
- Nitpicks in review should be automated by linters, not humans.

See also: [Automated review process](../../leadership/code-reviews/automated-review-process.md).

<details>
<summary>Follow-up questions</summary>

- How do you handle a 3,000-line PR that landed in your review queue?
- How do you measure review health? (time to first review, time to merge)

</details>

**Remember:** Small PRs, clear "why", green CI, fast reviews.

---

## Q5. Monorepo vs polyrepo — how do you decide?

**Short answer:** A monorepo puts many projects in one repository, which makes atomic cross-project changes, shared tooling and code reuse easy, but needs investment in build tooling so CI doesn't rebuild everything. Polyrepo gives each service its own repo, with clear ownership boundaries and independent pipelines, but cross-repo changes and dependency version drift become painful.

**How it works:**

| Concern | Monorepo | Polyrepo |
| --- | --- | --- |
| Cross-project change | One atomic PR | Coordinated PRs + version bumps |
| Shared code | Import directly | Publish packages |
| CI | Needs affected-only builds and caching | Simple per repo |
| Ownership | CODEOWNERS by path | Repo permissions |
| Tooling | Nx, Turborepo, Bazel, Pants, workspaces | Standard per-language tooling |
| Scale risk | Slow clones/CI if unmanaged | Dependency drift, duplicated config |

**Example:** A product team with a Next.js web app, a React Native app and a shared design system chooses a monorepo with Turborepo: changing a button component and all consumers happens in one PR, and CI only rebuilds affected packages.

**Trade-offs and pitfalls:**

- A monorepo without affected-only CI becomes slow quickly.
- Polyrepo with many internal packages turns into "dependency upgrade week".
- Monorepo does not mean monolith — services can still deploy independently.

<details>
<summary>Follow-up questions</summary>

- How do you run CI only for affected projects? (path filters, build graph)
- How do you enforce module boundaries inside a monorepo?

</details>

**Remember:** Monorepos trade tooling investment for easy cross-cutting change; polyrepos trade coordination cost for autonomy.

---

## Q6. How do you reduce merge conflicts at team scale?

**Short answer:** Most conflicts are a symptom of long-lived branches and shared hotspots. I reduce them by merging small changes often, rebasing on `main` frequently, splitting hotspot files, using code generation carefully, and coordinating big refactors explicitly. For the mechanics of resolving an individual conflict, see the existing Q192 in [Git, Docker, CI/CD, Tooling](../ci-cd-and-releases/01-git-docker-ci-cd-tooling.md).

**How it works:**

- **Integrate often:** short branches mean smaller diffs to reconcile.
- **Split hotspots:** a giant `routes.ts` or `constants.ts` that everyone edits should be split by feature.
- **Avoid churn:** run formatters in CI so whitespace changes don't collide.
- **Lock files:** regenerate rather than hand-merge (`package-lock.json`, `yarn.lock`).
- **Announce big refactors:** do a mechanical rename as a single fast PR at a quiet time.
- **Merge queues:** serialise merges and re-test against the latest `main` to avoid "semantic conflicts" (two PRs that pass alone but break together).

**Example:** Two engineers each add a DB migration numbered `0042`. Both pass CI alone but break together. Fix: timestamp-based migration names plus a merge queue that tests the combined result.

<details>
<summary>Follow-up questions</summary>

- What is a semantic conflict and why doesn't Git detect it?
- How does a merge queue work?

</details>

**Remember:** Prevent conflicts with small, frequent integration; resolve the rest with tests, not guesswork.

---

## Q7. What branch protection rules would you set on `main`?

**Short answer:** Require PRs (no direct pushes), required status checks, at least one approval (owner approval for sensitive paths), up-to-date branch or merge queue, signed or verified commits where needed, and block force-pushes and deletions. Admins should follow the same rules, with a documented break-glass process.

**How it works:** Branch protection turns team agreements into enforcement. The key is choosing checks that are fast and reliable; flaky required checks teach people to bypass rules.

**Example settings:**

- Require pull request with 1 approval; dismiss stale approvals on new commits.
- Require CODEOWNERS review.
- Required checks: `lint`, `unit-tests`, `build`, `security-scan`.
- Require linear history (squash or rebase merges).
- Disallow force push; restrict who can bypass.

**Trade-offs and pitfalls:** Too many required checks slow down delivery; flaky checks erode trust. Quarantine flaky tests rather than making them optional forever.

<details>
<summary>Follow-up questions</summary>

- Squash vs merge commit vs rebase merge — which do you choose and why?
- What does your break-glass procedure look like for a production hotfix?

</details>

**Remember:** Protect `main` with fast, trustworthy checks and no special exceptions.

---

## Q8. How do you manage versioning and changelogs?

**Short answer:** Use Semantic Versioning for anything others consume (libraries, APIs, SDKs), and derive versions and changelogs from structured commit messages such as Conventional Commits. For continuously deployed services, the commit SHA or build number is usually the real version, and the changelog is the deploy log.

**How it works:** SemVer is `MAJOR.MINOR.PATCH`: breaking change, backward-compatible feature, backward-compatible fix. Tools like semantic-release or Changesets read commit messages or changeset files to bump versions and write `CHANGELOG.md`.

**Example:**

```text
feat(api): add cursor-based pagination to /orders
fix(auth): refresh token no longer expires early
feat(api)!: remove deprecated /v1/orders endpoint   # "!" marks a breaking change
```

**Trade-offs and pitfalls:** Commit conventions only help if enforced (commit-lint in CI or PR title checks). Tags must be immutable — never move a release tag.

<details>
<summary>Follow-up questions</summary>

- How do you version a monorepo with many packages?
- How do you communicate breaking API changes to consumers?

</details>

**Remember:** SemVer for consumers, SHAs for deployables, automation for both.

---

## Q9. How do you handle a hotfix when `main` has unreleased changes?

**Short answer:** With trunk-based development and flags, `main` should be deployable, so the hotfix goes to `main` and deploys normally. If `main` contains risky unreleased work, I branch from the last released tag, apply the fix, release it, and make sure the same fix lands on `main` (usually fix on `main` first, then cherry-pick to the release branch).

**How it works:** "Fix forward on main, cherry-pick back" avoids losing the fix in the next release. The opposite direction (fix on release, forget main) causes regressions.

**Example:**

```bash
# Fix merged to main as commit abc123
git switch -c hotfix/5.3.1 v5.3.0   # branch from released tag
git cherry-pick abc123              # apply the same fix
git tag v5.3.1 && git push origin v5.3.1
```

<details>
<summary>Follow-up questions</summary>

- What if the fix doesn't cherry-pick cleanly onto the old release?
- How do you make sure every hotfix is also on main? (automation, checklist)

</details>

**Remember:** Fix on main first, back-port to releases, never the other way round only.

---

## Q10. How do you keep secrets and large files out of Git?

**Short answer:** Prevent, detect, and respond. Prevent with `.gitignore`, pre-commit hooks and secret scanning with push protection; detect with scanners in CI; respond by **rotating the secret immediately** — rewriting history is secondary because the secret must be assumed compromised. For large binaries, use Git LFS or an artifact store instead of committing them.

**How it works:** Once pushed, a secret may already be cloned, cached or forked. Rotation is the only real fix. History rewriting (for example with `git filter-repo`) is cleanup, not remediation.

**Trade-offs and pitfalls:** Rewriting shared history disrupts everyone; coordinate it. Pre-commit hooks can be skipped locally, so server-side scanning is still needed.

<details>
<summary>Follow-up questions</summary>

- A developer pushed an AWS key to a public repo. Walk through your response.
- How do you manage environment config without committing `.env` files?

</details>

**Remember:** A leaked secret is rotated first and cleaned up second.

---

## References

- [Git documentation](https://git-scm.com/doc)
- [GitHub Docs: About code owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
- [GitHub Docs: About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- [Trunk Based Development](https://trunkbaseddevelopment.com/)
- [Semantic Versioning](https://semver.org/)
- [Conventional Commits](https://www.conventionalcommits.org/)
