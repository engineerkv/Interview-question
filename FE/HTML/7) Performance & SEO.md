# ⚡ 7. Performance & SEO (Q86–101)

---

## 86) How do you optimize HTML for performance?

Concept:
Optimize HTML structure, reduce file size, minimize render-blocking resources, and use efficient loading strategies.

Example:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
```

Deep Insight:
- Minimize HTML file size
- Inline critical CSS
- Defer non-critical resources
- Use lazy loading for images
- Optimize resource loading order

---

## 87) What is the critical rendering path?

Concept:
The critical rendering path is the sequence of steps browsers take to render a page, from HTML parsing to pixel painting.

Example:
```html
<!DOCTYPE html>
<html>
<head>
  <!-- 1. HTML parsing starts -->
  <meta charset="UTF-8">
  
```

Deep Insight:
- HTML → CSS → JavaScript → Layout → Paint
- Render-blocking resources delay rendering
- Critical path determines initial render time
- Optimize by reducing blocking resources
- Use async/defer for non-critical scripts

---

## 88) How do you implement lazy loading for images?

Concept:
Lazy loading defers image loading until they're needed, improving initial page load performance.

Example:
```html
<!-- Native lazy loading -->
<img src="image.jpg" 
     loading="lazy" 
     alt="Description">

<!-- JavaScript lazy loading -->
```

Deep Insight:
- `loading="lazy"` provides native lazy loading
- JavaScript solution offers more control
- Improves initial page load time
- Reduces bandwidth usage
- Don't lazy load above-fold images

---

## 89) What are the different ways to minify HTML?

Concept:
Minify HTML by removing whitespace, comments, and unnecessary characters while preserving functionality.

Example:
```html
<!-- Before minification -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
```

Deep Insight:
- Removes unnecessary whitespace and comments
- Reduces file size by 20-30%
- Use build tools for automatic minification
- Be careful with inline CSS and JavaScript
- Test functionality after minification

---

## 90) How do you optimize HTML for mobile devices?

Concept:
Optimize HTML for mobile by using responsive design, touch-friendly elements, and mobile-specific optimizations.

Example:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
```

Deep Insight:
- Use proper viewport meta tag
- Make touch targets at least 44px
- Optimize images for mobile screens
- Use appropriate input types
- Consider mobile-specific features

---

## 91) What is the importance of HTML structure for SEO?

Concept:
Proper HTML structure helps search engines understand content hierarchy and importance, improving search rankings.

Example:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Best Practices for HTML SEO</title>
  <meta name="description" content="Learn how to optimize HTML for search engines">
```

Deep Insight:
- Use semantic HTML elements
- Create clear heading hierarchy (h1 → h2 → h3)
- Only one h1 per page
- Use descriptive alt text for images
- Structure content logically

---

## 92) How do you create proper meta tags for SEO?

Concept:
Meta tags provide information about the page to search engines and social media platforms.

Example:
```html
<head>
  <!-- Basic meta tags -->
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Page Title - Company Name</title>
  <meta name="description" content="Brief description of page content (150-160 characters)">
```

Deep Insight:
- Title should be 50-60 characters
- Description should be 150-160 characters
- Use Open Graph for social sharing
- Canonical URL prevents duplicate content
- Keywords meta tag has limited SEO value

---

## 93) What is structured data and how do you implement it?

Concept:
Structured data uses schema.org markup to help search engines understand content and display rich snippets.

Example:
```html
<!-- JSON-LD structured data -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How to Optimize HTML for SEO",
```

Deep Insight:
- Helps search engines understand content
- Can result in rich snippets in search results
- Use JSON-LD for easier implementation
- Test with Google's Rich Results Test
- Follow schema.org guidelines

---

## 94) How do you optimize HTML for Core Web Vitals?

Concept:
Core Web Vitals measure user experience metrics that impact SEO rankings: LCP, FID, and CLS.

Example:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
```

Deep Insight:
- LCP: Optimize largest contentful paint element
- FID: Minimize JavaScript execution time
- CLS: Prevent unexpected layout shifts
- Use preload for critical resources
- Specify image dimensions

---

## 95) What are the best practices for HTML caching?

Concept:
Implement proper caching strategies using HTTP headers and HTML meta tags to improve performance.

