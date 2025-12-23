# 1) Problem Statement

Design and implement a secure payment processing system that addresses the following challenges:

- **Core Functionality**: Process payments securely through payment gateways, support multiple payment methods (credit cards, debit cards, wallets), handle refunds, and maintain payment history
- **Scale Requirements**: Handle 1B+ transactions per day, millions of concurrent payment requests, and high transaction volumes during peak hours
- **Performance**: Payment processing < 2 seconds, fast payment history retrieval, low-latency payment status updates
- **Security**: PCI-DSS compliance, secure payment data handling, fraud detection mechanisms, protect against fraudulent transactions
- **Reliability**: 99.99% reliability, zero duplicate charges, ensure idempotency, handle payment gateway failures gracefully
- **Payment Gateway Integration**: Integrate with multiple payment gateways, handle webhooks for payment status updates, process payment responses
- **Fraud Detection**: Implement fraud detection mechanisms, analyze transaction patterns, block suspicious transactions
- **Data Consistency**: Ensure idempotency to prevent duplicate charges, maintain transaction consistency, handle concurrent payment requests reliably

---

# 2) High Level Design (HLD)

## a) Functional Requirements

- Process payments (credit cards, debit cards, wallets) with secure payment forms
- Payment gateway integration via SDK
- Refund processing UI
- Payment history display and filtering
- Payment method management (save, update, delete payment methods)
- Real-time payment status updates
- Payment analytics dashboard

---

## b) Non-Functional Requirements

- Payment form submission < 2 seconds
- 99.9% frontend availability
- PCI-DSS compliant payment form handling
- Idempotency key generation (prevent duplicate charges)
- Responsive design for mobile and desktop
- Accessible payment forms (keyboard navigation, screen readers)

---

## c) MVP (Minimum Viable Product)

**Phase 1: Core Features (Must Have)**

- Payment form with card input
- Payment processing with idempotency
- Payment status display
- Basic error handling
- Responsive web interface

**Phase 2: Enhanced Features**

- Payment method management
- Payment history with filtering
- Refund request UI
- Payment analytics dashboard
- Real-time status updates

**Phase 3: Advanced Features**

- Multiple payment gateway support
- Recurring payments UI
- Payment method tokenization
- Advanced analytics and reporting

---

## d) Technology Choices

### Frontend Framework

- **React 19** - Latest React version with useOptimistic, useActionState, useTransition, useDeferredValue, and use() hook
- **TypeScript** - Type safety and better developer experience

### State Management

- **React Query (TanStack Query)** - Server state management for payment data, transaction history, payment status
- **Redux Toolkit** - Client state management for UI state (selected payment method, form state, payment preferences)
- **Context API** - App-wide configuration (user authentication, theme, app settings)

### Payment Integration

- **Payment Gateway SDK** - Stripe.js, PayPal SDK, or similar for secure payment processing
- **Tokenization** - Client-side tokenization for secure payment method storage

### UI/UX Libraries

- **React Router** - Client-side routing and navigation
- **React Hot Toast** - Toast notifications for payment status, errors, and success messages

### Build Tools

- **Vite** - Fast build tool and development server

### Testing

- **React Testing Library** - Component testing
- **Vitest** - Unit testing framework
- **Playwright** - E2E testing for payment flows

### Deployment

- **Vercel/Netlify** - Static site hosting with CDN
- **AWS S3 + CloudFront** - Alternative deployment with custom CDN configuration

**Trade-offs:**

- **React Query vs SWR**: React Query provides better caching and mutation handling for payments, but SWR is lighter - choose React Query for complex payment operations
- **Redux Toolkit vs Zustand**: Redux Toolkit offers better DevTools for debugging payment state, but Zustand is simpler - choose Redux Toolkit for complex payment form state
- **Payment Gateway SDK**: Stripe.js provides excellent UX but requires PCI compliance - essential for secure payment processing

---

## e) Architecture Overview

The frontend follows a secure payment processing architecture with idempotency, fraud detection, and distributed transaction management.

**Component Structure:**

```

Frontend Application
├── Presentation Layer
│   ├── UI Components (PaymentForm, PaymentMethodCard, TransactionCard, ReceiptView)
│   ├── Feature Components (PaymentProcessor, PaymentHistory, RefundRequest, PaymentMethodManager)
│   └── Layout Components (Header, Sidebar, Navigation, MainLayout)
├── Business/Controller Layer
│   ├── Business Logic (Payment validation, amount validation, idempotency key generation)
│   ├── Custom Hooks (usePayment, useRefund, usePaymentMethods, usePaymentHistory)
│   └── Service Functions (Card validation, amount formatting, idempotency key generation)
├── Payment Integration Layer
│   ├── Payment Gateway SDK (Secure payment processing)
│   ├── Tokenization (Tokenize payment methods for secure storage)
│   └── Payment Flow (Payment initiation, confirmation, status updates)
├── State Management
│   ├── Client State
│   │   ├── Local State (useState) - Component-specific UI state
│   │   ├── Global State (Redux Toolkit) - Payment methods, transaction history, user preferences
│   │   └── Context API - User authentication, theme preferences, app-wide payment settings
│   └── Server State
│       ├── React Query (useQuery/useMutation) - Payment data caching, transaction history, refetching, optimistic updates
│       └── Service Worker - Offline caching for payment history
├── API Integration
│   ├── API Client (Axios with interceptors for auth, error handling, retry logic)
│   ├── API Services (paymentService, refundService, paymentMethodService)
│   └── Request/Response Transformation (Payment data normalization, error handling, idempotency key injection)
└── Routing
    ├── Public Routes (Home)
    ├── Protected Routes (Payment, History, Settings)
    └── Route Guards (Authentication and authorization checks)

```

