# ⚡ 7. Performance & SEO (Q86–101)

---

## 🧩 Q86. How do you optimize HTML for performance?

### 🧠 Concept

Optimize HTML structure, reduce file size, minimize render-blocking resources, and use efficient loading strategies. HTML optimization reduces initial load time and improves Core Web Vitals.

---

### 💡 Example

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="preload" href="critical.css" as="style">
</head>
<body><!-- Content --></body>
</html>
```

---

### 🔍 Deep Insights

* **Rule:** Minimize HTML file size, inline critical CSS, defer non-critical resources.
* **Use Case:** Use lazy loading for images, optimize resource loading order.
* **Common Mistake:** Loading all resources at once, blocking initial render.
* **Pro Tip:** Use preload for critical resources, minify HTML.

---

### ⭐ Senior Takeaway

HTML optimization reduces initial load time and improves Core Web Vitals.

---

## 🧩 Q87. What is the Critical Rendering Path?

### 🧠 Concept

The critical rendering path is the sequence of steps browsers take to render a page, from HTML parsing to pixel painting. Optimizing the critical path improves First Contentful Paint.

---

### 💡 Example

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="critical.css">
  <script src="deferred.js" defer></script>
</head>
<body><!-- Content --></body>
</html>
```

---

### 🔍 Deep Insights

* **Rule:** HTML → CSS → JavaScript → Layout → Paint.
* **Use Case:** Render-blocking resources delay rendering, critical path determines initial render time.
* **Common Mistake:** Loading all CSS and JavaScript synchronously.
* **Pro Tip:** Use async/defer for non-critical scripts, inline critical CSS.

---

### ⭐ Senior Takeaway

Optimizing the critical path improves First Contentful Paint.

---

## 🧩 Q88. How do you implement lazy loading?

### 🧠 Concept

Lazy loading defers image loading until they're needed, improving initial page load performance. Lazy loading is essential for pages with many images.

---

### 💡 Example

```html
<img src="image.jpg" loading="lazy" alt="Description">
<img data-src="image.jpg" class="lazy" alt="Description">
<script>
document.querySelectorAll('.lazy').forEach(img => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => { 
      if (entry.isIntersecting) { 
        img.src = img.dataset.src; 
        observer.unobserve(img); 
      } 
    });
  });
  observer.observe(img);
});
</script>
```

---

### 🔍 Deep Insights

* **Rule:** `loading="lazy"` provides native lazy loading, JavaScript solution offers more control.
* **Use Case:** Improves initial page load time, reduces bandwidth usage.
* **Common Mistake:** Lazy loading above-fold images (should be eager).
* **Pro Tip:** Use Intersection Observer for better performance than scroll listeners.

---

### ⭐ Senior Takeaway

Lazy loading is essential for pages with many images.

---

## 🧩 Q89. How do you minify HTML?

### 🧠 Concept

Minify HTML by removing whitespace, comments, and unnecessary characters while preserving functionality. Minification is standard practice for production builds.

---

### 💡 Example

```html
<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Page Title</title></head><body><!-- Content --></body></html>
```

---

### 🔍 Deep Insights

* **Rule:** Removes unnecessary whitespace and comments, reduces file size by 20-30%.
* **Use Case:** Use build tools for automatic minification (Webpack, Gulp, etc.).
* **Common Mistake:** Not testing functionality after minification, breaking inline JavaScript.
* **Pro Tip:** Be careful with inline CSS and JavaScript, preserve required whitespace.

---

### ⭐ Senior Takeaway

Minification is standard practice for production builds.

---

## 🧩 Q90. How do you optimize for mobile?

### 🧠 Concept

Optimize HTML for mobile by using responsive design, touch-friendly elements, and mobile-specific optimizations. Mobile optimization is essential for modern web development.

---

### 💡 Example

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mobile Optimized Page</title>
</head>
<body>
  <button style="min-width: 44px; min-height: 44px;">Touch Target</button>
  <img src="mobile-image.jpg" alt="Mobile image" 
       srcset="mobile-320w.jpg 320w, mobile-640w.jpg 640w" 
       sizes="100vw">
