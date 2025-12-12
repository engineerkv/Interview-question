# Food Delivery System

> **Project Type:** Full-Stack Web Application (MERN Stack)
> **Scale:** Handle 50M+ users, 10M+ orders per day, real-time order tracking
> **Tech Stack:** React.js, Node.js, Express.js, MongoDB, Redis, Socket.io, Geo-spatial DB

# 1) Problem Statement

Design and implement a food delivery platform that addresses the following challenges:

- **Core Functionality**: Enable users to browse restaurants and menus, place orders, track deliveries in real-time, and process payments
- **Scale Requirements**: Handle 50M+ users, 10M+ orders per day, thousands of restaurants, millions of concurrent users during peak hours
- **Performance**: Order placement < 3 seconds, real-time location tracking, fast restaurant and menu browsing, accurate ETA calculation
- **Order Management**: Process orders with real-time inventory updates, prevent overselling, handle complex menus and customization options, manage order lifecycle
- **Delivery Matching**: Match orders with delivery partners based on proximity, optimize delivery routes, handle concurrent order assignments
- **Real-time Tracking**: Provide live tracking of order status and delivery location, real-time updates to users, restaurants, and delivery partners
- **Payment Processing**: Secure payment processing, handle multiple payment methods, process order payments and restaurant payouts
- **Data Consistency**: Ensure accurate order processing, maintain inventory consistency, handle concurrent order requests reliably

---

# 2) High Level Design (HLD)

## a) Requirements

### i) Functional Requirements

- Browse restaurants and menus

- Place orders

- Assign delivery partners

- Real-time order tracking

- Payment processing

- Order history

### ii) Non-Functional Requirements

- Order placement < 3 seconds

- Real-time location tracking

- Handle peak hours (lunch/dinner)

- ETA calculation

---

## b) Scope and Priority

### Phase 1: MVP (Must Have) - Priority 1

- Core functionality

- Basic features

### Phase 2: Enhanced Features - Priority 2

- Additional capabilities

- Performance improvements

### Phase 2: Enhanced Features - Priority 2

- Order scheduling (book orders in advance)

- Multiple payment methods

- Restaurant ratings and reviews

- Order recommendations and personalization

- Loyalty programs and discounts

---

## c) Technology Choices

### Backend Framework

- **Node.js with Express.js** - Handle orders and delivery

### Database

- **Geospatial Database** - Store restaurant and delivery partner locations

- **Redis** - Cache active orders and locations

### Real-time Communication

- **WebSocket** - Real-time order tracking

### Additional Services

- **Message Queue** - Order processing and assignment

- **Maps API** - Route calculation and ETA

---

## d) Capacity Estimation

### Throughput Requirements

- **Total Users**: 50 million users
- **Daily Active Users (DAU)**: 25 million users per day
- **Peak Traffic**: 3x average during peak hours (lunch/dinner) (75 million users per day)
- **Orders per Day**: 10 million orders
- **Order Requests per Day**: 15 million order requests (some cancelled)
- **Read:Write Ratio**: 100:1 (browsing restaurants/menus vs placing orders)

**Calculations:**

- **Average Writes Per Second (WPS)**: 15M order requests / 86,400 seconds ≈ 174 WPS
- **Peak WPS**: 174 × 3 = 522 WPS
- **Average Reads Per Second (RPS)**: 174 × 100 = 17,400 RPS
- **Peak RPS**: 17,400 × 3 = 52,200 RPS
- **Concurrent Active Orders**: 500,000 concurrent active orders
- **Location Updates**: 10M orders × 50 location updates/order = 500M location updates/day ≈ 5,787 updates/second

### Storage Estimation

**Storage per Order:**

- Order metadata: 2 KB (id, userId, restaurantId, items, status, timestamps)
- Location tracking: 5 KB (50 location points × 100 bytes)
- Payment data: 1 KB (total, payment method, transaction ID)
- **Total per Order**: ~8 KB

**Storage Requirements:**

- **Orders per Year**: 10M orders/day × 365 = 3.65 billion orders
- **Order Storage**: 3.65B × 8 KB ≈ 29.2 TB per year
- **User Data**: 50M users × 5 KB ≈ 250 GB
- **Restaurant Data**: 100K restaurants × 50 KB ≈ 5 GB
- **Menu Data**: 100K restaurants × 500 KB ≈ 50 GB
- **Total Storage**: ~29.2 TB (orders) + 250 GB (users) + 5 GB (restaurants) + 50 GB (menus) ≈ 29.5 TB/year

### Bandwidth Estimation

- **Average Location Update Size**: 100 bytes per update
- **Daily Bandwidth**: 500M location updates × 100 bytes = 50 GB/day
- **Peak Bandwidth**: 50 GB × 3 = 150 GB/day during peak hours
- **Average Bandwidth**: 50 GB / 86,400 seconds ≈ 579 KB/s
- **Peak Bandwidth**: 579 KB/s × 3 ≈ 1.74 MB/s

### Caching Estimation

Following the **80-20 rule** where 20% of restaurants generate 80% of traffic:

- **Cache 20% of popular restaurants**: 100K × 0.2 = 20K restaurants
- **Cache memory required**: 20K × 550 KB (restaurant + menu) = 11 GB (distributed across Redis cluster)
- **Cache hit ratio**: 90% (only 10% of restaurant/menu requests hit database)
- **Requests hitting Database**: 17,400 × 0.10 ≈ 1,740 RPS (manageable with sharding)

### Infrastructure Sizing

- **WebSocket Servers**: 1,000-2,000 instances behind load balancer, each handling 2,000-5,000 concurrent connections
- **API Servers**: 500-1,000 instances for REST API, each handling 50-100 RPS
- **Matching Service**: 50-100 instances for delivery partner matching
- **Message Queue**: RabbitMQ/Kafka cluster with 20-50 nodes for order processing and assignment
- **Database**: MongoDB cluster with 50-100 nodes for storage and high read/write throughput, with geospatial indexes
- **Cache Layer**: Redis cluster with 50-100 nodes for high availability and performance
- **Maps API**: Google Maps/Mapbox API for route calculation and ETA
- **Payment Gateway**: Stripe/PayPal for payment processing

---

## e) Architecture Overview

The system follows a food delivery architecture with real-time order tracking, geospatial matching, and distributed order management. Here's how the complete system works:

### Frontend Architecture

**Frontend Layers:**

1. **Presentation Layer (React Components)**
   - **UI Components**: Reusable components (RestaurantCard, MenuItem, OrderCard, TrackingMap)
   - **Feature Components**: RestaurantList, MenuView, OrderPlacer, OrderTracker, PaymentForm
   - **Layout Components**: Header, Sidebar, Navigation, MainLayout
   - **Page Components**: HomePage, RestaurantPage, OrderPage, TrackingPage

2. **State Management Layer**
   - **Local State (useState)**: Component-specific UI state (selected items, cart, loading, errors)
   - **Server State (Redux Toolkit)**: Global state for restaurants, orders, cart, user
   - **WebSocket State**: Real-time order status updates, delivery location updates

3. **Map Integration Layer**
   - **Map Component**: Google Maps/Mapbox integration for restaurant and delivery tracking
   - **Location Services**: Get current location, geocoding, route calculation
   - **Marker Management**: Display restaurants, delivery partner locations, route visualization

4. **API Integration Layer**
   - **API Client**: Axios instance with interceptors for auth, error handling
   - **Redux Thunks**: Async actions for API operations (placeOrder, trackOrder, processPayment)
   - **Request/Response Transformation**: Data normalization and error handling

5. **WebSocket Layer**
   - **Socket.io Client**: WebSocket connection for real-time updates
   - **Event Handlers**: Order status change, delivery location update, ETA update
   - **Connection Management**: Auto-reconnect, heartbeat, connection state

6. **Routing Layer (React Router)**
   - **Route Configuration**: Define routes and protected routes
   - **Navigation**: Programmatic and declarative navigation
   - **Route Guards**: Authentication and authorization checks

7. **Build & Deployment Layer**
   - **Build Process**: Webpack/Vite bundling with code splitting
   - **Static Assets**: Served from CDN (CloudFront/Cloudflare)
   - **Environment Configuration**: Environment-specific API endpoints and WebSocket URLs

**Frontend Request Flow:**

1. **User Interaction** → User browses restaurants, places order, or tracks delivery
2. **State Update** → Redux action dispatched or local state updated
3. **API Call** → Axios makes HTTP request to backend API
4. **WebSocket** → Real-time updates via Socket.io
5. **Map Update** → Map component updates with new locations
6. **UI Update** → Components re-render with new data

### Backend Architecture

**Backend Layers:**

1. **WebSocket Server Layer** - Handles real-time WebSocket connections
2. **API Gateway/Load Balancer** - Entry point for all HTTP and WebSocket requests
3. **Order Service Layer** - Stateless servers handling order requests and management
4. **Matching Service Layer** - Geospatial matching algorithm for delivery partner assignment
5. **Location Service Layer** - Real-time location tracking and updates
6. **Message Queue Layer** - RabbitMQ/Kafka for reliable order processing and assignment
7. **Application Service Layer** - Business logic and orchestration
8. **Cache Layer** - In-memory caching for performance
9. **Database Layer** - Persistent data storage with geospatial indexes
10. **External Services Layer** - Maps API, Payment Gateway integration

### Complete Request Flow

**Order Placement Flow:**

1. **Frontend**: User selects restaurant, adds items to cart, places order
2. **API Call**: POST request to order API with order details
3. **Backend**: Validate order, check inventory, process payment
4. **Database**: Create order record with status "placed"
5. **Matching**: Find nearest available delivery partner using geospatial query
6. **Assignment**: Assign order to delivery partner
7. **WebSocket**: Notify restaurant, delivery partner, and user of order status
8. **Response**: Return order confirmation with estimated delivery time
9. **Frontend**: Show order confirmation and tracking screen

**Order Tracking Flow:**

1. **Frontend**: User opens order tracking page
2. **API Call**: GET request to order API
3. **Backend**: Fetch order details and current status
4. **WebSocket**: Join order room for real-time updates
5. **Location Updates**: Delivery partner sends location updates every 5 seconds
6. **Broadcast**: Server broadcasts location to user
7. **Frontend**: Map component updates with delivery partner location and ETA

**Delivery Partner Assignment Flow:**

1. **Order Created**: New order created, needs delivery partner
2. **Geospatial Query**: Find available delivery partners within 5km radius
3. **Filtering**: Filter by availability, rating, current load
4. **Assignment**: Assign order to best matching delivery partner
5. **Notification**: Notify delivery partner via push notification and WebSocket
6. **Acceptance**: Delivery partner accepts order
7. **Update**: Update order status and notify all parties

### Key Components

- **Frontend (React.js)**: Single-page application with WebSocket integration, map integration, component-based architecture, Redux for state management, Socket.io client for real-time updates
- **WebSocket Servers**: Stateless servers handling WebSocket connections, order status updates, location updates
- **Load Balancer**: Distributes WebSocket and HTTP traffic across servers, sticky sessions for WebSocket connections
- **Order Service Servers**: Stateless design for horizontal scaling, handle order placement, order management, payment processing
- **Matching Service**: Geospatial matching algorithm using Redis GeoHash or MongoDB geospatial indexes
- **Location Service**: Real-time location tracking and updates, geospatial queries
- **Message Queue (RabbitMQ/Kafka)**: Reliable order processing, ensures order assignment, handles order state transitions
- **Application Services**: Order Service, Restaurant Service, Delivery Service, Payment Service, Notification Service
- **Cache Layer (Redis)**: In-memory cache for active orders (20% of traffic), restaurant locations (GeoHash), menu data
- **Database (MongoDB)**: Sharded across multiple nodes for horizontal scaling, stores orders, restaurants, users with geospatial indexes
- **Maps API**: Google Maps/Mapbox for route calculation, ETA, geocoding
- **Payment Gateway**: Stripe/PayPal for secure payment processing

---

# 3) Low Level Design (LLD)

---

## Component Architecture

### Service Components

```typescript
class Service {
  async processRequest(data: any) {
    // Implementation details
  }
}

```

---

## Frontend Design

### Component Architecture

Think of the frontend as a tree of React components - each component handles a specific part of the UI, and they work together to create the complete user experience.

**Component Hierarchy:**

