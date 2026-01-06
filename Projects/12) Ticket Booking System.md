# Ticket Booking System

---

## 📍 Navigation

<div align="center">

[Home: README](README.md) • [← Previous: Time-Limited Content System](11%29%20Time-Limited%20Content%20System.md) • [Next: Ride-Sharing System →](13%29%20Ride-Sharing%20System.md)

[📋 Cheatsheet](Projects%20Interview%20Cheatsheet.md)

</div>

---

## Overview

Design a ticket booking system for events, movies, or shows where users can browse available seats, select seats, and complete bookings while preventing double booking through seat locking and real-time availability updates.

---

## 1) Requirements

### Functional Requirements

**Core Features:**
- Browse events, movies, or shows
- Visual seat map with availability (available, occupied, locked)
- Real-time seat availability updates
- Seat selection and locking during booking
- Booking flow with payment processing
- Booking confirmation and tickets
- Booking management (view, cancel, modify)
- Prevent double booking

**Advanced Features:**
- Waitlist for sold-out events
- Group booking discounts
- Seat recommendations
- Booking analytics
- Refund processing

### Non-Functional Requirements

**Performance:**
- Booking latency: < 2 seconds
- Fast seat availability updates
- Real-time seat status updates

**Scalability:**
- Handle 10M+ users
- 1M+ bookings per day
- Millions of concurrent seat selections during popular events

**Reliability:**
- 99.9% uptime
- Zero double bookings
- Handle high concurrency

---

## 2) Component Hierarchy

The frontend is a React application for ticket booking. Here's the structure:

```
App
├── Layout
│   ├── Header
│   │   ├── Logo
│   │   └── UserMenu
│   └── MainContent
├── Pages
│   ├── EventsPage
│   │   └── EventList
│   │       └── EventCard
│   ├── EventDetailPage
│   │   ├── EventInfo
│   │   └── BookTicketsButton
│   ├── SeatSelectionPage
│   │   ├── SeatMap
│   │   │   ├── SeatGrid
│   │   │   │   └── Seat (available/occupied/locked/selected)
│   │   │   └── Legend (seat status colors)
│   │   ├── SelectedSeatsSummary
│   │   └── ContinueButton
│   ├── BookingPage
│   │   ├── BookingSummary
│   │   ├── PaymentForm
│   │   └── ConfirmBookingButton
│   └── BookingConfirmationPage
│       ├── BookingDetails
│       └── DownloadTicketsButton
└── SharedComponents
    ├── SeatMap
    ├── Seat
    └── Toast
```

### Key Components Explained

**1. SeatMap Component**
- Visual representation of venue
- Shows seat grid with status
- Real-time availability updates via WebSocket
- Seat selection handling
- Legend for seat status

**2. Seat Component**
- Individual seat in grid
- Status: available, occupied, locked, selected
- Color-coded by status
- Clickable to select/deselect
- Disabled when occupied or locked

**3. SeatSelectionPage Component**
- Main seat selection interface
- Seat map with real-time updates
- Selected seats summary
- Continue to booking button

---

## 3) Data Models

Here are the key data structures:

```typescript
// Event
interface Event {
  id: string;
  name: string;
  description: string;
  venue: Venue;
  date: string;
  time: string;
  price: number;
  availableSeats: number;
  totalSeats: number;
}

// Venue
interface Venue {
  id: string;
  name: string;
  address: string;
  seatLayout: SeatLayout;
}

// Seat layout
interface SeatLayout {
  rows: number;
  seatsPerRow: number;
  sections: Section[];
}

// Section
interface Section {
  id: string;
  name: string;
  rows: string[];  // ["A", "B", "C"]
  seatsPerRow: number;
  price: number;
}

// Seat
interface Seat {
  id: string;
  sectionId: string;
  row: string;
  number: number;
  status: "available" | "occupied" | "locked" | "selected";
  lockedBy?: string;  // User ID if locked
  lockedUntil?: string;  // Lock expiration time
  price: number;
}

// Booking
interface Booking {
  id: string;
  eventId: string;
  userId: string;
  seats: Seat[];
  totalAmount: number;
  status: "pending" | "confirmed" | "cancelled";
  createdAt: string;
  paymentId?: string;
}
```

