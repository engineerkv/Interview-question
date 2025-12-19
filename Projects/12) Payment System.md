# Payment System

> **Project Type:** Full-Stack Web Application (MERN Stack)
> **Scale:** Handle 1B+ transactions per day, 99.99% reliability, fraud detection
> **Tech Stack:** React.js, Node.js, Express.js, MongoDB/PostgreSQL, Redis, Payment Gateway SDKs

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

## a) Requirements

### i) Functional Requirements

- Process payments (credit cards, debit cards, wallets)

- Payment gateway integration

- Refund processing

- Payment history

- Fraud detection

- Webhook handling

### ii) Non-Functional Requirements

- Payment processing < 2 seconds

- 99.99% reliability

- PCI-DSS compliance

- Idempotency (prevent duplicate charges)

---

## b) Scope and Priority

### Phase 1: MVP (Must Have) - Priority 1

- Core functionality

- Basic features

### Phase 2: Enhanced Features - Priority 2

- Additional capabilities

- Performance improvements

### Phase 2: Enhanced Features - Priority 2

- Multiple payment gateways support

- Advanced fraud detection

- Payment analytics and reporting

- Recurring payments and subscriptions

- Payment method management

---

## c) Technology Choices

### Backend Framework

- **Node.js with Express.js** - Fast, secure backend for payment processing

### Payment Gateway

- **Payment Gateway Integration** - Secure payment processing via payment gateway

### Database

- **SQL Database** - ACID compliance for transaction data

- **Redis** - Idempotency keys and transaction state

### Additional Services

- **Message Queue** - For async payment processing and webhooks

- **Webhook Handler** - Process payment status updates

---

## e) Architecture Overview

The system follows a secure payment processing architecture with idempotency, fraud detection, and distributed transaction management. Here's how the complete system works:

### Frontend Architecture

**Frontend Layers:**

1. **Presentation Layer (React Components)**
 - **UI Components**: Reusable components (PaymentForm, PaymentMethodCard, TransactionCard, ReceiptView)
 - **Feature Components**: PaymentProcessor, PaymentHistory, RefundRequest, PaymentMethodManager
 - **Layout Components**: Header, Sidebar, Navigation, MainLayout
 - **Page Components**: PaymentPage, HistoryPage, SettingsPage

2. **State Management Layer**
 - **Local State (useState)**: Component-specific UI state (form inputs, loading, errors, payment status)
 - **Server State (Redux Toolkit)**: Global state for transactions, payment methods, user
 - **API State (React Query)**: Transaction data caching, refetching, optimistic updates

3. **Payment Integration Layer**
 - **Payment Gateway SDK**: Payment gateway SDK integration for secure payment processing
 - **Tokenization**: Tokenize payment methods for secure storage
 - **Payment Flow**: Handle payment initiation, confirmation, and status updates

4. **API Integration Layer**
 - **API Client**: Axios instance with interceptors for auth, error handling
 - **Redux Thunks**: Async actions for API operations (processPayment, getPaymentHistory, processRefund)
 - **Request/Response Transformation**: Data normalization and error handling

5. **Routing Layer (React Router)**
 - **Route Configuration**: Define routes and protected routes
 - **Navigation**: Programmatic and declarative navigation
 - **Route Guards**: Authentication and authorization checks

6. **Build & Deployment Layer**
 - **Build Process**: Webpack/Vite bundling with code splitting
 - **Static Assets**: Served from CDN (CloudFront/Cloudflare)
 - **Environment Configuration**: Environment-specific API endpoints and payment gateway keys

**Frontend Request Flow:**

1. **User Interaction** → User initiates payment or views payment history
2. **State Update** → Redux action dispatched or React Query mutation triggered
3. **API Call** → Axios makes HTTP request to backend API with idempotency key
4. **Loading State** → UI shows loading indicator
5. **Response Handling** → Success/error state updates Redux store or React Query cache
6. **UI Update** → Components re-render with payment status

### Backend Architecture

**Backend Layers:**

1. **API Gateway/Load Balancer** - Entry point for all HTTP requests
2. **API Server Layer** - Stateless servers handling HTTP requests
3. **Payment Processing Layer** - Workers for async payment processing
4. **Webhook Handler Layer** - Process payment gateway webhooks
5. **Fraud Detection Layer** - ML-based fraud detection service
6. **Application Service Layer** - Business logic and orchestration
7. **Cache Layer** - In-memory caching for performance
8. **Database Layer** - Persistent data storage with ACID compliance
9. **Payment Gateway Layer** - Integration with multiple payment gateways

### Complete Request Flow

**Payment Processing Flow:**

1. **Frontend**: User initiates payment, sends payment request with idempotency key
2. **API Call**: POST request to payment API with payment details and idempotency key
3. **Idempotency Check**: Check Redis for existing transaction with same idempotency key
4. **Fraud Detection**: Analyze transaction for fraud risk
5. **Payment Gateway**: Process payment via payment gateway
6. **Database**: Create transaction record with status
7. **Webhook**: Payment gateway sends webhook with payment status
8. **Update**: Update transaction status based on webhook
9. **Response**: Return payment status to frontend
10. **Frontend**: Show payment confirmation or error

**Webhook Processing Flow:**

1. **Payment Gateway**: Sends webhook with payment status update
2. **Webhook Handler**: Receive and validate webhook signature
3. **Idempotency Check**: Check if webhook already processed
4. **Database**: Update transaction status
5. **Notification**: Notify user of payment status change
6. **Response**: Send acknowledgment to payment gateway

**Refund Processing Flow:**

1. **Frontend**: User requests refund
2. **API Call**: POST request to refund API
3. **Validation**: Validate refund eligibility
4. **Payment Gateway**: Process refund via payment gateway
5. **Database**: Update transaction status to "refunded"
6. **Response**: Return refund confirmation
7. **Frontend**: Show refund confirmation

### Key Components

