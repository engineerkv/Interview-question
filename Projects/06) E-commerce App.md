# 1) Problem Statement

Design and implement a full-featured e-commerce platform that addresses the following challenges:

- **Core Functionality**: Enable users to browse products, manage shopping carts, process secure payments, and track orders with a seamless shopping experience
- **Scale Requirements**: Handle millions of products, support thousands of concurrent users, and scale to handle peak traffic during sales events (10x normal traffic)
- **Performance**: Fast page loads (< 2 seconds), optimized product images, efficient search and filtering
- **Product Catalog**: Support complex search and filtering, product recommendations, reviews and ratings
- **Inventory Management**: Real-time inventory tracking with consistency guarantees to prevent overselling
- **Payment Processing**: Secure payment processing with multiple payment methods (cards, UPI, wallets, COD) and fraud detection
- **Order Management**: Order tracking, cancellation, returns, refunds, and invoice generation
- **Data Consistency**: Maintain data consistency for inventory and orders across distributed systems

---

# 2) High Level Design (HLD)

## a) Functional Requirements

#### User Management

- **User registration and authentication** - Users can sign up with email, phone, or social login - makes it easy to get started

- **User profile management** - Users can update profile, addresses, payment methods

- **Guest checkout** - Users can purchase without creating account - reduces friction

- **Wishlist** - Save products for later - like a shopping list

- **Order history** - View past orders and track current orders

#### Product Catalog

- **Product browsing** - Browse products by category, brand, price range

- **Product search** - Search products by name, description, features

- **Product filters** - Filter by price, brand, rating, availability

- **Product sorting** - Sort by price, rating, popularity, newest

- **Product details** - View product images, description, reviews, specifications

- **Product recommendations** - "Customers who bought this also bought" - helps discover products

#### Shopping Cart

- **Add to cart** - Add products to shopping cart

- **Update cart** - Change quantities, remove items

- **Cart persistence** - Cart saved across sessions - don't lose items

- **Cart summary** - See total, discounts, shipping costs

#### Checkout & Payment

- **Multiple addresses** - Save and select delivery addresses

- **Payment methods** - Credit/debit cards, UPI, net banking, wallets, COD

- **Coupon codes** - Apply discount codes - save money

- **Order summary** - Review order before placing

- **Order placement** - Place order and get confirmation

#### Order Management

- **Order tracking** - Track order status in real-time - know where your order is

- **Order cancellation** - Cancel orders before shipping

- **Returns & refunds** - Return products and get refunds

- **Invoice generation** - Download invoices for orders

#### Reviews & Ratings

- **Product reviews** - Users can write reviews with ratings

- **Review moderation** - Moderate reviews before publishing

- **Helpful votes** - Users can vote if review is helpful

- **Review filters** - Filter reviews by rating, verified purchase

---

## b) Non-Functional Requirements

#### Performance

- **Fast page loads** - Product pages load in < 2 seconds - users expect fast shopping

- **Image optimization** - Lazy load product images, use WebP format - faster loading

- **Code splitting** - Only load code for current page - faster initial load

- **Caching** - Cache product data, search results - reduce server load

#### Scalability

- **Handle traffic spikes** - Handle Black Friday, sale events - thousands of concurrent users

- **CDN for assets** - Serve images, static files from CDN - faster globally

- **Database optimization** - Fast product search, efficient queries

- **Load balancing** - Distribute traffic across multiple servers

#### User Experience

- **Responsive design** - Works great on mobile, tablet, desktop - most users shop on mobile

- **Smooth navigation** - Fast page transitions, no lag

- **Search suggestions** - Auto-complete search as user types - like Google search

- **Quick view** - View product details without leaving list page

#### Security

- **Secure payments** - PCI-DSS compliant payment processing

- **Data encryption** - All sensitive data encrypted

- **XSS protection** - Prevent script injection in reviews

- **CSRF protection** - Prevent cross-site request forgery

---

---

## c) MVP (Minimum Viable Product)

### Phase 1: Core Features - Must Have