Example:
```html
<!-- Cache control meta tags (limited support) -->
<meta http-equiv="Cache-Control" content="public, max-age=31536000">
<meta http-equiv="Expires" content="Wed, 21 Oct 2025 07:28:00 GMT">

<!-- ETag for cache validation -->
<meta http-equiv="ETag" content="W/\"abc123\"">
```

Deep Insight:
- Use versioning for static resources
- Set appropriate cache headers server-side
- Separate static and dynamic content
- Use ETags for cache validation
- Consider CDN for global caching

---

## 96) What are resource hints and how do you use them to optimize page performance?

Concept:
Resource hints instruct the browser to perform actions ahead of time to improve loading performance, including early DNS lookups, establishing connections, and prefetching resources before they're discovered.

Example:
```html
<head>
  <!-- preconnect: Establish connection to cross-origin server -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  
  <!-- dns-prefetch: Perform DNS lookup only -->
  <link rel="dns-prefetch" href="https://api.example.com">
  <link rel="dns-prefetch" href="https://cdn.example.com">
  
  <!-- preload: Fetch critical resources early -->
  <link rel="preload" href="/lcp-image.jpg" as="image" imagesrcset="image-320w.jpg 320w, image-640w.jpg 640w">
  <link rel="preload" href="/font.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="/critical.css" as="style">
  
  <!-- prefetch: Low priority fetch for likely future navigation -->
  <link rel="prefetch" href="/next-page.css" as="style">
  <link rel="prefetch" href="/next-page.js" as="script">
</head>

<!-- Fetch Priority API -->
<div class="gallery">
  <img src="poster-1.jpg" fetchpriority="high" alt="LCP image">
  <img src="thumbnail-2.jpg" fetchpriority="low" alt="Thumbnail">
  <img src="thumbnail-3.jpg" fetchpriority="low" alt="Thumbnail">
</div>
```

