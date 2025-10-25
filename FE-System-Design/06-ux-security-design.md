# 🏗️ Frontend System Design Interview Notes (2025 Edition)

## 🧱 Section 6 — UX, Security & Design Systems — Q111-Q135

---

### 111. 🧱 What is accessibility (a11y), and why is it essential in frontend design?

**🧠 Concept**

Accessibility ensures web applications are usable by people with disabilities, providing equal access to information and functionality.

**💻 Example**

```html
<!-- Accessible button -->
<button 
  aria-label="Close dialog"
  aria-describedby="close-help"
  onclick="closeDialog()"
>
  ×
</button>
<span id="close-help">Closes the current dialog</span>

<!-- Accessible form -->
<label for="email">Email Address</label>
<input 
  type="email" 
  id="email" 
  required 
  aria-describedby="email-error"
/>
<div id="email-error" role="alert"></div>
```

**💬 Explanation + Insight**

- **Equal Access** - Ensure all users can access content
- **Legal Compliance** - Meet accessibility standards and laws
- **User Experience** - Improve experience for all users
- **SEO Benefits** - Better search engine optimization
- **Best Practice** - Essential for modern web development

---

### 112. 🧱 What are ARIA attributes, and how are they used?

**🧠 Concept**

ARIA (Accessible Rich Internet Applications) attributes provide additional information to screen readers and assistive technologies.

**💻 Example**

```html
<!-- ARIA attributes for accessibility -->
<div 
  role="button" 
  tabindex="0"
  aria-pressed="false"
  aria-label="Toggle menu"
  onclick="toggleMenu()"
>
  Menu
</div>

<!-- ARIA live region for dynamic content -->
<div 
  aria-live="polite" 
  aria-atomic="true"
  id="status-message"
>
  Loading...
</div>
```

**💬 Explanation + Insight**

- **Screen Reader Support** - Provide information to assistive technologies
- **Semantic Meaning** - Add semantic meaning to elements
- **Dynamic Content** - Announce changes to screen readers
- **User Navigation** - Help users navigate complex interfaces
- **Standards Compliance** - Meet accessibility guidelines

---

### 113. 🧱 How do you make web apps keyboard-navigable?

**🧠 Concept**

Keyboard navigation allows users to navigate and interact with web applications using only the keyboard, essential for accessibility.

**💻 Example**

```javascript
// Keyboard navigation implementation
function handleKeyDown(event) {
  switch(event.key) {
    case 'Tab':
      // Focus management
      if (event.shiftKey) {
        focusPrevious();
      } else {
        focusNext();
      }
      break;
    case 'Enter':
    case ' ':
      // Activate focused element
      activateFocused();
      break;
    case 'Escape':
      // Close modals or menus
      closeModal();
      break;
  }
}

// Focus trap for modals
function trapFocus(modal) {
  const focusableElements = modal.querySelectorAll(
    'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
  );
  const firstElement = focusableElements[0];
  const lastElement = focusableElements[focusableElements.length - 1];
  
  firstElement.focus();
}
```

**💬 Explanation + Insight**

- **Tab Navigation** - Use Tab key for navigation
- **Focus Management** - Manage focus order and visibility
- **Keyboard Shortcuts** - Provide keyboard alternatives
- **Focus Traps** - Keep focus within modals
- **User Experience** - Essential for keyboard users

---

### 114. 🧱 What are WCAG guidelines, and what levels (A, AA, AAA) mean?

**🧠 Concept**

WCAG (Web Content Accessibility Guidelines) provide standards for web accessibility with three levels of compliance.

**💻 Example**

```html
<!-- WCAG Level A - Basic accessibility -->
<img src="image.jpg" alt="Descriptive text">

<!-- WCAG Level AA - Enhanced accessibility -->
<button 
  aria-expanded="false"
  aria-controls="menu"
  style="color: #000; background: #fff;"
>
  Menu
</button>

<!-- WCAG Level AAA - Advanced accessibility -->
<button 
  aria-expanded="false"
  aria-controls="menu"
  style="color: #000; background: #fff; border: 2px solid #000;"
>
  Menu
</button>
```

**💬 Explanation + Insight**

- **Level A** - Basic accessibility requirements
- **Level AA** - Enhanced accessibility, most common target
- **Level AAA** - Advanced accessibility, highest level
- **Compliance** - Meet legal and accessibility standards
- **User Experience** - Improve experience for all users