**Frontend Deployment:**

- **Build**: Production bundle with code splitting and lazy loading using Webpack/Vite
- **CDN**: Static assets served from CloudFront/Cloudflare edge locations for fast global delivery
- **Caching**: Aggressive caching for static assets, cache-busting for updates
- **Environment**: Environment variables for API endpoints and payment gateway keys

**Key Frontend Components:**

- **React 19 Application**:
  - Single-page application with client-side routing
  - Component-based architecture for reusability
  - React Query with React 19 hooks (useOptimistic, useTransition, useActionState)
  - Secure payment form with tokenization via payment gateway SDK
  - Responsive design for mobile and desktop
  - Modern React 19 features for better performance and UX

- **CDN/Edge**:
  - Global distribution of static assets
  - Edge caching for improved performance
  - DDoS protection and rate limiting at edge

**Trade-offs:**

- **Layered Architecture**: Provides clear separation of concerns and maintainability, but can add complexity for simple payments - works great for complex payment systems with multiple gateways
- **Business/Controller Layer**: Centralizes payment logic and makes it testable, but requires careful design to avoid over-engineering - essential for complex payment validation and processing
- **State Management Separation**: Client and server state separation improves performance and caching, but requires understanding when to use each - React Query for payment data, Redux for payment form state

## f) App Flow

### Complete System Flow (Frontend Perspective)

**Primary User Flow - Payment Processing:**

1. **User lands on checkout page** → React Router renders CheckoutPage component
2. **User enters payment details** → PaymentForm component captures card details via secure payment gateway SDK
3. **Card validation** → Payment gateway SDK validates card in real-time
4. **Idempotency key generation** → usePayment hook generates unique idempotency key
5. **Form submission** → PaymentForm triggers React Query mutation with useActionState (React 19)
6. **Loading state** → SubmitButton shows loading spinner, form disabled
7. **Payment processing** → useMutation sends POST request to /api/v1/payments with idempotency key
8. **Optimistic update** → useOptimistic (React 19) shows payment as processing immediately
9. **Success response** → React Query caches response, ReceiptView component renders
10. **State update** → Components re-render with payment confirmation data

**Component Interaction Flow:**

```

User Enters Card → PaymentForm (secure gateway SDK)
            ↓
Card Validation → PaymentGateway SDK (real-time validation)
            ↓
Form Submit → PaymentForm (React Query mutation with useActionState)
            ↓
Idempotency Key → usePayment hook (generates unique key)
            ↓
API Call → paymentService (business logic)
            ↓
Response → React Query cache update
            ↓
Re-render → ReceiptView (receives cached payment data)

```

**State Update Flow:**

1. **Local State** → PaymentForm uses useState for form inputs
2. **Form State** → useActionState (React 19) manages form submission state
3. **Optimistic State** → useOptimistic (React 19) shows payment as processing before confirmation
4. **Server State** → React Query manages payment data, transaction history, caching, refetching
5. **Global State** → Redux Toolkit manages selected payment method, payment preferences
6. **Component Re-render** → React updates UI based on state changes

**Error Handling Flow:**

1. **Payment Error** → React Query mutation returns error
2. **Error Boundary** → Catches component errors, shows fallback UI
3. **User Feedback** → Toast notification displays error message with retry option
4. **Retry Logic** → User can retry failed payment with same idempotency key (prevents duplicate charges)
5. **Fraud Detection** → System blocks suspicious transactions, shows appropriate error

**Payment Status Update Flow:**

1. **Webhook received** → Payment gateway sends webhook for status update
2. **Status update** → React Query refetches payment data
3. **UI update** → PaymentStatus component updates to show new status
4. **Notification** → Toast notification confirms status change

**Refund Flow:**

1. **User initiates refund** → RefundRequest component opens
2. **Refund amount input** → User enters refund amount (partial or full)
3. **Refund submission** → useRefund hook triggers React Query mutation
4. **Optimistic update** → useOptimistic (React 19) shows refund as processing
5. **Confirmation** → Refund confirmation displayed, payment history updated

**Payment Method Management Flow:**

