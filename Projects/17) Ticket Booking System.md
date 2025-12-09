# Ticket Booking System

> **Project Type:** Full-Stack Web Application (MERN Stack)
> **Scale:** Handle 10M+ users, 1M+ bookings per day, prevent double booking
> **Tech Stack:** React.js, Node.js, Express.js, MongoDB, Redis, Message Queue

# 1) Problem Statement

Design and implement a ticket booking system that addresses the following challenges:

- **Core Functionality**: Enable users to browse available seats, select seats, and complete bookings for events, movies, or shows while preventing double booking
- **Scale Requirements**: Handle 10M+ users, 1M+ bookings per day, millions of concurrent seat selections during popular events
- **Performance**: Booking latency < 2 seconds, fast seat availability updates, smooth booking experience
- **Seat Management**: Handle concurrent seat selection from multiple users, lock seats during booking process, prevent double booking, provide real-time seat availability
- **Booking Process**: Secure booking flow, seat locking mechanism, payment processing, booking confirmation
- **Concurrency Control**: Handle high concurrency during popular events, prevent race conditions, ensure seat availability accuracy
- **Payment Processing**: Process payments securely, handle payment failures, manage booking lifecycle
- **Data Consistency**: Ensure zero double bookings, maintain seat availability consistency, handle concurrent booking requests reliably

---

# 2) High Level Design (HLD)

## a) Requirements

### i) Functional Requirements

- Browse movies/events

- Select seats

- Book tickets

- Payment processing

- Prevent double booking

- Booking history

### ii) Non-Functional Requirements

- Booking latency < 2 seconds

- 100% prevent double booking

- Handle concurrent seat selection

- Handle peak hours (movie releases)

---

## b) Scope and Priority

### Phase 1: MVP (Must Have) - Priority 1

- Core functionality

- Basic features

### Phase 2: Enhanced Features - Priority 2

- Additional capabilities

- Performance improvements

### Phase 2: Enhanced Features - Priority 2

- Seat recommendations

- Booking cancellation and refunds

- Waitlist functionality

- Group bookings

- Booking analytics and reporting

---

## c) Technology Choices

### Backend Framework

- **Node.js with Express.js** - Handle booking requests

### Database

- **SQL Database** - ACID compliance for seat locking

- **Redis** - Distributed locks for seat allocation

### Additional Services

- **Message Queue** - Process bookings asynchronously

- **Payment Gateway** - Secure payment processing

---

---

## Architecture Overview

```

┌─────────────┐
│   Client    │
└──────┬──────┘
       │
       ▼
┌─────────────────┐
│  Load Balancer  │
└──────┬──────────┘
       │
   ┌───┴───┐
   ▼       ▼
┌──────┐ ┌──────┐
│Server│ │Server│
└──┬───┘ └──┬───┘
   │        │
   └───┬────┘
       ▼
┌─────────────────┐
│  Database       │
└─────────────────┘

```

---

## Key Design Decisions

1. **Seat Locking:** Lock seats during booking process

2. **Distributed Locks:** Use Redis distributed locks for seat reservation

3. **Database Transactions:** Use transactions for atomic booking