---

### 115. 🧱 How do you ensure contrast and readability in design systems?

**🧠 Concept**

Contrast and readability ensure text is legible against backgrounds, meeting accessibility standards and improving user experience.

**💻 Example**

```css
/* WCAG AA contrast ratios */
.text-primary {
  color: #000000; /* Black text */
  background: #ffffff; /* White background */
  /* Contrast ratio: 21:1 (AAA) */
}

.text-secondary {
  color: #333333; /* Dark gray text */
  background: #ffffff; /* White background */
  /* Contrast ratio: 12.6:1 (AAA) */
}

.text-muted {
  color: #666666; /* Medium gray text */
  background: #ffffff; /* White background */
  /* Contrast ratio: 4.5:1 (AA) */
}
```

**💬 Explanation + Insight**

- **Contrast Ratios** - Meet WCAG contrast requirements
- **Readability** - Ensure text is legible
- **Accessibility** - Support users with visual impairments
- **Design Consistency** - Maintain consistent contrast
- **User Experience** - Improve readability for all users

---

### 116. 🧱 What are design tokens, and how do they unify design and code?

**🧠 Concept**

Design tokens are named values that store design decisions, creating consistency between design and development.

**💻 Example**

```javascript
// Design tokens
const tokens = {
  colors: {
    primary: '#007bff',
    secondary: '#6c757d',
    success: '#28a745',
    danger: '#dc3545'
  },
  spacing: {
    xs: '4px',
    sm: '8px',
    md: '16px',
    lg: '24px',
    xl: '32px'
  },
  typography: {
    fontFamily: 'Inter, sans-serif',
    fontSize: {
      sm: '14px',
      md: '16px',
      lg: '18px'
    }
  }
};

// Usage in components
const Button = styled.button`
  background-color: ${tokens.colors.primary};
  padding: ${tokens.spacing.sm} ${tokens.spacing.md};
  font-family: ${tokens.typography.fontFamily};
`;
```

**💬 Explanation + Insight**

- **Consistency** - Ensure consistent design across applications
- **Maintainability** - Centralize design decisions
- **Scalability** - Scale design systems across teams
- **Automation** - Generate code from design tokens
- **Collaboration** - Bridge design and development

---

### 117. 🧱 How do you manage color, spacing, and typography tokens in CSS?

**🧠 Concept**

CSS custom properties (variables) enable design token management, providing centralized control over design values.

**💻 Example**

```css
/* Design tokens as CSS custom properties */
:root {
  /* Colors */
  --color-primary: #007bff;
  --color-secondary: #6c757d;
  --color-success: #28a745;
  
  /* Spacing */
  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 24px;
  
  /* Typography */
  --font-family: 'Inter', sans-serif;
  --font-size-sm: 14px;
  --font-size-md: 16px;
  --font-size-lg: 18px;
}

/* Usage in components */
.button {
  background-color: var(--color-primary);
  padding: var(--spacing-sm) var(--spacing-md);
  font-family: var(--font-family);
  font-size: var(--font-size-md);
}
```

**💬 Explanation + Insight**

- **CSS Variables** - Use custom properties for tokens
- **Centralized Control** - Manage design values in one place
- **Dynamic Updates** - Change values at runtime
- **Browser Support** - Wide browser support for CSS variables
- **Maintainability** - Easy to update and maintain

---

### 118. 🧱 How does theming work in design systems?

**🧠 Concept**

Theming allows design systems to support multiple visual themes while maintaining consistent structure and behavior.

**💻 Example**

```javascript
// Theme configuration
const themes = {
  light: {
    colors: {
      primary: '#007bff',
      background: '#ffffff',
      text: '#000000'
    }
  },
  dark: {
    colors: {
      primary: '#0d6efd',
      background: '#000000',
      text: '#ffffff'
    }
  }
};

// Theme provider
const ThemeProvider = ({ children, theme }) => {
  const themeTokens = themes[theme];
  return (
    <ThemeContext.Provider value={themeTokens}>
      {children}
    </ThemeContext.Provider>
  );
};
```

**💬 Explanation + Insight**

- **Multiple Themes** - Support different visual themes
- **Consistent Structure** - Maintain component structure
- **User Preference** - Allow users to choose themes
- **Brand Flexibility** - Support different brand themes
- **Accessibility** - Support high contrast and dark modes

