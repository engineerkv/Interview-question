# 🎨 CSS Interview Cheatsheet

> **Quick Reference Guide** - Essential CSS concepts, selectors, layouts, and modern features for interviews

---

## 📋 **Table of Contents**

- [CSS Basics](#-css-basics)
- [Selectors & Specificity](#-selectors--specificity)
- [Box Model & Layout](#-box-model--layout)
- [Flexbox & Grid](#-flexbox--grid)
- [Positioning & Display](#-positioning--display)
- [Responsive Design](#-responsive-design)
- [Animations & Transitions](#-animations--transitions)
- [CSS Variables & Functions](#-css-variables--functions)
- [Performance & Optimization](#-performance--optimization)
- [Modern CSS Features](#-modern-css-features)

---

## 🧠 **CSS Basics**

### **CSS Syntax**
```css
selector {
  property: value;
  property: value;
}

/* Comments */
/* Multi-line
   comments */
```

### **Ways to Include CSS**
```html
<!-- External CSS -->
<link rel="stylesheet" href="styles.css">

<!-- Internal CSS -->
<style>
  body { margin: 0; }
</style>

<!-- Inline CSS -->
<div style="color: red;">Inline styling</div>
```

### **CSS Units**
```css
/* Absolute units */
width: 100px;        /* Pixels */
width: 2in;          /* Inches */
width: 5cm;          /* Centimeters */

/* Relative units */
width: 50%;          /* Percentage of parent */
width: 2em;          /* 2x parent font size */
width: 2rem;         /* 2x root font size */
width: 50vw;         /* 50% of viewport width */
width: 50vh;         /* 50% of viewport height */
```

---

## 🎯 **Selectors & Specificity**

### **Basic Selectors**
```css
/* Element selector */
p { color: blue; }

/* Class selector */
.highlight { background: yellow; }

/* ID selector */
#header { font-size: 24px; }

/* Universal selector */
* { box-sizing: border-box; }
```

### **Combinators**
```css
/* Descendant selector */
div p { color: red; }

/* Child selector */
div > p { color: blue; }

/* Adjacent sibling */
h1 + p { margin-top: 0; }

/* General sibling */
h1 ~ p { color: green; }
```

### **Pseudo-classes & Pseudo-elements**
```css
/* Pseudo-classes */
a:hover { color: red; }
input:focus { border-color: blue; }
li:first-child { font-weight: bold; }
li:nth-child(2n) { background: gray; }

/* Pseudo-elements */
p::before { content: "→ "; }
p::after { content: " ←"; }
p::first-line { font-weight: bold; }
```

### **Specificity Calculation**
```css
/* Specificity: 0,0,0,1 (element) */
p { color: black; }

/* Specificity: 0,0,1,0 (class) */
.highlight { color: yellow; }

/* Specificity: 0,1,0,0 (ID) */
#special { color: red; }

/* Specificity: 1,0,0,0 (inline style) */
<div style="color: purple;">Inline</div>

/* Specificity: 0,0,0,0 (inherited) */
/* Inherited from parent */
```

---

## 📦 **Box Model & Layout**

### **Box Model Properties**
```css
.element {
  width: 200px;        /* Content width */
  height: 100px;       /* Content height */
  padding: 20px;       /* Space inside border */
  border: 2px solid black; /* Border around padding */
  margin: 10px;        /* Space outside border */
  box-sizing: border-box;  /* Include padding/border in width */
}
```

### **Display Properties**
```css
/* Block elements */
.block { display: block; }        /* Full width, new line */

/* Inline elements */
.inline { display: inline; }      /* Flows with text */

/* Inline-block elements */
.inline-block { display: inline-block; } /* Best of both */

/* Flexbox */
.flex { display: flex; }

/* Grid */
.grid { display: grid; }

/* None */
.hidden { display: none; }        /* Completely removed */
```

### **Margin & Padding**
```css
/* Individual sides */
margin-top: 10px;
margin-right: 20px;
margin-bottom: 10px;
margin-left: 30px;

/* Shorthand (top right bottom left) */
margin: 10px 20px 10px 30px;

/* Shorthand (top/bottom left/right) */
margin: 10px 20px;

/* All sides */
margin: 10px;

/* Auto centering */
margin: 0 auto; /* Centers block elements */
```

---

## 🔧 **Flexbox & Grid**

### **Flexbox Properties**
```css
.container {
  display: flex;
  flex-direction: row;        /* row, column, row-reverse, column-reverse */
  justify-content: center;    /* Main axis alignment */
  align-items: center;        /* Cross axis alignment */
  flex-wrap: wrap;           /* wrap, nowrap, wrap-reverse */
  gap: 20px;                 /* Space between items */
}

.item {
  flex: 1;                   /* flex-grow flex-shrink flex-basis */
  flex-grow: 1;              /* How much to grow */
  flex-shrink: 0;            /* How much to shrink */
  flex-basis: 200px;         /* Initial size */
  align-self: flex-start;    /* Override container alignment */
}
```

### **CSS Grid Properties**
```css
.container {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;  /* Column sizes */
  grid-template-rows: 100px 200px;     /* Row sizes */
  gap: 20px;                           /* Gap between items */
  grid-template-areas: 
    "header header header"
    "sidebar main main"
    "footer footer footer";
}

.item {
  grid-column: 1 / 3;         /* Start at 1, end at 3 */
  grid-row: 1;                /* Row 1 */
  grid-area: header;          /* Named grid area */
  justify-self: center;       /* Align within grid cell */
  align-self: start;          /* Align within grid cell */
}
```

---

## 📍 **Positioning & Display**

### **Position Values**
```css
.static { position: static; }     /* Default, normal flow */
.relative { position: relative; } /* Relative to normal position */
.absolute { position: absolute; } /* Relative to positioned ancestor */
.fixed { position: fixed; }       /* Relative to viewport */
.sticky { position: sticky; }     /* Switches between relative/fixed */
```

### **Z-Index & Stacking**
```css
.layer1 { z-index: 1; }
.layer2 { z-index: 2; }
.layer3 { z-index: 3; }

/* Only works on positioned elements */
.positioned {
  position: relative;
  z-index: 10;
}
```

### **Visibility & Display**
```css
.hidden-visibility { visibility: hidden; } /* Hidden but takes space */
.hidden-display { display: none; }         /* Completely removed */
.visible { visibility: visible; }          /* Default visibility */
```

---

## 📱 **Responsive Design**

### **Media Queries**
```css
/* Mobile first approach */
.container {
  width: 100%;
  padding: 10px;
}

/* Tablet */
@media (min-width: 768px) {
  .container {
    width: 750px;
    padding: 20px;
  }
}

/* Desktop */
@media (min-width: 1024px) {
  .container {
    width: 1200px;
    padding: 30px;
  }
}

/* High DPI displays */
@media (-webkit-min-device-pixel-ratio: 2) {
  .logo { background-image: url('logo@2x.png'); }
}
```

### **Responsive Units**
```css
.responsive-text {
  font-size: clamp(16px, 4vw, 24px); /* Min, preferred, max */
  width: min(100%, 800px);           /* Smaller of two values */
  height: max(200px, 50vh);          /* Larger of two values */
}
```

---

## 🎬 **Animations & Transitions**

### **Transitions**
```css
.button {
  background-color: blue;
  transition: background-color 0.3s ease;
}

.button:hover {
  background-color: red;
}

/* Multiple properties */
.element {
  transition: all 0.3s ease;
  /* Or specify individually */
  transition: 
    background-color 0.3s ease,
    transform 0.2s ease-in-out;
}
```

### **Animations**
```css
@keyframes slideIn {
  from {
    transform: translateX(-100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

.animated {
  animation: slideIn 0.5s ease-out;
  animation-fill-mode: forwards;
  animation-delay: 0.2s;
}
```

---

## 🔧 **CSS Variables & Functions**

### **CSS Custom Properties**
```css
:root {
  --primary-color: #007bff;
  --secondary-color: #6c757d;
  --font-size-base: 16px;
  --spacing-unit: 8px;
}

.element {
  color: var(--primary-color);
  font-size: var(--font-size-base);
  margin: calc(var(--spacing-unit) * 2);
}

/* Fallback values */
.element {
  color: var(--primary-color, #000);
}
```

### **CSS Functions**
```css
.element {
  width: calc(100% - 20px);           /* Mathematical calculations */
  background: linear-gradient(45deg, red, blue); /* Gradients */
  transform: rotate(45deg) scale(1.2); /* Transformations */
  filter: blur(2px) brightness(1.5);   /* Visual effects */
  clip-path: polygon(0 0, 100% 0, 50% 100%); /* Clipping */
}
```

---

## ⚡ **Performance & Optimization**

### **Critical CSS**
```html
<!-- Inline critical CSS -->
<style>
  .above-fold { /* Critical styles */ }
</style>

<!-- Load non-critical CSS asynchronously -->
<link rel="preload" href="styles.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
```

### **Hardware Acceleration**
```css
.accelerated {
  transform: translateZ(0); /* Force hardware acceleration */
  will-change: transform;   /* Hint browser about changes */
}

/* Use transform instead of changing layout properties */
.smooth {
  transform: translateX(100px); /* Better than left: 100px */
}
```

### **Efficient Selectors**
```css
/* Good - specific and fast */
.header .nav-item { }

/* Avoid - slow and overly specific */
div > ul > li > a.nav-link { }

/* Use classes for styling */
.button-primary { }
```

---

## 🚀 **Modern CSS Features**

### **Container Queries**
```css
.card-container {
  container-type: inline-size;
}

@container (min-width: 300px) {
  .card {
    display: flex;
    flex-direction: row;
  }
}
```

### **CSS Nesting**
```css
.card {
  padding: 20px;
  
  .title {
    font-size: 24px;
    
    &:hover {
      color: blue;
    }
  }
  
  @media (max-width: 768px) {
    padding: 10px;
  }
}
```

### **Logical Properties**
```css
.element {
  margin-inline-start: 20px;  /* Left in LTR, right in RTL */
  margin-block-end: 10px;     /* Bottom in horizontal writing */
  border-inline: 1px solid;   /* Left and right borders */
  padding-block: 20px;        /* Top and bottom padding */
}
```

### **Advanced Selectors**
```css
/* :is() - grouping selector */
:is(h1, h2, h3) { color: blue; }

/* :where() - zero specificity */
:where(.button, .link) { text-decoration: none; }

/* :has() - parent selector */
.card:has(.button) { border: 2px solid blue; }
```

---

## 🎯 **Common Patterns**

### **Center Elements**
```css
/* Flexbox centering */
.flex-center {
  display: flex;
  justify-content: center;
  align-items: center;
}

/* Grid centering */
.grid-center {
  display: grid;
  place-items: center;
}

/* Absolute centering */
.absolute-center {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
```

### **Responsive Grid**
```css
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
}
```

### **Sticky Header**
```css
.header {
  position: sticky;
  top: 0;
  z-index: 100;
  background: white;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
```

---

## 🔑 **Interview Keywords**

### **Must Know Concepts**
- **Box Model** - Content, padding, border, margin
- **Specificity** - How CSS determines which styles apply
- **Cascade** - How styles are inherited and overridden
- **Flexbox** - One-dimensional layout system
- **Grid** - Two-dimensional layout system
- **Responsive Design** - Adapting to different screen sizes
- **Performance** - Optimizing CSS for speed

### **Common Gotchas**
```css
/* Box-sizing affects width calculation */
* { box-sizing: border-box; }

/* Z-index only works on positioned elements */
.positioned { position: relative; z-index: 1; }

/* Margin collapse in vertical direction */
.margin-collapse { margin: 20px 0; }

/* Flexbox gap vs margin for spacing */
.flex { display: flex; gap: 20px; }
```

### **Key Differences**
| Property | Difference |
|----------|------------|
| `margin` vs `padding` | Outside vs inside border |
| `display: none` vs `visibility: hidden` | Removed vs hidden |
| `em` vs `rem` | Parent vs root font size |
| `flex` vs `grid` | 1D vs 2D layout |
| `position: absolute` vs `fixed` | Parent vs viewport |

---

## 🚀 **Final Tips**

1. **Practice Layouts** - Master Flexbox and Grid
2. **Understand Specificity** - Know how CSS cascade works
3. **Think Responsive** - Mobile-first approach
4. **Optimize Performance** - Use efficient selectors and properties
5. **Stay Current** - Learn modern CSS features
6. **Test Cross-Browser** - Ensure compatibility

**Good luck with your CSS interview! 🎉**