- **Frontend (React.js)**: Single-page application with payment gateway SDK integration, component-based architecture, Redux for state management, secure payment form handling
- **Load Balancer**: Distributes HTTP traffic across API servers, SSL/TLS termination
- **API Servers**: Stateless design for horizontal scaling, handle payment requests, refund requests, payment history
- **Payment Processing Workers**: Async workers for payment processing, handle payment gateway communication
- **Webhook Handlers**: Process payment gateway webhooks, update transaction status
- **Fraud Detection Service**: ML-based fraud detection, analyze transaction patterns, block suspicious transactions
- **Application Services**: Payment Service, Refund Service, Fraud Detection Service, Webhook Service
- **Cache Layer (Redis)**: In-memory cache for idempotency keys, payment methods, transaction status
- **Database (PostgreSQL)**: ACID-compliant database for transaction storage, ensures data consistency
- **Payment Gateways**: Multiple payment gateway providers with failover support

---

# 3) Low Level Design (LLD)

---

## Component Architecture

### Payment Service

```javascript
class PaymentService {
 async processPayment(paymentData: PaymentRequest){
 // Validate payment data
 // Check idempotency
 // Create payment record
 // Call payment gateway
 // Update payment status
 // Return payment result
 }

 async refundPayment(paymentId, amount){
 // Validate refund request
 // Create refund record
 // Call payment gateway refund API
 // Update refund status
 // Return refund result
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
│ ├── Logo
│ ├── Navigation
│ └── UserMenu (Profile, Settings, Sign out)
├── MainContent
│ ├── PaymentFormPage
│ │ ├── PaymentAmount
│ │ ├── PaymentMethodSelector
│ │ │ ├── SavedCards
│ │ │ ├── CardInput
│ │ │ ├── WalletOptions
│ │ │ └── UPIInput
│ │ ├── PaymentForm
│ │ │ ├── CardNumberInput
│ │ │ ├── ExpiryDateInput
│ │ │ ├── CVVInput
│ │ │ ├── CardholderNameInput
│ │ │ └── SaveCardCheckbox
│ │ ├── BillingAddressForm
│ │ └── PayButton
│ ├── PaymentStatusPage
│ │ ├── PaymentStatusIndicator
│ │ ├── TransactionDetails
│ │ │ ├── TransactionId
│ │ │ ├── Amount
│ │ │ ├── PaymentMethod
│ │ │ └── Timestamp
│ │ └── ActionButtons
│ │ ├── DownloadReceipt
│ │ └── RetryPayment (if failed)
│ ├── PaymentHistoryPage
│ │ ├── FilterBar
│ │ │ ├── DateRangeFilter
│ │ │ ├── StatusFilter
│ │ │ └── PaymentMethodFilter
│ │ ├── TransactionList
│ │ │ └── TransactionCard
│ │ │ ├── TransactionInfo
│ │ │ ├── Amount
│ │ │ ├── Status
│ │ │ └── ViewDetailsButton
│ │ └── Pagination
│ └── PaymentMethodsPage
│ ├── SavedCardsList
│ │ └── SavedCardItem
│ │ ├── CardInfo
│ │ └── DeleteButton
│ └── AddPaymentMethodButton
└── PaymentGatewayProvider (Payment SDK integration)

```

### Key React Components

**Frontend Implementation:**

```javascript
// Payment Form Component
const PaymentForm<{ amount; onSuccess: (transactionId) => void }> = ({
 amount,
 onSuccess
}) => {
 const [paymentMethod, setPaymentMethod] = useState('card');
 const [cardData, setCardData] = useState({ number: '', expiry: '', cvv: '', name: '' });
 const processPaymentMutation = useProcessPayment();

 const handleSubmit = async (e) => {
 e.preventDefault();

 processPaymentMutation.mutate({
 amount,
 paymentMethod,
 cardData: paymentMethod === 'card' ? cardData : undefined
 }, {
 onSuccess: (data) => {
 onSuccess(data.transactionId);
 }
 });
 };

 return (
 <form onSubmit={handleSubmit} className="payment-form">
 <PaymentMethodSelector
 selected={paymentMethod}
 onSelect={setPaymentMethod}
 />
 {paymentMethod === 'card' && (
 <CardInput
 value={cardData}
 onChange={setCardData}
 />
 )}
 <BillingAddressForm />
 <button
 type="submit"
 disabled={processPaymentMutation.isLoading}
 >
 {processPaymentMutation.isLoading ? 'Processing...' : `Pay $${amount}`}
 </button>
 </form>
 );
};

// Transaction Card Component
const TransactionCard<{ transaction: Transaction }> = ({ transaction }) => {
 return (
 <div className="transaction-card">
 <div className="transaction-info">
 <div className="transaction-id">#{transaction.id}</div>
 <div className="transaction-date">{formatDate(transaction.createdAt)}</div>
 </div>
 <div className="transaction-amount">${transaction.amount}</div>
 <div className={`transaction-status ${transaction.status}`}>
 {transaction.status}
 </div>
 <button onClick={() => navigate(`/transactions/${transaction.id}`)}>
 View Details
 </button>
 </div>
 );
};

```

### ii) State Management

**State Management Strategy (React 19):**

- **Local State (useState)**: Form inputs, UI state (loading, errors, selected payment method)
- **Optimistic Updates (useOptimistic)**: React 19 hook for optimistic payment processing
- **Form Actions (useActionState)**: React 19 hook for payment forms with server actions
- **Transitions (useTransition)**: React 19 hook for non-urgent payment status updates
- **API State**: React Query for server state (transactions, payment methods) - caching, refetching
- **Global State (Redux Toolkit)**: User authentication, saved payment methods, active payment session

**Frontend Implementation:**

```javascript
// Using React Query for API state management
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

const useProcessPayment = () => {
 const queryClient = useQueryClient();

 return useMutation({
 mutationFn: async (paymentData: PaymentRequest) => {
 const response = await axios.post('/api/v1/payments', paymentData);
 return response.data;
 },
 onSuccess: (data) => {
 // Invalidate transactions list
 queryClient.invalidateQueries({ queryKey: ['transactions'] });
 // Navigate to payment status page
 navigate(`/payments/${data.transactionId}/status`);
 }
 });
};

const useTransactions = (filters?: TransactionFilters) => {
 return useQuery({
 queryKey: ['transactions', filters],
 queryFn: async () => {
 const response = await axios.get('/api/v1/transactions', { params: filters });
 return response.data;
 },
 staleTime: 30 * 1000 // Cache for 30 seconds
 });
};

```

