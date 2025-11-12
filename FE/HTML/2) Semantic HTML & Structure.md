# 🏗️ 2. Semantic HTML & Structure (Q16–30)

---

## 🧩 Q16. What is semantic HTML and why is it important?

### 🧠 Concept

Semantic HTML uses meaningful tags that describe content purpose. It improves accessibility, SEO, and maintainability by giving meaning to structure.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Use tags that describe content meaning, not just appearance.
* **Use Case:** Improves screen reader navigation, SEO, and code maintainability.
* **Common Mistake:** Screen readers use semantic tags to navigate and understand content.
* **Pro Tip:** Search engines understand content structure better with semantic HTML.

---

### ⭐ Senior Takeaway

Semantic HTML is about meaning, not just styling.

---

## 🧩 Q17. What is the difference between `<header>` and `<h1>`?

### 🧠 Concept

`<header>` is a semantic container for introductory content. `<h1>` is a heading element for the main title. `<header>` creates landmark region for screen readers.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** `<header>` is a container, `<h1>` is a heading element.
* **Use Case:** `<header>` can contain multiple elements (title, nav, logo), `<h1>` is just the heading.
* **Common Mistake:** `<header>` creates landmark region for screen readers.
* **Pro Tip:** Only one `<h1>` per page for SEO, `<header>` can appear multiple times.

---

### ⭐ Senior Takeaway

`<header>` is a section, `<h1>` is a heading level.

---

## 🧩 Q18. What is the difference between `<article>` and `<section>`?

### 🧠 Concept

`<article>` represents complete standalone content. `<section>` represents thematic grouping within a document. `<article>` can contain multiple `<section>` elements.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** `<article>` should make sense on its own, `<section>` groups related content.
* **Use Case:** `<article>` for blog posts, news articles; `<section>` for chapters or sections within content.
* **Common Mistake:** `<article>` can contain multiple `<section>` elements.
* **Pro Tip:** Use `<section>` when you need a heading for a thematic group.

---

### ⭐ Senior Takeaway

`<article>` is complete content, `<section>` is part of content.

---

## 🧩 Q19. What is the purpose of the `<nav>` element?

### 🧠 Concept

`<nav>` identifies navigation links and creates a landmark region for screen readers. Use `aria-label` for descriptive names, can appear multiple times per page.

---

### 💡 Example

```html
<nav aria-label="Main navigation">
  <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/about">About</a></li>
  </ul>
</nav>
```

---

### 🔍 Deep Insights

* **Rule:** Identify navigation links and create accessible landmarks.
* **Use Case:** Main navigation, breadcrumbs, or any navigation links.
* **Common Mistake:** Creates landmark region for screen reader navigation.
* **Pro Tip:** Use `aria-label` for descriptive names, can appear multiple times per page.

---

### ⭐ Senior Takeaway

`<nav>` is for navigation, not just any links.

---

## 🧩 Q20. What is the document outline and how do you create it?

### 🧠 Concept

Use heading elements (`<h1>` to `<h6>`) in proper hierarchical order to create logical document structure. Screen readers use headings for navigation.

---

### 💡 Example

```html
<h1>Main Page Title</h1>
  <h2>Section Title</h2>
    <h3>Subsection Title</h3>
    <h3>Another Subsection</h3>
  <h2>Another Section</h2>
```

---

### 🔍 Deep Insights

* **Rule:** Start with `<h1>` for main title, don't skip heading levels.
* **Use Case:** Screen readers use headings for navigation, improves accessibility.
* **Common Mistake:** Proper heading hierarchy helps search engines understand content structure.
* **Pro Tip:** Only one `<h1>` per page, use headings to create document outline.

---

### ⭐ Senior Takeaway

Heading hierarchy is crucial for accessibility and SEO.

---

## 🧩 Q21. What is the difference between `<main>` and `<body>`?

### 🧠 Concept

`<main>` contains the primary content. `<body>` contains all visible content including headers and footers. `<main>` creates landmark region for screen readers.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** `<main>` is primary content only, `<body>` is all visible content.
* **Use Case:** `<main>` identifies main content area, only one per page.
* **Common Mistake:** `<main>` creates landmark region for screen readers.
* **Pro Tip:** Use `<main>` to wrap primary content, exclude headers and footers.

---

### ⭐ Senior Takeaway

`<main>` is a semantic landmark, `<body>` is the container.

---

## 🧩 Q22. What is the purpose of the `<aside>` element?

### 🧠 Concept

`<aside>` contains content tangentially related to main content. `<section>` groups thematically related content. `<aside>` is supplementary, `<section>` is part of main content.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** `<aside>` is supplementary content, `<section>` is thematically grouped content.
* **Use Case:** `<aside>` for sidebars, ads, related links; `<section>` for content chapters.
* **Common Mistake:** `<aside>` is tangentially related, `<section>` is directly related.
* **Pro Tip:** Both can have headings, both create landmark regions.

---

### ⭐ Senior Takeaway

`<aside>` is supplementary, `<section>` is part of main content.

---

## 🧩 Q23. What is the difference between `<figure>` and `<img>`?

### 🧠 Concept

`<figure>` represents self-contained content like images or code. `<img>` is just the image element. `<figure>` groups content with its caption for better accessibility.

---

### 💡 Example

```html
<figure>
  <img src="chart.jpg" alt="Sales data chart">
  <figcaption>Monthly sales data for Q1 2024</figcaption>
</figure>
```

---

### 🔍 Deep Insights