```
App
├── Header
│   ├── Logo
│   ├── LocationSelector
│   ├── SearchBar
│   └── CartIcon (with item count)
├── MainContent
│   ├── RestaurantListPage
│   │   ├── FilterBar
│   │   │   ├── CuisineFilter
│   │   │   ├── PriceFilter
│   │   │   └── RatingFilter
│   │   ├── RestaurantGrid
│   │   │   └── RestaurantCard
│   │   │       ├── RestaurantImage
│   │   │       ├── RestaurantName
│   │   │       ├── CuisineType
│   │   │       ├── Rating
│   │   │       ├── DeliveryTime
│   │   │       └── DeliveryFee
│   │   └── Pagination
│   ├── RestaurantDetailPage
│   │   ├── RestaurantHeader
│   │   │   ├── RestaurantImage
│   │   │   ├── RestaurantInfo
│   │   │   └── Rating
│   │   ├── MenuSection
│   │   │   └── MenuItem
│   │   │       ├── ItemImage
│   │   │       ├── ItemName
│   │   │       ├── ItemDescription
│   │   │       ├── ItemPrice
│   │   │       └── AddToCartButton
│   │   └── CartSummary
│   ├── CartPage
│   │   ├── CartItemList
│   │   │   └── CartItem
│   │   │       ├── ItemInfo
│   │   │       ├── QuantitySelector
│   │   │       └── RemoveButton
│   │   ├── OrderSummary
│   │   │   ├── Subtotal
│   │   │   ├── DeliveryFee
│   │   │   ├── Tax
│   │   │   ├── Total
│   │   │   └── CheckoutButton
│   │   └── DeliveryAddressForm
│   ├── OrderTrackingPage
│   │   ├── OrderStatusTimeline
│   │   ├── MapView
│   │   │   ├── RestaurantLocation
│   │   │   ├── DeliveryPartnerLocation
│   │   │   └── UserLocation
│   │   ├── DeliveryPartnerInfo
│   │   └── EstimatedArrival
│   └── OrderHistoryPage
│       ├── OrderList
│       │   └── OrderCard
│       │       ├── OrderInfo
│       │       ├── OrderItems
│       │       ├── OrderStatus
│       │       └── ReorderButton
└── SocketProvider (Real-time order updates)

```

### Key React Components

**Frontend Implementation:**

```typescript
// Restaurant Card Component
const RestaurantCard: React.FC<{ restaurant: Restaurant }> = ({ restaurant }) => {
  return (
    <div className="restaurant-card" onClick={() => navigate(`/restaurants/${restaurant.id}`)}>
      <img src={restaurant.image} alt={restaurant.name} />
      <h3>{restaurant.name}</h3>
      <div className="cuisine-type">{restaurant.cuisineType}</div>
      <div className="restaurant-meta">
        <span className="rating">⭐ {restaurant.rating}</span>
        <span className="delivery-time">{restaurant.deliveryTime} min</span>
        <span className="delivery-fee">${restaurant.deliveryFee}</span>
      </div>
    </div>
  );
};

// Menu Item Component
const MenuItem: React.FC<{ item: MenuItem; restaurantId: string }> = ({ item, restaurantId }) => {
  const dispatch = useAppDispatch();

  const handleAddToCart = () => {
    dispatch(addToCart({ item, restaurantId }));
  };

  return (
    <div className="menu-item">
      <img src={item.image} alt={item.name} />
      <div className="item-info">
        <h4>{item.name}</h4>
        <p>{item.description}</p>
        <div className="item-price">${item.price}</div>
      </div>
      <button onClick={handleAddToCart}>Add</button>
    </div>
  );
};

// Order Tracking Component
const OrderTrackingPage: React.FC<{ orderId: string }> = ({ orderId }) => {
  const { data: order } = useOrder(orderId);
  const { socket } = useSocket();

  useEffect(() => {
    socket.on('order-status-update', (status: OrderStatus) => {
      // Update order status
    });

    socket.on('delivery-location-update', (location: Location) => {
      // Update delivery partner location on map
    });

    return () => {
      socket.off('order-status-update');
      socket.off('delivery-location-update');
    };
  }, [socket]);

  return (
    <div className="order-tracking">
      <OrderStatusTimeline status={order?.status} />
      <MapView
        restaurantLocation={order?.restaurantLocation}
        deliveryPartnerLocation={order?.deliveryPartnerLocation}
        userLocation={order?.userLocation}
      />
      <DeliveryPartnerInfo partner={order?.deliveryPartner} />
      <EstimatedArrival eta={order?.eta} />
    </div>
  );
};

```

### State Management

**State Management Strategy:**

- **Local State (useState)**: Form inputs, UI state (loading, errors, selected filters)
- **Component State**: Each component manages its own UI state
- **API State**: React Query or SWR for server state (restaurants, menu, orders) - caching, refetching
- **Global State (Redux Toolkit)**: User authentication, cart items, selected location, active order

**Frontend Implementation:**

```typescript
// Using React Query for API state management
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

const useRestaurants = (filters: RestaurantFilters) => {
  return useQuery({
    queryKey: ['restaurants', filters],
    queryFn: async () => {
      const response = await axios.get('/api/v1/restaurants', { params: filters });
      return response.data;
    },
    staleTime: 5 * 60 * 1000 // Cache for 5 minutes
  });
};

const usePlaceOrder = () => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: async (orderData: OrderRequest) => {
      const response = await axios.post('/api/v1/orders', orderData);
      return response.data;
    },
    onSuccess: (data) => {
      // Navigate to order tracking
      navigate(`/orders/${data.orderId}/tracking`);
      // Clear cart
      dispatch(clearCart());
    }
  });
};

```

### Component Interactions

**Data Flow:**

1. **Restaurant Browsing** → RestaurantListPage fetches restaurants, displays RestaurantCard components
2. **Menu Viewing** → User clicks restaurant, navigates to RestaurantDetailPage with menu
3. **Cart Management** → User adds items to cart, updates Redux cart state
4. **Order Placement** → Checkout creates order, navigates to OrderTrackingPage
5. **Real-time Tracking** → Socket.io updates order status and delivery partner location

**Event Handling:**

- Restaurant search triggers debounced API call
- Cart updates sync with Redux state
- Order placement triggers payment processing
- Socket.io events update order status and tracking
- Location updates refresh nearby restaurants

### UI/UX Considerations

