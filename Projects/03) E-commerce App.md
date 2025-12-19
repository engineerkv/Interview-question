# E-commerce App

> **Project Type:** Full-Stack Web Application (MERN Stack)
> **Scale:** Handle millions of products, peak traffic during sales events, thousands of concurrent users
> **Tech Stack:** React.js, Node.js, Express.js, MongoDB, Redis, Elasticsearch, AWS S3, CDN

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

## a) Requirements

### i) Functional Requirements

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

### ii) Non-Functional Requirements

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

## b) Scope and Priority

### Phase 1: MVP (Must Have) - Priority 1

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

## c) Technology Choices

### Frontend Framework

- **React.js:** Perfect for building interactive e-commerce interfaces
 - **Component-based** - Product cards, cart items, filters are reusable components
 - **Fast updates** - Virtual DOM makes product list updates smooth
 - **Code splitting** - Load product pages only when needed
 - **TypeScript** - Type safety for product data, cart, orders

### State Management

- **Redux Toolkit:** Manages complex state (cart, user, products, orders)
 - **Cart state** - Products in cart, quantities, totals
 - **User state** - Authentication, profile, addresses
 - **Product state** - Product list, filters, search results
 - **Order state** - Current order, order history

### Routing

- **React Router v6:** Client-side routing for smooth navigation
 - **Product pages** - `/products/:id` for product details
 - **Category pages** - `/category/:name` for category browsing
 - **Cart page** - `/cart` for shopping cart
 - **Checkout** - `/checkout` for payment

### UI Components

- **Material-UI:** Pre-built components for faster development
 - **Product cards** - Consistent product display
 - **Forms** - Checkout forms, search forms
 - **Modals** - Quick view, product zoom
 - **Responsive grid** - Product grid that adapts to screen size

### Search

- **Client-side search:** For small catalogs, search in browser

- **Server-side search:** For large catalogs, search on server (Elasticsearch)
 - **Why server-side?** Can't load all products in browser
 - **Elasticsearch** - Fast full-text search, filters, sorting

### Image Handling

- **Image optimization:** Compress images, use WebP format

- **Lazy loading:** Load images as user scrolls - like Instagram

- **CDN:** Serve images from CDN - faster loading globally

- **Responsive images:** Show smaller images on mobile

### Payment Gateway

- **Payment Gateway:** Payment gateway for processing payments
 - **Multiple methods** - Cards, UPI, net banking, wallets
 - **Secure** - PCI-DSS compliant
 - **Easy integration** - Simple API, good documentation

---

## e) Architecture Overview

```

┌─────────────────────────────────────────────────────────┐
│ Frontend (React.js) - Client Side │
│ (This is what users see in their browser) │
├─────────────────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────────────┐ │
│ │ Browser (Chrome, Firefox, Safari) │ │
│ │ ┌────────────────────────────────────────────┐ │ │
│ │ │ React.js Application (SPA) │ │ │
│ │ │ ┌──────────────────────────────────────┐ │ │ │
│ │ │ │ React Router (Client-side Routing) │ │ │ │
│ │ │ └──────────────────────────────────────┘ │ │ │
│ │ │ ┌──────────────────────────────────────┐ │ │ │
│ │ │ │ Redux Toolkit (State Management) │ │ │ │
│ │ │ │ - Cart, User, Products, Orders │ │ │ │
│ │ │ └──────────────────────────────────────┘ │ │ │
│ │ │ ┌──────────────────────────────────────┐ │ │ │
│ │ │ │ Material-UI Components │ │ │ │
│ │ │ └──────────────────────────────────────┘ │ │ │
│ │ └────────────────────────────────────────────┘ │ │
│ └──────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
 │
 │ HTTP/REST API Calls
 ▼
┌─────────────────────────────────────────────────────────┐
│ Backend (Node.js + Express.js) │
│ (Server that handles business logic and data) │
├─────────────────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────────────┐ │
│ │ Load Balancer / API Gateway │ │
│ └──────────────────────────────────────────────────┘ │
│ │ │
│ ┌───────────────┼───────────────┐ │
│ ▼ ▼ ▼ │
│ ┌──────────┐ ┌──────────┐ ┌──────────┐ │
│ │ Express │ │ Express │ │ Express │ │
│ │ Server 1 │ │ Server 2 │ │ Server 3 │ │
│ └──────────┘ └──────────┘ └──────────┘ │
│ │ │ │ │
│ └───────────────┼───────────────┘ │
│ ▼ │
│ ┌──────────────────────────────────────────────────┐ │
│ │ Business Logic Layer │ │
│ │ - Product Service (catalog, search) │ │
│ │ - Cart Service (cart management) │ │
│ │ - Order Service (order processing) │ │
│ │ - User Service (authentication, profiles) │ │
│ │ - Review Service (reviews, ratings) │ │
│ └──────────────────────────────────────────────────┘ │
│ ▼ │
│ ┌──────────────────────────────────────────────────┐ │
│ │ Data Access Layer │ │
│ │ - MongoDB (Products, users, orders) │ │
│ │ - Elasticsearch (Product search) │ │
│ │ - Redis (Caching, sessions) │ │
│ └──────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
 │ │ │
 ▼ ▼ ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ MongoDB │ │ Elasticsearch│ │ Redis │
│ (Database) │ │ (Search) │ │ (Cache) │
│ │ │ │ │ │
│ - Products │ │ - Product │ │ - Product │
│ - Users │ │ Index │ │ Cache │
│ - Orders │ │ - Search │ │ - Sessions │
│ - Reviews │ │ Results │ │ │
└──────────────┘ └──────────────┘ └──────────────┘
 │ │ │
 └────────────────────┼────────────────────┘
 │
 ▼
 ┌──────────────┐
 │ External │
 │ Services │
 │ │
 │ - Payment │
 │ Gateway │
 │ - AWS S3 │
 │ - CDN │
 └──────────────┘

```

The system follows a layered architecture with clear separation of concerns across frontend and backend. Here's how the complete system works:

### Frontend Architecture

**Frontend Layers:**

1. **Presentation Layer (React Components)**
 - **UI Components**: Reusable components (ProductCard, CartItem, Button, Input)
 - **Feature Components**: ProductList, ShoppingCart, CheckoutForm, OrderHistory
 - **Layout Components**: Header, Footer, Navigation, MainLayout
 - **Page Components**: HomePage, ProductPage, CartPage, CheckoutPage

2. **State Management Layer**
 - **Local State (useState)**: Component-specific UI state (form inputs, loading, errors)
 - **Server State (Redux Toolkit)**: Global state for cart, user, products, orders
 - **API State (React Query)**: Product data caching, refetching, optimistic updates

3. **API Integration Layer**
 - **API Client**: Axios instance with interceptors for auth, error handling
 - **Redux Thunks**: Async actions for API operations (fetchProducts, addToCart)
 - **Request/Response Transformation**: Data normalization and error handling

4. **Routing Layer (React Router)**
 - **Route Configuration**: Define routes and protected routes
 - **Navigation**: Programmatic and declarative navigation
 - **Route Guards**: Authentication and authorization checks

5. **Build & Deployment Layer**
 - **Build Process**: Webpack/Vite bundling with code splitting
 - **Static Assets**: Served from CDN (CloudFront/Cloudflare)
 - **Environment Configuration**: Environment-specific API endpoints and configs

**Frontend Request Flow:**

1. **User Interaction** → User browses products or adds to cart
2. **State Update** → Redux action dispatched or React Query mutation triggered
3. **API Call** → Axios makes HTTP request to backend API
4. **Loading State** → UI shows loading indicator
5. **Response Handling** → Success/error state updates Redux store or React Query cache
6. **UI Update** → Components re-render with new data

3. **Application Service Layer** - Business logic and orchestration
4. **Cache Layer** - In-memory caching for performance
5. **Database Layer** - Persistent data storage
6. **Search Layer** - Elasticsearch for product search
7. **External Services** - Payment gateway, S3, CDN

### Complete Request Flow

**Product Browsing Flow:**

1. **Frontend**: User navigates to product listing page
2. **Load Balancer**: Routes request to available API server
3. **API Server**: Validates request, extracts query parameters
4. **Cache Check**: Check Redis for cached product list
5. **Database/Search**: If cache miss, query MongoDB or Elasticsearch
6. **Response**: Return product list to frontend
7. **Frontend**: Display products with images from CDN

**Add to Cart Flow:**

