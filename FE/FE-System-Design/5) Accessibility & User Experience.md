# 5) Accessibility & User Experience (Q44–53)

## 53) What are the WCAG 2.2 accessibility principles?

Concept: WCAG 2.2 (Web Content Accessibility Guidelines) provides four main principles: Perceivable, Operable, Understandable, and Robust (POUR), with specific success criteria for each level.

Example:
```javascript
// Perceivable - Text alternatives and captions
const ImageWithAlt = ({ src, alt, caption }) => (
  <figure>
    <img 
      src={src} 
      alt={alt}
      loading="lazy"
    />
    <figcaption>{caption}</figcaption>
  </figure>
);

// Operable - Keyboard navigation
const KeyboardNavigableButton = ({ onClick, children, ...props }) => (
  <button
    onClick={onClick}
    onKeyDown={(e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        onClick();
      }
    }}
    tabIndex={0}
    {...props}
  >
    {children}
  </button>
);

// Understandable - Clear language and instructions
const FormWithInstructions = () => (
  <form>
    <label htmlFor="password">
      Password
      <span className="sr-only">Must be at least 8 characters long</span>
    </label>
    <input
      id="password"
      type="password"
      aria-describedby="password-help"
      required
    />
    <div id="password-help" className="help-text">
      Password must be at least 8 characters long and contain at least one number.
    </div>
  </form>
);
```

Deep Insight:
- Perceivable: Information must be presentable in ways users can perceive
- Operable: Interface components must be operable by all users
- Understandable: Information and UI operation must be understandable
- Robust: Content must be robust enough for various assistive technologies
- Follow success criteria for AA compliance level

## 51) How do you make a UI accessible to screen readers (ARIA, semantic HTML)?

Concept: Screen reader accessibility requires semantic HTML elements, proper ARIA attributes, and logical content structure to provide meaningful information to assistive technologies.

Example:
```javascript
// Semantic HTML structure
const AccessibleNavigation = () => (
  <nav aria-label="Main navigation">
    <ul role="menubar">
      <li role="none">
        <a href="/home" role="menuitem" aria-current="page">
          Home
        </a>
      </li>
      <li role="none">
        <a href="/about" role="menuitem">
          About
        </a>
      </li>
    </ul>
  </nav>
);

// ARIA attributes for dynamic content
const AccessibleModal = ({ isOpen, onClose, title, children }) => (
  <div
    className={`modal ${isOpen ? 'open' : ''}`}
    role="dialog"
    aria-modal="true"
    aria-labelledby="modal-title"
    aria-hidden={!isOpen}
  >
    <div className="modal-content">
      <h2 id="modal-title">{title}</h2>
      <button
        onClick={onClose}
        aria-label="Close modal"
        className="close-button"
      >
        ×
      </button>
      {children}
    </div>
  </div>
);

// Form with proper labeling
const AccessibleForm = () => (
  <form>
    <fieldset>
      <legend>Contact Information</legend>
      <div className="form-group">
        <label htmlFor="email">Email Address</label>
        <input
          id="email"
          type="email"
          aria-describedby="email-error"
          aria-invalid={hasError}
          required
        />
        <div id="email-error" role="alert" className="error-message">
          {emailError}
        </div>
      </div>
    </fieldset>
  </form>
);
```

Deep Insight:
- Use semantic HTML elements (nav, main, article, section)
- Implement proper ARIA attributes and roles
- Ensure logical tab order and focus management
- Provide text alternatives for images and icons
- Test with actual screen readers

## 52) How do you ensure keyboard-only navigation in complex UIs?

Concept: Keyboard navigation requires proper tab order, focus management, keyboard shortcuts, and skip links to enable users to navigate complex interfaces without a mouse.

Example:
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
    if (e.key === 'Escape') {
      onClose();
    }
    if (e.key === 'Tab') {
      // Trap focus within modal
      const focusableElements = modalRef.current?.querySelectorAll(
        'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
      );
      const firstElement = focusableElements[0];
      const lastElement = focusableElements[focusableElements.length - 1];
      
      if (e.shiftKey && document.activeElement === firstElement) {
        e.preventDefault();
        lastElement?.focus();
      } else if (!e.shiftKey && document.activeElement === lastElement) {
        e.preventDefault();
        firstElement?.focus();
      }
    }
  };
  
  return (
    <div
      ref={modalRef}
      className="modal"
      tabIndex={-1}
      onKeyDown={handleKeyDown}
      role="dialog"
      aria-modal="true"
    >
      {children}
    </div>
  );
};