Deep Insight:
- `preconnect`: Opens connection including DNS, TCP, and TLS handshake—use for critical cross-origin resources like Google Fonts
- `dns-prefetch`: Only performs DNS lookup, less costly—good for non-critical third-party resources or likely navigation links
- `preload`: High priority fetch for late-discovered critical resources like fonts, CSS via @import, or LCP images—requires `as` attribute and `crossorigin` for CORS resources
- `prefetch`: Speculative low-priority fetch for likely future pages—use with analytics data to avoid wasted bandwidth
- `fetchpriority`: Control priority for `<link>`, `<img>`, `<script>`—especially effective for LCP images to improve Core Web Vitals
- Always include `crossorigin` for CORS resources (fonts) to avoid duplicate downloads
- Use `preconnect` sparingly (2-4 per page) and prioritize most critical cross-origin resources
- Reference: [web.dev resource hints](https://web.dev/learn/performance/resource-hints)

## 97) What is fetchpriority and how do you use it to optimize resource loading?

Concept:
`fetchpriority` is an HTML attribute that allows you to control the relative priority of resource fetches, helping browsers prioritize critical resources like LCP images and defer less important resources like thumbnails or below-the-fold images.

Example:
```html
<!-- High priority for LCP image -->
<img 
  src="/hero-image.jpg" 
  fetchpriority="high" 
  alt="Hero image"
  loading="eager"
>

<!-- Low priority for below-the-fold thumbnails -->
<div class="gallery">
  <img src="/thumb1.jpg" fetchpriority="low" alt="Thumbnail 1" loading="lazy">
  <img src="/thumb2.jpg" fetchpriority="low" alt="Thumbnail 2" loading="lazy">
  <img src="/thumb3.jpg" fetchpriority="auto" alt="Thumbnail 3" loading="lazy">
</div>

<!-- High priority for critical CSS -->
<link 
  rel="stylesheet" 
  href="/critical.css" 
  fetchpriority="high"
>

<!-- Low priority for non-critical CSS -->
<link 
  rel="stylesheet" 
  href="/non-critical.css" 
  fetchpriority="low"
>

<!-- High priority for critical JavaScript -->
<script 
  src="/critical.js" 
  fetchpriority="high"
></script>

<!-- Low priority for defer scripts -->
<script 
  src="/analytics.js" 
  fetchpriority="low" 
  defer
></script>

<!-- Combining with preload for LCP optimization -->
<link 
  rel="preload" 
  href="/lcp-image.jpg" 
  as="image" 
  fetchpriority="high"
  imagesrcset="image-320w.jpg 320w, image-640w.jpg 640w"
>

<!-- Use with responsive images -->
<picture>
  <source 
    media="(min-width: 1200px)" 
    srcset="/hero-large.jpg" 
    fetchpriority="high"
  >
  <source 
    media="(min-width: 768px)" 
    srcset="/hero-medium.jpg" 
    fetchpriority="high"
  >
  <img 
    src="/hero-small.jpg" 
    alt="Hero image" 
    fetchpriority="high"
    loading="eager"
  >
</picture>
```

Deep Insight:
- `fetchpriority="high"`: Gives resources highest priority—use for LCP images, critical CSS/JS, above-the-fold content
- `fetchpriority="low"`: Reduces priority—use for below-the-fold images, analytics scripts, non-critical resources
- `fetchpriority="auto"`: Default priority—browser decides based on element type and position (default if not specified)
- Works with `<img>`, `<link>`, `<script>`, and `<source>` elements
- Combines effectively with `loading="lazy"` for low-priority images
- Especially important for LCP (Largest Contentful Paint) optimization—can improve Core Web Vitals significantly
- Use `high` for critical resources that impact initial render
- Use `low` for resources that can wait without affecting user experience
- Browser support: Chrome 101+, Edge 101+, Firefox 102+, Safari 17+
- Test with Chrome DevTools Network tab to verify priority allocation
- Don't overuse `high`—only for truly critical resources (typically 1-2 per page)

---

## 98) What is SEO and how can you optimize it?

Concept:
SEO (Search Engine Optimization) is the practice of improving website visibility in search engine results. It involves on-page, technical, and off-page optimizations to help search engines understand, index, and rank content.

Example:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- Primary Meta Tags -->
  <title>Best Practices for Frontend SEO | Complete Guide 2025</title>
  <meta name="title" content="Best Practices for Frontend SEO | Complete Guide 2025">
  <meta name="description" content="Learn how to optimize your frontend for search engines. Complete guide covering meta tags, structured data, Core Web Vitals, and more.">
  <meta name="keywords" content="SEO, frontend optimization, meta tags, structured data">
  <meta name="author" content="Your Name">
  <meta name="robots" content="index, follow">
  
  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://example.com/seo-guide">
  <meta property="og:title" content="Best Practices for Frontend SEO">
  <meta property="og:description" content="Complete guide to frontend SEO optimization">
  <meta property="og:image" content="https://example.com/seo-preview.jpg">
  
  <!-- Twitter -->
  <meta property="twitter:card" content="summary_large_image">
  <meta property="twitter:url" content="https://example.com/seo-guide">
  <meta property="twitter:title" content="Best Practices for Frontend SEO">
  <meta property="twitter:description" content="Complete guide to frontend SEO optimization">
  <meta property="twitter:image" content="https://example.com/seo-preview.jpg">
  
  <!-- Canonical URL -->
  <link rel="canonical" href="https://example.com/seo-guide">
  
  <!-- Structured Data (JSON-LD) -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "Best Practices for Frontend SEO",
    "description": "Complete guide to frontend SEO optimization",
    "author": {
      "@type": "Person",
      "name": "Your Name"
    },
    "publisher": {
      "@type": "Organization",
      "name": "Your Company",
      "logo": {
        "@type": "ImageObject",
        "url": "https://example.com/logo.png"
      }
    },
    "datePublished": "2025-01-15",
    "dateModified": "2025-01-20",
    "mainEntityOfPage": {
      "@type": "WebPage",
      "@id": "https://example.com/seo-guide"
    }
  }
  </script>
  
  <!-- Sitemap reference -->
  <link rel="sitemap" href="/sitemap.xml">