- **Loading States**: Show skeleton loaders for restaurant lists, spinners for actions
- **Error Handling**: Display user-friendly error messages with retry options
- **Validation**: Client-side validation for address and payment
- **Responsive Design**: Mobile-first layout, optimized for touch interactions
- **Accessibility**: ARIA labels, keyboard navigation, screen reader support
- **Performance**: Image lazy loading, virtual scrolling for long lists, efficient map rendering

---

## Data Models

### Model Interface

```typescript
interface Model {
  id: string;
  // Model fields
  createdAt: Date;
  updatedAt: Date;
}

```

---

## Data APIs

### POST /api/v1/orders

- **URL:** `/api/v1/orders`

- **Method:** POST

- **Request Body:**

  ```json
  {
    "restaurantId": "restaurant_abc123",
    "items": [
      {
        "itemId": "item_xyz789",
        "quantity": 2,
        "price": 15.99
      }
    ],
    "deliveryAddress": {
      "street": "123 Main St",
      "city": "New York",
      "zipCode": "10001",
      "latitude": 40.7128,
      "longitude": -74.0060
    },
    "paymentMethod": "card"
  }

  ```

- **Response:**

  ```json
  {
    "success": true,
    "data": {
      "orderId": "order_abc123",
      "restaurantId": "restaurant_abc123",
      "status": "placed",
      "estimatedDeliveryTime": 30,
      "totalAmount": 31.98,
      "createdAt": "2024-01-15T10:30:00Z"
    }
  }

  ```

- **Status Codes:** 201 (Created), 400 (Validation Error)

### GET /api/v1/orders/:orderId

- **URL:** `/api/v1/orders/:orderId`

- **Method:** GET

- **Response:**

  ```json
  {
    "success": true,
    "data": {
      "orderId": "order_abc123",
      "status": "out_for_delivery",
      "restaurant": {
        "name": "Restaurant Name",
        "address": "123 Restaurant St"
      },
      "deliveryPartner": {
        "name": "John Doe",
        "phone": "+1234567890",
        "location": {
          "latitude": 40.7150,
          "longitude": -74.0080
        }
      },
      "estimatedDeliveryTime": 15,
      "items": [...],
      "totalAmount": 31.98
    }
  }

  ```

- **Status Codes:** 200 (Success), 404 (Not Found)

### GET /api/v1/restaurants

- **URL:** `/api/v1/restaurants?latitude=40.7128&longitude=-74.0060&radius=5`

- **Method:** GET

- **Query Parameters:**
  - `latitude`: number (required)
  - `longitude`: number (required)
  - `radius`: number (default: 5km)
  - `cuisine`: string (optional)

- **Response:**

  ```json
  {
    "success": true,
    "data": {
      "restaurants": [
        {
          "restaurantId": "restaurant_abc123",
          "name": "Restaurant Name",
          "cuisine": "Italian",
          "rating": 4.5,
          "distance": 2.5,
          "estimatedDeliveryTime": 25
        }
      ]
    }
  }

  ```

- **Status Codes:** 200 (Success)

---

## Backend Implementation Details

### Express.js Server Structure

```

server/
├── routes/
├── controllers/
├── services/
└── models/

```

### Order Service

```typescript
class OrderService {
  async createOrder(orderData: OrderRequest): Promise<Order> {
    // Validate order
    // Assign restaurant
    // Process payment
    // Create order
    // Assign delivery partner
    // Return order
  }

  async findNearbyRestaurants(lat: number, lon: number, radius: number): Promise<Restaurant[]> {
    // Geospatial query
    // Filter by radius
    // Return restaurants
  }
}

```

---

## Order Flow

1. User places order

2. Assign to restaurant

3. Restaurant accepts order

4. Assign delivery partner (nearest available)

5. Track order status

6. Delivery partner picks up

7. Track delivery in real-time

8. Mark delivered

## Protocols

### REST API Protocol

- **Protocol:** REST (Representational State Transfer)

- **Data Format:** JSON

- **Authentication:** JWT Bearer token

### Additional Protocols

- **WebSocket** - For real-time features (if applicable)

- **Message Queue** - For async processing (if applicable)

---

---

## Implementation Details

### Core Implementation

**Note:** Implementation details are split between frontend (React.js) and backend (Node.js/Express.js). Each section indicates where the code runs.

### Order Placement and Restaurant Matching

**Frontend Implementation:** React component handles order placement and restaurant selection
**Backend Implementation:** Express.js service handles order creation and restaurant assignment

- **Strategy:** Geospatial restaurant matching - like finding nearby restaurants on a map, matches orders to nearest available restaurants

- **Order Assignment:** Assign orders to restaurants based on location, capacity, and availability

**Backend (Express.js):**

```typescript
// Backend: services/OrderService.ts
import redis from '../config/redis';

class OrderService {
  async findNearbyRestaurants(lat: number, lon: number, radius: number = 5): Promise<Restaurant[]> {
    // Geospatial query using Redis GeoHash
    const restaurants = await redis.georadius(
      'restaurants:available',
      lon,
      lat,
      radius,
      'km',
      'WITHCOORD',
      'WITHDIST',
      'ASC'
    );

    return restaurants.map((restaurant: any) => ({
      restaurantId: restaurant[0],
      distance: restaurant[1],
      coordinates: {
        latitude: restaurant[2][1],
        longitude: restaurant[2][0]
      }
    }));
  }

  async createOrder(orderData: OrderRequest): Promise<Order> {
    const session = await mongoose.startSession();
    session.startTransaction();

    try {
      // Find nearby restaurant
      const restaurants = await this.findNearbyRestaurants(
        orderData.deliveryAddress.latitude,
        orderData.deliveryAddress.longitude
      );

      if (restaurants.length === 0) {
        throw new Error('No restaurants available in your area');
      }

      const restaurant = restaurants[0];

      // Process payment
      const payment = await paymentService.processPayment({
        amount: orderData.totalAmount,
        paymentMethod: orderData.paymentMethod
      });

      // Create order
      const order = await Order.create([{
        restaurantId: restaurant.restaurantId,
        userId: orderData.userId,
        items: orderData.items,
        deliveryAddress: orderData.deliveryAddress,
        status: 'placed',
        totalAmount: orderData.totalAmount,
        paymentId: payment.paymentId
      }], { session });

      // Assign delivery partner
      const deliveryPartner = await this.assignDeliveryPartner(
        restaurant.restaurantId,
        orderData.deliveryAddress
      );

      order[0].deliveryPartnerId = deliveryPartner.partnerId;
      await order[0].save({ session });

      await session.commitTransaction();

      // Emit order created event
      io.emit('order:created', order[0]);

      return order[0];
    } catch (error) {
      await session.abortTransaction();
      throw error;
    } finally {
      session.endSession();
    }
  }
}

```

