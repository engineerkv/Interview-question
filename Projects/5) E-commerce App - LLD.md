# E-commerce App (Amazon, Flipkart) - Low Level Design (LLD)

> **Project Type:** Full-Stack Web Application (MERN Stack)  
> **Tech Stack:** 
> - **Frontend:** React.js, TypeScript, React Router, Redux Toolkit, Axios, Material-UI
> - **Backend:** Node.js, Express.js, MongoDB, Redis, Elasticsearch, JWT
> - **Services:** Razorpay/Stripe Payment Gateway, AWS S3, CDN

---

## 3. Component Architecture

**Think of this as the building blocks - how components are organized and connected**

### Component Hierarchy (React.js)

```
App (Root Component - Entry Point)
├── Layout (Main Layout with Navigation)
│   ├── Header
│   │   ├── Logo
│   │   ├── SearchBar (with autocomplete)
│   │   ├── NavigationMenu
│   │   └── UserMenu (Cart icon, User account)
│   ├── Sidebar (Mobile Menu)
│   │   ├── CategoryMenu
│   │   └── UserMenu
│   └── Main Content Area
│       ├── HomePage
│       │   ├── HeroBanner
│       │   ├── CategoryGrid
│       │   ├── FeaturedProducts
│       │   └── DealsSection
│       ├── ProductListPage
│       │   ├── FilterSidebar
│       │   │   ├── PriceFilter
│       │   │   ├── BrandFilter
│       │   │   ├── RatingFilter
│       │   │   └── AvailabilityFilter
│       │   ├── ProductGrid
│       │   │   └── ProductCard
│       │   │       ├── ProductImage
│       │   │       ├── ProductTitle
│       │   │       ├── ProductPrice
│       │   │       ├── ProductRating
│       │   │       └── AddToCartButton
│       │   └── Pagination
│       ├── ProductDetailPage
│       │   ├── ProductImageGallery
│       │   ├── ProductInfo
│       │   │   ├── ProductTitle
│       │   │   ├── ProductPrice
│       │   │   ├── ProductRating
│       │   │   ├── ProductDescription
│       │   │   ├── AddToCartButton
│       │   │   └── BuyNowButton
│       │   ├── ProductSpecifications
│       │   ├── ProductReviews
│       │   │   ├── ReviewSummary
│       │   │   └── ReviewList
│       │   │       └── ReviewCard
│       │   └── RelatedProducts
│       ├── CartPage
│       │   ├── CartItemList
│       │   │   └── CartItem
│       │   │       ├── ProductImage
│       │   │       ├── ProductInfo
│       │   │       ├── QuantitySelector
│       │   │       ├── Price
│       │   │       └── RemoveButton
│       │   ├── CartSummary
│       │   │   ├── Subtotal
│       │   │   ├── Shipping
│       │   │   ├── Discount
│       │   │   ├── Total
│       │   │   └── CheckoutButton
│       │   └── EmptyCartState
│       ├── CheckoutPage
│       │   ├── AddressForm
│       │   ├── PaymentMethodSelection
│       │   ├── OrderSummary
│       │   └── PlaceOrderButton
│       ├── OrderHistoryPage
│       │   ├── OrderList
│       │   │   └── OrderCard
│       │   │       ├── OrderInfo
│       │   │       ├── OrderItems
│       │   │       ├── OrderStatus
│       │   │       └── TrackOrderButton
│       │   └── EmptyState
│       └── WishlistPage
│           ├── WishlistItems
│           │   └── WishlistItem
│           │       ├── ProductCard
│           │       └── RemoveButton
│           └── EmptyState
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

## 4. Data Models

### Product Model
```typescript
interface Product {
  id: string;
  name: string;
  description: string;
  price: number;
  originalPrice?: number;  // For discounts
  images: string[];        // Array of image URLs
  category: string;
  brand: string;
  rating: number;          // Average rating (1-5)
  reviewCount: number;
  stock: number;           // Available quantity
  specifications: Record<string, string>;  // Key-value pairs
  tags: string[];
  createdAt: Date;
  updatedAt: Date;
}
```

### Cart Item Model
```typescript
interface CartItem {
  productId: string;
  product: Product;        // Populated product data
  quantity: number;
  price: number;           // Price at time of adding to cart
}
```

### Order Model
```typescript
interface Order {
  id: string;
  userId: string;
  items: OrderItem[];
  shippingAddress: Address;
  billingAddress: Address;
  paymentMethod: string;
  paymentStatus: 'pending' | 'paid' | 'failed' | 'refunded';
  orderStatus: 'pending' | 'confirmed' | 'shipped' | 'delivered' | 'cancelled';
  subtotal: number;
  shipping: number;
  discount: number;
  total: number;
  orderDate: Date;
  estimatedDelivery?: Date;
  trackingNumber?: string;
}
```

### Review Model
```typescript
interface Review {
  id: string;
  productId: string;
  userId: string;
  userName: string;
  rating: number;          // 1-5 stars
  title: string;
  comment: string;
  verifiedPurchase: boolean;
  helpfulCount: number;
  createdAt: Date;
}
```

### User Model
```typescript
interface User {
  id: string;
  email: string;
  name: string;
  phone?: string;
  addresses: Address[];
  paymentMethods: PaymentMethod[];
  wishlist: string[];      // Array of product IDs
  createdAt: Date;
}
```

---

## 5. Data APIs

**Note:** All API endpoints are implemented on the **backend (Node.js/Express)**, and the **frontend (React.js)** calls these APIs using Axios.

### Product APIs

**Backend Implementation:** Express.js routes handle product logic  
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

## 6. Backend Implementation Details

### Express.js Server Structure

**Backend Architecture:**
```
Backend Server (Node.js + Express.js)
├── Routes (API Endpoints)
│   ├── /api/products/* - Product routes
│   ├── /api/cart/* - Cart routes
│   ├── /api/orders/* - Order routes
│   ├── /api/reviews/* - Review routes
│   ├── /api/auth/* - Authentication routes
│   └── /api/users/* - User routes
├── Middleware
│   ├── Authentication (JWT verification)
│   ├── Validation (Request validation)
│   ├── Rate Limiting
│   └── Error Handling
├── Controllers (Business Logic)
│   ├── ProductController
│   ├── CartController
│   ├── OrderController
│   ├── ReviewController
│   └── UserController
├── Services (Data Access)
│   ├── ProductService
│   ├── CartService
│   ├── OrderService
│   ├── SearchService (Elasticsearch)
│   └── PaymentService
└── Models (Database Schemas)
    ├── Product Model
    ├── Order Model
    ├── User Model
    └── Review Model
```

### Backend Product Service Example

**Backend (Express.js):**
```typescript
// Backend: services/productService.ts
export class ProductService {
  async getProducts(filters: ProductFilters): Promise<Product[]> {
    // If search query, use Elasticsearch
    if (filters.search) {
      return await this.searchProducts(filters.search, filters);
    }
    
    // Otherwise, query MongoDB
    const query = this.buildMongoQuery(filters);
    const products = await Product.find(query)
      .skip((filters.page - 1) * filters.limit)
      .limit(filters.limit)
      .sort(this.buildSort(filters));
    
    return products;
  }
  
  async searchProducts(query: string, filters: ProductFilters): Promise<Product[]> {
    // Search in Elasticsearch
    const result = await elasticsearchClient.search({
      index: 'products',
      body: {
        query: {
          bool: {
            must: [
              { match: { name: query } },
              { range: { price: { gte: filters.minPrice, lte: filters.maxPrice } } }
            ]
          }
        }
      }
    });
    
    return result.hits.hits.map(hit => hit._source);
  }
}
```

### Backend Cart Service Example

**Backend (Express.js):**
```typescript
// Backend: services/cartService.ts
export class CartService {
  async addToCart(userId: string, productId: string, quantity: number): Promise<Cart> {
    // Get product
    const product = await Product.findById(productId);
    if (!product || product.stock < quantity) {
      throw new Error('Product not available');
    }
    
    // Get or create cart
    let cart = await Cart.findOne({ userId });
    if (!cart) {
      cart = await Cart.create({ userId, items: [] });
    }
    
    // Check if product already in cart
    const existingItem = cart.items.find(item => item.productId === productId);
    if (existingItem) {
      existingItem.quantity += quantity;
    } else {
      cart.items.push({
        productId,
        quantity,
        price: product.price
      });
    }
    
    await cart.save();
    return cart;
  }
}
```

---

## 7. Implementation Details

**Note:** Implementation details are split between frontend (React.js) and backend (Node.js/Express.js). Each section indicates where the code runs.

### Product Search with Autocomplete

**Frontend Implementation:** React component handles search input and displays suggestions  
**Backend Implementation:** Express.js API provides search results from Elasticsearch

**Backend (Express.js):**
```typescript
// Backend: routes/products.ts
router.get('/search', async (req, res) => {
  const { q, limit = 10 } = req.query;
  
  // Search in Elasticsearch
  const result = await elasticsearchClient.search({
    index: 'products',
    body: {
      query: {
        multi_match: {
          query: q,
          fields: ['name^2', 'description', 'tags']
        }
      },
      size: limit
    }
  });
  
  const products = result.hits.hits.map(hit => hit._source);
  const suggestions = await getSearchSuggestions(q);
  
  res.json({
    success: true,
    data: { products, suggestions }
  });
});
```

**Frontend Implementation:**
```typescript
// Frontend: components/SearchBar.tsx
const SearchBar: React.FC = () => {
  const [query, setQuery] = useState('');
  const [suggestions, setSuggestions] = useState<string[]>([]);
  
  const debouncedSearch = useMemo(
    () => debounce(async (q: string) => {
      if (q.length > 2) {
        const response = await axios.get(`/api/products/search?q=${q}`);
        setSuggestions(response.data.data.suggestions);
      }
    }, 300),
    []
  );
  
  useEffect(() => {
    debouncedSearch(query);
  }, [query, debouncedSearch]);
  
  return (
    <Autocomplete
      options={suggestions}
      onInputChange={(e, value) => setQuery(value)}
      renderInput={(params) => <TextField {...params} placeholder="Search products" />}
    />
  );
};
```

### Shopping Cart Management

**Frontend Implementation:** Redux manages cart state, React components display cart  
**Backend Implementation:** Express.js API handles cart persistence

**Frontend (Redux):**
```typescript
// Frontend: Redux slice for cart
const cartSlice = createSlice({
  name: 'cart',
  initialState: { items: [], loading: false },
  reducers: {
    addToCart: (state, action) => {
      const { product, quantity } = action.payload;
      const existingItem = state.items.find(item => item.productId === product.id);
      
      if (existingItem) {
        existingItem.quantity += quantity;
      } else {
        state.items.push({ productId: product.id, product, quantity, price: product.price });
      }
    },
    removeFromCart: (state, action) => {
      state.items = state.items.filter(item => item.productId !== action.payload);
    }
  }
});
```

### Payment Gateway Integration

**Frontend Implementation:** React component initiates payment  
**Backend Implementation:** Express.js handles payment gateway integration

**Backend (Express.js):**
```typescript
// Backend: routes/orders.ts
router.post('/create-payment', authenticate, async (req, res) => {
  const { orderId } = req.body;
  const order = await Order.findById(orderId);
  
  // Create payment order with Razorpay
  const razorpayOrder = await razorpay.orders.create({
    amount: order.total * 100, // Convert to paise
    currency: 'INR',
    receipt: orderId
  });
  
  res.json({
    success: true,
    data: {
      orderId: razorpayOrder.id,
      amount: razorpayOrder.amount,
      key: process.env.RAZORPAY_KEY_ID
    }
  });
});
```

### Image Optimization and CDN

**Frontend Implementation:** React components lazy load images  
**Backend Implementation:** Express.js serves image URLs from S3/CDN

**Frontend:**
```typescript
// Frontend: components/ProductImage.tsx
const ProductImage: React.FC<{ src: string; alt: string }> = ({ src, alt }) => {
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

## 8. Performance Optimizations

**Frontend Optimizations:** React.js code splitting, lazy loading, memoization  
**Backend Optimizations:** Database indexing, Redis caching, Elasticsearch for search

### Frontend Optimizations

- **Code Splitting:** Lazy load product pages, checkout page
- **Image Lazy Loading:** Load product images as user scrolls
- **Memoization:** Memoize expensive calculations (cart totals, filters)
- **Virtual Scrolling:** For large product lists

### Backend Optimizations

- **Database Indexing:** Index product fields (category, brand, price)
- **Redis Caching:** Cache popular products, search results
- **Elasticsearch:** Fast product search with filters
- **CDN:** Serve product images from CDN

---

## 9. Security Implementation

**Frontend Security:** XSS protection, input validation, secure token storage  
**Backend Security:** Authentication, authorization, data validation, encryption

### Payment Security

**Backend (Express.js):**
```typescript
// Backend: Validate payment webhook
router.post('/payment-webhook', async (req, res) => {
  const signature = req.headers['x-razorpay-signature'];
  const isValid = razorpay.validateWebhookSignature(
    JSON.stringify(req.body),
    signature,
    process.env.RAZORPAY_WEBHOOK_SECRET
  );
  
  if (!isValid) {
    return res.status(400).json({ error: 'Invalid signature' });
  }
  
  // Process payment
  const { order_id, payment_id, status } = req.body.payload.payment.entity;
  
  if (status === 'captured') {
    await Order.updateOne(
      { razorpayOrderId: order_id },
      { paymentStatus: 'paid', paymentId: payment_id }
    );
  }
  
  res.json({ success: true });
});
```