**Core shopping experience - what users need to buy products**

#### Functional

- **User authentication** - Sign up, login, guest checkout

- **Product catalog** - Browse products, search, filters, product details

- **Shopping cart** - Add to cart, update, checkout

- **Payment integration** - Payment gateway integration

- **Order management** - Place order, view orders, basic tracking

#### Non-Functional

- **Performance** - Fast page loads, optimized images

- **Responsive** - Mobile-first design

- **Security** - Secure payments, data encryption

### Phase 2: Enhanced Features - Priority 2

**Features that improve user experience and increase sales**

#### Functional

- **Wishlist** - Save products for later

- **Product recommendations** - "You may also like"

- **Reviews & ratings** - User reviews and ratings

- **Advanced search** - Better search with filters

- **Order tracking** - Real-time order tracking

#### Non-Functional

- **Advanced caching** - Better caching strategies

- **Analytics** - Track user behavior, conversion rates

### Phase 3: Advanced Features - Priority 3

**Advanced features for power users and business growth**

#### Functional

- **Personalization** - Personalized product recommendations

- **Loyalty program** - Rewards, points, discounts

- **Social features** - Share products, wishlists

- **Advanced analytics** - Business intelligence, reports

---

---

## d) Technology Choices

### Frontend Framework

- **React.js** - Component-based UI library for building interactive interfaces
- **TypeScript** - Type safety and better developer experience
- **React Router** - Client-side routing for single-page application

### State Management

- **React Query (TanStack Query)** - Server state management, caching, and synchronization
- **Redux Toolkit** (or **Zustand**) - Global state for cart, user preferences, orders
- **Context API** - User authentication, app configuration
- **useState/useReducer** - Local component state

### UI/UX Libraries

- **Material-UI / Chakra UI** - Component library for faster development
- **React Hot Toast** - Toast notifications for user feedback
- **Chart.js / Recharts** - Analytics visualization (if needed)

### Build Tools

- **Vite** - Fast build tool and dev server
- **Webpack** (alternative) - Module bundler

### Testing

- **React Testing Library** - Component testing
- **Vitest / Jest** - Unit testing framework
- **Playwright / Cypress** - E2E testing

### Deployment

- **Vercel / Netlify** - Static site hosting with CDN
- **AWS S3 + CloudFront** - Alternative deployment option

---

## e) Architecture Overview

The frontend follows a layered architecture with clear separation of concerns, optimized for e-commerce operations.

**Component Structure:**

```

Frontend Application
├── Presentation Layer
│   ├── UI Components (Buttons, Inputs, Cards)
│   ├── Feature Components (ProductList, ShoppingCart)
│   └── Layout Components (Header, Footer, Navigation)
├── Business/Controller Layer
│   ├── Business Logic (Validation, calculations, formatting)
│   ├── Custom Hooks (useCart, useProducts, useCheckout)
│   └── Utilities (Helpers, formatters)
├── State Management
│   ├── Client State
│   │   ├── Local State (useState)
│   │   ├── Global State (Redux Toolkit)
│   │   └── Context API (App config)
│   └── Server State
│       ├── React Query (Primary)
│       └── Service Worker (Offline)
├── API Integration
│   ├── API Client (Axios with interceptors)
│   ├── API Services (productService, cartService)
│   └── Error Handling & Retry Logic
└── Routing
    ├── Public Routes (Home, Products)
    ├── Protected Routes (Cart, Checkout, Orders)
    └── Route Guards (Authentication checks)

```

**Frontend Deployment:**

- **Build**: Production bundle with code splitting using Webpack/Vite
- **CDN**: Static assets served from CloudFront/Cloudflare edge locations
- **Caching**: Aggressive caching for static assets, cache-busting for updates
- **Environment**: Environment variables for API endpoints and feature flags

**Key Frontend Components:**

- **React 19 Application**:
  - Single-page application with client-side routing
  - Component-based architecture for reusability
  - React Query with React 19 hooks (useOptimistic, useTransition, useDeferredValue)
  - Shopping cart with optimistic updates
  - Responsive design for mobile and desktop
  - Modern React 19 features for better performance and UX