1. **Frontend**: User clicks "Add to Cart" button
2. **Redux Action**: Dispatch addToCart action
3. **API Call**: POST request to cart API
4. **Backend**: Validate product, check inventory, update cart in MongoDB
5. **Cache Update**: Update Redis cache for cart
6. **Response**: Return updated cart to frontend
7. **Frontend**: Update Redux store, show cart badge with item count

**Checkout Flow:**

1. **Frontend**: User proceeds to checkout
2. **API Call**: POST request to checkout API with cart items and address
3. **Backend**: Validate cart, check inventory, calculate totals
4. **Payment Gateway**: Process payment via payment gateway
5. **Order Creation**: Create order in MongoDB with transaction
6. **Inventory Update**: Decrement inventory quantities
7. **Response**: Return order confirmation to frontend
8. **Frontend**: Show order confirmation page

### Key Components

- **Frontend (React.js)**: Single-page application with client-side routing, component-based architecture, Redux for state management
- **CDN/Edge**: Global distribution of static assets and product images, reduces latency
- **Load Balancer**: Distributes traffic across API servers, SSL/TLS termination
- **API Servers**: Stateless design for horizontal scaling, handle product catalog, cart, orders, payments
- **Application Services**: Product Service, Cart Service, Order Service, User Service, Review Service
- **Cache Layer (Redis)**: In-memory cache for hot products (20% of traffic), cart data, sessions
- **Database (MongoDB)**: Sharded across multiple nodes for horizontal scaling, stores products, users, orders, reviews
- **Search (Elasticsearch)**: Fast full-text search for products, handles complex filters and sorting
- **Payment Gateway**: Payment gateway for secure payment processing
- **Image Storage (AWS S3)**: Stores product images, served via CDN

1. **React.js for Frontend:** Perfect for interactive e-commerce - product filters, cart updates, search all need fast UI updates
 - **Component-based** - Product cards, cart items are reusable
 - **Fast navigation** - No page reloads, smooth transitions
 - **Code splitting** - Product pages load only when needed

2. **Redux Toolkit for State:** Complex state needs (cart, user, products) - Redux keeps it organized
 - **Cart state** - Products, quantities, totals - many components need this
 - **User state** - Authentication, profile - shared across app
 - **Product state** - Search results, filters - shared between pages

3. **Server-side Search:** Can't load all products in browser - use Elasticsearch for fast search
 - **Why Elasticsearch?** Fast full-text search, handles millions of products
 - **Filters & sorting** - Elasticsearch handles complex queries efficiently
 - **Scalable** - Can handle growing product catalog

4. **CDN for Images:** Product images are large - CDN makes them load faster globally
 - **Why CDN?** Images served from edge locations - closer to users
 - **Faster loading** - Especially important for product images
 - **Reduces server load** - Images don't hit main server

5. **Guest Checkout:** Users can buy without account - reduces friction, increases conversions
 - **Why important?** Many users don't want to create account
 - **Better UX** - Faster checkout process
 - **More sales** - Less friction = more purchases

---

# 3) Low Level Design (LLD)

## a) Frontend

### i) Component Architecture

**Think of this as the building blocks - how components are organized and connected**

### Component Hierarchy (React.js)

```

App (Root Component - Entry Point)
├── Layout (Main Layout with Navigation)
│ ├── Header
│ │ ├── Logo
│ │ ├── SearchBar (with autocomplete)
│ │ ├── NavigationMenu
│ │ └── UserMenu (Cart icon, User account)
│ ├── Sidebar (Mobile Menu)
│ │ ├── CategoryMenu
│ │ └── UserMenu
│ └── Main Content Area
│ ├── HomePage
│ │ ├── HeroBanner
│ │ ├── CategoryGrid
│ │ ├── FeaturedProducts
│ │ └── DealsSection
│ ├── ProductListPage
│ │ ├── FilterSidebar
│ │ │ ├── PriceFilter
│ │ │ ├── BrandFilter
│ │ │ ├── RatingFilter
│ │ │ └── AvailabilityFilter
│ │ ├── ProductGrid
│ │ │ └── ProductCard
│ │ │ ├── ProductImage
│ │ │ ├── ProductTitle
│ │ │ ├── ProductPrice
│ │ │ ├── ProductRating
│ │ │ └── AddToCartButton
│ │ └── Pagination
│ ├── ProductDetailPage
│ │ ├── ProductImageGallery
│ │ ├── ProductInfo
│ │ │ ├── ProductTitle
│ │ │ ├── ProductPrice
│ │ │ ├── ProductRating
│ │ │ ├── ProductDescription
│ │ │ ├── AddToCartButton
│ │ │ └── BuyNowButton
│ │ ├── ProductSpecifications
│ │ ├── ProductReviews
│ │ │ ├── ReviewSummary
│ │ │ └── ReviewList
│ │ │ └── ReviewCard
│ │ └── RelatedProducts
│ ├── CartPage
│ │ ├── CartItemList
│ │ │ └── CartItem
│ │ │ ├── ProductImage
│ │ │ ├── ProductInfo
│ │ │ ├── QuantitySelector
│ │ │ ├── Price
│ │ │ └── RemoveButton
│ │ ├── CartSummary
│ │ │ ├── Subtotal
│ │ │ ├── Shipping
│ │ │ ├── Discount
│ │ │ ├── Total
│ │ │ └── CheckoutButton
│ │ └── EmptyCartState
│ ├── CheckoutPage
│ │ ├── AddressForm
│ │ ├── PaymentMethodSelection
│ │ ├── OrderSummary
│ │ └── PlaceOrderButton
│ ├── OrderHistoryPage
│ │ ├── OrderList
│ │ │ └── OrderCard
│ │ │ ├── OrderInfo
│ │ │ ├── OrderItems
│ │ │ ├── OrderStatus
│ │ │ └── TrackOrderButton
│ │ └── EmptyState
│ └── WishlistPage
│ ├── WishlistItems
│ │ └── WishlistItem
│ │ ├── ProductCard
│ │ └── RemoveButton
│ └── EmptyState
└── Footer
 ├── Links
 ├── SocialMedia
 └── Copyright

```

**How components work together:**

- **App** - Root component, handles routing and global state

- **Layout** - Wraps all pages, provides navigation and header/footer

- **ProductListPage** - Shows products with filters and pagination

- **ProductDetailPage** - Shows single product with reviews and related products

- **CartPage** - Shows cart items and summary

- **CheckoutPage** - Handles address and payment selection

- **OrderHistoryPage** - Shows past orders with tracking

---

```
App
├── Header
│ ├── Logo
│ ├── SearchBar (with autocomplete)
│ ├── NavigationMenu
│ └── UserMenu (Cart, Profile, Sign out)
├── MainContent
│ ├── ProductListPage
│ │ ├── FilterSidebar
│ │ │ ├── CategoryFilter
│ │ │ ├── PriceRangeFilter
│ │ │ ├── BrandFilter
│ │ │ └── RatingFilter
│ │ ├── ProductGrid
│ │ │ └── ProductCard
│ │ │ ├── ProductImage
│ │ │ ├── ProductTitle
│ │ │ ├── ProductPrice
│ │ │ ├── ProductRating
│ │ │ └── AddToCartButton
│ │ └── Pagination
│ ├── ProductDetailPage
│ │ ├── ProductImages
│ │ ├── ProductInfo
│ │ │ ├── ProductTitle
│ │ │ ├── ProductPrice
│ │ │ ├── ProductRating
│ │ │ ├── QuantitySelector
│ │ │ ├── AddToCartButton
│ │ │ └── BuyNowButton
│ │ ├── ProductDescription
│ │ ├── ProductReviews
│ │ │ ├── ReviewList
│ │ │ └── ReviewForm
│ │ └── RelatedProducts
│ ├── CartPage
│ │ ├── CartItemList
│ │ │ └── CartItem
│ │ │ ├── ProductImage
│ │ │ ├── ProductInfo
│ │ │ ├── QuantitySelector
│ │ │ ├── Price
│ │ │ └── RemoveButton
│ │ ├── CartSummary
│ │ │ ├── Subtotal
│ │ │ ├── Shipping
│ │ │ ├── Discount
│ │ │ ├── Total
│ │ │ └── CheckoutButton
│ │ └── EmptyCartState
│ ├── CheckoutPage
│ │ ├── AddressForm
│ │ ├── PaymentMethodSelection
│ │ ├── OrderSummary
│ │ └── PlaceOrderButton
│ └── OrderHistoryPage
│ ├── OrderList
│ │ └── OrderCard
│ │ ├── OrderInfo
│ │ ├── OrderItems
│ │ ├── OrderStatus
│ │ └── TrackOrderButton
│ └── EmptyState
└── Footer
 ├── Links
 ├── SocialMedia
 └── Copyright

```