</body>
</html>
```

---

### 🔍 Deep Insights

* **Rule:** Use proper viewport meta tag, make touch targets at least 44px.
* **Use Case:** Optimize images for mobile screens, use appropriate input types.
* **Common Mistake:** Not setting viewport meta tag, causing zoom issues.
* **Pro Tip:** Consider mobile-specific features, use responsive images.

---

### ⭐ Senior Takeaway

Mobile optimization is essential for modern web development.

---

## 🧩 Q91. How do you structure HTML for SEO?

### 🧠 Concept

Proper HTML structure helps search engines understand content hierarchy and importance, improving search rankings. HTML structure is fundamental for SEO, not just styling.

---

### 💡 Example

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Best Practices for HTML SEO</title>
  <meta name="description" content="Learn how to optimize HTML for search engines">
</head>
<body>
  <header>
    <h1>SEO Best Practices</h1>
  </header>
  <main>
    <article>
      <h2>Introduction</h2>
      <p>Content...</p>
    </article>
  </main>
</body>
</html>
```

---

### 🔍 Deep Insights

* **Rule:** Use semantic HTML elements, create clear heading hierarchy (h1 → h2 → h3).
* **Use Case:** Only one h1 per page, use descriptive alt text for images.
* **Common Mistake:** Skipping heading levels, using multiple h1 tags.
* **Pro Tip:** Structure content logically, use semantic elements for better SEO.

---

### ⭐ Senior Takeaway

HTML structure is fundamental for SEO, not just styling.

---

## 🧩 Q92. What are meta tags and how do you use them?

### 🧠 Concept

Meta tags provide information about the page to search engines and social media platforms. Meta tags are essential for SEO and social sharing.

---

### 💡 Example

```html
<head>
  <title>Page Title - Company Name</title>
  <meta name="description" content="Brief description of page content (150-160 characters)">
  <meta name="keywords" content="keyword1, keyword2, keyword3">
  <link rel="canonical" href="https://example.com/page">
</head>
```

---

### 🔍 Deep Insights

* **Rule:** Title should be 50-60 characters, description should be 150-160 characters.
* **Use Case:** Use Open Graph for social sharing, canonical URL prevents duplicate content.
* **Common Mistake:** Keywords meta tag has limited SEO value (don't overuse).
* **Pro Tip:** Use descriptive, keyword-rich titles and descriptions.

---

### ⭐ Senior Takeaway

Meta tags are essential for SEO and social sharing.

---

## 🧩 Q93. How do you implement structured data?

### 🧠 Concept

Structured data uses schema.org markup to help search engines understand content and display rich snippets. Structured data improves search result visibility.

---

### 💡 Example

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How to Optimize HTML for SEO",
  "description": "Complete guide to HTML SEO optimization",
  "author": { "@type": "Person", "name": "John Doe" },
  "datePublished": "2025-01-15"
}
</script>
```

---

### 🔍 Deep Insights

* **Rule:** Helps search engines understand content, can result in rich snippets in search results.
* **Use Case:** Use JSON-LD for easier implementation, test with Google's Rich Results Test.
* **Common Mistake:** Not following schema.org guidelines, incorrect markup.
* **Pro Tip:** Follow schema.org guidelines, validate with Google's testing tools.

---

### ⭐ Senior Takeaway

Structured data improves search result visibility.

---

## 🧩 Q94. What are Core Web Vitals?

### 🧠 Concept

Core Web Vitals measure user experience metrics that impact SEO rankings: LCP, FID, and CLS. Core Web Vitals directly impact search rankings.

---

### 💡 Example

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <link rel="preload" href="lcp-image.jpg" as="image" fetchpriority="high">
  <link rel="preload" href="critical.css" as="style">
</head>
<body>
  <img src="lcp-image.jpg" fetchpriority="high" width="800" height="600" alt="LCP image">
  <script defer src="non-critical.js"></script>
</body>
</html>
```

