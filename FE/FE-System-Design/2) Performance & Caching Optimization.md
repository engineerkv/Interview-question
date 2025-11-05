# 2) Performance & Caching Optimization (Q11–27)

---

## 11) What are the Core Web Vitals, and how do you improve them?

Core Web Vitals are key metrics that measure user experience: LCP (Largest Contentful Paint), FID (First Input Delay), and CLS (Cumulative Layout Shift), which directly impact SEO and user satisfaction.

```javascript
import { getCLS, getFID, getLCP } from 'web-vitals';

getCLS(console.log);
getFID(console.log);
getLCP(console.log);

// Optimizing LCP with image preloading
const ImageComponent = ({ src, alt }) => {
  useEffect(() => {
    const link = document.createElement('link');
    link.rel = 'preload';
    link.as = 'image';
    link.href = src;
    document.head.appendChild(link);
  }, [src]);
  return <img src={src} alt={alt} loading="eager" />;
};
```

- **Core Metrics**: LCP measures loading performance (should be < 2.5s), FID measures interactivity (should be < 100ms), CLS measures visual stability (should be < 0.1)
- **Real-World Practice**: Optimize images, fonts, and critical resources
- **Common Tool**: Use performance budgets and monitoring tools
- **Advanced Strategy**: Measure and optimize each metric systematically
- **Interview Tip**: Explain that Core Web Vitals directly affect SEO rankings

---

## 12) How do you implement code splitting and lazy loading with React/Vue?

Code splitting breaks the application into smaller chunks that are loaded on-demand, reducing initial bundle size and improving performance through lazy loading.

```javascript
import { lazy, Suspense } from 'react';

const LazyComponent = lazy(() => import('./HeavyComponent'));

const App = () => (
  <Suspense fallback={<div>Loading...</div>}>
    <LazyComponent />
  </Suspense>
);

// Route-based code splitting
const Home = lazy(() => import('./pages/Home'));
const About = lazy(() => import('./pages/About'));
```

- **Core Technique**: Use route and component-level splitting
- **Real-World Use**: Prefer dynamic import() for better cacheability
- **Common Practice**: Share common chunks; avoid vendor bloat
- **Advanced Tool**: Analyze bundle split with tools (webpack-bundle-analyzer, rollup visualizer)
- **Interview Tip**: Explain that code splitting improves initial load time

---

## 26) What is minification and how do you enable it in modern build tools?

Minification removes unnecessary characters (whitespace, comments), shortens identifiers, and applies safe code transformations to reduce asset size for faster downloads and execution.

```javascript
// Webpack (JS minification via Terser)
module.exports = {
  mode: 'production',
  optimization: {
    minimize: true,
    minimizer: [
      new TerserPlugin({
        terserOptions: {
          compress: { drop_console: true, passes: 2 },
          mangle: true,
          format: { comments: false }
        }
      })
    ]
  }
};

// Vite (uses esbuild for minify by default)
export default defineConfig({
  build: {
    minify: 'esbuild',
    terserOptions: { compress: { drop_console: true } }
  }
});
```

- **Core Purpose**: Minify all text assets: JS, CSS, HTML; combine with compression (gzip/Brotli) for best results
- **Real-World Use**: Prefer source maps in production (hidden) to debug minified code
- **Common Practice**: Safe transforms: dead-code elimination, constant folding, boolean/if simplification
- **Advanced Feature**: Drop debug statements (`console.*`, `debugger`) to shrink bundles
- **Interview Tip**: Explain that measure impact with bundle analyzers and performance budgets

---

## 27) What is code obfuscation and when should you use it?

Code obfuscation transforms code to a functionally equivalent but hard-to-read form to make reverse-engineering more difficult. It differs from minification: minification focuses on size reduction; obfuscation focuses on readability reduction.

```javascript
// obfuscator.json
{
  "compact": true,
  "controlFlowFlattening": true,
  "deadCodeInjection": true,
  "stringArray": true,
  "stringArrayEncoding": ["rc4"],
  "renameGlobals": true,
  "disableConsoleOutput": true
}
```

- **Core Purpose**: Obfuscation ≠ Security: It's defense-in-depth, not a replacement for proper security
- **Real-World Trade-offs**: Larger bundles, slower runtime, harder debugging, potential compatibility issues
- **Common Use**: Consider obfuscating only sensitive modules (license checks, proprietary algorithms) rather than full app
- **Important Rule**: Do not ship public readable maps for obfuscated bundles; keep private maps securely
- **Interview Tip**: Explain that for strong protection, rely on server-side enforcement, licensing, watermarking

---
