---
sidebar_label: "Cheatsheet"
sidebar_position: 100
---
# 🎨 CSS Interview Cheatsheet
> **Reviewed:** 2026-09 · Modernized; legacy topics are labeled.

> **⏱️ Review Time: 10-15 minutes** | **Priority: ⭐⭐⭐ High** | Essential CSS concepts for interviews

**Quick Review Checklist:**

- [ ] Box Model & Specificity

- [ ] Flexbox (Container & Item Properties)

- [ ] CSS Grid (2D Layout System)

- [ ] Positioning (static, relative, absolute, fixed, sticky)

- [ ] Responsive Design (Media Queries, Mobile-first)

- [ ] Animations & Transitions

- [ ] Modern CSS (Container Queries, `:has()`, `@layer`, Nesting, Logical Properties, View Transitions)

- [ ] Styling approach (runtime CSS-in-JS vs zero-runtime: CSS Modules, Tailwind, vanilla-extract)

- [ ] Performance (compositor-friendly animations, `content-visibility`, critical CSS)

---

## 📋 **Quick Reference**

### **CSS Syntax & Inclusion**

**Definition:** CSS rules consist of selectors and declarations; can be included via external stylesheets, internal style tags, or inline styles with increasing specificity.

```css
selector { property: value; }
/* External */ <link rel="stylesheet" href="styles.css">
/* Internal */ <style>body { margin: 0; }</style>
/* Inline */ <div style="color: red;">Text</div>

```

### **Units**

**Definition:** Absolute units (px) are fixed; relative units (%, em, rem, vw, vh) scale based on parent/root/viewport, enabling responsive designs.

```css
/* Absolute: px, pt, in, cm, mm */
width: 100px;
/* Relative: %, em (own/parent font-size), rem (root), vw, vh */
width: 50%; font-size: 1.5em; margin: 2rem; height: 50vh;
/* Modern: dvh/svh/lvh (mobile viewport), cqi (container), ch (character width) */
min-height: 100dvh; max-width: 65ch;

```

---

## 🎯 **Selectors & Specificity**

### **Basic Selectors**

