---
sidebar_label: "Architecture & Design Systems"
---
# 🏗️ 4. Architecture & Design Systems (Q41–48)
> **Reviewed:** 2026-09 · Modernized; legacy topics are labeled.

> **Legacy note (2026):** BEM, OOCSS, and SMACSS (Q41–43) are naming/organization methodologies from the era before component scoping and cascade layers. They're still asked about and BEM remains common in plain-CSS codebases, but many modern projects get scoping from CSS Modules/Tailwind/zero-runtime CSS-in-JS and ordering from `@layer` instead.

---

## Q41. 📝 BEM methodology and how it works

BEM (Block, Element, Modifier) is a CSS naming convention that creates clear, maintainable, and scalable CSS by establishing a strict naming structure - BEM prevents specificity wars and improves maintainability. Block is an independent component, Element is part of block, Modifier is a variation or state.

- **Trade-offs**: The catch is clear relationships, no specificity wars, easy to understand and maintain - creates reusable components that can be combined without conflicts. Naming convention: Block__Element--Modifier (double underscore, double hyphen).

Example:

```css
.card {
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  padding: 20px;
}
.card__header {
  font-size: 24px;
  font-weight: bold;
}
.card--featured {
  border: 2px solid gold;
}

```

---

## Q42. 📦 OOCSS (Object-Oriented CSS) principles

OOCSS separates structure from skin, creating reusable CSS objects that can be combined to build complex interfaces without duplication - OOCSS promotes reusability and maintainability. Separate layout properties from visual properties (structure vs skin).

- **Trade-offs**: The catch is changes to structure don't affect skin, and vice versa - combine multiple objects to create complex components. Separate container styles from content styles and create reusable objects.

Example:

```css
.media {
  display: flex;
  align-items: flex-start;
  gap: 15px;
}
.media__image {
  width: 100px;
  height: 100px;
  border-radius: 50%;
}
.media__content {
  flex: 1;
}

```

---

## Q43. 🎨 SMACSS (Scalable and Modular CSS) and its principles

SMACSS organizes CSS into five categories (Base, Layout, Module, State, Theme) to create scalable and maintainable stylesheets - SMACSS provides structure for large CSS codebases. Base is default styles, Layout is major structure (prefixed with `l-`), Module is reusable components (prefixed with `m-`), State is element states (prefixed with `is-` or `has-`), Theme is visual themes (prefixed with `t-`).

- **Trade-offs**: The catch is not following prefixes or mixing categories - creates scalable architecture for large projects. Organizes large stylesheets into logical sections.

Example:

```css
html, body {
  margin: 0;
  padding: 0;
  font-family: Arial, sans-serif;
  line-height: 1.6;
}
.l-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.m-button {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
.is-active {
  background-color: #007bff;
  color: white;
}

```

---

## Q44. 🎨 CSS-in-JS and its benefits

CSS-in-JS allows you to write CSS styles in JavaScript, providing component-scoped styles, dynamic styling, and better integration with modern frameworks - CSS-in-JS improves component isolation and dynamic styling. Styles are automatically scoped to components with no global pollution.

- **Trade-offs**: The catch is no specificity wars, each component has its own style scope - dead code elimination, unused styles are automatically removed. Easy to create styles based on props or state, works seamlessly with React/Vue.

- **The real catch in 2026 — runtime cost**: *runtime* CSS-in-JS libraries (styled-components, Emotion) serialize styles, hash them, and inject `<style>` rules **in the browser while rendering**. That adds JS bundle weight, CPU work on every render with changing props, and can hurt INP. They also fit poorly with **React Server Components** (they need React context and client-side style injection, so styled components must be Client Components) and need extra setup for streaming SSR.

  > **Legacy note (2026):** styled-components entered **maintenance mode in 2025**, and many teams are migrating away from runtime CSS-in-JS. It's still very common in existing codebases, so know how it works — but don't recommend it as the default for new React/Next.js apps.

- **Zero-runtime alternatives** (styles extracted to static `.css` at build time):
  - **CSS Modules** – plain CSS, locally scoped class names (Q45)
  - **Tailwind CSS** – utility classes, generates only the classes you use; v4 is CSS-first (config via `@theme` in CSS) and uses cascade layers
  - **vanilla-extract** – type-safe styles authored in `.css.ts` files, compiled to static CSS
  - **Panda CSS**, **StyleX** (Meta), **Linaria** – CSS-in-JS *authoring* with build-time extraction
  - Dynamic values: pass them via **CSS custom properties** (`style={{ '--progress': pct }}`) instead of regenerating styles

| Approach | Runtime JS | RSC-friendly | Dynamic styles |
|---|---|---|---|
| styled-components / Emotion | Yes | Client Components only | Props interpolation |
| CSS Modules | No | Yes | Custom properties / class toggles |
| Tailwind | No | Yes | Class toggles / custom properties |
| vanilla-extract / Panda / StyleX | No (or minimal) | Yes | Variants + custom properties |

Example:

```javascript
// Runtime CSS-in-JS (legacy default for many React apps)
import styled from 'styled-components';

const Button = styled.button`
  background-color: ${props => props.primary ? '#007bff' : '#6c757d'};
  color: white;
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
`;

```

```javascript
// Zero-runtime: vanilla-extract (button.css.ts) — compiled to a static .css file
import { style, styleVariants } from '@vanilla-extract/css';

const base = style({ color: 'white', padding: '8px 16px', border: 'none', borderRadius: 4 });
export const button = styleVariants({
  primary: [base, { background: '#007bff' }],
  secondary: [base, { background: '#6c757d' }],
});
```

---

## Q45. 🎨 CSS Modules and how it works