---

### 119. 🧱 What is CSS-in-JS vs atomic CSS vs utility-first (Tailwind)?

**🧠 Concept**

Different CSS approaches: CSS-in-JS styles components in JavaScript, atomic CSS uses single-purpose classes, utility-first provides utility classes.

**💻 Example**

```javascript
// CSS-in-JS (Styled Components)
const Button = styled.button`
  background-color: ${props => props.primary ? '#007bff' : '#6c757d'};
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
`;

// Atomic CSS
<button class="bg-blue-500 px-4 py-2 rounded">Button</button>

// Utility-first (Tailwind)
<button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
  Button
</button>
```

**💬 Explanation + Insight**

- **CSS-in-JS** - Component-scoped styles, dynamic styling
- **Atomic CSS** - Single-purpose classes, utility-based
- **Utility-first** - Pre-built utility classes, rapid development
- **Performance** - Different performance characteristics
- **Use Cases** - Choose based on team preferences and needs

---

### 120. 🧱 What are the trade-offs of Tailwind vs Styled Components vs CSS Modules?

**🧠 Concept**

Each CSS approach has different trade-offs in terms of performance, maintainability, and developer experience.

**💻 Example**

```javascript
// Tailwind CSS
<button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
  Button
</button>

// Styled Components
const Button = styled.button`
  background-color: #007bff;
  color: white;
  padding: 8px 16px;
  border-radius: 4px;
  
  &:hover {
    background-color: #0056b3;
  }
`;

// CSS Modules
import styles from './Button.module.css';
<button className={styles.button}>Button</button>
```

**💬 Explanation + Insight**

- **Tailwind** - Fast development, utility-based, larger bundle
- **Styled Components** - Component-scoped, dynamic, runtime overhead
- **CSS Modules** - Scoped styles, build-time, no runtime overhead
- **Performance** - Different performance characteristics
- **Use Cases** - Choose based on project requirements

---

### 121. 🧱 How do you scale a design system across multiple projects?

**🧠 Concept**

Scaling design systems requires proper architecture, documentation, and processes to maintain consistency across projects.

**💻 Example**

```javascript
// Design system architecture
packages/
├── design-tokens/     # Design tokens
├── components/        # UI components
├── icons/            # Icon library
├── styles/           # Global styles
└── documentation/    # Storybook docs

// Component distribution
import { Button, Input, Card } from '@company/design-system';

// Token usage
import { tokens } from '@company/design-tokens';
const primaryColor = tokens.colors.primary;
```

**💬 Explanation + Insight**

- **Modular Architecture** - Organize into packages
- **Documentation** - Comprehensive documentation
- **Versioning** - Semantic versioning for components
- **Distribution** - Package and distribute components
- **Consistency** - Maintain consistency across projects

---

### 122. 🧱 What is Storybook, and how does it help component documentation?

**🧠 Concept**

Storybook provides an isolated development environment for UI components, enabling documentation, testing, and design system management.

**💻 Example**

```javascript
// Storybook story
import { Button } from './Button';

export default {
  title: 'Components/Button',
  component: Button,
  argTypes: {
    variant: {
      control: { type: 'select' },
      options: ['primary', 'secondary', 'danger']
    }
  }
};

export const Primary = {
  args: {
    variant: 'primary',
    children: 'Button'
  }
};

export const Secondary = {
  args: {
    variant: 'secondary',
    children: 'Button'
  }
};
```

**💬 Explanation + Insight**

- **Component Documentation** - Document component usage
- **Isolated Development** - Develop components in isolation
- **Testing** - Test component variations
- **Design System** - Manage design system components
- **Collaboration** - Share components with team

---

### 123. 🧱 What is component-driven development (CDD)?

**🧠 Concept**

Component-driven development builds applications from the bottom up, starting with atomic components and composing them into larger features.

**💻 Example**

```javascript
// Atomic components
const Button = ({ children, variant, size }) => (
  <button className={`btn btn-${variant} btn-${size}`}>
    {children}
  </button>
);

const Input = ({ label, type, placeholder }) => (
  <div className="input-group">
    <label>{label}</label>
    <input type={type} placeholder={placeholder} />
  </div>
);

// Composed components
const LoginForm = () => (
  <form>
    <Input label="Email" type="email" placeholder="Enter email" />
    <Input label="Password" type="password" placeholder="Enter password" />
    <Button variant="primary" size="lg">Login</Button>
  </form>
);
```