### Data Flow Explanation

**When a user selects seats:**
1. User clicks available seat
2. Seat status changes to "selected" (client-side)
3. Lock seat: POST /api/v1/seats/:id/lock
4. Seat status changes to "locked" (server-side)
5. Lock expires after timeout (e.g., 5 minutes)
6. Other users see seat as locked
7. On booking completion, seat becomes occupied

**Seat locking mechanism:**
1. User selects seat
2. Frontend sends lock request
3. Server locks seat for user (with timeout)
4. Other users see seat as locked
5. Lock expires if booking not completed
6. Seat becomes available again

---

## 4) API Design

### REST Endpoints

**GET /api/v1/events**
- Get events
- Query params: `date`, `category`, `page`, `limit`
- Returns: Paginated list of Event objects

**GET /api/v1/events/:id/seats**
- Get seat map for event
- Returns: SeatLayout with seat statuses

**POST /api/v1/seats/:id/lock**
- Lock a seat
- Request body: `{ timeout: number }` (minutes)
- Returns: Locked Seat object

**POST /api/v1/seats/:id/unlock**
- Unlock a seat
- Returns: Updated Seat object

**POST /api/v1/bookings**
- Create a booking
- Request body: `{ eventId: string, seatIds: string[], paymentMethodId: string }`
- Returns: Booking object

**GET /api/v1/bookings**
- Get user's bookings
- Returns: Paginated list of Booking objects

### WebSocket Events

**Connection:** `wss://api.example.com/events/:id/seats`

**Events:**
- `seat_locked` - Seat was locked
- `seat_unlocked` - Seat was unlocked
- `seat_occupied` - Seat was booked
- `seat_available` - Seat became available

---

## Key Design Decisions

**1. Seat Locking Mechanism**
- Lock seats during booking process
- Prevent double booking
- Lock expires after timeout
- Real-time updates via WebSocket

**2. Real-time Availability**
- WebSocket for instant seat status updates
- All users see same seat status
- Prevents race conditions

**3. Visual Seat Map**
- Color-coded seat status
- Easy seat selection
- Clear availability indication

---

## Interview Talking Points

**When explaining this system, I'd focus on:**

1. **Requirements First**: Start with core functionality - browse events, select seats, prevent double booking

2. **Component Structure**: Explain the React component hierarchy - seat map, seat selection, booking flow

3. **Data Models**: Walk through Event, Seat, Booking - and seat locking mechanism

4. **API Design**: Show the REST endpoints and WebSocket protocol - seat locking, booking, real-time updates

5. **Key Challenges**: 
   - Preventing double booking with seat locking
   - Real-time seat availability updates
   - Handling high concurrency during popular events
   - Seat locking timeout management

**Example explanation flow:**
> "So for a ticket booking system, the core requirement is allowing users to select seats and book tickets while preventing double booking. The frontend is a React app with a seat map component that displays the venue layout with color-coded seats (available, occupied, locked, selected). When a user selects a seat, we lock it on the server for a few minutes to prevent others from booking it. The lock expires if the booking isn't completed. Real-time seat availability is updated via WebSocket so all users see the same seat status. The data model includes Event objects, Seat objects with status tracking, and Booking objects for completed bookings. The main API endpoints handle seat locking, unlocking, and booking creation. Key challenges include preventing double booking through proper seat locking, handling high concurrency during popular events, and ensuring real-time seat availability updates so users see accurate seat status."

---

---

## 📍 Navigation

<div align="center">

[Home: README](README.md) • [← Previous: Time-Limited Content System](11%29%20Time-Limited%20Content%20System.md) • [Next: Ride-Sharing System →](13%29%20Ride-Sharing%20System.md)

[📋 Cheatsheet](Projects%20Interview%20Cheatsheet.md)

</div>

---