### Key React Components

**Frontend Implementation:**

```javascript
// Product Card Component
const ProductCard<{ product: Product }> = ({ product }) => {
 const dispatch = useAppDispatch();
 const [loading, setLoading] = useState(false);

 const handleAddToCart = async () => {
 setLoading(true);
 try {
 await dispatch(addToCart({ productId: product.id, quantity: 1 })).unwrap();
 // Show success toast
 } catch (err) {
 // Show error toast
 } finally {
 setLoading(false);
 }
 };

 return (
 <div className="product-card">
 <Link to={`/products/${product.id}`}>
 <img src={product.image} alt={product.name} />
 <h3>{product.name}</h3>
 <div className="price">${product.price}</div>
 <div className="rating">{product.rating} ⭐</div>
 </Link>
 <button onClick={handleAddToCart} disabled={loading}>
 {loading ? 'Adding...' : 'Add to Cart'}
 </button>
 </div>
 );
};

// Cart Item Component
const CartItem<{ item: CartItem }> = ({ item }) => {
 const dispatch = useAppDispatch();

 const handleQuantityChange = (newQuantity) => {
 dispatch(updateCartItem({ itemId: item.id, quantity: newQuantity }));
 };

 const handleRemove = () => {
 dispatch(removeFromCart(item.id));
 };

 return (
 <div className="cart-item">
 <img src={item.product.image} alt={item.product.name} />
 <div className="item-info">
 <h4>{item.product.name}</h4>
 <div className="price">${item.product.price}</div>
 </div>
 <QuantitySelector
 quantity={item.quantity}
 onChange={handleQuantityChange}
 max={item.product.stock}
 />
 <div className="item-total">${item.product.price * item.quantity}</div>
 <button onClick={handleRemove}>Remove</button>
 </div>
 );
};

```

### ii) State Management

**State Management Strategy (React 19):**

- **Local State (useState)**: Form inputs, UI state (loading, errors, modals, dropdowns)
- **Optimistic Updates (useOptimistic)**: React 19 hook for optimistic cart/product updates
- **Form Actions (useActionState)**: React 19 hook for checkout forms and server actions
- **Deferred Values (useDeferredValue)**: React 19 hook for search debouncing
- **Transitions (useTransition)**: React 19 hook for non-urgent UI updates
- **API State**: React Query for server state (product data, search results, order history) - caching, refetching
- **Global State (Redux Toolkit)**: Cart items, user authentication, wishlist, selected filters

**Frontend Implementation:**

```javascript
// Using React Query for API state management
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

const useProducts = (filters: ProductFilters) => {
 return useQuery({
 queryKey: ['products', filters],
 queryFn: async () => {
 const response = await axios.get('/api/v1/products', { params: filters });
 return response.data;
 },
 staleTime: 5 * 60 * 1000 // Cache for 5 minutes
 });
};

const useAddToCart = () => {
 const queryClient = useQueryClient();
 const dispatch = useAppDispatch();

 return useMutation({
 mutationFn: async ({ productId, quantity }: { productId; quantity}) => {
 const response = await axios.post('/api/v1/cart/items', { productId, quantity });
 return response.data;
 },
 onSuccess: (data) => {
 // Update Redux cart state
 dispatch(setCart(data.cart));
 // Invalidate cart queries
 queryClient.invalidateQueries({ queryKey: ['cart'] });
 }
 });
};

```

### iii) Advanced Shopping Cart Patterns

**Optimistic Cart Updates with React 19:**

```javascript
import { useOptimistic, useTransition } from 'react';

const ShoppingCart= () => {
 const [cart, setCart] = useState({ items: [] });
 const [isPending, startTransition] = useTransition();

 // React 19: useOptimistic for cart updates
 const [optimisticCart, addOptimisticItem] = useOptimistic(
 cart,
 (state, newItem: CartItem) => ({
 ...state,
 items: [...state.items, { ...newItem, id: 'temp', syncing: true }]
 })
 );

 const handleAddToCart = async (product: Product, quantity) => {
 const newItem: CartItem = {
 id: 'temp',
 productId: product.id,
 product,
 quantity,
 price: product.price
 };

 // Optimistically add to UI
 startTransition(() => {
 addOptimisticItem(newItem);
 });

 try {
 const result = await addToCartAPI({ productId: product.id, quantity });
 // Update with real data from server
 setCart(result.cart);
 toast.success('Added to cart!');
 } catch (error) {
 // Rollback on error - remove temp item
 setCart(prev => ({
 ...prev,
 items: prev.items.filter(item => item.id !== 'temp')
 }));
 toast.error('Failed to add item to cart');
 }
 };

 return (
 <div className="cart">
 {optimisticCart.items.map(item => (
 <CartItem key={item.id} item={item} />
 ))}
 </div>
 );
};
```

**Cart Persistence:**

```javascript
// Persist cart to localStorage
const cartMiddleware: Middleware = (store) => (next) => (action) => {
 const result = next(action);

 if (action.type.startsWith('cart/')) {
 const state = store.getState();
 localStorage.setItem('cart', JSON.stringify(state.cart));
 }

 return result;
};

// Hydrate cart on app load
useEffect(() => {
 const savedCart = localStorage.getItem('cart');
 if (savedCart) {
 const cart = JSON.parse(savedCart);
 dispatch(setCart(cart));
 // Sync with backend
 syncCartWithBackend(cart);
 }
}, []);
```

**Quantity Selector with Validation:**

```javascript
const QuantitySelector<{
 quantity;
 max;
 onChange: (qty) => void;
}> = ({ quantity, max, onChange }) => {
 const [localQty, setLocalQty] = useState(quantity);
 const [error, setError] = useState('');

 const handleChange = (value) => {
 const num = parseInt(value);

 if (isNaN(num) || num < 1) {
 setError('Quantity must be at least 1');
 return;
 }

 if (num > max) {
 setError(`Only ${max} available`);
 return;
 }

 setError('');
 setLocalQty(num);
 onChange(num);
 };

 const increment = () => {
 if (localQty < max) {
 handleChange((localQty + 1).toString());
 }
 };

 const decrement = () => {
 if (localQty > 1) {
 handleChange((localQty - 1).toString());
 }
 };

 return (
 <div className="quantity-selector">
 <button onClick={decrement} disabled={localQty <= 1}>-</button>
 <input
 type="number"
 value={localQty}
 onChange={(e) => handleChange(e.target.value)}
 min={1}
 max={max}
 aria-label="Quantity"
 />
 <button onClick={increment} disabled={localQty >= max}>+</button>
 {error && <span className="error">{error}</span>}
 {localQty >= max && <span className="warning">Max available</span>}
 </div>
 );
};
```

### iv) Product Catalog UI Patterns

**Advanced Product Search with Autocomplete:**

```javascript
const SearchBar= () => {
 const [query, setQuery] = useState('');
 const [suggestions, setSuggestions] = useState([]);
 const [showSuggestions, setShowSuggestions] = useState(false);

 const { data: searchResults } = useQuery({
 queryKey: ['search', query],
 queryFn: () => searchProducts(query),
 enabled: query.length >= 2,
 staleTime: 30000
 });

 useEffect(() => {
 if (searchResults) {
 setSuggestions(searchResults.slice(0, 5));
 setShowSuggestions(true);
 }
 }, [searchResults]);

 return (
 <div className="search-bar">
 <input
 type="text"
 value={query}
 onChange={(e) => setQuery(e.target.value)}
 onFocus={() => setShowSuggestions(true)}
 placeholder="Search products..."
 aria-label="Search products"
 />
 {showSuggestions && suggestions.length > 0 && (
 <ul className="suggestions" role="listbox">
 {suggestions.map(product => (
 <li
 key={product.id}
 onClick={() => {
 navigate(`/products/${product.id}`);
 setShowSuggestions(false);
 }}
 role="option"
 >
 <img src={product.image} alt={product.name} />
 <span>{product.name}</span>
 <span className="price">${product.price}</span>
 </li>
 ))}
 </ul>
 )}
 </div>
 );
};
```

**Product Image Gallery with Zoom:**

