# E-commerce App

---

## 📍 Navigation

<div align="center">

[Home: README](README.md) • [← Previous: Social Media Feed](07%29%20Social%20Media%20Feed.md) • [Next: Chat Messaging System →](09%29%20Chat%20Messaging%20System.md)

[📋 Cheatsheet](Projects%20Interview%20Cheatsheet.md)

</div>

---

## Overview

Design a full-featured e-commerce platform where users can browse products, manage shopping carts, process secure payments, and track orders. The system handles inventory management, product recommendations, and order processing.

---

## 1) Requirements

### Functional Requirements

**Core Features:**
- Product browsing and search with filters (category, price, brand, rating)
- Product details with images, reviews, specifications
- Shopping cart management (add, update, remove items)
- Secure checkout with address and payment selection
- Order management (track orders, cancellation, returns)
- User accounts with order history
- Product reviews and ratings
- Wishlist functionality
- Product recommendations ("Customers who bought this also bought")

**Advanced Features:**
- Real-time inventory tracking
- Multiple payment methods (cards, UPI, wallets, COD)
- Coupon codes and discounts
- Order tracking with status updates
- Return and refund processing
- Product comparison
- Recently viewed products

### Non-Functional Requirements

**Performance:**
- Fast page loads: < 2 seconds
- Optimized product images (lazy loading, WebP format)
- Efficient search and filtering
- Smooth infinite scroll

**Scalability:**
- Handle traffic spikes (Black Friday, sales events)
- Support millions of products
- Thousands of concurrent users
- CDN for global asset delivery

**User Experience:**
- Responsive design (mobile-first)
- Smooth navigation and page transitions
- Search suggestions (autocomplete)
- Quick view product details

**Security:**
- PCI-DSS compliant payment processing
- Secure authentication
- XSS and CSRF protection
- Data encryption

---

## 2) Component Hierarchy

The frontend is a React e-commerce application. Here's the structure:

```
App
├── Layout
│   ├── Header
│   │   ├── Logo
│   │   ├── SearchBar (global product search)
│   │   ├── ShoppingCartIcon (with item count)
│   │   └── UserMenu
│   └── MainContent
├── Pages
│   ├── HomePage
│   │   ├── HeroBanner
│   │   ├── CategoryList
│   │   └── FeaturedProducts
│   ├── ProductListPage
│   │   ├── FilterSidebar
│   │   │   ├── CategoryFilter
│   │   │   ├── PriceFilter (range slider)
│   │   │   ├── BrandFilter (multi-select)
│   │   │   └── RatingFilter (star rating)
│   │   ├── ProductGrid
│   │   │   └── ProductCard
│   │   │       ├── ProductImage (lazy loaded)
│   │   │       ├── ProductName
│   │   │       ├── ProductPrice
│   │   │       ├── ProductRating
│   │   │       ├── StockIndicator
│   │   │       └── AddToCartButton
│   │   └── Pagination (or InfiniteScroll)
│   ├── ProductDetailPage
│   │   ├── ProductImages (image gallery with zoom)
│   │   ├── ProductInfo
│   │   │   ├── ProductTitle
│   │   │   ├── ProductPrice
│   │   │   ├── ProductRating
│   │   │   ├── StockIndicator
│   │   │   ├── QuantitySelector
│   │   │   ├── AddToCartButton
│   │   │   └── BuyNowButton
│   │   ├── ProductDescription
│   │   ├── ProductSpecifications
│   │   └── ProductReviews
│   │       ├── ReviewList
│   │       │   └── ReviewItem (rating, comment, helpful votes)
│   │       └── ReviewForm (write review)
│   ├── ShoppingCartPage
│   │   ├── CartItemList
│   │   │   └── CartItem
│   │   │       ├── ProductImage
│   │   │       ├── ProductName
│   │   │       ├── QuantitySelector
│   │   │       ├── Price
│   │   │       └── RemoveButton
│   │   └── CartSummary
│   │       ├── Subtotal
│   │       ├── Shipping
│   │       ├── Discount (coupon code)
│   │       └── Total
│   ├── CheckoutPage
│   │   ├── AddressForm (select or add address)
│   │   ├── PaymentMethodSelector
│   │   ├── OrderSummary
│   │   └── PlaceOrderButton
│   └── OrderHistoryPage
│       ├── OrderList
│       │   └── OrderCard
│       │       ├── OrderId
│       │       ├── OrderDate
│       │       ├── OrderStatus
│       │       ├── OrderItems
│       │       └── OrderActions (Track, Cancel, Return)
│       └── OrderFilters
└── SharedComponents
    ├── Button
    ├── Input
    ├── Card
    ├── Toast
    └── LoadingSpinner
```

### Key Components Explained

