# 🏗️ Microfrontend

---

## 📍 Navigation

<div align="center">

[← Previous: Patterns](23%29%20Patterns.md) • [Home: Questions Index](question.md)

[📋 Cheatsheet](FE-System-Design%20Interview%20Cheatsheet.md)

</div>

---

---

## Q104. Microfrontend Architecture

Microfrontend is an architectural approach where a frontend application is composed of smaller, independent applications that can be developed, deployed, and maintained separately. Each microfrontend is owned by a different team and can use different technologies, but these work together to form a cohesive user experience.

---

## 1. What is Microfrontend

### 🔹 Core Concept

Microfrontend extends the microservices architecture pattern to the frontend. Instead of one monolithic frontend application, you have multiple smaller frontend applications that work together.

**Key Principles:**

* **Independent deployment**: Each microfrontend can be deployed independently

* **Technology diversity**: Different microfrontends can use different frameworks

* **Team autonomy**: Each team owns their microfrontend end-to-end

* **Isolation**: Microfrontends are isolated from each other

* **Composition**: They compose together to form the full application

### 🔹 Why Microfrontend

**Problems with Monolithic Frontend:**

* Large codebase becomes hard to maintain

* Teams step on each other's code

* Slow deployments (deploy entire app for small changes)

* Technology lock-in (hard to upgrade or change frameworks)

* Scaling teams is difficult

**Benefits of Microfrontend:**

* **Independent development**: Teams work independently

* **Independent deployment**: Deploy changes without affecting others

* **Technology freedom**: Use best tool for each part

* **Scalability**: Easier to scale teams

* **Faster development**: Smaller codebases are easier to work with

📌 **In simple terms**: Microfrontend breaks a large frontend app into smaller, independent apps. Each team owns their part, can deploy independently, and use different technologies.

---

## 2. Microfrontend Architecture Patterns

### 🔹 Pattern 1: Build-Time Integration

**How it works:**

* Each microfrontend is a separate package/library

* Main app imports and composes them at build time

* Everything bundled together into one app

**Example:**

```javascript
// Main app imports microfrontends at build time
import ProductApp from 'product-microfrontend';
import CartApp from 'cart-microfrontend';

function App() {
  return <div><ProductApp /><CartApp /></div>;
}

```

**Pros:**

* Simple to implement

* Good performance (single bundle)

* Type safety possible

**Cons:**

* Not truly independent (need to rebuild main app)

* Technology lock-in (all must be compatible)

* Coupling at build time

**When to use:**

* Small number of microfrontends

* Same technology stack

* Want simplicity over independence

### 🔹 Pattern 2: Run-Time Integration (Client-Side)

**How it works:**

* Each microfrontend is deployed separately

* Main app loads microfrontends at runtime

* Uses JavaScript to dynamically load and compose

**Example with Module Federation (Webpack 5):**

```javascript
// Main app loads microfrontends at runtime
const ProductApp = React.lazy(() => import('productApp/ProductApp'));

function App() {
  return <Suspense fallback={<Loading />}><ProductApp /></Suspense>;
}

```

**Pros:**

* True independent deployment

* Technology diversity possible

* Runtime composition

**Cons:**

* More complex setup

* Potential performance overhead

* Need to handle loading states

**When to use:**

* Need independent deployment

* Different technologies

* Large, complex applications

### 🔹 Pattern 3: Server-Side Integration (SSI/ESI)

**How it works:**

* Each microfrontend is a separate application

* Server composes HTML from multiple sources

* Returns composed HTML to browser

**Example with Server-Side Includes (SSI):**

```html
<!-- Main app composes HTML from multiple sources -->
<body>
  <!--# include virtual="/user-app/header.html" -->
  <!--# include virtual="/product-app/content.html" -->
</body>

```

**Pros:**

* Simple for users (single HTML)

* Good SEO

* Server handles composition

**Cons:**

* Server dependency

* Slower (multiple server requests)

* Less flexible

**When to use:**

* Need good SEO

* Simple composition needs

* Server-side rendering required

### 🔹 Pattern 4: iframe Integration

**How it works:**

* Each microfrontend runs in its own iframe

* Complete isolation between microfrontends

* Communication via postMessage

**Example:**

```html
<!-- Main app uses iframes for isolation -->
<div id="app">
  <iframe src="https://product-app.example.com"></iframe>
</div>
<script>
  window.addEventListener('message', (event) => {
    if (event.origin === 'https://product-app.example.com') {
      // Handle message from product app
    }
  });
</script>

```

**Pros:**

* Complete isolation

* Simple to implement

* No technology constraints