* **Rule:** Group content with its caption for better accessibility.
* **Use Case:** Images, code blocks, diagrams, or any content needing a caption.
* **Common Mistake:** Screen readers associate caption with content.
* **Pro Tip:** Use `<figcaption>` for descriptive captions, improves understanding.

---

### ⭐ Senior Takeaway

`<figure>` groups content and caption semantically.

---

## 🧩 Q24. What is the purpose of the `<figcaption>` element?

### 🧠 Concept

`<figcaption>` provides a caption for `<figure>` content. It improves accessibility by associating descriptive text with images, code, or diagrams.

---

### 💡 Example

```html
<figure>
  <img src="chart.jpg" alt="Sales data chart">
  <figcaption>Monthly sales data for Q1 2024</figcaption>
</figure>
```

---

### 🔍 Deep Insights

* **Rule:** Provides descriptive caption for figure content.
* **Use Case:** Images, code blocks, diagrams, or any content needing explanation.
* **Common Mistake:** Screen readers associate caption with content automatically.
* **Pro Tip:** Use descriptive captions that add context, not just repeat alt text.

---

### ⭐ Senior Takeaway

`<figcaption>` improves accessibility and understanding.

---

## 🧩 Q25. What is the difference between `<time>` and `<date>`?

### 🧠 Concept

`<time>` represents dates, times, or durations in machine-readable format. There is no `<date>` element in HTML—use `<time>` for all date/time needs.

---

### 💡 Example

```html
<time datetime="2024-01-15">January 15, 2024</time>
<time datetime="2024-01-15T14:30:00">2:30 PM</time>
<time datetime="PT2H30M">2 hours 30 minutes</time>
```

---

### 🔍 Deep Insights

* **Rule:** Provide machine-readable dates and times for better accessibility and SEO.
* **Use Case:** Events, articles, schedules, or any time-sensitive content.
* **Common Mistake:** Screen readers can announce dates properly with machine-readable format.
* **Pro Tip:** Enables date-based search and filtering.

---

### ⭐ Senior Takeaway

`<time>` makes dates accessible to both humans and machines.

---

## 🧩 Q26. What is the purpose of the `<mark>` element?

### 🧠 Concept

`<mark>` highlights text for reference purposes, like search results or important passages. Don't use for emphasis—use `<em>` or `<strong>` instead.

---

### 💡 Example

```html
<p>Search results for <mark>JavaScript</mark> programming</p>
<p>This is <mark>highlighted text</mark> for emphasis</p>
```

---

### 🔍 Deep Insights

* **Rule:** Highlight text for reference, not for emphasis.
* **Use Case:** Search result highlighting, important passages, or reference notes.
* **Common Mistake:** Default styling is yellow background, can be customized with CSS.
* **Pro Tip:** Don't use for emphasis (use `<em>` or `<strong>` instead).

---

### ⭐ Senior Takeaway

`<mark>` is for highlighting reference, not emphasis.

---

## 🧩 Q27. What are landmark regions and how do you use them?

### 🧠 Concept

Use semantic HTML5 elements and ARIA landmarks to create navigable regions for screen readers. Semantic elements automatically create landmarks.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Create navigable regions for screen readers using semantic elements.
* **Use Case:** Semantic elements automatically create landmarks, use ARIA roles if needed.
* **Common Mistake:** Screen readers navigate by landmarks, improves user experience.
* **Pro Tip:** Use semantic elements first, add ARIA roles only when needed.

---

### ⭐ Senior Takeaway

Landmarks enable screen reader navigation.

---

## 🧩 Q28. What is the difference between `<address>` and `<footer>`?

### 🧠 Concept

`<address>` contains contact information for the nearest article or body. `<footer>` contains footer content for its nearest sectioning element. Both have different semantic purposes.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** `<address>` is for contact information, `<footer>` is for footer content.
* **Use Case:** `<address>` for author contact, `<footer>` for site-wide footer content.
* **Common Mistake:** Both can appear multiple times, but serve different purposes.
* **Pro Tip:** `<address>` is semantic for contact info, `<footer>` is for footer sections.

---

### ⭐ Senior Takeaway

`<address>` is for contact info, `<footer>` is for footer sections.

---

## 🧩 Q29. What is the purpose of the `<details>` and `<summary>` elements?

### 🧠 Concept

`<details>` creates a disclosure widget that can be expanded or collapsed. `<summary>` provides the visible summary text. Perfect for collapsible content.

---

### 💡 Example

```html
<details>
  <summary>Click to expand</summary>
  <p>Hidden content that appears when expanded...</p>
</details>
```

---

### 🔍 Deep Insights

* **Rule:** Creates interactive disclosure widget without JavaScript.
* **Use Case:** FAQs, collapsible sections, or any expandable content.
* **Common Mistake:** Native HTML solution, accessible by default.
* **Pro Tip:** Use for progressive disclosure of information.

---

### ⭐ Senior Takeaway

`<details>` and `<summary>` provide native collapsible content.

---

## 🧩 Q30. How do you create a proper document structure?

### 🧠 Concept

Use semantic HTML5 elements, proper heading hierarchy, and landmark regions to create a logical document structure that's accessible and SEO-friendly.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Use semantic elements for structure, not generic divs.
* **Use Case:** Proper heading hierarchy and landmark regions improve accessibility.
* **Common Mistake:** Semantic structure helps search engines understand content.
* **Pro Tip:** Start with DOCTYPE, use semantic elements, maintain heading hierarchy.

---

### ⭐ Senior Takeaway

Proper document structure improves accessibility, SEO, and maintainability.

---