**Frontend Implementation:**

```typescript
// React component for order placement
import { useState } from 'react';
import { useMutation, useQuery } from '@tanstack/react-query';
import axios from 'axios';

const OrderPlacement: React.FC = () => {
  const [cart, setCart] = useState<CartItem[]>([]);
  const [deliveryAddress, setDeliveryAddress] = useState<Address | null>(null);

  // Get nearby restaurants
  const { data: restaurants } = useQuery({
    queryKey: ['restaurants', deliveryAddress],
    queryFn: () => axios.get('/api/v1/restaurants', {
      params: {
        latitude: deliveryAddress?.latitude,
        longitude: deliveryAddress?.longitude
      }
    }).then(res => res.data.data.restaurants),
    enabled: !!deliveryAddress
  });

  const { mutate: createOrder, isLoading } = useMutation({
    mutationFn: (orderData: any) =>
      axios.post('/api/v1/orders', orderData),
    onSuccess: () => {
      // Show success, navigate to tracking
    }
  });

  const handlePlaceOrder = () => {
    createOrder({
      restaurantId: selectedRestaurant,
      items: cart,
      deliveryAddress,
      paymentMethod: 'card'
    });
  };

  return (
    <div>
      {/* Restaurant selection */}
      {/* Cart */}
      {/* Delivery address */}
      <button onClick={handlePlaceOrder} disabled={isLoading}>
        {isLoading ? 'Placing Order...' : 'Place Order'}
      </button>
    </div>
  );
};

```

### Real-Time Order Tracking

**Frontend Implementation:** React component displays real-time order status and delivery partner location
**Backend Implementation:** Socket.io server broadcasts order status updates

- **Strategy:** WebSocket-based real-time tracking - like Uber tracking, shows live order status and delivery partner location

- **Status Updates:** Broadcast order status changes and location updates to users

**Backend (Express.js):**

```typescript
// Backend: socket/orderSocket.ts
export const setupOrderSocket = (io: Server) => {
  io.on('connection', (socket) => {
    socket.on('order:join', (orderId: string) => {
      socket.join(`order:${orderId}`);
    });

    // Broadcast order status updates
    socket.on('order:status:update', async (data: { orderId: string; status: string }) => {
      const order = await Order.findById(data.orderId);
      if (order) {
        order.status = data.status;
        await order.save();

        io.to(`order:${data.orderId}`).emit('order:status:changed', {
          orderId: data.orderId,
          status: data.status
        });
      }
    });

    // Broadcast delivery partner location
    socket.on('delivery:location:update', (data: { orderId: string; location: any }) => {
      io.to(`order:${data.orderId}`).emit('delivery:location:changed', {
        orderId: data.orderId,
        location: data.location
      });
    });
  });
};

```

### Error Handling

**Frontend Implementation:** React components handle errors and show user-friendly messages
**Backend Implementation:** Express.js middleware handles errors and returns proper status codes

**Backend (Express.js):**

```typescript
// Backend: middleware/errorHandler.ts
export const errorHandler = (err: Error, req: Request, res: Response, next: NextFunction) => {
  console.error('Order Error:', err);

  if (err.message === 'No restaurants available') {
    return res.status(404).json({ error: 'No restaurants available in your area. Please try a different location.' });
  }

  if (err.message === 'Payment failed') {
    return res.status(402).json({ error: 'Payment failed. Please try again.' });
  }

  if (err.name === 'ValidationError') {
    return res.status(400).json({ error: 'Invalid order data', details: err.message });
  }

  res.status(500).json({ error: 'Internal server error' });
};

```

**Error Scenarios:**

- **Restaurant Availability Errors:** Handle no restaurants available, restaurant closed - show clear error messages, suggest alternative locations

- **Payment Errors:** Handle payment failures, insufficient funds - retry payment, show alternative payment methods

- **Delivery Errors:** Handle delivery partner unavailability, delivery delays - reassign delivery partner, notify user

- **Location Errors:** Handle invalid delivery addresses, out of service area - validate addresses, show service area map

---

## Testing Strategy

### Frontend Testing (React.js)

**Unit Testing:**

- **Jest + React Testing Library** - Test components, order placement, tracking

- **Order Component Testing** - Test restaurant selection, menu, cart, order tracking

- **Mocking:** Mock API calls, Socket.io, geolocation API

**Integration Testing:**

- **Order Flow** - Test complete order placement process

- **Real-time Tracking** - Test Socket.io order status updates

- **API Integration Tests** - Test API calls with mock server

**E2E Testing:**

- **Cypress / Playwright** - Test food delivery flows

- **Test Scenarios:** Browse restaurants, place order, track delivery, payment

### Backend Testing (Node.js/Express.js)

**Unit Testing:**

- **Jest + Supertest** - Test API endpoints, order processing, delivery assignment

- **Geospatial Testing** - Test location-based restaurant and delivery matching

- **Mocking:** Mock MongoDB, Redis, Socket.io

**Integration Testing:**

- **MongoDB Memory Server** - Test database operations with geospatial queries

- **Redis Mock** - Test location caching

- **Socket.io Testing** - Test real-time order status updates

**Load Testing:**

- **Artillery / k6** - Test order processing under high load

- **Concurrent Orders:** Test performance with multiple simultaneous orders

---

## Deployment & DevOps

### Frontend Deployment

**Build Process:**

- **Production Build:** Optimized bundle with code splitting

- **CDN Deployment:** Deploy static assets to CDN

- **Environment Variables:** `.env.production` for production config

**Deployment Platforms:**

- **Vercel / Netlify** - Automatic deployments

- **AWS S3 + CloudFront** - Static site hosting with CDN

### Backend Deployment

**Server Setup:**

- **PM2:** Process manager with clustering

- **Nginx:** Load balancer and WebSocket proxy

- **Docker:** Containerized deployment

**Real-time Communication:**