**1. ProductCard Component**
- Displays product in grid/list view
- Shows image, name, price, rating
- Add to cart button with optimistic updates
- Stock indicator (in stock, low stock, out of stock)
- Links to product detail page

**2. ProductDetailPage Component**
- Full product information
- Image gallery with zoom
- Quantity selector (validates against stock)
- Add to cart and buy now buttons
- Reviews and ratings section

**3. ShoppingCart Component**
- Displays cart items with quantities
- Update quantity or remove items
- Cart summary with totals
- Proceed to checkout button
- Optimistic updates for instant feedback

**4. CheckoutForm Component**
- Address selection/creation
- Payment method selection
- Order summary review
- Place order with validation
- Order confirmation

**5. FilterSidebar Component**
- Multiple filter types (category, price, brand, rating)
- Updates URL query parameters
- Triggers product refetch
- Clear filters functionality

---

## 3) Data Models

Here are the key data structures:

```typescript
// Product
interface Product {
  id: string;
  name: string;
  description: string;
  price: number;
  originalPrice?: number;  // For discounts
  images: string[];
  category: string;
  brand: string;
  rating: number;  // Average rating
  reviewCount: number;
  inStock: boolean;
  stockCount: number;
  sku: string;
  specifications: Record<string, string>;  // Key-value pairs
  createdAt: string;
}

// Cart item
interface CartItem {
  id: string;
  productId: string;
  product: Product;
  quantity: number;
  price: number;  // Price at time of adding
  addedAt: string;
}

// Shopping cart
interface ShoppingCart {
  id: string;
  userId: string;
  items: CartItem[];
  subtotal: number;
  shipping: number;
  discount: number;
  total: number;
  couponCode?: string;
}

// Order
interface Order {
  id: string;
  userId: string;
  items: OrderItem[];
  shippingAddress: Address;
  paymentMethod: PaymentMethod;
  status: "pending" | "confirmed" | "shipped" | "delivered" | "cancelled" | "returned";
  subtotal: number;
  shipping: number;
  discount: number;
  total: number;
  createdAt: string;
  updatedAt: string;
  trackingNumber?: string;
}

// Order item
interface OrderItem {
  id: string;
  productId: string;
  product: Product;
  quantity: number;
  price: number;  // Price at time of order
}

// Address
interface Address {
  id: string;
  userId: string;
  name: string;
  phone: string;
  addressLine1: string;
  addressLine2?: string;
  city: string;
  state: string;
  zipCode: string;
  country: string;
  isDefault: boolean;
}

// Product review
interface Review {
  id: string;
  productId: string;
  userId: string;
  userName: string;
  rating: number;  // 1-5
  comment: string;
  helpfulCount: number;
  createdAt: string;
  isVerifiedPurchase: boolean;
}
```

### Data Flow Explanation

**When a user adds to cart:**
1. User clicks "Add to Cart" on ProductCard
2. Frontend validates inventory (checks stockCount)
3. Optimistic update: item appears in cart immediately
4. API call: POST /api/v1/cart with productId and quantity
5. Server validates inventory again
6. On success, cart updates; on failure, rollback optimistic update

**When a user checks out:**
1. User reviews cart and clicks "Checkout"
2. User selects/enters shipping address
3. User selects payment method
4. User reviews order summary
5. User places order
6. Server reserves inventory atomically (prevents overselling)
7. Order is created with "pending" status
8. Payment is processed
9. Order status updates to "confirmed"
10. User receives order confirmation

**Inventory management:**
1. Product pages show real-time stock status
2. Add to cart validates inventory
3. Checkout validates inventory again
4. Order placement reserves inventory atomically
5. Inventory decrements on order confirmation
6. Real-time updates via polling or WebSocket

---

## 4) API Design

### REST Endpoints

**GET /api/v1/products**
- Get products with filters
- Query params: `category`, `brand`, `minPrice`, `maxPrice`, `rating`, `page`, `limit`, `sortBy`
- Returns: Paginated list of Product objects

**GET /api/v1/products/:id**
- Get product details
- Returns: Product object with full details

**GET /api/v1/products/:id/reviews**
- Get product reviews
- Query params: `page`, `limit`, `rating`
- Returns: Paginated list of Review objects

**POST /api/v1/products/:id/reviews**
- Add a product review
- Request body: `{ rating: number, comment: string }`
- Returns: Review object

**GET /api/v1/cart**
- Get user's shopping cart
- Returns: ShoppingCart object

**POST /api/v1/cart/items**
- Add item to cart
- Request body: `{ productId: string, quantity: number }`
- Returns: Updated ShoppingCart

**PATCH /api/v1/cart/items/:id**
- Update cart item quantity
- Request body: `{ quantity: number }`
- Returns: Updated ShoppingCart

