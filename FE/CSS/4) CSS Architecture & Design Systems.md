# 🏗️ 4. CSS Architecture & Design Systems (Q41–48)

---

## 📍 Navigation

<div align="center">

[Advanced CSS Concepts](3%29%20Advanced%20CSS%20Concepts.md) • [Home: README](../README.md) • [Performance & Optimization →](5%29%20Performance%20%26%20Optimization.md)

[📋 Cheatsheet](CSS%20Interview%20Cheatsheet.md]

</div>

---

---

## Q41. 📝 BEM methodology and how it works

BEM (Block, Element, Modifier) is a CSS naming convention that creates clear, maintainable, and scalable CSS by establishing a strict naming structure - BEM prevents specificity wars and improves maintainability. Block (independent component), Element (part of block), Modifier (variation or state).

- **Trade-offs**: The catch is clear relationships, no specificity wars, easy to understand and maintain - creates reusable components that can be combined without conflicts. BEM prevents specificity wars and improves maintainability, but watch out - naming convention: Block__Element--Modifier (double underscore, double hyphen).

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

- **Trade-offs**: The catch is changes to structure don't affect skin, and vice versa - combine multiple objects to create complex components. OOCSS promotes reusability and maintainability, but watch out - separate container styles from content styles, create reusable objects.

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

SMACSS organizes CSS into five categories (Base, Layout, Module, State, Theme) to create scalable and maintainable stylesheets - SMACSS provides structure for large CSS codebases. Base (default styles), Layout (major structure, prefixed with `l-`), Module (reusable components, prefixed with `m-`), State (element states, prefixed with `is-` or `has-`), Theme (visual themes, prefixed with `t-`).

- **Trade-offs**: The catch is not following prefixes, mixing categories - creates scalable architecture for large projects. SMACSS provides structure for large CSS codebases, but watch out - organizes large stylesheets into logical sections.

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

CSS-in-JS allows you to write CSS styles in JavaScript, providing component-scoped styles, dynamic styling, and better integration with modern frameworks - CSS-in-JS improves component isolation and dynamic styling. Styles are automatically scoped to components, no global pollution.

- **Trade-offs**: The catch is no specificity wars, each component has its own style scope - dead code elimination, unused styles are automatically removed. CSS-in-JS improves component isolation and dynamic styling, but watch out - easy to create styles based on props or state, works seamlessly with React/Vue.

Example:

```javascript
import styled from 'styled-components';

const Button = styled.button`
  background-color: ${props => props.primary ? '#007bff' : '#6c757d'};
  color: white;
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
`;

```

---

## Q45. 🎨 CSS Modules and how it works

CSS Modules automatically scope CSS classes to components, preventing style conflicts and enabling modular CSS architecture - CSS Modules provide automatic scoping without JavaScript runtime. Classes are automatically prefixed with unique identifiers, preventing style conflicts.

- **Trade-offs**: The catch is can combine multiple classes easily, generates TypeScript definitions - build tool integration, type safety for CSS classes. CSS Modules provide automatic scoping without JavaScript runtime, but watch out - styles don't leak to other components, works with Webpack/Vite.

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

CSS custom properties enable consistent theming and design tokens in design systems, allowing dynamic theme switching and centralized style management - CSS variables are essential for modern design systems. Centralized values for colors, spacing, typography, and other design elements.

- **Trade-offs**: The catch is ensures consistent spacing, colors, and typography across components - single source of truth for design values, can be updated with JavaScript. CSS variables are essential for modern design systems, but watch out - easy to switch between different themes by changing root variables.

Example:

```css
:root {
  --color-primary: #007bff;
  --color-secondary: #6c757d;
  --color-success: #28a745;
  --spacing-unit: 8px;
  --border-radius: 4px;
}

```

---

## Q47. 🎨 CSS preprocessors in large projects

CSS architecture involves organizing stylesheets into logical sections and using methodologies to create maintainable, scalable CSS codebases - CSS architecture requires documentation and consistent conventions. Group related styles into separate files for better maintainability.

- **Trade-offs**: The catch is use consistent naming patterns (BEM, OOCSS, SMACSS) - break large stylesheets into smaller, focused modules. CSS architecture requires documentation and consistent conventions, but watch out - import files in logical order (reset, base, utilities, layout, components, pages).

Example:

```css
@import 'reset.css';
@import 'base.css';
@import 'utilities/spacing.css';
@import 'layout/header.css';
@import 'components/button.css';

```

---

CSS preprocessors provide powerful features for managing large CSS codebases, including variables, mixins, functions, and modular architecture - preprocessors compile to standard CSS, browser support depends on output. Centralized values for colors, spacing, breakpoints, and other design tokens.

- **Trade-offs**: The catch is custom functions for calculations and value transformations - break stylesheets into focused, importable modules. Preprocessors compile to standard CSS, browser support depends on output, but watch out - reusable style blocks (mixins) that can be included in multiple selectors.

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

```

---

---

## 📍 Navigation

<div align="center">

[Advanced CSS Concepts](3%29%20Advanced%20CSS%20Concepts.md) • [Home: README](../README.md) • [Performance & Optimization →](5%29%20Performance%20%26%20Optimization.md)

[📋 Cheatsheet](CSS%20Interview%20Cheatsheet.md]

</div>

---