- **Socket.io Scaling:** Redis adapter for horizontal scaling

- **Sticky Sessions:** Required for Socket.io

- **Load Balancer:** Configure for WebSocket support

**CI/CD Pipeline:**

- **Automated Testing:** Run tests before deployment

- **Zero-Downtime:** Rolling deployment strategy

- **Health Checks:** Verify order endpoints

---

## Environment Configuration

### Environment Variables

**Frontend:**

```env
REACT_APP_API_URL=https://api.example.com
REACT_APP_SOCKET_URL=wss://socket.example.com
REACT_APP_MAP_API_KEY=xxx
REACT_APP_ENVIRONMENT=production

```

**Backend:**

```env
NODE_ENV=production
PORT=3000
MONGODB_URI=mongodb://...
REDIS_URL=redis://...
JWT_SECRET=xxx
SOCKET_IO_REDIS_URL=redis://...

```

---

## Database Migrations & Seeding

### MongoDB Migrations

**Migration Scripts:**

- **Schema Changes:** Add geospatial indexes for location queries

- **Data Migrations:** Update order formats

- **Index Optimization:** Add compound indexes for order and restaurant queries

### Data Seeding

**Seed Data:**

- **Restaurants:** Seed test restaurants with locations

- **Menu Items:** Seed test menu items

- **Orders:** Seed test orders

- **Delivery Partners:** Seed test delivery partners

---

## API Documentation

### Swagger/OpenAPI

**API Documentation:**

- **Swagger UI:** Document REST APIs

- **Order API:** Document order placement endpoints

- **Restaurant API:** Document restaurant endpoints

- **Tracking API:** Document order tracking endpoints

- **WebSocket Documentation:** Document Socket.io events

---

## API Versioning

**Versioning Strategy:**

- **URL Versioning:** `/api/v1/orders`, `/api/v2/orders`

- **Header Versioning:** `Accept: application/vnd.api+json;version=1`

- **Backward Compatibility:** Maintain old API versions for existing clients

- **WebSocket Versioning:** Version Socket.io events

---

## Monitoring & Logging

### Application Monitoring

**Frontend:**

- **Error Tracking:** Sentry for order errors

- **Performance:** Track order placement times

- **User Analytics:** Track order patterns

**Backend:**

- **APM:** Monitor order processing performance

- **Socket.io Monitoring:** Track connection counts, order status updates

- **Order Metrics:** Track order volume, delivery times, restaurant performance

### Logging

**Structured Logging:**

- **Winston / Pino:** Log order operations

- **Order Events:** Log order placement, assignment, delivery, completion

- **Error Logging:** Detailed error logs with context

---

## Database Transactions & Consistency

### MongoDB Transactions

**Transaction Usage:**

- **Multi-Document Transactions** - For operations requiring ACID guarantees

- **Example:** Order creation + restaurant update + delivery assignment

- **Session Management:** Use MongoDB sessions for transaction control

**Example:**

```typescript
const session = await mongoose.startSession();
session.startTransaction();
try {
  await Order.create([orderData], { session });
  await Restaurant.updateOne({ restaurantId }, { $inc: { orderCount: 1 } }, { session });
  await DeliveryPartner.updateOne({ partnerId }, { $set: { status: 'busy' } }, { session });
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

- **Order Consistency:** Use transactions for order operations

- **Inventory Consistency:** Ensure menu item availability is consistent

- **Delivery Assignment Consistency:** Ensure delivery partner assignment is atomic

---

## Third-Party Service Integration

### Socket.io Integration

**Real-time Communication:**

- **Redis Adapter:** Enable horizontal scaling

- **Room Management:** Efficient room-based messaging for order tracking

- **Connection Management:** Handle reconnections, order status synchronization

### Redis Integration

**Caching & Location Tracking:**

- **Restaurant Caching:** Cache nearby restaurants

- **Location Caching:** Cache delivery partner locations

- **Distributed Locks:** Prevent race conditions in order assignment

### Map Service Integration

**Geolocation:**

- **Map API:** Google Maps / Mapbox integration

- **Route Calculation:** Calculate delivery routes and ETAs

- **Geocoding:** Convert addresses to coordinates

---

# 4) Algorithms

## Delivery Partner Matching Algorithm

**Purpose:** Find the nearest available delivery partner to a restaurant efficiently.

**Algorithm:**

1. Get restaurant location (latitude, longitude)
2. Search for available delivery partners within radius using geospatial query
3. Filter by availability status (not on active delivery)
4. Calculate distance to each partner
5. Consider partner rating and load
6. Select best match
7. Expand radius if no partner found

**Implementation:**

```typescript
class DeliveryMatchingService {
  async findNearestPartner(
    restaurantLat: number,
    restaurantLon: number,
    radius: number = 5
  ): Promise<string | null> {
    // Search using Redis GeoHash
    const partners = await redis.georadius(
      'partners:available',
      restaurantLon,
      restaurantLat,
      radius,
      'km',
      'WITHCOORD',
      'WITHDIST',
      'ASC',
      'COUNT',
      10
    );

    if (partners.length === 0 && radius < 10) {
      return this.findNearestPartner(restaurantLat, restaurantLon, 10);
    }

    // Filter available and rank by distance and rating
    const rankedPartners = await this.rankPartners(partners);

    return rankedPartners.length > 0 ? rankedPartners[0].partnerId : null;
  }
}

```

**Complexity:**

- Time: O(log n + m) where n is number of partners, m is results
- Space: O(m) for results
- **Matching Speed:** Geospatial queries enable < 100ms matching

---

## ETA Calculation Algorithm

**Purpose:** Calculate estimated delivery time based on distance, traffic, and historical data.

**Algorithm:**

1. Calculate distance from restaurant to customer
2. Get current traffic conditions
3. Look up historical delivery times for similar routes
4. Apply traffic multiplier
5. Add preparation time
6. Calculate final ETA

**Implementation:**

```typescript
function calculateETA(
  restaurantLocation: Location,
  customerLocation: Location,
  preparationTime: number = 20
): number {
  const distance = calculateDistance(restaurantLocation, customerLocation);
  const baseTime = distance / 30; // 30 km/h average speed
  const trafficMultiplier = getTrafficMultiplier(restaurantLocation, customerLocation);
  const historicalTime = getHistoricalETA(restaurantLocation, customerLocation);

  const travelTime = (baseTime * trafficMultiplier + historicalTime) / 2;
  const totalETA = preparationTime + travelTime;

  return Math.ceil(totalETA); // Round up to nearest minute
}

