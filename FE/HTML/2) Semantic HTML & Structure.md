# 🏗️ 2. Semantic HTML & Structure (Q16–30)

---

## 16) What is semantic HTML and why is it important?

Semantic HTML uses meaningful tags that describe content purpose. It improves accessibility, SEO, and maintainability.

```html
<article>
  <header><h1>Article Title</h1><time datetime="2024-01-15">Jan 15</time></header>
  <p>Article content here...</p>
</article>
```

- **Core Purpose**: Use tags that describe content meaning, not just appearance
- **Real-World Benefits**: Improves screen reader navigation, SEO, and code maintainability
- **Accessibility**: Screen readers use semantic tags to navigate and understand content
- **SEO Impact**: Search engines understand content structure better with semantic HTML
- **Interview Tip**: Explain that semantic HTML is about meaning, not just styling

---

## 17) What is the difference between `<header>` and `<h1>`?

`<header>` is a semantic container for introductory content. `<h1>` is a heading element for the main title.

```html
<header>
  <h1>Main Page Title</h1>
  <nav><ul><li><a href="/">Home</a></li><li><a href="/about">About</a></li></ul></nav>
</header>
```

- **Core Difference**: `<header>` is a container, `<h1>` is a heading element
- **Real-World Use**: `<header>` can contain multiple elements (title, nav, logo), `<h1>` is just the heading
- **Accessibility**: `<header>` creates landmark region for screen readers
- **SEO Rule**: Only one `<h1>` per page for SEO, `<header>` can appear multiple times
- **Interview Tip**: Explain that `<header>` is a section, `<h1>` is a heading level

---

## 18) What are the main semantic sectioning elements in HTML5?

HTML5 introduced semantic elements: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, and `<footer>`.

```html
<body>
  <header>Site header</header>
  <main>
    <article><section>Article section</section></article>
    <aside>Sidebar</aside>
  </main>
  <footer>Site footer</footer>
</body>
```

- **Core Elements**: Each element has specific semantic meaning for document structure
- **Real-World Use**: Improves document outline, accessibility, and SEO
- **Landmark Regions**: Creates navigable regions for screen readers
- **Search Engines**: Helps search engines understand content structure
- **Interview Tip**: Explain that semantic elements replace generic divs with meaning

---

## 19) When should you use `<article>` vs `<section>`?

`<article>` represents complete standalone content. `<section>` represents thematic grouping within a document.

```html
<main>
  <article>
    <h1>Blog Post Title</h1>
    <section><h2>Introduction</h2><p>Post introduction...</p></section>
  </article>
</main>
```

- **Core Rule**: `<article>` should make sense on its own, `<section>` groups related content
- **Real-World Use**: `<article>` for blog posts, news articles; `<section>` for chapters or sections within content
- **Composition**: `<article>` can contain multiple `<section>` elements
- **Best Practice**: Use `<section>` when you need a heading for a thematic group
- **Interview Tip**: Explain that `<article>` is complete content, `<section>` is part of content

---

## 20) What is the purpose of the `<nav>` element?

`<nav>` identifies navigation links and creates a landmark region for screen readers.

```html
<nav aria-label="Main navigation">
  <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/about">About</a></li>
  </ul>
</nav>
```

- **Core Purpose**: Identify navigation links and create accessible landmarks
- **Real-World Use**: Main navigation, breadcrumbs, or any navigation links
- **Accessibility**: Creates landmark region for screen reader navigation
- **Best Practice**: Use `aria-label` for descriptive names, can appear multiple times per page
- **Interview Tip**: Explain that `<nav>` is for navigation, not just any links

---

## 21) How do you create a proper document outline with heading hierarchy?

Use heading elements (`<h1>` to `<h6>`) in proper hierarchical order to create logical document structure.

```html
<h1>Main Page Title</h1>
  <h2>Section Title</h2>
    <h3>Subsection Title</h3>
    <h3>Another Subsection</h3>
  <h2>Another Section</h2>
```

- **Core Rule**: Start with `<h1>` for main title, don't skip heading levels
- **Real-World Impact**: Screen readers use headings for navigation, improves accessibility
- **SEO Benefit**: Proper heading hierarchy helps search engines understand content structure
- **Best Practice**: Only one `<h1>` per page, use headings to create document outline
- **Interview Tip**: Explain that heading hierarchy is crucial for accessibility and SEO

---

## 22) What is the difference between `<main>` and `<body>`?

`<main>` contains the primary content. `<body>` contains all visible content including headers and footers.

```html
<body>
  <header>Site header</header>
  <main><h1>Page Title</h1><p>Main content...</p></main>
  <footer>Site footer</footer>
</body>
```

- **Core Difference**: `<main>` is primary content only, `<body>` is all visible content
- **Real-World Use**: `<main>` identifies main content area, only one per page
- **Accessibility**: `<main>` creates landmark region for screen readers
- **Best Practice**: Use `<main>` to wrap primary content, exclude headers and footers
- **Interview Tip**: Explain that `<main>` is a semantic landmark, `<body>` is the container

---

## 23) When should you use `<aside>` vs `<section>`?

`<aside>` contains content tangentially related to main content. `<section>` groups thematically related content.

```html
<main>
  <article><h1>Article Title</h1><p>Main content...</p></article>
  <aside><h2>Related Articles</h2><p>Sidebar content...</p></aside>
</main>
```