1. **User adds payment method** → PaymentMethodForm component opens
2. **Card tokenization** → Payment gateway SDK tokenizes card securely
3. **Save payment method** → usePaymentMethods hook saves tokenized card
4. **Payment method list** → PaymentMethodList component displays saved methods
5. **Set default** → User can set default payment method
6. **Delete method** → User can remove saved payment methods

# 3) Component Architecture

Think of the frontend as a tree of React components - each component handles a specific part of the UI, and they work together to create the complete user experience.

**Component Hierarchy:**

```

App
├── Layout
│   ├── Header
│   │   ├── Logo
│   │   ├── Navigation
│   │   └── UserMenu
│   ├── MainContent
│   └── Footer
├── Pages
│   ├── CheckoutPage
│   │   ├── PaymentForm
│   │   │   ├── CardInput (Payment Gateway SDK)
│   │   │   ├── ExpiryInput
│   │   │   ├── CVVInput
│   │   │   └── SubmitButton
│   │   └── PaymentSummary
│   ├── PaymentHistoryPage
│   │   ├── PaymentHistoryList
│   │   │   └── TransactionCard
│   │   └── PaymentFilters
│   ├── PaymentMethodPage
│   │   ├── PaymentMethodList
│   │   │   └── PaymentMethodCard
│   │   └── PaymentMethodForm
│   ├── RefundPage
│   │   └── RefundRequest
│   └── ReceiptPage
│       └── ReceiptView
└── SharedComponents
    ├── Button
    ├── Input
    ├── Card
    ├── Toast
    ├── LoadingSpinner
    └── Modal

```

**Key React Components:**

**1. PaymentForm Component:**

- Handles secure payment form submission
- Integrates with payment gateway SDK (Stripe.js, PayPal SDK)
- Manages form state with useActionState (React 19)
- Generates idempotency key for duplicate prevention
- Uses useOptimistic (React 19) for instant UI feedback
- Validates payment details before submission

**2. PaymentMethodCard Component:**

- Displays saved payment method (masked card number)
- Handles set as default functionality
- Allows deletion of payment methods
- Shows payment method type and expiry

**3. TransactionCard Component:**

- Displays transaction details (amount, status, date)
- Shows payment method used
- Handles refund request initiation
- Links to receipt view

**4. RefundRequest Component:**

- Handles refund amount input
- Validates refund amount (cannot exceed payment amount)
- Processes refund with React Query mutation
- Shows refund status and confirmation

**5. PaymentHistoryList Component:**

- Displays list of transactions with virtual scrolling
- Fetches payment history with React Query useSuspenseQuery (React 19)
- Handles pagination and filtering
- Uses useTransition (React 19) for non-urgent filter updates

**6. ReceiptView Component:**

- Displays payment receipt details
- Shows transaction ID, amount, payment method
- Provides download receipt functionality
- Handles print receipt

**Component Communication:**

- **Props** → Parent to child data flow
- **Callbacks** → Child to parent communication
- **Context API** → Shared state across components (theme, user)
- **React Query** → Server state management (payments, transaction history)
- **Redux Toolkit** → Global client state (selected payment method, payment preferences)
- **Payment Gateway SDK** → Secure payment processing and tokenization

# 4) Data Models

### TypeScript Interfaces

```typescript
interface Payment {
  id: string;
  orderId: string;
  amount: number;
  currency: string;
  status: "pending" | "processing" | "succeeded" | "failed" | "refunded";
  paymentMethod: PaymentMethod;
  gatewayTransactionId?: string;
  processedAt?: string;
  createdAt: string;
}

interface PaymentMethod {
  id: string;
  type: "card" | "wallet" | "bank_transfer";
  card?: {
    last4: string;
    brand: string;
    expiryMonth: number;
    expiryYear: number;
  };
  isDefault: boolean;
  createdAt: string;
}

interface Refund {
  id: string;
  paymentId: string;
  amount: number;
  reason?: string;
  status: "pending" | "processing" | "succeeded" | "failed";
  createdAt: string;
}

interface Transaction {
  id: string;
  type: "payment" | "refund";
  amount: number;
  currency: string;
  status: string;
  paymentMethod: PaymentMethod;
  createdAt: string;
}

interface PaymentRequest {
  orderId: string;
  amount: number;
  currency: string;
  paymentMethod: "card" | "wallet" | "bank_transfer";
  paymentDetails: {
    cardToken?: string;
    walletId?: string;
    bankAccountId?: string;
  };
  idempotencyKey: string;
}

interface FormState {
  cardNumber: string;
  expiryMonth: string;
  expiryYear: string;
  cvv: string;
  errors: {
    cardNumber?: string;
    expiry?: string;
    cvv?: string;
  };
}

```

# 5) API Design

### POST /api/v1/payments

- **URL:** `/api/v1/payments`
- **Method:** POST
- **Description:** Process a payment
- **Headers:**
 - `Idempotency-Key`(optional) - Unique key to prevent duplicate charges
