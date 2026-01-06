# ⚡ 5. Performance & Optimization (Q49–58)

---

## 📍 Navigation

<div align="center">

[← Previous: Architecture & Design Systems](04%29%20Architecture%20%26%20Design%20Systems.md) • [Home: README](../README.md)

[📋 Cheatsheet](CSS%20Interview%20Cheatsheet.md)

</div>

---

---

## Q49. ⚡ Optimizing CSS for performance

CSS performance optimization involves reducing file size, minimizing reflows/repaints, and using efficient selectors to improve rendering performance - selector efficiency and animation performance are key to CSS optimization. Use class selectors over complex descendant selectors, and use `transform` and `opacity` for animations.

- **Trade-offs**: The catch is not minifying CSS or using inefficient selectors - remove whitespace and comments to reduce file size. CSS containment isolates layout and style recalculations, and use `font-display: swap` for fonts.

Example:

```css
.button {
  background: #007bff;
  color: white;
  padding: 8px 16px;
  border: none;
}

```

---

## Q50. 🎨 CSS minification and how to implement it

CSS minification removes unnecessary characters (whitespace, comments) and optimizes code to reduce file size and improve loading performance - minification is standard practice for production builds. Eliminates spaces, tabs, newlines, and removes CSS comments.

- **Trade-offs**: The catch is shortens property values where possible and combines similar selectors - use build tools for automatic minification (Webpack, Vite, etc.). Typically reduces CSS file size by 20-30%.

Example:

```css
.button { background-color: #007bff; color: white; padding: 8px 16px; border: none; }

```

---

## Q51. 🎨 CSS purging and how to implement it

CSS purging removes unused CSS rules from stylesheets, reducing file size and improving performance by eliminating dead code - CSS purging is essential for frameworks like Tailwind CSS. Removes CSS rules that aren't used in HTML/JS, can reduce file size by 50-80%.

- **Trade-offs**: The catch is can be configured to be more or less aggressive (safe mode) - significantly improves loading and parsing performance. Works with Webpack, Vite, and other bundlers.

Example:

```css
.button { background: #007bff; color: white; padding: 8px 16px; }

```

---

## Q52. 🎨 Critical CSS and how to implement it

Critical CSS is the minimal CSS needed to render above-the-fold content - inline it in the HTML head to improve First Contentful Paint, critical CSS improves initial render time. Inline essential styles for above-the-fold content, defer non-critical CSS.

- **Trade-offs**: The catch is not identifying what's truly critical or including too much CSS - use tools to automatically extract critical CSS from your stylesheets. Use `rel="preload"` for non-critical CSS and load after page render.

Example:

```html
<style>
.header { background: #333; color: white; padding: 1rem; }
.hero { padding: 2rem; }
</style>
<link rel="preload" href="styles.css" as="style" onload="this.onload=null;this.rel='stylesheet'">

```

---

## Q53. 🎨 CSS splitting and how to implement it

CSS splitting divides stylesheets into smaller chunks loaded on demand, reducing initial bundle size - split CSS by route or component for better performance. Split CSS by route, component, or feature for on-demand loading.

- **Trade-offs**: The catch is too many small files can increase HTTP requests - balance between file size and number of requests. Reduces initial bundle size and improves First Contentful Paint.

Example:

```html
<link rel="stylesheet" href="base.css">
<link rel="stylesheet" href="components.css">
<link rel="stylesheet" href="pages/home.css">

```

---

## Q54. 🎨 CSS lazy loading and how to implement it

CSS lazy loading defers non-critical CSS until it's needed, improving initial page load performance by loading only essential styles first - lazy loading CSS improves First Contentful Paint. Inline essential styles for above-the-fold content, use `rel="preload"` for non-critical CSS.

- **Trade-offs**: The catch is not providing fallback for JavaScript-disabled users - reduces initial render blocking time significantly. Load non-critical CSS after page load and ensure styles load even with JavaScript disabled.

Example:

```html
<style>.header { background: #333; color: white; padding: 1rem; }</style>
<link rel="preload" href="non-critical.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="non-critical.css"></noscript>

```

---

## Q55. 🎨 CSS preloading and how to implement it

CSS preloading hints the browser to fetch CSS files early, improving perceived performance - use `rel="preload"` for critical CSS that's discovered late. Preload critical CSS that's discovered late in the document.

- **Trade-offs**: The catch is overusing preload can waste bandwidth - use for critical CSS loaded via JavaScript or late in the document. Improves perceived performance by fetching CSS early.

Example:

```html
<link rel="preload" href="critical.css" as="style" onload="this.onload=null;this.rel='stylesheet'">

```

---

## Q56. 🎨 CSS prefetching and how to implement it

CSS prefetching hints the browser to fetch CSS files that might be needed soon, like for the next page - use for likely navigation paths. Prefetch CSS for likely navigation paths or next pages.

- **Trade-offs**: The catch is prefetching too many files wastes bandwidth - use for CSS files that will be needed soon. Improves performance for subsequent page loads.

Example:

```html
<link rel="prefetch" href="next-page.css" as="style">

```

---

## Q57. 🎨 CSS compression and how to implement it

CSS compression reduces file size through various techniques like minification, gzip compression, and Brotli compression to improve loading performance - compression is essential for reducing CSS file size. Minification removes whitespace and comments, gzip reduces file size by ~70%, Brotli by ~80%.

- **Trade-offs**: The catch is not enabling compression on server - modern browsers support both Gzip and Brotli. Enable compression on web server (Apache, Nginx).

Example:

```css
.button { background-color: #007bff; color: white; padding: 8px 16px; border: none; }

```

---

## Q58. ⚡ CSS optimization and how to implement it

CSS optimization combines multiple techniques—minification, purging, splitting, lazy loading, and compression—to improve performance - CSS optimization requires monitoring and continuous improvement. Combine minification, purging, splitting, lazy loading, and compression.

- **Trade-offs**: The catch is not testing optimization impact or over-optimizing - use build tools and performance monitoring for continuous optimization. Monitor performance metrics and identify bottlenecks.

Example:

```css
.button { background: #007bff; color: white; padding: 8px 16px; }

```

---

---

## 📍 Navigation

<div align="center">

[← Previous: Architecture & Design Systems](04%29%20Architecture%20%26%20Design%20Systems.md) • [Home: README](../README.md)

[📋 Cheatsheet](CSS%20Interview%20Cheatsheet.md)

</div>

---
