# 🏗️ 2. Semantic HTML & Structure (Q16–30)

---

## 16) What is semantic HTML and why is it important?

Concept:
Semantic HTML uses meaningful tags that describe content purpose, improving accessibility, SEO, and maintainability.

Example:
```html
<article>
  <header>
    <h1>Article Title</h1>
    <time datetime="2024-01-15">January 15, 2024</time>
  </header>
  <main>
```

Deep Insight:
- Improves screen reader navigation
- Enhances SEO through content structure
- Makes code more maintainable and readable
- Provides better browser default styling
- Enables better CSS targeting and styling

---

## 17) What is the difference between `<header>` and `<h1>`?

Concept:
`<header>` is a semantic container for introductory content; `<h1>` is a heading element for the main title.

Example:
```html
<header>
  <h1>Main Page Title</h1>
  <nav>
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/about">About</a></li>
```

Deep Insight:
- `<header>` can contain multiple elements (title, nav, logo)
- `<h1>` is specifically for the main heading
- `<header>` is a landmark for screen readers
- Only one `<h1>` per page for SEO
- `<header>` can appear multiple times per page

---

## 18) What are the main semantic sectioning elements in HTML5?

Concept:
HTML5 introduced semantic elements that define document structure: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, and `<footer>`.

Example:
```html
<body>
  <header>Site header</header>
  <nav>Navigation menu</nav>
  <main>
    <article>
      <section>Article section 1</section>
```

Deep Insight:
- Each element has specific semantic meaning
- Improves document outline and accessibility
- Helps search engines understand content structure
- Provides better default styling
- Creates landmark regions for screen readers

---

## 19) When should you use `<article>` vs `<section>`?

Concept:
`<article>` represents complete, standalone content; `<section>` represents thematic grouping within a document.

Example:
```html
<main>
  <article>
    <h1>Blog Post Title</h1>
    <section>
      <h2>Introduction</h2>
      <p>Post introduction...</p>
```

Deep Insight:
- `<article>` should make sense on its own
- `<section>` groups related content together
- `<article>` can contain multiple `<section>` elements
- Use `<section>` when you need a heading
- Both improve document structure and accessibility

---

## 20) What is the purpose of the `<nav>` element?

Concept:
`<nav>` identifies navigation links and creates a landmark region for screen readers.

Example:
```html
<nav aria-label="Main navigation">
  <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/about">About</a></li>
    <li><a href="/contact">Contact</a></li>
  </ul>
```

Deep Insight:
- Should contain navigation links only
- Creates landmark for screen reader navigation
- Use `aria-label` for descriptive names
- Can appear multiple times per page
- Improves keyboard navigation

---

## 21) How do you create a proper document outline with heading hierarchy?

Concept:
Use heading elements (`<h1>` to `<h6>`) in proper hierarchical order to create a logical document structure.

Example:
```html
<h1>Main Page Title</h1>
  <h2>Section Title</h2>
    <h3>Subsection Title</h3>
    <h3>Another Subsection</h3>
  <h2>Another Section</h2>
    <h3>Subsection</h3>
```

Deep Insight:
- Start with `<h1>` for main page title
- Don't skip heading levels (h1 → h3 is wrong)
- Only one `<h1>` per page
- Use headings to create document outline
- Screen readers use headings for navigation

---

## 22) What is the difference between `<main>` and `<body>`?

Concept:
`<main>` contains the primary content of the page; `<body>` contains all visible content including headers and footers.

Example:
```html
<body>
  <header>Site header</header>
  <nav>Navigation</nav>
  <main>
    <h1>Page Title</h1>
    <p>Main content goes here...</p>
```

Deep Insight:
- `<main>` identifies primary content area
- Only one `<main>` per page
- `<body>` contains all visible content
- `<main>` creates landmark for screen readers
- Improves content structure and accessibility

---

## 23) When should you use `<aside>` vs `<section>`?

Concept:
`<aside>` contains content tangentially related to main content; `<section>` groups thematically related content.

Example:
```html
<main>
  <article>
    <h1>Article Title</h1>
    <p>Main article content...</p>
  </article>
  <aside>
```

