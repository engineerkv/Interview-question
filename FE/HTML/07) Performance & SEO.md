# ⚡ 7. Performance & SEO (Q86–96)

---

## 📍 Navigation

<div align="center">

[← Previous: Media & Images](06%29%20Media%20%26%20Images.md) • [Home: README](../README.md)
[📋 Cheatsheet](HTML%20Interview%20Cheatsheet.md)

</div>

---

---

## Q86. 🔧 Implementing lazy loading

Lazy loading defers image loading until these are needed, improving initial page load performance - lazy loading is essential for pages with many images. `loading="lazy"` provides native lazy loading, JavaScript solution offers more control.

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

## Q87. 📄 Structuring HTML for SEO

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

## Q88. ❓ Meta tags and how to use them

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

## Q89. 🔧 Implementing structured data

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

## Q90. 💾 Implementing caching

Implement proper caching strategies using HTTP headers and HTML meta tags to improve performance - caching improves performance but requires proper invalidation strategy. Use versioning for static resources, set appropriate cache headers server-side.

- **Trade-offs**: The catch is HTML meta tags have limited support (use HTTP headers instead) - consider CDN for global caching, use proper cache headers. Caching improves performance but requires proper invalidation strategy, but watch out - separate static and dynamic content, use ETags for cache validation.

Example:

```html
<meta http-equiv="Cache-Control" content="public, max-age=31536000">
<meta http-equiv="Expires" content="Wed, 21 Oct 2025 07:28:00 GMT">

```

---

## Q91. ⚡ Resource hints and how to use them to optimize page performance

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

## Q92. ⚡ `fetchpriority` and how to use it to optimize resource loading

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

## Q93. ⚡ SEO and how to optimize it

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

## Q94. ❓ `sitemap.xml` and how to create it

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

## Q95. ❓ `robots.txt` and how to use it

robots.txt is a text file in the root directory that instructs web crawlers which pages or directories crawlers can or cannot access - robots.txt is a guideline, not security (bad bots may ignore it). Control crawler access, prevent crawling of sensitive or duplicate content.

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

## Q96. ❓ Open Graph tags and how to use them

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

---

## 📍 Navigation

<div align="center">

[← Previous: Media & Images](06%29%20Media%20%26%20Images.md) • [Home: README](../README.md)
[📋 Cheatsheet](HTML%20Interview%20Cheatsheet.md)

</div>

---
