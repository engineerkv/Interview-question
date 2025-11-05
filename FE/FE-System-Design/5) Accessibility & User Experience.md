# 5) Accessibility & User Experience (Q44–53)

---

## 53) What are the WCAG 2.2 accessibility principles?

WCAG 2.2 (Web Content Accessibility Guidelines) provides four main principles: Perceivable, Operable, Understandable, and Robust (POUR), with specific success criteria for each level.

```javascript
// Perceivable - Text alternatives and captions
const ImageWithAlt = ({ src, alt, caption }) => (
  <figure>
    <img src={src} alt={alt} loading="lazy" />
    <figcaption>{caption}</figcaption>
  </figure>
);

// Operable - Keyboard navigation
const KeyboardNavigableButton = ({ onClick, children }) => (
  <button
    onClick={onClick}
    onKeyDown={(e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        onClick();
      }
    }}
    tabIndex={0}
  >
    {children}
  </button>
);
```

- **Core Principles**: Perceivable (information must be presentable in ways users can perceive), Operable (interface components must be operable by all users), Understandable (information and UI operation must be understandable), Robust (content must be robust enough for various assistive technologies)
- **Real-World Requirement**: Follow success criteria for AA compliance level
- **Common Practice**: Implement all four principles systematically
- **Advanced Feature**: Go beyond AA to AAA for better accessibility
- **Interview Tip**: Explain that WCAG compliance is required for many organizations

---

## 51) How do you make a UI accessible to screen readers (ARIA, semantic HTML)?

Screen reader accessibility requires semantic HTML elements, proper ARIA attributes, and logical content structure to provide meaningful information to assistive technologies.

```javascript
// Semantic HTML structure
const AccessibleNavigation = () => (
  <nav aria-label="Main navigation">
    <ul role="menubar">
      <li role="none">
        <a href="/home" role="menuitem" aria-current="page">Home</a>
      </li>
    </ul>
  </nav>
);

// ARIA attributes for dynamic content
const AccessibleModal = ({ isOpen, onClose, title, children }) => (
  <div
    role="dialog"
    aria-modal="true"
    aria-labelledby="modal-title"
    aria-hidden={!isOpen}
  >
    <h2 id="modal-title">{title}</h2>
    <button onClick={onClose} aria-label="Close modal">×</button>
    {children}
  </div>
);
```

- **Core Practice**: Use semantic HTML elements (nav, main, article, section)
- **Real-World Use**: Implement proper ARIA attributes and roles
- **Common Requirement**: Ensure logical tab order and focus management
- **Advanced Feature**: Provide text alternatives for images and icons
- **Interview Tip**: Explain that test with actual screen readers

---

## 52) How do you ensure keyboard-only navigation in complex UIs?

Keyboard navigation requires proper tab order, focus management, keyboard shortcuts, and skip links to enable users to navigate complex interfaces without a mouse.

```javascript
// Skip link for main content
const SkipLink = () => (
  <a href="#main-content" className="skip-link">
    Skip to main content
  </a>
);

// Focus management for modals
const FocusableModal = ({ isOpen, onClose, children }) => {
  const modalRef = useRef();
  const previousFocusRef = useRef();
  
  useEffect(() => {
    if (isOpen) {
      previousFocusRef.current = document.activeElement;
      modalRef.current?.focus();
    } else {
      previousFocusRef.current?.focus();
    }
  }, [isOpen]);
  
  const handleKeyDown = (e) => {
    if (e.key === 'Escape') onClose();
    // Trap focus within modal
  };
  
  return (
    <div ref={modalRef} className="modal" onKeyDown={handleKeyDown} role="dialog">
      {children}
    </div>
  );
};
```

- **Core Requirement**: Implement skip links for main content areas
- **Real-World Use**: Manage focus properly in modals and dropdowns
- **Common Practice**: Provide keyboard shortcuts for common actions
- **Advanced Feature**: Ensure logical tab order throughout the interface
- **Interview Tip**: Explain that test navigation with keyboard only

---

## 53) How do you test accessibility in front-end applications (axe, Lighthouse, NVDA)?

