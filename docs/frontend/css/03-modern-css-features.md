---
sidebar_label: "Modern CSS Features"
---
# 3. Modern CSS Features
> **Reviewed:** 2026-09 · Modernized; legacy topics are labeled.

This section covers Q33–35 and Q37–39: the features that changed how CSS is written in the last few years. Related modern topics live next to their fundamentals: subgrid (Q36) and `color-mix()`/`oklch` (Q40) in [Layout & Styling](./02-layout-and-styling.md), and `@layer`-based architecture in [Architecture & Design Systems](./04-architecture-and-design-systems.md).

> **About "Baseline":** "Baseline" (shown on MDN and web.dev) means a feature works in the current versions of Chrome, Edge, Firefox, and Safari. "Baseline Newly available" = just reached all engines; "Widely available" = about 30 months later. When a feature isn't Baseline yet, say so and describe a fallback.

---

## Q33. 📦 Container queries and when to use them over media queries

Container queries let a component style itself based on the size of **its container**, not the viewport. That's what you actually want for reusable components: the same card should be vertical in a narrow sidebar and horizontal in a wide main column, regardless of screen size. Size container queries and container query units have been Baseline since 2023.

- **How it works**: mark an ancestor as a container with `container-type: inline-size` (optionally name it with `container-name`), then write `@container (width > 30rem) { ... }` rules for its descendants. Container units `cqi`/`cqb` (1% of the container's inline/block size) enable component-level fluid sizing.

- **Trade-offs**: The catch is an element can't query itself — it queries its nearest container ancestor, so you often need a wrapper. `container-type: inline-size` applies size containment on the inline axis, so the container can't size itself from its children's width (usually fine for block-level wrappers, surprising for shrink-to-fit elements). Use media queries for **page-level** layout and user preferences (`prefers-reduced-motion`, `prefers-color-scheme`); use container queries for **component-level** layout.

- **Style queries**: `@container style(--variant: compact)` queries custom property values. Support is still partial (Chromium and Safari, not all engines) — treat as emerging.

Example:

```css
.card-wrapper {
  container-type: inline-size;
  container-name: card;
}

.card { display: grid; gap: 1rem; }

@container card (width > 30rem) {
  .card { grid-template-columns: 10rem 1fr; }
  .card h2 { font-size: clamp(1.25rem, 1rem + 2cqi, 2rem); }
}
```

📌 **In simple terms**: Media queries ask "how big is the screen?"; container queries ask "how much room do I have right here?"

---

## Q34. 🔍 The `:has()` relational pseudo-class ("parent selector")

`:has()` selects an element if **any of the relative selectors passed to it match** — for the first time CSS can style a parent or previous sibling based on what's inside or after it. `:has()` has been Baseline since December 2023 (Firefox 121 was the last engine to ship it).

- **Common uses**:
  - Parent styling: `.card:has(img)` gives cards with images a different layout
  - Form state: `.field:has(input:user-invalid)` highlights the whole field wrapper
  - Previous-sibling: `h2:has(+ p)` styles a heading followed by a paragraph
  - Page-level state: `html:has(dialog[open]) { overflow: hidden; }` locks scroll when a modal is open — no JavaScript class toggling
  - Quantity queries: `ul:has(> li:nth-child(6))` changes layout when a list has 6+ items

- **Trade-offs**: The catch is `:has()` takes the specificity of its most specific argument, and very broad anchors (`body:has(...)`, `*:has(...)`) can force the browser to re-check a lot of the tree when the DOM changes — keep the subject selector reasonably specific. `:has()` can't be nested inside another `:has()`, and it doesn't work with pseudo-elements inside it. For older browsers, wrap enhancements in `@supports selector(:has(a))`.

Example:

```css
.field:has(input:user-invalid) {
  border-color: red;
}
.field:has(input:user-invalid) .error-message {
  display: block;
}

.card:has(> img) {
  grid-template-rows: 12rem auto;
}

html:has(dialog[open]) {
  overflow: hidden;
}
```

📌 **In simple terms**: `:has()` lets you say "style this element *if it contains* (or is followed by) that element" — lots of JS-driven class toggling becomes pure CSS.

---

## Q35. 🧱 Cascade layers (`@layer`) and why they matter

Cascade layers let you group styles into named layers and declare their **priority order explicitly**. In the cascade, **layer order is checked before specificity** — so a simple `.btn` rule in a later layer beats `#app .sidebar .btn` in an earlier layer. `@layer` has been Baseline since 2022.

- **How it works**:
  - Declare order once: `@layer reset, base, components, utilities;` (first = lowest priority)
  - Add rules to a layer: `@layer components { ... }` or import into one: `@import url(lib.css) layer(vendor);`
  - **Unlayered** styles beat all layered styles (for normal declarations) — useful for quick overrides, but it also means an unlayered third-party stylesheet will override your layers
  - `!important` **reverses** layer order: an important declaration in an *earlier* layer wins over one in a later layer (so resets can protect critical rules)
  - Layers can be nested (`@layer framework.components`)

- **Trade-offs**: The catch is teams must agree on a layer order up front and put everything (including third-party CSS) into layers, or unlayered styles will surprise you. The payoff: no more specificity wars or `!important` escalation when overriding library/design-system styles. Tailwind CSS v4 emits its output in `theme`, `base`, `components`, and `utilities` layers.

Example:

```css
@layer reset, vendor, base, components, utilities;

@import url('normalize.css') layer(reset);
@import url('datepicker.css') layer(vendor);

@layer base {
  a { color: var(--color-link); }
}

@layer components {
  .nav .item a { color: inherit; } /* specificity 0,2,1 */
}

@layer utilities {
  .text-danger { color: red; }     /* specificity 0,1,0 — still wins, later layer */
}
```

📌 **In simple terms**: `@layer` lets you say "utilities always beat components, components always beat the base" — regardless of how specific each selector is.

---

## Q37. 🪆 Native CSS nesting vs Sass nesting

CSS now supports nesting natively — write child rules inside a parent rule without a preprocessor. Native nesting has been Baseline since December 2023, and the "relaxed" syntax (nesting a bare element selector like `p { }` without `&`) is supported in all current engines.

- **How it differs from Sass**:
  - `&` represents the parent selector; `&:hover`, `& > li`, `.theme-dark &` all work
  - Nested rules behave like `:is(parent) child`, so the parent's specificity is that of its most specific selector (Sass just concatenates strings)
  - **No string concatenation**: Sass's `&__element` (BEM suffixing) does **not** work natively — `&__title` is invalid
  - You can nest **`@media`, `@container`, `@supports`, and `@layer`** inside rules
  - Declarations that come after nested rules are handled specially by the spec — keep declarations before nested rules for clarity

- **Trade-offs**: The catch is deep nesting still creates high-specificity, DOM-coupled selectors — keep it to 1–2 levels. If you need to support older browsers, a build tool (Lightning CSS, PostCSS nesting plugin) can flatten nested CSS.

Example:

```css
.card {
  padding: 1rem;
  border-radius: 0.5rem;

  & h2 { margin-block: 0 0.5rem; }
  &:hover { box-shadow: 0 4px 12px rgb(0 0 0 / 0.15); }
  .theme-dark & { background: #1e1e1e; }

  @media (width >= 48rem) {
    padding: 2rem;
  }
}

/* ❌ Sass-only — not valid native CSS */
/* .card { &__title { ... } } */
```

📌 **In simple terms**: Native nesting gives you Sass-style nesting without a build step, except for BEM-style `&__suffix` string joining.

---

## Q38. ↔️ Logical properties and `clamp()` for international, fluid layouts

**Logical properties** describe layout in terms of **flow direction** instead of physical sides: `inline` (the text direction — left/right in English) and `block` (the stacking direction — top/bottom in English). They automatically flip for right-to-left languages (Arabic, Hebrew) and adapt to vertical writing modes. They've been Baseline for years.

- **Mapping** (in a left-to-right, horizontal writing mode):
  - `margin-left` → `margin-inline-start`; `padding-left` + `padding-right` → `padding-inline`
  - `margin-top` → `margin-block-start`; `top/right/bottom/left` → `inset` / `inset-inline` / `inset-block`
  - `width` → `inline-size`; `height` → `block-size`
  - `text-align: left` → `text-align: start`; `border-left` → `border-inline-start`

- **`clamp(min, preferred, max)`** (with `min()`/`max()`) creates fluid values that scale smoothly between limits — spacing, type, widths — often replacing several breakpoints:
  - `padding-inline: clamp(1rem, 5vw, 3rem)`
  - `width: min(100% - 2rem, 70ch)` for a centered, readable content column
  - Include a `rem` term in fluid font sizes (`1rem + 2vw`) so text still responds to user zoom (WCAG 1.4.4)

- **Trade-offs**: The catch is mixing physical and logical properties in the same component causes confusing overrides in RTL — pick logical as the team default (a Stylelint rule can enforce it). Physical properties are still correct for things that are genuinely physical (e.g. a shadow that should always fall down-right).

Example:

```css
.callout {
  margin-block: 1.5rem;
  padding-inline: clamp(1rem, 4vw, 2.5rem);
  border-inline-start: 4px solid var(--color-accent); /* on the right in RTL */
  text-align: start;
}

.content {
  inline-size: min(100% - 2rem, 70ch);
  margin-inline: auto;
}
```

📌 **In simple terms**: Logical properties make layouts direction-agnostic, and `clamp()` makes them size-agnostic — together they remove a lot of RTL overrides and breakpoints.

---

## Q39. 🎞️ View transitions and scroll-driven animations

The **View Transitions API** animates between two UI states (or two pages) by snapshotting the old and new states and cross-fading/morphing between them with CSS.

- **Same-document (SPA) transitions**: call `document.startViewTransition(() => updateDOM())`. Supported in Chromium since 2023 and Safari 18; Firefox shipped it in 2025 — check current Baseline status before relying on it without a fallback.
- **Cross-document (MPA) transitions**: opt in on both pages with `@view-transition { navigation: auto; }` for same-origin navigations. Supported in Chromium and Safari at the time of review; treat as **emerging** / progressive enhancement.
- **Customize** with `view-transition-name: hero` on elements you want to morph (e.g. a thumbnail becoming a hero image) and style the `::view-transition-old(hero)` / `::view-transition-new(hero)` pseudo-elements.
- Frameworks are adding integrations (e.g. Astro's view transitions, React's experimental `<ViewTransition>` component, router-level support in some SPA routers).

**Scroll-driven animations** (`animation-timeline: scroll()` / `view()`) link a CSS animation's progress to scroll position — reading-progress bars, reveal-on-scroll — with no JavaScript and off the main thread. Chromium-first; Safari added support in 2025 and Firefox support is still behind a flag at the time of review — **emerging**, use `@supports (animation-timeline: view())`.

- **Trade-offs**: The catch is both are progressive enhancements — the update must still work instantly without them. Always respect `prefers-reduced-motion`. Each `view-transition-name` must be unique on the page at the moment of the transition. Long or large transitions can hurt perceived responsiveness (INP) — keep them short.

Example:

```javascript
function navigate(update) {
  if (!document.startViewTransition) return update();
  document.startViewTransition(() => update());
}
```

```css
.product-thumb { view-transition-name: product-hero; }

::view-transition-old(root),
::view-transition-new(root) { animation-duration: 200ms; }

@media (prefers-reduced-motion: reduce) {
  ::view-transition-group(*),
  ::view-transition-old(*),
  ::view-transition-new(*) { animation: none; }
}

/* Scroll-driven reading progress bar */
@supports (animation-timeline: scroll()) {
  .progress {
    transform-origin: left;
    animation: grow linear both;
    animation-timeline: scroll(root);
  }
  @keyframes grow { from { transform: scaleX(0); } to { transform: scaleX(1); } }
}
```

📌 **In simple terms**: View transitions give you native, app-like page/state animations; scroll-driven animations tie animation progress to scrolling — both are enhancements, not requirements.

---

## ⭐ Summary — 10-second Interview Version

> "Modern CSS lets components adapt to their container (container queries), style parents based on children (`:has()`), control the cascade explicitly (`@layer`), nest natively, flip for RTL automatically (logical properties), scale fluidly (`clamp()`), and animate between states (view transitions). Most are Baseline now; view transitions across documents and scroll-driven animations are still emerging, so I ship them as progressive enhancement."

---

## References

* [MDN — CSS container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_containment/Container_queries)
* [MDN — :has()](https://developer.mozilla.org/en-US/docs/Web/CSS/:has)
* [MDN — @layer](https://developer.mozilla.org/en-US/docs/Web/CSS/@layer)
* [MDN — CSS nesting](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_nesting)
* [MDN — CSS logical properties and values](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_logical_properties_and_values)
* [MDN — View Transition API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API)
* [web.dev — Baseline](https://web.dev/baseline)
