# ⚡ 5. Performance & Optimization (Q51–60)

---

## 🧩 Q51. How do you optimize CSS for performance?

### 🧠 Concept

CSS performance optimization involves reducing file size, minimizing reflows/repaints, and using efficient selectors to improve rendering performance. Selector efficiency and animation performance are key to CSS optimization.

---

### 💡 Example

```css
.button { 
  background: #007bff; 
  color: white; 
  padding: 8px 16px; 
  border: none; 
}
```

---

### 🔍 Deep Insights

* **Rule:** Use class selectors over complex descendant selectors, use `transform` and `opacity` for animations.
* **Use Case:** CSS containment isolates layout and style recalculations, use `font-display: swap` for fonts.
* **Common Mistake:** Not minifying CSS, using inefficient selectors.
* **Pro Tip:** Remove whitespace and comments to reduce file size.

---

### ⭐ Senior Takeaway

Selector efficiency and animation performance are key to CSS optimization.

---

## 🧩 Q52. What is CSS minification and how do you implement it?

### 🧠 Concept

CSS minification removes unnecessary characters (whitespace, comments) and optimizes code to reduce file size and improve loading performance. Minification is standard practice for production builds.

---

### 💡 Example

```css
.button { background-color: #007bff; color: white; padding: 8px 16px; border: none; }
```

---

### 🔍 Deep Insights

* **Rule:** Eliminates spaces, tabs, newlines, removes CSS comments.
* **Use Case:** Typically reduces CSS file size by 20-30%.
* **Common Mistake:** Shortens property values where possible, combines similar selectors.
* **Pro Tip:** Use build tools for automatic minification (Webpack, Vite, etc.).

---

### ⭐ Senior Takeaway

Minification is standard practice for production builds.

---

## 🧩 Q53. What is CSS purging and how do you implement it?

### 🧠 Concept

CSS purging removes unused CSS rules from stylesheets, reducing file size and improving performance by eliminating dead code. CSS purging is essential for frameworks like Tailwind CSS.

---

### 💡 Example

```css
.button { background: #007bff; color: white; padding: 8px 16px; }
```

---

### 🔍 Deep Insights

* **Rule:** Removes CSS rules that aren't used in HTML/JS, can reduce file size by 50-80%.
* **Use Case:** Works with Webpack, Vite, and other bundlers.
* **Common Mistake:** Can be configured to be more or less aggressive (safe mode).
* **Pro Tip:** Significantly improves loading and parsing performance.

---

### ⭐ Senior Takeaway

CSS purging is essential for frameworks like Tailwind CSS.

---

## 🧩 Q54. What is critical CSS and how do you implement it?

### 🧠 Concept

Critical CSS is the minimal CSS needed to render above-the-fold content. Inline it in the HTML head to improve First Contentful Paint. Critical CSS improves initial render time.

---

### 💡 Example

```html
<style>
.header { background: #333; color: white; padding: 1rem; }
.hero { padding: 2rem; }
</style>
<link rel="preload" href="styles.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
```

---

### 🔍 Deep Insights

* **Rule:** Inline essential styles for above-the-fold content, defer non-critical CSS.
* **Use Case:** Use `rel="preload"` for non-critical CSS, load after page render.
* **Common Mistake:** Not identifying what's truly critical, including too much CSS.
* **Pro Tip:** Use tools to automatically extract critical CSS from your stylesheets.

---

### ⭐ Senior Takeaway

Critical CSS improves initial render time.

---

## 🧩 Q55. What is CSS splitting and how do you implement it?

### 🧠 Concept

CSS splitting divides stylesheets into smaller chunks loaded on demand, reducing initial bundle size. Split CSS by route or component for better performance.

---

### 💡 Example

```html
<link rel="stylesheet" href="base.css">
<link rel="stylesheet" href="components.css">
<link rel="stylesheet" href="pages/home.css">
```

---

### 🔍 Deep Insights

* **Rule:** Split CSS by route, component, or feature for on-demand loading.
* **Use Case:** Reduces initial bundle size, improves First Contentful Paint.
* **Common Mistake:** Too many small files can increase HTTP requests.
* **Pro Tip:** Balance between file size and number of requests.