```javascript
const ProductImageGallery<{ images[] }> = ({ images }) => {
 const [selectedIndex, setSelectedIndex] = useState(0);
 const [zoom, setZoom] = useState(false);
 const [zoomPosition, setZoomPosition] = useState({ x: 0, y: 0 });

 const handleMouseMove = (e: React.MouseEvent) => {
 if (!zoom) return;

 const rect = e.currentTarget.getBoundingClientRect();
 const x = ((e.clientX - rect.left) / rect.width) * 100;
 const y = ((e.clientY - rect.top) / rect.height) * 100;

 setZoomPosition({ x, y });
 };

 return (
 <div className="product-gallery">
 <div
 className="main-image"
 onMouseEnter={() => setZoom(true)}
 onMouseLeave={() => setZoom(false)}
 onMouseMove={handleMouseMove}
 >
 <img
 src={images[selectedIndex]}
 alt={`Product image ${selectedIndex + 1}`}
 style={{
 transform: zoom ? `scale(2) translate(-${zoomPosition.x}%, -${zoomPosition.y}%)` : 'scale(1)',
 transformOrigin: `${zoomPosition.x}% ${zoomPosition.y}%`
 }}
 />
 </div>
 <div className="thumbnail-list">
 {images.map((img, index) => (
 <button
 key={index}
 onClick={() => setSelectedIndex(index)}
 className={selectedIndex === index ? 'active' : ''}
 aria-label={`View image ${index + 1}`}
 >
 <img src={img} alt={`Thumbnail ${index + 1}`} />
 </button>
 ))}
 </div>
 </div>
 );
};
```

**Infinite Scroll Product List:**

```javascript
const ProductList<{ filters: ProductFilters }> = ({ filters }) => {
 const {
 data,
 fetchNextPage,
 hasNextPage,
 isFetchingNextPage,
 isLoading
 } = useInfiniteQuery({
 queryKey: ['products', filters],
 queryFn: ({ pageParam = 1 }) => fetchProducts({ ...filters, page: pageParam }),
 getNextPageParam: (lastPage, pages) => {
 return lastPage.hasNextPage ? pages.length + 1 : undefined;
 }
 });

 const observerTarget = useRef(null);

 useEffect(() => {
 const observer = new IntersectionObserver(
 (entries) => {
 if (entries[0].isIntersecting && hasNextPage && !isFetchingNextPage) {
 fetchNextPage();
 }
 },
 { threshold: 0.1 }
 );

 if (observerTarget.current) {
 observer.observe(observerTarget.current);
 }

 return () => observer.disconnect();
 }, [hasNextPage, isFetchingNextPage, fetchNextPage]);

 const products = data?.pages.flatMap(page => page.products) || [];

 return (
 <div className="product-list">
 {products.map(product => (
 <ProductCard key={product.id} product={product} />
 ))}
 <div ref={observerTarget} className="load-more-trigger">
 {isFetchingNextPage && <LoadingSpinner />}
 </div>
 </div>
 );
};
```

**Filter Sidebar with URL State:**

```javascript
const FilterSidebar= () => {
 const [searchParams, setSearchParams] = useSearchParams();
 const [filters, setFilters] = useState({
 minPrice: searchParams.get('minPrice') || '',
 maxPrice: searchParams.get('maxPrice') || '',
 brands: searchParams.get('brands')?.split(',') || [],
 rating: searchParams.get('rating') || ''
 });

 const updateFilters = (newFilters: Partial<typeof filters>) => {
 const updated = { ...filters, ...newFilters };
 setFilters(updated);

 // Update URL params
 const params = new URLSearchParams();
 if (updated.minPrice) params.set('minPrice', updated.minPrice);
 if (updated.maxPrice) params.set('maxPrice', updated.maxPrice);
 if (updated.brands.length) params.set('brands', updated.brands.join(','));
 if (updated.rating) params.set('rating', updated.rating);

 setSearchParams(params);
 };

 return (
 <aside className="filter-sidebar">
 <h3>Filters</h3>

 <div className="filter-group">
 <label>Price Range</label>
 <div className="price-inputs">
 <input
 type="number"
 placeholder="Min"
 value={filters.minPrice}
 onChange={(e) => updateFilters({ minPrice: e.target.value })}
 />
 <span>-</span>
 <input
 type="number"
 placeholder="Max"
 value={filters.maxPrice}
 onChange={(e) => updateFilters({ maxPrice: e.target.value })}
 />
 </div>
 </div>

 <div className="filter-group">
 <label>Brand</label>
 {brands.map(brand => (
 <label key={brand} className="checkbox-label">
 <input
 type="checkbox"
 checked={filters.brands.includes(brand)}
 onChange={(e) => {
 const brands = e.target.checked
 ? [...filters.brands, brand]
 : filters.brands.filter(b => b !== brand);
 updateFilters({ brands });
 }}
 />
 {brand}
 </label>
 ))}
 </div>

 <button onClick={() => {
 setFilters({ minPrice: '', maxPrice: '', brands: [], rating: '' });
 setSearchParams({});
 }}>
 Clear Filters
 </button>
 </aside>
 );
};
```

### v) Checkout Flow Implementation

**Multi-Step Checkout Form:**

```javascript
const CheckoutPage= () => {
 const [step, setStep] = useState(1);
 const [formData, setFormData] = useState({
 address: {},
 payment: {},
 shipping: {}
 });

 const steps = [
 { id: 1, name: 'Shipping Address', component: AddressForm },
 { id: 2, name: 'Payment Method', component: PaymentForm },
 { id: 3, name: 'Review Order', component: OrderReview }
 ];

 const CurrentStepComponent = steps[step - 1].component;

 const handleNext = (data: any) => {
 setFormData(prev => ({ ...prev, ...data }));
 if (step < steps.length) {
 setStep(step + 1);
 }
 };

 const handleBack = () => {
 if (step > 1) {
 setStep(step - 1);
 }
 };

 return (
 <div className="checkout-page">
 <div className="checkout-steps">
 {steps.map((s, index) => (
 <div
 key={s.id}
 className={`step ${step === s.id ? 'active' : step > s.id ? 'completed' : ''}`}
 >
 <div className="step-number">{s.id}</div>
 <div className="step-name">{s.name}</div>
 </div>
 ))}
 </div>

 <CurrentStepComponent
 data={formData}
 onNext={handleNext}
 onBack={handleBack}
 isLastStep={step === steps.length}
 />
 </div>
 );
};
```

**Address Form with Validation:**

```javascript
const AddressForm = ({ data, onNext }) => {
 const [formData, setFormData] = useState(data.address);
 const [errors, setErrors] = useState>({});

 const validate = ()=> {
 const newErrors: Record<string, string> = {};
 if (!formData.fullName.trim()) newErrors.fullName = 'Full name is required';
 if (!formData.addressLine1.trim()) newErrors.addressLine1 = 'Address is required';
 if (!formData.city.trim()) newErrors.city = 'City is required';
 if (!formData.state) newErrors.state = 'State is required';
 if (!formData.zipCode.trim()) newErrors.zipCode = 'Zip code is required';

 setErrors(newErrors);
 return Object.keys(newErrors).length === 0;
 };

 const onSubmit = (e) => {
 e.preventDefault();
 if (validate()) {
 onNext({ address: formData });
 }
 };

 return (
 <form onSubmit={onSubmit}>
 <div className="form-group">
 <label>Full Name</label>
 <input
 value={formData.fullName}
 onChange={(e) => setFormData({ ...formData, fullName: e.target.value })}
 aria-invalid={errors.fullName ? 'true' : 'false'}
 />
 {errors.fullName && <span className="error">{errors.fullName}</span>}
 </div>

 <div className="form-group">
 <label>Address Line 1</label>
 <input
 value={formData.addressLine1}
 onChange={(e) => setFormData({ ...formData, addressLine1: e.target.value })}
 />
 {errors.addressLine1 && <span className="error">{errors.addressLine1}</span>}
 </div>

 <div className="form-group">
 <label>City</label>
 <input
 value={formData.city}
 onChange={(e) => setFormData({ ...formData, city: e.target.value })}
 />
 {errors.city && <span className="error">{errors.city}</span>}
 </div>

 <div className="form-row">
 <div className="form-group">
 <label>State</label>
 <select
 value={formData.state}
 onChange={(e) => setFormData({ ...formData, state: e.target.value })}
 >
 {states.map(state => (
 <option key={state} value={state}>{state}</option>
 ))}
 </select>
 </div>

 <div className="form-group">
 <label>ZIP Code</label>
 <input {...register('zipCode')} />
 </div>
 </div>

 <button type="submit">Continue to Payment</button>
 </form>
 );
};
```

**Payment Integration:**

