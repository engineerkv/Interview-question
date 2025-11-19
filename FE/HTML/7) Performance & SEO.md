# 7. Performance & SEO (Q86–101)

---

## Q86. How do you optimize HTML for performance?

Optimize HTML structure, reduce file size, minimize render-blocking resources, and use efficient loading strategies - HTML optimization reduces initial load time and improves Core Web Vitals. Minimize HTML file size, inline critical CSS, defer non-critical resources.

- **Trade-offs**: The catch is loading all resources at once, blocking initial render - use preload for critical resources, minify HTML. HTML optimization reduces initial load time and improves Core Web Vitals, but watch out - use lazy loading for images, optimize resource loading order.

Example:

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

## Q87. What is the Critical Rendering Path?

The critical rendering path is the sequence of steps browsers take to render a page, from HTML parsing to pixel painting - optimizing the critical path improves First Contentful Paint. HTML → CSS → JavaScript → Layout → Paint.

- **Trade-offs**: The catch is loading all CSS and JavaScript synchronously - use async/defer for non-critical scripts, inline critical CSS. Optimizing the critical path improves First Contentful Paint, but watch out - render-blocking resources delay rendering, critical path determines initial render time.

Example:

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

## Q88. How do you implement lazy loading?

Lazy loading defers image loading until they're needed, improving initial page load performance - lazy loading is essential for pages with many images. `loading="lazy"` provides native lazy loading, JavaScript solution offers more control.

- **Trade-offs**: The catch is lazy loading above-fold images (should be eager) - use Intersection Observer for better performance than scroll listeners. Lazy loading is essential for pages with many images, but watch out - improves initial page load time, reduces bandwidth usage.

Example:

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

## Q89. How do you minify HTML?

Minify HTML by removing whitespace, comments, and unnecessary characters while preserving functionality - minification is standard practice for production builds. Removes unnecessary whitespace and comments, reduces file size by 20-30%.

- **Trade-offs**: The catch is not testing functionality after minification, breaking inline JavaScript - be careful with inline CSS and JavaScript, preserve required whitespace. Minification is standard practice for production builds, but watch out - use build tools for automatic minification (Webpack, Gulp, etc.).

Example:

```html
<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Page Title</title></head><body><!-- Content --></body></html>
```

---

## Q90. How do you optimize for mobile?

Optimize HTML for mobile by using responsive design, touch-friendly elements, and mobile-specific optimizations - mobile optimization is essential for modern web development. Use proper viewport meta tag, make touch targets at least 44px.

- **Trade-offs**: The catch is not setting viewport meta tag, causing zoom issues - consider mobile-specific features, use responsive images. Mobile optimization is essential for modern web development, but watch out - optimize images for mobile screens, use appropriate input types.

Example:

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

## Q91. How do you structure HTML for SEO?

Proper HTML structure helps search engines understand content hierarchy and importance, improving search rankings - HTML structure is fundamental for SEO, not just styling. Use semantic HTML elements, create clear heading hierarchy (h1 → h2 → h3).

- **Trade-offs**: The catch is skipping heading levels, using multiple h1 tags - structure content logically, use semantic elements for better SEO. HTML structure is fundamental for SEO, not just styling, but watch out - only one h1 per page, use descriptive alt text for images.

Example:

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

## Q92. What are meta tags and how do you use them?

Meta tags provide information about the page to search engines and social media platforms - meta tags are essential for SEO and social sharing. Title should be 50-60 characters, description should be 150-160 characters.