</head>
<body>
  <!-- Semantic HTML structure -->
  <header>
    <nav aria-label="Main navigation">
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/blog">Blog</a></li>
      </ul>
    </nav>
  </header>
  
  <main>
    <article>
      <!-- Proper heading hierarchy -->
      <h1>Best Practices for Frontend SEO</h1>
      
      <!-- Descriptive images with alt text -->
      <img 
        src="/seo-diagram.jpg" 
        alt="SEO optimization checklist diagram showing on-page, technical, and off-page factors"
        loading="lazy"
        width="800"
        height="600"
      >
      
      <section>
        <h2>On-Page SEO Optimization</h2>
        <p>On-page SEO focuses on optimizing individual web pages...</p>
        
        <h3>Title Tags and Meta Descriptions</h3>
        <p>Use descriptive, keyword-rich titles under 60 characters...</p>
      </section>
      
      <section>
        <h2>Technical SEO</h2>
        <p>Technical SEO ensures search engines can crawl and index your site...</p>
      </section>
    </article>
  </main>
  
  <footer>
    <p>&copy; 2025 Your Company. All rights reserved.</p>
  </footer>
</body>
</html>
```

```javascript
// Dynamic SEO with Next.js or similar frameworks
// pages/seo-guide.js (Next.js)
export default function SEOGuide() {
  return (
    <>
      <Head>
        <title>Best Practices for Frontend SEO | Complete Guide 2025</title>
        <meta name="description" content="Learn how to optimize your frontend for search engines..." />
        <meta property="og:title" content="Best Practices for Frontend SEO" />
        <meta property="og:description" content="Complete guide to frontend SEO optimization" />
        <meta property="og:image" content="https://example.com/seo-preview.jpg" />
        <link rel="canonical" href="https://example.com/seo-guide" />
      </Head>
      
      <main>
        <article>
          <h1>Best Practices for Frontend SEO</h1>
          {/* Content */}
        </article>
      </main>
    </>
  );
}

// robots.txt
// User-agent: *
// Allow: /
// Disallow: /admin/
// Disallow: /api/
// Sitemap: https://example.com/sitemap.xml

// sitemap.xml structure
// <?xml version="1.0" encoding="UTF-8"?>
// <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
//   <url>
//     <loc>https://example.com/</loc>
//     <lastmod>2025-01-20</lastmod>
//     <changefreq>daily</changefreq>
//     <priority>1.0</priority>
//   </url>
// </urlset>
```

Deep Insight:
- **On-Page SEO**: Optimize title tags (50-60 chars), meta descriptions (150-160 chars), headings hierarchy (H1-H6), alt text for images, internal linking structure, URL structure (short, descriptive, keyword-rich), and content quality (original, valuable, keyword-optimized without stuffing)
- **Technical SEO**: Ensure fast page load (Core Web Vitals), mobile responsiveness, HTTPS, proper HTTP status codes (200, 301 redirects), XML sitemap, robots.txt, canonical URLs (prevent duplicate content), structured data (JSON-LD schema.org), and crawlability (proper HTML structure, no JavaScript-blocked content)
- **Core Web Vitals**: LCP (Largest Contentful Paint < 2.5s), FID (First Input Delay < 100ms), CLS (Cumulative Layout Shift < 0.1)—directly impact search rankings
- **Semantic HTML**: Use proper semantic tags (`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<footer>`) to help search engines understand content structure
- **Mobile-First**: Google uses mobile-first indexing—ensure responsive design, fast mobile load times, and mobile-friendly navigation
- **Structured Data**: Implement schema.org markup (JSON-LD preferred) for rich snippets—Article, Product, FAQ, BreadcrumbList, Organization, etc.
- **Image Optimization**: Use descriptive alt text, proper file formats (WebP, AVIF), lazy loading for below-fold images, and responsive images with `srcset`
- **URL Structure**: Keep URLs short, descriptive, keyword-rich, and readable (avoid parameters when possible, use hyphens not underscores)
- **Internal Linking**: Create logical internal link structure to help crawlers discover content and establish site hierarchy
- **Performance**: Page speed is a ranking factor—minimize render-blocking resources, optimize images, use CDN, enable compression (gzip/Brotli), and leverage browser caching
- **Analytics & Monitoring**: Use Google Search Console to monitor search performance, identify crawl errors, submit sitemaps, and track keyword rankings

---

## 99) What is sitemap.xml and how do you create it?

Concept:
A sitemap.xml is an XML file that lists all pages on a website, helping search engines discover, crawl, and index content more efficiently. It includes metadata like last modification dates, change frequency, and priority.

Example:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
        http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
  
  <!-- Homepage with highest priority -->
  <url>
    <loc>https://example.com/</loc>
    <lastmod>2025-01-20</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
  
  <!-- Product page -->
  <url>
    <loc>https://example.com/products/</loc>
    <lastmod>2025-01-19</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  
  <!-- Individual product -->
  <url>
    <loc>https://example.com/products/item-123</loc>
    <lastmod>2025-01-18</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
  
  <!-- Blog post -->
  <url>
    <loc>https://example.com/blog/seo-guide</loc>
    <lastmod>2025-01-15</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.5</priority>
  </url>
</urlset>
```

