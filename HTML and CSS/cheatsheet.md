# 🎨 HTML & CSS Cheatsheet - Interview Quick Reference

## 🚀 Quick Reference Guide

### 🟢 HTML Fundamentals
- **Semantic HTML**: Use proper tags for meaning (header, nav, main, article, section, aside, footer)
- **Accessibility**: ARIA attributes, alt text, keyboard navigation
- **SEO**: Meta tags, structured data, semantic markup
- **Forms**: Input types, validation, accessibility

### 🎨 CSS Basics & Layout
- **Box Model**: content, padding, border, margin
- **Display**: block, inline, inline-block, flex, grid
- **Positioning**: static, relative, absolute, fixed, sticky
- **Flexbox**: Main axis, cross axis, justify-content, align-items
- **Grid**: Grid container, grid items, grid lines, grid areas

### ✨ Advanced CSS & Animations
- **Transitions**: property, duration, timing-function, delay
- **Animations**: @keyframes, animation-name, animation-duration
- **Transforms**: translate, rotate, scale, skew
- **3D Effects**: perspective, transform-style, backface-visibility

### 📱 Responsive Design
- **Media Queries**: @media (min-width), @media (max-width)
- **Breakpoints**: mobile-first, desktop-first approaches
- **Viewport**: meta viewport tag, device-width
- **Flexible Units**: rem, em, vw, vh, %

### 🎯 Tailwind CSS
- **Utility Classes**: spacing, colors, typography, layout
- **Responsive**: sm:, md:, lg:, xl: prefixes
- **State Variants**: hover:, focus:, active:, disabled:
- **Customization**: config file, custom utilities

### 🧩 UI Libraries
- **Component Libraries**: Material-UI, Ant Design, Chakra UI
- **CSS Frameworks**: Bootstrap, Bulma, Foundation
- **Design Systems**: Storybook, design tokens
- **Accessibility**: WCAG guidelines, screen readers

## 🎯 Common Patterns

### Flexbox Layout
```css
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  gap: 1rem;
}
```

### Grid Layout
```css
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1rem;
}
```

### Responsive Design
```css
@media (min-width: 768px) {
  .container {
    max-width: 1200px;
    margin: 0 auto;
  }
}
```

### CSS Animations
```css
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

.animate {
  animation: fadeIn 0.5s ease-out;
}
```

### Tailwind Utilities
```html
<div class="flex items-center justify-between p-4 bg-blue-500 text-white rounded-lg shadow-md hover:bg-blue-600 transition-colors">
  <h2 class="text-xl font-bold">Title</h2>
  <button class="px-4 py-2 bg-white text-blue-500 rounded hover:bg-gray-100">Click</button>
</div>
```

## 📊 CSS Properties Cheatsheet

### Layout Properties
| Property | Values | Description |
|----------|--------|-------------|
| `display` | block, inline, flex, grid | How element is displayed |
| `position` | static, relative, absolute, fixed | Element positioning |
| `float` | left, right, none | Float element |
| `clear` | left, right, both, none | Clear floats |

### Flexbox Properties
| Property | Values | Description |
|----------|--------|-------------|
| `justify-content` | flex-start, center, space-between | Main axis alignment |
| `align-items` | flex-start, center, stretch | Cross axis alignment |
| `flex-direction` | row, column, row-reverse | Flex direction |
| `flex-wrap` | nowrap, wrap, wrap-reverse | Wrap behavior |

### Grid Properties
| Property | Values | Description |
|----------|--------|-------------|
| `grid-template-columns` | 1fr, repeat(3, 1fr) | Column definitions |
| `grid-template-rows` | auto, 1fr, 200px | Row definitions |
| `grid-gap` | 1rem, 20px | Gap between items |
| `grid-area` | header, main, footer | Grid area name |

### Typography Properties
| Property | Values | Description |
|----------|--------|-------------|
| `font-family` | Arial, sans-serif | Font family |
| `font-size` | 16px, 1rem, 1.2em | Font size |
| `font-weight` | normal, bold, 400, 700 | Font weight |
| `line-height` | 1.5, 24px | Line height |

### Color Properties
| Property | Values | Description |
|----------|--------|-------------|
| `color` | #333, rgb(51,51,51) | Text color |
| `background-color` | #fff, transparent | Background color |
| `border-color` | #ccc, currentColor | Border color |
| `opacity` | 0.5, 1 | Element opacity |

## 🎨 Design Principles

### Visual Hierarchy
- **Typography**: Use different font sizes and weights
- **Color**: Use color to create emphasis and grouping
- **Spacing**: Use white space to separate content
- **Contrast**: Ensure sufficient contrast for readability

### Accessibility Guidelines
- **Color Contrast**: Minimum 4.5:1 ratio for normal text
- **Keyboard Navigation**: All interactive elements accessible via keyboard
- **Screen Readers**: Use semantic HTML and ARIA attributes
- **Focus Indicators**: Clear focus states for keyboard users

### Performance Optimization
- **CSS Minification**: Remove whitespace and comments
- **Critical CSS**: Inline above-the-fold styles
- **CSS Splitting**: Load only necessary styles
- **Preloading**: Use rel="preload" for critical resources

## 🚀 Interview Tips

### HTML Best Practices
1. **Semantic HTML**: Use appropriate tags for content structure
2. **Accessibility**: Include alt text, ARIA labels, keyboard navigation
3. **SEO**: Use proper heading hierarchy, meta tags
4. **Performance**: Optimize images, use lazy loading

### CSS Best Practices
1. **Mobile First**: Start with mobile styles, then add desktop
2. **BEM Methodology**: Use Block__Element--Modifier naming
3. **CSS Variables**: Use custom properties for theming
4. **Component Architecture**: Organize styles by components

### Common Interview Questions
- **Box Model**: Explain content, padding, border, margin
- **Flexbox vs Grid**: When to use each layout method
- **Responsive Design**: Mobile-first vs desktop-first approach
- **CSS Specificity**: How browsers determine which styles to apply
- **Performance**: How to optimize CSS for faster loading

---

*This cheatsheet covers essential HTML and CSS concepts for interview preparation, including layout techniques, responsive design, and modern CSS features.*
