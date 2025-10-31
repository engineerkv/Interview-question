# ⚡️ JavaScript Interview Questions

146 carefully curated questions covering JavaScript fundamentals to advanced topics.

## 📋 Quick Navigation

| Section | Topic | Questions | Difficulty |
|---------|-------|-----------|------------|
| [1️⃣](#1-core-javascript-fundamentals) | Core JavaScript Fundamentals | Q1–15 | ⭐⭐ |
| [2️⃣](#2-functions-closures--execution-context) | Functions, Closures & Execution Context | Q16–25 | ⭐⭐⭐ |
| [3️⃣](#3-promises-asyncawait-and-event-loop) | Promises, Async/Await & Event Loop | Q26–51 | ⭐⭐⭐⭐ |
| [4️⃣](#4-objects-prototypes--inheritance) | Objects, Prototypes & Inheritance | Q52–63 | ⭐⭐⭐ |
| [5️⃣](#5-classes--inheritance-es6) | Classes & Inheritance (ES6+) | Q64–73 | ⭐⭐⭐ |
| [6️⃣](#6-es6-features) | ES6+ Features | Q66–75 | ⭐⭐ |
| [7️⃣](#7-v8-engine-internals-step-by-step-deep-dive) | V8 Engine Internals - Deep Dive | Q76–88 | ⭐⭐⭐⭐⭐ |
| [8️⃣](#8-practical-javascript-questions) | Practical JavaScript Questions | Q78–109 | ⭐⭐⭐⭐ |
| [9️⃣](#9-web-workers--service-workers) | Web Workers & Service Workers | Q120–129 | ⭐⭐⭐⭐ |
| [🔟](#10-real-world--edge-javascript-topics) | Real-World & Edge Topics | Q130–139 | ⭐⭐⭐ |

## 🧠 1. Core JavaScript Fundamentals

1. What are the different data types in JavaScript?
2. What is the difference between `var`, `let`, and `const`?
3. What is the difference between `==` and `===`?
4. Explain hoisting in JavaScript.
5. What is scope (global, local, block)?
6. What is the difference between null and undefined?
7. What are function declarations vs function expressions?
8. What are arrow functions and how do they differ from regular functions?
9. What are first-class functions in JavaScript?
10. What is lexical scope?
11. What will "typeof NaN" return and why?
12. What will [2] == [2] return and why?
13. What does 0.1 + 0.2 === 0.3 evaluate to and why?
14. What will '5' + 3 and '5' - 3 return?
15. What are different ways to create an object in JavaScript?

## 🧩 2. Functions, Closures & Execution Context

11. What is a closure?
12. What is the difference between function declaration and function expression?
13. What is the execution context in JavaScript?
14. What is the call stack?
15. What is the difference between synchronous and asynchronous JavaScript?
16. What is lexical environment?
17. How does the `this` keyword work in JavaScript?
18. What is the difference between call, apply, and bind?
19. What is a higher-order function?
20. What is currying in JavaScript?

## ⚡ 3. Promises, Async/Await & Event Loop

21. What is a Promise in JavaScript?
22. What is the difference between callbacks and Promises?
23. How do you chain Promises?
24. What is async/await and how does it work?
25. What is the difference between Promise.resolve() and new Promise()?
26. How do you handle errors in Promises?
27. What is callback hell and how do you avoid it?
28. What is the Event Loop in JavaScript?
29. What is the difference between microtasks and macrotasks?
30. How do you run Promises concurrently?
31. What is Promise.all() and when do you use it?
32. What is Promise.race() and when do you use it?
33. What is Promise.allSettled() and when do you use it?
34. What is Promise.any() and when do you use it?
35. How do you implement retry logic with Promises?
36. What is Promise cancellation and how do you implement it?
37. How do you run Promises sequentially?
38. How do you implement progress updates with Promises?
39. What is Promise.finally() and when do you use it?
40. How do you mix Promises and async/await?
41. What is the difference between Promise and async/await?
42. How do you handle multiple async operations?
43. What is the difference between Promise and Observable?
44. How do you implement timeout with Promises?
45. What is the difference between Promise and Generator?
46. How does the fetch Promise work internally in V8?

## 🏗️ 4. Objects, Prototypes & Inheritance

46. What is an object in JavaScript?
47. What is the difference between object literal and object constructor?
48. What is a prototype in JavaScript?
49. What is __proto__ in JavaScript?
50. What is the prototype chain?
51. What is the difference between `__proto__` and `prototype`?
52. What is the difference between `hasOwnProperty` and `in` operator?
53. What is the difference between `Object.create()` and `new` operator?
54. What is the difference between `Object.assign()` and spread operator?
55. What is the difference between `Object.freeze()` and `Object.seal()`?
56. What is the difference between `Object.keys()` and `Object.getOwnPropertyNames()`?
57. What is the difference between `Object.entries()` and `Object.values()`?

## 🏛️ 5. Classes & Inheritance (ES6+)

58. What is a class in JavaScript?
59. What is the difference between class and function constructor?
60. What is the difference between `static` and instance methods?
61. What is the difference between `public` and `private` fields?
62. What is the difference between `extends` and `implements`?
63. What is the difference between `super()` and `super.method()`?
64. What is the difference between `get` and `set` methods?
65. What is the difference between `Symbol` and `Symbol.for()`?
66. What is the difference between `Symbol.iterator` and `Symbol.asyncIterator`?
67. What is the difference between `Symbol.toPrimitive` and `valueOf()`?

## 🚀 6. ES6+ Features

68. What is destructuring assignment?
69. What is the spread operator and how do you use it?
70. What is the rest parameter and how do you use it?
71. What is template literals and how do you use it?
72. What is the difference between `let` and `const`?
73. What is the difference between `var` and `let`?
74. What is the difference between `const` and `let`?
75. What is the difference between `const` and `var`?
76. What is the difference between `const` and `var`?
77. What is the difference between `const` and `var`?

## ⚙️ 7. V8 Engine Internals: Step-by-Step Deep Dive

78. What is the V8 engine and how does it work?
79. What is the difference between compilation and interpretation?
80. What is the difference between JIT and AOT compilation?
81. What is the difference between garbage collection and memory management?
82. What is the difference between heap and stack memory?
83. What is the difference between shallow and deep copying?
84. What is the difference between `Object.assign()` and spread operator?
85. What is the difference between `Object.freeze()` and `Object.seal()`?
86. What is the difference between `Object.keys()` and `Object.getOwnPropertyNames()`?
87. What is the difference between `Object.entries()` and `Object.values()`?
88. How does the Fetch API work internally in V8?

## 🛠️ 8. Practical JavaScript Questions

89. How do you implement a debounce function?
90. How do you implement a throttle function?
91. How do you implement a deep clone function?
92. How do you implement a memoization function?
93. How do you implement a curry function?
94. How do you implement a compose function?
95. How do you implement a pipe function?
96. How do you implement a flatten function?
97. How do you implement a unique function?
98. How do you implement a groupBy function?
99. How do you implement a chunk function?
100. How do you implement a zip function?
101. How do you implement a unzip function?
102. How do you implement a intersection function?
103. How do you implement a difference function?
104. How do you implement a union function?
105. How do you implement a symmetricDifference function?
106. How do you implement a isEqual function?
107. How do you implement a isEmpty function?
108. How do you implement a isArray function?
109. How do you implement useMemo from scratch?
110. How do you implement useCallback from scratch?
111. What is Compact Number (Intl.NumberFormat)?
112. Explain why the following doesn't work as an IIFE: function foo(){ }();. What needs to be changed to properly make it an IIFE?
113. What are JavaScript object property flags and descriptors?
114. What are server-sent events?
115. What are proxies in JavaScript used for?
116. What are some techniques for reducing reflows and repaints?
117. What are some tools that can be used to measure and analyze JavaScript performance?
118. Explain the concept of a microtask queue?
119. How do you check HTTP status codes in axios and fetch API?
120. How can you optimize DOM manipulation for better performance?

## 🔧 9. Web Workers & Service Workers

120. What is a Web Worker and how do you use it?
121. What is the difference between Web Worker and Service Worker?
122. What is the difference between Dedicated Worker and Shared Worker?
123. What is the difference between Web Worker and iframe?
124. What is the difference between Web Worker and WebSocket?
125. What is the difference between Web Worker and WebRTC?
126. What is the difference between Web Worker and WebAssembly?
127. What is the difference between Web Worker and WebGL?
128. What is the difference between Web Worker and Web Audio API?
129. What is the difference between Web Worker and Web Crypto API?

## 🌟 10. Real-World & Edge Topics

130. What is the difference between JavaScript and TypeScript?
131. What is the difference between JavaScript and CoffeeScript?
132. What is the difference between JavaScript and Dart?
133. What is the difference between JavaScript and Python?
134. What is the difference between JavaScript and Java?
135. What is the difference between JavaScript and C#?
136. What is the difference between JavaScript and Go?
137. What is the difference between JavaScript and Rust?
138. What is the difference between JavaScript and Swift?
139. What is the difference between JavaScript and Kotlin?

---

## 📖 Complete Answer Guide

- [1) Core JavaScript Fundamentals](1%20Core%20JavaScript%20Fundamentals.md) - Q1-10
- [2) Functions, Closures & Execution Context](2%20Functions%2C%20Closures%20%26%20Execution%20Context.md) - Q11-20
- [3) Promises, Async/Await & Event Loop](3%20Promises%2C%20Async-Await%20%26%20Event%20Loop.md) - Q21-46
- [4) Objects, Prototypes & Inheritance](4%20Objects%2C%20Prototypes%20%26%20Inheritance.md) - Q46-55
- [5) Classes & Inheritance (ES6+)](5%20Classes%20%26%20Inheritance%20%28ES6%2B%29.md) - Q56-65
- [6) ES6+ Features](6%20ES6%2B%20Features.md) - Q66-75
- [7) V8 Engine Internals - Deep Dive](7%20V8%20Engine%20Internals%20-%20Deep%20Dive.md) - Q76-88
- [8) Practical JavaScript Questions](8%20Practical%20JavaScript%20Questions.md) - Q78-109
- [9) Web Workers & Service Workers](9%20Web%20Workers%20%26%20Service%20Workers.md) - Q120-129
- [10) Real-World & Edge Topics](10%20Real-World%20%26%20Edge%20Topics.md) - Q130-139

## 📝 Cheatsheet

[JavaScript Interview Cheatsheet](JavaScript%20Interview%20Cheatsheet.md) - Quick reference guide