**DELETE /api/v1/cart/items/:id**
- Remove item from cart
- Returns: Updated ShoppingCart

**POST /api/v1/orders**
- Create an order
- Request body: `{ addressId: string, paymentMethodId: string, couponCode?: string }`
- Returns: Order object

**GET /api/v1/orders**
- Get user's orders
- Query params: `page`, `limit`, `status`
- Returns: Paginated list of Order objects

**GET /api/v1/orders/:id**
- Get order details
- Returns: Order object

**PATCH /api/v1/orders/:id/cancel**
- Cancel an order
- Returns: Updated Order object

### API Request/Response Examples

**Get Products:**
```json
// GET /api/v1/products?category=electronics&minPrice=100&maxPrice=1000&page=1&limit=20
// Response
{
  "success": true,
  "data": {
    "products": [
      {
        "id": "prod_123",
        "name": "Wireless Headphones",
        "price": 99.99,
        "images": ["https://cdn.example.com/headphones.jpg"],
        "category": "electronics",
        "brand": "TechBrand",
        "rating": 4.5,
        "reviewCount": 1250,
        "inStock": true,
        "stockCount": 50
      }
    ],
    "total": 150,
    "page": 1,
    "limit": 20
  }
}
```

**Add to Cart:**
```json
// POST /api/v1/cart/items
{
  "productId": "prod_123",
  "quantity": 2
}

// Response
{
  "success": true,
  "data": {
    "id": "cart_123",
    "items": [
      {
        "id": "item_123",
        "productId": "prod_123",
        "product": { ... },
        "quantity": 2,
        "price": 99.99
      }
    ],
    "subtotal": 199.98,
    "shipping": 10.00,
    "total": 209.98
  }
}
```

**Create Order:**
```json
// POST /api/v1/orders
{
  "addressId": "addr_123",
  "paymentMethodId": "pm_123",
  "couponCode": "SAVE10"
}

// Response
{
  "success": true,
  "data": {
    "id": "order_123",
    "status": "confirmed",
    "items": [ ... ],
    "total": 189.98,
    "createdAt": "2024-01-15T10:00:00Z"
  }
}
```

---

## Key Design Decisions

**1. Optimistic Updates for Cart**
- Show items in cart immediately (useOptimistic)
- Better perceived performance
- Rollback if API call fails
- Instant user feedback

**2. Inventory Validation at Multiple Points**
- Validate before adding to cart
- Validate again at checkout
- Reserve inventory atomically on order placement
- Prevents overselling

**3. Real-time Inventory Updates**
- Poll inventory status for active product pages
- Or use WebSocket for real-time updates
- Show stock status accurately
- Disable add to cart when out of stock

**4. URL State for Filters**
- Store filters in URL query parameters
- Enables shareable filtered product URLs
- Browser back/forward works correctly
- Deep linking support

**5. Image Optimization**
- Lazy load product images
- Use WebP format for better compression
- CDN delivery for fast global access
- Responsive images (different sizes for different devices)

**6. Search with Autocomplete**
- Debounce search input
- Show suggestions as user types
- Fast search results
- Keyboard navigation support

---

## Interview Talking Points

**When explaining this system, I'd focus on:**

1. **Requirements First**: Start with core functionality - browse products, shopping cart, checkout, orders

2. **Component Structure**: Explain the React component hierarchy - product list, product detail, cart, checkout

3. **Data Models**: Walk through Product, CartItem, Order, Address - and how they relate

4. **API Design**: Show the REST endpoints - products, cart, orders, reviews

5. **Key Challenges**: 
   - Inventory management and preventing overselling
   - Optimistic updates for better UX
   - Real-time inventory tracking
   - Handling traffic spikes during sales
   - Secure payment processing

**Example explanation flow:**
> "So for an e-commerce app, the core requirement is allowing users to browse products, add them to a cart, and complete purchases. The frontend is a React app with a product list page showing products in a grid with filters. Users can view product details, add items to cart with optimistic updates for instant feedback, and proceed to checkout. The data model centers around Product objects with inventory tracking, CartItem objects for the shopping cart, and Order objects for completed purchases. Inventory is validated at multiple points - before adding to cart, at checkout, and atomically reserved when placing an order to prevent overselling. The main API endpoints handle product browsing with filters, cart management, order creation, and order tracking. Key challenges include managing inventory accurately to prevent overselling, providing real-time stock updates, handling traffic spikes during sales events, and ensuring secure payment processing."

---

## 📍 Navigation

<div align="center">

[Home: README](README.md) • [← Previous: Social Media Feed](07%29%20Social%20Media%20Feed.md) • [Next: Chat Messaging System →](09%29%20Chat%20Messaging%20System.md)

[📋 Cheatsheet](Projects%20Interview%20Cheatsheet.md)

</div>

---
