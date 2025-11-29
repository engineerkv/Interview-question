<div align="center">

**[← Previous: Data & Caching Architecture](10%29%20Data%20%26%20Caching%20Architecture.md)** | **[Next: Logging & Monitoring →](12%29%20Logging%20%26%20Monitoring.md)**

</div>

# 11. Security (Q132–146)

---

## Q132. Security overview

Frontend security protects users and applications from attacks like XSS, CSRF, clickjacking, and data theft by implementing defense-in-depth strategies across multiple layers. Security requires input validation, output encoding, secure headers, HTTPS, and proper authentication mechanisms.

- **Trade-offs**: Security is an ongoing process, not a one-time setup—implement multiple layers of defense since no single measure is foolproof. The catch is security measures can impact user experience (like strict CSP breaking third-party widgets) or development velocity—balance security with usability and always stay updated on new threats and best practices.

Example:

```javascript
// Defense-in-depth approach
// 1. Input validation
// 2. Output encoding
// 3. Security headers (CSP, HSTS, etc.)
// 4. HTTPS everywhere
// 5. Secure authentication
// 6. Regular dependency updates
```

---

## Q133. XSS (Cross-Site Scripting)

XSS attacks inject malicious scripts into web pages that execute in users' browsers, stealing data, hijacking sessions, or defacing sites. Attackers inject scripts through user input, URL parameters, or third-party content that gets rendered without sanitization.

- **Trade-offs**: Preventing XSS requires input validation, output encoding, and Content Security Policy (CSP) headers. The catch is different contexts (HTML, JavaScript, CSS, URLs) need different encoding—use libraries like DOMPurify for HTML sanitization and always encode output based on context. React and Vue automatically escape content, but watch out for `dangerouslySetInnerHTML` or `v-html` which bypass protections.

Example:

```javascript
// ❌ Vulnerable - direct innerHTML
element.innerHTML = userInput; // XSS if userInput = "<img src=x onerror='steal()'>"

// ✅ Safe - textContent or React's automatic escaping
element.textContent = userInput;
// React: <div>{userInput}</div> // Automatically escaped

// ✅ Safe - sanitize HTML if you must render it
import DOMPurify from 'dompurify';
element.innerHTML = DOMPurify.sanitize(userInput);

// ✅ Content Security Policy header
// Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline'
```

---

## Q134. CSRF (Cross-Site Request Forgery)

CSRF attacks trick authenticated users into executing unwanted actions on sites where they're logged in by making requests from malicious sites. Attackers exploit the browser's automatic cookie sending to perform actions like changing passwords or transferring funds.

- **Trade-offs**: CSRF tokens validate requests originate from your site, while SameSite cookies prevent cross-site cookie sending. The catch is SameSite=Strict can break legitimate cross-site flows (like OAuth redirects), so use SameSite=Lax for GET requests and Strict for state-changing operations. Double-submit cookies provide defense-in-depth but require JavaScript—always use HTTPS to prevent token theft.

Example:

```javascript
// ✅ CSRF Token in form
<form action="/api/transfer" method="POST">
  <input type="hidden" name="csrfToken" value="{{csrfToken}}" />
  <input type="text" name="amount" />
  <button type="submit">Transfer</button>
</form>

// ✅ Verify token on server
app.post('/api/transfer', (req, res) => {
  if (req.body.csrfToken !== req.session.csrfToken) {
    return res.status(403).json({ error: 'Invalid CSRF token' });
  }
  // Process transfer
});

// ✅ SameSite cookie protection
Set-Cookie: sessionId=abc123; SameSite=Strict; Secure; HttpOnly

// ✅ Double-submit cookie pattern
// Set cookie and header with same random value, verify they match
```

---

## Q135. CORS

CORS (Cross-Origin Resource Sharing) allows browsers to make cross-origin requests while preventing unauthorized access. Browsers block cross-origin requests by default, but CORS headers let servers explicitly allow specific origins, methods, and headers.

- **Trade-offs**: CORS protects users from malicious sites accessing their data, but configuring it incorrectly can expose your API or break legitimate access. The catch is preflight requests (OPTIONS) add latency, and wildcard origins (`*`) don't work with credentials—always specify exact origins in production and use credentials only when necessary. Simple requests (GET, POST with certain headers) skip preflight, while complex requests require it.

Example:

