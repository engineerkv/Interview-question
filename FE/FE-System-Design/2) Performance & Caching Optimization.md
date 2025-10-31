# 2) Performance & Caching Optimization (Q11–27)

## 11) What are the Core Web Vitals, and how do you improve them?

Concept: Core Web Vitals are key metrics that measure user experience: LCP (Largest Contentful Paint), FID (First Input Delay), and CLS (Cumulative Layout Shift), which directly impact SEO and user satisfaction.

Example:
```javascript
// Measuring Core Web Vitals
import { getCLS, getFID, getFCP, getLCP, getTTFB } from 'web-vitals';

getCLS(console.log);
getFID(console.log);
getFCP(console.log);
getLCP(console.log);
getTTFB(console.log);

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

Deep Insight:
- LCP measures loading performance (should be < 2.5s)
- FID measures interactivity (should be < 100ms)
- CLS measures visual stability (should be < 0.1)
- Optimize images, fonts, and critical resources
- Use performance budgets and monitoring tools

## 12) How do you implement code splitting and lazy loading with React/Vue?

Concept: Code splitting breaks the application into smaller chunks that are loaded on-demand, reducing initial bundle size and improving performance through lazy loading.

Example:
```javascript
// React lazy loading with Suspense
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

const App = () => (
  <Routes>
    <Route path="/" element={<Home />} />
    <Route path="/about" element={<About />} />
  </Routes>
);
```

Deep Insight:
- Use route and component-level splitting
- Prefer dynamic import() for better cacheability
- Share common chunks; avoid vendor bloat
- Analyze bundle split with tools (webpack-bundle-analyzer, rollup visualizer)

---

## 26) What is minification and how do you enable it in modern build tools?

Concept:
Minification removes unnecessary characters (whitespace, comments), shortens identifiers, and applies safe code transformations to reduce asset size for faster downloads and execution. It typically targets JavaScript, CSS, and HTML during production builds.

Example:
```js
// Webpack (JS minification via Terser)
// webpack.config.js
const TerserPlugin = require('terser-webpack-plugin');

module.exports = {
  mode: 'production', // enables minification by default
  optimization: {
    minimize: true,
    minimizer: [
      new TerserPlugin({
        terserOptions: {
          compress: {
            drop_console: true,
            passes: 2,
          },
          mangle: true,
          format: { comments: false },
        },
        extractComments: false,
      }),
    ],
  },
};

// Rollup (JS minification via terser)
// rollup.config.mjs
import terser from '@rollup/plugin-terser';

export default {
  input: 'src/index.js',
  output: [{ file: 'dist/index.min.js', format: 'esm', sourcemap: true }],
  plugins: [terser({ compress: { passes: 2 }, mangle: true })],
};

// esbuild (built-in super-fast minify)
// build.mjs
import esbuild from 'esbuild';

await esbuild.build({
  entryPoints: ['src/index.tsx'],
  bundle: true,
  minify: true, // enable minification
  sourcemap: true,
  outdir: 'dist',
  target: ['es2018'],
});

// Vite (uses esbuild for minify by default)
// vite.config.ts
import { defineConfig } from 'vite';

export default defineConfig({
  build: {
    minify: 'esbuild', // or 'terser' for advanced options
    terserOptions: {
      compress: { drop_console: true },
    },
  },
});

// CSS minification (PostCSS + cssnano)
// postcss.config.js
module.exports = {
  plugins: [
    require('autoprefixer'),
    require('cssnano')({ preset: 'default' }), // minify CSS
  ],
};

// HTML minification (html-minifier-terser)
// build-html.mjs
import { minify } from 'html-minifier-terser';
import fs from 'node:fs/promises';

const html = await fs.readFile('index.html', 'utf8');
const minimized = await minify(html, {
  collapseWhitespace: true,
  removeComments: true,
  minifyCSS: true,
  minifyJS: true,
});
await fs.writeFile('dist/index.html', minimized);
```

Deep Insight:
- Minify all text assets: JS, CSS, HTML; combine with compression (gzip/Brotli) for best results
- Prefer source maps in production (hidden) to debug minified code: `devtool: 'source-map'` or `build.sourcemap: true`
- Safe transforms: dead-code elimination, constant folding, boolean/if simplification; beware of side effects and `pure` annotations
- Drop debug statements (`console.*`, `debugger`) to shrink bundles and reduce runtime overhead
- Tree-shaking works on ESM; ensure libraries export ESM to maximize dead-code removal
- For libraries, ship multiple outputs (ESM, CJS, minified) with accurate `package.json` `exports`
- Measure impact with bundle analyzers and performance budgets; iterate with profiling (Lighthouse, Web Vitals)

---

## 27) What is code obfuscation and when should you use it?

Concept:
Code obfuscation transforms code to a functionally equivalent but hard-to-read form to make reverse-engineering more difficult. It differs from minification: minification focuses on size reduction; obfuscation focuses on readability reduction (IP protection, slowing attackers), often at the cost of debuggability and sometimes performance.

Example:
```bash
# JavaScript obfuscation (javascript-obfuscator)
# CLI
npx javascript-obfuscator dist --config obfuscator.json --output dist-obf
```
```json
// obfuscator.json
{
  "compact": true,
  "controlFlowFlattening": true,
  "deadCodeInjection": true,
  "stringArray": true,
  "stringArrayEncoding": ["rc4"],
  "renameGlobals": true,
  "selfDefending": false,
  "disableConsoleOutput": true,
  "transformObjectKeys": true
}
```
```js
// Webpack plugin (not recommended for general apps; consider targeted)
// webpack.config.js
const JavaScriptObfuscator = require('webpack-obfuscator');

module.exports = {
  // ...
  plugins: [
    new JavaScriptObfuscator({
      rotateStringArray: true,
      controlFlowFlattening: true,
      stringArrayThreshold: 0.75,
    }, [
      // Exclude vendor/runtime chunks to reduce risk
      'vendor.*.js', 'runtime.*.js'
    ])
  ]
};

// Source maps precaution (never publish readable maps publicly)
// For minified (not obfuscated) builds, prefer hidden source maps on server
```

Deep Insight:
- Obfuscation ≠ Security: It’s defense-in-depth, not a replacement for proper security; never store secrets/keys in client code
- Trade-offs: Larger bundles, slower runtime, harder debugging, potential compatibility issues
- Targeted Usage: Consider obfuscating only sensitive modules (license checks, proprietary algorithms) rather than full app
- Source Maps: Do not ship public readable maps for obfuscated bundles; keep private maps securely for internal debugging
- Legal/IP: Obfuscation can deter casual copying; for strong protection, rely on server-side enforcement, licensing, watermarking
- Performance: Some obfuscation options (control flow flattening, string encoding) can degrade performance—measure impact
- DX: Document build steps and provide a non-obfuscated debug build for support teams