4. **Optimistic Locking:** Use version numbers to prevent concurrent updates

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
│   ├── Navigation
│   └── UserMenu (Profile, Bookings, Sign out)
├── MainContent
│   ├── EventsListPage
│   │   ├── FilterBar
│   │   │   ├── CategoryFilter
│   │   │   ├── DateFilter
│   │   │   └── LocationFilter
│   │   ├── EventGrid
│   │   │   └── EventCard
│   │   │       ├── EventImage
│   │   │       ├── EventTitle
│   │   │       ├── EventDate
│   │   │       ├── EventLocation
│   │   │       ├── TicketPrice
│   │   │       └── BookButton
│   │   └── Pagination
│   ├── EventDetailPage
│   │   ├── EventHeader
│   │   │   ├── EventImage
│   │   │   ├── EventInfo
│   │   │   └── TicketPriceRange
│   │   ├── ShowtimeSelector
│   │   │   └── ShowtimeButton
│   │   └── BookButton
│   ├── SeatSelectionPage
│   │   ├── SeatMap
│   │   │   ├── ScreenIndicator
│   │   │   ├── SeatGrid
│   │   │   │   └── Seat
│   │   │   │       ├── SeatNumber
│   │   │   │       └── SeatStatus (available, selected, booked)
│   │   │   └── Legend
│   │   ├── SelectedSeatsSummary
│   │   │   ├── SelectedSeatsList
│   │   │   ├── TotalPrice
│   │   │   └── ContinueButton
│   │   └── Timer (Booking expiry)
│   ├── BookingPage
│   │   ├── BookingSummary
│   │   │   ├── EventInfo
│   │   │   ├── SelectedSeats
│   │   │   ├── Showtime
│   │   │   └── TotalPrice
│   │   ├── CustomerInfoForm
│   │   │   ├── NameInput
│   │   │   ├── EmailInput
│   │   │   └── PhoneInput
│   │   └── PaymentSection
│   └── BookingHistoryPage
│       ├── BookingList
│       │   └── BookingCard
│       │       ├── EventInfo
│       │       ├── BookingDetails
│       │       ├── BookingStatus
│       │       └── DownloadTicketButton
└── SocketProvider (Real-time seat availability)
```

### Key React Components

**Frontend Implementation:**

```typescript
// Seat Map Component
const SeatMap: React.FC<{ showtimeId: string }> = ({ showtimeId }) => {
  const [selectedSeats, setSelectedSeats] = useState<string[]>([]);
  const { data: seatMap } = useSeatMap(showtimeId);
  const { socket } = useSocket();

  useEffect(() => {
    socket.on('seat-status-update', (update: SeatStatusUpdate) => {
      // Update seat availability in real-time
    });

    return () => {
      socket.off('seat-status-update');
    };
  }, [socket]);

  const handleSeatClick = (seatId: string, status: SeatStatus) => {
    if (status === 'booked') return;

    if (status === 'selected') {
      setSelectedSeats(prev => prev.filter(id => id !== seatId));
      // Release seat lock
      socket.emit('release-seat', { showtimeId, seatId });
    } else {
      setSelectedSeats(prev => [...prev, seatId]);
      // Lock seat
      socket.emit('lock-seat', { showtimeId, seatId });
    }
  };

  return (
    <div className="seat-map">
      <div className="screen">Screen</div>
      <div className="seat-grid">
        {seatMap?.seats.map(seat => (
          <Seat
            key={seat.id}
            seat={seat}
            isSelected={selectedSeats.includes(seat.id)}
            onClick={() => handleSeatClick(seat.id, seat.status)}
          />
        ))}
      </div>
      <Legend />
    </div>
  );
};

// Booking Summary Component
const BookingSummary: React.FC<{ booking: Booking }> = ({ booking }) => {
  return (
    <div className="booking-summary">
      <h3>Booking Summary</h3>
      <div className="event-info">
        <h4>{booking.event.title}</h4>
        <p>{formatDate(booking.showtime.date)}</p>
        <p>{booking.showtime.time}</p>
      </div>
      <div className="seats-info">
        <h4>Selected Seats</h4>
        <ul>
          {booking.seats.map(seat => (
            <li key={seat.id}>
              {seat.row}{seat.number} - ${seat.price}
            </li>
          ))}
        </ul>
      </div>
      <div className="total-price">
        Total: ${booking.totalPrice}
      </div>
    </div>
  );
};
```

### State Management

**State Management Strategy:**

- **Local State (useState)**: Selected seats, form inputs, UI state (loading, errors, timer)
- **Component State**: Each component manages its own UI state
- **API State**: React Query or SWR for server state (events, seat maps, bookings) - caching, refetching
- **Global State (Redux Toolkit)**: User authentication, active booking session, selected seats

**Frontend Implementation:**

```typescript
// Using React Query for API state management
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

const useSeatMap = (showtimeId: string) => {
  return useQuery({
    queryKey: ['seat-map', showtimeId],
    queryFn: async () => {
      const response = await axios.get(`/api/v1/showtimes/${showtimeId}/seats`);
      return response.data;
    },
    refetchInterval: 5000 // Refetch every 5 seconds for real-time updates
  });
};