```javascript
// ✅ Server CORS configuration
app.use(cors({
  origin: 'https://myapp.com', // Specific origin
  credentials: true, // Allow cookies
  methods: ['GET', 'POST', 'PUT'],
  allowedHeaders: ['Content-Type', 'Authorization']
}));

// ✅ Preflight request (browser sends automatically)
// OPTIONS /api/data
// Access-Control-Request-Method: POST
// Access-Control-Request-Headers: Content-Type

// ✅ Server response
// Access-Control-Allow-Origin: https://myapp.com
// Access-Control-Allow-Methods: GET, POST, PUT
// Access-Control-Allow-Headers: Content-Type, Authorization
// Access-Control-Allow-Credentials: true

// ✅ Client request with credentials
fetch('https://api.example.com/data', {
  credentials: 'include', // Send cookies
  headers: { 'Content-Type': 'application/json' }
});
```

---

## Q136. Clickjacking (iFrame Protection)

Clickjacking overlays invisible or disguised elements over legitimate content, tricking users into clicking buttons or links they didn't intend to. Attackers embed your site in an iframe and overlay their own content, making users perform actions like liking posts or authorizing payments.

- **Trade-offs**: X-Frame-Options and CSP frame-ancestors prevent your site from being embedded in iframes, blocking clickjacking. The catch is some legitimate use cases (like embedding widgets) require iframe access—use frame-ancestors with specific allowed origins instead of blanket blocking. Content Security Policy is more flexible than X-Frame-Options and supports multiple origins.

Example:

```javascript
// ✅ X-Frame-Options header (older, simpler)
// X-Frame-Options: DENY // Block all iframes
// X-Frame-Options: SAMEORIGIN // Allow same origin only

// ✅ Content Security Policy (modern, more flexible)
// Content-Security-Policy: frame-ancestors 'none' // Block all
// Content-Security-Policy: frame-ancestors 'self' // Same origin only
// Content-Security-Policy: frame-ancestors https://trusted.com // Specific origins

// ✅ Server configuration
app.use((req, res, next) => {
  res.setHeader('X-Frame-Options', 'DENY');
  res.setHeader("Content-Security-Policy", "frame-ancestors 'none'");
  next();
});

// ✅ JavaScript frame-busting (additional defense)
if (window.top !== window.self) {
  window.top.location = window.self.location;
}
```

---

## Q137. Security headers

Security headers provide defense-in-depth by instructing browsers to enforce security policies like Content Security Policy (CSP), HTTP Strict Transport Security (HSTS), and X-Content-Type-Options. These headers protect against XSS, clickjacking, MIME sniffing, and other attacks.

- **Trade-offs**: Security headers are powerful but can break functionality if misconfigured—CSP especially requires careful tuning to allow legitimate resources while blocking malicious ones. The catch is some headers (like HSTS) are cached by browsers, so test thoroughly before deploying—start with report-only mode for CSP to identify issues without breaking the site.

Example:

```javascript
// ✅ Comprehensive security headers
app.use((req, res, next) => {
  res.setHeader('Content-Security-Policy', "default-src 'self'; script-src 'self' 'unsafe-inline'");
  res.setHeader('Strict-Transport-Security', 'max-age=31536000; includeSubDomains');
  res.setHeader('X-Content-Type-Options', 'nosniff');
  res.setHeader('X-Frame-Options', 'DENY');
  res.setHeader('X-XSS-Protection', '1; mode=block');
  res.setHeader('Referrer-Policy', 'strict-origin-when-cross-origin');
  res.setHeader('Permissions-Policy', 'geolocation=(), microphone=(), camera=()');
  next();
});
```

---

## Q138. Client-side security

Client-side security protects data and functionality in the browser by validating input, sanitizing output, securing storage, and preventing client-side attacks. Never trust client-side validation alone—always validate on the server.

- **Trade-offs**: Client-side security improves user experience with immediate feedback, but the catch is it can be bypassed—never rely on client-side validation for security, always validate on the server. Use secure storage practices (httpOnly cookies for tokens, avoid storing secrets in localStorage), and be careful with third-party scripts that can access your data.

Example:

```javascript
// ✅ Client-side validation (UX only, not security)
function validateEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

// ✅ Always validate on server too
app.post('/api/register', (req, res) => {
  if (!isValidEmail(req.body.email)) {
    return res.status(400).json({ error: 'Invalid email' });
  }
  // Process registration
});

// ✅ Secure token storage
// Store in httpOnly cookie, not localStorage
res.cookie('token', token, { httpOnly: true, secure: true, sameSite: 'strict' });

// ❌ Don't store sensitive data in localStorage
// localStorage.setItem('token', token); // Vulnerable to XSS
```

---

## Q139. Secure communication (HTTPS)

HTTPS encrypts data in transit using TLS/SSL, preventing man-in-the-middle attacks, data interception, and tampering. Always use HTTPS for all web traffic, especially for authentication, payments, and sensitive data.