Accessibility testing involves automated tools, manual testing, and assistive technology testing to ensure compliance with accessibility standards.

```javascript
// Automated testing with axe-core
import { axe, toHaveNoViolations } from 'jest-axe';

expect.extend(toHaveNoViolations);

test('should not have accessibility violations', async () => {
  const { container } = render(<MyComponent />);
  const results = await axe(container);
  expect(results).toHaveNoViolations();
});
```

- **Core Tools**: Use automated tools for initial accessibility checks
- **Real-World Practice**: Perform manual testing with keyboard navigation
- **Common Requirement**: Test with actual screen readers and assistive technologies
- **Advanced Practice**: Include accessibility in code review process
- **Interview Tip**: Explain that regular accessibility audits and user testing

---

## 51) How do you handle color contrast, animations, and motion sensitivity?

Accessibility considerations include sufficient color contrast, reduced motion options, and alternative ways to convey information beyond visual cues.

```javascript
// Reduced motion support
const MotionSensitiveComponent = () => {
  const [prefersReducedMotion, setPrefersReducedMotion] = useState(false);
  
  useEffect(() => {
    const mediaQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
    setPrefersReducedMotion(mediaQuery.matches);
    mediaQuery.addEventListener('change', (e) => setPrefersReducedMotion(e.matches));
  }, []);
  
  return (
    <div className={`animated-element ${prefersReducedMotion ? 'no-animation' : ''}`}>
      Content with conditional animation
    </div>
  );
};
```

- **Core Requirement**: Ensure color contrast meets WCAG AA standards (4.5:1)
- **Real-World Use**: Provide reduced motion options for sensitive users
- **Common Practice**: Use multiple ways to convey information (color + text)
- **Advanced Feature**: Test with color blindness simulators
- **Interview Tip**: Explain that consider high contrast mode support

---

## 52) How do you ensure accessibility in SPAs where content dynamically updates?

Dynamic content updates in SPAs require proper ARIA live regions, focus management, and announcements to keep assistive technology users informed of changes.

```javascript
// ARIA live region for dynamic updates
const LiveRegion = ({ message, priority = 'polite' }) => (
  <div aria-live={priority} aria-atomic="true" className="sr-only">
    {message}
  </div>
);

// Dynamic content with announcements
const DynamicContent = () => {
  const [items, setItems] = useState([]);
  const [announcement, setAnnouncement] = useState('');
  
  const addItem = (newItem) => {
    setItems(prev => [...prev, newItem]);
    setAnnouncement(`Added ${newItem.name} to the list`);
  };
  
  return (
    <div>
      <LiveRegion message={announcement} />
      <button onClick={() => addItem({ id: Date.now(), name: 'New Item' })}>
        Add Item
      </button>
    </div>
  );
};
```

- **Core Technique**: Use ARIA live regions for important updates
- **Real-World Use**: Manage focus when content changes
- **Common Practice**: Provide clear announcements for state changes
- **Advanced Feature**: Ensure keyboard navigation works with dynamic content
- **Interview Tip**: Explain that test with screen readers during development

---

## 53) What's the difference between usability, accessibility, and inclusivity?

Usability focuses on ease of use, accessibility ensures access for people with disabilities, and inclusivity considers diverse user needs and experiences.

```javascript
// Usability - Easy to use interface
const UsableForm = () => (
  <form>
    <label htmlFor="email">Email</label>
    <input id="email" type="email" placeholder="Enter your email" required />
    <button type="submit">Submit</button>
  </form>
);

// Accessibility - Accessible to all users
const AccessibleForm = () => (
  <form>
    <label htmlFor="email">Email Address</label>
    <input
      id="email"
      type="email"
      aria-describedby="email-help"
      aria-required="true"
      required
    />
    <div id="email-help" className="help-text">
      We'll never share your email with anyone else.
    </div>
  </form>
);
```