const useBookTickets = () => {
  const queryClient = useQueryClient();
  
  return useMutation({
    mutationFn: async (bookingData: BookingRequest) => {
      const response = await axios.post('/api/v1/bookings', bookingData);
      return response.data;
    },
    onSuccess: (data) => {
      // Navigate to booking confirmation
      navigate(`/bookings/${data.bookingId}/confirmation`);
      // Invalidate bookings list
      queryClient.invalidateQueries({ queryKey: ['bookings'] });
    }
  });
};
```

### Component Interactions

**Data Flow:**

1. **Event Selection** → User browses events, selects event and showtime
2. **Seat Selection** → User selects seats, seats are locked via Socket.io
3. **Booking Creation** → User fills customer info, creates booking
4. **Payment Processing** → Payment processed, booking confirmed
5. **Real-time Updates** → Socket.io updates seat availability in real-time

**Event Handling:**

- Seat clicks lock/unlock seats via Socket.io
- Timer counts down booking expiry
- Real-time seat status updates prevent double booking
- Booking creation triggers payment processing
- Payment success confirms booking

### UI/UX Considerations

- **Loading States**: Show skeleton loaders for seat maps, spinners for booking actions
- **Error Handling**: Display user-friendly error messages, handle seat conflicts gracefully
- **Validation**: Client-side validation for customer info and seat selection
- **Responsive Design**: Mobile-first layout, touch-optimized seat selection
- **Accessibility**: ARIA labels, keyboard navigation, screen reader support
- **Performance**: Efficient seat map rendering, debounced seat locking, real-time updates via WebSocket

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

### POST /api/v1/bookings

- **URL:** `/api/v1/bookings`

- **Method:** POST

- **Request Body:**
  ```json
  {
    "eventId": "event_abc123",
    "seatIds": ["seat_1", "seat_2", "seat_3"],
    "userId": "user123",
    "paymentMethod": "card"
  }
  ```

- **Response:**
  ```json
  {
    "success": true,
    "data": {
      "bookingId": "booking_abc123",
      "eventId": "event_abc123",
      "seatIds": ["seat_1", "seat_2", "seat_3"],
      "status": "confirmed",
      "totalAmount": 150.00,
      "createdAt": "2024-01-15T10:30:00Z"
    }
  }
  ```

- **Status Codes:** 201 (Created), 400 (Validation Error), 409 (Seats Already Booked)

### GET /api/v1/bookings/:bookingId

- **URL:** `/api/v1/bookings/:bookingId`

- **Method:** GET

- **Response:**
  ```json
  {
    "success": true,
    "data": {
      "bookingId": "booking_abc123",
      "eventId": "event_abc123",
      "seatIds": ["seat_1", "seat_2", "seat_3"],
      "status": "confirmed",
      "totalAmount": 150.00,
      "qrCode": "https://example.com/qr/booking_abc123",
      "createdAt": "2024-01-15T10:30:00Z"
    }
  }
  ```

- **Status Codes:** 200 (Success), 404 (Not Found)

### POST /api/v1/seats/lock

- **URL:** `/api/v1/seats/lock`

- **Method:** POST

- **Request Body:**
  ```json
  {
    "eventId": "event_abc123",
    "seatIds": ["seat_1", "seat_2"]
  }
  ```

- **Response:**
  ```json
  {
    "success": true,
    "data": {
      "lockedSeats": ["seat_1", "seat_2"],
      "lockExpiresAt": "2024-01-15T10:35:00Z"
    }
  }
  ```

- **Status Codes:** 200 (Success), 409 (Seats Already Locked/Booked)

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

### Booking Service

```typescript
class BookingService {
  async createBooking(bookingData: BookingRequest): Promise<Booking> {
    // Lock seats
    // Process payment
    // Create booking
    // Release lock
    // Return booking
  }

  async lockSeats(eventId: string, seatIds: string[]): Promise<void> {
    // Acquire distributed lock
    // Check seat availability
    // Lock seats in Redis
    // Set TTL
  }
}

```

---

## Booking Flow

1. User selects seats

2. Lock seats (Redis distributed lock, 5-minute TTL)

3. User enters payment details

4. Process payment

5. Create booking (database transaction)

6. Release lock

7. Send confirmation

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

### Seat Locking and Booking

**Frontend Implementation:** React component handles seat selection and booking flow
**Backend Implementation:** Express.js service handles seat locking with distributed locks and booking transactions

- **Strategy:** Distributed locking with Redis - like reserving seats at a theater, locks seats temporarily to prevent double booking

- **Lock Duration:** 5-minute TTL - gives users time to complete payment while preventing indefinite locks

**Backend (Express.js):**

```typescript
// Backend: services/BookingService.ts
import redis from '../config/redis';
import { v4 as uuidv4 } from 'uuid';

