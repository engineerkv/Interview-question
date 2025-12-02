<div align="center">

**[← Previous: HTML Fundamentals](1%29%20HTML%20Fundamentals.md)** | **[Next: Forms & Input Elements →](3%29%20Forms%20%26%20Input%20Elements.md)**

</div>

# 🏗️ 2. Semantic HTML & Structure (Q16–30)

---

## Q16. 📄 Semantic HTML and its importance

Semantic HTML uses meaningful tags that describe content purpose rather than just appearance - it improves accessibility, SEO, and maintainability by giving meaning to structure. Screen readers use semantic tags to navigate and understand content, and search engines understand content structure better.

- **Trade-offs**: Semantic HTML is about meaning, not just styling - it improves screen reader navigation, SEO rankings, and code maintainability, but requires understanding when to use each semantic element.

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

## Q17. 🤔 `<header>` vs `<h1>`

`<header>` is a semantic container for introductory content that creates a landmark region for screen readers, while `<h1>` is a heading element for the main title. `<header>` can contain multiple elements like title, nav, and logo, and can appear multiple times per page.

- **Trade-offs**: Only one `<h1>` per page for SEO, while `<header>` can appear multiple times - use `<header>` for page or section headers, and `<h1>` for the main page title within the header.

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

## Q18. 🤔 `<article>` vs `<section>`

`<article>` represents complete standalone content that makes sense on its own, while `<section>` represents thematic grouping within a document. `<article>` can contain multiple `<section>` elements, and `<section>` is used when you need a heading for a thematic group.

- **Trade-offs**: Use `<article>` for blog posts, news articles, or any standalone content, and `<section>` for chapters or sections within content - `<article>` is complete content, `<section>` is part of content.

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

## Q19. 💡 Purpose of the `<nav>` element

`<nav>` identifies navigation links and creates a landmark region for screen readers, making it easier for assistive technologies to navigate. Use `aria-label` for descriptive names, and it can appear multiple times per page for main navigation, breadcrumbs, or other navigation links.

- **Trade-offs**: `<nav>` is specifically for navigation links, not just any links - it creates accessible landmarks that improve screen reader navigation, but should only be used for actual navigation sections.

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

## Q20. 🔧 Document outline and how to create it

Use heading elements (`<h1>` to `<h6>`) in proper hierarchical order to create logical document structure - start with `<h1>` for main title, don't skip heading levels. Screen readers use headings for navigation, and proper heading hierarchy helps search engines understand content structure.

- **Trade-offs**: Only one `<h1>` per page for SEO, and heading hierarchy is crucial for accessibility - screen readers use headings for navigation, so skipping levels or improper hierarchy hurts accessibility and SEO.

Example:

```html
<h1>Main Page Title</h1>
  <h2>Section Title</h2>
    <h3>Subsection Title</h3>
    <h3>Another Subsection</h3>
  <h2>Another Section</h2>

```

---

## Q21. 🤔 `<main>` vs `<body>`

`<main>` contains the primary content and creates a landmark region for screen readers, while `<body>` contains all visible content including headers and footers. Use `<main>` to wrap primary content, excluding headers and footers, and only one `<main>` per page.

- **Trade-offs**: `<main>` is a semantic landmark that identifies the main content area for accessibility, while `<body>` is the container for all visible content - use `<main>` to help screen readers quickly navigate to primary content.

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

## Q22. 💡 Purpose of the `<aside>` element

`<aside>` contains content tangentially related to main content, while `<section>` groups thematically related content that's directly part of the main content. Both can have headings and create landmark regions, but `<aside>` is supplementary and `<section>` is part of main content.

- **Trade-offs**: Use `<aside>` for sidebars, ads, or related links that are tangentially related, and `<section>` for content chapters that are directly related - `<aside>` is supplementary, `<section>` is part of main content.

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

## Q23. 🤔 `<figure>` vs `<img>`

`<figure>` represents self-contained content like images or code and groups it with its caption for better accessibility, while `<img>` is just the image element. Screen readers associate the caption with content automatically when using `<figure>` with `<figcaption>`.

- **Trade-offs**: Use `<figure>` for images, code blocks, diagrams, or any content needing a caption - it groups content and caption semantically, improving accessibility and understanding.

Example:

```html
<figure>
  <img src="chart.jpg" alt="Sales data chart">
  <figcaption>Monthly sales data for Q1 2024</figcaption>
</figure>

```

---

## Q24. 💡 Purpose of the `<figcaption>` element