- **CDN/Edge**:
  - Global distribution of static assets
  - Edge caching for improved performance
  - DDoS protection and rate limiting at edge

---

## f) App Flow

### Complete System Flow (Frontend Perspective)

**Primary User Flow - Product Purchase:**

1. **User browses products** → ProductList component displays products with React Query useSuspenseQuery (React 19)
2. **User applies filters** → FilterSidebar updates filters, useDeferredValue (React 19) defers expensive filtering
3. **User clicks product** → ProductCard navigates to ProductDetailPage
4. **User adds to cart** → AddToCartButton triggers useOptimistic (React 19) for instant cart update
5. **Cart updates** → ShoppingCart component shows updated cart with optimistic item
6. **User proceeds to checkout** → CheckoutPage renders with cart items and total
7. **Payment processing** → PaymentForm uses useActionState (React 19) for form handling
8. **Order confirmation** → OrderConfirmation component displays order details

**Component Interaction Flow:**

```
User Browses → ProductList (React Query useSuspenseQuery)
            ↓
Filter Applied → FilterSidebar (useDeferredValue for performance)
            ↓
Add to Cart → AddToCartButton (useOptimistic for instant UI)
            ↓
Cart Update → ShoppingCart (Redux Toolkit state)
            ↓
Checkout → CheckoutForm (useActionState for form)
            ↓
Order Created → OrderConfirmation (receives order data)
```

**State Update Flow:**

1. **Local State** → Product filters, form inputs use useState
2. **Deferred State** → useDeferredValue (React 19) defers expensive product filtering
3. **Optimistic State** → useOptimistic (React 19) shows cart items immediately
4. **Server State** → React Query manages products, cart, orders, caching, refetching
5. **Global State** → Redux Toolkit manages cart, user preferences
6. **Component Re-render** → React updates UI based on state changes

**Error Handling Flow:**

1. **API Error** → React Query mutation returns error
2. **Error Boundary** → Catches component errors, shows fallback UI
3. **User Feedback** → Toast notification displays error message
4. **Retry Logic** → User can retry failed requests

**Shopping Cart Flow:**

1. **User adds product** → AddToCartButton triggers mutation
2. **Optimistic update** → useOptimistic (React 19) adds item to cart immediately
3. **API call** → useMutation sends POST request to /api/v1/cart
4. **Success response** → React Query cache updates, cart persists
5. **Cart display** → ShoppingCart shows updated cart with item count

**Checkout Flow:**

1. **User clicks checkout** → Navigate to CheckoutPage
2. **Address selection** → AddressForm allows selecting/adding address
3. **Payment method** → PaymentMethodSelector allows choosing payment
4. **Order review** → OrderSummary shows items, total, shipping
5. **Order placement** → PlaceOrderButton triggers useActionState (React 19)
6. **Order confirmation** → OrderConfirmation displays order ID and details

**Product Filtering Flow:**

1. **User selects filters** → FilterSidebar updates filter state
2. **URL update** → Query params updated via React Router
3. **Deferred filtering** → useDeferredValue (React 19) defers expensive filtering
4. **Refetch products** → React Query refetches with new filters
5. **Update UI** → ProductList re-renders with filtered products

# 3) Component Architecture

Think of the frontend as a tree of React components - each component handles a specific part of the UI, and they work together to create the complete user experience.

**Component Hierarchy:**