**💬 Explanation + Insight**

- **Bottom-up Development** - Build from small to large
- **Reusability** - Create reusable components
- **Composition** - Compose components into features
- **Maintainability** - Easier to maintain and test
- **Design System** - Natural fit for design systems

---

### 124. 🧱 What is the role of Figma tokens or style dictionaries in design systems?

**🧠 Concept**

Figma tokens and style dictionaries bridge design and development, ensuring design decisions are accurately implemented in code.

**💻 Example**

```javascript
// Style dictionary configuration
// tokens.json
{
  "color": {
    "primary": {
      "value": "#007bff",
      "type": "color"
    },
    "secondary": {
      "value": "#6c757d",
      "type": "color"
    }
  },
  "spacing": {
    "sm": {
      "value": "8px",
      "type": "spacing"
    },
    "md": {
      "value": "16px",
      "type": "spacing"
    }
  }
}

// Generated CSS
:root {
  --color-primary: #007bff;
  --color-secondary: #6c757d;
  --spacing-sm: 8px;
  --spacing-md: 16px;
}
```

**💬 Explanation + Insight**

- **Design-Development Bridge** - Connect design and code
- **Automation** - Generate code from design tokens
- **Consistency** - Ensure design-code consistency
- **Maintainability** - Centralize design decisions
- **Collaboration** - Improve design-development workflow

---

### 125. 🧱 How do you enforce consistency and linting in UI components?

**🧠 Concept**

Consistency enforcement uses linting rules, automated testing, and design system guidelines to maintain component quality.

**💻 Example**

```javascript
// ESLint rules for components
module.exports = {
  rules: {
    'react/prop-types': 'error',
    'react/display-name': 'error',
    'react/no-unused-prop-types': 'error'
  }
};

// Component testing
import { render, screen } from '@testing-library/react';
import { Button } from './Button';

test('renders button with correct text', () => {
  render(<Button>Click me</Button>);
  expect(screen.getByText('Click me')).toBeInTheDocument();
});

// Design system guidelines
const componentGuidelines = {
  button: {
    variants: ['primary', 'secondary', 'danger'],
    sizes: ['sm', 'md', 'lg'],
    requiredProps: ['children']
  }
};
```

**💬 Explanation + Insight**

- **Linting Rules** - Enforce coding standards
- **Automated Testing** - Test component behavior
- **Design Guidelines** - Establish component standards
- **Quality Assurance** - Maintain component quality
- **Consistency** - Ensure consistent component usage

---

### 126. 🧱 How do you version and publish UI components as npm packages?

**🧠 Concept**

Component versioning and publishing enables distribution of design system components across projects and teams.

**💻 Example**

```javascript
// Package.json for component library
{
  "name": "@company/design-system",
  "version": "1.2.3",
  "main": "dist/index.js",
  "module": "dist/index.esm.js",
  "types": "dist/index.d.ts",
  "files": ["dist"],
  "peerDependencies": {
    "react": ">=16.8.0",
    "react-dom": ">=16.8.0"
  }
}

// Publishing workflow
npm version patch  # 1.2.3 -> 1.2.4
npm publish

// Usage in projects
import { Button, Input, Card } from '@company/design-system';
```

**💬 Explanation + Insight**

- **Semantic Versioning** - Use semantic versioning
- **Package Distribution** - Publish to npm registry
- **Dependency Management** - Manage peer dependencies
- **Version Control** - Track component versions
- **Team Collaboration** - Share components across teams

---

### 127. 🧱 What is code splitting for design system imports?

**🧠 Concept**

Code splitting for design systems allows importing only needed components, reducing bundle size and improving performance.

**💻 Example**

```javascript
// Tree-shakable exports
// index.js
export { Button } from './Button';
export { Input } from './Input';
export { Card } from './Card';

// Individual component imports
import { Button } from '@company/design-system/Button';
import { Input } from '@company/design-system/Input';

// Dynamic imports
const Button = lazy(() => import('@company/design-system/Button'));
const Input = lazy(() => import('@company/design-system/Input'));
```

**💬 Explanation + Insight**