```javascript
const PaymentForm = ({ data, onNext }) => {
 const [paymentMethod, setPaymentMethod] = useState('card');
 const [cardElement, setCardElement] = useState(null);

 const handlePayment = async (paymentData: PaymentData) => {
 try {
 // Process payment via payment gateway
 const result = await processPayment({
 amount: data.orderTotal,
 method: paymentMethod,
 ...paymentData
 });

 if (result.success) {
 onNext({ payment: { ...paymentData, transactionId: result.id } });
 } else {
 toast.error('Payment failed. Please try again.');
 }
 } catch (error) {
 toast.error('Payment error occurred');
 }
 };

 return (
 <div className="payment-form">
 <div className="payment-methods">
 <button
 className={paymentMethod === 'card' ? 'active' : ''}
 onClick={() => setPaymentMethod('card')}
 >
 Credit/Debit Card
 </button>
 <button
 className={paymentMethod === 'upi' ? 'active' : ''}
 onClick={() => setPaymentMethod('upi')}
 >
 UPI
 </button>
 <button
 className={paymentMethod === 'cod' ? 'active' : ''}
 onClick={() => setPaymentMethod('cod')}
 >
 Cash on Delivery
 </button>
 </div>

 {paymentMethod === 'card' && (
 <CardElement
 options={{
 style: { base: { fontSize: '16px' } }
 }}
 onReady={(element: any) => setCardElement(element)}
 />
 )}

 {paymentMethod === 'upi' && (
 <UPIInput onComplete={handlePayment} />
 )}

 {paymentMethod === 'cod' && (
 <div>
 <p>Pay cash when your order is delivered</p>
 <button onClick={() => handlePayment({ method: 'cod' })}>
 Place Order
 </button>
 </div>
 )}
 </div>
 );
};
```

### vi) Performance Optimizations

**Image Lazy Loading & Optimization:**

```javascript
const ProductImage<{ src; alt; priority?}> = ({
 src,
 alt,
 priority = false
}) => {
 const [loaded, setLoaded] = useState(false);
 const [error, setError] = useState(false);

 return (
 <div className="product-image-wrapper">
 {!loaded && !error && (
 <div className="image-skeleton" aria-hidden="true" />
 )}
 <img
 src={error ? '/placeholder.png' : src}
 alt={alt}
 loading={priority ? 'eager' : 'lazy'}
 decoding="async"
 onLoad={() => setLoaded(true)}
 onError={() => {
 setError(true);
 setLoaded(true);
 }}
 className={loaded ? 'loaded' : 'loading'}
 style={{ opacity: loaded ? 1 : 0 }}
 />
 </div>
 );
};
```

**Virtual Scrolling for Product Lists:**

```javascript
const VirtualizedProductList<{ products: Product[] }> = ({ products }) => {
 const parentRef = useRef(null);

 const virtualizer = useVirtualizer({
 count: products.length,
 getScrollElement: () => parentRef.current,
 estimateSize: () => 400, // Estimated product card height
 overscan: 5
 });

 return (
 <div ref={parentRef} style={{ height: '100vh', overflow: 'auto' }}>
 <div
 style={{
 height: `${virtualizer.getTotalSize()}px`,
 width: '100%',
 position: 'relative'
 }}
 >
 {virtualizer.getVirtualItems().map(virtualItem => (
 <div
 key={virtualItem.key}
 style={{
 position: 'absolute',
 top: 0,
 left: 0,
 width: '100%',
 height: `${virtualItem.size}px`,
 transform: `translateY(${virtualItem.start}px)`
 }}
 >
 <ProductCard product={products[virtualItem.index]} />
 </div>
 ))}
 </div>
 </div>
 );
};
```

**Debounced Search:**

```javascript
const useDebouncedSearch = (query, delay= 300) => {
 const [debouncedQuery, setDebouncedQuery] = useState(query);

 useEffect(() => {
 const timer = setTimeout(() => {
 setDebouncedQuery(query);
 }, delay);

 return () => clearTimeout(timer);
 }, [query, delay]);

 return debouncedQuery;
};

const ProductSearch= () => {
 const [query, setQuery] = useState('');
 const debouncedQuery = useDebouncedSearch(query);

 const { data: results } = useQuery({
 queryKey: ['search', debouncedQuery],
 queryFn: () => searchProducts(debouncedQuery),
 enabled: debouncedQuery.length >= 2
 });

 return (
 <input
 type="text"
 value={query}
 onChange={(e) => setQuery(e.target.value)}
 placeholder="Search products..."
 />
 );
};
```

### vii) Real-time Inventory Updates

**WebSocket Integration for Stock Updates:**

```javascript
const useProductStock = (productId) => {
 const [stock, setStock] = useState(null);
 const socketRef = useRef<WebSocket | null>(null);

 useEffect(() => {
 socketRef.current = new WebSocket(`ws://api.example.com/products/${productId}/stock`);

 socketRef.current.onmessage = (event) => {
 const data = JSON.parse(event.data);
 setStock(data.stock);

 if (data.stock === 0) {
 toast.error('Product is out of stock');
 }
 };

 return () => {
 socketRef.current?.close();
 };
 }, [productId]);

 return stock;
};
```

### viii) Implementation Details

**Data Flow:**

1. **Product Browsing** → ProductListPage fetches products via React Query with infinite scroll, displays ProductCard components with lazy-loaded images
2. **Product Selection** → User clicks ProductCard, navigates to ProductDetailPage with image gallery and zoom
3. **Add to Cart** → User clicks AddToCartButton, optimistically updates Redux cart state, syncs with backend, shows toast notification
4. **Cart View** → CartPage displays cart items from Redux with quantity selector, allows real-time updates
5. **Checkout** → Multi-step checkout form collects address and payment, processes payment via gateway, creates order

**Event Handling:**

- Product search triggers debounced API call with autocomplete suggestions
- Add to cart updates Redux state optimistically with rollback on error
- Cart quantity changes sync with backend and update totals in real-time
- Form submissions validate client-side before API calls
- Real-time inventory updates via WebSocket for stock availability
- Payment processing with loading states and error handling

**UI/UX Considerations:**

- **Loading States**: Skeleton loaders for product lists, spinners for actions, progress indicators for multi-step forms
- **Error Handling**: User-friendly error messages with retry options, toast notifications for actions
- **Validation**: Real-time client-side form validation with helpful error messages
- **Responsive Design**: Mobile-first layout using CSS Grid/Flexbox, collapsible filters on mobile, touch-friendly buttons
- **Accessibility**: ARIA labels, keyboard navigation, screen reader support, focus management, semantic HTML
- **Performance**: Image lazy loading with WebP/AVIF formats, virtual scrolling for long product lists, code splitting per route, service worker for offline support
- **Progressive Enhancement**: Works without JavaScript for basic browsing, enhanced experience with JS enabled

---

## Data Models

### Product Model

```javascript
// Product structure:
//
 id;
 name;
 description;
 price;
 originalPrice?; // For discounts
 images[]; // Array of image URLs
 category;
 brand;
 rating; // Average rating (1-5)
 reviewCount;
 stock; // Available quantity
 specifications: Record<string, string>; // Key-value pairs
 tags[];
 createdAt;
 updatedAt;

```

### Cart Item Model

```javascript
// CartItem structure:
//
 productId;
 product: Product; // Populated product data
 quantity;
 price; // Price at time of adding to cart

```

### Order Model

```javascript
// Order structure:
//
 id;
 userId;
 items: OrderItem[];
 shippingAddress: Address;
 billingAddress: Address;
 paymentMethod;
 paymentStatus: 'pending' | 'paid' | 'failed' | 'refunded';
 orderStatus: 'pending' | 'confirmed' | 'shipped' | 'delivered' | 'cancelled';
 subtotal;
 shipping;
 discount;
 total;
 orderDate;
 estimatedDelivery?;
 trackingNumber?;

```

### Review Model

```javascript
// Review structure:
//
 id;
 productId;
 userId;
 userName;
 rating; // 1-5 stars
 title;
 comment;
 verifiedPurchase;
 helpfulCount;
 createdAt;

```

### User Model

```javascript
// User structure:
//
 id;
 email;
 name;
 phone?;
 addresses: Address[];
 paymentMethods: PaymentMethod[];
 wishlist[]; // Array of product IDs
 createdAt;

