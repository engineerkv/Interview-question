# Roundbook

Spoken interview answers, full-stack designs, and pocket cards for Senior Engineer and Tech Lead rounds. Markdown notes, published as a quiet reading site.

**Site:** https://engineerkv.github.io/Interview-question/

## The library

| Section | What it is |
| --- | --- |
| **Start Here** | How to use the book, pick a path, and practise out loud |
| **Language Core** | JavaScript, TypeScript, and DSA you can write from memory |
| **Interface Engineering** | HTML, CSS, React, Next.js, and how the browser actually renders |
| **Service Engineering** | APIs, data, workers, and messaging behind the product |
| **Production Engineering** | Ship, observe, and recover: Git through Kubernetes, SLOs, and security |
| **Design Rounds** | Timed full-stack designs with trade-offs you can defend |
| **Applied AI** | LLMs, RAG, evals, and AI in the delivery loop without shipping fiction |
| **Agent Systems** | When to use an agent, how to tool it, and where humans stay in the loop |
| **Staff Craft** | Reviews, decisions, mentoring, and STAR stories for Tech Lead loops |
| **Warmups** | Short puzzles for a 10-minute reset |
| **Pocket Cards** | One-page cheatsheets for last-mile revision |
| **House Style** | How answers are written so the book stays consistent |

Open [docs/intro/learning-paths.md](docs/intro/learning-paths.md) for the full sequence.

## Local development

Requires Node 20+.

```bash
npm ci
npm start
```

The app runs at http://localhost:3000. GitHub Pages uses `/Interview-question/` automatically in CI.

```bash
npm run build
npm run serve
```

## Deploy

Pushes to `main` build and deploy through [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml).

Repository settings:

1. **Pages** → Source: **GitHub Actions**
2. Confirm Pages is deployed via GitHub Actions (CI sets `baseUrl` to `/Interview-question/`)

## Content layout

```text
docs/
├── intro/                  Start Here
├── fundamentals/           Language Core
├── frontend/               Interface Engineering
├── backend/                Service Engineering
├── devops/                 Production Engineering
├── case-studies/           Design Rounds
├── ai/                     Applied AI
├── agentic-workflows/      Agent Systems
├── leadership/             Staff Craft
├── puzzles/                Warmups
├── reference/              Pocket Cards
└── contributing/           House Style
```

## How to contribute

1. Read [House Style](docs/contributing/content-standards.md).
2. Prefer updating existing answers over adding duplicate questions.
3. Label legacy topics instead of deleting them.
4. Add a practical example, and a Mermaid diagram when the topic is a flow or architecture.

## License

Personal study notes. Review third-party snippets before reuse in production.
