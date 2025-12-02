# E-commerce App (Amazon, Flipkart) - High Level Design (HLD)

> **Project Type:** Full-Stack Web Application (MERN Stack)  
> **Frontend:** React.js Web Application  
> **Backend:** Node.js, Express.js, MongoDB, REST APIs  
> **Tech Stack:** 
> - **Frontend:** React.js, TypeScript, React Router, Redux Toolkit, Axios, Material-UI
> - **Backend:** Node.js, Express.js, MongoDB, Redis, Elasticsearch, JWT
> - **Services:** Razorpay/Stripe Payment Gateway, AWS S3 (for product images), CDN
> **Team Size:** 3-5 person team  
> **Built:** From scratch

---

## 1. Requirements

### a) Functional Requirements

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

### b) Non-Functional Requirements

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

## 2. Scope & Priority

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

## 3. Tech Choices

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
- **Razorpay / Stripe:** Payment gateway for processing payments
  - **Multiple methods** - Cards, UPI, net banking, wallets
  - **Secure** - PCI-DSS compliant
  - **Easy integration** - Simple API, good documentation

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│              Frontend (React.js) - Client Side           │
│  (This is what users see in their browser)              │
├─────────────────────────────────────────────────────────┤
│  ┌──────────────────────────────────────────────────┐   │
│  │         Browser (Chrome, Firefox, Safari)        │   │
│  │  ┌────────────────────────────────────────────┐  │   │
│  │  │     React.js Application (SPA)             │  │   │
│  │  │  ┌──────────────────────────────────────┐  │  │   │
│  │  │  │  React Router (Client-side Routing)  │  │  │   │
│  │  │  └──────────────────────────────────────┘  │  │   │
│  │  │  ┌──────────────────────────────────────┐  │  │   │
│  │  │  │  Redux Toolkit (State Management)    │  │  │   │
│  │  │  │  - Cart, User, Products, Orders      │  │  │   │
│  │  │  └──────────────────────────────────────┘  │  │   │
│  │  │  ┌──────────────────────────────────────┐  │  │   │
│  │  │  │  Material-UI Components              │  │  │   │
│  │  │  └──────────────────────────────────────┘  │  │   │
│  │  └────────────────────────────────────────────┘  │   │
│  └──────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
                        │
                        │ HTTP/REST API Calls
                        ▼
┌─────────────────────────────────────────────────────────┐
│              Backend (Node.js + Express.js)              │
│  (Server that handles business logic and data)          │
├─────────────────────────────────────────────────────────┤
│  ┌──────────────────────────────────────────────────┐   │
│  │         Load Balancer / API Gateway              │   │
│  └──────────────────────────────────────────────────┘   │
│                        │                                 │
│        ┌───────────────┼───────────────┐                │
│        ▼               ▼               ▼                │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐             │
│  │ Express  │  │ Express  │  │ Express  │             │
│  │ Server 1 │  │ Server 2 │  │ Server 3 │             │
│  └──────────┘  └──────────┘  └──────────┘             │
│        │               │               │                │
│        └───────────────┼───────────────┘                │
│                        ▼                                 │
│  ┌──────────────────────────────────────────────────┐   │
│  │         Business Logic Layer                     │   │
│  │  - Product Service (catalog, search)             │   │
│  │  - Cart Service (cart management)                │   │
│  │  - Order Service (order processing)              │   │
│  │  - User Service (authentication, profiles)       │   │
│  │  - Review Service (reviews, ratings)             │   │
│  └──────────────────────────────────────────────────┘   │
│                        ▼                                 │
│  ┌──────────────────────────────────────────────────┐   │
│  │         Data Access Layer                        │   │
│  │  - MongoDB (Products, users, orders)             │   │
│  │  - Elasticsearch (Product search)                │   │
│  │  - Redis (Caching, sessions)                     │   │
│  └──────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
        │                    │                    │
        ▼                    ▼                    ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│   MongoDB    │  │ Elasticsearch│  │    Redis     │
│  (Database)  │  │   (Search)   │  │   (Cache)    │
│              │  │              │  │              │
│  - Products  │  │  - Product   │  │  - Product   │
│  - Users     │  │    Index     │  │    Cache     │
│  - Orders    │  │  - Search    │  │  - Sessions  │
│  - Reviews   │  │    Results   │  │              │
└──────────────┘  └──────────────┘  └──────────────┘
        │                    │                    │
        └────────────────────┼────────────────────┘
                             │
                             ▼
                    ┌──────────────┐
                    │   External   │
                    │   Services   │
                    │              │
                    │  - Razorpay  │
                    │  - AWS S3    │
                    │  - CDN       │
                    └──────────────┘
```

**How it works:**
1. **Frontend (React.js):** User browses products, adds to cart, checks out
2. **API Calls:** React app makes HTTP requests to backend API (using Axios)
3. **Backend (Node.js):** Express server receives request, processes business logic
4. **Search:** Product search queries go to Elasticsearch for fast search
5. **Database:** Backend reads/writes data from MongoDB, caches in Redis
6. **Payment:** Backend integrates with payment gateway for processing payments
7. **Images:** Product images served from AWS S3 via CDN for fast loading
8. **Response:** Backend sends response back to frontend, React updates UI

---

## Key Design Decisions

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