**Cons:**

* Performance overhead

* Styling challenges

* Communication complexity

* SEO issues

**When to use:**

* Need complete isolation

* Legacy applications

* Different domains

📌 **In simple terms**: Build-time bundles everything together. Runtime loads at runtime (Module Federation). Server-side composes on server. iframe provides complete isolation.

---

## 3. Implementation Approaches

### 🔹 Approach 1: Module Federation (Webpack 5)

Module Federation allows a JavaScript application to dynamically load code from another application at runtime.

**Setup:**

**Host App (Main App):**

```javascript
// webpack.config.js - configure remotes
new ModuleFederationPlugin({
  name: 'host',
  remotes: { productApp: 'productApp@http://localhost:3001/remoteEntry.js' },
  shared: { react: { singleton: true } },
});

// App.js - load remote at runtime
const ProductApp = React.lazy(() => import('productApp/ProductApp'));

```

**Remote App (Product Microfrontend):**

```javascript
// webpack.config.js - expose component
new ModuleFederationPlugin({
  name: 'productApp',
  exposes: { './ProductApp': './src/ProductApp' },
  shared: { react: { singleton: true } },
});

```

**Key Features:**

* Runtime integration

* Shared dependencies

* Independent deployment

* TypeScript support

### 🔹 Approach 2: Single-SPA

Single-SPA is a framework for building microfrontends that can work together.

**Setup:**

**Root Config:**

```javascript
// root-config.js - register microfrontends
registerApplication({
  name: 'product',
  app: () => System.import('product'),
  activeWhen: ['/products'],
});
start();

```

**Product App:**

```javascript
// product.app.js - export lifecycles
const lifecycles = singleSpaReact({
  React, ReactDOM, rootComponent: ProductApp
});
export const { bootstrap, mount, unmount } = lifecycles;

```

**Key Features:**

* Framework agnostic

* Routing integration

* Lifecycle management

* Multiple frameworks supported

### 🔹 Approach 3: Nx Monorepo

Nx is a monorepo tool that can be used for microfrontends with build-time or runtime integration.

**Setup:**

```bash

# Create Nx workspace

npx create-nx-workspace@latest myorg

# Generate applications

nx generate @nrwl/react:application product-app
nx generate @nrwl/react:application cart-app
nx generate @nrwl/react:application host-app

```

**Module Federation with Nx:**

```javascript
// apps/host-app/webpack.config.js
module.exports = withModuleFederation({
  name: 'host',
  remotes: {
    productApp: 'productApp@http://localhost:4201/remoteEntry.js',
  },
});

```

**Key Features:**

* Monorepo support

* Code sharing

* Build optimization

* Testing tools

📌 **In simple terms**: Module Federation uses Webpack 5 for runtime integration. Single-SPA is framework-agnostic. Nx provides monorepo tooling for microfrontends.

---

## 4. Communication Between Microfrontends

### 🔹 Communication Patterns

**1. Props/Events (Parent-Child):**

```javascript
// Host app passes props
<ProductApp userId={user.id} onProductSelect={handleSelect} />

// Product app emits events
function ProductApp({ onProductSelect }) {
  return <button onClick={() => onProductSelect(product)}>Select</button>;
}

```

**2. Custom Events (Sibling Communication):**

```javascript
// Product app emits event
window.dispatchEvent(new CustomEvent('product-selected', {
  detail: { productId: 123 }
}));

// Cart app listens
window.addEventListener('product-selected', (event) => {
  const { productId } = event.detail;
  addToCart(productId);
});

```

**3. Shared State (Global State):**

```javascript
// Shared state store
class SharedState {
  setState(key, value) { this.state[key] = value; this.notify(key, value); }
  subscribe(listener) { this.listeners.push(listener); }
}
export const sharedState = new SharedState();

// Product app sets state
sharedState.setState('selectedProduct', product);

// Cart app subscribes
sharedState.subscribe((key, value) => {
  if (key === 'selectedProduct') addToCart(value);
});

```

**4. URL/Query Parameters:**

```javascript
// Product app updates URL
history.pushState({}, '', `/products?selected=${productId}`);

// Cart app reads URL
const params = new URLSearchParams(window.location.search);
const selectedProduct = params.get('selected');

```

**5. Message Bus/Event Bus:**

```javascript
// message-bus.js
class MessageBus {
  publish(topic, data) {
    this.subscribers[topic]?.forEach(callback => callback(data));
  }
  subscribe(topic, callback) {
    if (!this.subscribers[topic]) this.subscribers[topic] = [];
    this.subscribers[topic].push(callback);
  }
}

// Product app publishes
messageBus.publish('product-selected', { productId: 123 });

// Cart app subscribes
messageBus.subscribe('product-selected', (data) => addToCart(data.productId));

```

