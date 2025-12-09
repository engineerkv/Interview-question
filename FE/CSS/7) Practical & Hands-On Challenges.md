# 🛠️ 6. Practical & Hands-On Challenges (Q59–68)

---

## 📍 Navigation

<div align="center">

[Performance & Optimization](5%29%20Performance%20%26%20Optimization.md) • [Home: README](../README.md)

[📋 Cheatsheet](CSS%20Interview%20Cheatsheet.md]

</div>

---

---

## Q59. 🧭 Creating a responsive navigation menu

Build a responsive navigation that adapts to different screen sizes using CSS Grid for overall layout and Flexbox for menu items and alignment - combining Grid and Flexbox creates flexible, responsive navigation. Use CSS Grid for overall container structure, Flexbox for menu items and centering.

- **Trade-offs**: The catch is not ensuring keyboard navigation and screen reader compatibility - use efficient selectors and minimize reflows. Combining Grid and Flexbox creates flexible, responsive navigation, but watch out - start with mobile layout and enhance for larger screens (mobile-first).

Example:

```css
.nav-container {
  display: grid;
  grid-template-columns: auto 1fr auto;
  align-items: center;
  padding: 1rem;
  background: #333;
}
.nav-menu {
  display: flex;
  gap: 1rem;
  list-style: none;
}
@media (max-width: 768px) {
  .nav-menu { display: none; }
}

```

---

## Q60. 🎨 Creating a CSS-only carousel

Build a carousel component using only CSS with smooth slide transitions, navigation controls, and responsive design - CSS-only carousels use radio buttons for navigation. Use `transform: translateX()` for smooth slide effects.

- **Trade-offs**: The catch is use absolute positioning for controls and indicators - use radio buttons for state management without JavaScript. CSS-only carousels use radio buttons for navigation, but watch out - use flexbox for horizontal slide arrangement.

Example:

```css
.carousel {
  position: relative;
  width: 100%;
  max-width: 800px;
  margin: 0 auto;
  overflow: hidden;
}
.carousel-track {
  display: flex;
  transition: transform 0.3s ease;
}
.carousel-item {
  flex: 0 0 100%;
}

```

---

## Q61. 🎨 Creating a CSS-only modal

Create a modal dialog using only CSS with backdrop blur effect, smooth animations, and proper focus management - modals require focus management and keyboard navigation. Use `backdrop-filter: blur()` for modern glassmorphism effects.

- **Trade-offs**: The catch is ensure proper focus handling for accessibility - use appropriate z-index values for proper stacking. Modals require focus management and keyboard navigation, but watch out - use `scale()` for smooth modal appearance/disappearance.

Example:

```css
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0,0,0,0.5);
  backdrop-filter: blur(5px);
}
.modal {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: white;
  padding: 2rem;
  border-radius: 8px;
}

```

---

## Q62. 🎨 Creating a CSS-only tooltip

Build a tooltip component using only CSS with proper positioning, smooth animations, and responsive behavior - tooltips should work on all screen sizes. Use absolute positioning with transform for precise placement.

- **Trade-offs**: The catch is use `translateX()` and `translateY()` for smooth positioning - use `:hover` pseudo-class for tooltip visibility. Tooltips should work on all screen sizes, but watch out - use border properties to create tooltip arrows.

Example:

```css
.tooltip-container {
  position: relative;
  display: inline-block;
}
.tooltip {
  position: absolute;
  bottom: 100%;
  opacity: 0;
  transition: opacity 0.3s;
  pointer-events: none;
}
.tooltip-container:hover .tooltip {
  opacity: 1;
}

```

---

## Q63. 🎨 Creating a CSS-only accordion

Build an accordion component using only CSS with smooth expand/collapse animations and proper accessibility features - CSS-only accordions use checkbox inputs for state. Use `max-height` for smooth expand/collapse effects.

- **Trade-offs**: The catch is ensure proper ARIA attributes and keyboard navigation - use efficient selectors and avoid layout-triggering properties. CSS-only accordions use checkbox inputs for state, but watch out - use `transform: rotate()` for icon animations, checkbox input for state management.

Example:

```css
.accordion {
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
}
.accordion-content {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.3s ease;
}
.accordion-input:checked + .accordion-label + .accordion-content {
  max-height: 500px;
}

```