- **Trade-offs**: HTTPS adds initial latency (~100-300ms for TLS handshake) but enables secure communication and is required for modern web features (Service Workers, geolocation). The catch is HTTPS requires valid SSL certificates and proper configuration—use HSTS headers to force HTTPS and prevent downgrade attacks. HTTP/2 and HTTP/3 work over HTTPS and provide performance benefits.

Example:

```javascript
// ✅ Force HTTPS redirect
app.use((req, res, next) => {
  if (req.header('x-forwarded-proto') !== 'https') {
    res.redirect(`https://${req.header('host')}${req.url}`);
  } else {
    next();
  }
});

// ✅ HSTS header (force HTTPS for future visits)
// Strict-Transport-Security: max-age=31536000; includeSubDomains; preload

// ✅ Secure cookie flag (only send over HTTPS)
res.cookie('session', sessionId, { secure: true });

// ✅ Mixed content protection
// Content-Security-Policy: upgrade-insecure-requests
```

---

## Q140. Dependency security

Dependency security involves keeping third-party packages updated, scanning for vulnerabilities, and using tools like npm audit or Snyk to identify and fix security issues. Regularly update dependencies and monitor for security advisories.

- **Trade-offs**: Keeping dependencies updated reduces security risks but can introduce breaking changes—use automated tools to scan for vulnerabilities and update regularly. The catch is some vulnerabilities require immediate patching (critical CVEs), while others can wait for scheduled updates—prioritize critical security updates and test thoroughly before deploying.

Example:

```javascript
// ✅ Check for vulnerabilities
// npm audit
// npm audit fix

// ✅ Use automated dependency updates
// Dependabot, Renovate, or Snyk

// ✅ Lock file security
// package-lock.json or yarn.lock ensures consistent versions

// ✅ Review dependencies before adding
// Check package popularity, maintenance, and security history

// ✅ Use minimal dependencies
// Fewer dependencies = smaller attack surface
```

---

## Q141. Compliance and regulation

Compliance involves adhering to regulations like GDPR, CCPA, HIPAA, and PCI-DSS that govern data privacy, security, and handling. Implement proper data protection, user consent, and audit trails to meet compliance requirements.

- **Trade-offs**: Compliance protects users and avoids legal penalties, but implementing compliance measures adds complexity and cost. The catch is different regulations have different requirements—GDPR requires user consent and data portability, PCI-DSS requires secure payment processing, HIPAA requires healthcare data protection. Always consult legal experts for compliance requirements.

Example:

```javascript
// ✅ GDPR compliance - user consent
function requestConsent() {
  if (!localStorage.getItem('consent')) {
    showConsentBanner();
  }
}

// ✅ Data portability (GDPR)
app.get('/api/user/data', (req, res) => {
  const userData = getUserData(req.user.id);
  res.json(userData); // Allow users to export their data
});

// ✅ Data deletion (GDPR right to be forgotten)
app.delete('/api/user/data', (req, res) => {
  deleteUserData(req.user.id);
  res.json({ deleted: true });
});

// ✅ Audit logging for compliance
function logAccess(userId, resource, action) {
  auditLog.create({ userId, resource, action, timestamp: new Date() });
}
```

---

## Q142. Input validation and sanitization

Input validation checks that data meets expected format and constraints, while sanitization removes or neutralizes potentially dangerous content. Always validate and sanitize all user input on both client and server side.

- **Trade-offs**: Client-side validation improves UX with immediate feedback, but the catch is it can be bypassed—always validate on the server for security. Sanitization prevents XSS and injection attacks but can remove legitimate content if too aggressive—use context-aware sanitization (HTML, JavaScript, SQL, URLs need different approaches).

Example:

```javascript
// ✅ Input validation
function validateInput(input, type) {
  switch (type) {
    case 'email':
      return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(input);
    case 'url':
      try { new URL(input); return true; } catch { return false; }
    case 'number':
      return !isNaN(input) && isFinite(input);
    default:
      return input.length > 0 && input.length < 1000;
  }
}

// ✅ HTML sanitization
import DOMPurify from 'dompurify';
const clean = DOMPurify.sanitize(userInput, { ALLOWED_TAGS: ['b', 'i'] });

// ✅ SQL injection prevention (parameterized queries)
db.query('SELECT * FROM users WHERE id = ?', [userId]);

// ✅ Server-side validation
app.post('/api/users', (req, res) => {
  const { email, name } = req.body;
  if (!validateEmail(email) || !validateName(name)) {
    return res.status(400).json({ error: 'Invalid input' });
  }
  // Process request
});
```

---

## Q143. Server-Side Request Forgery (SSRF)

SSRF attacks trick servers into making requests to internal or external resources, potentially exposing internal networks or bypassing firewalls. Attackers exploit server-side functionality that makes HTTP requests based on user input.

- **Trade-offs**: SSRF is primarily a server-side vulnerability, but frontend developers should validate URLs before sending them to the server. The catch is SSRF can expose internal services, cloud metadata, or bypass authentication—always validate and whitelist allowed URLs on the server, and never make requests to internal IPs or localhost based on user input.

Example:

```javascript
// ❌ Vulnerable - user controls URL
fetch(userProvidedUrl); // SSRF if user provides internal URL