📌 **In simple terms**: Microfrontends communicate via props (parent-child), custom events (siblings), shared state (global), URL parameters, or message bus. Choose based on coupling needs.

---

## 5. Routing in Microfrontends

### 🔹 Routing Strategies

**1. Client-Side Routing (Each App Has Own Router):**

```javascript
// Host app routes to microfrontends
<BrowserRouter>
  <Routes>
    <Route path="/products/*" element={<ProductApp />} />
    <Route path="/cart/*" element={<CartApp />} />
  </Routes>
</BrowserRouter>

// Product app handles /products/*
<BrowserRouter basename="/products">
  <Routes>
    <Route path="/" element={<ProductList />} />
    <Route path="/:id" element={<ProductDetail />} />
  </Routes>
</BrowserRouter>

```

**2. Centralized Routing:**

```javascript
// Host app manages all routes
<BrowserRouter>
  <Routes>
    <Route path="/products" element={<ProductList />} />
    <Route path="/products/:id" element={<ProductDetail />} />
    <Route path="/cart" element={<CartApp />} />
  </Routes>
</BrowserRouter>

```

**3. Hash-Based Routing:**

```javascript
// Each app uses hash routing
// Host: #/products, #/cart
// Product: #/products/list, #/products/:id

```

**Best Practices:**

* Use base paths for each microfrontend

* Avoid route conflicts

* Handle 404s gracefully

* Support deep linking

📌 **In simple terms**: Each microfrontend can have its own router with base paths, or host app can manage all routes centrally. Avoid route conflicts.

---

## 6. Styling and CSS Isolation

### 🔹 CSS Isolation Strategies

**1. CSS Modules:**

```javascript
// Product app
import styles from './ProductApp.module.css';

function ProductApp() {
  return <div className={styles.container}>Product</div>;
}

```

**2. Scoped CSS (Vue, Svelte):**

```vue
<style scoped>
.container {
  color: blue;
}
</style>

```

**3. CSS-in-JS:**

```javascript
// Styled-components
const Container = styled.div`
  color: blue;
`;

```

**4. Shadow DOM:**

```javascript
class ProductApp extends HTMLElement {
  connectedCallback() {
    const shadow = this.attachShadow({ mode: 'closed' });
    shadow.innerHTML = `<style>.container { color: blue; }</style>
      <div class="container">Product</div>`;
  }
}

```

**5. CSS Namespacing:**

```css
/* Product app */
.product-app .container {
  color: blue;
}

/* Cart app */
.cart-app .container {
  color: red;
}

```

**Best Practices:**

* Use CSS Modules or CSS-in-JS for isolation

* Avoid global CSS conflicts

* Use consistent naming conventions

* Consider design system/tokens

📌 **In simple terms**: Isolate CSS using CSS Modules, scoped CSS, CSS-in-JS, Shadow DOM, or namespacing to prevent style conflicts between microfrontends.

---

## 7. Shared Dependencies and Code Sharing

### 🔹 Dependency Sharing Strategies

**1. Shared Dependencies (Module Federation):**

```javascript
// webpack.config.js
shared: {
  react: { singleton: true, requiredVersion: '^18.0.0' },
  'react-dom': { singleton: true, requiredVersion: '^18.0.0' },
  'react-router-dom': { singleton: true },
}

```

**2. External Dependencies (CDN):**

```html
<!-- Load from CDN -->
<script src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
<script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>

```

**3. Shared Libraries:**

```javascript
// shared-libs package
export { Button, Input, Modal } from './components';
export { apiClient, authService } from './services';
export { formatCurrency, formatDate } from './utils';

// Microfrontends import
import { Button, apiClient } from '@company/shared-libs';

```

**4. Monorepo Sharing:**

```javascript
// In monorepo
// packages/shared-components
export const Button = () => { /* ... */ };

// apps/product-app
import { Button } from '@company/shared-components';

```

**Best Practices:**

* Share common dependencies (React, utilities)

* Version dependencies carefully

* Use singleton for shared state libraries

* Document shared dependencies

📌 **In simple terms**: Share common dependencies (React, utilities) to reduce bundle size. Use Module Federation shared config, CDN, or shared packages.

---

## 8. Testing Microfrontends

### 🔹 Testing Strategies

**1. Unit Testing (Each Microfrontend):**

