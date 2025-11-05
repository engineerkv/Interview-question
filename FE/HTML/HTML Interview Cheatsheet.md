# 🌐 HTML Interview Cheatsheet

> **⏱️ Review Time: 10-15 minutes** | **Priority: ⭐⭐⭐ High** | Essential HTML concepts for interviews

**Quick Review Checklist:**
- [ ] Document Structure & Semantic HTML
- [ ] Forms & Input Types
- [ ] Accessibility (ARIA, Keyboard Navigation)
- [ ] HTML5 Features (New Elements, Data Attributes)
- [ ] Media Elements (Images, Video, Audio)
- [ ] Performance & SEO (Meta Tags, Core Web Vitals)
- [ ] Browser Rendering Pipeline

---

## 📋 **Quick Reference**

### **Document Structure**
```html
<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Page Title</title></head>
<body><!-- Content --></body>
</html>
```

### **Semantic Elements**
```html
<body>
  <header><h1>Site Title</h1><nav><ul><li><a href="/">Home</a></li></ul></nav></header>
  <main><article><section><h2>Article Title</h2><p>Content...</p></section></article><aside>Sidebar</aside></main>
  <footer><p>Copyright 2024</p></footer>
</body>
```

### **Form Structure**
```html
<form action="/submit" method="POST">
  <fieldset><legend>Personal Information</legend>
    <label for="name">Name:</label><input type="text" id="name" name="name" required>
    <label for="email">Email:</label><input type="email" id="email" name="email" required>
    <button type="submit">Submit</button>
  </fieldset>
</form>
```

---

## 🏗️ **Semantic HTML Quick Guide**

| Element | Purpose | Key Points |
|---------|---------|------------|
| `<header>` | Introductory content | Can appear multiple times |
| `<nav>` | Navigation links | Creates landmark region |
| `<main>` | Primary content | Only one per page |
| `<article>` | Standalone content | Can be syndicated |
| `<section>` | Thematic grouping | Needs a heading |
| `<aside>` | Tangential content | Sidebar, related links |
| `<footer>` | Closing content | Site/app footer |

**Rules**: One `<h1>` per page, don't skip heading levels (h1→h3 is wrong), use semantic elements over divs.

---

## 📝 **Forms & Input Types**

### **Input Types**
```html
<!-- Text: text, email, password, url, tel, search -->
<!-- Selection: radio, checkbox, select, file -->
<!-- Date/Time: date, time, datetime-local, month, week -->
<!-- Other: number, range, color -->
```

### **Validation Attributes**
```html
<input required>           <!-- Required field -->
<input minlength="3">     <!-- Min length -->
<input maxlength="50">    <!-- Max length -->
<input pattern="[A-Za-z]+">  <!-- Regex pattern -->
<input min="0" max="100"> <!-- Numeric range -->
```

### **Button Types**
```html
<button type="submit">Submit</button>  <!-- Submits form -->
<button type="reset">Reset</button>    <!-- Clears form -->
<button type="button">Cancel</button>  <!-- No default action -->
```

---

## ♿ **Accessibility (A11y)**

### **ARIA Landmarks**
```html
<header role="banner">
<nav role="navigation" aria-label="Main navigation">
<main role="main">
<aside role="complementary">
<footer role="contentinfo">
```

### **Essential ARIA Attributes**
```html
<!-- Labels -->
<button aria-label="Close dialog">×</button>
<input aria-describedby="help-text" required>
<div id="help-text">This field is required</div>

<!-- States -->
<button aria-expanded="false" aria-controls="menu">Menu</button>
<div id="menu" aria-hidden="true">Menu content</div>

<!-- Live regions -->
<div aria-live="polite">Status updates</div>
<div aria-live="assertive">Urgent alerts</div>
```

### **Accessible Images**
```html
<!-- Decorative: empty alt -->
<img src="decoration.jpg" alt="" role="presentation">

<!-- Informative: descriptive alt -->
<img src="chart.jpg" alt="Sales increased 25% in Q3 2024">

<!-- Complex: alt + longdesc or caption -->
<figure>
  <img src="infographic.jpg" alt="Sales data visualization">
  <figcaption>Complete sales data for 2024</figcaption>
</figure>
```

### **Keyboard Navigation**
```html
<!-- Tab order -->
<button tabindex="0">Natural order</button>      <!-- Focusable -->
<div tabindex="-1">Not in tab order</div>        <!-- Programmatic focus -->
<button tabindex="3">Custom order</button>       <!-- Avoid: use 0 or -1 -->

<!-- Skip links -->
<a href="#main" class="skip-link">Skip to main content</a>
```

---

## 🚀 **HTML5 Features**

### **New Elements**
```html
<main>, <section>, <article>, <aside>, <header>, <footer>, <nav>
<figure><img><figcaption></figure>
<details><summary>Expand</summary><p>Content</p></details>
<time datetime="2024-01-15">Jan 15</time>
<mark>Highlighted text</mark>
```

### **New Input Types**
```html
email, url, tel, search, number, range, date, time, datetime-local, color
```

### **Data Attributes**
```html
<div data-user-id="123" data-role="admin">Content</div>
<!-- Access: element.dataset.userId, element.dataset.role -->
```

### **Template Element**
```html
<template id="card-template">
  <div class="card"><h3></h3><p></p></div>
</template>
<!-- Usage: template.content.cloneNode(true) -->
```

---

## 🎬 **Media Elements**