```

**Complexity:**

- Time: O(1) for calculation
- Space: O(1)
- **ETA Accuracy:** Historical data improves accuracy

---

# 5) Data Models

## Orders Collection (MongoDB)

```javascript
{
  _id: ObjectId,
  orderId: String,           // Unique order ID, indexed
  userId: ObjectId,          // Customer reference, indexed
  restaurantId: ObjectId,    // Restaurant reference, indexed
  deliveryPartnerId: ObjectId, // Delivery partner reference, indexed
  items: [Object],           // Array of order items
  totalAmount: Number,       // Total order amount
  deliveryFee: Number,       // Delivery fee
  status: String,           // placed, accepted, preparing, ready, picked_up, in_transit, delivered, cancelled
  deliveryAddress: Object,   // { address, latitude, longitude }
  estimatedDeliveryTime: Number, // ETA in minutes
  actualDeliveryTime: Date,  // Actual delivery timestamp
  paymentId: ObjectId,       // Payment reference
  placedAt: Date,           // Order placed timestamp, indexed
  createdAt: Date,
  updatedAt: Date
}

// Indexes:
// - { orderId: 1 } (unique)
// - { userId: 1, placedAt: -1 } (compound)
// - { restaurantId: 1, status: 1 } (compound)
// - { deliveryPartnerId: 1, status: 1 } (compound)
// - { status: 1, placedAt: -1 } (compound)

```

## Delivery Partners Collection (MongoDB)

```javascript
{
  _id: ObjectId,
  partnerId: String,         // Unique partner ID, indexed
  userId: ObjectId,          // User reference, indexed
  location: Object,          // { latitude, longitude } (geospatial index)
  status: String,           // available, busy, offline
  rating: Number,           // Average rating
  totalDeliveries: Number,  // Total deliveries completed
  currentOrderId: ObjectId, // Current active order
  createdAt: Date,
  updatedAt: Date
}

// Indexes:
// - { partnerId: 1 } (unique)
// - { location: "2dsphere" } (geospatial index)
// - { status: 1 } (indexed)

```

---

# 6) Database Transactions and Consistency

### MongoDB Transactions

**Transaction Usage:**

- **Multi-Document Transactions** - For operations requiring ACID guarantees
- **Example:** Order creation + restaurant update + delivery assignment in single transaction
- **Session Management:** Use MongoDB sessions for transaction control

**Example:**

```typescript
const session = await mongoose.startSession();
session.startTransaction();
try {
  await Order.create([orderData], { session });
  await Restaurant.updateOne({ restaurantId }, { $inc: { orderCount: 1 } }, { session });
  await DeliveryPartner.updateOne({ partnerId }, { $set: { status: 'busy' } }, { session });
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
- **Inventory Consistency:** Ensure menu item availability is consistent
- **Delivery Assignment Consistency:** Ensure delivery partner assignment is atomic
- **Eventual Consistency:** Accept eventual consistency for location updates (may update with slight delay)

---

# 7) Protocols

### REST API Protocol

- **Protocol:** REST (Representational State Transfer)
- **Data Format:** JSON
- **HTTP Methods:** GET, POST, PUT, DELETE
- **Status Codes:** 200 (Success), 201 (Created), 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), 500 (Server Error)
- **Authentication:** JWT Bearer token in Authorization header

### WebSocket Protocol

- **Protocol:** Socket.io over WebSocket
- **Events:** `order:status`, `location:update`, `eta:update`
- **Authentication:** JWT token in handshake
- **Use Case:** Real-time order tracking and location updates

---

# 8) API Design

### POST /api/v1/orders

- **URL:** `/api/v1/orders`
- **Method:** POST
- **Description:** Create a new order
- **Request Body:**

  ```json
  {
    "restaurantId": "rest_abc123",
    "items": [
      { "itemId": "item_1", "quantity": 2, "price": 15.99 }
    ],
    "deliveryAddress": {
      "address": "123 Main St",
      "latitude": 40.7128,
      "longitude": -74.0060
    }
  }

  ```

- **Response:**

  ```json
  {
    "success": true,
    "data": {
      "orderId": "order_abc123",
      "status": "placed",
      "estimatedDeliveryTime": 30,
      "totalAmount": 31.98
    }
  }

  ```

- **Status Codes:** 201 (Created), 400 (Validation Error)

### GET /api/v1/orders/:orderId

- **URL:** `/api/v1/orders/:orderId`
- **Method:** GET
- **Description:** Get order details with real-time status
- **Response:**

  ```json
  {
    "success": true,
    "data": {
      "orderId": "order_abc123",
      "status": "in_transit",
      "deliveryPartner": {...},
      "currentLocation": {...},
      "eta": 5
    }
  }

  ```

- **Status Codes:** 200 (Success), 404 (Order Not Found)

---

# 9) Caching Strategy

### Redis Cache

**Cache Strategy:**

- **Key Format:** `order:{orderId}`, `partner:location:{partnerId}`, `restaurants:nearby:{lat}:{lon}`
- **Value:** Serialized JSON (order data, partner location, nearby restaurants)
- **TTL:**
  - Order data: 300 seconds (5 minutes)
  - Partner locations: 60 seconds (frequently updated)
  - Nearby restaurants: 600 seconds (10 minutes)
- **Eviction Policy:** TTL-based eviction

**Cache Patterns:**

- **Cache-Aside Pattern:** Check cache first, if miss query database and update cache
- **Write-Through Pattern:** Update cache when order status changes
- **Cache Invalidation:** Invalidate order cache on status updates

---

# 10) Error Handling

### Error Scenarios and Responses

**Edge Cases Handling:**

- **Restaurant Closed:** Return 400 Bad Request with "Restaurant is currently closed"
- **Item Unavailable:** Return 400 Bad Request with unavailable items list
- **No Delivery Partner Available:** Return 503 Service Unavailable, queue order for later assignment
- **Payment Failure:** Return 402 Payment Required with payment error details
- **Order Not Found:** Return 404 Not Found

**Error Response Format:**