```javascript
// Product app tests
import { render, screen } from '@testing-library/react';
import ProductApp from './ProductApp';

test('renders product list', () => {
  render(<ProductApp />);
  expect(screen.getByText('Products')).toBeInTheDocument();
});

```

**2. Integration Testing:**

```javascript
// Test microfrontend integration
import { render } from '@testing-library/react';
import HostApp from './HostApp';

test('loads product microfrontend', async () => {
  render(<HostApp />);
  await waitFor(() => {
    expect(screen.getByText('Product App')).toBeInTheDocument();
  });
});

```

**3. E2E Testing:**

```javascript
// Cypress test
describe('Microfrontend Integration', () => {
  it('navigates between microfrontends', () => {
    cy.visit('/');
    cy.contains('Products').click();
    cy.url().should('include', '/products');
    cy.contains('Product List').should('be.visible');
  });
});

```

**4. Contract Testing:**

```javascript
// Test API contracts between microfrontends
test('product app publishes correct event format', () => {
  const event = new CustomEvent('product-selected', {
    detail: { productId: 123 }
  });
  expect(event.detail).toHaveProperty('productId');
  expect(typeof event.detail.productId).toBe('number');
});

```

📌 **In simple terms**: Test each microfrontend independently (unit tests), test integration, test end-to-end flows, and test contracts between microfrontends.

---

## 9. Deployment Strategies

### 🔹 Deployment Approaches

**1. Independent Deployment:**

* Each microfrontend deployed separately

* Different URLs/domains

* Host app loads from different origins

**2. Coordinated Deployment:**

* Deploy in specific order

* Use feature flags

* Gradual rollout

**3. Blue-Green Deployment:**

* Deploy new version alongside old

* Switch traffic when ready

* Rollback if issues

**4. Canary Deployment:**

* Deploy to small percentage of users

* Monitor and gradually increase

* Rollback if problems

**Best Practices:**

* Independent deployment when possible

* Use feature flags for gradual rollout

* Monitor deployments

* Have rollback strategy

📌 **In simple terms**: Deploy microfrontends independently when possible. Use feature flags, blue-green, or canary deployments for safer releases.

---

## 10. Challenges and Solutions

### 🔹 Common Challenges

**1. Bundle Size:**

* **Problem**: Multiple frameworks increase bundle size

* **Solution**: Share dependencies, code splitting, lazy loading

**2. Performance:**

* **Problem**: Runtime loading can be slow

* **Solution**: Preload critical microfrontends, optimize bundles, use CDN

**3. Consistency:**

* **Problem**: Different teams, different styles

* **Solution**: Design system, shared components, style guide

**4. Communication:**

* **Problem**: Complex communication between microfrontends

* **Solution**: Clear contracts, message bus, shared state management

**5. Testing:**

* **Problem**: Hard to test integration

* **Solution**: Contract testing, integration tests, E2E tests

**6. Versioning:**

* **Problem**: Different versions of dependencies

* **Solution**: Shared dependency versions, version contracts

📌 **In simple terms**: Challenges include bundle size, performance, consistency, communication, testing, and versioning. Address with shared dependencies, design systems, clear contracts, and proper testing.

---

## ⭐ Summary — 10-second Interview Version

> "Microfrontend breaks large frontend into independent apps. Patterns: build-time (simple), runtime (Module Federation), server-side (SSI), iframe (isolation). Use Module Federation or Single-SPA. Handle communication, routing, styling isolation, shared dependencies, testing, and deployment."

---

## ⭐ Extra Points (If Interviewer Asks More)

### What are the main benefits of microfrontends?

Independent development and deployment, technology diversity, team autonomy, scalability, and faster development with smaller codebases.

### How do you handle communication between microfrontends?

Use props for parent-child, custom events for siblings, shared state for global data, URL parameters, or a message bus. Choose based on coupling needs.

### What's the difference between Module Federation and Single-SPA?

Module Federation uses Webpack 5 for runtime integration with shared dependencies. Single-SPA is framework-agnostic with lifecycle management and routing integration.

### How do you prevent CSS conflicts in microfrontends?

Use CSS Modules, scoped CSS, CSS-in-JS, Shadow DOM, or CSS namespacing to isolate styles and prevent conflicts between microfrontends.

### What are the main challenges with microfrontends?

Bundle size (multiple frameworks), performance (runtime loading), consistency (different teams), communication complexity, testing integration, and dependency versioning.

---

---

## 📍 Navigation

<div align="center">

[19) Patterns.md](19%29%20Patterns.md) • [Questions Index](question.md)

[FE-System-Design Cheatsheet](FE-System-Design%20Interview%20Cheatsheet.md]

</div>

---
