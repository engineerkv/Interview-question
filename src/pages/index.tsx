import type {ReactNode} from 'react';
import Link from '@docusaurus/Link';
import Layout from '@theme/Layout';
import SearchBar from '@theme/SearchBar';
import styles from './index.module.css';

type Track = {
  title: string;
  description: string;
  to: string;
  steps: string[];
};

const tracks: Track[] = [
  {
    title: 'Frontend',
    description: 'Browser, JavaScript, React, Next.js, performance and frontend architecture.',
    to: '/frontend',
    steps: ['HTML & CSS', 'JavaScript & TypeScript', 'React & Next.js', 'Architecture deep dives'],
  },
  {
    title: 'System Design',
    description: 'Full-stack case studies with frontend, backend, scalability and trade-offs.',
    to: '/case-studies',
    steps: ['Backend architecture', 'Messaging & storage', 'Case studies', 'Scaling with AI'],
  },
  {
    title: 'DevOps & Production',
    description: 'Docker, Kubernetes, CI/CD, cloud, telemetry, reliability and supply-chain security.',
    to: '/devops',
    steps: ['Containers', 'Kubernetes', 'CI/CD & releases', 'SLOs & incidents'],
  },
  {
    title: 'AI Engineering',
    description: 'LLMs, RAG, evaluation, guardrails and AI-assisted software delivery.',
    to: '/ai',
    steps: ['LLM fundamentals', 'RAG & retrieval', 'Evaluation & safety', 'AI-assisted SDLC'],
  },
  {
    title: 'Agentic Workflows',
    description: 'Agents, tools, MCP, orchestration, evaluation and human approval gates.',
    to: '/agentic-workflows',
    steps: ['Agents vs workflows', 'Tools & MCP', 'Orchestration', 'Human-in-the-loop'],
  },
  {
    title: 'Tech Lead',
    description: 'Architecture decisions, code reviews, mentoring, delivery and behavioral rounds.',
    to: '/leadership',
    steps: ['Code reviews', 'Technical leadership', 'Behavioral (STAR)', 'Automated review'],
  },
];

const quickLinks = [
  {label: 'Backend: Node.js & Express', to: '/backend/node-express/question-index'},
  {label: 'Backend: Python Top 100', to: '/backend/python'},
  {label: 'Celery workers', to: '/backend/celery'},
  {label: 'RabbitMQ', to: '/backend/rabbitmq'},
  {label: 'MinIO object storage', to: '/backend/minio'},
  {label: 'DSA problems', to: '/fundamentals/dsa'},
  {label: 'All cheatsheets', to: '/reference'},
  {label: 'Automated code review', to: '/leadership/code-reviews/automated-review-process'},
];

function TrackCard({title, description, to, steps}: Track) {
  return (
    <Link to={to} className={styles.card}>
      <h3 className={styles.cardTitle}>{title}</h3>
      <p className={styles.cardText}>{description}</p>
      <ol className={styles.steps}>
        {steps.map((step) => (
          <li key={step}>{step}</li>
        ))}
      </ol>
      <span className={styles.cardCta}>Start this path</span>
    </Link>
  );
}

export default function Home(): ReactNode {
  return (
    <Layout
      title="Interview preparation"
      description="Senior Engineer and Tech Lead interview preparation knowledge base">
      <header className={styles.hero}>
        <div className="container">
          <h1 className={styles.heroTitle}>Prepare for Senior Engineer and Tech Lead interviews</h1>
          <p className={styles.heroSubtitle}>
            Interview-ready answers, full-stack case studies, and cheatsheets for quick revision.
            Search any concept or pick a learning path.
          </p>
          <div className={styles.search}>
            <SearchBar />
          </div>
          <div className={styles.heroActions}>
            <Link className="button button--primary button--lg" to="/intro/learning-paths">
              Choose a learning path
            </Link>
            <Link className="button button--secondary button--lg" to="/reference">
              Revise with cheatsheets
            </Link>
          </div>
        </div>
      </header>
      <main className="container margin-vert--xl">
        <h2 className={styles.sectionTitle}>Learning paths</h2>
        <div className={styles.grid}>
          {tracks.map((track) => (
            <TrackCard key={track.title} {...track} />
          ))}
        </div>
        <h2 className={styles.sectionTitle}>Quick navigation</h2>
        <ul className={styles.quickLinks}>
          {quickLinks.map((link) => (
            <li key={link.to}>
              <Link to={link.to}>{link.label}</Link>
            </li>
          ))}
        </ul>
      </main>
    </Layout>
  );
}