```

---

## Data APIs

**Note:** All API endpoints are implemented on the **backend (Node.js/Express)**, and the **frontend (React.js)** calls these APIs using Axios.

### Product APIs

**Frontend Implementation:** React components call these APIs and display products

#### GET /api/products

- **URL:** `/api/products?category=electronics&page=1&limit=20&sort=price&order=asc`

- **Method:** GET

- **Query Parameters:**
 - `category` - Filter by category
 - `page` - Page number
 - `limit` - Items per page
 - `sort` - Sort field (price, rating, name)
 - `order` - Sort order (asc, desc)
 - `minPrice`, `maxPrice` - Price range
 - `brand` - Filter by brand
 - `rating` - Minimum rating

- **Response:**

 ```json
 {
 "success": true,
 "data": {
 "products": [/* Product objects */],
 "pagination": {
 "page": 1,
 "limit": 20,
 "total": 150,
 "totalPages": 8
 }
 }
 }

 ```

#### GET /api/products/:id

- **URL:** `/api/products/123`

- **Method:** GET

- **Response:**

 ```json
 {
 "success": true,
 "data": {
 "product": {/* Product object with full details */}
 }
 }

 ```

#### GET /api/products/search

- **URL:** `/api/products/search?q=laptop&page=1`

- **Method:** GET

- **Description:** Search products using Elasticsearch

- **Response:**

 ```json
 {
 "success": true,
 "data": {
 "products": [/* Product objects */],
 "suggestions": ["laptop bag", "laptop stand"],
 "pagination": {/* pagination info */}
 }
 }

 ```

### Cart APIs

#### GET /api/cart

- **URL:** `/api/cart`

- **Method:** GET

- **Authentication:** Required

- **Response:**

 ```json
 {
 "success": true,
 "data": {
 "items": [/* CartItem objects */],
 "subtotal": 5000,
 "shipping": 100,
 "total": 5100
 }
 }

 ```

#### POST /api/cart/add

- **URL:** `/api/cart/add`

- **Method:** POST

- **Request Body:**

 ```json
 {
 "productId": "123",
 "quantity": 2
 }

 ```

#### PUT /api/cart/update

- **URL:** `/api/cart/update`

- **Method:** PUT

- **Request Body:**

 ```json
 {
 "productId": "123",
 "quantity": 3
 }

 ```

#### DELETE /api/cart/remove/:productId

- **URL:** `/api/cart/remove/123`

- **Method:** DELETE

### Order APIs

#### POST /api/orders

- **URL:** `/api/orders`

- **Method:** POST

- **Request Body:**

 ```json
 {
 "shippingAddress": {/* Address object */},
 "paymentMethod": "card",
 "paymentDetails": {/* Payment details */}
 }

 ```

#### GET /api/orders

- **URL:** `/api/orders`

- **Method:** GET

- **Response:**

 ```json
 {
 "success": true,
 "data": {
 "orders": [/* Order objects */]
 }
 }

 ```

#### GET /api/orders/:id

- **URL:** `/api/orders/123`

- **Method:** GET

---

## b) Backend

*Note: Backend implementation details are kept minimal. Focus is on frontend integration.*

**API Endpoints Reference:**

- `GET /api/products` - Get products with filters
- `GET /api/products/search` - Search products with autocomplete
- `GET /api/products/:id` - Get product details
- `POST /api/cart/items` - Add item to cart
- `PUT /api/cart/items/:id` - Update cart item quantity
- `DELETE /api/cart/items/:id` - Remove item from cart
- `POST /api/orders` - Create order
- `POST /api/orders/create-payment` - Initialize payment
- `GET /api/orders` - Get order history

---

```javascript
// Frontend: components/ProductImage.tsx
const ProductImage<{ src; alt}> = ({ src, alt }) => {
 return (
 <img
 src={src}
 alt={alt}
 loading="lazy"
 srcSet={`${src}?w=300 300w, ${src}?w=600 600w, ${src}?w=900 900w`}
 sizes="(max-width: 600px) 300px, (max-width: 900px) 600px, 900px"
 />
 );
};

```

---

## Protocols

### REST API Protocol

- **Protocol:** REST (Representational State Transfer)

- **Data Format:** JSON (JavaScript Object Notation)

- **HTTP Methods:** GET, POST, PUT, DELETE, PATCH

- **Authentication:** JWT Bearer token in Authorization header

### Payment Gateway Protocol

- **Provider:** Payment Gateway

- **Integration:** SDK and Webhooks

- **Webhook Events:** `payment.success`, `payment.failed`, `payment.refunded`

### CDN Protocol

- **Provider:** AWS CloudFront / Cloudflare

- **Content:** Static assets (images, JavaScript, CSS)

- **Caching:** Cache-Control headers for browser caching

---

## Performance Optimizations

**Frontend Optimizations:** React.js code splitting, lazy loading, memoization

### Frontend Optimizations

- **Code Splitting:** Lazy load product pages, checkout page

- **Image Lazy Loading:** Load product images as user scrolls

- **Memoization:** Memoize expensive calculations (cart totals, filters)

- **Virtual Scrolling:** For large product lists

- **Database Indexing:** Index product fields (category, brand, price)

- **Redis Caching:** Cache popular products, search results

- **Elasticsearch:** Fast product search with filters

- **CDN:** Serve product images from CDN

---

## Security Implementation

**Frontend Security:** XSS protection, input validation, secure token storage

### Payment Security

**Backend (Express.js):**

```javascript
// Backend: Validate payment webhook
router.post('/payment-webhook', async (req, res) => {
 const signature = req.headers['x-payment-gateway-signature'];
 const isValid = paymentGateway.validateWebhookSignature(
 JSON.stringify(req.body),
 signature,
 process.env.PAYMENT_GATEWAY_WEBHOOK_SECRET
 );

 if (!isValid) {
 return res.status(400).json({ error: 'Invalid signature' });
 }

 // Process payment
 const { order_id, payment_id, status } = req.body.payload.payment.entity;

 if (status === 'captured') {
 await Order.updateOne(
 { paymentGatewayOrderId: order_id },
 { paymentStatus: 'paid', paymentId: payment_id }
 );
 }

 res.json({ success: true });
});

```

---

## Testing Strategy

### Frontend Testing (React.js)

**Unit Testing:**

- **Jest + React Testing Library** - Test components, hooks, utilities

- **Redux Testing** - Test Redux slices and actions

- **Test Coverage:** Aim for 80%+ coverage

**Integration Testing:**

- **React Testing Library** - Test component interactions

- **API Mocking** - Mock API responses with MSW (Mock Service Worker)

**E2E Testing:**

- **Cypress / Playwright** - Test complete user journeys

- **Test Scenarios:** Product search, cart, checkout, payment flow

---

## Deployment & DevOps

### Frontend Deployment

**Build & Deploy:**

- **Production Build:** Optimized bundle with code splitting

- **CDN:** Deploy static assets to CDN (CloudFront/Cloudflare)

- **CI/CD:** Automated deployment from Git (Vercel/Netlify)

**CI/CD Pipeline:**

- **Automated Testing:** Run tests before deployment

- **Database Migrations:** Run migrations automatically

- **Zero-Downtime:** Blue-green deployment strategy

### Database & Services

**MongoDB:**

- **MongoDB Atlas:** Managed MongoDB service

- **Backup Strategy:** Daily automated backups

- **Monitoring:** MongoDB Atlas monitoring

**Redis:**

- **Redis Cloud / ElastiCache:** Managed Redis service

- **High Availability:** Redis cluster setup

**Elasticsearch:**

- **Elastic Cloud:** Managed Elasticsearch service

- **Index Management:** Automated index creation and updates

---

## Environment Configuration

### Environment Variables

**Frontend:**

```env
REACT_APP_API_URL=https://api.example.com
REACT_APP_PAYMENT_KEY=pk_live_xxx
REACT_APP_ENVIRONMENT=production

```

**Backend:**

```env
NODE_ENV=production
MONGODB_URI=mongodb://...
REDIS_URL=redis://...
ELASTICSEARCH_URL=https://...
PAYMENT_GATEWAY_SECRET=xxx
AWS_ACCESS_KEY_ID=xxx