```
App
├── Layout
│   ├── Header
│   │   ├── Logo
│   │   ├── Navigation
│   │   ├── SearchBar
│   │   └── ShoppingCartIcon
│   ├── MainContent
│   └── Footer
├── Pages
│   ├── HomePage
│   │   ├── HeroBanner
│   │   ├── CategoryList
│   │   └── FeaturedProducts
│   ├── ProductListPage
│   │   ├── FilterSidebar
│   │   │   ├── PriceFilter
│   │   │   ├── BrandFilter
│   │   │   └── RatingFilter
│   │   └── ProductGrid
│   │       └── ProductCard
│   ├── ProductDetailPage
│   │   ├── ProductImages
│   │   ├── ProductInfo
│   │   │   ├── ProductTitle
│   │   │   ├── ProductPrice
│   │   │   ├── ProductRating
│   │   │   └── AddToCartButton
│   │   └── ProductReviews
│   ├── ShoppingCartPage
│   │   ├── CartItemList
│   │   │   └── CartItem
│   │   └── CartSummary
│   ├── CheckoutPage
│   │   ├── AddressForm
│   │   ├── PaymentMethodSelector
│   │   └── OrderSummary
│   └── OrderHistoryPage
│       └── OrderList
└── SharedComponents
    ├── Button
    ├── Input
    ├── Card
    ├── Toast
    └── LoadingSpinner
```

**Key React Components:**

**1. ProductList Component:**

- Displays products in grid or list view
- Fetches products with React Query useSuspenseQuery (React 19)
- Uses useDeferredValue (React 19) for deferred filtering
- Implements virtual scrolling for large product lists
- Handles pagination and infinite scroll

**2. ProductCard Component:**

- Displays product image, name, price, rating
- Handles add to cart functionality
- Uses useOptimistic (React 19) for instant cart updates
- Shows product availability status
- Links to product detail page

**3. ShoppingCart Component:**

- Displays cart items with quantities
- Manages cart state with Redux Toolkit
- Handles quantity updates and item removal
- Shows cart total and item count
- Uses useOptimistic (React 19) for instant updates

**4. CheckoutForm Component:**

- Handles address and payment method selection
- Uses useActionState (React 19) for form submission
- Validates form inputs before submission
- Processes order creation
- Shows order confirmation

**5. FilterSidebar Component:**

- Displays product filters (price, brand, rating)
- Updates filter state with Redux Toolkit
- Uses useDeferredValue (React 19) for deferred filtering
- Updates URL query parameters
- Handles filter clearing

**Component Communication:**

- **Props** → Parent to child data flow
- **Callbacks** → Child to parent communication
- **Context API** → Shared state across components (theme, user)
- **React Query** → Server state management (products, cart, orders)
- **Redux Toolkit** → Global client state (cart, filters, user preferences)

# 4) Data Models

### TypeScript Interfaces

```typescript
interface Product {
  id: string;
  name: string;
  description: string;
  price: number;
  originalPrice?: number;
  images: string[];
  category: string;
  brand: string;
  rating: number;
  reviewCount: number;
  inStock: boolean;
  stockCount: number;
  createdAt: string;
}

interface CartItem {
  id: string;
  productId: string;
  product: Product;
  quantity: number;
  price: number;
  addedAt: string;
}

interface Cart {
  id: string;
  userId: string;
  items: CartItem[];
  total: number;
  subtotal: number;
  shipping: number;
  tax: number;
  updatedAt: string;
}

interface Order {
  id: string;
  userId: string;
  items: CartItem[];
  total: number;
  status: "pending" | "processing" | "shipped" | "delivered" | "cancelled";
  shippingAddress: Address;
  paymentMethod: PaymentMethod;
  createdAt: string;
  updatedAt: string;
}

interface Address {
  id: string;
  userId: string;
  type: "home" | "work" | "other";
  street: string;
  city: string;
  state: string;
  zipCode: string;
  country: string;
  isDefault: boolean;
}

interface PaymentMethod {
  id: string;
  type: "card" | "upi" | "wallet" | "cod";
  last4?: string;
  isDefault: boolean;
}

interface FormState {
  productId: string;
  quantity: number;
  errors: {
    productId?: string;
    quantity?: string;
  };
}
  images: string[];
  inStock: boolean;
}

```

# 5) API Design

### GET /api/v1/products

- **URL:** `/api/v1/products?q=query&category=electronics&minPrice=100&maxPrice=1000&page=1&limit=20`
- **Method:** GET
- **Description:** Search and filter products
- **Query Parameters:**
 - `q`(optional) - Search query
 - `category`(optional) - Filter by category
 - `minPrice`, `maxPrice`(optional) - Price range filter
 - `page`(default: 1)
 - `limit`(default: 20)