// ✅ Client-side validation (helps but server must validate too)
function isValidUrl(url) {
  try {
    const parsed = new URL(url);
    // Block internal IPs
    if (parsed.hostname === 'localhost' || parsed.hostname.startsWith('127.') || parsed.hostname.startsWith('192.168.')) {
      return false;
    }
    // Only allow HTTP/HTTPS
    return parsed.protocol === 'http:' || parsed.protocol === 'https:';
  } catch {
    return false;
  }
}

// ✅ Server-side validation (critical)
app.post('/api/fetch', (req, res) => {
  const url = req.body.url;
  if (!isAllowedUrl(url)) { // Whitelist allowed domains
    return res.status(400).json({ error: 'URL not allowed' });
  }
  // Make request
});
```

---

## Q144. Server-side JavaScript Injection (SSJI)

SSJI attacks inject malicious JavaScript code that executes on the server, potentially allowing remote code execution, data theft, or server compromise. This occurs when user input is evaluated as JavaScript code on the server.

- **Trade-offs**: SSJI is a server-side vulnerability, but frontend developers should avoid sending executable code to the server. The catch is using `eval()`, `Function()`, or `setTimeout()` with user input on the server is dangerous—never evaluate user input as code, use safe serialization formats like JSON, and validate all server inputs.

Example:

```javascript
// ❌ Vulnerable - evaluating user input
eval(userInput); // SSJI if userInput = "require('child_process').exec('rm -rf /')"

// ❌ Vulnerable - Function constructor
new Function(userInput)(); // Dangerous

// ✅ Safe - use JSON for data
const data = JSON.parse(userInput); // Safe if input is valid JSON

// ✅ Safe - use parameterized queries, not string concatenation
db.query('SELECT * FROM users WHERE name = ?', [userInput]);

// ✅ Frontend - validate before sending
function sanitizeInput(input) {
  // Remove any code-like patterns
  return input.replace(/[<>{}[\]();]/g, '');
}
```

---

## Q145. Feature Policy (Permissions-Policy)

Permissions-Policy (formerly Feature Policy) controls which browser features and APIs can be used in your application, preventing abuse of sensitive APIs like geolocation, camera, microphone, or payment APIs. This helps prevent malicious scripts from accessing sensitive features.

- **Trade-offs**: Permissions-Policy provides fine-grained control over browser features, but the catch is it can break legitimate functionality if too restrictive—test thoroughly and allow features only where needed. Use it to disable unused features and reduce attack surface, especially for third-party scripts.

Example:

```javascript
// ✅ Permissions-Policy header
// Permissions-Policy: geolocation=(), microphone=(), camera=(), payment=()

// ✅ Allow specific origins
// Permissions-Policy: geolocation=(self "https://maps.example.com")

// ✅ Server configuration
app.use((req, res, next) => {
  res.setHeader('Permissions-Policy', 
    'geolocation=(), microphone=(), camera=(), payment=(), usb=(), magnetometer=()'
  );
  next();
});

// ✅ Check feature availability before using
if ('geolocation' in navigator) {
  navigator.geolocation.getCurrentPosition(handlePosition);
}
```

---

## Q146. Subresource Integrity (SRI)

SRI allows browsers to verify that resources (scripts, stylesheets) loaded from CDNs haven't been tampered with by checking cryptographic hashes. This protects against compromised CDNs or man-in-the-middle attacks.

- **Trade-offs**: SRI provides strong protection against resource tampering, but the catch is it requires updating hashes whenever resources change—use automated tools to generate SRI hashes during build. SRI only works for same-origin or CORS-enabled resources, and browsers will block resources that don't match the hash.

Example:

```javascript
// ✅ SRI hash for script
// Generate hash: openssl dgst -sha384 -binary script.js | openssl base64 -A

<script 
  src="https://cdn.example.com/library.js"
  integrity="sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/uxy9rx7HNQlGYl1kPzQho1wx4JwY8wC"
  crossorigin="anonymous">
</script>

// ✅ SRI hash for stylesheet
<link 
  rel="stylesheet"
  href="https://cdn.example.com/styles.css"
  integrity="sha384-..."
  crossorigin="anonymous">

// ✅ Generate SRI hashes automatically
// webpack-subresource-integrity plugin
// or: npm install --save-dev webpack-subresource-integrity
```

---