### **Responsive Images**
```html
<!-- srcset for different densities -->
<img src="image.jpg" srcset="image-320w.jpg 320w, image-640w.jpg 640w" sizes="(max-width: 600px) 320px, 640px" alt="Responsive">

<!-- picture for art direction -->
<picture>
  <source media="(min-width: 800px)" srcset="large.jpg">
  <img src="small.jpg" alt="Responsive image">
</picture>
```

### **Video & Audio**
```html
<video controls>
  <source src="video.mp4" type="video/mp4">
  <source src="video.webm" type="video/webm">
  <track kind="subtitles" src="subtitles.vtt" srclang="en" label="English" default>
  Fallback text
</video>

<audio controls>
  <source src="audio.mp3" type="audio/mpeg">
  Fallback text
</audio>
```

---

## ⚡ **Performance & SEO**

### **Essential Meta Tags**
```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Page Title (50-60 chars)</title>
<meta name="description" content="Description (150-160 chars)">
<link rel="canonical" href="https://example.com/page">
```

### **Open Graph (Social Sharing)**
```html
<meta property="og:type" content="website">
<meta property="og:title" content="Page Title">
<meta property="og:description" content="Description">
<meta property="og:image" content="https://example.com/image.jpg">
<meta property="og:url" content="https://example.com/page">
```

### **Performance Optimization**
```html
<!-- Lazy loading -->
<img src="image.jpg" loading="lazy" alt="Description">

<!-- Preload critical resources -->
<link rel="preload" href="critical.css" as="style">
<link rel="preload" href="hero-image.jpg" as="image" fetchpriority="high">

<!-- Resource hints -->
<link rel="preconnect" href="https://api.example.com">
<link rel="dns-prefetch" href="//fonts.googleapis.com">
```

### **Core Web Vitals**
- **LCP**: Preload LCP image, optimize largest element
- **FID**: Minimize JavaScript execution, use defer/async
- **CLS**: Specify image dimensions, avoid layout shifts

---

## 🎯 **Common Patterns**

### **Navigation**
```html
<nav aria-label="Main navigation">
  <ul><li><a href="/" aria-current="page">Home</a></li></ul>
</nav>
```

### **Modal Dialog**
```html
<div role="dialog" aria-labelledby="modal-title" aria-modal="true" aria-hidden="true" tabindex="-1">
  <h2 id="modal-title">Modal Title</h2>
  <button aria-label="Close dialog">Close</button>
</div>
```

### **Data Table**
```html
<table>
  <caption>Table Title</caption>
  <thead><tr><th scope="col">Header</th></tr></thead>
  <tbody><tr><td>Data</td></tr></tbody>
</table>
```

### **Breadcrumbs**
```html
<nav aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li aria-current="page">Current</li></ol>
</nav>
```

---

## 🔑 **Key Differences**

| Elements | Difference | When to Use |
|----------|------------|-------------|
| `<div>` vs `<section>` | Generic vs thematic | Use `<section>` when you need a heading |
| `<article>` vs `<section>` | Standalone vs grouped | Use `<article>` for complete, distributable content |
| `<strong>` vs `<b>` | Semantic importance vs visual | Use `<strong>` for important text |
| `<em>` vs `<i>` | Semantic emphasis vs visual | Use `<em>` for emphasized text |
| `<header>` vs `<head>` | Visible content vs metadata | `<header>` in body, `<head>` in document head |

---

## ⚠️ **Common Gotchas**

```html
<!-- ❌ Don't skip heading levels -->
<h1>Title</h1><h3>Subtitle</h3>  <!-- Wrong: skipped h2 -->

<!-- ❌ Don't use div for interactive elements -->
<div>Click here</div>  <!-- Wrong: use <button> -->

<!-- ❌ Always provide alt text -->
<img src="image.jpg">  <!-- Wrong: missing alt -->

<!-- ❌ Only one h1 per page -->
<h1>Title 1</h1><h1>Title 2</h1>  <!-- Wrong: multiple h1 -->
```

---

## 🌐 **Browser Rendering Pipeline (Quick)**

**When you type a URL:**

1. **DNS Resolution** → Domain to IP (checks cache first)
2. **TCP/TLS Handshake** → Secure connection (HTTPS)
3. **HTTP Request** → GET request sent
4. **HTTP Response** → HTML received in chunks
5. **HTML Parsing** → Builds DOM tree
6. **CSS Parsing** → Builds CSSOM tree
7. **JavaScript Execution** → Runs scripts (blocks if not async/defer)
8. **Render Tree** → DOM + CSSOM combined
9. **Layout (Reflow)** → Calculate positions/sizes
10. **Paint** → Convert to pixels
11. **Composite** → GPU merges layers
12. **Event Loop** → Handles interactions

**Key**: Blocking resources delay rendering. Use `async`/`defer` for scripts, preload critical resources, lazy load below-fold content.

---

## 🚀 **Interview Quick Tips**

1. **Semantic HTML** → Use elements based on meaning
2. **Accessibility** → WCAG 2.1 AA, proper ARIA, keyboard navigation
3. **SEO** → Meta tags, structured data (JSON-LD), semantic structure
4. **Performance** → Lazy loading, resource hints, Core Web Vitals
5. **Forms** → Proper labels, validation, fieldset/legend
6. **Media** → Responsive images, alt text, captions

---

## 📊 **Quick Stats**

- **Questions**: Q1-Q111 (111 total)
- **Categories**: Fundamentals, Semantic, Forms, Accessibility, HTML5, Media, Performance/SEO, Advanced
- **Key Focus**: Semantic HTML, Accessibility, Performance, SEO

---

**Review Time**: 10-15 minutes | **Focus**: Semantic HTML, Accessibility, Forms, Performance

**Good luck! 🎉**