```json
{
  "error": {
    "code": "NO_PARTNER_AVAILABLE",
    "message": "No delivery partner available",
    "details": "We're experiencing high demand. Your order will be assigned shortly.",
    "retryAfter": 60
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

**WebSocket Scaling:**

- **Socket.io Redis Adapter:** Enable horizontal scaling of WebSocket connections
- **Sticky Sessions:** Required for Socket.io (use session affinity in load balancer)
- **Connection Management:** Monitor and manage WebSocket connections

**Database Scaling:**

- **Read Replicas:** Deploy read replicas for order queries
- **Sharding:** Shard orders by region or userId for write scaling
- **Connection Pooling:** Use connection pooling to manage database connections

**Caching:**

- Distributed Redis cluster for high availability
- Cache orders and partner locations
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

### Backend Deployment

**Server Setup:**

- **PM2:** Process manager with clustering for Node.js apps
- **Nginx:** Load balancer and reverse proxy with SSL termination
- **Docker:** Containerized deployment for consistency
- **Kubernetes:** Container orchestration for auto-scaling

**CI/CD Pipeline:**

- **Automated Testing:** Run tests before deployment
- **Zero-Downtime:** Rolling deployment strategy
- **Health Checks:** Verify order endpoints are healthy
- **Blue-Green Deployment:** Maintain two identical production environments

### Database Deployment

**MongoDB Setup:**

- **MongoDB Atlas** - Managed MongoDB service with automatic backups
- **Backup Strategy:** Daily automated backups with point-in-time recovery
- **Indexing:** Proper indexes on orderId, userId, restaurantId, status, geospatial index on location
- **Replication:** Replica sets for high availability

**Redis Setup:**

- **Redis Cloud / AWS ElastiCache** - Managed Redis service
- **Cluster Mode:** Redis cluster for high availability and performance
- **Persistence:** RDB snapshots and AOF for data durability

---

# 12) Security Considerations

### Rate Limiting

- Implement rate limiting at API layer to prevent abuse
- Limit number of orders per user per hour
- Use Redis for distributed rate limiting across multiple servers

### Input Validation

- Validate all API inputs (order data, addresses)
- Sanitize user input to prevent injection attacks
- Validate location coordinates (latitude/longitude ranges)

### HTTPS/TLS

- All communication between clients and API encrypted using HTTPS
- Prevents eavesdropping and man-in-the-middle attacks
- SSL/TLS certificates for secure connections

### Location Privacy

- **Location Encryption:** Encrypt location data in transit and at rest
- **Privacy Controls:** Allow users to control location sharing
- **Data Retention:** Implement location data retention policies

### Authentication and Authorization

- **JWT Tokens:** Use JWT for stateless authentication
- **Token Expiration:** Set appropriate token expiration times
- **Role-Based Access Control:** Implement RBAC for customer vs delivery partner access
- **Order Ownership:** Verify user owns order before allowing access

### Payment Security

- **PCI-DSS Compliance:** Use payment gateway SDKs that handle PCI-DSS compliance
- **Tokenization:** Never store full payment card details, use tokens
- **Idempotency:** Use idempotency keys to prevent duplicate charges

### Monitoring and Alerts

- Set up monitoring for unusual activity patterns
- Trigger alerts for potential security issues
- Track metrics: order rates, delivery success rates, payment success rates
- Log all operations for security auditing

---

# 3) Interview Answers

---

## Q1. 💡 Designing a food delivery system

**Situation:** Need to design a food delivery system for 50M+ users that handles 10M+ orders per day with real-time order tracking and delivery partner assignment.

**Action:** I designed a food delivery system:

- **Order Management:** Create order, assign to restaurant, track order status through state machine

- **Delivery Partner Assignment:** Match orders with nearest available delivery partner using geospatial queries

- **Real-time Tracking:** Use WebSocket for real-time location updates from delivery partners

- **Geospatial Database:** Use Redis GeoHash to find nearest delivery partners efficiently

- **Order State Machine:** Track order through states (placed, accepted, preparing, ready, picked up, in transit, delivered)

- **ETA Calculation:** Calculate estimated delivery time using distance, traffic, and historical data

- **Payment Processing:** Integrate payment gateway, process payment on order placement

- **Notification System:** Send notifications for order status updates (SMS, push, in-app)

**Result:** System handles 10M+ orders per day. Order placement completes in < 3 seconds. Real-time tracking updates every 5 seconds. 95% of orders assigned to delivery partner within 2 minutes.

**Takeaway:** Geospatial databases enable efficient delivery partner matching. Real-time tracking improves user experience. State machine ensures order consistency.

---

## Q2. 💡 Assigning delivery partners to orders

**Situation:** Need to match orders with nearest available delivery partner efficiently.

**Action:** I implemented delivery partner assignment:

- **Geospatial Query:** Use Redis GeoHash to find delivery partners within 5km radius of restaurant

- **Availability Filter:** Filter only available delivery partners (not on active delivery)

- **Distance Calculation:** Calculate distance using Haversine formula

- **Load Balancing:** Distribute orders evenly across delivery partners

- **Rating Consideration:** Prefer delivery partners with higher ratings

- **Batch Assignment:** Assign multiple orders to same delivery partner if on same route

- **Fallback:** If no partner in 5km, expand radius to 10km

**Result:** 95% of orders assigned within 2 minutes. Geospatial queries complete in < 100ms. Delivery partners assigned efficiently.

**Takeaway:** Geospatial databases provide efficient location-based matching. Load balancing ensures fair distribution.

---

## Q3. ⏰ ⏰ ⏰ Tracking orders in real-time

**Situation:** Users want to see delivery partner location and ETA in real-time.

**Action:** I implemented real-time order tracking:

- **Location Updates:** Delivery partner app sends location updates every 5 seconds via WebSocket

- **WebSocket Server:** Maintain WebSocket connections for real-time updates

- **Location Storage:** Store delivery partner locations in Redis GeoHash

- **Client Updates:** Push location updates to user's app via WebSocket

- **ETA Calculation:** Recalculate ETA based on current location and traffic

- **Map Integration:** Integrate with Google Maps for route visualization

- **Offline Handling:** Store last known location if delivery partner goes offline

**Result:** Real-time location updates every 5 seconds. ETA accuracy within 2 minutes. Users see delivery partner location on map.

**Takeaway:** WebSocket enables real-time updates. Geospatial storage provides efficient location queries.