- **Core Difference**: `<aside>` is supplementary content, `<section>` is thematically grouped content
- **Real-World Use**: `<aside>` for sidebars, ads, related links; `<section>` for content chapters
- **Semantic Meaning**: `<aside>` is tangentially related, `<section>` is directly related
- **Both Can Have Headings**: Both can have headings, both create landmark regions
- **Interview Tip**: Explain that `<aside>` is supplementary, `<section>` is part of main content

---

## 24) What is the purpose of the `<figure>` and `<figcaption>` elements?

`<figure>` represents self-contained content like images or code. `<figcaption>` provides a caption.

```html
<figure>
  <img src="chart.jpg" alt="Sales data chart">
  <figcaption>Monthly sales data for Q1 2024</figcaption>
</figure>
```

- **Core Purpose**: Group content with its caption for better accessibility
- **Real-World Use**: Images, code blocks, diagrams, or any content needing a caption
- **Accessibility**: Screen readers associate caption with content
- **Best Practice**: Use `<figcaption>` for descriptive captions, improves understanding
- **Interview Tip**: Explain that `<figure>` groups content and caption semantically

---

## 25) How do you create proper heading structure for accessibility?

Use heading hierarchy to create logical document structure that screen readers can navigate.

```html
<h1>Page Title</h1>
  <h2>Main Section</h2>
    <h3>Subsection</h3>
    <h3>Another Subsection</h3>
  <h2>Another Main Section</h2>
```

- **Core Rule**: Start with `<h1>`, don't skip levels, maintain hierarchy
- **Real-World Impact**: Screen readers use headings for navigation, improves accessibility
- **SEO Benefit**: Proper hierarchy helps search engines understand content structure
- **Best Practice**: Only one `<h1>` per page, use headings logically
- **Interview Tip**: Explain that heading hierarchy enables screen reader navigation

---

## 26) What is the difference between `<header>` and `<head>`?

`<head>` contains metadata not displayed on page. `<header>` contains visible introductory content.

```html
<head><title>Page Title</title><meta charset="UTF-8"></head>
<body><header><h1>Page Title</h1></header></body>
```

- **Core Difference**: `<head>` is metadata in document head, `<header>` is visible content in body
- **Real-World Use**: `<head>` for metadata, scripts, styles; `<header>` for visible page header
- **Location**: `<head>` is in document head, `<header>` is in document body
- **Purpose**: `<head>` is for browser/search engines, `<header>` is for users
- **Interview Tip**: Explain that `<head>` is metadata, `<header>` is visible content

---

## 27) When should you use `<time>` element?

`<time>` represents dates, times, or durations in machine-readable format.

```html
<time datetime="2024-01-15">January 15, 2024</time>
<time datetime="2024-01-15T14:30:00">2:30 PM</time>
<time datetime="PT2H30M">2 hours 30 minutes</time>
```

- **Core Purpose**: Provide machine-readable dates and times for better accessibility and SEO
- **Real-World Use**: Events, articles, schedules, or any time-sensitive content
- **Accessibility**: Screen readers can announce dates properly with machine-readable format
- **SEO Benefit**: Enables date-based search and filtering
- **Interview Tip**: Explain that `<time>` makes dates accessible to both humans and machines

---

## 28) What is the purpose of the `<mark>` element?

`<mark>` highlights text for reference purposes, like search results or important passages.

```html
<p>Search results for <mark>JavaScript</mark> programming</p>
<p>This is <mark>highlighted text</mark> for emphasis</p>
```

- **Core Purpose**: Highlight text for reference, not for emphasis
- **Real-World Use**: Search result highlighting, important passages, or reference notes
- **Visual Styling**: Default styling is yellow background, can be customized with CSS
- **Semantic Note**: Don't use for emphasis (use `<em>` or `<strong>` instead)
- **Interview Tip**: Explain that `<mark>` is for highlighting reference, not emphasis

---

## 29) How do you create proper landmark regions?

Use semantic HTML5 elements and ARIA landmarks to create navigable regions for screen readers.

```html
<body>
  <header role="banner">Site header</header>
  <nav role="navigation" aria-label="Main navigation">Nav</nav>
  <main role="main">Main content</main>
  <aside role="complementary">Sidebar</aside>
  <footer role="contentinfo">Site footer</footer>
</body>
```

- **Core Purpose**: Create navigable regions for screen readers using semantic elements
- **Real-World Use**: Semantic elements automatically create landmarks, use ARIA roles if needed
- **Accessibility**: Screen readers navigate by landmarks, improves user experience
- **Best Practice**: Use semantic elements first, add ARIA roles only when needed
- **Interview Tip**: Explain that landmarks enable screen reader navigation

---

## 30) What are the benefits of using semantic HTML for SEO?

Semantic HTML helps search engines understand content structure and importance, improving search rankings.

```html
<article itemscope itemtype="http://schema.org/Article">
  <header><h1 itemprop="headline">Article Title</h1><time itemprop="datePublished" datetime="2024-01-15">Jan 15</time></header>
  <div itemprop="articleBody"><p>Article content...</p></div>
</article>
```

- **Core Benefit**: Search engines understand content hierarchy and structure better
- **Real-World Impact**: Improves content indexing and search result display
- **Structured Data**: Semantic HTML works with structured data for rich results
- **User Experience**: Better structure improves user experience, which improves rankings
- **Interview Tip**: Explain that semantic HTML is future-proof for SEO

---
