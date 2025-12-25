# Food Delivery System

## Overview

Design a food delivery platform where users can browse restaurants and menus, place orders, track deliveries in real-time, and process payments. The system handles order management, delivery partner matching, and real-time tracking.

---

## 1) Requirements

### Functional Requirements

**Core Features:**
- Browse restaurants and menus
- Place orders with customization
- Real-time order tracking
- Delivery partner assignment
- Payment processing
- Order history
- Restaurant ratings and reviews
- Order scheduling (book in advance)

**Advanced Features:**
- Multiple payment methods
- Order recommendations
- Loyalty programs
- Group ordering
- Order cancellation and refunds

### Non-Functional Requirements

**Performance:**
- Order placement: < 3 seconds
- Real-time location tracking
- Fast restaurant and menu browsing

**Scalability:**
- Handle 50M+ users
- 10M+ orders per day
- Thousands of restaurants
- Millions of concurrent users during peak hours

**Reliability:**
- 99.9% uptime
- Accurate order processing
- Real-time tracking accuracy

---

## 2) Component Hierarchy

The frontend is a React application with map integration. Here's the structure:

```
App
├── Layout
│   ├── Header
│   │   ├── Logo
│   │   ├── LocationSelector
│   │   └── UserMenu
│   └── MainContent
├── Pages
│   ├── HomePage
│   │   ├── RestaurantList
│   │   │   └── RestaurantCard
│   │   └── CategoryFilters
│   ├── RestaurantPage
│   │   ├── RestaurantInfo
│   │   ├── MenuList
│   │   │   └── MenuItem
│   │   │       ├── ItemImage
│   │   │       ├── ItemName
│   │   │       ├── ItemPrice
│   │   │       ├── CustomizationOptions
│   │   │       └── AddToCartButton
│   │   └── CartSummary
│   ├── CheckoutPage
│   │   ├── OrderSummary
│   │   ├── DeliveryAddress
│   │   ├── PaymentMethod
│   │   └── PlaceOrderButton
│   ├── OrderTrackingPage
│   │   ├── OrderStatus (preparing, out for delivery, delivered)
│   │   ├── TrackingMap
│   │   │   ├── RestaurantMarker
│   │   │   ├── DeliveryPartnerMarker
│   │   │   └── RoutePolyline
│   │   ├── ETA
│   │   └── DeliveryPartnerInfo
│   └── OrderHistoryPage
│       └── OrderList
└── SharedComponents
    ├── RestaurantCard
    ├── MenuItem
    └── TrackingMap
```

### Key Components Explained

**1. RestaurantList Component**
- Displays restaurants in grid/list
- Filters by category, cuisine, rating
- Shows delivery time and minimum order
- Clickable to view restaurant

**2. MenuList Component**
- Displays restaurant menu
- Menu items with customization options
- Add to cart functionality
- Cart summary sidebar

**3. OrderTrackingPage Component**
- Real-time order status
- Map showing restaurant and delivery partner
- ETA calculation
- Delivery partner information

---

## 3) Data Models

Here are the key data structures:

```typescript
// Restaurant
interface Restaurant {
  id: string;
  name: string;
  cuisine: string;
  rating: number;
  deliveryTime: number;  // Minutes
  minimumOrder: number;
  deliveryFee: number;
  imageUrl: string;
  address: string;
  isOpen: boolean;
}

// Menu item
interface MenuItem {
  id: string;
  restaurantId: string;
  name: string;
  description: string;
  price: number;
  imageUrl?: string;
  category: string;
  customizationOptions?: CustomizationOption[];
  isAvailable: boolean;
}

// Customization option
interface CustomizationOption {
  id: string;
  name: string;
  type: "single" | "multiple";
  options: Option[];
  required: boolean;
}

// Order
interface Order {
  id: string;
  userId: string;
  restaurantId: string;
  restaurant: Restaurant;
  items: OrderItem[];
  deliveryAddress: Address;
  status: "pending" | "confirmed" | "preparing" | "out_for_delivery" | "delivered" | "cancelled";
  deliveryPartnerId?: string;
  deliveryPartner?: DeliveryPartner;
  totalAmount: number;
  estimatedDeliveryTime: string;
  createdAt: string;
}

// Order item
interface OrderItem {
  id: string;
  menuItemId: string;
  menuItem: MenuItem;
  quantity: number;
  price: number;
  customizations: Record<string, string[]>;  // Selected options
}

// Delivery partner
interface DeliveryPartner {
  id: string;
  name: string;
  phone: string;
  currentLocation: Location;
  vehicle: Vehicle;
  rating: number;
}
```