class BookingService {
  async lockSeats(eventId: string, seatIds: string[], userId: string): Promise<boolean> {
    const lockKey = `lock:${eventId}:${seatIds.join(',')}`;
    const lockValue = uuidv4();
    const lockTTL = 300; // 5 minutes

    // Try to acquire lock
    const acquired = await redis.set(lockKey, lockValue, 'EX', lockTTL, 'NX');

    if (!acquired) {
      throw new Error('Seats already locked');
    }

    // Check if seats are available
    for (const seatId of seatIds) {
      const seatKey = `seat:${eventId}:${seatId}`;
      const isBooked = await redis.get(seatKey);

      if (isBooked) {
        // Release lock
        await redis.del(lockKey);
        throw new Error(`Seat ${seatId} is already booked`);
      }
    }

    // Lock seats
    for (const seatId of seatIds) {
      const seatKey = `seat:${eventId}:${seatId}`;
      await redis.setex(seatKey, lockTTL, userId);
    }

    return true;
  }

  async createBooking(bookingData: BookingRequest): Promise<Booking> {
    const session = await mongoose.startSession();
    session.startTransaction();

    try {
      // Lock seats
      await this.lockSeats(bookingData.eventId, bookingData.seatIds, bookingData.userId);

      // Process payment
      const payment = await paymentService.processPayment({
        amount: bookingData.totalAmount,
        paymentMethod: bookingData.paymentMethod
      });

      // Create booking
      const booking = await Booking.create([{
        eventId: bookingData.eventId,
        seatIds: bookingData.seatIds,
        userId: bookingData.userId,
        status: 'confirmed',
        totalAmount: bookingData.totalAmount,
        paymentId: payment.paymentId
      }], { session });

      // Mark seats as booked
      for (const seatId of bookingData.seatIds) {
        await Seat.updateOne(
          { eventId: bookingData.eventId, seatId },
          { $set: { status: 'booked', bookingId: booking[0].bookingId } },
          { session }
        );
      }

      // Release lock
      const lockKey = `lock:${bookingData.eventId}:${bookingData.seatIds.join(',')}`;
      await redis.del(lockKey);

      await session.commitTransaction();
      return booking[0];
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
// React component for seat selection and booking
import { useState } from 'react';
import { useMutation } from '@tanstack/react-query';
import axios from 'axios';

const SeatBooking: React.FC<{ eventId: string }> = ({ eventId }) => {
  const [selectedSeats, setSelectedSeats] = useState<string[]>([]);

  const { mutate: lockSeats, isLoading: isLocking } = useMutation({
    mutationFn: (seatIds: string[]) =>
      axios.post('/api/v1/seats/lock', { eventId, seatIds }),
    onSuccess: () => {
      // Proceed to payment
    }
  });

  const { mutate: createBooking, isLoading: isBooking } = useMutation({
    mutationFn: (bookingData: any) =>
      axios.post('/api/v1/bookings', bookingData),
    onSuccess: () => {
      // Show success message
    }
  });

  const handleSeatSelect = (seatId: string) => {
    setSelectedSeats(prev => [...prev, seatId]);
  };

  const handleBook = () => {
    // Lock seats first
    lockSeats(selectedSeats, {
      onSuccess: () => {
        // Then create booking
        createBooking({
          eventId,
          seatIds: selectedSeats,
          paymentMethod: 'card'
        });
      }
    });
  };

  return (
    <div>
      {/* Seat map */}
      <button onClick={handleBook} disabled={isLocking || isBooking}>
        {isBooking ? 'Booking...' : 'Book Seats'}
      </button>
    </div>
  );
};

```

### Error Handling

**Frontend Implementation:** React components handle errors and show user-friendly messages
**Backend Implementation:** Express.js middleware handles errors and returns proper status codes

**Backend (Express.js):**

```typescript
// Backend: middleware/errorHandler.ts
export const errorHandler = (err: Error, req: Request, res: Response, next: NextFunction) => {
  console.error('Booking Error:', err);

  if (err.message === 'Seats already locked' || err.message.includes('already booked')) {
    return res.status(409).json({ error: 'Seats are no longer available. Please select different seats.' });
  }

  if (err.message === 'Payment failed') {
    return res.status(402).json({ error: 'Payment failed. Please try again.' });
  }

  if (err.name === 'ValidationError') {
    return res.status(400).json({ error: 'Invalid booking data', details: err.message });
  }

  res.status(500).json({ error: 'Internal server error' });
};

```

**Frontend Implementation:**

```typescript
// React error handling
axios.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 409) {
      toast.error('Seats are no longer available. Please select different seats.');
    } else if (error.response?.status === 402) {
      toast.error('Payment failed. Please try again.');
    } else {
      toast.error('Booking failed. Please try again.');
    }
    return Promise.reject(error);
  }
);