```html
<!-- Reference sitemap in HTML head (optional) -->
<head>
  <link rel="sitemap" type="application/xml" href="/sitemap.xml">
</head>
```

```javascript
// Dynamically generate sitemap (Node.js/Express example)
app.get('/sitemap.xml', (req, res) => {
  res.set('Content-Type', 'application/xml');
  
  const urls = [
    { loc: 'https://example.com/', lastmod: '2025-01-20', priority: '1.0' },
    { loc: 'https://example.com/about', lastmod: '2025-01-15', priority: '0.8' },
    // ... more URLs
  ];
  
  let xml = '<?xml version="1.0" encoding="UTF-8"?>\n';
  xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n';
  
  urls.forEach(url => {
    xml += `  <url>\n`;
    xml += `    <loc>${url.loc}</loc>\n`;
    xml += `    <lastmod>${url.lastmod}</lastmod>\n`;
    xml += `    <priority>${url.priority}</priority>\n`;
    xml += `  </url>\n`;
  });
  
  xml += '</urlset>';
  res.send(xml);
});

// Sitemap index for large sites (multiple sitemaps)
// sitemap.xml (index file)
<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <sitemap>
    <loc>https://example.com/sitemap-pages.xml</loc>
    <lastmod>2025-01-20</lastmod>
  </sitemap>
  <sitemap>
    <loc>https://example.com/sitemap-products.xml</loc>
    <lastmod>2025-01-19</lastmod>
  </sitemap>
  <sitemap>
    <loc>https://example.com/sitemap-blog.xml</loc>
    <lastmod>2025-01-18</lastmod>
  </sitemap>
</sitemapindex>
```

Deep Insight:
- **Purpose**: Helps search engines discover all pages, especially deep pages that might not be linked internally, and indicates page importance (priority) and update frequency (changefreq)
- **Location**: Place at root (`/sitemap.xml`) or reference in `robots.txt` with `Sitemap: https://example.com/sitemap.xml`
- **Priority**: Range 0.0–1.0 (default 0.5); relative, not absolute—homepage typically 1.0
- **Change Frequency**: `always`, `hourly`, `daily`, `weekly`, `monthly`, `yearly`, `never`—hints for crawlers, not strict rules
- **Last Modified**: ISO 8601 date format (`YYYY-MM-DD` or `YYYY-MM-DDTHH:mm:ss+00:00`)—helps crawlers know when content changed
- **Size Limits**: Single sitemap max 50,000 URLs, 50MB uncompressed—split into multiple sitemaps for larger sites using sitemap index
- **Image Sitemaps**: Include `<image:image>` tags for image SEO—helps images appear in Google Image search
- **Video Sitemaps**: Use `<video:video>` tags for video content—can improve video search visibility
- **Submission**: Submit via Google Search Console, Bing Webmaster Tools, or reference in robots.txt
- **Dynamic Generation**: Automatically generate from database for e-commerce/blog sites—update whenever content changes
- **Compression**: Gzip compress large sitemaps (`.xml.gz`) to reduce bandwidth and file size
- **HTTPS**: Use HTTPS URLs in sitemap even if site supports both HTTP/HTTPS—prefers secure version

---

## 100) What is robots.txt and how do you use it?

Concept:
robots.txt is a text file in the root directory that instructs web crawlers which pages or directories they can or cannot access. It's the first file crawlers check before crawling a site.