---

### ⭐ Senior Takeaway

CSS splitting reduces initial bundle size and improves performance.

---

## 🧩 Q56. What is CSS lazy loading and how do you implement it?

### 🧠 Concept

CSS lazy loading defers non-critical CSS until it's needed, improving initial page load performance by loading only essential styles first. Lazy loading CSS improves First Contentful Paint.

---

### 💡 Example

```html
<style>.header { background: #333; color: white; padding: 1rem; }</style>
<link rel="preload" href="non-critical.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="non-critical.css"></noscript>
```

---

### 🔍 Deep Insights

* **Rule:** Inline essential styles for above-the-fold content, use `rel="preload"` for non-critical CSS.
* **Use Case:** Load non-critical CSS after page load, ensure styles load even with JavaScript disabled.
* **Common Mistake:** Not providing fallback for JavaScript-disabled users.
* **Pro Tip:** Reduces initial render blocking time significantly.

---

### ⭐ Senior Takeaway

Lazy loading CSS improves First Contentful Paint.

---

## 🧩 Q57. What is CSS preloading and how do you implement it?

### 🧠 Concept

CSS preloading hints the browser to fetch CSS files early, improving perceived performance. Use `rel="preload"` for critical CSS that's discovered late.

---

### 💡 Example

```html
<link rel="preload" href="critical.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
```

---

### 🔍 Deep Insights

* **Rule:** Preload critical CSS that's discovered late in the document.
* **Use Case:** Improves perceived performance by fetching CSS early.
* **Common Mistake:** Overusing preload can waste bandwidth.
* **Pro Tip:** Use for critical CSS loaded via JavaScript or late in the document.

---

### ⭐ Senior Takeaway

CSS preloading improves perceived performance for critical styles.

---

## 🧩 Q58. What is CSS prefetching and how do you implement it?

### 🧠 Concept

CSS prefetching hints the browser to fetch CSS files that might be needed soon, like for the next page. Use for likely navigation paths.

---

### 💡 Example

```html
<link rel="prefetch" href="next-page.css" as="style">
```

---

### 🔍 Deep Insights

* **Rule:** Prefetch CSS for likely navigation paths or next pages.
* **Use Case:** Improves performance for subsequent page loads.
* **Common Mistake:** Prefetching too many files wastes bandwidth.
* **Pro Tip:** Use for CSS files that will be needed soon.

---

### ⭐ Senior Takeaway

CSS prefetching improves performance for subsequent page loads.

---

## 🧩 Q59. What is CSS compression and how do you implement it?

### 🧠 Concept

CSS compression reduces file size through various techniques like minification, gzip compression, and Brotli compression to improve loading performance. Compression is essential for reducing CSS file size.

---

### 💡 Example

```css
.button { background-color: #007bff; color: white; padding: 8px 16px; border: none; }
```

---

### 🔍 Deep Insights

* **Rule:** Minification removes whitespace and comments, gzip reduces file size by ~70%, Brotli by ~80%.
* **Use Case:** Enable compression on web server (Apache, Nginx).
* **Common Mistake:** Not enabling compression on server.
* **Pro Tip:** Modern browsers support both Gzip and Brotli.

---

### ⭐ Senior Takeaway

Compression is essential for reducing CSS file size.

---

## 🧩 Q60. What is CSS optimization and how do you implement it?

### 🧠 Concept

CSS optimization combines multiple techniques—minification, purging, splitting, lazy loading, and compression—to improve performance. CSS optimization requires monitoring and continuous improvement.

---

### 💡 Example

```css
.button { background: #007bff; color: white; padding: 8px 16px; }
```

---

### 🔍 Deep Insights

* **Rule:** Combine minification, purging, splitting, lazy loading, and compression.
* **Use Case:** Monitor performance metrics, identify bottlenecks.
* **Common Mistake:** Not testing optimization impact, over-optimizing.
* **Pro Tip:** Use build tools and performance monitoring for continuous optimization.

---

### ⭐ Senior Takeaway

CSS optimization requires monitoring and continuous improvement.

---
