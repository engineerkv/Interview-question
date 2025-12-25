# Payment System

## Overview

Design a secure payment processing system that handles payments through payment gateways, supports multiple payment methods, and ensures secure, reliable transactions with fraud detection.

---

## 1) Requirements

### Functional Requirements

**Core Features:**
- Process payments (credit cards, debit cards, wallets, UPI)
- Payment gateway integration (Stripe, PayPal, Razorpay, etc.)
- Payment method management (save, update, delete payment methods)
- Payment history with filtering and search
- Refund processing
- Payment status tracking (real-time updates)
- Receipt generation and download
- Payment analytics dashboard

**Security Features:**
- PCI-DSS compliant payment form handling
- Payment method tokenization (don't store raw card data)
- Idempotency (prevent duplicate charges)
- Fraud detection and blocking

### Non-Functional Requirements

**Performance:**
- Payment processing: < 2 seconds
- Fast payment history retrieval
- Low-latency status updates

**Reliability:**
- 99.99% reliability
- Zero duplicate charges (idempotency)
- Handle payment gateway failures gracefully

**Security:**
- PCI-DSS compliance
- Secure payment data handling
- Fraud detection mechanisms
- Encrypted data transmission

**User Experience:**
- Responsive design (mobile and desktop)
- Accessible payment forms
- Clear error messages
- Payment confirmation

---

## 2) Component Hierarchy

The frontend is a React application with secure payment processing. Here's the structure:

```
App
├── Layout
│   ├── Header
│   │   ├── Logo
│   │   └── UserMenu
│   └── MainContent
├── Pages
│   ├── CheckoutPage
│   │   ├── OrderSummary (items, total, shipping)
│   │   ├── PaymentForm
│   │   │   ├── PaymentMethodSelector (Card, UPI, Wallet)
│   │   │   ├── CardInput (via payment gateway SDK)
│   │   │   │   ├── CardNumber (secure input)
│   │   │   │   ├── ExpiryDate
│   │   │   │   ├── CVV
│   │   │   │   └── CardholderName
│   │   │   ├── UPIPayment (UPI ID input)
│   │   │   ├── WalletSelector (Paytm, PhonePe, etc.)
│   │   │   ├── SavedPaymentMethods (show saved cards)
│   │   │   └── SubmitButton
│   │   └── PaymentStatus (processing, success, error)
│   ├── PaymentHistoryPage
│   │   ├── PaymentFilters (date range, status, amount)
│   │   ├── PaymentList
│   │   │   └── PaymentCard
│   │   │       ├── TransactionId
│   │   │       ├── Amount
│   │   │       ├── Status
│   │   │       ├── Date
│   │   │       └── Actions (View Receipt, Refund)
│   │   └── Pagination
│   ├── PaymentMethodPage
│   │   ├── PaymentMethodList
│   │   │   └── PaymentMethodCard
│   │   │       ├── CardInfo (last 4 digits, brand)
│   │   │       ├── ExpiryDate
│   │   │       └── Actions (Set Default, Delete)
│   │   └── AddPaymentMethodButton
│   └── ReceiptPage
│       ├── ReceiptView (transaction details)
│       └── DownloadButton
└── SharedComponents
    ├── PaymentGatewaySDK (Stripe, Razorpay integration)
    ├── Toast
    └── LoadingSpinner
```

### Key Components Explained

**1. PaymentForm Component**
- Main payment form with payment gateway SDK integration
- Handles card input securely (never touches raw card data)
- Validates payment details in real-time
- Generates idempotency key to prevent duplicate charges
- Uses useActionState (React 19) for form handling

**2. CardInput Component**
- Secure card input using payment gateway SDK
- Payment gateway SDK handles card validation
- Tokenizes card data (returns token, not raw card number)
- PCI-DSS compliant (no card data touches our servers)

**3. PaymentMethodSelector Component**
- Allows selecting payment method (Card, UPI, Wallet)
- Shows saved payment methods
- Handles different payment flows for each method

**4. PaymentHistory Component**
- Displays payment history with filtering
- Shows payment status, amount, date
- Actions: view receipt, request refund
- Real-time status updates via polling or WebSocket

**5. PaymentMethodManager Component**
- Manages saved payment methods
- Add, update, delete payment methods
- Set default payment method
- Shows masked card information

---

## 3) Data Models

Here are the key data structures:

```typescript
// Payment transaction
interface Payment {
  id: string;
  orderId: string;
  amount: number;
  currency: string;
  status: "pending" | "processing" | "completed" | "failed" | "refunded";
  paymentMethod: PaymentMethod;
  paymentGateway: string;  // "stripe", "razorpay", etc.
  transactionId: string;  // Gateway transaction ID
  idempotencyKey: string;  // Prevents duplicate charges
  createdAt: string;
  updatedAt: string;
  receiptUrl?: string;
  refundAmount?: number;
  refundReason?: string;
}

// Payment method
interface PaymentMethod {
  id: string;
  type: "card" | "upi" | "wallet" | "netbanking";
  // For cards
  last4?: string;  // Last 4 digits
  brand?: string;  // "visa", "mastercard", etc.
  expiryMonth?: number;
  expiryYear?: number;
  // For UPI
  upiId?: string;
  // For wallets
  walletType?: string;  // "paytm", "phonepe", etc.
  isDefault: boolean;
  token: string;  // Tokenized payment method ID
}

// Payment request
interface PaymentRequest {
  orderId: string;
  amount: number;
  currency: string;
  paymentMethodId?: string;  // For saved payment methods
  paymentMethodToken?: string;  // For new payment methods (from gateway)
  idempotencyKey: string;
  metadata?: Record<string, string>;  // Additional data
}

// Payment response
interface PaymentResponse {
  success: boolean;
  data: {
    paymentId: string;
    status: string;
    transactionId: string;
    receiptUrl?: string;
  };
  error?: {
    code: string;  // "INSUFFICIENT_FUNDS", "CARD_DECLINED", etc.
    message: string;
  };
}

// Refund request
interface RefundRequest {
  paymentId: string;
  amount?: number;  // Partial refund, omit for full refund
  reason: string;
}

// Payment analytics
interface PaymentAnalytics {
  totalRevenue: number;
  totalTransactions: number;
  successRate: number;
  averageTransactionAmount: number;
  paymentsByMethod: Array<{
    method: string;
    count: number;
    amount: number;
  }>;
  paymentsByStatus: Array<{
    status: string;
    count: number;
  }>;
}
```

### Data Flow Explanation

**When a user makes a payment:**
1. User enters payment details in PaymentForm
2. Payment gateway SDK validates and tokenizes card data
3. Frontend generates unique idempotency key
4. Submit payment request with token and idempotency key
5. Server processes payment via payment gateway
6. Payment status updates in real-time
7. On success, show receipt and confirmation

**Idempotency flow:**
1. Frontend generates idempotency key (UUID) before payment
2. Key is sent with payment request
3. Server checks if payment with this key already exists
4. If exists, returns existing payment (prevents duplicate charge)
5. If new, processes payment and stores key

**Payment method tokenization:**
1. User enters card details in secure gateway SDK input
2. Gateway SDK validates and tokenizes card
3. Frontend receives token (not raw card data)
4. Token is sent to server for payment
5. Token can be saved for future payments (with user consent)

**Refund flow:**
1. User requests refund from PaymentHistory
2. User enters refund amount (partial or full) and reason
3. Refund request sent to server
4. Server processes refund via payment gateway
5. Payment status updates to "refunded"
6. User receives confirmation

---

## 4) API Design

### REST Endpoints

**POST /api/v1/payments**
- Process a payment
- Request body: PaymentRequest with idempotency key
- Returns: PaymentResponse
- Status codes: 200 (Success), 400 (Invalid Request), 402 (Payment Failed)

**GET /api/v1/payments**
- Get payment history
- Query params: `page`, `limit`, `status`, `startDate`, `endDate`
- Returns: Paginated list of Payment objects

**GET /api/v1/payments/:id**
- Get payment details
- Returns: Payment object

**POST /api/v1/payments/:id/refund**
- Process a refund
- Request body: RefundRequest
- Returns: Updated Payment object

**GET /api/v1/payments/:id/receipt**
- Get payment receipt
- Returns: Receipt PDF download

**GET /api/v1/payment-methods**
- Get saved payment methods
- Returns: Array of PaymentMethod objects

**POST /api/v1/payment-methods**
- Add a payment method
- Request body: PaymentMethod with token
- Returns: PaymentMethod object

**DELETE /api/v1/payment-methods/:id**
- Delete a payment method
- Returns: Success confirmation

**GET /api/v1/payments/analytics**
- Get payment analytics
- Query params: `startDate`, `endDate`
- Returns: PaymentAnalytics object

### API Request/Response Examples

**Process Payment:**
```json
// POST /api/v1/payments
{
  "orderId": "order_123",
  "amount": 99.99,
  "currency": "USD",
  "paymentMethodToken": "tok_abc123",  // From payment gateway
  "idempotencyKey": "idemp_xyz789"
}

// Response
{
  "success": true,
  "data": {
    "paymentId": "pay_123",
    "status": "completed",
    "transactionId": "txn_abc456",
    "receiptUrl": "https://api.example.com/receipts/pay_123.pdf"
  }
}
```

**Get Payment History:**
```json
// GET /api/v1/payments?page=1&limit=20&status=completed
// Response
{
  "success": true,
  "data": {
    "payments": [
      {
        "id": "pay_123",
        "orderId": "order_123",
        "amount": 99.99,
        "currency": "USD",
        "status": "completed",
        "paymentMethod": {
          "type": "card",
          "last4": "4242",
          "brand": "visa"
        },
        "createdAt": "2024-01-15T10:00:00Z"
      }
    ],
    "total": 150,
    "page": 1,
    "limit": 20
  }
}
```

**Process Refund:**
```json
// POST /api/v1/payments/pay_123/refund
{
  "amount": 50.00,  // Partial refund, omit for full
  "reason": "Customer requested refund"
}

// Response
{
  "success": true,
  "data": {
    "id": "pay_123",
    "status": "refunded",
    "refundAmount": 50.00,
    "refundReason": "Customer requested refund"
  }
}
```

**Error Response:**
```json
{
  "success": false,
  "error": {
    "code": "CARD_DECLINED",
    "message": "Your card was declined",
    "details": "Insufficient funds"
  }
}
```

---

## Key Design Decisions

**1. Payment Gateway SDK Integration**
- Use payment gateway SDK (Stripe, Razorpay) for card input
- SDK handles PCI-DSS compliance
- Card data never touches our servers
- Returns tokenized payment method

**2. Idempotency for Duplicate Prevention**
- Generate unique idempotency key before payment
- Server checks for existing payment with same key
- Prevents duplicate charges on retry
- Critical for reliability

**3. Payment Method Tokenization**
- Store tokenized payment methods (not raw card data)
- Tokens can be reused for future payments
- More secure than storing card numbers
- Reduces PCI-DSS scope

**4. Real-time Status Updates**
- Poll payment status or use WebSocket
- Update UI when payment status changes
- Better user experience
- Handle async payment processing

**5. Optimistic Updates**
- Show payment as processing immediately
- Use useOptimistic (React 19) for instant feedback
- Rollback if payment fails
- Better perceived performance

**6. Error Handling**
- Clear error messages for different failure types
- Retry logic for transient failures
- Fraud detection blocking
- User-friendly error display

---

## Interview Talking Points

**When explaining this system, I'd focus on:**

1. **Requirements First**: Start with core functionality - secure payment processing, multiple payment methods, refunds

2. **Component Structure**: Explain the React component hierarchy - payment form, payment method selector, payment history

3. **Data Models**: Walk through Payment, PaymentMethod, PaymentRequest - and idempotency key importance

4. **API Design**: Show the REST endpoints - process payment, refund, payment history, payment methods

5. **Key Challenges**: 
   - PCI-DSS compliance (never store raw card data)
   - Idempotency to prevent duplicate charges
   - Payment gateway integration and error handling
   - Real-time payment status updates
   - Fraud detection and blocking

**Example explanation flow:**
> "So for a payment system, the core requirement is processing payments securely through payment gateways. The frontend uses a payment gateway SDK (like Stripe) for card input - this is critical for PCI-DSS compliance because the SDK handles card data securely and never sends raw card numbers to our servers. Instead, it returns a tokenized payment method. When processing a payment, we generate an idempotency key to prevent duplicate charges - if the same key is used twice, the server returns the existing payment instead of charging again. The data model includes Payment objects with status tracking, PaymentMethod objects for saved payment methods (tokenized), and PaymentRequest with the idempotency key. The main API endpoints handle payment processing, refunds, payment history, and payment method management. Key challenges include ensuring PCI-DSS compliance, implementing idempotency correctly, handling payment gateway failures gracefully, and providing real-time status updates."