- **Request Body:**

 ```json
 {
 "orderId": "order_abc123",
 "amount": 100.00,
 "currency": "USD",
 "paymentMethod": "card",
 "paymentDetails": {
 "cardToken": "tok_visa_1234"
 }
 }

 ```

- **Response:**

 ```json
 {
 "success": true,
 "data": {
 "paymentId": "payment_abc123",
 "orderId": "order_abc123",
 "amount": 100.00,
 "status": "succeeded",
 "gatewayTransactionId": "txn_xyz789",
 "processedAt": "2024-01-15T10:30:00Z"
 }
 }

 ```

- **Status Codes:** 201 (Created), 400 (Validation Error), 402 (Payment Failed), 409 (Duplicate Payment)

### POST /api/v1/payments/:paymentId/refund

- **URL:** `/api/v1/payments/:paymentId/refund`
- **Method:** POST
- **Description:** Process a refund
- **Request Body:**

 ```json
 {
 "amount": 100.00,
 "reason": "Customer request"
 }

 ```

- **Response:**

 ```json
 {
 "success": true,
 "data": {
 "refundId": "refund_abc123",
 "paymentId": "payment_abc123",
 "amount": 100.00,
 "status": "processing",
 "createdAt": "2024-01-15T10:30:00Z"
 }
 }

 ```

- **Status Codes:** 201 (Created), 400 (Validation Error), 404 (Payment Not Found)

### POST /api/v1/webhooks/payment

- **URL:** `/api/v1/webhooks/payment`
- **Method:** POST
- **Description:** Payment gateway webhook endpoint
- **Headers:**
 - `X-Signature`(required) - HMAC-SHA256 signature
- **Request Body:**

 ```json
 {
 "event": "payment.succeeded",
 "data": {
 "paymentId": "payment_abc123",
 "status": "succeeded",
 "gatewayTransactionId": "txn_xyz789"
 }
 }

 ```

- **Response:**

 ```json
 {
 "success": true,
 "message": "Webhook processed"
 }

 ```

- **Status Codes:** 200 (Success), 401 (Invalid Signature), 400 (Invalid Payload)

### GET /api/v1/payments

- **URL:** `/api/v1/payments?page=1&limit=20&status=succeeded`
- **Method:** GET
- **Description:** Get payment history
- **Query Parameters:**
  - `page` (default: 1) - Page number
  - `limit` (default: 20) - Results per page
  - `status` (optional) - Filter by payment status
  - `startDate` (optional) - Filter by start date
  - `endDate` (optional) - Filter by end date
- **Response:**

  ```json
  {
    "success": true,
    "data": {
      "payments": [
        {
          "id": "payment_abc123",
          "orderId": "order_abc123",
          "amount": 100.00,
          "currency": "USD",
          "status": "succeeded",
          "paymentMethod": {
            "type": "card",
            "card": {
              "last4": "4242",
              "brand": "visa"
            }
          },
          "createdAt": "2024-01-15T10:30:00Z"
        }
      ],
      "total": 125,
      "page": 1,
      "limit": 20
    }
  }
  ```

- **Status Codes:** 200 (Success)

### GET /api/v1/payments/:paymentId

- **URL:** `/api/v1/payments/:paymentId`
- **Method:** GET
- **Description:** Get payment details
- **Response:**

  ```json
  {
    "success": true,
    "data": {
      "id": "payment_abc123",
      "orderId": "order_abc123",
      "amount": 100.00,
      "currency": "USD",
      "status": "succeeded",
      "paymentMethod": {
        "id": "pm_123",
        "type": "card",
        "card": {
          "last4": "4242",
          "brand": "visa",
          "expiryMonth": 12,
          "expiryYear": 2025
        }
      },
      "gatewayTransactionId": "txn_xyz789",
      "processedAt": "2024-01-15T10:30:00Z",
      "createdAt": "2024-01-15T10:30:00Z"
    }
  }
  ```

- **Status Codes:** 200 (Success), 404 (Payment Not Found)

### GET /api/v1/payment-methods

- **URL:** `/api/v1/payment-methods`
- **Method:** GET
- **Description:** Get saved payment methods
- **Response:**

  ```json
  {
    "success": true,
    "data": {
      "paymentMethods": [
        {
          "id": "pm_123",
          "type": "card",
          "card": {
            "last4": "4242",
            "brand": "visa",
            "expiryMonth": 12,
            "expiryYear": 2025
          },
          "isDefault": true,
          "createdAt": "2024-01-15T10:30:00Z"
        }
      ]
    }
  }
  ```

- **Status Codes:** 200 (Success)

### POST /api/v1/payment-methods

- **URL:** `/api/v1/payment-methods`
- **Method:** POST
- **Description:** Save a payment method
- **Request Body:**

  ```json
  {
    "type": "card",
    "cardToken": "tok_visa_1234",
    "isDefault": false
  }
  ```