```

**Error Scenarios:**

- **Seat Availability Errors:** Handle seats already booked, seats locked by another user - show clear error messages, refresh seat map

- **Payment Errors:** Handle payment failures, insufficient funds - retry payment, show alternative payment methods

- **Lock Timeout Errors:** Handle lock expiration during booking - re-lock seats, extend lock duration

- **Concurrency Errors:** Handle race conditions in seat booking - use distributed locks, database transactions

---

## Testing Strategy

### Frontend Testing (React.js)

**Unit Testing:**

- **Jest + React Testing Library** - Test components, seat selection, booking flow

- **Booking Component Testing** - Test seat map, booking form, payment integration

- **Mocking:** Mock API calls, payment gateway, seat availability

**Integration Testing:**

- **Booking Flow** - Test complete booking process

- **Seat Selection** - Test seat selection and locking

- **API Integration Tests** - Test API calls with mock server

**E2E Testing:**

- **Cypress / Playwright** - Test booking flows

- **Test Scenarios:** Select seats, book tickets, handle concurrent bookings, payment

### Backend Testing (Node.js/Express.js)

**Unit Testing:**

- **Jest + Supertest** - Test API endpoints, seat locking logic

- **Concurrency Testing** - Test seat locking under concurrent requests

- **Mocking:** Mock database, Redis, payment gateway

**Integration Testing:**

- **MongoDB Memory Server** - Test database operations

- **Redis Mock** - Test seat locking

- **Payment Gateway Mock** - Test payment processing

**Load Testing:**

- **Artillery / k6** - Test booking system under high load

- **Concurrent Bookings:** Test performance with multiple simultaneous bookings

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

- **Nginx:** Load balancer and reverse proxy

- **Docker:** Containerized deployment

**CI/CD Pipeline:**

- **Automated Testing:** Run tests before deployment

- **Zero-Downtime:** Rolling deployment strategy

- **Health Checks:** Verify booking endpoints

### Database Deployment

**MongoDB Setup:**

- **MongoDB Atlas** - Managed MongoDB service

- **Backup Strategy:** Daily automated backups

- **Indexing:** Proper indexes for seat and booking queries

**Redis Setup:**

- **Redis Cloud / AWS ElastiCache** - Managed Redis service

- **Seat Locking:** Use Redis for distributed seat locks

---

## Environment Configuration

### Environment Variables

**Frontend:**

```env
REACT_APP_API_URL=https://api.example.com
REACT_APP_PAYMENT_GATEWAY_KEY=pk_live_xxx
REACT_APP_ENVIRONMENT=production

```

**Backend:**

```env
NODE_ENV=production
PORT=3000
MONGODB_URI=mongodb://...
REDIS_URL=redis://...
PAYMENT_GATEWAY_SECRET_KEY=sk_live_xxx
SEAT_LOCK_TTL=300