---

## Q64. 🧩 Creating a CSS-only tabs component

Create a tab component using only CSS with smooth content transitions, active states, and responsive design - CSS-only tabs require proper keyboard navigation. Use radio buttons for single-selection tab behavior.

- **Trade-offs**: The catch is use `:checked` pseudo-class for active tab styling - use flexbox for equal-width tab buttons. CSS-only tabs require proper keyboard navigation, but watch out - use `translateY()` for smooth content transitions.

Example:

```css
.tabs {
  max-width: 800px;
  margin: 0 auto;
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
}
.tab-button {
  padding: 1rem;
  border: none;
  background: #f0f0f0;
  cursor: pointer;
}
.tab-content {
  display: none;
  padding: 1rem;
}
.tab-input:checked + .tab-label + .tab-content {
  display: block;
}

```

---

## Q65. 🎨 Creating a CSS-only dropdown menu

Create a dropdown menu using only CSS with smooth animations, proper positioning, and accessibility features - CSS-only dropdowns require proper focus management. Use `position: absolute` for proper dropdown placement.

- **Trade-offs**: The catch is combine opacity and visibility for smooth fade effects - use checkbox input for state management without JavaScript. CSS-only dropdowns require proper focus management, but watch out - use `translateY()` for smooth slide-down effects.

Example:

```css
.dropdown {
  position: relative;
  display: inline-block;
}
.dropdown-menu {
  position: absolute;
  top: 100%;
  opacity: 0;
  visibility: hidden;
  transition: all 0.3s;
}
.dropdown-input:checked + .dropdown-label + .dropdown-menu {
  opacity: 1;
  visibility: visible;
}

```

---

## Q66. 🎨 Creating a CSS-only loading spinner

Create a loading spinner using only CSS with smooth rotation animations, customizable colors, and different sizes - GPU-accelerated properties ensure smooth animations. Use `transform: rotate()` for smooth spinning effects.

- **Trade-offs**: The catch is use `cubic-bezier()` for custom animation timing - use BEM methodology for different spinner variants. GPU-accelerated properties ensure smooth animations, but watch out - use border properties to create spinner appearance.

Example:

```css
.spinner {
  display: inline-block;
  width: 40px;
  height: 40px;
  border: 4px solid #f3f3f3;
  border-top: 4px solid #007bff;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

```

---

## Q67. 🎨 Creating a CSS-only progress bar

Build a progress bar using only CSS with smooth animations, customizable colors, and different states - CSS progress bars use animations or transitions for smooth updates. Use `width` transitions or animations for smooth progress updates.

- **Trade-offs**: The catch is ensure proper accessibility with ARIA attributes - use CSS variables for customizable colors. CSS progress bars use animations or transitions for smooth updates, but watch out - use gradients for visual appeal, `transform: scaleX()` for performance.

Example:

```css
.progress-container {
  width: 100%;
  height: 8px;
  background: #f0f0f0;
  border-radius: 4px;
  overflow: hidden;
}
.progress-bar {
  height: 100%;
  background: #007bff;
  transition: width 0.3s ease;
  width: 0%;
}
.progress-bar.animate {
  animation: progress 2s ease-in-out;
}
@keyframes progress {
  to { width: 100%; }
}

```

---

## Q68. 🧩 Creating a CSS-only card component

Create a reusable card component with smooth hover animations, transitions, and responsive design using modern CSS features - hover effects should work with keyboard navigation. Use `transform` and `box-shadow` for smooth, performant animations.

- **Trade-offs**: The catch is use consistent timing functions for cohesive animations - use GPU-accelerated properties for smooth 60fps animations. Hover effects should work with keyboard navigation, but watch out - apply `transform: scale()` to images for engaging hover effects.

Example:

```css
.card {
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  overflow: hidden;
  transition: all 0.3s ease;
}
.card:hover {
  box-shadow: 0 4px 16px rgba(0,0,0,0.2);
  transform: translateY(-4px);
}

```

---

---

## 📍 Navigation

<div align="center">

[Performance & Optimization](5%29%20Performance%20%26%20Optimization.md) • [Home: README](../README.md)

[📋 Cheatsheet](CSS%20Interview%20Cheatsheet.md]

</div>

---