CSS Modules automatically scope CSS classes to components, preventing style conflicts and enabling modular CSS architecture - CSS Modules provide automatic scoping without JavaScript runtime. Classes are automatically prefixed with unique identifiers, preventing style conflicts.

- **Trade-offs**: The catch is can combine multiple classes easily, generates TypeScript definitions - build tool integration, type safety for CSS classes. Styles don't leak to other components and works with Webpack/Vite. CSS Modules are zero-runtime (plain static CSS), which makes them a safe default with React Server Components and Next.js App Router. Type definitions for class names usually come from a plugin (e.g. `typescript-plugin-css-modules`) rather than out of the box. Pair them with `@layer` if you need predictable ordering between global and module styles.

Example:

```css
/* Button.module.css */
.button {
  background-color: #007bff;
  color: white;
  padding: 8px 16px;
  border: none;
}
.button--large {
  padding: 12px 24px;
  font-size: 18px;
}

```

```javascript
import styles from './Button.module.css';
function Button({ children, size }) {
  const className = [
    styles.button,
    size === 'large' && styles['button--large']
  ].filter(Boolean).join(' ');
  return <button className={className}>{children}</button>;
}

```

---

## Q46. 🎨 CSS architecture and how to organize large stylesheets

CSS architecture involves organizing stylesheets into logical sections and using methodologies to create maintainable, scalable CSS codebases - CSS architecture requires documentation and consistent conventions. Group related styles into separate files for better maintainability, use consistent naming patterns (BEM, OOCSS, SMACSS), and break large stylesheets into smaller, focused modules.

- **Trade-offs**: The catch is import files in logical order (reset, base, utilities, layout, components, pages) - use consistent naming patterns to avoid conflicts and improve maintainability. Breaking large stylesheets into smaller modules makes it easier to find and update styles, but requires good documentation and team conventions.

Example:

```css
@import 'reset.css';
@import 'base.css';
@import 'utilities/spacing.css';
@import 'layout/header.css';
@import 'components/button.css';

```

- **2026 practice**: encode that order with **cascade layers** so file order and specificity stop mattering, and bundle at build time (runtime CSS `@import` chains create sequential downloads — let Vite/Lightning CSS/PostCSS inline them):

```css
@layer reset, base, layout, components, utilities;

@import 'reset.css' layer(reset);
@import 'base.css' layer(base);
@import 'layout/header.css' layer(layout);
@import 'components/button.css' layer(components);
@import 'utilities/spacing.css' layer(utilities);
```

---

## Q47. 🎨 CSS preprocessors in large projects

CSS preprocessors like SASS and LESS extend CSS with variables, mixins, nesting, and functions - they compile to regular CSS and help manage large codebases. Preprocessors provide features like variables for reusable values, mixins for reusable code blocks, nesting for better organization, and functions for calculations.

- **Trade-offs**: The catch is preprocessors require a build step to compile to CSS, but they make large projects more maintainable with features like variables, mixins, and nesting. SASS and LESS are the most popular, with SASS having more features and better tooling support.

- **2026 perspective**: native CSS now has custom properties, nesting, `@layer`, `color-mix()`, and math functions, so preprocessors are less essential. Sass is still useful for maps, loops, and mixins in large design systems; use **Dart Sass** with `@use`/`@forward` (`@import` and global functions like `map-get` are deprecated in favour of `map.get` from `sass:map`). Compile-time Sass variables can't change at runtime — expose themeable values as CSS custom properties.

Example:

```scss
$primary-color: #007bff;
$secondary-color: #6c757d;
$breakpoints: (
  mobile: 768px,
  tablet: 1024px,
  desktop: 1200px
);
@mixin responsive($breakpoint) {
  @media (min-width: map-get($breakpoints, $breakpoint)) {
    @content;
  }
}
.button {
  background-color: $primary-color;
  @include responsive(tablet) {
    padding: 12px 24px;
  }
}

```

---

## Q48. 🎨 Design system implementation with CSS

Design systems provide consistent, reusable components and patterns across applications - CSS plays a crucial role in implementing design tokens, component styles, and theming. Design systems ensure visual consistency and maintainability across large applications.

- **Trade-offs**: The catch is CSS variables enable dynamic theming and design tokens - component-based CSS architecture supports reusable patterns. Requires careful planning and documentation for team adoption.

Example:

```css
/* Design tokens using CSS variables */
:root {
  --color-primary: #007bff;
  --color-secondary: #6c757d;
  --spacing-unit: 8px;
  --border-radius: 4px;
}

/* Component styles using tokens */
.button {
  background-color: var(--color-primary);
  padding: calc(var(--spacing-unit) * 2);
  border-radius: var(--border-radius);
}

/* Theming support */
[data-theme="dark"] {
  --color-primary: #0d6efd;
  --color-secondary: #6c757d;
}

```

- **Modern design-system CSS toolkit**:
  - **Token tiers**: primitive (`--blue-600`) → semantic (`--color-action`) → component (`--button-bg`); themes override the semantic tier. Tokens are often authored in the W3C Design Tokens format and generated with tools like Style Dictionary.
  - **`@layer`** so consumer overrides reliably beat library defaults (ship library styles in a named layer).
  - **`:where()`** for zero-specificity defaults.
  - **Container queries** so components adapt to where they're placed, not the viewport.
  - **`oklch()` + `color-mix()`** to generate tint/shade scales with consistent contrast; `light-dark()` + `color-scheme` for themes.
  - **Logical properties** (`padding-inline`, `margin-block`) so RTL works without overrides.
  - Zero-runtime styling (CSS Modules, Tailwind, vanilla-extract) to keep components RSC-compatible.

See [3. Modern CSS Features](./03-modern-css-features.md) for details on these features.

---