**Definition:** Target elements by type (p), class (.class), ID (#id), attribute ([attr]), or universal (*) to apply styles to specific elements.

```css
p { } .class { } #id { } * { } [attr] { }

```

### **Combinators**

**Definition:** Combine selectors to target relationships: descendant (space), child (>), adjacent sibling (+), or general sibling (~) for precise styling.

```css
div p { } /* Descendant */
div > p { } /* Child */
h1 + p { } /* Adjacent sibling */
h1 ~ p { } /* General sibling */

```

### **Pseudo-classes & Elements**

```css
:hover :focus :first-child :nth-child(2n) ::before ::after

```

### **Specificity Order**

```

Inline styles (1000) > IDs (100) > Classes (10) > Elements (1)
Later rules win when specificity is equal
Cascade layers are compared BEFORE specificity (later @layer wins)
:where() = 0 specificity; :is()/:not()/:has() = most specific argument

```

---

## 📦 **Box Model**

### **Box Model Components**

**Definition:** Every element has content, padding (inner space), border, and margin (outer space); box-sizing controls whether padding/border are included in width.

```css
.element { width: 200px; padding: 20px; border: 2px solid; margin: 10px; }

```

**Structure**: Content → Padding → Border → Margin
**Total width**: content + padding + border + margin
**Box-sizing**: `border-box` includes padding+border in width

### **Margin & Padding Shorthand**

```css
margin: 10px; /* All sides */
margin: 10px 20px; /* top/bottom left/right */
margin: 10px 20px 15px 25px; /* top right bottom left */

```

---

## 🔧 **Flexbox**

### **Container Properties**

**Definition:** Flexbox container controls layout direction, alignment (justify-content for main axis, align-items for cross axis), wrapping, and spacing between items.

```css
.container {
  display: flex;
  flex-direction: row | column;
  justify-content: center | space-between;
  align-items: center | stretch;
  flex-wrap: wrap;
  gap: 20px;
}

```

### **Item Properties**

```css
.item {
  flex: 1; /* grow shrink basis */
  flex-grow: 1;
  flex-shrink: 0;
  flex-basis: 200px;
  align-self: center;
}

```

**Main axis**: `flex-direction` controls
**Cross axis**: `align-items` controls

---

## 🎯 **CSS Grid**

### **Grid Container**

**Definition:** CSS Grid creates 2D layouts with rows and columns; define template areas, column/row sizes, and gaps for complex responsive designs.

```css
.container {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;
  grid-template-rows: auto 1fr auto;
  gap: 20px;
  grid-template-areas: "header header" "sidebar main" "footer footer";
}

```

### **Grid Items**

```css
.item {
  grid-column: 1 / 3;
  grid-row: 1;
  grid-area: header;
}

```

**Grid vs Flexbox**: Grid = 2D (rows+columns), Flexbox = 1D (row OR column)

---

## 📍 **Positioning**

### **Position Values**

**Definition:** Control element positioning: static (default flow), relative (offset from normal), absolute (relative to positioned parent), fixed (viewport), sticky (hybrid).

```css
static { } /* Default, normal flow */
relative { position: relative; top: 10px; } /* Offset from normal */
absolute { position: absolute; top: 50px; } /* Relative to positioned parent */
fixed { position: fixed; bottom: 20px; } /* Relative to viewport */
sticky { position: sticky; top: 0; } /* Hybrid relative/fixed */

```

### **Z-Index**

```css
.layer1 { position: relative; z-index: 1; }
.layer2 { position: relative; z-index: 2; }
/* Works on positioned elements AND flex/grid items */
/* <dialog>.showModal() and popovers render in the top layer — no z-index needed */

```

---

## 📱 **Responsive Design**

### **Media Queries**

```css
.container { width: 100%; }
@media (width >= 768px) { .container { max-width: 750px; } }
@media (width >= 1024px) { .container { max-width: 1200px; } }

```

### **Container Queries**

```css
.wrapper { container-type: inline-size; }
@container (width > 30rem) { .card { grid-template-columns: 10rem 1fr; } }
```

**Rule of thumb**: media queries for page layout + user preferences; container queries for components

**Mobile-first**: Start with mobile, add `min-width` breakpoints
**Breakpoints**: 768px (tablet), 1024px (desktop), 1200px (large)

### **Responsive Units**

```css
font-size: clamp(1rem, 0.75rem + 1.5vw, 1.5rem); /* min preferred max; rem term keeps zoom working */
width: min(100%, 800px);
height: max(200px, 50vh);

```

---

## 🎬 **Animations & Transitions**

### **Transitions**

```css
.button { background: blue; transition: all 0.3s ease; }
.button:hover { background: red; }

```

### **Animations**

```css
@keyframes slideIn {
  0% { transform: translateX(-100%); opacity: 0; }
  100% { transform: translateX(0); opacity: 1; }
}
.element { animation: slideIn 0.5s ease-in-out; }

```

**GPU-accelerated**: `transform`, `opacity` perform better than layout properties

**Respect users**: wrap non-essential motion in `@media (prefers-reduced-motion: no-preference)`

---

## ✨ **Modern CSS (2026)**

```css
/* :has() — style parent based on children (Baseline 2023) */
.field:has(input:user-invalid) { border-color: red; }

/* @layer — explicit cascade order (Baseline 2022) */
@layer reset, base, components, utilities;

/* Native nesting (Baseline 2023) — no &__suffix like Sass */
.card { & h2 { margin: 0; } &:hover { box-shadow: 0 2px 8px #0003; } }

/* Logical properties — RTL-safe */
.box { padding-inline: 1rem; margin-block: 2rem; inset-inline-start: 0; }

/* Modern color */
.btn { background: oklch(0.6 0.2 255); }
.btn:hover { background: color-mix(in oklch, currentColor 20%, transparent); }

/* Subgrid (Baseline 2023) */
.card { display: grid; grid-row: span 3; grid-template-rows: subgrid; }

/* View transitions (SPA widely supported; cross-document emerging) */
@view-transition { navigation: auto; }
```

### **Styling Approaches**

| Approach | Runtime cost | Notes |
|---|---|---|
| styled-components / Emotion | Runtime JS + style injection | Client Components only in RSC; styled-components in maintenance mode (2025) |
| CSS Modules | Zero | Scoped class names, plain CSS |
| Tailwind CSS | Zero | Utilities generated at build; v4 uses `@layer` |
| vanilla-extract / Panda / StyleX | Zero (build-time) | Type-safe CSS-in-JS authoring |

---

## 🔧 **CSS Variables & Functions**

### **Custom Properties**

```css
:root {
  --primary-color: #007bff;
  --spacing: 8px;
}
.element { color: var(--primary-color); margin: calc(var(--spacing) * 2); }

```

### **Functions**

```css
width: calc(100% - 40px);
background: linear-gradient(45deg, red, blue);
transform: translateX(50px) rotate(45deg);
filter: blur(5px) brightness(1.2);

```

---

## ⚡ **Performance**

### **Hardware Acceleration**

```css
.accelerated { will-change: transform; } /* only right before animating; translateZ(0) hack is legacy */
.smooth { transform: translateX(100px); } /* Better than left: 100px */
.offscreen { content-visibility: auto; contain-intrinsic-size: auto 500px; }

```

### **Efficient Selectors**

```css
/* Good */ .header .nav-item { }
/* Avoid */ div > ul > li > a.nav-link { }

```

**Use**: `transform`/`opacity` for animations, classes for styling, avoid deep selectors

---

## 🔑 **Key Differences**

| Concept | Difference |
|---------|------------|
| **margin** vs **padding** | Outside vs inside border |
| **display: none** vs **visibility: hidden** | Removed vs hidden (space preserved) |
| **em** vs **rem** | Parent font size vs root font size |
| **flex** vs **grid** | 1D (row OR column) vs 2D (rows AND columns) |
| **absolute** vs **fixed** | Parent-relative vs viewport-relative |
| **block** vs **inline-block** | Full width, new line vs flows with text, respects size |

---

## 🎯 **Common Patterns**

### **Centering**

```css
/* Flexbox */
.center { display: flex; justify-content: center; align-items: center; }
/* Grid */
.center { display: grid; place-items: center; }
/* Absolute */
.center { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); }

```

### **Responsive Grid**

```css
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; }

```

### **Sticky Header**

```css
.header { position: sticky; top: 0; z-index: 100; background: white; }

```

---

## ⚠️ **Common Gotchas**

```css
/* Box-sizing affects width */

* { box-sizing: border-box; }

/* Z-index needs a positioned element or a flex/grid item */
.positioned { position: relative; z-index: 1; }

/* Margin collapse vertically */
/* Adjacent vertical margins collapse to larger value */

/* Flexbox gap for spacing (better than margin) */
.flex { display: flex; gap: 20px; }

```

---

## 🚀 **Quick Tips**

1. **Box Model**: Understand content → padding → border → margin

2. **Specificity**: Inline (1000) > ID (100) > Class (10) > Element (1)

3. **Flexbox**: 1D layouts, use for components

4. **Grid**: 2D layouts, use for page structure

5. **Position**: Static (default), relative, absolute, fixed, sticky

6. **Responsive**: Mobile-first, use media queries with `min-width`

7. **Performance**: Use `transform`/`opacity` for animations

8. **Variables**: Use CSS custom properties for theming

---

## ⚡ **Last-Minute Review (5 minutes)**

### **Must-Know Concepts**

- **Box Model**: Content → Padding → Border → Margin

- **Specificity**: Inline (1000) > ID (100) > Class (10) > Element (1)

- **Flexbox**: 1D layout (row OR column), use for components

- **Grid**: 2D layout (rows AND columns), use for page structure

- **Position**: static (default), relative, absolute, fixed, sticky

- **Centering**: Flexbox (`justify-content: center; align-items: center`)

### **Quick Code Snippets**

```css
/* Centering */
.center { display: flex; justify-content: center; align-items: center; }

/* Responsive Grid */
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); }

/* Sticky Header */
.header { position: sticky; top: 0; z-index: 100; }

```

### **Common Gotchas**

- `box-sizing: border-box` includes padding+border in width

- `z-index` only works on positioned elements (and flex/grid items)

- `100vh` on mobile ≠ visible area — use `100dvh`/`100svh`

- Vertical margins collapse (larger value wins)

- `display: none` removes from flow, `visibility: hidden` keeps space

**Review Time**: 10-15 minutes | **Focus**: Box Model, Flexbox, Grid, Positioning, Responsive, Modern CSS ([details](./03-modern-css-features.md))

**Good luck! 🎉**
