# 2. Semantic HTML & Structure (Q16–30)

---

## Q16. What is semantic HTML and why is it important?

Semantic HTML uses meaningful tags that describe content purpose - it improves accessibility, SEO, and maintainability by giving meaning to structure. Use tags that describe content meaning, not just appearance.

- **Trade-offs**: The catch is screen readers use semantic tags to navigate and understand content - search engines understand content structure better with semantic HTML. Semantic HTML is about meaning, not just styling, but watch out - it improves screen reader navigation, SEO, and code maintainability.

Example:

```html
<article>
  <header>
    <h1>Article Title</h1>
    <time datetime="2024-01-15">Jan 15</time>
  </header>
  <p>Article content here...</p>
</article>
```

---

## Q17. What is the difference between `<header>` and `<h1>`?

`<header>` is a semantic container for introductory content, while `<h1>` is a heading element for the main title - `<header>` creates landmark region for screen readers. `<header>` is a container, `<h1>` is a heading element.

- **Trade-offs**: The catch is `<header>` creates landmark region for screen readers - only one `<h1>` per page for SEO, `<header>` can appear multiple times. `<header>` is a section, `<h1>` is a heading level, but watch out - `<header>` can contain multiple elements (title, nav, logo), `<h1>` is just the heading.

Example:

```html
<header>
  <h1>Main Page Title</h1>
  <nav>
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/about">About</a></li>
    </ul>
  </nav>
</header>
```

---

## Q18. What is the difference between `<article>` and `<section>`?

`<article>` represents complete standalone content, while `<section>` represents thematic grouping within a document - `<article>` can contain multiple `<section>` elements. `<article>` should make sense on its own, `<section>` groups related content.

- **Trade-offs**: The catch is `<article>` can contain multiple `<section>` elements - use `<section>` when you need a heading for a thematic group. `<article>` is complete content, `<section>` is part of content, but watch out - `<article>` for blog posts, news articles; `<section>` for chapters or sections within content.

Example:

```html
<main>
  <article>
    <h1>Blog Post Title</h1>
    <section>
      <h2>Introduction</h2>
      <p>Post introduction...</p>
    </section>
  </article>
</main>
```

---

## Q19. What is the purpose of the `<nav>` element?

`<nav>` identifies navigation links and creates a landmark region for screen readers - use `aria-label` for descriptive names, can appear multiple times per page. Identify navigation links and create accessible landmarks.

- **Trade-offs**: The catch is creates landmark region for screen reader navigation - use `aria-label` for descriptive names, can appear multiple times per page. `<nav>` is for navigation, not just any links, but watch out - good for main navigation, breadcrumbs, or any navigation links.

Example:

```html
<nav aria-label="Main navigation">
  <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/about">About</a></li>
  </ul>
</nav>
```

---

## Q20. What is the document outline and how do you create it?

Use heading elements (`<h1>` to `<h6>`) in proper hierarchical order to create logical document structure - screen readers use headings for navigation. Start with `<h1>` for main title, don't skip heading levels.

- **Trade-offs**: The catch is proper heading hierarchy helps search engines understand content structure - only one `<h1>` per page, use headings to create document outline. Heading hierarchy is crucial for accessibility and SEO, but watch out - screen readers use headings for navigation, improves accessibility.

Example:

```html
<h1>Main Page Title</h1>
  <h2>Section Title</h2>
    <h3>Subsection Title</h3>
    <h3>Another Subsection</h3>
  <h2>Another Section</h2>
```

---

## Q21. What is the difference between `<main>` and `<body>`?

`<main>` contains the primary content, while `<body>` contains all visible content including headers and footers - `<main>` creates landmark region for screen readers. `<main>` is primary content only, `<body>` is all visible content.

- **Trade-offs**: The catch is `<main>` creates landmark region for screen readers - use `<main>` to wrap primary content, exclude headers and footers. `<main>` is a semantic landmark, `<body>` is the container, but watch out - `<main>` identifies main content area, only one per page.

Example:

```html
<body>
  <header>Site header</header>
  <main>
    <h1>Page Title</h1>
    <p>Main content...</p>
  </main>
  <footer>Site footer</footer>
</body>
```

---

## Q22. What is the purpose of the `<aside>` element?

`<aside>` contains content tangentially related to main content, while `<section>` groups thematically related content - `<aside>` is supplementary, `<section>` is part of main content. `<aside>` is supplementary content, `<section>` is thematically grouped content.

- **Trade-offs**: The catch is `<aside>` is tangentially related, `<section>` is directly related - both can have headings, both create landmark regions. `<aside>` is supplementary, `<section>` is part of main content, but watch out - `<aside>` for sidebars, ads, related links; `<section>` for content chapters.

Example:

```html
<main>
  <article>
    <h1>Article Title</h1>
    <p>Main content...</p>
  </article>
  <aside>
    <h2>Related Articles</h2>
    <p>Sidebar content...</p>
  </aside>
</main>
```

---

## Q23. What is the difference between `<figure>` and `<img>`?

`<figure>` represents self-contained content like images or code, while `<img>` is just the image element - `<figure>` groups content with its caption for better accessibility. Group content with its caption for better accessibility.

- **Trade-offs**: The catch is screen readers associate caption with content - use `<figcaption>` for descriptive captions, improves understanding. `<figure>` groups content and caption semantically, but watch out - good for images, code blocks, diagrams, or any content needing a caption.