- **Bundle Optimization** - Reduce bundle size
- **Tree Shaking** - Remove unused code
- **Performance** - Improve loading performance
- **Selective Imports** - Import only needed components
- **Use Cases** - Large design systems, performance optimization

---

### 128. 🧱 How do you handle brand theming for white-label apps?

**🧠 Concept**

White-label theming allows customization of design systems for different brands while maintaining consistent structure.

**💻 Example**

```javascript
// Brand theme configuration
const brandThemes = {
  brandA: {
    colors: {
      primary: '#007bff',
      secondary: '#6c757d'
    },
    fonts: {
      primary: 'Inter, sans-serif'
    }
  },
  brandB: {
    colors: {
      primary: '#dc3545',
      secondary: '#6c757d'
    },
    fonts: {
      primary: 'Roboto, sans-serif'
    }
  }
};

// Theme provider
const BrandThemeProvider = ({ brand, children }) => {
  const theme = brandThemes[brand];
  return (
    <ThemeContext.Provider value={theme}>
      {children}
    </ThemeContext.Provider>
  );
};
```

**💬 Explanation + Insight**

- **Brand Customization** - Customize for different brands
- **Theme Flexibility** - Support multiple brand themes
- **Consistent Structure** - Maintain component structure
- **White-label Support** - Enable white-label applications
- **Scalability** - Scale across multiple brands

---

### 129. 🧱 What is cross-brand tokenization in enterprise design systems?

**🧠 Concept**

Cross-brand tokenization enables sharing of design tokens across multiple brands while maintaining brand-specific customization.

**💻 Example**

```javascript
// Cross-brand token system
const baseTokens = {
  spacing: {
    xs: '4px',
    sm: '8px',
    md: '16px'
  },
  typography: {
    fontFamily: 'Inter, sans-serif',
    fontSize: {
      sm: '14px',
      md: '16px'
    }
  }
};

const brandTokens = {
  brandA: {
    ...baseTokens,
    colors: { primary: '#007bff' }
  },
  brandB: {
    ...baseTokens,
    colors: { primary: '#dc3545' }
  }
};
```

**💬 Explanation + Insight**

- **Token Sharing** - Share common tokens across brands
- **Brand Customization** - Customize brand-specific tokens
- **Consistency** - Maintain consistent spacing and typography
- **Scalability** - Scale across multiple brands
- **Maintainability** - Centralize token management

---

### 130. 🧱 How do you handle a11y testing (axe-core, jest-axe)?

**🧠 Concept**

Accessibility testing ensures components meet accessibility standards through automated testing tools and manual testing.

**💻 Example**

```javascript
// Jest-axe testing
import { axe, toHaveNoViolations } from 'jest-axe';
import { render } from '@testing-library/react';
import { Button } from './Button';

expect.extend(toHaveNoViolations);

test('button should not have accessibility violations', async () => {
  const { container } = render(<Button>Click me</Button>);
  const results = await axe(container);
  expect(results).toHaveNoViolations();
});

// Axe-core integration
import { axe } from 'axe-core';

const results = await axe.run(document);
console.log(results.violations);
```

**💬 Explanation + Insight**

- **Automated Testing** - Test accessibility automatically
- **Standards Compliance** - Ensure WCAG compliance
- **Continuous Testing** - Test accessibility in CI/CD
- **Quality Assurance** - Maintain accessibility quality
- **Use Cases** - Design systems, accessibility compliance

---

### 131. 🧱 What is XSS, and how can it affect React/Next.js apps?

**🧠 Concept**

XSS (Cross-Site Scripting) attacks inject malicious scripts into web applications, potentially stealing data or performing unauthorized actions.

**💻 Example**

```javascript
// Vulnerable XSS
function UserProfile({ userInput }) {
  return <div dangerouslySetInnerHTML={{ __html: userInput }} />;
}

// Secure XSS prevention
function UserProfile({ userInput }) {
  const sanitizedInput = DOMPurify.sanitize(userInput);
  return <div dangerouslySetInnerHTML={{ __html: sanitizedInput }} />;
}

// React's built-in protection
function UserProfile({ userInput }) {
  return <div>{userInput}</div>; // React escapes by default
}
```

**💬 Explanation + Insight**

- **Script Injection** - Malicious scripts in user input
- **Data Theft** - Steal user data and cookies
- **Session Hijacking** - Hijack user sessions
- **Prevention** - Sanitize user input, use React's built-in protection
- **Security** - Critical for user data protection

