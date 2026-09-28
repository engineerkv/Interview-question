---
sidebar_label: "Question Index"
sidebar_position: 0
---
# ⚡️ JavaScript Interview Questions

> **Reviewed:** 2026-09 · Modernized; legacy topics are labeled.

Numbered up to Q212, covering JavaScript fundamentals to advanced topics, including 60 output-based questions. Examples use ES modules (`import`/`export`) by default; CommonJS is called out as legacy/Node interop where it appears.

> **Numbering note:** Question numbers **Q9–Q15** and **Q127** are intentionally unused - nothing is missing. Existing numbers are kept stable so links and notes that reference them don't break. The five questions added in the 2026 review continue from the highest number (Q208–Q212).

## 📋 Quick Navigation

| Section | Topic | Questions | Difficulty |
|---------|-------|-----------|------------|
| [1️⃣](#1-core-javascript-fundamentals) | Fundamentals & Core Concepts | Q1–8 | ⭐⭐ |
| [2️⃣](#2-functions-closures--execution-context) | Functions & Execution Context | Q16–24 | ⭐⭐⭐ |
| [3️⃣](#3-objects-prototypes--inheritance) | Objects & Prototypes | Q25–43 | ⭐⭐⭐ |
| [4️⃣](#4-es6-features) | Modern JavaScript (ES6+) | Q44–53 | ⭐⭐ |
| [5️⃣](#5-promises-asyncawait-and-event-loop) | Asynchronous Programming | Q54–79 | ⭐⭐⭐⭐ |
| [6️⃣](#6-practical-javascript-questions) | Practical Coding Challenges | Q80–126 | ⭐⭐⭐⭐ |
| [7️⃣](#7-web-workers-service-workers--real-world-topics) | Web APIs & Real-World Topics | Q128–147, Q208–212 | ⭐⭐⭐⭐ |
| [8️⃣](#8-javascript-output-questions) | Output-Based Questions | Q148–207 | ⭐⭐⭐⭐ |

## 🧠 1. Fundamentals & Core Concepts

1. Data types in JavaScript

2. `==` vs `===` in JavaScript

3. `null` vs `undefined`

4. First-class functions in JavaScript

5. `typeof NaN` return value and why

6. `[2] == [2]` return value and why

7. `0.1 + 0.2 === 0.3` evaluation and why

8. `'5' + 3` and `'5' - 3` return values

## 🧩 2. Functions & Execution Context

22. Creation and execution phases in JavaScript

21. Call stack in JavaScript

24. How lexical environment relates to closures

16. Closures in JavaScript

17. Higher-order functions

18. Function currying: what it is and how to implement it

19. IIFEs (Immediately Invoked Function Expressions)

20. How `this` keyword behaves in different contexts

23. Synchronous vs asynchronous execution

## 🏗️ 3. Objects & Prototypes

25. Objects in JavaScript

26. Prototype in JavaScript

28. Prototype chain

27. `__proto__` in JavaScript

29. `__proto__` vs `prototype`

31. `Object.create()` vs `new` operator

30. `hasOwn` vs `in` operator

32. `Object.assign()` vs spread operator

33. `Object.freeze()` vs `Object.seal()`

34. `Object.keys()` vs `Object.getOwnPropertyNames()`

35. `Object.entries()` vs `Object.values()` vs `Object.keys()`

36. Getters and setters in JavaScript

37. Classes in JavaScript

38. Class declaration vs class expression

39. `extends` keyword: what it is and how it works

40. `super()`: what it is and when to use it

41. Static members in classes

42. Private class fields

43. ES6 classes vs prototype-based inheritance

## 🎯 4. Modern JavaScript (ES6+)

44. Destructuring assignment

45. Spread operator: what it is and how to use it

46. Rest parameter: what it is and how to use it

47. Template literals: what they are and how to use them

48. `let` vs `const`

49. ES modules: what they are and how to use them

50. Generators: what they are and how to use them

51. Async generators

52. Symbols: what they are and how to use them

53. Maps, Sets, WeakMaps, and WeakSets

## ⚡ 5. Asynchronous Programming

54. Promises in JavaScript

55. Callbacks vs Promises

56. Chaining Promises

57. Async/await: what it is and how it works

58. `Promise.resolve()` vs `new Promise()`

59. Handling errors in Promises

60. Callback hell: what it is and how to avoid it

61. Event Loop in JavaScript

62. Microtasks vs macrotasks

63. Running Promises concurrently

64. `Promise.all()`: what it is and when to use it

65. `Promise.race()`: what it is and when to use it

66. `Promise.allSettled()`: what it is and when to use it

67. `Promise.any()`: what it is and when to use it

68. Implementing retry logic with Promises

69. Promise cancellation: what it is and how to implement it

70. Running Promises sequentially

71. Implementing progress updates with Promises

72. `Promise.finally()`: what it is and when to use it

73. Promise vs async/await: differences and mixing them

74. Handling multiple async operations

75. Promise vs Observable

76. Implementing timeout with Promises

77. Promise vs Generator

78. How fetch Promise works internally in V8

79. Promise chaining and error propagation

## 🛠️ 6. Practical Coding Challenges

80-126. Practical coding challenges covering debounce, throttle, promises (all, race, any, allSettled), closures, event loop, prototypes, array chunking, worker pools, and advanced language features.

## 🔧 7. Web APIs & Real-World Topics

128. Web Workers and how they work

129. What can't be accessed inside a Web Worker

130. Communicating between the main thread and a Web Worker

131. Shared Workers

132. Service Workers

133. Lifecycle events of a Service Worker (install, activate, fetch)

134. How Service Workers enable offline caching

135. Difference between Web Workers and Service Workers

136. Handling background sync or push notifications

137. Unregistering a Service Worker

138. Event delegation

139. Event bubbling and capturing

140. Shadow DOM

141. Difference between `innerHTML`, `textContent`, and `innerText`

142. Difference between `for...in` and `for...of`

143. Polyfill and when to use one

144. Data attributes and how to access them in JavaScript

145. Pure functions and side effects

146. Memory leak and how to detect it

147. How JavaScript handles tail call optimization (TCO)

### Added in 2026 review (in the Web APIs file)

208. `AbortController` and cancelling async work

209. `structuredClone()` vs `JSON.parse(JSON.stringify())`

210. ES modules in the browser

211. Web Workers vs the main thread: what goes where?

212. Event loop ordering with `await` - predict the output

## 📝 8. Output-Based Questions

148-207. Tricky JavaScript output-based questions covering event loop, async/await, closures, prototypes, `this` binding, and other JavaScript traps commonly asked in interviews.

---

## 📖 Complete Answer Guide

- [1) Fundamentals & Core Concepts](./01-fundamentals-and-core-concepts.md) - Q1-8

- [2) Functions & Execution Context](./02-functions-and-execution-context.md) - Q16-24

- [3) Objects & Prototypes](./03-objects-and-prototypes.md) - Q25-43

- [4) Modern JavaScript (ES6+)](./04-modern-javascript-es6-plus.md) - Q44-53

- [5) Asynchronous Programming](./05-asynchronous-programming.md) - Q54-79

- [6) Practical Coding Challenges](./06-practical-coding-challenges.md) - Q80-126

- [7) Web APIs & Real-World Topics](./07-web-apis-and-real-world-topics.md) - Q128-147, Q208-212

- [8) Output-Based Questions](./08-output-based-questions.md) - Q148-207

## 📝 Cheatsheet

[JavaScript Interview Cheatsheet](./cheatsheet.md) - Quick reference guide
