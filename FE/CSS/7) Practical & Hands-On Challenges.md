# 🎨 7. Practical & Hands-On Challenges (Q91–100)

---

## 91) Create a responsive navigation menu using CSS Grid and Flexbox.

Build a responsive navigation that adapts to different screen sizes using CSS Grid for overall layout and Flexbox for menu items and alignment.

```css
.nav-container { display: grid; grid-template-columns: auto 1fr auto; align-items: center; padding: 1rem; background: #333; }
.nav-menu { display: flex; gap: 1rem; list-style: none; }
@media (max-width: 768px) { .nav-menu { display: none; } }
```

- **Core Strategy**: Use CSS Grid for overall container structure, Flexbox for menu items and centering
- **Real-World Use**: Start with mobile layout and enhance for larger screens (mobile-first)
- **Common Mistake**: Not ensuring keyboard navigation and screen reader compatibility
- **Optimization**: Use efficient selectors and minimize reflows
- **Interview Tip**: Explain that combining Grid and Flexbox creates flexible, responsive navigation

---

## 92) Build a card component with hover effects and animations.

Create a reusable card component with smooth hover animations, transitions, and responsive design using modern CSS features.

```css
.card { background: white; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); overflow: hidden; transition: all 0.3s ease; }
.card:hover { box-shadow: 0 4px 16px rgba(0,0,0,0.2); transform: translateY(-4px); }
```

- **Core Techniques**: Use `transform` and `box-shadow` for smooth, performant animations
- **Real-World Use**: Apply `transform: scale()` to images for engaging hover effects
- **Common Mistake**: Use consistent timing functions for cohesive animations
- **Optimization**: Use GPU-accelerated properties for smooth 60fps animations
- **Interview Tip**: Explain that hover effects should work with keyboard navigation

---

## 93) Implement a CSS-only modal dialog with backdrop blur.

Create a modal dialog using only CSS with backdrop blur effect, smooth animations, and proper focus management.

```css
.modal-overlay { position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.5); backdrop-filter: blur(5px); }
.modal { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); background: white; padding: 2rem; border-radius: 8px; }
```

- **Core Features**: Use `backdrop-filter: blur()` for modern glassmorphism effects
- **Real-World Use**: Use `scale()` for smooth modal appearance/disappearance
- **Common Mistake**: Ensure proper focus handling for accessibility
- **Optimization**: Use appropriate z-index values for proper stacking
- **Interview Tip**: Explain that modals require focus management and keyboard navigation

---

## 94) Create a CSS-only accordion component with smooth animations.

Build an accordion component using only CSS with smooth expand/collapse animations and proper accessibility features.

```css
.accordion { border: 1px solid #ddd; border-radius: 8px; overflow: hidden; }
.accordion-content { max-height: 0; overflow: hidden; transition: max-height 0.3s ease; }
.accordion-input:checked + .accordion-label + .accordion-content { max-height: 500px; }
```

- **Core Technique**: Use `max-height` for smooth expand/collapse effects
- **Real-World Use**: Use `transform: rotate()` for icon animations, checkbox input for state management
- **Common Mistake**: Ensure proper ARIA attributes and keyboard navigation
- **Optimization**: Use efficient selectors and avoid layout-triggering properties
- **Interview Tip**: Explain that CSS-only accordions use checkbox inputs for state

---

## 95) Build a responsive image gallery with CSS Grid and hover effects.

Create a responsive image gallery using CSS Grid with masonry-like layout, hover effects, and smooth transitions.

```css
.gallery {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
  padding: 20px;
}
```

- **Core Layout**: Use `auto-fit` and `minmax()` for responsive grid columns
- **Real-World Use**: Use `column-count` for Pinterest-like masonry layout
- **Advanced Features**: Use absolute positioning and gradients for overlay effects
- **Optimization**: Apply `transform: scale()` for engaging hover effects
- **Interview Tip**: Explain that Grid's auto-fit creates responsive galleries automatically

