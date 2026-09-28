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
    title: 'Interface Engineering',
    description: 'HTML, CSS, React, Next.js, and how the browser actually renders — so you can explain it, not just use it.',
    to: '/frontend',
    steps: ['HTML & CSS', 'JavaScript & TypeScript', 'React & Next.js', 'Architecture deep dives'],
  },
  {
    title: 'Design Rounds',
    description: 'Timed full-stack designs. Capacity, failure, and trade-offs you can defend in 45 minutes.',
    to: '/case-studies',
    steps: ['Service architecture', 'Messaging & storage', 'Walk a case', 'Scale with AI'],
  },
  {
    title: 'Production Engineering',
    description: 'The path from a merged PR to a healthy system: containers, Kubernetes, SLOs, and recovery.',
    to: '/devops',
    steps: ['Containers', 'Kubernetes', 'CI/CD & releases', 'SLOs & incidents'],
  },
  {
    title: 'Applied AI',
    description: 'LLMs, RAG, evals, and AI in the delivery loop — without shipping fiction.',
    to: '/ai',
    steps: ['LLM fundamentals', 'RAG & retrieval', 'Evaluation & safety', 'AI-assisted SDLC'],
  },
  {
    title: 'Agent Systems',
    description: 'When an agent is the right tool, how to wire it, and where humans stay in the loop.',
    to: '/agentic-workflows',
    steps: ['Agents vs workflows', 'Tools & MCP', 'Orchestration', 'Human-in-the-loop'],
  },
  {
    title: 'Staff Craft',
    description: 'Reviews, decisions, mentoring, and STAR stories for Tech Lead loops.',
    to: '/leadership',
    steps: ['Code reviews', 'Technical leadership', 'Behavioral (STAR)', 'Automated review'],
  },
];

const quickLinks = [
  {label: 'Language Core: DSA', to: '/fundamentals/dsa'},
  {label: 'Service Engineering: Node', to: '/backend/node-express/question-index'},
  {label: 'Service Engineering: Python', to: '/backend/python'},
  {label: 'Celery workers', to: '/backend/celery'},
  {label: 'RabbitMQ', to: '/backend/rabbitmq'},
  {label: 'MinIO object storage', to: '/backend/minio'},
  {label: 'Pocket Cards', to: '/reference'},
  {label: 'Automated review', to: '/leadership/code-reviews/automated-review-process'},
];

const loop = [
  {n: '01', title: 'Pick a path', text: 'Stay on one track until you can teach it.'},
  {n: '02', title: 'Read the short answer', text: 'Say it out loud before you open notes.'},
  {n: '03', title: 'Walk one example', text: 'Trace a real case, not a definition.'},
  {n: '04', title: 'Drill follow-ups', text: 'Two questions deeper, then mark the cheatsheet.'},
];

function TrackCard({title, description, to, steps, index}: Track & {index: number}) {
  return (
    <Link
      to={to}
      className={styles.card}
      style={{animationDelay: `${120 + index * 70}ms`}}>
      <span className={styles.cardIndex}>{String(index + 1).padStart(2, '0')}</span>
      <h3 className={styles.cardTitle}>{title}</h3>
      <p className={styles.cardText}>{description}</p>
      <ol className={styles.steps}>
        {steps.map((step, stepIndex) => (
          <li key={step}>
            <span className={styles.stepMark}>{stepIndex + 1}</span>
            {step}
          </li>
        ))}
      </ol>
      <span className={styles.cardCta}>
        Open this shelf
        <span className={styles.arrow} aria-hidden="true">
          →
        </span>
      </span>
    </Link>
  );
}

export default function Home(): ReactNode {
  return (
    <Layout
      title="Spoken answers for interview rounds"
      description="Roundbook is a quiet study book for Senior Engineer and Tech Lead interviews: drills, design rounds, and pocket cards.">
      <header className={styles.hero}>
        <div className={`container ${styles.heroInner}`}>
          <p className={styles.kicker}>Roundbook</p>
          <h1 className={styles.heroTitle}>Answers you can say out loud</h1>
          <p className={styles.heroSubtitle}>
            A Senior Engineer and Tech Lead study book: drills, design rounds, and pocket cards,
            written for long reading. Search a concept, or settle into one path.
          </p>
          <div className={styles.search}>
            <SearchBar />
          </div>
          <div className={styles.heroActions}>
            <Link className="button button--primary button--lg" to="/intro/learning-paths">
              Open the paths
            </Link>
            <Link className="button button--secondary button--lg" to="/reference">
              Open pocket cards
            </Link>
          </div>
        </div>
      </header>
      <main className={`container margin-vert--lg ${styles.section}`}>
        <h2 className={styles.sectionTitle}>The study loop</h2>
        <p className={styles.sectionLead}>
          Hover a step to preview it. Use the loop as a 30-minute drill or a 90-minute design round.
        </p>
        <ol className={styles.loop}>
          {loop.map((item) => (
            <li key={item.n} className={styles.loopItem} tabIndex={0}>
              <span className={styles.loopN}>{item.n}</span>
              <strong>{item.title}</strong>
              <p>{item.text}</p>
            </li>
          ))}
        </ol>
        <h2 className={styles.sectionTitle}>The library</h2>
        <p className={styles.sectionLead}>
          Pick one shelf and stay with it until you can teach it. Each path is ordered: read, drill, revise.
        </p>
        <div className={styles.grid}>
          {tracks.map((track, index) => (
            <TrackCard key={track.title} {...track} index={index} />
          ))}
        </div>
        <h2 className={styles.sectionTitle}>Jump in</h2>
        <p className={styles.sectionLead}>Go straight to a shelf you already know you need.</p>
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