- **Trade-offs**: The catch is keywords meta tag has limited SEO value (don't overuse) - use descriptive, keyword-rich titles and descriptions. Meta tags are essential for SEO and social sharing, but watch out - use Open Graph for social sharing, canonical URL prevents duplicate content.

Example:

```html
<head>
  <title>Page Title - Company Name</title>
  <meta name="description" content="Brief description of page content (150-160 characters)">
  <meta name="keywords" content="keyword1, keyword2, keyword3">
  <link rel="canonical" href="https://example.com/page">
</head>
```

---

## Q93. How do you implement structured data?

Structured data uses schema.org markup to help search engines understand content and display rich snippets - structured data improves search result visibility. Helps search engines understand content, can result in rich snippets in search results.

- **Trade-offs**: The catch is not following schema.org guidelines, incorrect markup - follow schema.org guidelines, validate with Google's testing tools. Structured data improves search result visibility, but watch out - use JSON-LD for easier implementation, test with Google's Rich Results Test.

Example:

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

## Q94. What are Core Web Vitals?

Core Web Vitals measure user experience metrics that impact SEO rankings: LCP, FID, and CLS - Core Web Vitals directly impact search rankings. LCP (optimize largest contentful paint), FID (minimize JavaScript execution), CLS (prevent layout shifts).

- **Trade-offs**: The catch is not specifying image dimensions, causing layout shifts - optimize LCP element, minimize render-blocking resources. Core Web Vitals directly impact search rankings, but watch out - use preload for critical resources, specify image dimensions.

Example:

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

## Q95. How do you implement caching?

Implement proper caching strategies using HTTP headers and HTML meta tags to improve performance - caching improves performance but requires proper invalidation strategy. Use versioning for static resources, set appropriate cache headers server-side.

- **Trade-offs**: The catch is HTML meta tags have limited support (use HTTP headers instead) - consider CDN for global caching, use proper cache headers. Caching improves performance but requires proper invalidation strategy, but watch out - separate static and dynamic content, use ETags for cache validation.

Example:

```html
<meta http-equiv="Cache-Control" content="public, max-age=31536000">
<meta http-equiv="Expires" content="Wed, 21 Oct 2025 07:28:00 GMT">
```

---

## Q96. What are resource hints and how do you use them to optimize page performance?

Resource hints instruct the browser to perform actions ahead of time to improve loading performance - resource hints improve perceived performance by doing work early. preconnect (opens connection), dns-prefetch (DNS lookup), preload (critical resources), prefetch (future pages).

- **Trade-offs**: The catch is overusing preconnect (limit to 2-4 per page), forgetting crossorigin for CORS resources - use preload for late-discovered critical resources, prefetch for likely navigation. Resource hints improve perceived performance by doing work early, but watch out - use preconnect for critical cross-origin resources like Google Fonts.

Example:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="dns-prefetch" href="https://api.example.com">
<link rel="preload" href="/lcp-image.jpg" as="image" 
      imagesrcset="image-320w.jpg 320w, image-640w.jpg 640w">
<link rel="prefetch" href="/next-page.css" as="style">
```

---

## Q97. What is fetchpriority and how do you use it to optimize resource loading?

`fetchpriority` is an HTML attribute that controls the relative priority of resource fetches, helping browsers prioritize critical resources - fetchpriority is modern browser feature for resource prioritization. `high` for LCP images and critical CSS/JS, `low` for below-the-fold content.

- **Trade-offs**: The catch is overusing `high` priority (typically 1-2 per page), not using it for LCP images - use `high` for critical resources, `low` for non-critical resources. fetchpriority is modern browser feature for resource prioritization, but watch out - especially important for LCP optimization, can improve Core Web Vitals significantly.

Example:

```html
<img src="/hero-image.jpg" fetchpriority="high" alt="Hero image" loading="eager">
<img src="/thumb1.jpg" fetchpriority="low" alt="Thumbnail 1" loading="lazy">
<link rel="stylesheet" href="/critical.css" fetchpriority="high">
<script src="/analytics.js" fetchpriority="low" defer></script>
```

---

## Q98. What is SEO and how can you optimize it?

SEO is the practice of improving website visibility in search engine results through on-page, technical, and off-page optimizations - SEO is ongoing process requiring technical and content optimization. On-page (title tags, meta descriptions, headings), technical (Core Web Vitals, structured data), off-page (backlinks).

- **Trade-offs**: The catch is keyword stuffing, ignoring Core Web Vitals, not using structured data - use semantic HTML, implement schema.org markup, optimize performance. SEO is ongoing process requiring technical and content optimization, but watch out - Core Web Vitals directly impact search rankings, mobile-first indexing is essential.

Example:

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

## Q99. What is sitemap.xml and how do you create it?

A sitemap.xml is an XML file that lists all pages on a website, helping search engines discover and index content efficiently - sitemaps are essential for large sites with many pages. Helps search engines discover all pages, especially deep pages not linked internally.

- **Trade-offs**: The catch is not updating sitemap when content changes, exceeding size limits (50,000 URLs, 50MB) - use sitemap index for large sites, include lastmod dates, compress large sitemaps. Sitemaps are essential for large sites with many pages, but watch out - place at root (`/sitemap.xml`), reference in robots.txt, submit via Google Search Console.

Example:

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

## Q100. What is robots.txt and how do you use it?

robots.txt is a text file in the root directory that instructs web crawlers which pages or directories they can or cannot access - robots.txt is a guideline, not security (bad bots may ignore it). Control crawler access, prevent crawling of sensitive or duplicate content.

- **Trade-offs**: The catch is using robots.txt for security (it's publicly accessible), not testing syntax - use specific rules for different bots, reference sitemap location. robots.txt is a guideline, not security (bad bots may ignore it), but watch out - block `/admin/`, `/api/`, query strings, prevent duplicate content indexing.

Example:

```txt
User-agent: *
Allow: /
Disallow: /admin/
Disallow: /api/
Sitemap: https://example.com/sitemap.xml
```

---

## Q101. What are Open Graph tags and how do you use them?

Open Graph tags are HTML meta tags that control how content appears when shared on social media platforms - Open Graph tags improve social sharing appearance and engagement. Control how links appear when shared on social platforms, creates rich previews.

- **Trade-offs**: The catch is not using absolute URLs for images, incorrect image dimensions (recommended 1200x630px) - use Twitter Card tags alongside OG tags, test with platform debugger tools. Open Graph tags improve social sharing appearance and engagement, but watch out - required tags: og:title, og:type, og:image, og:url (also og:description recommended).

Example:

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
