# Interview Prep Hub

Personal interview knowledge base for Senior Engineer, Frontend Architect, and Tech Lead preparation. Content is Markdown; the site is Docusaurus 3 on GitHub Pages.

**Site:** https://engineerkv.github.io/Interview-question/

## Learning paths

| Path | Start here |
| --- | --- |
| Frontend | HTML → CSS → JavaScript → TypeScript → React → Next.js → Frontend architecture |
| Full-stack | Node **or** Python → SQL / Mongo → Celery / RabbitMQ / MinIO → Backend architecture → DevOps |
| System design | Backend architecture + frontend architecture + [case studies](docs/case-studies/index.md) |
| DevOps | Git → Docker → CI/CD → Cloud → Kubernetes → Telemetry → Reliability → Security |
| AI | LLM fundamentals → RAG → evaluation → AI-assisted development |
| Agentic workflows | Agents → tools/MCP → orchestration → evals → human gates |
| Tech Lead | Code reviews (manual + automated) → leadership → behavioral STAR |

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
├── intro/                  How to use the site, learning paths, assessment
├── fundamentals/           JavaScript, TypeScript, DSA
├── frontend/               HTML, CSS, React, Next.js, React Native, architecture
├── backend/                Node, SQL, Mongo, Python, Celery, RabbitMQ, MinIO, architecture
├── devops/                 Git, Docker, K8s, CI/CD, cloud, IaC, telemetry, SRE, security
├── case-studies/           Full-stack project designs
├── ai/                     LLM, RAG, evals, AI-assisted SDLC
├── agentic-workflows/      Agents, MCP, orchestration, human-in-the-loop
├── leadership/             Reviews, Tech Lead, behavioral
├── puzzles/
├── reference/              Cheatsheet index
└── contributing/           Content standards
```

## How to contribute

1. Read [content standards](docs/contributing/content-standards.md).
2. Prefer updating existing answers over adding duplicate questions.
3. Label legacy topics instead of deleting them.
4. Add a practical example, and a Mermaid diagram when the topic is a flow or architecture.

## License

Personal study notes. Review third-party snippets before reuse in production.