- **Response:**

 ```json
 {
 "success": true,
 "data": {
 "products": [...],
 "total": 1250,
 "page": 1,
 "limit": 20
 }
 }

 ```

- **Status Codes:** 200 (Success)

### POST /api/v1/cart

- **URL:** `/api/v1/cart`
- **Method:** POST
- **Description:** Add item to cart
- **Request Body:**

 ```json
 {
 "productId": "product_abc123",
 "quantity": 2
 }

 ```

- **Response:**

 ```json
 {
 "success": true,
 "data": {
 "cart": {
 "items": [...],
 "total": 199.98
 }
 }
 }

 ```

- **Status Codes:** 201 (Created), 400 (Validation Error), 404 (Product Not Found)

---

### Redis Cache

**Cache Strategy:**

- **Key Format:** `product:{productId}`, `search:{query}:{filters}`, `cart:{userId}`
- **Value:** Serialized JSON (product data, search results, cart data)
- **TTL:**
 - Product data: 3600 seconds (1 hour)
 - Search results: 300 seconds (5 minutes)
 - Cart data: 86400 seconds (24 hours)
- **Eviction Policy:** LRU (Least Recently Used)

**Cache Patterns:**

- **Cache-Aside Pattern:** Check cache first, if miss query database and update cache
- **Write-Through Pattern:** Update cache when product data changes
- **Cache Invalidation:** Invalidate product cache on product updates

---

### Error Scenarios and Responses

**Edge Cases Handling:**

- **Product Out of Stock:** Return 409 Conflict when adding out-of-stock product to cart
- **Invalid Payment:** Return 402 Payment Required with payment error details
- **Order Not Found:** Return 404 Not Found
- **Inventory Insufficient:** Return 409 Conflict when order quantity exceeds available stock

**Error Response Format:**

```json
{
 "error": {
 "code": "OUT_OF_STOCK",
 "message": "Product is out of stock",
 "details": "Product product_abc123 has 0 units available"
 }
}

```

---

# 6) Protocols

### REST API Protocol

**Request Format:**

## iii) Implementation Details

### Business/Controller Layer

**Custom Hooks:**

- Encapsulate business logic and API calls
- Example: `useCart`, `useProducts`, `useCheckout`, `useOrders`
- Handle data transformation and validation

**Service Functions:**

- Pure functions for data processing and validation
- URL validation, data transformation, format checking
- Reusable across components

### Advanced Component Patterns

**Compound Components:**

- Group related components together (e.g., Form.Input, Form.Button)
- Share implicit state between components

**Render Props Pattern:**

- Pass render functions as props for flexible component composition

**Custom Hooks Pattern:**

- Extract reusable logic into custom hooks
- Example: `useCart`, `useProducts`, `useWishlist`

**Higher-Order Components (HOCs):**

- Wrap components with additional functionality
- Example: `withAuth`, `withLoading`

### Performance Optimizations

- **Code splitting** with React.lazy() and Suspense
- **Memoization** with useMemo() and useCallback()
- **Virtual scrolling** for long lists (react-window, react-virtuoso)
- **Image optimization** and lazy loading
- **Debouncing and throttling** for user inputs
- **React.memo** for preventing unnecessary re-renders

### UI/UX Enhancements

- **Toast notifications** for user feedback (react-hot-toast)
- **Loading states** and skeleton screens
- **Error boundaries** for error handling
- **Responsive design** for mobile and desktop
- **Accessibility features** (ARIA labels, keyboard navigation, focus management)
- **Animations** with Framer Motion or CSS transitions

### Code Examples

**Custom Hook Example:**

```typescript
**Custom Hook: useCart (React 19)**
```typescript

import { useOptimistic, useTransition } from 'react';
import { useMutation } from '@tanstack/react-query';