### iii) Advanced Payment Patterns with React 19

**Payment Processing with React 19:**

```javascript
import { useActionState, useFormStatus, useOptimistic, useTransition } from 'react';

// React 19: Server Action for payment processing
async function processPaymentAction(
 prevState: { error?; transactionId?},
 formData: FormData
) {
 const paymentData = {
 amount: parseFloat(formData.get('amount') as string),
 paymentMethod: formData.get('paymentMethod') as string,
 cardData: formData.get('cardData') ? JSON.parse(formData.get('cardData') as string) : undefined,
 idempotencyKey: crypto.randomUUID()
 };

 try {
 const payment = await processPaymentAPI(paymentData);
 return { success: true, transactionId: payment.paymentId };
 } catch (error: any) {
 return { error: error.message || 'Payment failed. Please try again.' };
 }
}

const PayButton= () => {
 const { pending } = useFormStatus(); // React 19 hook

 return (
 <button type="submit" disabled={pending}>
 {pending ? 'Processing...' : 'Pay'}
 </button>
 );
};

const PaymentForm<{ amount; onSuccess: (transactionId) => void }> = ({
 amount,
 onSuccess
}) => {
 const [paymentMethod, setPaymentMethod] = useState('card');
 const [cardData, setCardData] = useState({ number: '', expiry: '', cvv: '', name: '' });
 const [isPending, startTransition] = useTransition();

 // React 19: useActionState for payment form
 const [state, formAction] = useActionState(processPaymentAction, {});

 // React 19: useOptimistic for payment status
 const [optimisticStatus, setOptimisticStatus] = useOptimistic(
 'pending',
 (state, newStatus) => newStatus
 );

 const handleSubmit = (formData: FormData) => {
 formData.append('amount', amount.toString());
 formData.append('paymentMethod', paymentMethod);
 if (paymentMethod === 'card') {
 formData.append('cardData', JSON.stringify(cardData));
 }

 // Optimistically set status
 startTransition(() => {
 setOptimisticStatus('processing');
 });

 formAction(formData);
 };

 useEffect(() => {
 if (state.success && state.transactionId) {
 setOptimisticStatus('succeeded');
 onSuccess(state.transactionId);
 } else if (state.error) {
 setOptimisticStatus('failed');
 }
 }, [state, onSuccess]);

 return (
 <form action={handleSubmit} className="payment-form">
 <PaymentMethodSelector
 selected={paymentMethod}
 onSelect={setPaymentMethod}
 />
 {paymentMethod === 'card' && (
 <CardInput
 value={cardData}
 onChange={setCardData}
 />
 )}
 <BillingAddressForm />
 <div className={`payment-status ${optimisticStatus}`}>
 Status: {optimisticStatus}
 </div>
 {state.error && <span className="error">{state.error}</span>}
 <PayButton />
 </form>
 );
};
```

**Transaction History with React 19:**

```javascript
import { useDeferredValue, useTransition } from 'react';

const TransactionHistoryPage= () => {
 const [filters, setFilters] = useState({});
 const [isPending, startTransition] = useTransition();

 // React 19: useDeferredValue for filter debouncing
 const deferredFilters = useDeferredValue(filters);

 const { data: transactions } = useQuery({
 queryKey: ['transactions', deferredFilters],
 queryFn: () => fetchTransactions(deferredFilters),
 staleTime: 30 * 1000
 });

 const handleFilterChange = (newFilters: TransactionFilters) => {
 setFilters(newFilters);
 startTransition(() => {
 // Filter updates are lower priority
 });
 };

 return (
 <div className="transaction-history">
 <FilterBar
 filters={filters}
 onChange={handleFilterChange}
 />
 {isPending && <span>Loading...</span>}
 <TransactionList transactions={transactions || []} />
 </div>
 );
};
```

**Saved Payment Methods with React 19:**

```javascript
import { useOptimistic, useTransition } from 'react';

const SavedPaymentMethods= () => {
 const [methods, setMethods] = useState([]);
 const [isPending, startTransition] = useTransition();

 // React 19: useOptimistic for payment method deletion
 const [optimisticMethods, removeOptimisticMethod] = useOptimistic(
 methods,
 (state, methodId) => state.filter(m => m.id !== methodId)
 );

 const handleDelete = async (methodId) => {
 // Optimistically remove
 startTransition(() => {
 removeOptimisticMethod(methodId);
 });

 try {
 await deletePaymentMethodAPI(methodId);
 } catch (error) {
 // Rollback on error
 setMethods(methods);
 }
 };

 return (
 <div className="saved-methods">
 {optimisticMethods.map(method => (
 <SavedCardItem
 key={method.id}
 method={method}
 onDelete={() => handleDelete(method.id)}
 />
 ))}
 </div>
 );
};
```

### iv) Implementation Details

**Data Flow:**

1. **Payment Initiation** → User fills payment form with React 19 useActionState, submits payment request optimistically
2. **Payment Processing** → Backend processes payment via payment gateway, status updates optimistically with useOptimistic
3. **Payment Status** → Payment status updates via webhook or polling with React 19 transitions
4. **Transaction History** → User views past transactions with filters using useDeferredValue for debouncing
5. **Payment Methods** → User manages saved payment methods with optimistic updates

**Event Handling:**

- Payment form submission triggers payment processing with React 19 form actions
- Payment gateway callbacks update payment status optimistically
- Webhook events update transaction status in real-time with transitions
- Saved payment methods load from user profile with React Query
- Transaction filters update transaction list with useDeferredValue

**UI/UX Considerations:**

- **Loading States**: Spinner during payment processing, skeleton loaders for transaction list, loading indicators
- **Error Handling**: User-friendly error messages, handle payment failures gracefully, retry options
- **Validation**: Client-side validation for card details, expiry dates, CVV with React 19 form validation
- **Responsive Design**: Mobile-first layout, optimized for touch interactions, adaptive forms
- **Accessibility**: ARIA labels, keyboard navigation, screen reader support, focus management
- **Security**: PCI-DSS compliance, secure card input handling, tokenization, no sensitive data in state

