# Ride-Sharing System

---

## 📍 Navigation

<div align="center">

[Home: README](README.md) • [← Previous: Ticket Booking System](12%29%20Ticket%20Booking%20System.md) • [Next: Food Delivery System →](14%29%20Food%20Delivery%20System.md)

[📋 Cheatsheet](Projects%20Interview%20Cheatsheet.md)

</div>

---

## Overview

Design a ride-sharing platform like Uber where users can request rides, get matched with nearby drivers, track rides in real-time, and process payments. The system handles geospatial matching, dynamic pricing, and real-time location tracking.

---

## 1) Requirements

### Functional Requirements

**Core Features:**
- Request rides (pickup and dropoff locations)
- Real-time driver matching (nearest available driver)
- Real-time location tracking (driver and rider)
- Ride status updates (requested, matched, arriving, in-progress, completed)
- ETA calculation and display
- Dynamic pricing (surge pricing during peak hours)
- Payment processing
- Ride history and receipts
- Rating and review system

**Advanced Features:**
- Ride scheduling (book rides in advance)
- Multiple ride types (economy, premium, XL)
- Ride sharing (pool/group rides)
- Driver earnings dashboard
- Route optimization

### Non-Functional Requirements

**Performance:**
- Ride matching: < 5 seconds
- Real-time location updates: every 5 seconds
- Low-latency ride requests

**Scalability:**
- Handle 100M+ users
- 10M+ rides per day
- Millions of concurrent users during peak hours

**Reliability:**
- 99.9% uptime
- Accurate location tracking
- Reliable ride matching

---

## 2) Component Hierarchy

The frontend is a React application with map integration. Here's the structure:

```
App
├── Layout
│   └── MainContent
├── Pages
│   ├── HomePage
│   │   ├── MapView (Google Maps/Mapbox)
│   │   │   ├── PickupMarker
│   │   │   ├── DropoffMarker
│   │   │   ├── DriverMarker (if matched)
│   │   │   └── RoutePolyline
│   │   ├── RideRequestPanel
│   │   │   ├── PickupInput
│   │   │   ├── DropoffInput
│   │   │   ├── RideTypeSelector
│   │   │   ├── PriceEstimate
│   │   │   └── RequestRideButton
│   │   └── ActiveRidePanel (when ride active)
│   │       ├── RideStatus
│   │       ├── DriverInfo
│   │       ├── ETA
│   │       ├── CancelButton
│   │       └── ContactDriverButton
│   ├── RideHistoryPage
│   │   └── RideList
│   │       └── RideCard
│   └── DriverDashboard (for drivers)
│       ├── DriverStatusToggle
│       └── RideRequests
└── SharedComponents
    ├── MapView
    ├── LocationPicker
    └── Toast
```

### Key Components Explained

**1. MapView Component**
- Google Maps or Mapbox integration
- Shows pickup/dropoff locations
- Displays driver location (when matched)
- Shows route between locations
- Real-time location updates

**2. RideRequestPanel Component**
- Pickup and dropoff location inputs
- Autocomplete for addresses
- Ride type selection
- Price estimate display
- Request ride button

**3. ActiveRidePanel Component**
- Shows active ride status
- Driver information and ETA
- Real-time location updates
- Cancel ride button
- Contact driver button

---

## 3) Data Models

Here are the key data structures:

```typescript
// Ride
interface Ride {
  id: string;
  riderId: string;
  driverId?: string;
  driver?: Driver;
  pickupLocation: Location;
  dropoffLocation: Location;
  status: "requested" | "matched" | "arriving" | "in_progress" | "completed" | "cancelled";
  rideType: "economy" | "premium" | "xl";
  price: number;
  estimatedDuration: number;  // Minutes
  estimatedDistance: number;  // Kilometers
  actualDuration?: number;
  actualDistance?: number;
  requestedAt: string;
  matchedAt?: string;
  startedAt?: string;
  completedAt?: string;
  rating?: number;
  review?: string;
}

// Location
interface Location {
  latitude: number;
  longitude: number;
  address: string;
}

// Driver
interface Driver {
  id: string;
  name: string;
  avatar?: string;
  vehicle: Vehicle;
  rating: number;
  currentLocation: Location;
  isAvailable: boolean;
}

// Vehicle
interface Vehicle {
  make: string;
  model: string;
  licensePlate: string;
  color: string;
}

// Price estimate
interface PriceEstimate {
  rideType: string;
  estimatedPrice: number;
  estimatedDuration: number;
  estimatedDistance: number;
  surgeMultiplier?: number;  // For surge pricing
}
```

