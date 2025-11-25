# 7) Authentication, Security & Encryption (Q71–80)

<div align="center">

**[← Previous: REST APIs & Practical Server Scenarios](6%29%20REST%20APIs%20%26%20Practical%20Server%20Scenarios.md)** | **[Next: Performance, Optimization, Scaling & Monitoring →](8%29%20Performance%2C%20Optimization%2C%20Scaling%20%26%20Monitoring.md)**

</div>
## Q71. Session-based vs token-based authentication

Session-based authentication stores user state on the server (more secure, harder to scale), while token-based authentication stores user information in a client-side token (stateless, easier to scale) - sessions are vulnerable to CSRF attacks, tokens are vulnerable to XSS attacks. Choose based on security requirements and scalability needs.

- **Trade-offs**: Sessions: server-side state, more secure, harder to scale - Tokens: client-side state, stateless, easier to scale. Sessions vulnerable to CSRF attacks - tokens vulnerable to XSS attacks. Choose based on security requirements and scalability needs - sessions are better for security, tokens are better for scalability.

Example:

```javascript
const session = require('express-session');
app.use(session({
  secret: 'secret-key',
  resave: false,
  saveUninitialized: false
}));

app.post('/login', (req, res) => {
  req.session.userId = user.id;
  res.json({ message: 'Logged in' });
});

const jwt = require('jsonwebtoken');
app.post('/login', (req, res) => {
  const token = jwt.sign({ userId: user.id }, 'secret-key');
  res.json({ token });
});
```

## Q72. Implementing JWT authentication in Express.js

JWT (JSON Web Token) authentication uses signed tokens containing user information, verified on each request without server-side session storage - use environment variables for JWT secrets, set appropriate token expiration times, include minimal necessary information in tokens, implement token refresh for long-lived sessions, and consider token blacklisting for logout.

- **Trade-offs**: Use environment variables for JWT secrets - set appropriate token expiration times. Include minimal necessary information in tokens - implement token refresh for long-lived sessions. Consider token blacklisting for logout - stateless and scalable, but watch out - tokens can't be revoked easily, so use short expiration times and refresh tokens.

Example:

```javascript
const jwt = require('jsonwebtoken');
const express = require('express');
const app = express();

app.post('/login', (req, res) => {
  const { username, password } = req.body;
  const token = jwt.sign(
    { userId: user.id, username: user.username },
    process.env.JWT_SECRET,
    { expiresIn: '1h' }
  );
  res.json({ token });
});

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

## Q73. Implementing route guards and middleware

Route guards are middleware functions that check authentication and authorization before allowing access to protected routes - separate authentication and authorization concerns, use middleware for reusable route protection, implement role-based access control, return appropriate HTTP status codes, and consider permission-based authorization for fine-grained control.

- **Trade-offs**: Separate authentication and authorization concerns - use middleware for reusable route protection. Implement role-based access control - return appropriate HTTP status codes. Consider permission-based authorization for fine-grained control - makes route protection easy and reusable, but watch out - middleware order matters, so place guards before route handlers.

Example:

```javascript
function requireAuth(req, res, next) {
  if (!req.user) {
    return res.status(401).json({ error: 'Authentication required' });
  }
  next();
}

function requireRole(role) {
  return (req, res, next) => {
    if (req.user.role !== role) {
      return res.status(403).json({ error: 'Insufficient permissions' });
    }
    next();
  };
}

app.get('/admin', requireAuth, requireRole('admin'), (req, res) => {
  res.json({ message: 'Admin only content' });
});

app.get('/profile', requireAuth, (req, res) => {
  res.json({ user: req.user });
});
```

## Q74. Implementing HTTP-only cookies for security

HTTP-only cookies cannot be accessed by JavaScript, preventing XSS attacks from stealing authentication tokens, while SameSite attributes prevent CSRF attacks - HTTP-only prevents XSS token theft, secure flag ensures HTTPS-only transmission, SameSite prevents CSRF attacks, maxAge controls cookie expiration, and consider token refresh with HTTP-only cookies.

- **Trade-offs**: HTTP-only prevents XSS token theft - secure flag ensures HTTPS-only transmission. SameSite prevents CSRF attacks - maxAge controls cookie expiration. Consider token refresh with HTTP-only cookies - more secure than localStorage, but watch out - cookies have size limits and can be affected by browser settings.

Example:

```javascript
const cookieParser = require('cookie-parser');
app.use(cookieParser());

app.post('/login', (req, res) => {
  const token = jwt.sign({ userId: user.id }, process.env.JWT_SECRET);
  res.cookie('token', token, {
    httpOnly: true,
    secure: process.env.NODE_ENV === 'production',
    sameSite: 'strict',
    maxAge: 24 * 60 * 60 * 1000
  });
  res.json({ message: 'Logged in' });
});

app.get('/protected', (req, res) => {
  const token = req.cookies.token;
  if (!token) return res.status(401).json({ error: 'No token' });
});
```

## Q75. Implementing OAuth 2.0 in Express.js

OAuth 2.0 allows users to authenticate with third-party providers (Google, Facebook) by redirecting to the provider and handling the callback with authorization codes - use Passport.js for OAuth implementation, store provider-specific user IDs, handle user creation and linking, implement proper error handling, and consider multiple OAuth providers.

- **Trade-offs**: Use Passport.js for OAuth implementation - store provider-specific user IDs. Handle user creation and linking - implement proper error handling. Consider multiple OAuth providers - makes login easier for users, but watch out - OAuth adds complexity and dependency on third-party providers.

Example:

```javascript
const passport = require('passport');
const GoogleStrategy = require('passport-google-oauth20').Strategy;