function useCart() {
  const [optimisticCart, addOptimisticItem] = useOptimistic(
    [] as CartItem[],
    (currentCart, newItem: CartItem) => [...currentCart, newItem]
  );
  const [isPending, startTransition] = useTransition();

  return useMutation({
    mutationFn: async (item: CartItem) => {
      addOptimisticItem(item);
      return await addToCart(item);
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['cart'] });
    }
  });
}

```

**Component with React Query (React 19):**
```typescript

function AddToCartButton({ product }: { product: Product }) {
  const [isPending, startTransition] = useTransition();
  const addToCartMutation = useCart();

  const handleAddToCart = () => {
    startTransition(() => {
      addToCartMutation.mutate({
        productId: product.id,
        quantity: 1
      });
    });
  };

  return (
    <button onClick={handleAddToCart} disabled={isPending}>
      {isPending ? 'Adding...' : 'Add to Cart'}
    </button>
  );
}

```

```

**Cart Implementation:**

- Add/remove items with optimistic updates
- Calculate totals
- Persist to localStorage
- Sync with server

**Product Filtering:**

- URL-based filter state
- Debounced price range
- Multi-select categories

# 7) Low Level Design (LLD)

## ii) State Management

### Client State

**Local State (useState):**

- Component-specific UI state (form inputs, modal visibility, loading states)
- Example: `const [isOpen, setIsOpen] = useState(false);`

**Global State:**

- Redux Toolkit OR Zustand for complex global state
- Context API for user authentication, theme preferences
- Example: User preferences, app configuration

### Server State

**React Query (TanStack Query):**

- `useQuery` for data fetching and caching
- `useMutation` for data mutations (create, update, delete)
- Automatic refetching, background updates, optimistic updates
- Example: API data caching, synchronization

**Cart State:**

- Redux Toolkit for cart items
- React Query for product data
- LocalStorage for cart persistence
- Optimistic updates for cart operations

## iii) Implementation Details

### Business/Controller Layer

**Custom Hooks:**

- Encapsulate business logic and API calls
- Example: `useCart`, `useProducts`, `useCheckout`, `useOrders`

**Service Functions:**

- Pure functions for data processing and validation
- URL validation, data transformation, format checking

### Performance Optimizations

- Code splitting with React.lazy()
- Memoization with useMemo() and useCallback()
- Virtual scrolling for long lists
- Image optimization and lazy loading
- Debouncing and throttling for user inputs

### UI/UX Enhancements

- Toast notifications for user feedback
- Loading states and skeleton screens
- Error boundaries for error handling
- Responsive design for mobile and desktop
  - Modern React 19 features for better performance and UX
- Accessibility features (ARIA labels, keyboard navigation)

**Cart Implementation:**

- Add/remove items with optimistic updates
- Calculate totals
- Persist to localStorage
- Sync with server

**Product Filtering:**

- URL-based filter state
- Debounced price range
- Multi-select categories

## iv) Testing

### Component Testing

- React Testing Library for component tests
- Test user interactions and component behavior
- Example: Test form submission, button clicks, input validation

### Integration Testing

- Test component interactions
- Test API integration with mock data
- Test state management flows

### E2E Testing

- Playwright or Cypress for end-to-end tests
- Test complete user flows
- Example: Test E-commerce App flow from start to finish

**Cart Tests:**

- Test add to cart
- Test remove from cart
- Test quantity update
- Test cart persistence

# 8) Algorithms

### Frontend Algorithms

**Cart Total Calculation Algorithm:**

```javascript
function calculateCartTotal(cartItems) {
  const subtotal = cartItems.reduce((sum, item) => {
    return sum + (item.price * item.quantity);
  }, 0);

  const shipping = subtotal > 100 ? 0 : 10; // Free shipping over $100
  const tax = subtotal * 0.08; // 8% tax
  const total = subtotal + shipping + tax;

  return {
    subtotal: Math.round(subtotal * 100) / 100,
    shipping: Math.round(shipping * 100) / 100,
    tax: Math.round(tax * 100) / 100,
    total: Math.round(total * 100) / 100
  };
}
```

