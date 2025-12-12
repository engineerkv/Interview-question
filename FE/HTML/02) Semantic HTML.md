# 🏗️ 2. Semantic HTML (Q16–26)

---

## 📍 Navigation

<div align="center">

[← Previous: Fundamentals & Basics](01%29%20Fundamentals%20%26%20Basics.md) • [Home: README](../README.md) • [Next: Forms & Inputs →](03%29%20Forms%20%26%20Inputs.md)

[📋 Cheatsheet](HTML%20Interview%20Cheatsheet.md)

</div>

---

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

## Q20. 🤔 `<main>` vs `<body>`

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

## Q21. 💡 Purpose of the `<aside>` element

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

## Q22. 🤔 `<figure>` vs `<img>`

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

## Q23. 💡 Purpose of the `<figcaption>` element

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

## Q24. 💡 Purpose of the `<mark>` element

`<mark>` highlights text for reference purposes, like search results or important passages - don't use for emphasis, use `<em>` or `<strong>` instead. Default styling is yellow background, but can be customized with CSS.

- **Trade-offs**: `<mark>` is for highlighting reference, not emphasis - use it for search result highlighting, important passages, or reference notes, but use `<em>` or `<strong>` for emphasis.

Example:

```html
<p>Search results for <mark>JavaScript</mark> programming</p>
<p>This is <mark>highlighted text</mark> for emphasis</p>

```

---

## Q25. 💡 Landmark regions and landmark roles and their usage

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

## Q26. 💡 Purpose of the `<details>` and `<summary>` elements

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

---

## 📍 Navigation

<div align="center">

[← Previous: Fundamentals & Basics](01%29%20Fundamentals%20%26%20Basics.md) • [Home: README](../README.md) • [Next: Forms & Inputs →](03%29%20Forms%20%26%20Inputs.md)

[📋 Cheatsheet](HTML%20Interview%20Cheatsheet.md)

</div>

---
