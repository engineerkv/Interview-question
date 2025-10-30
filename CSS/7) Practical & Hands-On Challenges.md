# 🎨 7. Practical & Hands-On Challenges (Q91–100)

## 91) Create a responsive navigation menu using CSS Grid and Flexbox.

Concept:
Build a responsive navigation that adapts to different screen sizes using CSS Grid for overall layout and Flexbox for menu items and alignment.

Example:
```css
.nav-container {
  display: grid;
  grid-template-columns: auto 1fr auto;
  align-items: center;
  padding: 1rem;
  background: #333;
```

Deep Insight:
- **Grid Layout**: Use CSS Grid for overall container structure and responsive behavior
- **Flexbox Alignment**: Use Flexbox for menu items and centering content
- **Mobile-First**: Start with mobile layout and enhance for larger screens
- **Accessibility**: Ensure keyboard navigation and screen reader compatibility
- **Performance**: Use efficient selectors and minimize reflows

## 92) Build a card component with hover effects and animations.

Concept:
Create a reusable card component with smooth hover animations, transitions, and responsive design using modern CSS features.

Example:
```css
.card {
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  overflow: hidden;
  transition: all 0.3s ease;
```

Deep Insight:
- **Hover Effects**: Use `transform` and `box-shadow` for smooth, performant animations
- **Image Scaling**: Apply `transform: scale()` to images for engaging hover effects
- **Transition Timing**: Use consistent timing functions for cohesive animations
- **Accessibility**: Ensure hover effects work with keyboard navigation
- **Performance**: Use GPU-accelerated properties for smooth 60fps animations

## 93) Implement a CSS-only modal dialog with backdrop blur.

Concept:
Create a modal dialog using only CSS with backdrop blur effect, smooth animations, and proper focus management.

Example:
```css
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
```

Deep Insight:
- **Backdrop Filter**: Use `backdrop-filter: blur()` for modern glassmorphism effects
- **Transform Animations**: Use `scale()` for smooth modal appearance/disappearance
- **Focus Management**: Ensure proper focus handling for accessibility
- **Z-Index Layering**: Use appropriate z-index values for proper stacking
- **Responsive Design**: Ensure modal works on all screen sizes

## 94) Create a CSS-only accordion component with smooth animations.

Concept:
Build an accordion component using only CSS with smooth expand/collapse animations and proper accessibility features.

Example:
```css
.accordion {
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
}

```

Deep Insight:
- **Max-Height Animation**: Use `max-height` for smooth expand/collapse effects
- **Transform Rotations**: Use `transform: rotate()` for icon animations
- **CSS-Only**: Use checkbox input for state management without JavaScript
- **Accessibility**: Ensure proper ARIA attributes and keyboard navigation
- **Performance**: Use efficient selectors and avoid layout-triggering properties

## 95) Build a responsive image gallery with CSS Grid and hover effects.

Concept:
Create a responsive image gallery using CSS Grid with masonry-like layout, hover effects, and smooth transitions.

Example:
```css
.gallery {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
  padding: 20px;
}
```

Deep Insight:
- **Grid Layout**: Use `auto-fit` and `minmax()` for responsive grid columns
- **Masonry Effect**: Use `column-count` for Pinterest-like layout
- **Hover Overlays**: Use absolute positioning and gradients for overlay effects
- **Image Scaling**: Apply `transform: scale()` for engaging hover effects
- **Responsive Design**: Adapt layout for different screen sizes

## 96) Implement a CSS-only dropdown menu with animations.

Concept:
Create a dropdown menu using only CSS with smooth animations, proper positioning, and accessibility features.

Example:
```css
.dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-toggle {
```

Deep Insight:
- **Positioning**: Use `position: absolute` for proper dropdown placement
- **Transform Animations**: Use `translateY()` for smooth slide-down effects
- **Opacity Transitions**: Combine opacity and visibility for smooth fade effects
- **CSS-Only**: Use checkbox input for state management without JavaScript
- **Accessibility**: Ensure proper focus management and keyboard navigation

## 97) Create a CSS-only carousel with smooth transitions.

Concept:
Build a carousel component using only CSS with smooth slide transitions, navigation controls, and responsive design.

Example:
```css
.carousel {
  position: relative;
  width: 100%;
  max-width: 800px;
  margin: 0 auto;
  overflow: hidden;
```

Deep Insight:
- **Transform Animations**: Use `transform: translateX()` for smooth slide effects
- **Flexbox Layout**: Use flexbox for horizontal slide arrangement
- **Positioning**: Use absolute positioning for controls and indicators
- **CSS-Only**: Use radio buttons for state management without JavaScript
- **Responsive Design**: Ensure carousel works on all screen sizes

## 98) Build a CSS-only tab component with smooth transitions.

Concept:
Create a tab component using only CSS with smooth content transitions, active states, and responsive design.

Example:
```css
.tabs {
  max-width: 800px;
  margin: 0 auto;
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
```

Deep Insight:
- **Radio Button State**: Use radio buttons for single-selection tab behavior
- **Transform Animations**: Use `translateY()` for smooth content transitions
- **Active States**: Use `:checked` pseudo-class for active tab styling
- **Flexbox Layout**: Use flexbox for equal-width tab buttons
- **Accessibility**: Ensure proper keyboard navigation and screen reader support

## 99) Implement a CSS-only loading spinner with animations.

Concept:
Create a loading spinner using only CSS with smooth rotation animations, customizable colors, and different sizes.

Example:
```css
.spinner {
  display: inline-block;
  width: 40px;
  height: 40px;
  border: 4px solid #f3f3f3;
  border-top: 4px solid #007bff;
```

Deep Insight:
- **Rotation Animation**: Use `transform: rotate()` for smooth spinning effects
- **Border Technique**: Use border properties to create spinner appearance
- **Keyframe Timing**: Use `cubic-bezier()` for custom animation timing
- **Modifier Classes**: Use BEM methodology for different spinner variants
- **Performance**: Use GPU-accelerated properties for smooth animations

## 100) Create a CSS-only tooltip with positioning and animations.

Concept:
Build a tooltip component using only CSS with proper positioning, smooth animations, and responsive behavior.

Example:
```css
.tooltip-container {
  position: relative;
  display: inline-block;
}

.tooltip-trigger {
```

Deep Insight:
- **Positioning**: Use absolute positioning with transform for precise placement
- **Arrow Creation**: Use border properties to create tooltip arrows
- **Transform Animations**: Use `translateX()` and `translateY()` for smooth positioning
- **Hover States**: Use `:hover` pseudo-class for tooltip visibility
- **Responsive Design**: Ensure tooltips work on all screen sizes
