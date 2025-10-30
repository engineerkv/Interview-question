# 8) Authentication, Security & Encryption (Q71–80)

## 71) What is the difference between session-based and token-based authentication?

Concept: Session-based authentication stores user state on the server, while token-based authentication stores user information in a client-side token, with different trade-offs for security and scalability.

Example:
```javascript
// Session-based authentication
const session = require('express-session');
app.use(session({
  secret: 'secret-key',
  resave: false,
  saveUninitialized: false
}));

app.post('/login', (req, res) => {
  // Validate credentials
  req.session.userId = user.id;
  res.json({ message: 'Logged in' });
});

// Token-based authentication
const jwt = require('jsonwebtoken');
app.post('/login', (req, res) => {
  const token = jwt.sign({ userId: user.id }, 'secret-key');
  res.json({ token });
});
```

Deep Insight:
- Sessions: Server-side state, more secure, harder to scale
- Tokens: Client-side state, stateless, easier to scale
- Sessions vulnerable to CSRF attacks
- Tokens vulnerable to XSS attacks
- Choose based on security requirements and scalability needs

## 72) How do you implement JWT authentication in Node + Express?

Concept: JWT (JSON Web Token) authentication uses signed tokens containing user information, verified on each request without server-side session storage.

Example:
```javascript
const jwt = require('jsonwebtoken');
const express = require('express');
const app = express();

// Login endpoint
app.post('/login', (req, res) => {
  const { username, password } = req.body;
  // Validate credentials
  const token = jwt.sign(
    { userId: user.id, username: user.username },
    process.env.JWT_SECRET,
    { expiresIn: '1h' }
  );
  res.json({ token });
});

// Protected route middleware
function authenticateToken(req, res, next) {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];
  
  if (!token) return res.sendStatus(401);
  
  jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
    if (err) return res.sendStatus(403);
    req.user = user;
    next();
  });
}

app.get('/protected', authenticateToken, (req, res) => {
  res.json({ message: 'Protected data', user: req.user });
});
```

Deep Insight:
- Use environment variables for JWT secrets
- Set appropriate token expiration times
- Include minimal necessary information in tokens
- Implement token refresh for long-lived sessions
- Consider token blacklisting for logout

## 73) How do you secure routes using middleware guards?

Concept: Route guards are middleware functions that check authentication and authorization before allowing access to protected routes.

Example:
```javascript
// Authentication middleware
function requireAuth(req, res, next) {
  if (!req.user) {
    return res.status(401).json({ error: 'Authentication required' });
  }
  next();
}

// Authorization middleware
function requireRole(role) {
  return (req, res, next) => {
    if (req.user.role !== role) {
      return res.status(403).json({ error: 'Insufficient permissions' });
    }
    next();
  };
}

// Protected routes
app.get('/admin', requireAuth, requireRole('admin'), (req, res) => {
  res.json({ message: 'Admin only content' });
});

app.get('/profile', requireAuth, (req, res) => {
  res.json({ user: req.user });
});
```

Deep Insight:
- Separate authentication and authorization concerns
- Use middleware for reusable route protection
- Implement role-based access control
- Return appropriate HTTP status codes
- Consider permission-based authorization for fine-grained control

## 74) What are HTTP-only cookies, and how do they enhance security?

Concept: HTTP-only cookies cannot be accessed by JavaScript, preventing XSS attacks from stealing authentication tokens, while SameSite attributes prevent CSRF attacks.

Example:
```javascript
const cookieParser = require('cookie-parser');
app.use(cookieParser());

// Set HTTP-only cookie
app.post('/login', (req, res) => {
  const token = jwt.sign({ userId: user.id }, process.env.JWT_SECRET);
  res.cookie('token', token, {
    httpOnly: true,
    secure: process.env.NODE_ENV === 'production',
    sameSite: 'strict',
    maxAge: 24 * 60 * 60 * 1000 // 24 hours
  });
  res.json({ message: 'Logged in' });
});

// Read HTTP-only cookie
app.get('/protected', (req, res) => {
  const token = req.cookies.token;
  if (!token) return res.status(401).json({ error: 'No token' });
  // Verify token...
});
```

Deep Insight:
- HTTP-only prevents XSS token theft
- Secure flag ensures HTTPS-only transmission
- SameSite prevents CSRF attacks
- MaxAge controls cookie expiration
- Consider token refresh with HTTP-only cookies

## 75) How do you implement OAuth 2.0 or social login in Node.js?

Concept: OAuth 2.0 allows users to authenticate with third-party providers (Google, Facebook) by redirecting to the provider and handling the callback with authorization codes.

Example:
```javascript
const passport = require('passport');
const GoogleStrategy = require('passport-google-oauth20').Strategy;

// Configure Google OAuth strategy
passport.use(new GoogleStrategy({
  clientID: process.env.GOOGLE_CLIENT_ID,
  clientSecret: process.env.GOOGLE_CLIENT_SECRET,
  callbackURL: '/auth/google/callback'
}, (accessToken, refreshToken, profile, done) => {
  // Find or create user
  User.findOrCreate({ googleId: profile.id }, (err, user) => {
    return done(err, user);
  });
}));

// OAuth routes
app.get('/auth/google', passport.authenticate('google', {
  scope: ['profile', 'email']
}));

app.get('/auth/google/callback',
  passport.authenticate('google', { failureRedirect: '/login' }),
  (req, res) => {
    res.redirect('/dashboard');
  }
);
```