- **Response:**

  ```json
  {
    "success": true,
    "data": {
      "id": "pm_123",
      "type": "card",
      "card": {
        "last4": "4242",
        "brand": "visa",
        "expiryMonth": 12,
        "expiryYear": 2025
      },
      "isDefault": false,
      "createdAt": "2024-01-15T10:30:00Z"
    }
  }
  ```

- **Status Codes:** 201 (Created), 400 (Validation Error)

---

# 6) Protocols

### REST API Protocol

**Request Format:**

- HTTP methods: GET, POST, PUT, DELETE
- Headers: Content-Type: application/json
- Authentication: Bearer token in Authorization header
- Idempotency: Idempotency-Key header for payment requests

**Response Format:**

- Success: `{ success: true, data: {...} }`
- Error: `{ success: false, error: {...} }`
- Status codes: 200 (Success), 201 (Created), 400 (Bad Request), 401 (Unauthorized), 402 (Payment Failed), 404 (Not Found), 409 (Duplicate Payment), 500 (Server Error)

**Error Response Format:**

```json
{
  "success": false,
  "error": {
    "code": "PAYMENT_FAILED",
    "message": "Payment processing failed",
    "details": "Insufficient funds"
  }
}

```

**Authentication:**

- Bearer token authentication for protected routes
- Token stored in httpOnly cookie
- Automatic token refresh on 401 responses
- Redirect to login on authentication failure

**Idempotency:**

- Idempotency-Key header required for payment requests
- Prevents duplicate charges for same payment
- Key must be unique per payment request
- Server returns same response for duplicate requests

**Request Headers:**

```

Content-Type: application/json
Authorization: Bearer <token>
Idempotency-Key: <unique-key>
Accept: application/json

```

**Response Headers:**

```

Content-Type: application/json
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1640995200

```

**Payment Gateway Integration:**

- Payment gateway SDK (Stripe.js, PayPal SDK) handles secure card input
- Tokenization: Card details tokenized client-side, never sent to backend
- Webhooks: Payment gateway sends webhooks for status updates
- Signature verification: Webhook signatures verified using HMAC-SHA256

---

# 7) Low Level Design (LLD)

## ii) State Management

### Client State

**Local State (useState):**

- Component-specific UI state (form inputs, modal visibility, loading states)
- Example: `const [isOpen, setIsOpen] = useState(false);`

**Global State:**

- Redux Toolkit for complex global state (selected payment method, payment preferences)
- Context API for user authentication, theme preferences
- Example: Payment method selection, payment preferences, transaction filters

### Server State

**React Query (TanStack Query):**

- `useQuery` for data fetching and caching
- `useMutation` for data mutations (payment, refund, save payment method)
- `useSuspenseQuery` (React 19) for better loading states
- Automatic refetching, background updates, optimistic updates
- Example: Payment history caching, payment status synchronization

**State Management for Payment System:**

**Client State Examples (React 19):**

```typescript
import { useState, useActionState, useOptimistic, useTransition } from 'react';

// Payment form state with useActionState (React 19)
const [formState, formAction, isPending] = useActionState(
  async (prevState: FormState, formData: FormData) => {
    // Process payment
    return { ...prevState, errors: {} };
  },
  { cardNumber: '', expiryMonth: '', expiryYear: '', cvv: '', errors: {} }
);

// Payment status with optimistic updates (React 19)
const [optimisticPayments, addOptimisticPayment] = useOptimistic(
  [] as Payment[],
  (currentPayments, newPayment: Payment) => [...currentPayments, newPayment]
);

// UI state with transition (React 19)
const [isPending, startTransition] = useTransition();

```

**Server State with React Query (React 19):**

```typescript
import { use, useTransition } from 'react';
import { useQuery, useMutation, useSuspenseQuery } from '@tanstack/react-query';

// Fetch payment history with Suspense (React 19)
const { data: payments } = useSuspenseQuery({
  queryKey: ['payments', filters],
  queryFn: () => fetchPayments(filters),
  staleTime: 30000 // 30 seconds
});

// Payment mutation with optimistic updates
const paymentMutation = useMutation({
  mutationFn: processPayment,
  onMutate: async (newPayment) => {
    await queryClient.cancelQueries({ queryKey: ['payments'] });
    const previousPayments = queryClient.getQueryData(['payments']);
    queryClient.setQueryData(['payments'], (old: Payment[]) => [...old, newPayment]);
    return { previousPayments };
  },
  onError: (err, newPayment, context) => {
    queryClient.setQueryData(['payments'], context?.previousPayments);
  }
});

// Using use() hook for promise handling (React 19)
function PaymentReceipt({ paymentPromise }: { paymentPromise: Promise<Payment> }) {
  const payment = use(paymentPromise);
  return <ReceiptView payment={payment} />;
}

```

**Global State (Redux Toolkit):**