// Keyboard shortcuts
const KeyboardShortcuts = () => {
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.ctrlKey || e.metaKey) {
        switch (e.key) {
          case 'k':
            e.preventDefault();
            openSearch();
            break;
          case 's':
            e.preventDefault();
            saveDocument();
            break;
        }
      }
    };
    
    document.addEventListener('keydown', handleKeyDown);
    return () => document.removeEventListener('keydown', handleKeyDown);
  }, []);
  
  return null;
};
```

Deep Insight:
- Implement skip links for main content areas
- Manage focus properly in modals and dropdowns
- Provide keyboard shortcuts for common actions
- Ensure logical tab order throughout the interface
- Test navigation with keyboard only

## 53) How do you test accessibility in front-end applications (axe, Lighthouse, NVDA)?

Concept: Accessibility testing involves automated tools, manual testing, and assistive technology testing to ensure compliance with accessibility standards.

Example:
```javascript
// Automated testing with axe-core
import { axe, toHaveNoViolations } from 'jest-axe';

expect.extend(toHaveNoViolations);

test('should not have accessibility violations', async () => {
  const { container } = render(<MyComponent />);
  const results = await axe(container);
  expect(results).toHaveNoViolations();
});

// Lighthouse accessibility audit
const lighthouseConfig = {
  extends: 'lighthouse:default',
  settings: {
    onlyAudits: [
      'accessibility',
      'best-practices'
    ]
  }
};

// Manual testing checklist
const accessibilityChecklist = {
  keyboard: [
    'All interactive elements are keyboard accessible',
    'Tab order is logical and intuitive',
    'Focus indicators are visible',
    'No keyboard traps'
  ],
  screenReader: [
    'All images have alt text',
    'Form labels are properly associated',
    'ARIA attributes are used correctly',
    'Content is announced in logical order'
  ],
  visual: [
    'Color contrast meets WCAG standards',
    'Text is readable at 200% zoom',
    'No content is lost when styles are disabled',
    'Focus indicators are visible'
  ]
};
```

Deep Insight:
- Use automated tools for initial accessibility checks
- Perform manual testing with keyboard navigation
- Test with actual screen readers and assistive technologies
- Include accessibility in code review process
- Regular accessibility audits and user testing

## 51) How do you handle color contrast, animations, and motion sensitivity?

Concept: Accessibility considerations include sufficient color contrast, reduced motion options, and alternative ways to convey information beyond visual cues.

Example:
```javascript
// Color contrast validation
const ColorContrastChecker = ({ textColor, backgroundColor }) => {
  const contrastRatio = calculateContrastRatio(textColor, backgroundColor);
  const isAccessible = contrastRatio >= 4.5; // AA standard
  
  return (
    <div style={{ color: textColor, backgroundColor }}>
      <span style={{ color: isAccessible ? 'green' : 'red' }}>
        Contrast Ratio: {contrastRatio.toFixed(2)}
      </span>
    </div>
  );
};

// Reduced motion support
const MotionSensitiveComponent = () => {
  const [prefersReducedMotion, setPrefersReducedMotion] = useState(false);
  
  useEffect(() => {
    const mediaQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
    setPrefersReducedMotion(mediaQuery.matches);
    
    const handleChange = (e) => setPrefersReducedMotion(e.matches);
    mediaQuery.addEventListener('change', handleChange);
    return () => mediaQuery.removeEventListener('change', handleChange);
  }, []);
  
  return (
    <div
      className={`animated-element ${prefersReducedMotion ? 'no-animation' : ''}`}
    >
      Content with conditional animation
    </div>
  );
};