---

## Data Models

### Payment Model

```javascript
// Payment structure:
//
 paymentId;
 orderId;
 amount;
 currency;
 status: 'pending' | 'processing' | 'succeeded' | 'failed' | 'refunded';
 paymentMethod: PaymentMethod;
 gatewayTransactionId?;
 idempotencyKey;
 metadata?: Record<string, any>;
 createdAt;
 updatedAt;
 completedAt?;

// PaymentMethod structure:
//
 type: 'card' | 'upi' | 'netbanking' | 'wallet';
 cardNumber?;
 expiryMonth?;
 expiryYear?;
 cvv?;
 cardholderName?;

```

---

## Data APIs

### POST /api/v1/payments

- **URL:** `/api/v1/payments`

- **Method:** POST

- **Request Body:**

 ```json
 {
 "amount": 100.50,
 "currency": "USD",
 "orderId": "order_abc123",
 "paymentMethod": {
 "type": "card",
 "cardNumber": "4111111111111111",
 "expiryMonth": 12,
 "expiryYear": 2025,
 "cvv": "123",
 "cardholderName": "John Doe"
 },
 "idempotencyKey": "unique_key_123"
 }

 ```

- **Response:**

 ```json
 {
 "success": true,
 "data": {
 "paymentId": "pay_abc123",
 "status": "processing",
 "amount": 100.50,
 "currency": "USD",
 "orderId": "order_abc123",
 "createdAt": "2024-01-15T10:30:00Z"
 }
 }

 ```

- **Status Codes:** 201 (Created), 400 (Validation Error), 409 (Duplicate - Idempotency Key)

### GET /api/v1/payments/:paymentId

- **URL:** `/api/v1/payments/:paymentId`

- **Method:** GET

- **Response:**

 ```json
 {
 "success": true,
 "data": {
 "paymentId": "pay_abc123",
 "status": "succeeded",
 "amount": 100.50,
 "currency": "USD",
 "orderId": "order_abc123",
 "gatewayTransactionId": "txn_xyz789",
 "createdAt": "2024-01-15T10:30:00Z",
 "completedAt": "2024-01-15T10:30:05Z"
 }
 }

 ```

- **Status Codes:** 200 (Success), 404 (Not Found)

### POST /api/v1/payments/:paymentId/refund

- **URL:** `/api/v1/payments/:paymentId/refund`

- **Method:** POST

- **Request Body:**

 ```json
 {
 "amount": 50.25,
 "reason": "Customer request"
 }

 ```

- **Response:**

 ```json
 {
 "success": true,
 "data": {
 "refundId": "refund_abc123",
 "paymentId": "pay_abc123",
 "amount": 50.25,
 "status": "processing",
 "createdAt": "2024-01-15T11:00:00Z"
 }
 }

 ```

- **Status Codes:** 201 (Created), 400 (Validation Error), 404 (Not Found)

### POST /api/v1/webhooks/payment-gateway

- **URL:** `/api/v1/webhooks/payment-gateway`

- **Method:** POST

- **Description:** Webhook endpoint for payment gateway callbacks

- **Request Body:**

 ```json
 {
 "event": "payment.succeeded",
 "data": {
 "paymentId": "pay_abc123",
 "status": "succeeded",
 "gatewayTransactionId": "txn_xyz789"
 },
 "signature": "webhook_signature"
 }

 ```

- **Response:**

 ```json
 {
 "success": true,
 "message": "Webhook processed"
 }

 ```

- **Status Codes:** 200 (Success), 400 (Invalid Signature), 401 (Unauthorized)

---

## b) Backend

*Note: Backend implementation details are kept minimal. Focus is on frontend integration.*

**API Endpoints Reference:**

- `POST /api/v1/payments` - Process payment (requires idempotency key header)
- `GET /api/v1/payments/:paymentId` - Get payment details
- `GET /api/v1/transactions` - Get transaction history
- `POST /api/v1/payments/verify` - Verify payment
- `POST /api/v1/payments/:paymentId/refund` - Process refund
- `GET /api/v1/payment-methods` - Get saved payment methods
- `POST /api/v1/payment-methods` - Save payment method
- `DELETE /api/v1/payment-methods/:id` - Delete payment method

**Webhook Events:**

- `payment.captured` - Payment successfully captured
- `payment.failed` - Payment failed
- `payment.refunded` - Payment refunded

---

### Express.js Server Structure

```

server/
├── routes/
├── controllers/
├── services/
└── models/

```

### Service Implementation

```javascript
class Service {
 async processRequest(data: any) {
 // Implementation details
 }
}

```

---

## Payment Flow

1. Client initiates payment

2. Generate idempotency key

3. Create payment record (pending)

4. Call payment gateway

5. Update payment status

6. Send webhook to merchant

7. Update order status

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

### Payment Processing Flow

**Frontend Implementation:** React component handles payment form and checkout flow
**Backend Implementation:** Express.js service processes payments with idempotency and webhook handling

- **Strategy:** Idempotent payment processing - like ensuring the same payment isn't processed twice, uses idempotency keys

- **Webhook Handling:** Async payment status updates via webhooks from payment gateway

**Backend (Express.js):**