Example:

```html
<figure>
  <img src="chart.jpg" alt="Sales data chart">
  <figcaption>Monthly sales data for Q1 2024</figcaption>
</figure>
```

---

## Q24. What is the purpose of the `<figcaption>` element?

`<figcaption>` provides a caption for `<figure>` content - it improves accessibility by associating descriptive text with images, code, or diagrams. Provides descriptive caption for figure content.

- **Trade-offs**: The catch is screen readers associate caption with content automatically - use descriptive captions that add context, not just repeat alt text. `<figcaption>` improves accessibility and understanding, but watch out - good for images, code blocks, diagrams, or any content needing explanation.

Example:

```html
<figure>
  <img src="chart.jpg" alt="Sales data chart">
  <figcaption>Monthly sales data for Q1 2024</figcaption>
</figure>
```

---

## Q25. What is the difference between `<time>` and `<date>`?

`<time>` represents dates, times, or durations in machine-readable format - there is no `<date>` element in HTML, use `<time>` for all date/time needs. Provide machine-readable dates and times for better accessibility and SEO.

- **Trade-offs**: The catch is screen readers can announce dates properly with machine-readable format - enables date-based search and filtering. `<time>` makes dates accessible to both humans and machines, but watch out - good for events, articles, schedules, or any time-sensitive content.

Example:

```html
<time datetime="2024-01-15">January 15, 2024</time>
<time datetime="2024-01-15T14:30:00">2:30 PM</time>
<time datetime="PT2H30M">2 hours 30 minutes</time>
```

---

## Q26. What is the purpose of the `<mark>` element?

`<mark>` highlights text for reference purposes, like search results or important passages - don't use for emphasis, use `<em>` or `<strong>` instead. Highlight text for reference, not for emphasis.

- **Trade-offs**: The catch is default styling is yellow background, can be customized with CSS - don't use for emphasis (use `<em>` or `<strong>` instead). `<mark>` is for highlighting reference, not emphasis, but watch out - good for search result highlighting, important passages, or reference notes.

Example:

```html
<p>Search results for <mark>JavaScript</mark> programming</p>
<p>This is <mark>highlighted text</mark> for emphasis</p>
```

---

## Q27. What are landmark regions and how do you use them?

Use semantic HTML5 elements and ARIA landmarks to create navigable regions for screen readers - semantic elements automatically create landmarks. Create navigable regions for screen readers using semantic elements.

- **Trade-offs**: The catch is screen readers navigate by landmarks, improves user experience - use semantic elements first, add ARIA roles only when needed. Landmarks enable screen reader navigation, but watch out - semantic elements automatically create landmarks, use ARIA roles if needed.

Example:

```html
<body>
  <header role="banner">Site header</header>
  <nav role="navigation" aria-label="Main navigation">Nav</nav>
  <main role="main">Main content</main>
  <aside role="complementary">Sidebar</aside>
  <footer role="contentinfo">Site footer</footer>
</body>
```

---

## Q28. What is the difference between `<address>` and `<footer>`?

`<address>` contains contact information for the nearest article or body, while `<footer>` contains footer content for its nearest sectioning element - both have different semantic purposes. `<address>` is for contact information, `<footer>` is for footer content.

- **Trade-offs**: The catch is both can appear multiple times, but serve different purposes - `<address>` is semantic for contact info, `<footer>` is for footer sections. `<address>` is for contact info, `<footer>` is for footer sections, but watch out - `<address>` for author contact, `<footer>` for site-wide footer content.

Example:

```html
<article>
  <h1>Article Title</h1>
  <p>Content...</p>
  <address>
    Contact: <a href="mailto:author@example.com">author@example.com</a>
  </address>
</article>
<footer>
  <p>&copy; 2024 Company Name</p>
</footer>
```

---

## Q29. What is the purpose of the `<details>` and `<summary>` elements?

`<details>` creates a disclosure widget that can be expanded or collapsed, while `<summary>` provides the visible summary text - perfect for collapsible content. Creates interactive disclosure widget without JavaScript.

- **Trade-offs**: The catch is native HTML solution, accessible by default - use for progressive disclosure of information. `<details>` and `<summary>` provide native collapsible content, but watch out - good for FAQs, collapsible sections, or any expandable content.

Example:

```html
<details>
  <summary>Click to expand</summary>
  <p>Hidden content that appears when expanded...</p>
</details>
```

---

## Q30. How do you create a proper document structure?

Use semantic HTML5 elements, proper heading hierarchy, and landmark regions to create a logical document structure that's accessible and SEO-friendly. Use semantic elements for structure, not generic divs.

- **Trade-offs**: The catch is semantic structure helps search engines understand content - start with DOCTYPE, use semantic elements, maintain heading hierarchy. Proper document structure improves accessibility, SEO, and maintainability, but watch out - proper heading hierarchy and landmark regions improve accessibility.

Example:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Page Title</title>
  </head>
  <body>
    <header>
      <h1>Site Title</h1>
      <nav>Navigation</nav>
    </header>
    <main>
      <article>
        <h2>Article Title</h2>
        <p>Content...</p>
      </article>
    </main>
    <footer>Footer</footer>
  </body>
</html>
```

---