```

---

## Database Migrations & Seeding

### MongoDB Migrations

**Migration Scripts:**

- **Schema Changes:** Add indexes for booking queries

- **Data Migrations:** Update booking formats

- **Index Optimization:** Add compound indexes for seat availability queries

### Data Seeding

**Seed Data:**

- **Events:** Seed test events

- **Seats:** Seed test seat configurations

- **Bookings:** Seed test bookings

---

## API Documentation

### Swagger/OpenAPI

**API Documentation:**

- **Swagger UI:** Document REST APIs

- **Booking API:** Document booking endpoints

- **Seat API:** Document seat availability endpoints

---

## API Versioning

**Versioning Strategy:**

- **URL Versioning:** `/api/v1/bookings`, `/api/v2/bookings`

- **Header Versioning:** `Accept: application/vnd.api+json;version=1`

- **Backward Compatibility:** Maintain old API versions for existing clients

---

## Monitoring & Logging

### Application Monitoring

**Frontend:**

- **Error Tracking:** Sentry for booking errors

- **Performance:** Track booking processing times

- **User Analytics:** Track booking patterns

**Backend:**

- **APM:** Monitor booking processing performance

- **Seat Lock Monitoring:** Track seat lock operations

- **Booking Metrics:** Track booking volume, success rates, seat utilization

### Logging

**Structured Logging:**

- **Winston / Pino:** Log booking operations

- **Booking Events:** Log seat selection, booking creation, payment processing

- **Error Logging:** Detailed error logs with context

---

## Database Transactions & Consistency

### MongoDB Transactions

**Transaction Usage:**

- **Multi-Document Transactions** - For operations requiring ACID guarantees

- **Example:** Booking creation + seat update + payment processing

- **Session Management:** Use MongoDB sessions for transaction control

**Example:**

```typescript
const session = await mongoose.startSession();
session.startTransaction();
try {
  await Booking.create([bookingData], { session });
  await Seat.updateOne({ seatId }, { $set: { status: 'booked' } }, { session });
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

- **Booking Consistency:** Use transactions for booking operations

- **Seat Consistency:** Use distributed locks + transactions for seat booking

- **Payment Consistency:** Ensure payment and booking updates are atomic

---

## Third-Party Service Integration

### Payment Gateway Integration

**Payment Processing:**

- **SDK Integration:** Integrate payment gateway SDK

- **Webhook Handling:** Handle payment gateway webhooks

- **Idempotency:** Implement idempotency for payment requests

### Redis Integration

**Distributed Locking:**

- **Seat Locking:** Use Redis SETNX for distributed seat locks

- **Lock TTL:** Set TTL on locks to prevent deadlocks

- **Lock Release:** Release locks after booking completion or timeout

---

# 3) Interview Answers

---

## Q1. Designing a ticket booking system

**Situation:** Need to design a ticket booking system for 10M+ users that prevents double booking, handles concurrent seat selection, and processes 1M+ bookings per day.

**Action:** I designed a ticket booking system:

- **Seat Locking:** Lock seats using Redis distributed locks when user selects seats (5-minute TTL)

- **Distributed Locks:** Use Redis SETNX for distributed locking across multiple servers

- **Database Transactions:** Use database transactions for atomic booking creation

- **Optimistic Locking:** Use version numbers in seat table to prevent concurrent updates

- **Payment Processing:** Integrate payment gateway, create booking only after payment success

- **Lock Expiration:** Auto-release locks after 5 minutes if booking not completed

- **Seat Availability Cache:** Cache seat availability in Redis for fast lookups

- **Queue System:** Queue booking requests during peak hours to prevent overload

**Result:** System handles 1M+ bookings per day. Zero double bookings in production. Booking completes in < 2 seconds. Handles concurrent seat selection correctly.

**Takeaway:** Distributed locks prevent double booking. Database transactions ensure atomicity. Lock expiration prevents deadlocks.

---

## Q2. Preventing double booking of the same seat

**Situation:** Two users try to book the same seat simultaneously, need to prevent double booking.

**Action:** I implemented double booking prevention:

- **Distributed Locks:** Use Redis SETNX to lock seat when user selects it

- **Lock Key:** Use seat ID as lock key (e.g., "lock:seat:123")

- **Lock TTL:** Set 5-minute TTL on lock to prevent deadlocks

- **Database Transaction:** Use database transaction with row-level locking

- **Optimistic Locking:** Use version number in seat table, increment on update

- **Validation:** Check seat availability again before creating booking

- **Atomic Operations:** Use database atomic operations (UPDATE ... WHERE available = true)

**Result:** Zero double bookings in production. Distributed locks prevent concurrent seat selection. Database transactions ensure consistency.

**Takeaway:** Distributed locks + database transactions provide strong consistency. Optimistic locking handles edge cases.

---

## Q3. Handling concurrent seat selection

**Situation:** Multiple users select seats simultaneously, need to handle conflicts.

**Action:** I implemented concurrent seat selection:

- **Seat Locking:** Lock seat immediately when user selects it

- **Lock Status:** Return lock status to client, show seat as "selecting" to other users

- **Lock Expiration:** Auto-release lock after 5 minutes if booking not completed

- **Conflict Resolution:** If seat already locked, return error to user

- **Real-time Updates:** Use WebSocket to notify other users when seat is selected/released

- **Batch Selection:** Allow users to select multiple seats, lock all at once

**Result:** Concurrent seat selection handled correctly. Users see real-time seat availability. No conflicts or double selections.

**Takeaway:** Immediate locking prevents conflicts. Real-time updates improve user experience.