```typescript
// Payment method slice
const paymentMethodSlice = createSlice({
  name: 'paymentMethod',
  initialState: null as PaymentMethod | null,
  reducers: {
    setPaymentMethod: (state, action) => action.payload,
    clearPaymentMethod: () => null
  }
});

// Payment preferences slice
const paymentPreferencesSlice = createSlice({
  name: 'paymentPreferences',
  initialState: {
    defaultCurrency: 'USD',
    savePaymentMethods: true
  },
  reducers: {
    updatePreferences: (state, action) => {
      return { ...state, ...action.payload };
    }
  }
});

```

## iii) Implementation Details

### Business/Controller Layer

**Custom Hooks:**

- Encapsulate business logic and API calls
- Example: `usePayment`, `useRefund`, `usePaymentMethods`, `usePaymentHistory`
- Handle data transformation and validation

**Service Functions:**

- Pure functions for data processing and validation
- Card validation, amount formatting, idempotency key generation
- Reusable across components

### Advanced Component Patterns

**Compound Components:**

- Group related components together (e.g., PaymentForm.CardInput, PaymentForm.SubmitButton)
- Share implicit state between components

**Render Props Pattern:**

- Pass render functions as props for flexible component composition

**Custom Hooks Pattern:**

- Extract reusable logic into custom hooks
- Example: `usePayment`, `useRefund`, `useCardValidation`, `useIdempotencyKey`

**Higher-Order Components (HOCs):**

- Wrap components with additional functionality
- Example: `withPaymentAccess`, `withPaymentGateway`

### Performance Optimizations (React 19)

- **Code splitting** with React.lazy() and Suspense (React 19 improves Suspense)
- **Memoization** with useMemo() and useCallback()
- **useDeferredValue()** for deferring non-urgent payment operations (React 19)
- **useTransition()** for marking non-urgent state updates (React 19)
- **Virtual scrolling** for long transaction lists (react-window, react-virtuoso)
- **Debouncing and throttling** for form inputs
- **React.memo** for preventing unnecessary re-renders
- **useOptimistic()** for instant UI feedback on payment operations (React 19)

### UI/UX Enhancements

- **Toast notifications** for user feedback (react-hot-toast)
- **Loading states** and skeleton screens
- **Error boundaries** for error handling
- **Responsive design** for mobile and desktop
- **Accessibility features** (ARIA labels, keyboard navigation, focus management)
- **Animations** with Framer Motion or CSS transitions
- **Payment gateway SDK** for secure card input

### Code Examples

**Custom Hook: usePayment (React 19)**

```typescript
import { useOptimistic, useActionState } from 'react';
import { useMutation } from '@tanstack/react-query';

function usePayment() {
  const [optimisticPayments, addOptimisticPayment] = useOptimistic(
    [] as Payment[],
    (currentPayments, newPayment: Payment) => [...currentPayments, newPayment]
  );

  return useMutation({
    mutationFn: async (paymentData: PaymentRequest) => {
      addOptimisticPayment({ ...paymentData, status: 'processing' } as Payment);
      return await processPayment(paymentData);
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['payments'] });
    }
  });
}

```

**Component with React Query (React 19):**

```typescript
function PaymentForm() {
  const [formState, formAction, isPending] = useActionState(
    async (prevState: FormState, formData: FormData) => {
      const cardToken = await stripe.createToken(cardElement);
      return await processPayment({
        cardToken: cardToken.id,
        idempotencyKey: generateIdempotencyKey()
      });
    },
    { cardNumber: '', errors: {} }
  );

  return (
    <form action={formAction}>
      <CardInput />
      <SubmitButton disabled={isPending} />
    </form>
  );
}

```

**Idempotency Key Generation:**

```typescript
function generateIdempotencyKey(): string {
  return `${Date.now()}-${Math.random().toString(36).substring(2, 15)}`;
}

```

**Card Validation:**

```typescript
function validateCardNumber(cardNumber: string): boolean {
  // Luhn algorithm
  const digits = cardNumber.replace(/\D/g, '');
  let sum = 0;
  let isEven = false;

  for (let i = digits.length - 1; i >= 0; i--) {
    let digit = parseInt(digits[i]);
    if (isEven) {
      digit *= 2;
      if (digit > 9) digit -= 9;
    }
    sum += digit;
    isEven = !isEven;
  }

  return sum % 10 === 0;
}

```

## iv) Testing

### Component Testing

- React Testing Library for component tests
- Test user interactions and component behavior
- Example: Test payment form submission, card validation, refund request

### Integration Testing

- Test component interactions
- Test API integration with mock data
- Test state management flows

### E2E Testing

- Playwright or Cypress for end-to-end tests
- Test complete user flows
- Example: Test payment flow from start to finish

**Payment System Specific Tests:**

**Component Test: PaymentForm**

```typescript
test('validates card number', async () => {
  render(<PaymentForm />);
  const cardInput = screen.getByLabelText('Card Number');
  fireEvent.change(cardInput, { target: { value: '4242424242424242' } });
  await waitFor(() => {
    expect(screen.queryByText(/invalid card/i)).not.toBeInTheDocument();
  });
});

test('generates idempotency key on submit', async () => {
  render(<PaymentForm />);
  const submitButton = screen.getByText('Pay');
  fireEvent.click(submitButton);
  await waitFor(() => {
    expect(mockProcessPayment).toHaveBeenCalledWith(
      expect.objectContaining({
        idempotencyKey: expect.any(String)
      })
    );
  });
});

```