```

**Secrets Management:**

- **AWS Secrets Manager:** Store sensitive credentials

- **Environment-Specific:** Separate configs for each environment

---

## Database Migrations & Seeding

### MongoDB Migrations

**Migration Scripts:**

- **Schema Changes:** Add indexes, update schemas

- **Data Migrations:** Transform existing data

- **Version Control:** Track migration versions

### Data Seeding

**Seed Data:**

- **Products:** Seed product catalog

- **Categories:** Seed product categories

- **Test Users:** Seed test accounts for development

---

## API Documentation

### Swagger/OpenAPI

**API Documentation:**

- **Swagger UI:** Interactive API documentation

- **OpenAPI Spec:** Machine-readable API specification

- **Auto-Generated:** Generate from code annotations

---

## API Versioning

**Versioning Strategy:**

- **URL Versioning:** `/api/v1/products`, `/api/v2/products`

- **Header Versioning:** `Accept: application/vnd.api+json;version=1`

- **Backward Compatibility:** Maintain old API versions for existing clients

---

## Monitoring & Logging

### Application Monitoring

**Frontend:**

- **Error Tracking:** Sentry for frontend errors

- **Performance:** Web Vitals tracking

- **Analytics:** User behavior tracking

**Backend:**

- **APM:** New Relic / Datadog

- **Error Tracking:** Sentry for backend errors

- **Log Aggregation:** ELK Stack / CloudWatch

### Logging

**Structured Logging:**

- **Winston / Pino:** Structured logging

- **Log Levels:** Error, Warn, Info, Debug

- **JSON Format:** Easy parsing and searching

---

## Database Transactions & Consistency

### MongoDB Transactions

**ACID Transactions:**

- **Multi-Document:** For operations requiring consistency

- **Example:** Order creation + inventory update + payment processing

- **Session Management:** Use MongoDB sessions

**Example:**

```javascript
const session = await mongoose.startSession();
session.startTransaction();
try {
 await Order.create([orderData], { session });
 await Product.updateOne({ _id: productId }, { $inc: { stock: -quantity } }, { session });
 await Payment.create([paymentData], { session });
 await session.commitTransaction();
} catch (error) {
 await session.abortTransaction();
 throw error;
} finally {
 session.endSession();
}

```

---

## Third-Party Service Integration

### Payment Gateway

**Integration:**

- **SDK:** Payment gateway SDK

- **Webhooks:** Secure webhook handling

- **Idempotency:** Prevent duplicate payments

### AWS S3

**File Storage:**

- **Product Images:** Store product images

- **CDN:** CloudFront for image delivery

- **Access Control:** Private buckets with signed URLs

### Elasticsearch

**Search Integration:**

- **Indexing:** Index products for search

- **Real-time Updates:** Update index on product changes

- **Query Optimization:** Optimize search queries

---

# 4) Algorithms

## Product Search Ranking Algorithm

**Purpose:** Rank product search results by relevance, popularity, and business metrics.

**Algorithm:**

1. Calculate BM25 relevance score for text matching
2. Apply business boosts (popularity, sales, rating, recency)
3. Combine scores with weighted formula
4. Sort products by final score

**Implementation:**

```javascript
function rankProducts(products: Product[], query): Product[] {
 return products.map(product => {
 // BM25 relevance score
 const relevanceScore = calculateBM25(product, query);

 // Business boosts
 const popularityBoost = product.salesCount * 0.1;
 const ratingBoost = product.rating * 0.2;
 const recencyBoost = getRecencyBoost(product.createdAt);

 // Combined score
 const finalScore = relevanceScore * 0.6 + popularityBoost * 0.2 + ratingBoost * 0.15 + recencyBoost * 0.05;

 return { ...product, score: finalScore };
 }).sort((a, b) => b.score - a.score);
}

```

**Complexity:**

- Time: O(n * m) where n is number of products, m is query length
- Space: O(n) for scoring
- **Ranking Quality:** Combined scoring improves search relevance

---

## Shopping Cart Merge Algorithm

**Purpose:** Merge client-side and server-side cart when user logs in.

**Algorithm:**

1. Load server cart and client cart
2. Merge items by product ID
3. For duplicates, use maximum quantity
4. Validate prices and inventory
5. Save merged cart to server

**Implementation:**

```javascript
function mergeCarts(serverCart: CartItem[], clientCart: CartItem[]): CartItem[] {
 const merged = new Map<string, CartItem>();

 // Add server cart items
 for (const item of serverCart) {
 merged.set(item.productId, { ...item });
 }

 // Merge client cart items
 for (const item of clientCart) {
 const existing = merged.get(item.productId);

 if (existing) {
 // Use maximum quantity
 existing.quantity = Math.max(existing.quantity, item.quantity);
 } else {
 merged.set(item.productId, { ...item });
 }
 }

 return Array.from(merged.values());
}

```

**Complexity:**

- Time: O(n + m) where n and m are cart sizes
- Space: O(n + m)
- **Cart Consistency:** Merge algorithm ensures no items are lost

---

# 5) Data Models

## Products Collection (MongoDB)

```javascript
{
 _id: ObjectId,
 productId: String, // Unique product ID, indexed
 name: String, // Product name, indexed
 description: String, // Product description
 price: Number, // Product price, indexed
 category: String, // Product category, indexed
 brand: String, // Brand name, indexed
 images: [String], // Array of image URLs
 specifications: Object, // Product specifications
 rating: Number, // Average rating (0-5)
 reviewCount: Number, // Number of reviews
 salesCount: Number, // Number of sales
 stock: Number, // Available stock, indexed
 status: String, // active, inactive, out_of_stock
 createdAt, // Created timestamp, indexed
 updatedAt// Updated timestamp
}

// Indexes:
// - { productId: 1 } (unique)
// - { category: 1, price: 1 } (compound)
// - { brand: 1 } (indexed)
// - { status: 1, stock: 1 } (compound)
// - { name: "text", description: "text" } (text index for search)

```

## Orders Collection (MongoDB)

```javascript
{
 _id: ObjectId,
 orderId: String, // Unique order ID, indexed
 userId: ObjectId, // User reference, indexed
 items: [Object], // Array of order items
 totalAmount: Number, // Total order amount
 status: String, // pending, confirmed, shipped, delivered, cancelled
 shippingAddress: Object, // Shipping address
 paymentId: ObjectId, // Payment reference
 createdAt, // Created timestamp, indexed
 updatedAt// Updated timestamp
}

// Indexes:
// - { orderId: 1 } (unique)
// - { userId: 1, createdAt: -1 } (compound)
// - { status: 1, createdAt: -1 } (compound)

```

---

# 6) Database Transactions and Consistency

### MongoDB Transactions

**Transaction Usage:**

- **Multi-Document Transactions** - For operations requiring ACID guarantees
- **Example:** Order creation + inventory update + payment processing in single transaction
- **Session Management:** Use MongoDB sessions for transaction control

**Example:**

```javascript
const session = await mongoose.startSession();
session.startTransaction();
try {
 await Order.create([orderData], { session });
 for (const item of orderData.items) {
 await Product.updateOne(
 { productId: item.productId },
 { $inc: { stock: -item.quantity } },
 { session }
 );
 }
 await Payment.create([paymentData], { session });
 await session.commitTransaction();
} catch (error) {
 await session.abortTransaction();
 throw error;
} finally {
 session.endSession();
}