```javascript
// Backend: services/PaymentService.ts
import PaymentGateway from 'payment-gateway-sdk';
import crypto from 'crypto';

class PaymentService {
 private paymentGateway: PaymentGateway;

 constructor() {
 this.paymentGateway = new PaymentGateway({
 key_id: process.env.PAYMENT_GATEWAY_KEY_ID!,
 key_secret: process.env.PAYMENT_GATEWAY_KEY_SECRET!
 });
 }

 async processPayment(paymentData: PaymentRequest){
 // Check idempotency - prevent duplicate payments
 const existingPayment = await Payment.findOne({
 idempotencyKey: paymentData.idempotencyKey
 });

 if (existingPayment) {
 return existingPayment; // Return existing payment
 }

 // Create payment record with pending status
 const payment = await Payment.create({
 orderId: paymentData.orderId,
 amount: paymentData.amount,
 currency: paymentData.currency,
 status: 'pending',
 idempotencyKey: paymentData.idempotencyKey,
 paymentMethod: paymentData.paymentMethod
 });

 try {
 // Call payment gateway
 const gatewayOrder = await this.paymentGateway.orders.create({
 amount: paymentData.amount * 100, // Convert to smallest currency unit
 currency: paymentData.currency,
 receipt: payment.paymentId
 });

 // Update payment with gateway order ID
 payment.gatewayOrderId = gatewayOrder.id;
 payment.status = 'processing';
 await payment.save();

 return payment;
 } catch (error) {
 // Update payment status to failed
 payment.status = 'failed';
 payment.errorMessage = error.message;
 await payment.save();
 throw error;
 }
 }

 async handleWebhook(webhookData: any, signature){
 // Verify webhook signature
 const expectedSignature = crypto
 .createHmac('sha256', process.env.PAYMENT_GATEWAY_WEBHOOK_SECRET!)
 .update(JSON.stringify(webhookData))
 .digest('hex');

 if (signature !== expectedSignature) {
 throw new Error('Invalid webhook signature');
 }

 // Process webhook event
 if (webhookData.event === 'payment.captured') {
 const payment = await Payment.findOne({
 gatewayTransactionId: webhookData.payload.payment.entity.id
 });

 if (payment) {
 payment.status = 'succeeded';
 payment.gatewayTransactionId = webhookData.payload.payment.entity.id;
 payment.completedAt = new Date();
 await payment.save();

 // Update order status
 await Order.updateOne(
 { orderId: payment.orderId },
 { $set: { status: 'paid' } }
 );
 }
 }
 }
}

```

**Frontend Implementation:**

```javascript
// React component for payment form
import { useState } from 'react';
import { useMutation } from '@tanstack/react-query';
import axios from 'axios';
import { loadPaymentGateway } from '../utils/paymentGateway';

const PaymentForm<{ orderId; amount}> = ({ orderId, amount }) => {
 const [cardData, setCardData] = useState({
 cardNumber: '',
 expiryMonth: '',
 expiryYear: '',
 cvv: '',
 cardholderName: ''
 });

 const { mutate: processPayment, isLoading } = useMutation({
 mutationFn: async (paymentData: any) => {
 // Generate idempotency key
 const idempotencyKey = `${orderId}-${Date.now()}`;

 // Create payment
 const response = await axios.post('/api/v1/payments', {
 ...paymentData,
 idempotencyKey
 });

 // Initialize payment gateway checkout
 const paymentGateway = await loadPaymentGateway();
 const options = {
 key: process.env.REACT_APP_PAYMENT_GATEWAY_KEY_ID,
 amount: amount * 100,
 currency: 'INR',
 name: 'My Company',
 description: `Payment for Order ${orderId}`,
 order_id: response.data.data.gatewayOrderId,
 handler: async (response: any) => {
 // Payment successful
 await axios.post('/api/v1/payments/verify', {
 paymentId: response.data.paymentId,
 gatewayPaymentId: response.gateway_payment_id,
 gatewayOrderId: response.gateway_order_id,
 gatewaySignature: response.gateway_signature
 });
 },
 prefill: {
 name: cardData.cardholderName
 }
 };

 const gatewayInstance = new paymentGateway(options);
 gatewayInstance.open();

 return response.data;
 },
 onError: (error) => {
 console.error('Payment failed:', error);
 }
 });

 const handleSubmit = (e) => {
 e.preventDefault();
 processPayment({
 orderId,
 amount,
 paymentMethod: {
 type: 'card',
 ...cardData
 }
 });
 };

 return (
 <form onSubmit={handleSubmit}>
 {/* Payment form fields */}
 <button type="submit" disabled={isLoading}>
 {isLoading ? 'Processing...' : 'Pay Now'}
 </button>
 </form>
 );
};

```

### Idempotency and Webhook Handling

**Frontend Implementation:** React component handles payment status polling
**Backend Implementation:** Express.js handles idempotency keys and webhook verification

- **Strategy:** Idempotency keys prevent duplicate payments - same key returns same result

- **Webhook Verification:** Verify webhook signatures to ensure authenticity

**Backend (Express.js):**

```javascript
// Backend: middleware/idempotency.ts
export const idempotencyMiddleware = async (req: Request, res: Response, next: NextFunction) => {
 const idempotencyKey = req.headers['idempotency-key'] as string;

 if (!idempotencyKey) {
 return res.status(400).json({ error: 'Idempotency key required' });
 }

 // Check if request was already processed
 const existingResult = await IdempotencyKey.findOne({ key: idempotencyKey });

 if (existingResult) {
 // Return cached response
 return res.status(existingResult.statusCode).json(existingResult.response);
 }

 // Store original res.json
 const originalJson = res.json.bind(res);

 // Override res.json to cache response
 res.json = function(body: any) {
 IdempotencyKey.create({
 key: idempotencyKey,
 statusCode: res.statusCode,
 response: body
 });

 return originalJson(body);
 };

 next();
};

```

### Error Handling

**Error Scenarios:**

- **Payment Gateway Errors:** Handle payment gateway failures, network timeouts, invalid responses - retry with exponential backoff, log for investigation

- **Transaction Failures:** Handle insufficient funds, card declined, expired cards - show user-friendly error messages, suggest alternative payment methods

- **Idempotency Errors:** Handle duplicate payment requests - return existing transaction result, prevent double charging

- **Webhook Failures:** Handle webhook delivery failures - retry with exponential backoff, store in dead letter queue after max retries

---

## Testing Strategy

### Frontend Testing (React.js)

**Unit Testing:**

- **Jest + React Testing Library** - Test components, payment form, checkout flow

- **Payment Component Testing** - Test payment form validation, card input, error handling

- **Mocking:** Mock API calls, payment gateway SDK

**Integration Testing:**

- **Payment Flow** - Test complete payment process

- **Payment Gateway Integration** - Test payment gateway SDK integration

- **API Integration Tests** - Test API calls with mock server

**E2E Testing:**

- **Cypress / Playwright** - Test payment flows

- **Test Scenarios:** Process payment, handle payment failures, refund processing