### Data Flow Explanation

**When a user requests a ride:**
1. User enters pickup and dropoff locations
2. System calculates price estimate
3. User confirms and requests ride
4. System matches with nearest available driver
5. Ride status: "requested" → "matched"
6. Driver accepts and status: "matched" → "arriving"
7. Driver arrives and status: "arriving" → "in_progress"
8. Ride completes and status: "in_progress" → "completed"
9. Payment processed and receipt generated

**Real-time location tracking:**
1. Driver location updated every 5 seconds
2. WebSocket broadcasts location to rider
3. Map updates driver marker position
4. ETA recalculated based on current location
5. Route updated if driver takes different path

---

## 4) API Design

### REST Endpoints

**POST /api/v1/rides/estimate**
- Get price estimate
- Request body: `{ pickupLocation: Location, dropoffLocation: Location, rideType: string }`
- Returns: PriceEstimate object

**POST /api/v1/rides**
- Request a ride
- Request body: `{ pickupLocation: Location, dropoffLocation: Location, rideType: string }`
- Returns: Ride object

**GET /api/v1/rides/:id**
- Get ride details
- Returns: Ride object

**PATCH /api/v1/rides/:id/cancel**
- Cancel a ride
- Returns: Updated Ride object

**POST /api/v1/rides/:id/rate**
- Rate a completed ride
- Request body: `{ rating: number, review?: string }`
- Returns: Updated Ride object

**GET /api/v1/rides**
- Get ride history
- Query params: `page`, `limit`
- Returns: Paginated list of Ride objects

### WebSocket Events

**Connection:** `wss://api.example.com/rides/:id`

**Events:**
- `ride_matched` - Driver matched to ride
- `driver_location` - Driver location update
- `ride_status` - Ride status changed
- `eta_update` - ETA updated

**Message Format:**
```json
{
  "type": "driver_location",
  "data": {
    "driverId": "driver_123",
    "location": {
      "latitude": 37.7749,
      "longitude": -122.4194
    },
    "eta": 5  // Minutes
  }
}
```

---

## Key Design Decisions

**1. Geospatial Matching**
- Match riders with nearest available drivers
- Use geospatial indexing for fast queries
- Consider driver availability and rating

**2. Real-time Location Tracking**
- Update driver location every 5 seconds
- WebSocket for instant updates
- Update map and ETA in real-time

**3. Dynamic Pricing**
- Calculate base price from distance/time
- Apply surge multiplier during peak hours
- Show price estimate before booking

**4. Ride Status Management**
- Clear status transitions
- Real-time status updates
- Handle cancellations gracefully

---

## Interview Talking Points

**When explaining this system, I'd focus on:**

1. **Requirements First**: Start with core functionality - request rides, driver matching, real-time tracking, payments

2. **Component Structure**: Explain the React component hierarchy - map view, ride request panel, active ride panel

3. **Data Models**: Walk through Ride, Location, Driver - and ride status flow

4. **API Design**: Show the REST endpoints and WebSocket protocol - ride requests, location tracking, status updates

5. **Key Challenges**: 
   - Geospatial matching for driver assignment
   - Real-time location tracking and updates
   - Dynamic pricing calculation
   - Handling peak hour traffic

**Example explanation flow:**
> "So for a ride-sharing system, the core requirement is connecting riders with nearby drivers and tracking rides in real-time. The frontend is a React app with a map component (Google Maps/Mapbox) that shows pickup/dropoff locations and driver location. When a user requests a ride, they enter pickup and dropoff locations, and the system matches them with the nearest available driver. Real-time location tracking updates the driver's position every 5 seconds via WebSocket, and the map and ETA update accordingly. The data model includes Ride objects with status tracking (requested, matched, arriving, in_progress, completed), Location objects for geospatial data, and Driver objects with availability status. Dynamic pricing calculates the fare based on distance, time, and surge multipliers during peak hours. The main API endpoints handle ride requests, price estimates, and ride management, while WebSocket handles real-time location and status updates. Key challenges include geospatial matching for efficient driver assignment, real-time location tracking at scale, and handling traffic spikes during peak hours."

---

---

## 📍 Navigation

<div align="center">

[Home: README](README.md) • [← Previous: Ticket Booking System](12%29%20Ticket%20Booking%20System.md) • [Next: Food Delivery System →](14%29%20Food%20Delivery%20System.md)

[📋 Cheatsheet](Projects%20Interview%20Cheatsheet.md)

</div>

---