**Product Filtering Algorithm:**

```javascript
function filterProducts(products, filters) {
  return products.filter(product => {
    if (filters.category && product.category !== filters.category) return false;
    if (filters.minPrice && product.price < filters.minPrice) return false;
    if (filters.maxPrice && product.price > filters.maxPrice) return false;
    if (filters.brand && product.brand !== filters.brand) return false;
    if (filters.rating && product.rating < filters.rating) return false;
    if (filters.inStock && !product.inStock) return false;
    return true;
  });
}
```

**Price Formatting Algorithm:**

```javascript
function formatPrice(price, currency = 'USD') {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: currency
  }).format(price);
}
```

**Debouncing Algorithm (for search):**

```javascript
function debounce(func, delay) {
  let timeoutId;
  return (...args) => {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => func(...args), delay);
  };
}
```

**Cart Total Calculation:**

```javascript
function calculateCartTotal(items) {
  return items.reduce((total, item) => {
    return total + (item.price * item.quantity);
  }, 0);
}

```

# 9) Security

### Frontend Security

**Input Validation:**

- Client-side validation before form submission
- Sanitize user input to prevent XSS attacks
- Validate data formats (URLs, emails, custom aliases)

**XSS Prevention:**

- React automatically escapes content
- Use `dangerouslySetInnerHTML` only when necessary with sanitization
- Content Security Policy (CSP) headers

**CSRF Protection:**

- SameSite cookies for authentication
- CSRF tokens for state-changing operations
- Verify origin header on API requests

**Secure Storage:**

- Never store sensitive data in localStorage
- Use httpOnly cookies for authentication tokens
- Clear sensitive data on logout

**HTTPS:**

- All API calls over HTTPS
- Enforce HTTPS in production
- HSTS headers for security

**Rate Limiting (Client-Side):**

- Debounce API calls to prevent abuse
- Show user-friendly messages when rate limited
- Implement exponential backoff for retries

**Cart Security:**

- Validate product IDs
- Sanitize quantity inputs
- Rate limit cart operations
- CSRF protection for cart updates

# 10) Deployment and DevOps

### Frontend Deployment

**Build Optimization:**

- Production build with code splitting and tree shaking
- Minification and compression
- Asset optimization (images, fonts)
- Environment variables for API endpoints

**CI/CD Pipeline:**

- Automated testing on pull requests
- Build and deploy on merge to main
- Preview deployments for feature branches
- Rollback capabilities

**Deployment Platforms:**

- Vercel / Netlify for static site hosting with CDN
- AWS S3 + CloudFront for alternative deployment
- GitHub Pages for simple static sites

**Monitoring:**

- Error tracking (Sentry, LogRocket)
- Performance monitoring (Web Vitals)
- Analytics (user behavior, page views)

**E-commerce Config:**

- `VITE_API_URL`
- `VITE_PAYMENT_GATEWAY_URL`
- `VITE_ENABLE_CART_PERSISTENCE`

# 11) Interview Answers (Frontend Focus)

### Q: How would you handle state management for this system?

**Answer (STAR Method):**

**Situation:** In a E-commerce App system, we need to manage both client-side UI state and server-side data efficiently.

**Action:**

- Use React Query for server state (URL data, analytics) - handles caching, refetching, and synchronization
- Use useState for local component state (form inputs, modal visibility)
- Use Context API for global client state (user authentication, theme preferences)
- Implement optimistic updates for better UX

**Result:** Reduced API calls through caching, improved performance, better user experience with instant feedback.

**Takeaway:** Separating client and server state management leads to cleaner code and better performance.

### Q: How would you implement shopping cart functionality?

**Answer (STAR Method):**

**Situation:** Users need to add products and manage cart.

**Action:**

- Use Redux Toolkit for cart state
- Implement optimistic updates
- Persist to localStorage
- Sync with server on login

**Result:** Fast cart operations, offline support, better UX.

**Takeaway:** Optimistic updates and localStorage persistence improve cart UX.