passport.use(new GoogleStrategy({
  clientID: process.env.GOOGLE_CLIENT_ID,
  clientSecret: process.env.GOOGLE_CLIENT_SECRET,
  callbackURL: '/auth/google/callback'
}, (accessToken, refreshToken, profile, done) => {
  User.findOrCreate({ googleId: profile.id }, (err, user) => {
    return done(err, user);
  });
}));

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

## Q76. Implementing CORS in Express.js

CORS (Cross-Origin Resource Sharing) allows web pages to make requests to different domains, configured with specific origins, methods, and headers - configure specific origins instead of wildcard, set appropriate methods and headers, enable credentials for authenticated requests, use dynamic CORS for complex scenarios, and consider preflight request handling.

- **Trade-offs**: Configure specific origins instead of wildcard - set appropriate methods and headers. Enable credentials for authenticated requests - use dynamic CORS for complex scenarios. Consider preflight request handling - essential for cross-origin requests, but watch out - allowing all origins with credentials is a security risk, so be specific.

Example:

```javascript
const cors = require('cors');

app.use(cors());

app.use(cors({
  origin: ['https://example.com', 'https://app.example.com'],
  methods: ['GET', 'POST', 'PUT', 'DELETE'],
  allowedHeaders: ['Content-Type', 'Authorization'],
  credentials: true
}));

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

## Q77. Implementing security headers with Helmet

Helmet sets various HTTP headers to improve security by preventing common attacks like XSS, clickjacking, and MIME type sniffing - it sets security-related HTTP headers, prevents XSS, clickjacking, and MIME sniffing, configures Content Security Policy, enables HTTPS Strict Transport Security, and is essential for production applications.

- **Trade-offs**: Sets security-related HTTP headers - prevents XSS, clickjacking, and MIME sniffing. Configures Content Security Policy - enables HTTPS Strict Transport Security. Essential for production applications - easy to add security headers, but watch out - CSP can break your app if not configured correctly, so test thoroughly.

Example:

```javascript
const helmet = require('helmet');
app.use(helmet());

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

## Q78. Preventing SQL injection, XSS, and CSRF attacks

Prevent common web attacks by using parameterized queries, input validation, output encoding, and CSRF tokens - use parameterized queries to prevent SQL injection, validate and sanitize all input data, encode output to prevent XSS, use CSRF tokens for state-changing operations, and implement Content Security Policy headers.

- **Trade-offs**: Use parameterized queries to prevent SQL injection - validate and sanitize all input data. Encode output to prevent XSS - use CSRF tokens for state-changing operations. Implement Content Security Policy headers - essential for security, but watch out - security requires multiple layers, so don't rely on just one method.

Example:

```javascript
const express = require('express');
const { body, validationResult } = require('express-validator');
const csrf = require('csurf');

const csrfProtection = csrf({ cookie: true });
app.use(csrfProtection);

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

app.post('/users', validateInput, (req, res) => {
  const { username, email } = req.body;
  res.json({ message: 'User created' });
});
```

## Q79. Implementing password hashing with bcrypt or argon2

Passwords should never be stored in plain text, using strong hashing algorithms like bcrypt or argon2 with salt to prevent rainbow table attacks - never store passwords in plain text, use strong hashing algorithms (bcrypt, argon2), use appropriate salt rounds (12+ for bcrypt), consider argon2 for new applications, and implement password strength requirements.

- **Trade-offs**: Never store passwords in plain text - use strong hashing algorithms (bcrypt, argon2). Use appropriate salt rounds (12+ for bcrypt) - consider argon2 for new applications. Implement password strength requirements - essential for security, but watch out - hashing is CPU-intensive, so balance security with performance.

Example:

```javascript
const bcrypt = require('bcrypt');
const argon2 = require('argon2');

async function hashPassword(password) {
  const saltRounds = 12;
  return await bcrypt.hash(password, saltRounds);
}

async function verifyPassword(password, hash) {
  return await bcrypt.compare(password, hash);
}

async function hashPasswordArgon2(password) {
  return await argon2.hash(password, {
    type: argon2.argon2id,
    memoryCost: 2 ** 16,
    timeCost: 3,
    parallelism: 1
  });
}

app.post('/register', async (req, res) => {
  const { username, password } = req.body;
  const hashedPassword = await hashPassword(password);
  res.json({ message: 'User registered' });
});
```

## Q80. Managing secrets and API keys securely

Secrets should be stored in environment variables, never in code, with proper access controls, encryption, and secure key management practices - store secrets in environment variables, use .env files for local development, never commit .env files to version control, use different secrets for different environments, and consider secret management services for production.

- **Trade-offs**: Store secrets in environment variables - use .env files for local development. Never commit .env files to version control - use different secrets for different environments. Consider secret management services for production - essential for security, but watch out - managing secrets across environments can be complex, so use tools like AWS Secrets Manager for production.

Example:

```javascript
const dotenv = require('dotenv');
dotenv.config();

const config = {
  jwtSecret: process.env.JWT_SECRET,
  dbPassword: process.env.DB_PASSWORD,
  apiKey: process.env.API_KEY,
  nodeEnv: process.env.NODE_ENV
};

const requiredEnvVars = ['JWT_SECRET', 'DB_PASSWORD'];
requiredEnvVars.forEach(envVar => {
  if (!process.env[envVar]) {
    throw new Error(`Missing required environment variable: ${envVar}`);
  }
});

app.post('/login', (req, res) => {
  const token = jwt.sign({ userId: user.id }, config.jwtSecret);
  res.json({ token });
});
```