Example:
```txt
# robots.txt - Standard directives

# Allow all crawlers to access all content
User-agent: *
Allow: /

# Disallow specific directories
User-agent: *
Disallow: /admin/
Disallow: /private/
Disallow: /api/
Disallow: /temp/
Disallow: /search?q=

# Allow specific crawler, disallow others
User-agent: Googlebot
Allow: /

User-agent: *
Disallow: /

# Crawl-delay (time in seconds between requests)
User-agent: *
Crawl-delay: 1

# Sitemap location
Sitemap: https://example.com/sitemap.xml
Sitemap: https://example.com/sitemap-products.xml

# Specific rules for different bots
User-agent: Googlebot
Allow: /products/
Disallow: /private/

User-agent: Bingbot
Allow: /
Crawl-delay: 2

# Block bad bots
User-agent: BadBot
Disallow: /

User-agent: ScraperBot
Disallow: /

# Allow images (for Google Image search)
User-agent: Googlebot-Image
Allow: /images/
Disallow: /private-images/

# Block crawling of specific file types
User-agent: *
Disallow: /*.pdf$
Disallow: /*.docx$

# Allow specific paths with wildcards
User-agent: *
Allow: /public/*.html
Disallow: /private/
```

```html
<!-- robots.txt must be at root: /robots.txt -->
<!-- Accessible at: https://example.com/robots.txt -->
```

```javascript
// Dynamically serve robots.txt (Node.js/Express)
app.get('/robots.txt', (req, res) => {
  res.set('Content-Type', 'text/plain');
  
  let robots = `User-agent: *\n`;
  robots += `Disallow: /admin/\n`;
  robots += `Disallow: /api/\n`;
  robots += `Disallow: /private/\n`;
  robots += `\n`;
  robots += `Sitemap: ${req.protocol}://${req.get('host')}/sitemap.xml\n`;
  
  res.send(robots);
});

// Environment-based robots.txt
app.get('/robots.txt', (req, res) => {
  res.set('Content-Type', 'text/plain');
  
  if (process.env.NODE_ENV === 'production') {
    res.send(`User-agent: *\nAllow: /\nSitemap: https://example.com/sitemap.xml`);
  } else {
    // Block all crawlers in development/staging
    res.send(`User-agent: *\nDisallow: /`);
  }
});
```

Deep Insight:
- **Location**: Must be at root directory (`/robots.txt`)—case-sensitive, lowercase file name required
- **Syntax**: Simple text format—one directive per line, `#` for comments, empty lines for readability
- **User-agent**: Specify which crawler (`*` for all, `Googlebot`, `Bingbot`, etc.)—more specific rules override general ones
- **Disallow/Allow**: `Disallow` blocks access, `Allow` overrides disallow—order matters (first matching rule wins)
- **Wildcards**: Use `*` for any sequence, `$` for end of URL—`Disallow: /search?q=*` blocks search pages
- **Crawl-delay**: Time in seconds between requests (not respected by all crawlers)—helps reduce server load but not standard
- **Sitemap**: Reference sitemap location—can list multiple sitemaps, helps crawlers discover content
- **Not Security**: robots.txt is publicly accessible—don't use it to hide sensitive data (crawlers may ignore it)
- **Meta Robots**: Can also use `<meta name="robots" content="noindex, nofollow">` in HTML head—more granular per-page control
- **HTTP Headers**: Can use `X-Robots-Tag` HTTP header for programmatic control—useful for API responses
- **Testing**: Use Google Search Console robots.txt tester to verify syntax and test specific URLs
- **Common Patterns**: Block `/admin/`, `/api/`, `/private/`, query strings, duplicate content, test/staging environments
- **Compliance**: Well-behaved crawlers (Google, Bing) respect robots.txt—bad bots may ignore it (need server-level blocking)

---

## 101) What are Open Graph tags and how do you use them?

Concept:
Open Graph (OG) tags are HTML meta tags that control how content appears when shared on social media platforms (Facebook, Twitter, LinkedIn, etc.). They enable rich previews with images, titles, and descriptions.

