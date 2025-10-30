# ⚡ 7. Performance & SEO (Q86–95)

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