- **Core Differences**: Usability (focus on efficiency and user satisfaction), Accessibility (ensure access for people with disabilities), Inclusivity (consider diverse backgrounds and needs)
- **Real-World Practice**: All three work together for better user experience
- **Common Approach**: Regular user testing with diverse groups
- **Advanced Strategy**: Design with all three in mind from the start
- **Interview Tip**: Explain that accessibility is a subset of inclusivity

---

## 51) How do you design components with focus management in mind?

Focus management ensures keyboard users can navigate and interact with components effectively, requiring proper focus trapping, restoration, and visual indicators.

```javascript
// Focus trap hook
const useFocusTrap = (isActive) => {
  const containerRef = useRef();
  
  useEffect(() => {
    if (!isActive || !containerRef.current) return;
    
    const focusableElements = containerRef.current.querySelectorAll(
      'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
    );
    const firstElement = focusableElements[0];
    const lastElement = focusableElements[focusableElements.length - 1];
    
    const handleTabKey = (e) => {
      if (e.key === 'Tab') {
        if (e.shiftKey && document.activeElement === firstElement) {
          e.preventDefault();
          lastElement?.focus();
        } else if (!e.shiftKey && document.activeElement === lastElement) {
          e.preventDefault();
          firstElement?.focus();
        }
      }
    };
    
    document.addEventListener('keydown', handleTabKey);
    firstElement?.focus();
    return () => document.removeEventListener('keydown', handleTabKey);
  }, [isActive]);
  
  return containerRef;
};
```

- **Core Practice**: Implement focus trapping for modals and dropdowns
- **Real-World Use**: Restore focus when components unmount
- **Common Requirement**: Provide clear focus indicators
- **Advanced Feature**: Ensure logical tab order
- **Interview Tip**: Explain that test with keyboard navigation

---

## 52) What's your approach to internationalization (i18n) and localization (l10n)?

Internationalization prepares applications for multiple languages and regions, while localization adapts content for specific locales, including text, dates, numbers, and cultural considerations.

```javascript
import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

i18n.use(initReactI18next).init({
  resources: {
    en: { translation: { welcome: 'Welcome', date: '{{date, date}}' } },
    es: { translation: { welcome: 'Bienvenido', date: '{{date, date}}' } }
  },
  lng: 'en',
  fallbackLng: 'en'
});

const LocalizedComponent = () => {
  const { t } = useTranslation();
  const formatDate = (date) => new Intl.DateTimeFormat('en').format(date);
  return <div><h1>{t('welcome')}</h1><p>{formatDate(new Date())}</p></div>;
};
```

- **Core Strategy**: Plan for internationalization from the start
- **Real-World Use**: Use proper i18n libraries and tools
- **Common Consideration**: Consider right-to-left (RTL) languages
- **Advanced Feature**: Test with different locales and character sets
- **Interview Tip**: Explain that provide fallbacks for missing translations

---

## 53) How do you design error states, empty states, and loading UX effectively?

Effective error, empty, and loading states provide clear feedback, guidance, and maintain user engagement during different application states.

```javascript
// Error state component
const ErrorState = ({ error, onRetry, onDismiss }) => (
  <div className="error-state" role="alert">
    <h2>Something went wrong</h2>
    <p>{error.message}</p>
    <button onClick={onRetry} className="primary">Try Again</button>
    <button onClick={onDismiss} className="secondary">Dismiss</button>
  </div>
);

// Empty state component
const EmptyState = ({ title, description, action }) => (
  <div className="empty-state">
    <h2>{title}</h2>
    <p>{description}</p>
    {action && <button onClick={action.onClick}>{action.label}</button>}
  </div>
);

// Loading state with skeleton
const LoadingState = () => (
  <div className="loading-state">
    <div className="skeleton skeleton-text" />
    <div className="skeleton skeleton-text" />
    <div className="skeleton skeleton-button" />
  </div>
);
```

- **Core Principle**: Provide clear, actionable error messages
- **Real-World Use**: Use skeleton screens for better perceived performance
- **Common Practice**: Design empty states that encourage user action
- **Advanced Feature**: Consider accessibility in all states
- **Interview Tip**: Explain that test error scenarios and edge cases

---