---

## 96) Implement a CSS-only dropdown menu with animations.

Create a dropdown menu using only CSS with smooth animations, proper positioning, and accessibility features.

```css
.dropdown { position: relative; display: inline-block; }
.dropdown-menu { position: absolute; top: 100%; opacity: 0; visibility: hidden; transition: all 0.3s; }
.dropdown-input:checked + .dropdown-label + .dropdown-menu { opacity: 1; visibility: visible; }
```

- **Core Positioning**: Use `position: absolute` for proper dropdown placement
- **Real-World Use**: Use `translateY()` for smooth slide-down effects
- **Advanced Technique**: Combine opacity and visibility for smooth fade effects
- **Optimization**: Use checkbox input for state management without JavaScript
- **Interview Tip**: Explain that CSS-only dropdowns require proper focus management

---

## 97) Create a CSS-only carousel with smooth transitions.

Build a carousel component using only CSS with smooth slide transitions, navigation controls, and responsive design.

```css
.carousel { position: relative; width: 100%; max-width: 800px; margin: 0 auto; overflow: hidden; }
.carousel-track { display: flex; transition: transform 0.3s ease; }
.carousel-item { flex: 0 0 100%; }
```

- **Core Animation**: Use `transform: translateX()` for smooth slide effects
- **Real-World Use**: Use flexbox for horizontal slide arrangement
- **Advanced Features**: Use absolute positioning for controls and indicators
- **Optimization**: Use radio buttons for state management without JavaScript
- **Interview Tip**: Explain that CSS-only carousels use radio buttons for navigation

---

## 98) Build a CSS-only tab component with smooth transitions.

Create a tab component using only CSS with smooth content transitions, active states, and responsive design.

```css
.tabs { max-width: 800px; margin: 0 auto; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; }
.tab-button { padding: 1rem; border: none; background: #f0f0f0; cursor: pointer; }
.tab-content { display: none; padding: 1rem; }
.tab-input:checked + .tab-label + .tab-content { display: block; }
```

- **Core Technique**: Use radio buttons for single-selection tab behavior
- **Real-World Use**: Use `translateY()` for smooth content transitions
- **Advanced Feature**: Use `:checked` pseudo-class for active tab styling
- **Optimization**: Use flexbox for equal-width tab buttons
- **Interview Tip**: Explain that CSS-only tabs require proper keyboard navigation

---

## 99) Implement a CSS-only loading spinner with animations.

Create a loading spinner using only CSS with smooth rotation animations, customizable colors, and different sizes.

```css
.spinner { display: inline-block; width: 40px; height: 40px; border: 4px solid #f3f3f3; border-top: 4px solid #007bff; border-radius: 50%; animation: spin 1s linear infinite; }
@keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
```

- **Core Technique**: Use `transform: rotate()` for smooth spinning effects
- **Real-World Use**: Use border properties to create spinner appearance
- **Advanced Feature**: Use `cubic-bezier()` for custom animation timing
- **Optimization**: Use BEM methodology for different spinner variants
- **Interview Tip**: Explain that GPU-accelerated properties ensure smooth animations

---

## 100) Create a CSS-only tooltip with positioning and animations.

Build a tooltip component using only CSS with proper positioning, smooth animations, and responsive behavior.

```css
.tooltip-container { position: relative; display: inline-block; }
.tooltip { position: absolute; bottom: 100%; opacity: 0; transition: opacity 0.3s; pointer-events: none; }
.tooltip-container:hover .tooltip { opacity: 1; }
```

- **Core Positioning**: Use absolute positioning with transform for precise placement
- **Real-World Use**: Use border properties to create tooltip arrows
- **Advanced Feature**: Use `translateX()` and `translateY()` for smooth positioning
- **Optimization**: Use `:hover` pseudo-class for tooltip visibility
- **Interview Tip**: Explain that tooltips should work on all screen sizes

---