**Integration Test: Payment Flow**

```typescript
test('complete payment flow', async () => {
  render(<App />);
  fireEvent.change(screen.getByLabelText('Card Number'), {
    target: { value: '4242424242424242' }
  });
  fireEvent.click(screen.getByText('Pay'));
  await waitFor(() => {
    expect(screen.getByText(/payment successful/i)).toBeInTheDocument();
  });
});

```

**E2E Test: Complete Payment Journey**

```typescript
test('user can make payment and view receipt', async ({ page }) => {
  await page.goto('/checkout');
  await page.fill('input[name="cardNumber"]', '4242424242424242');
  await page.fill('input[name="expiry"]', '12/25');
  await page.fill('input[name="cvv"]', '123');
  await page.click('button[type="submit"]');
  await page.waitForSelector('text=/payment successful/i');
  await expect(page.locator('text=/receipt/i')).toBeVisible();
});

```

# 8) Algorithms

### Frontend Algorithms

**Idempotency Key Generation Algorithm:**

```javascript
function generateIdempotencyKey() {
  return `${Date.now()}-${Math.random().toString(36).substring(2, 15)}-${crypto.randomUUID()}`;
}

```

**Card Number Validation (Luhn Algorithm):**

```javascript
function validateCardNumber(cardNumber) {
  const digits = cardNumber.replace(/\D/g, '');
  let sum = 0;
  let isEven = false;

  for (let i = digits.length - 1; i >= 0; i--) {
    let digit = parseInt(digits[i]);
    if (isEven) {
      digit *= 2;
      if (digit > 9) digit -= 9;
    }
    sum += digit;
    isEven = !isEven;
  }

  return sum % 10 === 0 && digits.length >= 13 && digits.length <= 19;
}

```

**Card Number Formatting:**

```javascript
function formatCardNumber(cardNumber) {
  const digits = cardNumber.replace(/\D/g, '');
  const formatted = digits.match(/.{1,4}/g)?.join(' ') || digits;
  return formatted.substring(0, 19); // Max 19 characters (16 digits + 3 spaces)
}

```

**Amount Formatting:**

```javascript
function formatAmount(amount, currency = 'USD') {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: currency
  }).format(amount);
}

```

**Expiry Date Validation:**

```javascript
function validateExpiryDate(month, year) {
  const currentDate = new Date();
  const currentYear = currentDate.getFullYear() % 100;
  const currentMonth = currentDate.getMonth() + 1;

  if (year < currentYear) return false;
  if (year === currentYear && month < currentMonth) return false;
  if (month < 1 || month > 12) return false;

  return true;
}

```

**CVV Validation:**

```javascript
function validateCVV(cvv, cardType) {
  const digits = cvv.replace(/\D/g, '');
  if (cardType === 'amex') {
    return digits.length === 4;
  }
  return digits.length === 3;
}

```

# 9) Security

### Frontend Security

**Input Validation:**

- Client-side validation before payment submission
- Validate card number using Luhn algorithm
- Validate expiry date, CVV format
- Sanitize payment form inputs

**PCI-DSS Compliance:**

- Never store full card numbers
- Use payment gateway SDK for secure card input
- Tokenize card details client-side
- Never log sensitive payment data

**XSS Prevention:**

- React automatically escapes content
- Use `dangerouslySetInnerHTML` only when necessary with sanitization
- Content Security Policy (CSP) headers
- Sanitize payment data before displaying

**CSRF Protection:**

- SameSite cookies for authentication
- CSRF tokens for state-changing operations
- Verify origin header on API requests

**Secure Storage:**

- Never store card details in localStorage or sessionStorage
- Use httpOnly cookies for authentication tokens
- Clear sensitive data on logout
- Tokenize payment methods for secure storage

**HTTPS:**

- All API calls over HTTPS
- Enforce HTTPS in production
- HSTS headers for security

**Rate Limiting (Client-Side):**

- Debounce payment API calls to prevent abuse
- Show user-friendly messages when rate limited
- Implement exponential backoff for retries
- Limit payment attempts per session

**Payment System Specific Security:**

**Card Number Masking:**

```typescript
function maskCardNumber(cardNumber: string): string {
  const digits = cardNumber.replace(/\D/g, '');
  if (digits.length < 4) return cardNumber;
  const last4 = digits.slice(-4);
  return `**** **** **** ${last4}`;
}

```

**Idempotency Key Storage:**

```typescript
// Store idempotency keys in sessionStorage to prevent duplicate payments
function storeIdempotencyKey(orderId: string, key: string): void {
  sessionStorage.setItem(`idempotency_${orderId}`, key);
}

function getIdempotencyKey(orderId: string): string | null {
  return sessionStorage.getItem(`idempotency_${orderId}`);
}

```