`<figcaption>` provides a caption for `<figure>` content, improving accessibility by associating descriptive text with images, code, or diagrams. Screen readers associate the caption with content automatically, so use descriptive captions that add context, not just repeat alt text.

- **Trade-offs**: `<figcaption>` improves accessibility and understanding by providing context - use it for images, code blocks, diagrams, or any content needing explanation beyond what alt text provides.

Example:

```html
<figure>
  <img src="chart.jpg" alt="Sales data chart">
  <figcaption>Monthly sales data for Q1 2024</figcaption>
</figure>

```

---

## Q25. 🤔 `<time>` vs `<date>`

`<time>` represents dates, times, or durations in machine-readable format - there is no `<date>` element in HTML, so use `<time>` for all date/time needs. Screen readers can announce dates properly with machine-readable format, and it enables date-based search and filtering.

- **Trade-offs**: `<time>` makes dates accessible to both humans and machines - use it for events, articles, schedules, or any time-sensitive content to improve accessibility and enable date-based functionality.

Example:

```html
<time datetime="2024-01-15">January 15, 2024</time>
<time datetime="2024-01-15T14:30:00">2:30 PM</time>
<time datetime="PT2H30M">2 hours 30 minutes</time>

```

---

## Q26. 💡 Purpose of the `<mark>` element

`<mark>` highlights text for reference purposes, like search results or important passages - don't use for emphasis, use `<em>` or `<strong>` instead. Default styling is yellow background, but can be customized with CSS.

- **Trade-offs**: `<mark>` is for highlighting reference, not emphasis - use it for search result highlighting, important passages, or reference notes, but use `<em>` or `<strong>` for emphasis.

Example:

```html
<p>Search results for <mark>JavaScript</mark> programming</p>
<p>This is <mark>highlighted text</mark> for emphasis</p>

```

---

## Q27. 💡 Landmark regions and landmark roles and their usage

Use semantic HTML5 elements and ARIA landmark roles to create navigable regions for screen readers - semantic elements automatically create landmarks, and ARIA roles provide explicit landmark identification when needed. Screen readers navigate by landmarks, which improves user experience.

- **Trade-offs**: Use semantic elements first (they have implicit landmark roles), add ARIA roles only when needed - only one banner, main, and contentinfo per page, while navigation can appear multiple times. Landmarks enable quick navigation for screen reader users.

Example:

```html
<body>
  <header role="banner">Site header</header>
  <nav role="navigation" aria-label="Main navigation">
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/about">About</a></li>
    </ul>
  </nav>
  <main role="main">Main content</main>
  <aside role="complementary">Sidebar</aside>
  <footer role="contentinfo">Site footer</footer>
</body>

```

---

## Q28. 🤔 `<address>` vs `<footer>`

`<address>` contains contact information for the nearest article or body, while `<footer>` contains footer content for its nearest sectioning element - both can appear multiple times but serve different semantic purposes. Use `<address>` for author contact information, and `<footer>` for site-wide footer content.

- **Trade-offs**: `<address>` is semantic for contact info, while `<footer>` is for footer sections - use `<address>` for contact information within articles, and `<footer>` for footer sections like copyright or site navigation.

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

## Q29. 💡 Purpose of the `<details>` and `<summary>` elements

`<details>` creates a disclosure widget that can be expanded or collapsed, while `<summary>` provides the visible summary text - it's a native HTML solution that's accessible by default, perfect for collapsible content without JavaScript. Use for progressive disclosure of information.

- **Trade-offs**: `<details>` and `<summary>` provide native collapsible content that's accessible by default - use them for FAQs, collapsible sections, or any expandable content where you want progressive disclosure.

Example:

```html
<details>
  <summary>Click to expand</summary>
  <p>Hidden content that appears when expanded...</p>
</details>

```

---

## Q30. 💡 Creating a proper document structure

Use semantic HTML5 elements, proper heading hierarchy, and landmark regions to create a logical document structure that's accessible and SEO-friendly. Start with DOCTYPE, use semantic elements instead of generic divs, and maintain proper heading hierarchy.

- **Trade-offs**: Proper document structure improves accessibility, SEO, and maintainability - semantic structure helps search engines understand content, and proper heading hierarchy and landmark regions improve accessibility for screen reader users.

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

<div align="center">

**[← Previous: HTML Fundamentals](1%29%20HTML%20Fundamentals.md)** | **[Next: Forms & Input Elements →](3%29%20Forms%20%26%20Input%20Elements.md)**

</div>
