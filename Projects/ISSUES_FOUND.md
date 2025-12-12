# Issues Found in Projects Directory

## Critical Issues

### 1. Question Format Violation

**Rule:** All questions must be in concept statement format, not question format (no question marks)

**Found Issues:**

- All questions use question format: "How would you design...", "What was the most complex...", "How did you implement..."
- Examples:
  - `## Q1. How would you design a URL shortener like Bitly?` ❌
  - `## Q1. What was the most complex technical challenge you faced while building the rate limiter?` ❌

**Should be:**

- `## Q1. Designing a scalable URL shortener system` ✅
- `## Q1. Most complex technical challenge in building the rate limiter` ✅

### 2. Brand Names Violation

**Rule:** Use generic names, avoid brand-specific references

**Found Issues:**

- "Bitly" mentioned in URL Shortener Q1
- "Youtube" mentioned in Video Streaming Platform Q1
- "Razorpay/Stripe" mentioned in E-commerce App Q5

**Should be:**

- "URL shortener" (not "like Bitly")
- "Video streaming platform" (not "Youtube")
- "Payment gateway" (not "Razorpay/Stripe")

### 3. Missing Frontend/Backend Labels

**Rule:** Action sections should clearly separate with "**Frontend (React.js):**" and "**Backend (Node.js/Express.js):**" labels

**Found Issues:**

- Rate Limiter Q1: Action section doesn't have proper labels
- Rate Limiter Q3: Action section doesn't have proper labels
- Some other questions missing consistent labeling

### 4. Language Requirements

**Rule:** Use conversational language with analogies and "think of this as" phrases

**Found Issues:**

- Limited use of analogies
- Missing "think of this as" phrases in section introductions
- Some technical jargon that could be simplified

**Examples Needed:**

- "Redis is like a walkie-talkie for real-time communication"
- "Think of this as the building blocks of the system"
- "Payment gateway is like a cashier that processes transactions"

## Moderate Issues

### 5. Inconsistent Formatting

- Some Action sections have labels, others don't
- Inconsistent spacing in some answers
- Some answers have proper separation, others are more compact

### 6. Missing Conversational Comments in Code

**Rule:** Code examples should have conversational comments explaining what code does

**Found Issues:**

- Some code blocks lack conversational comments
- Comments are sometimes too technical

## Files That Need Updates

1. All project files need question format fixes (concept statements)
2. URL Shortener - Remove "Bitly" reference
3. Video Streaming Platform - Remove "Youtube" reference
4. E-commerce App - Remove "Razorpay/Stripe" references
5. Rate Limiter Q1, Q3 - Add Frontend/Backend labels
6. All files - Add more analogies and conversational language

## Priority

1. **HIGH:** Fix question format (concept statements)
2. **HIGH:** Remove brand names
3. **MEDIUM:** Add missing Frontend/Backend labels
4. **MEDIUM:** Add more conversational language and analogies