---

### 🔍 Deep Insights

* **Rule:** LCP (optimize largest contentful paint), FID (minimize JavaScript execution), CLS (prevent layout shifts).
* **Use Case:** Use preload for critical resources, specify image dimensions.
* **Common Mistake:** Not specifying image dimensions, causing layout shifts.
* **Pro Tip:** Optimize LCP element, minimize render-blocking resources.

---

### ⭐ Senior Takeaway

Core Web Vitals directly impact search rankings.

---

## 🧩 Q95. How do you implement caching?

### 🧠 Concept

Implement proper caching strategies using HTTP headers and HTML meta tags to improve performance. Caching improves performance but requires proper invalidation strategy.

---

### 💡 Example

```html
<meta http-equiv="Cache-Control" content="public, max-age=31536000">
<meta http-equiv="Expires" content="Wed, 21 Oct 2025 07:28:00 GMT">
```

---

### 🔍 Deep Insights

* **Rule:** Use versioning for static resources, set appropriate cache headers server-side.
* **Use Case:** Separate static and dynamic content, use ETags for cache validation.
* **Common Mistake:** HTML meta tags have limited support (use HTTP headers instead).
* **Pro Tip:** Consider CDN for global caching, use proper cache headers.

---

### ⭐ Senior Takeaway

Caching improves performance but requires proper invalidation strategy.

---

## 🧩 Q96. What are resource hints and how do you use them to optimize page performance?

### 🧠 Concept

Resource hints instruct the browser to perform actions ahead of time to improve loading performance. Resource hints improve perceived performance by doing work early.

---

### 💡 Example

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="dns-prefetch" href="https://api.example.com">
<link rel="preload" href="/lcp-image.jpg" as="image" 
      imagesrcset="image-320w.jpg 320w, image-640w.jpg 640w">
<link rel="prefetch" href="/next-page.css" as="style">
```

---

### 🔍 Deep Insights

* **Rule:** preconnect (opens connection), dns-prefetch (DNS lookup), preload (critical resources), prefetch (future pages).
* **Use Case:** Use preconnect for critical cross-origin resources like Google Fonts.
* **Common Mistake:** Overusing preconnect (limit to 2-4 per page), forgetting crossorigin for CORS resources.
* **Pro Tip:** Use preload for late-discovered critical resources, prefetch for likely navigation.

---

### ⭐ Senior Takeaway

Resource hints improve perceived performance by doing work early.

---

## 🧩 Q97. What is fetchpriority and how do you use it to optimize resource loading?

### 🧠 Concept

`fetchpriority` is an HTML attribute that controls the relative priority of resource fetches, helping browsers prioritize critical resources. fetchpriority is modern browser feature for resource prioritization.

---

### 💡 Example

```html
<img src="/hero-image.jpg" fetchpriority="high" alt="Hero image" loading="eager">
<img src="/thumb1.jpg" fetchpriority="low" alt="Thumbnail 1" loading="lazy">
<link rel="stylesheet" href="/critical.css" fetchpriority="high">
<script src="/analytics.js" fetchpriority="low" defer></script>
```

---

### 🔍 Deep Insights

* **Rule:** `high` for LCP images and critical CSS/JS, `low` for below-the-fold content.
* **Use Case:** Especially important for LCP optimization, can improve Core Web Vitals significantly.
* **Common Mistake:** Overusing `high` priority (typically 1-2 per page), not using it for LCP images.
* **Pro Tip:** Use `high` for critical resources, `low` for non-critical resources.

---

### ⭐ Senior Takeaway

fetchpriority is modern browser feature for resource prioritization.

---

## 🧩 Q98. What is SEO and how can you optimize it?

### 🧠 Concept

SEO is the practice of improving website visibility in search engine results through on-page, technical, and off-page optimizations. SEO is ongoing process requiring technical and content optimization.

---

### 💡 Example

```html
<head>
  <title>Best Practices for Frontend SEO | Complete Guide 2025</title>
  <meta name="description" content="Learn how to optimize your frontend for search engines.">
  <link rel="canonical" href="https://example.com/seo-guide">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "Best Practices for Frontend SEO",
    "author": { "@type": "Person", "name": "Your Name" }
  }
  </script>