```

### Consistency Strategies

**Data Consistency:**

- **Order Consistency:** Use transactions for order operations to ensure atomicity
- **Inventory Consistency:** Ensure inventory updates are atomic with order creation
- **Payment Consistency:** Ensure payment and order updates are atomic
- **Cache Consistency:** Invalidate product cache on inventory updates

---

# 7) Protocols

### REST API Protocol

- **Protocol:** REST (Representational State Transfer)
- **Data Format:** JSON
- **HTTP Methods:** GET, POST, PUT, DELETE
- **Status Codes:** 200 (Success), 201 (Created), 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), 409 (Conflict), 500 (Server Error)
- **Authentication:** JWT Bearer token in Authorization header

---

# 8) API Design

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

# 9) Caching Strategy

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

# 10) Error Handling

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

# 11) Deployment and DevOps

### Scalability

**API Layer:**

- Deploy API layer across multiple instances behind load balancer
- Use auto-scaling based on CPU/memory metrics
- Stateless design allows horizontal scaling

**Database Scaling:**

- **Read Replicas:** Deploy read replicas for product queries
- **Sharding:** Shard products by category or productId for write scaling
- **Connection Pooling:** Use connection pooling to manage database connections

**Caching:**

- Distributed Redis cluster for high availability
- Cache product data and search results
- Reduces database load significantly

### Availability

**Replication:**

- Database replication ensures data availability
- Multi-region replication for disaster recovery

**Failover:**

- Automated failover mechanisms for API and data store layers
- Health checks and monitoring for proactive failover
- Circuit breaker pattern to prevent cascading failures

**Geo-Distributed Deployment:**

- Deploy service across multiple geographical regions
- Reduces latency for users worldwide
- Improves availability by eliminating single point of failure

### Frontend Deployment

**Build Process:**

- **Production Build:** Optimized bundle with code splitting
- **CDN Deployment:** Deploy static assets to CDN for fast global delivery
- **Environment Variables:** `.env.production` for production config

**Deployment Platforms:**

- **Vercel / Netlify** - Automatic deployments from Git
- **AWS S3 + CloudFront** - Static site hosting with CDN

### Database Deployment

**MongoDB Setup:**

- **MongoDB Atlas** - Managed MongoDB service with automatic backups
- **Backup Strategy:** Daily automated backups with point-in-time recovery
- **Indexing:** Proper indexes on productId, category, price, status
- **Replication:** Replica sets for high availability

**Redis Setup:**

- **Redis Cloud / AWS ElastiCache** - Managed Redis service
- **Cluster Mode:** Redis cluster for high availability and performance
- **Persistence:** RDB snapshots and AOF for data durability

---

# 12) Security Considerations

### Rate Limiting

- Implement rate limiting at API layer to prevent abuse
- Limit number of requests per user/IP per minute/hour
- Use Redis for distributed rate limiting across multiple servers

### Input Validation

- Validate all API inputs (product data, order data, payment data)
- Sanitize user input to prevent injection attacks
- Validate file uploads (images) for type and size

### HTTPS/TLS

- All communication between clients and API encrypted using HTTPS
- Prevents eavesdropping and man-in-the-middle attacks
- SSL/TLS certificates for secure connections

### Payment Security

- **PCI-DSS Compliance:** Use payment gateway SDKs that handle PCI-DSS compliance
- **Tokenization:** Never store full payment card details, use tokens
- **Idempotency:** Use idempotency keys to prevent duplicate charges

### Authentication and Authorization

- **JWT Tokens:** Use JWT for stateless authentication
- **Token Expiration:** Set appropriate token expiration times
- **Role-Based Access Control:** Implement RBAC for admin vs user access

### Monitoring and Alerts

- Set up monitoring for unusual activity patterns
- Trigger alerts for potential security issues
- Track metrics: order rates, payment success rates, inventory levels
- Log all operations for security auditing

---

# 3) Interview Answers

---

## Q1. 💡 Most complex technical challenge in building the e-commerce platform

**Situation:** Building a full-stack e-commerce platform that handles millions of products, thousands of concurrent users, complex search requirements, shopping cart management, payment processing, and order management while ensuring performance, scalability, and data consistency.

**Action:** The most complex challenge was implementing a scalable product search system that handles millions of products with fast search, filters, and sorting. **Backend (Node.js/Express.js):**, I integrated **Elasticsearch** for full-text product search - indexed product data (name, description, tags, specifications) with proper analyzers and mappings. I implemented **search service** that handles complex queries with filters (price, brand, rating, availability) and sorting. I used **Redis caching** for popular search queries to reduce Elasticsearch load. **Frontend (React.js):**, I implemented **search autocomplete** with debouncing that queries Elasticsearch as user types. I created **advanced filter UI** with multiple filter options that update search results in real-time. I used **React Query** for caching search results and managing search state. I implemented **infinite scroll** for search results to handle large result sets efficiently.

**Result:** Successfully delivered a fast, scalable search system. Search latency is < 100ms for most queries. System handles millions of products. Search autocomplete provides instant suggestions. Advanced filters work seamlessly. User experience is excellent.

**Takeaway:** Elasticsearch is essential for large-scale product search. Caching popular queries improves performance. Debouncing prevents excessive API calls. Infinite scroll handles large result sets. Search UX is crucial for e-commerce.

---

## Q2. ⚛️ Designing React.js frontend architecture for scalability and maintainability

**Situation:** The React.js frontend needed to handle complex state (products, cart, user, orders), support multiple pages (product listing, details, cart, checkout), and maintain performance as features grow.

**Action:** I designed a scalable React.js architecture. I used **Redux Toolkit** for global state management with separate slices for products, cart, user, orders, and UI state. I implemented **React Router v6** for client-side routing with code splitting using `React.lazy()` - each route loads only when needed, reducing initial bundle size by 40%. I created **reusable components** following composition pattern - `ProductCard`, `CartItem`, `FilterSidebar` can be combined in different ways. I used **Material-UI** for consistent UI components and theming. I implemented **React Query** for server state (product data, search results) with automatic caching and refetching. I created **custom hooks** (`useCart`, `useProduct`, `useSearch`) to encapsulate business logic. I used **memoization** (`React.memo`, `useMemo`, `useCallback`) to prevent unnecessary re-renders. I implemented **image lazy loading** and **virtual scrolling** for product lists.

**Result:** Frontend architecture is scalable and maintainable. Adding new features is easy. Code reusability is 70%. Bundle size reduced by 40%. Performance is optimal. New developers can onboard quickly.

**Takeaway:** Proper React.js architecture with code splitting, state management separation, and reusable components is crucial. Use React Query for server state, Redux for client state. Custom hooks encapsulate business logic. Memoization improves performance.

---

## Q3. 💡 Implementing shopping cart management with persistence across sessions

**Situation:** Users needed to add products to cart, update quantities, and have cart persist across browser sessions and devices, requiring both client-side and server-side cart management.

**Action:** I implemented a hybrid cart management system. **Frontend (React.js):**, I used **Redux Toolkit** for cart state management - cart items stored in Redux with product details, quantities, and prices. I implemented **localStorage persistence** - cart is saved to localStorage on every change for offline access. I created **cart synchronization** - on login, merge localStorage cart with server cart. **Backend (Node.js/Express.js):**, I created **cart API endpoints** - GET, POST (add), PUT (update), DELETE (remove) cart items. I stored **cart in MongoDB** for authenticated users with userId. I implemented **cart expiration** - carts expire after 30 days of inactivity. I added **price validation** - when cart is loaded, validate prices haven't changed, show warnings if prices increased. I implemented **inventory checking** - verify products are in stock before allowing checkout.

**Result:** Cart management works seamlessly. Cart persists across sessions and devices. 100% cart data saved. Price validation prevents checkout issues. Inventory checking prevents overselling. User experience is excellent.

**Takeaway:** Hybrid cart management (client + server) provides best UX. Persist cart in localStorage for offline access. Sync cart on login. Validate prices and inventory before checkout. Cart expiration prevents stale data.

---

## Q4. 🔎 Implementing product search with Elasticsearch in Node.js

**Situation:** The system needed fast, accurate product search across millions of products with support for filters, sorting, and autocomplete.

**Action:** I implemented Elasticsearch integration for product search. **Backend (Node.js/Express.js):**, I set up **Elasticsearch cluster** and created product index with proper mappings (text fields for search, numeric fields for filters). I implemented **indexing pipeline** - when products are created/updated, they're indexed in Elasticsearch. I created **search service** that builds Elasticsearch queries with:

- **Multi-match query** for text search across name, description, tags

- **Bool query** with filters for price range, brand, rating, availability

- **Sort** by relevance, price, rating, newest

- **Pagination** using from/size or search_after for deep pagination

I implemented **search autocomplete** using Elasticsearch completion suggester. I added **Redis caching** for popular search queries (5-minute TTL). I implemented **search analytics** to track popular searches and optimize index. I added **fuzzy matching** for typo tolerance.

**Result:** Product search is fast and accurate. Search latency is < 100ms. System handles millions of products. Autocomplete provides instant suggestions. Filters and sorting work seamlessly. User experience is excellent.

**Takeaway:** Elasticsearch is essential for large-scale product search. Proper index mapping is crucial. Caching popular queries improves performance. Autocomplete enhances UX. Search analytics help optimization.

---

## Q5. 💡 Handling payment gateway integration

**Situation:** The system needed secure payment processing for multiple payment methods (cards, UPI, net banking, wallets) with proper error handling, webhook processing, and order management.

**Action:** I implemented secure payment gateway integration. **Frontend (React.js):**, I integrated **payment gateway SDK** for payment UI - think of it like a cashier that processes transactions securely. I created **payment flow** - user selects payment method, enters details, SDK handles secure payment processing. **Backend (Node.js/Express.js):**, I created **payment service** that:

- Creates payment order with payment gateway

- Stores payment intent in database

- Handles payment webhooks for status updates

- Verifies webhook signatures for security

- Updates order status based on payment status

I implemented **idempotency** using unique order IDs to prevent duplicate processing. I created **payment state machine** (pending → processing → success/failed) with proper transitions. I added **retry mechanism** for failed payments. I implemented **refund handling** for cancellations and returns. I stored **payment data securely** - never storing card details, only transaction IDs.

**Result:** Payment integration is secure and reliable. 98%+ payment success rate. Webhook processing ensures real-time status updates. Zero security incidents. Refund processing works seamlessly.

**Takeaway:** Payment integration requires careful error handling and webhook management. Always verify webhook signatures. Implement idempotency. Never store sensitive payment data. Proper state management is essential.
