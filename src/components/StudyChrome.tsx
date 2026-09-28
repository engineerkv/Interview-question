import {useCallback, useEffect, useState, type ReactNode} from 'react';
import {useLocation} from '@docusaurus/router';
import useBaseUrl from '@docusaurus/useBaseUrl';

function isHomePath(pathname: string, baseUrl: string): boolean {
  const strip = (value: string) => value.replace(/\/+$/, '') || '/';
  return strip(pathname) === strip(baseUrl);
}

export default function StudyChrome(): ReactNode {
  const location = useLocation();
  const baseUrl = useBaseUrl('/');
  const onHome = isHomePath(location.pathname, baseUrl);
  const [progress, setProgress] = useState(0);
  const [showTop, setShowTop] = useState(false);

  const update = useCallback(() => {
    const root = document.documentElement;
    const max = root.scrollHeight - root.clientHeight;
    const next = max > 0 ? Math.min(100, (root.scrollTop / max) * 100) : 0;
    setProgress(next);
    setShowTop(root.scrollTop > 480);
  }, []);

  useEffect(() => {
    update();
    window.addEventListener('scroll', update, {passive: true});
    window.addEventListener('resize', update);
    return () => {
      window.removeEventListener('scroll', update);
      window.removeEventListener('resize', update);
    };
  }, [location.pathname, update]);

  const scrollTop = () => {
    const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    window.scrollTo({top: 0, behavior: reduce ? 'auto' : 'smooth'});
  };

  return (
    <>
      {!onHome && (
        <div
          className="reading-progress"
          role="progressbar"
          aria-hidden="true"
          style={{transform: `scaleX(${progress / 100})`}}
        />
      )}
      <button
        type="button"
        className={`back-to-top${showTop ? ' is-visible' : ''}`}
        aria-label="Back to top"
        onClick={scrollTop}>
        ↑
      </button>
    </>
  );
}