---

### 132. 🧱 What is CSRF, and how do you prevent it on the frontend?

**🧠 Concept**

CSRF (Cross-Site Request Forgery) attacks trick users into performing unwanted actions on authenticated websites.

**💻 Example**

```javascript
// CSRF prevention with tokens
const csrfToken = document.querySelector('meta[name="csrf-token"]').content;

fetch('/api/data', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'X-CSRF-Token': csrfToken
  },
  body: JSON.stringify({ data: 'value' })
});

// SameSite cookie protection
document.cookie = "sessionId=abc123; SameSite=Strict; Secure; HttpOnly";
```

**💬 Explanation + Insight**

- **Request Forgery** - Unauthorized requests on behalf of users
- **Token Validation** - Use CSRF tokens for protection
- **SameSite Cookies** - Prevent cross-site cookie usage
- **Security Headers** - Use security headers for protection
- **Authentication** - Protect authenticated user actions

---

### 133. 🧱 How do you prevent DOM-based XSS vulnerabilities?

**🧠 Concept**

DOM-based XSS prevention involves sanitizing user input and avoiding dangerous DOM manipulation methods.

**💻 Example**

```javascript
// Vulnerable DOM manipulation
function updateContent(userInput) {
  document.getElementById('content').innerHTML = userInput;
}

// Secure DOM manipulation
function updateContent(userInput) {
  const sanitizedInput = DOMPurify.sanitize(userInput);
  document.getElementById('content').innerHTML = sanitizedInput;
}

// React's safe approach
function Content({ userInput }) {
  return <div>{userInput}</div>; // React escapes automatically
}
```

**💬 Explanation + Insight**

- **DOM Manipulation** - Avoid direct DOM manipulation
- **Input Sanitization** - Sanitize all user input
- **React Protection** - Use React's built-in protection
- **Safe Methods** - Use safe DOM methods
- **Security** - Prevent script injection attacks

---

### 134. 🧱 How do you securely store auth tokens in SPAs?

**🧠 Concept**

Secure token storage in SPAs involves using secure storage methods and implementing proper token management.

**💻 Example**

```javascript
// Secure token storage
class TokenManager {
  setToken(token) {
    // Use httpOnly cookies (server-side)
    document.cookie = `token=${token}; HttpOnly; Secure; SameSite=Strict`;
    
    // Or use secure storage for client-side
    if (window.crypto && window.crypto.subtle) {
      // Encrypt token before storage
      const encryptedToken = encrypt(token);
      localStorage.setItem('encryptedToken', encryptedToken);
    }
  }
  
  getToken() {
    // Retrieve from secure storage
    const encryptedToken = localStorage.getItem('encryptedToken');
    return encryptedToken ? decrypt(encryptedToken) : null;
  }
}
```

**💬 Explanation + Insight**

- **HttpOnly Cookies** - Most secure for token storage
- **Encryption** - Encrypt tokens before storage
- **Secure Storage** - Use secure storage methods
- **Token Rotation** - Regularly rotate tokens
- **Security** - Protect against token theft

---

### 135. 🧱 What are best practices for Content Security Policy (CSP)?

**🧠 Concept**

CSP (Content Security Policy) prevents XSS attacks by controlling which resources can be loaded and executed.

**💻 Example**

```html
<!-- CSP header -->
<meta http-equiv="Content-Security-Policy" 
      content="default-src 'self'; 
               script-src 'self' 'unsafe-inline' https://trusted-cdn.com; 
               style-src 'self' 'unsafe-inline'; 
               img-src 'self' data: https:; 
               connect-src 'self' https://api.example.com;">

<!-- Strict CSP -->
<meta http-equiv="Content-Security-Policy" 
      content="default-src 'none'; 
               script-src 'self'; 
               style-src 'self'; 
               img-src 'self' data:; 
               connect-src 'self';">
```

**💬 Explanation + Insight**

- **Resource Control** - Control which resources can load
- **XSS Prevention** - Prevent script injection attacks
- **Policy Enforcement** - Enforce security policies
- **Gradual Implementation** - Implement CSP gradually
- **Security** - Essential for web application security

---

*This comprehensive UX, security, and design systems section covers all essential concepts including accessibility, design tokens, theming, component development, security best practices, and design system management for building inclusive and secure frontend applications.*