// CSS for reduced motion
const reducedMotionStyles = `
  @media (prefers-reduced-motion: reduce) {
    * {
      animation-duration: 0.01ms !important;
      animation-iteration-count: 1 !important;
      transition-duration: 0.01ms !important;
    }
  }
  
  .animated-element {
    transition: transform 0.3s ease;
  }
  
  .animated-element.no-animation {
    transition: none;
  }
`;
```

Deep Insight:
- Ensure color contrast meets WCAG AA standards (4.5:1)
- Provide reduced motion options for sensitive users
- Use multiple ways to convey information (color + text)
- Test with color blindness simulators
- Consider high contrast mode support

## 52) How do you ensure accessibility in SPAs where content dynamically updates?

Concept: Dynamic content updates in SPAs require proper ARIA live regions, focus management, and announcements to keep assistive technology users informed of changes.

Example:
```javascript
// ARIA live region for dynamic updates
const LiveRegion = ({ message, priority = 'polite' }) => (
  <div
    aria-live={priority}
    aria-atomic="true"
    className="sr-only"
  >
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
  
  const removeItem = (itemId) => {
    setItems(prev => prev.filter(item => item.id !== itemId));
    setAnnouncement('Item removed from the list');
  };
  
  return (
    <div>
      <LiveRegion message={announcement} />
      <button onClick={() => addItem({ id: Date.now(), name: 'New Item' })}>
        Add Item
      </button>
      <ul>
        {items.map(item => (
          <li key={item.id}>
            {item.name}
            <button onClick={() => removeItem(item.id)}>
              Remove
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

// Focus management for dynamic content
const FocusManager = () => {
  const [focusedItem, setFocusedItem] = useState(null);
  const itemRefs = useRef({});
  
  const focusItem = (itemId) => {
    const element = itemRefs.current[itemId];
    if (element) {
      element.focus();
      setFocusedItem(itemId);
    }
  };
  
  return (
    <div>
      {items.map(item => (
        <div
          key={item.id}
          ref={el => itemRefs.current[item.id] = el}
          tabIndex={0}
          onFocus={() => setFocusedItem(item.id)}
        >
          {item.content}
        </div>
      ))}
    </div>
  );
};
```

Deep Insight:
- Use ARIA live regions for important updates
- Manage focus when content changes
- Provide clear announcements for state changes
- Ensure keyboard navigation works with dynamic content
- Test with screen readers during development

## 53) What's the difference between usability, accessibility, and inclusivity?

Concept: Usability focuses on ease of use, accessibility ensures access for people with disabilities, and inclusivity considers diverse user needs and experiences.

Example:
```javascript
// Usability - Easy to use interface
const UsableForm = () => (
  <form>
    <div className="form-group">
      <label htmlFor="email">Email</label>
      <input
        id="email"
        type="email"
        placeholder="Enter your email"
        required
      />
      <button type="submit">Submit</button>
    </div>
  </form>
);

// Accessibility - Accessible to all users
const AccessibleForm = () => (
  <form>
    <div className="form-group">
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
      <button type="submit" aria-describedby="submit-help">
        Submit
      </button>
      <div id="submit-help" className="sr-only">
        Click to submit your email address
      </div>
    </div>
  </form>
);

// Inclusivity - Considers diverse needs
const InclusiveForm = () => {
  const [language, setLanguage] = useState('en');
  const [preferredName, setPreferredName] = useState('');
  
  return (
    <form>
      <div className="form-group">
        <label htmlFor="name">Preferred Name</label>
        <input
          id="name"
          type="text"
          value={preferredName}
          onChange={(e) => setPreferredName(e.target.value)}
          placeholder={language === 'es' ? 'Ingrese su nombre' : 'Enter your name'}
        />
      </div>
      <div className="form-group">
        <label htmlFor="pronouns">Pronouns (Optional)</label>
        <select id="pronouns">
          <option value="">Select pronouns</option>
          <option value="he/him">He/Him</option>
          <option value="she/her">She/Her</option>
          <option value="they/them">They/Them</option>
          <option value="other">Other</option>
        </select>
      </div>
    </form>
  );
};
```

Deep Insight:
- Usability: Focus on efficiency and user satisfaction
- Accessibility: Ensure access for people with disabilities
- Inclusivity: Consider diverse backgrounds and needs
- All three work together for better user experience
- Regular user testing with diverse groups

## 51) How do you design components with focus management in mind?

Concept: Focus management ensures keyboard users can navigate and interact with components effectively, requiring proper focus trapping, restoration, and visual indicators.

Example:
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
        if (e.shiftKey) {
          if (document.activeElement === firstElement) {
            e.preventDefault();
            lastElement?.focus();
          }
        } else {
          if (document.activeElement === lastElement) {
            e.preventDefault();
            firstElement?.focus();
          }
        }
      }
    };
    
    document.addEventListener('keydown', handleTabKey);
    firstElement?.focus();
    
    return () => document.removeEventListener('keydown', handleTabKey);
  }, [isActive]);
  
  return containerRef;
};

// Focus management component
const FocusManagedModal = ({ isOpen, onClose, children }) => {
  const containerRef = useFocusTrap(isOpen);
  const previousFocusRef = useRef();
  
  useEffect(() => {
    if (isOpen) {
      previousFocusRef.current = document.activeElement;
    } else {
      previousFocusRef.current?.focus();
    }
  }, [isOpen]);
  
  return (
    <div
      ref={containerRef}
      className="modal"
      role="dialog"
      aria-modal="true"
      tabIndex={-1}
    >
      {children}
    </div>
  );
};
```

Deep Insight:
- Implement focus trapping for modals and dropdowns
- Restore focus when components unmount
- Provide clear focus indicators
- Ensure logical tab order
- Test with keyboard navigation

## 52) What's your approach to internationalization (i18n) and localization (l10n)?

Concept: Internationalization prepares applications for multiple languages and regions, while localization adapts content for specific locales, including text, dates, numbers, and cultural considerations.

Example:
```javascript
// i18n setup with react-i18next
import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

i18n.use(initReactI18next).init({
  resources: {
    en: {
      translation: {
        welcome: 'Welcome',
        goodbye: 'Goodbye',
        date: '{{date, date}}',
        currency: '{{amount, currency}}'
      }
    },
    es: {
      translation: {
        welcome: 'Bienvenido',
        goodbye: 'Adiós',
        date: '{{date, date}}',
        currency: '{{amount, currency}}'
      }
    }
  },
  lng: 'en',
  fallbackLng: 'en',
  interpolation: {
    escapeValue: false
  }
});

// Localized component
const LocalizedComponent = () => {
  const { t } = useTranslation();
  const [locale, setLocale] = useState('en');
  
  const formatDate = (date) => {
    return new Intl.DateTimeFormat(locale).format(date);
  };
  
  const formatCurrency = (amount) => {
    return new Intl.NumberFormat(locale, {
      style: 'currency',
      currency: locale === 'es' ? 'EUR' : 'USD'
    }).format(amount);
  };
  
  return (
    <div>
      <h1>{t('welcome')}</h1>
      <p>{formatDate(new Date())}</p>
      <p>{formatCurrency(100)}</p>
      <button onClick={() => setLocale(locale === 'en' ? 'es' : 'en')}>
        Switch Language
      </button>
    </div>
  );
};
```

Deep Insight:
- Plan for internationalization from the start
- Use proper i18n libraries and tools
- Consider right-to-left (RTL) languages
- Test with different locales and character sets
- Provide fallbacks for missing translations

## 53) How do you design error states, empty states, and loading UX effectively?

Concept: Effective error, empty, and loading states provide clear feedback, guidance, and maintain user engagement during different application states.

Example:
```javascript
// Error state component
const ErrorState = ({ error, onRetry, onDismiss }) => (
  <div className="error-state" role="alert">
    <h2>Something went wrong</h2>
    <p>{error.message}</p>
    <div className="error-actions">
      <button onClick={onRetry} className="primary">
        Try Again
      </button>
      <button onClick={onDismiss} className="secondary">
        Dismiss
      </button>
    </div>
  </div>
);

// Empty state component
const EmptyState = ({ title, description, action }) => (
  <div className="empty-state">
    <div className="empty-icon" aria-hidden="true">
      📭
    </div>
    <h2>{title}</h2>
    <p>{description}</p>
    {action && (
      <button onClick={action.onClick} className="primary">
        {action.label}
      </button>
    )}
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

// State management
const DataComponent = () => {
  const [state, setState] = useState('loading');
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  
  const fetchData = async () => {
    setState('loading');
    try {
      const result = await api.getData();
      setData(result);
      setState(result.length > 0 ? 'success' : 'empty');
    } catch (err) {
      setError(err);
      setState('error');
    }
  };
  
  useEffect(() => {
    fetchData();
  }, []);
  
  switch (state) {
    case 'loading':
      return <LoadingState />;
    case 'error':
      return <ErrorState error={error} onRetry={fetchData} />;
    case 'empty':
      return <EmptyState title="No data found" description="Try adjusting your filters" />;
    case 'success':
      return <DataList data={data} />;
    default:
      return null;
  }
};
```

Deep Insight:
- Provide clear, actionable error messages
- Use skeleton screens for better perceived performance
- Design empty states that encourage user action
- Consider accessibility in all states
- Test error scenarios and edge cases
