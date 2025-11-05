# ⚡ 7. Performance & SEO (Q86–101)

---

## 86) How do you optimize HTML for performance?

Optimize HTML structure, reduce file size, minimize render-blocking resources, and use efficient loading strategies.

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

- **Core Techniques**: Minimize HTML file size, inline critical CSS, defer non-critical resources
- **Real-World Use**: Use lazy loading for images, optimize resource loading order
- **Common Mistake**: Loading all resources at once, blocking initial render
- **Optimization**: Use preload for critical resources, minify HTML
- **Interview Tip**: Explain that HTML optimization reduces initial load time and improves Core Web Vitals

---

## 87) What is the critical rendering path?

The critical rendering path is the sequence of steps browsers take to render a page, from HTML parsing to pixel painting.

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

- **Core Sequence**: HTML → CSS → JavaScript → Layout → Paint
- **Real-World Impact**: Render-blocking resources delay rendering, critical path determines initial render time
- **Common Mistake**: Loading all CSS and JavaScript synchronously
- **Optimization**: Use async/defer for non-critical scripts, inline critical CSS
- **Interview Tip**: Explain that optimizing the critical path improves First Contentful Paint

---

## 88) How do you implement lazy loading for images?

Lazy loading defers image loading until they're needed, improving initial page load performance.

```html
<img src="image.jpg" loading="lazy" alt="Description">
<img data-src="image.jpg" class="lazy" alt="Description">
<script>
document.querySelectorAll('.lazy').forEach(img => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => { if (entry.isIntersecting) { img.src = img.dataset.src; observer.unobserve(img); } });
  });
  observer.observe(img);
});
</script>
```

- **Core Methods**: `loading="lazy"` provides native lazy loading, JavaScript solution offers more control
- **Real-World Use**: Improves initial page load time, reduces bandwidth usage
- **Common Mistake**: Lazy loading above-fold images (should be eager)
- **Optimization**: Use Intersection Observer for better performance than scroll listeners
- **Interview Tip**: Explain that lazy loading is essential for pages with many images

---

## 89) What are the different ways to minify HTML?

Minify HTML by removing whitespace, comments, and unnecessary characters while preserving functionality.

```html
<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Page Title</title></head><body><!-- Content --></body></html>
```

- **Core Process**: Removes unnecessary whitespace and comments, reduces file size by 20-30%
- **Real-World Use**: Use build tools for automatic minification (Webpack, Gulp, etc.)
- **Common Mistake**: Not testing functionality after minification, breaking inline JavaScript
- **Optimization**: Be careful with inline CSS and JavaScript, preserve required whitespace
- **Interview Tip**: Explain that minification is standard practice for production builds

---

## 90) How do you optimize HTML for mobile devices?

Optimize HTML for mobile by using responsive design, touch-friendly elements, and mobile-specific optimizations.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mobile Optimized Page</title>
</head>
<body>
  <button style="min-width: 44px; min-height: 44px;">Touch Target</button>
  <img src="mobile-image.jpg" alt="Mobile image" srcset="mobile-320w.jpg 320w, mobile-640w.jpg 640w" sizes="100vw">
</body>
</html>
```

- **Core Requirements**: Use proper viewport meta tag, make touch targets at least 44px
- **Real-World Use**: Optimize images for mobile screens, use appropriate input types
- **Common Mistake**: Not setting viewport meta tag, causing zoom issues
- **Optimization**: Consider mobile-specific features, use responsive images
- **Interview Tip**: Explain that mobile optimization is essential for modern web development

---

## 91) What is the importance of HTML structure for SEO?

Proper HTML structure helps search engines understand content hierarchy and importance, improving search rankings.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Best Practices for HTML SEO</title>
  <meta name="description" content="Learn how to optimize HTML for search engines">
</head>
<body>
  <header><h1>SEO Best Practices</h1></header>
  <main><article><h2>Introduction</h2><p>Content...</p></article></main>
</body>
</html>
```