Deep Insight:
- Use Passport.js for OAuth implementation
- Store provider-specific user IDs
- Handle user creation and linking
- Implement proper error handling
- Consider multiple OAuth providers

## 76) How do you enable and configure CORS correctly in Express?

Concept: CORS (Cross-Origin Resource Sharing) allows web pages to make requests to different domains, configured with specific origins, methods, and headers.

Example:
```javascript
const cors = require('cors');

// Basic CORS
app.use(cors());

// Configured CORS
app.use(cors({
  origin: ['https://example.com', 'https://app.example.com'],
  methods: ['GET', 'POST', 'PUT', 'DELETE'],
  allowedHeaders: ['Content-Type', 'Authorization'],
  credentials: true
}));

// Dynamic CORS
app.use(cors((req, callback) => {
  const origin = req.header('Origin');
  const allowedOrigins = ['https://example.com'];
  
  if (allowedOrigins.includes(origin)) {
    callback(null, { origin: true, credentials: true });
  } else {
    callback(new Error('Not allowed by CORS'));
  }
}));
```

Deep Insight:
- Configure specific origins instead of wildcard
- Set appropriate methods and headers
- Enable credentials for authenticated requests
- Use dynamic CORS for complex scenarios
- Consider preflight request handling

## 77) How does the Helmet middleware improve security?

Concept: Helmet sets various HTTP headers to improve security by preventing common attacks like XSS, clickjacking, and MIME type sniffing.

Example:
```javascript
const helmet = require('helmet');
app.use(helmet());

// Configure specific Helmet options
app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      styleSrc: ["'self'", "'unsafe-inline'"],
      scriptSrc: ["'self'"]
    }
  },
  hsts: {
    maxAge: 31536000,
    includeSubDomains: true,
    preload: true
  }
}));
```

Deep Insight:
- Sets security-related HTTP headers
- Prevents XSS, clickjacking, and MIME sniffing
- Configures Content Security Policy
- Enables HTTPS Strict Transport Security
- Essential for production applications

## 78) How do you prevent SQL Injection, XSS, and CSRF attacks?

Concept: Prevent common web attacks by using parameterized queries, input validation, output encoding, and CSRF tokens.

Example:
```javascript
const express = require('express');
const { body, validationResult } = require('express-validator');
const csrf = require('csurf');

// CSRF protection
const csrfProtection = csrf({ cookie: true });
app.use(csrfProtection);

// Input validation
const validateInput = [
  body('username').trim().escape(),
  body('email').isEmail().normalizeEmail(),
  (req, res, next) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({ errors: errors.array() });
    }
    next();
  }
];

// SQL injection prevention (using parameterized queries)
app.post('/users', validateInput, (req, res) => {
  const { username, email } = req.body;
  // Use parameterized queries: db.query('INSERT INTO users (username, email) VALUES (?, ?)', [username, email]);
  res.json({ message: 'User created' });
});
```

Deep Insight:
- Use parameterized queries to prevent SQL injection
- Validate and sanitize all input data
- Encode output to prevent XSS
- Use CSRF tokens for state-changing operations
- Implement Content Security Policy headers

## 79) How do you store and hash passwords securely (bcrypt, argon2)?

Concept: Passwords should never be stored in plain text, using strong hashing algorithms like bcrypt or argon2 with salt to prevent rainbow table attacks.

Example:
```javascript
const bcrypt = require('bcrypt');
const argon2 = require('argon2');

// Using bcrypt
async function hashPassword(password) {
  const saltRounds = 12;
  return await bcrypt.hash(password, saltRounds);
}

async function verifyPassword(password, hash) {
  return await bcrypt.compare(password, hash);
}

// Using argon2 (more secure)
async function hashPasswordArgon2(password) {
  return await argon2.hash(password, {
    type: argon2.argon2id,
    memoryCost: 2 ** 16,
    timeCost: 3,
    parallelism: 1
  });
}

// Registration
app.post('/register', async (req, res) => {
  const { username, password } = req.body;
  const hashedPassword = await hashPassword(password);
  // Store username and hashedPassword in database
  res.json({ message: 'User registered' });
});
```

Deep Insight:
- Never store passwords in plain text
- Use strong hashing algorithms (bcrypt, argon2)
- Use appropriate salt rounds (12+ for bcrypt)
- Consider argon2 for new applications
- Implement password strength requirements

## 80) How do you manage secrets, tokens, and environment variables safely?

Concept: Secrets should be stored in environment variables, never in code, with proper access controls, encryption, and secure key management practices.

Example:
```javascript
const dotenv = require('dotenv');
dotenv.config();

// Environment variables
const config = {
  jwtSecret: process.env.JWT_SECRET,
  dbPassword: process.env.DB_PASSWORD,
  apiKey: process.env.API_KEY,
  nodeEnv: process.env.NODE_ENV
};

// Validate required environment variables
const requiredEnvVars = ['JWT_SECRET', 'DB_PASSWORD'];
requiredEnvVars.forEach(envVar => {
  if (!process.env[envVar]) {
    throw new Error(`Missing required environment variable: ${envVar}`);
  }
});

// Use secrets
app.post('/login', (req, res) => {
  const token = jwt.sign({ userId: user.id }, config.jwtSecret);
  res.json({ token });
});
```

Deep Insight:
- Store secrets in environment variables
- Use .env files for local development
- Never commit .env files to version control
- Use different secrets for different environments
- Consider secret management services for production