### Backend Testing (Node.js/Express.js)

**Unit Testing:**

- **Jest + Supertest** - Test API endpoints, payment processing

- **Payment Gateway Testing** - Test payment gateway integration

- **Mocking:** Mock database, payment gateway, Redis

**Integration Testing:**

- **MongoDB Memory Server** - Test database operations

- **Redis Mock** - Test idempotency keys

- **Payment Gateway Mock** - Test payment gateway responses

**Load Testing:**

- **Artillery / k6** - Test payment processing under high load

- **Concurrent Payments:** Test performance with multiple simultaneous payments

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

- **Health Checks:** Verify payment endpoints

### Database Deployment

**MongoDB/PostgreSQL Setup:**

- **Managed Database Service** - MongoDB Atlas / AWS RDS

- **Backup Strategy:** Daily automated backups, point-in-time recovery

- **Transaction Logs:** Maintain transaction logs for audit

**Redis Setup:**

- **Redis Cloud / AWS ElastiCache** - Managed Redis service

- **Idempotency Keys:** Store idempotency keys in Redis

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
PAYMENT_GATEWAY_WEBHOOK_SECRET=whsec_xxx

```

---

## Database Migrations & Seeding

### MongoDB/PostgreSQL Migrations

**Migration Scripts:**

- **Schema Changes:** Add indexes for transaction queries

- **Data Migrations:** Update transaction formats

- **Index Optimization:** Add compound indexes for payment queries

### Data Seeding

**Seed Data:**

- **Test Transactions:** Seed test transactions

- **Payment Methods:** Seed test payment methods

---

## API Documentation

### Swagger/OpenAPI

**API Documentation:**

- **Swagger UI:** Document REST APIs

- **Payment API:** Document payment endpoints

- **Webhook API:** Document webhook endpoints

---

## API Versioning

**Versioning Strategy:**

- **URL Versioning:** `/api/v1/payments`, `/api/v2/payments`

- **Header Versioning:** `Accept: application/vnd.api+json;version=1`

- **Backward Compatibility:** Maintain old API versions for existing clients

---

## Monitoring & Logging

### Application Monitoring

**Frontend:**

- **Error Tracking:** Sentry for payment errors

- **Performance:** Track payment processing times

- **User Analytics:** Track payment success rates

**Backend:**

- **APM:** Monitor payment processing performance

- **Payment Gateway Monitoring:** Track payment gateway response times

- **Payment Metrics:** Track transaction volume, success rates, failures

### Logging

**Structured Logging:**

- **Winston / Pino:** Log payment operations

- **Payment Events:** Log payment initiation, processing, completion, failures

- **Error Logging:** Detailed error logs with context (no sensitive data)

---

## Database Transactions & Consistency

### MongoDB/PostgreSQL Transactions

**Transaction Usage:**

- **Multi-Document Transactions** - For operations requiring ACID guarantees

- **Example:** Payment creation + balance update + transaction log

- **Session Management:** Use database sessions for transaction control

**Example:**

```javascript
const session = await mongoose.startSession();
session.startTransaction();
try {
 await Payment.create([paymentData], { session });
 await Wallet.updateOne({ userId }, { $inc: { balance: -amount } }, { session });
 await TransactionLog.create([logData], { session });
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

- **Payment Consistency:** Use transactions for payment operations

- **Idempotency:** Use idempotency keys to prevent duplicate payments

- **Balance Consistency:** Ensure balance updates are atomic

---

## Third-Party Service Integration

### Payment Gateway Integration

**Payment Processing:**

- **SDK Integration:** Integrate payment gateway SDK for payment processing

- **Webhook Handling:** Handle payment gateway webhooks

- **Idempotency:** Implement idempotency for payment requests

- **Error Handling:** Handle payment gateway errors gracefully

### Redis Integration

**Idempotency & Caching:**

- **Idempotency Keys:** Store idempotency keys in Redis

- **Payment Status Caching:** Cache payment status

- **Rate Limiting:** Use Redis for rate limiting

---

# 4) Algorithms

## Idempotency Key Algorithm

**Purpose:** Prevent duplicate payment processing using idempotency keys stored in Redis.

**Algorithm:**

1. Client sends payment request with idempotency key (or server generates UUID)
2. Check if idempotency key exists in Redis
3. If exists, return cached payment result
4. If not exists, process payment and store result in Redis with TTL
5. Return payment result

**Implementation:**

```javascript
class PaymentService {
 async processPaymentWithIdempotency(
 paymentData: PaymentRequest,
 idempotencyKey){
 // Check if idempotency key exists
 const cached = await redis.get(`idempotency:${idempotencyKey}`);
 if (cached) {
 return JSON.parse(cached);
 }

 // Process payment
 const result = await this.processPayment(paymentData);

 // Store result in Redis with 24-hour TTL
 await redis.setex(
 `idempotency:${idempotencyKey}`,
 86400,
 JSON.stringify(result)
 );

 return result;
 }
}

```

**Complexity:**

- Time: O(1) for Redis operations
- Space: O(1) per idempotency key
- **Duplicate Prevention:** 100% effective for duplicate requests

---

## Payment Retry Algorithm

**Purpose:** Retry failed payment requests with exponential backoff.

**Algorithm:**

1. Attempt payment processing
2. If fails, wait with exponential backoff (1s, 2s, 4s, 8s)
3. Retry up to maximum attempts (3-5 retries)
4. If all retries fail, mark payment as failed

**Implementation:**

```javascript
async function retryPayment(
 paymentData: PaymentRequest,
 maxRetries= 3
){
 let lastError: Error;

 for (let attempt = 0; attempt < maxRetries; attempt++) {
 try {
 return await processPayment(paymentData);
 } catch (error) {
 lastError = error;

 // Don't retry on certain errors (e.g., invalid card)
 if (error.code === 'INVALID_CARD' || error.code === 'INSUFFICIENT_FUNDS') {
 throw error;
 }

 // Exponential backoff
 if (attempt < maxRetries - 1) {
 const delay = Math.pow(2, attempt) * 1000; // 1s, 2s, 4s
 await sleep(delay);
 }
 }
 }

 throw lastError!;
}

```

**Complexity:**

- Time: O(k) where k is number of retries
- Space: O(1)
- **Retry Strategy:** Exponential backoff prevents overwhelming payment gateway

---

# 5) Data Models

## Payments Collection (MongoDB/PostgreSQL)

```javascript
{
 _id: ObjectId,
 paymentId: String, // Unique payment ID, indexed
 orderId: String, // Order reference, indexed
 userId: ObjectId, // User reference, indexed
 amount: Number, // Payment amount
 currency: String, // Currency code (USD, INR)
 status: String, // pending, processing, succeeded, failed, refunded
 paymentMethod: String, // card, upi, wallet, netbanking
 paymentGateway: String, // payment gateway provider identifier
 gatewayTransactionId: String, // Payment gateway transaction ID
 idempotencyKey: String, // Idempotency key, indexed
 failureReason: String, // Failure reason if failed
 metadata: Object, // Additional metadata
 processedAt, // When payment was processed
 createdAt, // Created timestamp, indexed
 updatedAt// Updated timestamp
}

// Indexes:
// - { paymentId: 1 } (unique)
// - { idempotencyKey: 1 } (unique)
// - { userId: 1, createdAt: -1 } (compound)
// - { orderId: 1 } (indexed)
// - { status: 1, createdAt: -1 } (compound)
// - { gatewayTransactionId: 1 } (indexed)

```

## Refunds Collection (MongoDB/PostgreSQL)

```javascript
{
 _id: ObjectId,
 refundId: String, // Unique refund ID, indexed
 paymentId: ObjectId, // Payment reference, indexed
 amount: Number, // Refund amount
 reason: String, // Refund reason
 status: String, // pending, processing, succeeded, failed
 gatewayRefundId: String, // Payment gateway refund ID
 processedAt, // When refund was processed
 createdAt, // Created timestamp, indexed
 updatedAt// Updated timestamp
}

// Indexes:
// - { refundId: 1 } (unique)
// - { paymentId: 1 } (indexed)
// - { status: 1, createdAt: -1 } (compound)

```

---

# 6) Database Transactions and Consistency

### MongoDB/PostgreSQL Transactions

**Transaction Usage:**

- **Multi-Document Transactions** - For operations requiring ACID guarantees
- **Example:** Payment creation + balance update + transaction log in single transaction
- **Session Management:** Use database sessions for transaction control

**Example:**

```javascript
const session = await mongoose.startSession();
session.startTransaction();
try {
 await Payment.create([paymentData], { session });
 await Wallet.updateOne({ userId }, { $inc: { balance: -amount } }, { session });
 await TransactionLog.create([logData], { session });
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

- **Payment Consistency:** Use transactions for payment operations to ensure atomicity
- **Idempotency:** Use idempotency keys to prevent duplicate payments
- **Balance Consistency:** Ensure balance updates are atomic with payment creation
- **Eventual Consistency:** Accept eventual consistency for webhook processing (webhooks may arrive out of order)

---

# 7) Protocols

### REST API Protocol

- **Protocol:** REST (Representational State Transfer)
- **Data Format:** JSON
- **HTTP Methods:** GET, POST, PUT
- **Status Codes:** 200 (Success), 201 (Created), 400 (Bad Request), 401 (Unauthorized), 402 (Payment Required), 404 (Not Found), 409 (Duplicate Payment), 500 (Server Error)
- **Authentication:** JWT Bearer token in Authorization header

### Webhook Protocol

- **Protocol:** HTTP POST
- **Data Format:** JSON
- **Signature Verification:** HMAC-SHA256 signature in header
- **Idempotency:** Webhook ID for duplicate detection
- **Use Case:** Payment gateway status updates

---

# 8) API Design

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

---

# 9) Caching Strategy

### Redis Cache

**Cache Strategy:**

- **Key Format:** `idempotency:{key}`, `payment:{paymentId}`, `payment:status:{paymentId}`
- **Value:** Serialized JSON (payment result, payment status)
- **TTL:**
 - Idempotency keys: 86400 seconds (24 hours)
 - Payment status: 3600 seconds (1 hour)
 - Payment result: 86400 seconds (24 hours)
- **Eviction Policy:** LRU (Least Recently Used)

**Cache Patterns:**

- **Cache-Aside Pattern:** Check cache first, if miss query database and update cache
- **Write-Through Pattern:** Update cache when payment status changes
- **Cache Invalidation:** Invalidate payment cache on status updates

---

# 10) Error Handling

### Error Scenarios and Responses

**Edge Cases Handling:**

- **Duplicate Payment:** Return 409 Conflict with cached payment result
- **Payment Gateway Failure:** Return 502 Bad Gateway, retry with exponential backoff
- **Invalid Payment Method:** Return 400 Bad Request with validation errors
- **Insufficient Funds:** Return 402 Payment Required with error details
- **Invalid Webhook Signature:** Return 401 Unauthorized, log for security audit
- **Payment Timeout:** Return 504 Gateway Timeout, mark payment as pending

**Error Response Format:**

```json
{
 "error": {
 "code": "PAYMENT_FAILED",
 "message": "Payment processing failed",
 "details": "Card declined by bank",
 "paymentId": "payment_abc123",
 "retryable": true
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

**Database Scaling:**

- **Read Replicas:** Deploy read replicas for payment history queries
- **Sharding:** Shard payments by userId or paymentId for write scaling
- **Connection Pooling:** Use connection pooling to manage database connections

**Caching:**

- Distributed Redis cluster for high availability
- Cache idempotency keys and payment status
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
- **Health Checks:** Verify payment endpoints are healthy
- **Blue-Green Deployment:** Maintain two identical production environments

### Database Deployment

**MongoDB/PostgreSQL Setup:**

- **Managed Database Service** - MongoDB Atlas or AWS RDS
- **Backup Strategy:** Daily automated backups with point-in-time recovery
- **Indexing:** Proper indexes on paymentId, orderId, userId, idempotencyKey
- **Replication:** Replica sets for high availability

**Redis Setup:**

- **Redis Cloud / AWS ElastiCache** - Managed Redis service
- **Cluster Mode:** Redis cluster for high availability and performance
- **Persistence:** RDB snapshots and AOF for data durability

---

# 12) Security Considerations

### PCI-DSS Compliance

- **Never Store Card Data:** Use payment gateway tokens, never store full card numbers
- **Tokenization:** Use payment gateway tokenization for card storage
- **Encryption:** Encrypt all payment data in transit (HTTPS) and at rest
- **Access Control:** Restrict access to payment data, use role-based access control

### Payment Security

- **Idempotency:** Use idempotency keys to prevent duplicate charges
- **Webhook Verification:** Verify webhook signatures to prevent fraud
- **Rate Limiting:** Implement rate limiting to prevent payment abuse
- **Fraud Detection:** ML-based fraud detection analyzing transaction patterns

### Input Validation

- Validate all payment inputs (amount, currency, payment method)
- Sanitize user input to prevent injection attacks
- Validate payment gateway responses

### HTTPS/TLS

- All communication between clients and API encrypted using HTTPS
- Prevents eavesdropping and man-in-the-middle attacks
- SSL/TLS certificates for secure connections

### Authentication and Authorization

- **JWT Tokens:** Use JWT for stateless authentication
- **Token Expiration:** Set appropriate token expiration times
- **Role-Based Access Control:** Implement RBAC for payment operations
- **API Keys:** Use API keys for service-to-service authentication

### Monitoring and Alerts

- Set up monitoring for unusual payment patterns
- Trigger alerts for potential fraud or security issues
- Track metrics: payment success rates, fraud detection rates, payment gateway latency
- Log all payment operations for security auditing (without sensitive data)

---

# 3) Interview Answers

---

## Q1. 💡 Designing a payment system

**Situation:** Need to design a payment processing system for 1B+ transactions per day with 99.99% reliability, handling multiple payment methods and fraud detection.

**Action:** I designed a payment system:

- **Idempotency:** Use idempotency keys to prevent duplicate charges (store in Redis)

- **Payment Gateway Integration:** Integrate with multiple payment gateways

- **Webhook Handling:** Process payment status updates via webhooks with signature verification

- **Message Queue:** Use Kafka/RabbitMQ for async payment processing to avoid blocking

- **Fraud Detection:** ML-based fraud detection system analyzing transaction patterns

- **Retry Logic:** Retry failed payments with exponential backoff

- **Database Transactions:** Use database transactions to ensure payment and order consistency

- **Audit Logging:** Log all payment operations for compliance and debugging

**Result:** System handles 1B+ transactions per day with 99.99% reliability. Zero duplicate charges due to idempotency. Fraud detection reduces fraudulent transactions by 95%.

**Takeaway:** Idempotency is critical for payment systems. Webhooks provide reliable status updates. Fraud detection protects both users and merchants.

---

## Q2. 💡 Ensuring idempotency in payment processing

**Situation:** Need to prevent duplicate charges when payment request is retried.

**Action:** I implemented idempotency:

- **Idempotency Key:** Client sends unique idempotency key with each payment request

- **Redis Storage:** Store idempotency key → payment result mapping in Redis with 24-hour TTL

- **Duplicate Detection:** Check if idempotency key exists before processing payment

- **Return Cached Result:** If key exists, return cached payment result instead of processing again

- **Key Generation:** Client generates idempotency key (UUID) or server generates if not provided

**Result:** Zero duplicate charges in production. Idempotency keys prevent duplicate processing even with network retries.

**Takeaway:** Idempotency keys are essential for payment systems. Redis provides fast duplicate detection.

---

## Q3. 🪝 🪝 🪝 Handling payment webhooks

**Situation:** Payment gateway sends webhooks to notify payment status changes.

**Action:** I implemented webhook handling:

- **Signature Verification:** Verify webhook signature to ensure authenticity

- **Idempotency:** Use webhook ID to prevent duplicate processing

- **Queue Processing:** Queue webhooks for async processing to avoid blocking

- **Retry Logic:** Retry failed webhook processing with exponential backoff

- **Status Updates:** Update payment and order status based on webhook events

- **Logging:** Log all webhook events for audit trail

**Result:** 99.9% webhook processing success rate. Payment status updates in real-time. Zero duplicate webhook processing.

**Takeaway:** Webhook signature verification is critical for security. Async processing prevents blocking.

---

## Q4. 💡 Implementing payment retry logic

**Situation:** Payment gateway may fail temporarily, need to retry failed payments without creating duplicate charges.

**Action:** I implemented payment retry logic:

- **Idempotency Keys:** Use same idempotency key for retries to prevent duplicate charges
- **Exponential Backoff:** Retry with exponential backoff (1s, 2s, 4s, 8s) to avoid overwhelming gateway
- **Max Retries:** Limit retries to 3-5 attempts to prevent infinite loops
- **Error Classification:** Don't retry on certain errors (invalid card, insufficient funds)
- **Retry Queue:** Queue failed payments for retry processing
- **Status Tracking:** Track retry attempts and last retry time
- **Notification:** Notify user after max retries exceeded

**Result:** Payment success rate improved from 95% to 99.5%. Retry logic handles temporary gateway failures. Zero duplicate charges due to idempotency.

**Takeaway:** Idempotency keys enable safe retries. Exponential backoff prevents gateway overload. Error classification avoids unnecessary retries.

---

## Q5. 💡 Handling payment refunds

**Situation:** Users request refunds, need to process refunds securely and maintain refund history.

**Action:** I implemented refund processing:

- **Refund Validation:** Validate refund eligibility (within refund window, payment succeeded)
- **Partial Refunds:** Support partial refunds for orders with multiple items
- **Refund Processing:** Process refund through payment gateway API
- **Status Tracking:** Track refund status (pending, processing, succeeded, failed)
- **Webhook Handling:** Handle refund status updates via webhooks
- **Refund History:** Maintain refund history linked to original payment
- **Notification:** Notify user when refund is processed

**Result:** Refunds processed within 24 hours. Refund success rate 99.9%. Complete refund history maintained. Users notified promptly.

**Takeaway:** Refund validation prevents invalid refunds. Webhook handling provides real-time status updates. Refund history enables audit trail.