### Data Flow Explanation

**When a user places an order:**
1. User browses restaurants and selects items
2. User customizes items (if options available)
3. User proceeds to checkout
4. User selects delivery address and payment method
5. Order is placed: POST /api/v1/orders
6. Order status: "pending" → "confirmed" → "preparing"
7. Delivery partner assigned
8. Order status: "preparing" → "out_for_delivery"
9. Real-time tracking of delivery partner
10. Order status: "out_for_delivery" → "delivered"

**Real-time tracking:**
1. Delivery partner location updated every 5 seconds
2. WebSocket broadcasts location to user
3. Map updates delivery partner marker
4. ETA recalculated based on current location
5. Route updated as delivery partner moves

---

## 4) API Design

### REST Endpoints

**GET /api/v1/restaurants**
- Get restaurants
- Query params: `location`, `cuisine`, `rating`, `page`, `limit`
- Returns: Paginated list of Restaurant objects

**GET /api/v1/restaurants/:id/menu**
- Get restaurant menu
- Returns: Array of MenuItem objects

**POST /api/v1/orders**
- Create an order
- Request body: `{ restaurantId: string, items: OrderItem[], deliveryAddressId: string, paymentMethodId: string }`
- Returns: Order object

**GET /api/v1/orders/:id**
- Get order details
- Returns: Order object

**GET /api/v1/orders/:id/tracking**
- Get order tracking info
- Returns: Order with delivery partner location

**GET /api/v1/orders**
- Get order history
- Query params: `page`, `limit`, `status`
- Returns: Paginated list of Order objects

### WebSocket Events

**Connection:** `wss://api.example.com/orders/:id`

**Events:**
- `order_status` - Order status changed
- `delivery_location` - Delivery partner location update
- `eta_update` - ETA updated

---

## Key Design Decisions

**1. Real-time Order Tracking**
- Track delivery partner location in real-time
- Update map and ETA continuously
- Better user experience
- WebSocket for instant updates

**2. Order Status Management**
- Clear status transitions
- Real-time status updates
- Handle cancellations gracefully

**3. Menu Customization**
- Support item customization options
- Store selected customizations
- Calculate price with customizations

---

## Interview Talking Points

**When explaining this system, I'd focus on:**

1. **Requirements First**: Start with core functionality - browse restaurants, place orders, real-time tracking, payments

2. **Component Structure**: Explain the React component hierarchy - restaurant list, menu, order tracking

3. **Data Models**: Walk through Restaurant, MenuItem, Order - and order status flow

4. **API Design**: Show the REST endpoints and WebSocket protocol - orders, tracking, real-time updates

5. **Key Challenges**: 
   - Real-time delivery tracking
   - Order status management
   - Handling peak hours (lunch/dinner)
   - Delivery partner matching

**Example explanation flow:**
> "So for a food delivery system, the core requirement is allowing users to browse restaurants, place orders, and track deliveries in real-time. The frontend is a React app with a restaurant list showing available restaurants, a menu view for selecting items with customization options, and an order tracking page with a map showing the delivery partner's location. When a user places an order, it goes through status transitions (pending, confirmed, preparing, out_for_delivery, delivered). Real-time tracking updates the delivery partner's location every 5 seconds via WebSocket, and the map and ETA update accordingly. The data model includes Restaurant objects, MenuItem objects with customization options, and Order objects with status tracking. The main API endpoints handle restaurant browsing, order creation, and order tracking, while WebSocket handles real-time location and status updates. Key challenges include real-time delivery tracking, handling traffic spikes during peak meal times, and ensuring accurate order status updates."