Example:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Best Practices for Frontend SEO | Complete Guide 2025</title>
  
  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://example.com/seo-guide">
  <meta property="og:title" content="Best Practices for Frontend SEO | Complete Guide 2025">
  <meta property="og:description" content="Learn how to optimize your frontend for search engines. Complete guide covering meta tags, structured data, Core Web Vitals, and more.">
  <meta property="og:image" content="https://example.com/images/seo-guide-preview.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="SEO optimization checklist diagram">
  <meta property="og:site_name" content="Your Site Name">
  <meta property="og:locale" content="en_US">
  
  <!-- Article-specific OG tags -->
  <meta property="og:type" content="article">
  <meta property="article:published_time" content="2025-01-15T10:00:00+00:00">
  <meta property="article:modified_time" content="2025-01-20T15:30:00+00:00">
  <meta property="article:author" content="John Doe">
  <meta property="article:section" content="Technology">
  <meta property="article:tag" content="SEO">
  <meta property="article:tag" content="Frontend">
  <meta property="article:tag" content="Web Development">
  
  <!-- Video-specific OG tags -->
  <meta property="og:type" content="video.other">
  <meta property="og:video" content="https://example.com/video.mp4">
  <meta property="og:video:type" content="video/mp4">
  <meta property="og:video:width" content="1280">
  <meta property="og:video:height" content="720">
  <meta property="og:video:secure_url" content="https://example.com/video.mp4">
  
  <!-- Twitter Card (complements Open Graph) -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:url" content="https://example.com/seo-guide">
  <meta name="twitter:title" content="Best Practices for Frontend SEO">
  <meta name="twitter:description" content="Complete guide to frontend SEO optimization">
  <meta name="twitter:image" content="https://example.com/images/seo-guide-preview.jpg">
  <meta name="twitter:image:alt" content="SEO optimization checklist">
  <meta name="twitter:site" content="@yourhandle">
  <meta name="twitter:creator" content="@johndoe">
</head>
<body>
  <!-- Content -->
</body>
</html>
```

```javascript
// Dynamic Open Graph tags (Next.js example)
import Head from 'next/head';

export default function Article({ article }) {
  return (
    <>
      <Head>
        <title>{article.title}</title>
        <meta property="og:type" content="article" />
        <meta property="og:title" content={article.title} />
        <meta property="og:description" content={article.excerpt} />
        <meta property="og:image" content={article.imageUrl} />
        <meta property="og:url" content={`https://example.com/articles/${article.slug}`} />
        <meta property="article:published_time" content={article.publishedAt} />
        <meta property="article:author" content={article.author.name} />
      </Head>
      
      <article>
        <h1>{article.title}</h1>
        {/* Content */}
      </article>
    </>
  );
}

// React with Helmet
import { Helmet } from 'react-helmet';

function ProductPage({ product }) {
  return (
    <>
      <Helmet>
        <meta property="og:type" content="product" />
        <meta property="og:title" content={product.name} />
        <meta property="og:description" content={product.description} />
        <meta property="og:image" content={product.image} />
        <meta property="og:url" content={`https://example.com/products/${product.id}`} />
        <meta property="product:price:amount" content={product.price} />
        <meta property="product:price:currency" content="USD" />
      </Helmet>
      
      <div>
        <h1>{product.name}</h1>
        {/* Product details */}
      </div>
    </>
  );
}
```

Deep Insight:
- **Purpose**: Control how links appear when shared on social platforms—creates rich previews with images, titles, descriptions instead of plain text links
- **Required Tags**: `og:title`, `og:type`, `og:image`, `og:url` (also `og:description` recommended)—minimum set for basic previews
- **Image Guidelines**: Recommended 1200x630px for optimal display across platforms, use absolute URLs (https://), max 5MB file size, JPG/PNG format—previews look professional with proper images
- **OG Types**: `website` (default), `article` (blog posts), `product` (e-commerce), `video.other`, `music.song`, `profile`—different types enable platform-specific features
- **Article Tags**: `article:published_time`, `article:modified_time`, `article:author`, `article:section`, `article:tag`—help organize and display article metadata
- **Twitter Cards**: Use alongside OG tags—Twitter supports both, prefers Twitter Card tags (`twitter:card`, `twitter:image`, etc.)
- **Dynamic Content**: Generate OG tags server-side or with SSR—ensures crawlers see tags even for JS-rendered content
- **Testing Tools**: Use Facebook Sharing Debugger, Twitter Card Validator, LinkedIn Post Inspector—test how links appear before sharing
- **Cache Busting**: Social platforms cache OG data—use their debugger tools to refresh cache after updating tags
- **Multiple Images**: Can specify multiple images with `og:image`, `og:image:secure_url`—platforms choose which to display
- **Localization**: Use `og:locale` and `og:locale:alternate` for multi-language sites—helps platforms serve correct language
- **Video/Audio**: Use `og:video` or `og:audio` tags for media content—enables inline playback in some platforms
- **App Integration**: Use `og:app_id` for Facebook apps—enables deeper integration with Facebook platform features