- **Core Principle**: Use semantic HTML elements, create clear heading hierarchy (h1 → h2 → h3)
- **Real-World Impact**: Only one h1 per page, use descriptive alt text for images
- **Common Mistake**: Skipping heading levels, using multiple h1 tags
- **Optimization**: Structure content logically, use semantic elements for better SEO
- **Interview Tip**: Explain that HTML structure is fundamental for SEO, not just styling

---

## 92) How do you create proper meta tags for SEO?

Meta tags provide information about the page to search engines and social media platforms.

```html
<head>
  <title>Page Title - Company Name</title>
  <meta name="description" content="Brief description of page content (150-160 characters)">
  <meta name="keywords" content="keyword1, keyword2, keyword3">
  <link rel="canonical" href="https://example.com/page">
</head>
```

- **Core Requirements**: Title should be 50-60 characters, description should be 150-160 characters
- **Real-World Use**: Use Open Graph for social sharing, canonical URL prevents duplicate content
- **Common Mistake**: Keywords meta tag has limited SEO value (don't overuse)
- **Optimization**: Use descriptive, keyword-rich titles and descriptions
- **Interview Tip**: Explain that meta tags are essential for SEO and social sharing

---

## 93) What is structured data and how do you implement it?

Structured data uses schema.org markup to help search engines understand content and display rich snippets.

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

- **Core Purpose**: Helps search engines understand content, can result in rich snippets in search results
- **Real-World Use**: Use JSON-LD for easier implementation, test with Google's Rich Results Test
- **Common Mistake**: Not following schema.org guidelines, incorrect markup
- **Optimization**: Follow schema.org guidelines, validate with Google's testing tools
- **Interview Tip**: Explain that structured data improves search result visibility

---

## 94) How do you optimize HTML for Core Web Vitals?

Core Web Vitals measure user experience metrics that impact SEO rankings: LCP, FID, and CLS.

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

- **Core Metrics**: LCP (optimize largest contentful paint), FID (minimize JavaScript execution), CLS (prevent layout shifts)
- **Real-World Use**: Use preload for critical resources, specify image dimensions
- **Common Mistake**: Not specifying image dimensions, causing layout shifts
- **Optimization**: Optimize LCP element, minimize render-blocking resources
- **Interview Tip**: Explain that Core Web Vitals directly impact search rankings

---

## 95) What are the best practices for HTML caching?

Implement proper caching strategies using HTTP headers and HTML meta tags to improve performance.

```html
<meta http-equiv="Cache-Control" content="public, max-age=31536000">
<meta http-equiv="Expires" content="Wed, 21 Oct 2025 07:28:00 GMT">
```

- **Core Strategy**: Use versioning for static resources, set appropriate cache headers server-side
- **Real-World Use**: Separate static and dynamic content, use ETags for cache validation
- **Common Mistake**: HTML meta tags have limited support (use HTTP headers instead)
- **Optimization**: Consider CDN for global caching, use proper cache headers
- **Interview Tip**: Explain that caching improves performance but requires proper invalidation strategy

---

## 96) What are resource hints and how do you use them to optimize page performance?

Resource hints instruct the browser to perform actions ahead of time to improve loading performance.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="dns-prefetch" href="https://api.example.com">
<link rel="preload" href="/lcp-image.jpg" as="image" imagesrcset="image-320w.jpg 320w, image-640w.jpg 640w">
<link rel="prefetch" href="/next-page.css" as="style">
```

- **Core Types**: preconnect (opens connection), dns-prefetch (DNS lookup), preload (critical resources), prefetch (future pages)
- **Real-World Use**: Use preconnect for critical cross-origin resources like Google Fonts
- **Common Mistake**: Overusing preconnect (limit to 2-4 per page), forgetting crossorigin for CORS resources
- **Optimization**: Use preload for late-discovered critical resources, prefetch for likely navigation
- **Interview Tip**: Explain that resource hints improve perceived performance by doing work early

---

## 97) What is fetchpriority and how do you use it to optimize resource loading?

`fetchpriority` is an HTML attribute that controls the relative priority of resource fetches, helping browsers prioritize critical resources.

```html
<img src="/hero-image.jpg" fetchpriority="high" alt="Hero image" loading="eager">
<img src="/thumb1.jpg" fetchpriority="low" alt="Thumbnail 1" loading="lazy">
<link rel="stylesheet" href="/critical.css" fetchpriority="high">
<script src="/analytics.js" fetchpriority="low" defer></script>
```

- **Core Values**: `high` for LCP images and critical CSS/JS, `low` for below-the-fold content
- **Real-World Use**: Especially important for LCP optimization, can improve Core Web Vitals significantly
- **Common Mistake**: Overusing `high` priority (typically 1-2 per page), not using it for LCP images
- **Optimization**: Use `high` for critical resources, `low` for non-critical resources
- **Interview Tip**: Explain that fetchpriority is modern browser feature for resource prioritization

---

## 98) What is SEO and how can you optimize it?

SEO is the practice of improving website visibility in search engine results through on-page, technical, and off-page optimizations.

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
  <header><h1>Best Practices for Frontend SEO</h1></header>
  <main><article><h2>On-Page SEO</h2><p>Content...</p></article></main>
</body>
```

- **Core Areas**: On-page (title tags, meta descriptions, headings), technical (Core Web Vitals, structured data), off-page (backlinks)
- **Real-World Impact**: Core Web Vitals directly impact search rankings, mobile-first indexing is essential
- **Common Mistake**: Keyword stuffing, ignoring Core Web Vitals, not using structured data
- **Optimization**: Use semantic HTML, implement schema.org markup, optimize performance
- **Interview Tip**: Explain that SEO is ongoing process requiring technical and content optimization

---

## 99) What is sitemap.xml and how do you create it?

A sitemap.xml is an XML file that lists all pages on a website, helping search engines discover and index content efficiently.

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

- **Core Purpose**: Helps search engines discover all pages, especially deep pages not linked internally
- **Real-World Use**: Place at root (`/sitemap.xml`), reference in robots.txt, submit via Google Search Console
- **Common Mistake**: Not updating sitemap when content changes, exceeding size limits (50,000 URLs, 50MB)
- **Optimization**: Use sitemap index for large sites, include lastmod dates, compress large sitemaps
- **Interview Tip**: Explain that sitemaps are essential for large sites with many pages

---

## 100) What is robots.txt and how do you use it?

robots.txt is a text file in the root directory that instructs web crawlers which pages or directories they can or cannot access.

```txt
User-agent: *
Allow: /
Disallow: /admin/
Disallow: /api/
Sitemap: https://example.com/sitemap.xml
```

- **Core Purpose**: Control crawler access, prevent crawling of sensitive or duplicate content
- **Real-World Use**: Block `/admin/`, `/api/`, query strings, prevent duplicate content indexing
- **Common Mistake**: Using robots.txt for security (it's publicly accessible), not testing syntax
- **Optimization**: Use specific rules for different bots, reference sitemap location
- **Interview Tip**: Explain that robots.txt is a guideline, not security (bad bots may ignore it)

---

## 101) What are Open Graph tags and how do you use them?

Open Graph tags are HTML meta tags that control how content appears when shared on social media platforms.

```html
<head>
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://example.com/seo-guide">
  <meta property="og:title" content="Best Practices for Frontend SEO">
  <meta property="og:description" content="Complete guide to frontend SEO optimization">
  <meta property="og:image" content="https://example.com/seo-preview.jpg">
</head>
```

- **Core Purpose**: Control how links appear when shared on social platforms, creates rich previews
- **Real-World Use**: Required tags: og:title, og:type, og:image, og:url (also og:description recommended)
- **Common Mistake**: Not using absolute URLs for images, incorrect image dimensions (recommended 1200x630px)
- **Optimization**: Use Twitter Card tags alongside OG tags, test with platform debugger tools
- **Interview Tip**: Explain that Open Graph tags improve social sharing appearance and engagement

---