</head>
<body>
  <header>
    <h1>Best Practices for Frontend SEO</h1>
  </header>
  <main>
    <article>
      <h2>On-Page SEO</h2>
      <p>Content...</p>
    </article>
  </main>
</body>
```

---

### 🔍 Deep Insights

* **Rule:** On-page (title tags, meta descriptions, headings), technical (Core Web Vitals, structured data), off-page (backlinks).
* **Use Case:** Core Web Vitals directly impact search rankings, mobile-first indexing is essential.
* **Common Mistake:** Keyword stuffing, ignoring Core Web Vitals, not using structured data.
* **Pro Tip:** Use semantic HTML, implement schema.org markup, optimize performance.

---

### ⭐ Senior Takeaway

SEO is ongoing process requiring technical and content optimization.

---

## 🧩 Q99. What is sitemap.xml and how do you create it?

### 🧠 Concept

A sitemap.xml is an XML file that lists all pages on a website, helping search engines discover and index content efficiently. Sitemaps are essential for large sites with many pages.

---

### 💡 Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://example.com/</loc>
    <lastmod>2025-01-20</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>
```

---

### 🔍 Deep Insights

* **Rule:** Helps search engines discover all pages, especially deep pages not linked internally.
* **Use Case:** Place at root (`/sitemap.xml`), reference in robots.txt, submit via Google Search Console.
* **Common Mistake:** Not updating sitemap when content changes, exceeding size limits (50,000 URLs, 50MB).
* **Pro Tip:** Use sitemap index for large sites, include lastmod dates, compress large sitemaps.

---

### ⭐ Senior Takeaway

Sitemaps are essential for large sites with many pages.

---

## 🧩 Q100. What is robots.txt and how do you use it?

### 🧠 Concept

robots.txt is a text file in the root directory that instructs web crawlers which pages or directories they can or cannot access. robots.txt is a guideline, not security (bad bots may ignore it).

---

### 💡 Example

```txt
User-agent: *
Allow: /
Disallow: /admin/
Disallow: /api/
Sitemap: https://example.com/sitemap.xml
```

---

### 🔍 Deep Insights

* **Rule:** Control crawler access, prevent crawling of sensitive or duplicate content.
* **Use Case:** Block `/admin/`, `/api/`, query strings, prevent duplicate content indexing.
* **Common Mistake:** Using robots.txt for security (it's publicly accessible), not testing syntax.
* **Pro Tip:** Use specific rules for different bots, reference sitemap location.

---

### ⭐ Senior Takeaway

robots.txt is a guideline, not security (bad bots may ignore it).

---

## 🧩 Q101. What are Open Graph tags and how do you use them?

### 🧠 Concept

Open Graph tags are HTML meta tags that control how content appears when shared on social media platforms. Open Graph tags improve social sharing appearance and engagement.

---

### 💡 Example

```html
<head>
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://example.com/seo-guide">
  <meta property="og:title" content="Best Practices for Frontend SEO">
  <meta property="og:description" content="Complete guide to frontend SEO optimization">
  <meta property="og:image" content="https://example.com/seo-preview.jpg">
</head>
```

---

### 🔍 Deep Insights

* **Rule:** Control how links appear when shared on social platforms, creates rich previews.
* **Use Case:** Required tags: og:title, og:type, og:image, og:url (also og:description recommended).
* **Common Mistake:** Not using absolute URLs for images, incorrect image dimensions (recommended 1200x630px).
* **Pro Tip:** Use Twitter Card tags alongside OG tags, test with platform debugger tools.

---

### ⭐ Senior Takeaway

Open Graph tags improve social sharing appearance and engagement.

---