Deep Insight:
- `<aside>` is for tangential/supplementary content
- `<section>` is for thematically grouped content
- `<aside>` often contains sidebars, ads, related links
- Both can have headings
- `<aside>` creates landmark region

---

## 24) What is the purpose of the `<figure>` and `<figcaption>` elements?

Concept:
`<figure>` represents self-contained content like images or code; `<figcaption>` provides a caption for the figure.

Example:
```html
<figure>
  <img src="chart.jpg" alt="Sales data chart">
  <figcaption>Monthly sales data for Q1 2024</figcaption>
</figure>

<figure>
```

Deep Insight:
- `<figure>` groups content with its caption
- `<figcaption>` provides description for the figure
- Improves accessibility for images and code
- Can contain images, code, diagrams, etc.
- Screen readers associate caption with content

---

## 25) How do you create proper heading structure for accessibility?

Concept:
Use heading hierarchy to create logical document structure that screen readers can navigate.

Example:
```html
<h1>Page Title</h1>
  <h2>Main Section</h2>
    <h3>Subsection</h3>
    <h3>Another Subsection</h3>
  <h2>Another Main Section</h2>
    <h3>Subsection</h3>
```

Deep Insight:
- Start with `<h1>` for page title
- Don't skip heading levels
- Use only one `<h1>` per page
- Headings create document outline
- Screen readers use headings for navigation

---

## 26) What is the difference between `<header>` and `<head>`?

Concept:
`<head>` contains metadata not displayed on page; `<header>` contains visible introductory content.

Example:
```html
<head>
  <title>Page Title</title>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
```

Deep Insight:
- `<head>` is in document head, not visible
- `<header>` is in document body, visible content
- `<head>` contains metadata, scripts, styles
- `<header>` contains introductory content
- Both serve different purposes in document structure

---

## 27) When should you use `<time>` element?

Concept:
`<time>` represents specific dates, times, or durations in a machine-readable format.

Example:
```html
<time datetime="2024-01-15">January 15, 2024</time>
<time datetime="2024-01-15T14:30:00">2:30 PM</time>
<time datetime="PT2H30M">2 hours 30 minutes</time>
<time datetime="2024-01-15" pubdate>Published on January 15</time>
```

Deep Insight:
- `datetime` attribute provides machine-readable format
- Improves SEO and accessibility
- Enables date-based search and filtering
- Screen readers can announce dates properly
- Useful for events, articles, and schedules

---

## 28) What is the purpose of the `<mark>` element?

Concept:
`<mark>` highlights text for reference purposes, like search results or important passages.

Example:
```html
<p>Search results for <mark>JavaScript</mark> programming</p>
<p>This is <mark>highlighted text</mark> for emphasis</p>
<p>Remember to <mark>save your work</mark> frequently</p>
```

Deep Insight:
- Used for highlighting, not emphasis
- Default styling is yellow background
- Useful for search result highlighting
- Don't use for emphasis (use `<em>` or `<strong>`)
- Improves user experience in search contexts

---

## 29) How do you create proper landmark regions?

Concept:
Use semantic HTML5 elements and ARIA landmarks to create navigable regions for screen readers.

Example:
```html
<body>
  <header role="banner">Site header</header>
  <nav role="navigation" aria-label="Main navigation">Nav</nav>
  <main role="main">Main content</main>
  <aside role="complementary">Sidebar</aside>
  <footer role="contentinfo">Site footer</footer>
```

Deep Insight:
- Semantic elements create automatic landmarks
- Use ARIA roles for additional landmarks
- Screen readers navigate by landmarks
- Improves accessibility and user experience
- Follow landmark hierarchy best practices

---

## 30) What are the benefits of using semantic HTML for SEO?

Concept:
Semantic HTML helps search engines understand content structure and importance, improving search rankings.

Example:
```html
<article itemscope itemtype="http://schema.org/Article">
  <header>
    <h1 itemprop="headline">Article Title</h1>
    <time itemprop="datePublished" datetime="2024-01-15">Jan 15, 2024</time>
  </header>
  <main itemprop="articleBody">
```

Deep Insight:
- Search engines understand content hierarchy
- Semantic elements improve content indexing
- Structured data enhances search results
- Better user experience improves rankings
- Semantic HTML is future-proof for SEO