**Payment Data Sanitization:**

```typescript
function sanitizePaymentData(data: PaymentRequest): PaymentRequest {
  return {
    ...data,
    // Remove any sensitive fields that shouldn't be sent
    paymentDetails: {
      cardToken: data.paymentDetails.cardToken,
      // Never send full card number
    }
  };
}

```

# 10) Deployment and DevOps

### Frontend Deployment

**Build Optimization:**

- Production build with code splitting and tree shaking
- Minification and compression
- Asset optimization (images, fonts)
- Environment variables for API endpoints and payment gateway keys

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

**Payment System Deployment Configuration:**

**Environment Variables:**

```bash
VITE_API_URL=https://api.payment.example.com
VITE_STRIPE_PUBLIC_KEY=pk_test_...
VITE_PAYPAL_CLIENT_ID=...
VITE_ENABLE_PAYMENT_GATEWAY=true

```

**Build Configuration (vite.config.ts):**

```typescript
export default defineConfig({
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          'react-vendor': ['react', 'react-dom', 'react-router-dom'],
          'query-vendor': ['@tanstack/react-query'],
          'redux-vendor': ['@reduxjs/toolkit'],
          'payment-vendor': ['@stripe/stripe-js']
        }
      }
    }
  }
});

```

**CDN Configuration:**

- Static assets cached for 1 year
- HTML files cached for 5 minutes
- Cache busting via query parameters for updates
- Gzip/Brotli compression enabled

**Monitoring Setup:**

- Track payment success rate
- Monitor API response times
- Alert on error rate spikes (> 5%)
- Track payment analytics (successful payments, refunds, failed payments)

# 11) Interview Answers (Frontend Focus)

### Q: How would you handle state management for this system?

**Answer (STAR Method):**

**Situation:** In a payment system, we need to manage payment forms, transaction history, payment methods, and ensure idempotency to prevent duplicate charges.

**Action:**

- Use React Query for server state (payment history, payment methods) - handles caching, refetching, and synchronization
- Use `useOptimistic()` (React 19) for instant UI feedback on payment operations
- Use `useActionState()` (React 19) for payment form handling with built-in form state management
- Use `useTransition()` (React 19) for non-urgent payment history updates
- Use Redux Toolkit for global client state (selected payment method, payment preferences)
- Use useState for local component state (form inputs, modal visibility)
- Use Context API for user authentication, theme preferences

**Result:** Reduced API calls through caching, improved performance with optimistic updates, better user experience with instant feedback, prevented duplicate charges through idempotency.

**Takeaway:** Separating client and server state management leads to cleaner code and better performance. React 19's useActionState is perfect for payment forms, and useOptimistic provides instant feedback.

### Q: How would you prevent duplicate charges?

**Answer (STAR Method):**

**Situation:** Users might accidentally submit payment forms multiple times, leading to duplicate charges.

**Action:**

- Generate unique idempotency key for each payment request
- Store idempotency key in sessionStorage to reuse on retry
- Send idempotency key in request header to backend
- Disable submit button immediately after first submission
- Use `useActionState()` (React 19) to prevent multiple form submissions
- Show loading state during payment processing
- Backend uses idempotency key to return same response for duplicate requests

**Result:** Zero duplicate charges, improved user experience, reliable payment processing.

**Takeaway:** Idempotency keys are essential for payment systems - they prevent duplicate charges while allowing safe retries.

### Q: How would you ensure PCI-DSS compliance?

**Answer (STAR Method):**

**Situation:** Payment systems must comply with PCI-DSS standards for secure card data handling.

**Action:**

- Use payment gateway SDK (Stripe.js, PayPal SDK) for secure card input
- Never store full card numbers in frontend
- Tokenize card details client-side before sending to backend
- Never log sensitive payment data
- Use HTTPS for all API calls
- Implement Content Security Policy (CSP) headers
- Mask card numbers when displaying (show only last 4 digits)
- Clear sensitive data from memory after use

**Result:** PCI-DSS compliant payment processing, secure card data handling, reduced security risks.

**Takeaway:** Payment gateway SDKs handle PCI-DSS compliance - never handle raw card data in frontend.

### Q: How would you handle payment failures gracefully?

**Answer (STAR Method):**

**Situation:** Payment processing can fail due to various reasons (insufficient funds, network issues, gateway errors).

**Action:**

- Use `useOptimistic()` (React 19) to show payment as processing, then update on failure
- Display user-friendly error messages based on error codes
- Provide retry functionality with same idempotency key
- Show specific error messages (insufficient funds, card declined, network error)
- Implement exponential backoff for retries
- Allow user to update payment method and retry
- Log errors for debugging without exposing sensitive data

**Result:** Better user experience during failures, reduced support tickets, improved payment success rate.

**Takeaway:** Graceful error handling with clear messages and retry options improves payment success rates.
