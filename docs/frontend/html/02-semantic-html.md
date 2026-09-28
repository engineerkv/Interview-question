---
sidebar_label: "Semantic HTML"
---
# 🏗️ 2. Semantic HTML (Q16–26)

---

## Q16. 📄 Semantic HTML and its importance

Semantic HTML uses meaningful tags that describe content purpose rather than just appearance - it improves accessibility, SEO, and maintainability by giving meaning to structure. When you use semantic tags, screen readers can navigate and understand content better, and search engines understand content structure better.

- **Trade-offs**: The catch is semantic HTML is about meaning, not just styling - it improves screen reader navigation, SEO rankings, and code maintainability, but you need to understand when to use each semantic element.

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

`<header>` is a semantic container for introductory content that creates a landmark region for screen readers, while `<h1>` is a heading element for the main title. You can put multiple elements like title, nav, and logo inside `<header>`, and you can use it multiple times per page.

- **Trade-offs**: The catch is only one `<h1>` per page for SEO, while `<header>` can appear multiple times - use `<header>` for page or section headers, and `<h1>` for the main page title within the header.

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

`<article>` is for complete standalone content that makes sense on its own, while `<section>` is for thematic grouping within a document. You can put multiple `<section>` elements inside `<article>`, and use `<section>` when you need a heading for a thematic group.

- **Trade-offs**: The catch is `<article>` works great for blog posts, news articles, or any standalone content, while `<section>` is for chapters or sections within content - `<article>` is complete content, `<section>` is part of content.

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

`<nav>` identifies navigation links and creates a landmark region for screen readers, making it easier for assistive technologies to navigate. Use `aria-label` for descriptive names, and you can use it multiple times per page for main navigation, breadcrumbs, or other navigation links.

- **Trade-offs**: The catch is `<nav>` is specifically for navigation links, not just any links - it creates accessible landmarks that improve screen reader navigation, but you should only use it for actual navigation sections.

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

- **Trade-offs**: The catch is `<main>` is a semantic landmark that identifies the main content area for accessibility, while `<body>` is the container for all visible content - use `<main>` to help screen readers quickly navigate to primary content.

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

`<aside>` is for content that's related but not essential to the main content - like sidebars, ads, or related links. It's supplementary content, while `<section>` groups content that's directly part of the main flow. Both can have headings and create landmark regions for screen readers.

- **Trade-offs**: The catch is `<aside>` works great for sidebars, ads, or related links that are tangentially related, while `<section>` is for content chapters that are directly part of the main content - `<aside>` is supplementary, `<section>` is part of main content.

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

## Q22. 🤔 When to use `<figure>` vs `<img>`?

`<figure>` groups self-contained content like images or code with its caption for better accessibility, while `<img>` is just the image element. When you use `<figure>` with `<figcaption>`, screen readers automatically associate the caption with the content.

- **Trade-offs**: The catch is `<figure>` works great for images, code blocks, diagrams, or any content needing a caption - it groups content and caption semantically, which improves accessibility and understanding.

Example:

```html
<figure>
  <img src="chart.jpg" alt="Sales data chart">
  <figcaption>Monthly sales data for Q1 2024</figcaption>
</figure>

```

---

## Q23. 💡 Purpose of the `<figcaption>` element

`<figcaption>` provides a caption for `<figure>` content, improving accessibility by associating descriptive text with images, code, or diagrams. When you use it, screen readers automatically associate the caption with content, so use descriptive captions that add context, not just repeat alt text.

- **Trade-offs**: The catch is `<figcaption>` improves accessibility and understanding by providing context - use it for images, code blocks, diagrams, or any content needing explanation beyond what alt text provides.

Example:

```html
<figure>
  <img src="chart.jpg" alt="Sales data chart">
  <figcaption>Monthly sales data for Q1 2024</figcaption>
</figure>

```

---

## Q24. 💡 Purpose of the `<mark>` element

`<mark>` highlights text for reference purposes, like search results or important passages - don't use it for emphasis, use `<em>` or `<strong>` instead. Default styling is yellow background, but you can customize it with CSS.

- **Trade-offs**: The catch is `<mark>` is for highlighting reference, not emphasis - use it for search result highlighting, important passages, or reference notes, but use `<em>` or `<strong>` for emphasis.

Example:

```html
<p>Search results for <mark>JavaScript</mark> programming</p>
<p>This is <mark>highlighted text</mark> for emphasis</p>

```

---

## Q25. 💡 Landmark regions and landmark roles and their usage

Use semantic HTML5 elements and ARIA landmark roles to create navigable regions for screen readers - when you use semantic elements, they automatically create landmarks, and ARIA roles provide explicit landmark identification when needed. Screen readers navigate by landmarks, which improves user experience.

- **Trade-offs**: The catch is use semantic elements first (these have implicit landmark roles), add ARIA roles only when needed - only one banner, main, and contentinfo per page, while navigation can appear multiple times. Landmarks enable quick navigation for screen reader users.

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

`<details>` creates a disclosure widget that you can expand or collapse, while `<summary>` provides the visible summary text - it's a native HTML solution that's accessible by default, perfect for collapsible content without JavaScript. Use it for progressive disclosure of information.

- **Trade-offs**: The catch is `<details>` and `<summary>` provide native collapsible content that's accessible by default - use them for FAQs, collapsible sections, or any expandable content where you want progressive disclosure.

Example:

```html
<details>
  <summary>Click to expand</summary>
  <p>Hidden content that appears when expanded...</p>
</details>

```

---

