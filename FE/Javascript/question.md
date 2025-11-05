# ⚡️ JavaScript Interview Questions

180 carefully curated questions covering JavaScript fundamentals to advanced topics, including 50 output-based questions.

## 📋 Quick Navigation

| Section | Topic | Questions | Difficulty |
|---------|-------|-----------|------------|
| [1️⃣](#1-core-javascript-fundamentals) | Core JavaScript Fundamentals | Q1–15 | ⭐⭐ |
| [2️⃣](#2-functions-closures--execution-context) | Functions, Closures & Execution Context | Q16–25 | ⭐⭐⭐ |
| [3️⃣](#3-promises-asyncawait-and-event-loop) | Promises, Async/Await & Event Loop | Q26–51 | ⭐⭐⭐⭐ |
| [4️⃣](#4-objects-prototypes--inheritance) | Objects, Prototypes & Inheritance | Q52–71 | ⭐⭐⭐ |
| [6️⃣](#6-es6-features) | ES6+ Features | Q72–81 | ⭐⭐ |
| [8️⃣](#8-practical-javascript-questions) | Practical JavaScript Questions | Q82–110 | ⭐⭐⭐⭐ |
| [9️⃣](#9-web-workers--service-workers) | Web Workers & Service Workers | Q111–120 | ⭐⭐⭐⭐ |
| [🔟](#10-real-world--edge-javascript-topics) | Real-World & Edge Topics | Q121–130 | ⭐⭐⭐ |
| [1️⃣1️⃣](#11-javascript-output-questions) | JavaScript Output Questions | Q131–180 | ⭐⭐⭐⭐ |

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

16. What is a closure?
17. What are higher-order functions?
18. What is function currying and how do you implement it?
19. What are IIFEs (Immediately Invoked Function Expressions)?
20. How does the `this` keyword behave in different contexts?
21. What is the call stack?
22. What happens in the creation and execution phases of JavaScript?
23. What is the difference between synchronous and asynchronous execution?
24. How does lexical environment relate to closures?
25. What is the difference between function declaration and arrow function `this` binding?

## ⚡ 3. Promises, Async/Await & Event Loop

26. What is a Promise in JavaScript?
27. What is the difference between callbacks and Promises?
28. How do you chain Promises?
29. What is async/await and how does it work?
30. What is the difference between Promise.resolve() and new Promise()?
31. How do you handle errors in Promises?
32. What is callback hell and how do you avoid it?
33. What is the Event Loop in JavaScript?
34. What is the difference between microtasks and macrotasks?
35. How do you run Promises concurrently?
36. What is Promise.all() and when do you use it?
37. What is Promise.race() and when do you use it?
38. What is Promise.allSettled() and when do you use it?
39. What is Promise.any() and when do you use it?
40. How do you implement retry logic with Promises?
41. What is Promise cancellation and how do you implement it?
42. How do you run Promises sequentially?
43. How do you implement progress updates with Promises?
44. What is Promise.finally() and when do you use it?
45. How do you mix Promises and async/await?
46. What is the difference between Promise and async/await?
47. How do you handle multiple async operations?
48. What is the difference between Promise and Observable?
49. How do you implement timeout with Promises?
50. What is the difference between Promise and Generator?
51. How does the fetch Promise work internally in V8?

## 🏗️ 4. Objects, Prototypes & Inheritance

52. What is an object in JavaScript?
53. What is the difference between object literal and object constructor?
54. What is a prototype in JavaScript?
55. What is __proto__ in JavaScript?
56. What is the prototype chain?
57. What is the difference between `__proto__` and `prototype`?
58. What is the difference between `hasOwnProperty` and `in` operator?
59. What is the difference between `Object.create()` and `new` operator?
60. What is the difference between `Object.assign()` and spread operator?
61. What is the difference between `Object.freeze()` and `Object.seal()`?
62. What is the difference between `Object.keys()` and `Object.getOwnPropertyNames()`?
63. What is the difference between `Object.entries()` and `Object.values()`?
64. What are getters and setters in JavaScript?
65. What are classes in JavaScript?
66. What is the difference between class declaration and class expression?
67. What is the `extends` keyword and how does it work?
68. What is `super()` and when do you use it?
69. What are static members in classes?
70. What are private class fields?
71. What is the difference between ES6 classes and prototype-based inheritance?

## 🚀 6. ES6+ Features

72. What is destructuring assignment?
73. What is the spread operator and how do you use it?
74. What is the rest parameter and how do you use it?
75. What is template literals and how do you use it?
76. What is the difference between `let` and `const`?
77. What are ES modules and how do you use them?
78. What are generators and how do you use them?
79. What are async generators?
80. What are Symbols and how do you use them?
81. What are Maps, Sets, WeakMaps, and WeakSets?

## 🛠️ 8. Practical JavaScript Questions

82. How do you implement a debounce function?
83. How do you implement a throttle function?
84. How do you implement a deep clone function?
85. How do you implement a memoization function?
86. How do you implement a curry function?
87. How do you implement a compose function?
88. How do you implement a pipe function?
89. How do you implement a flatten function?
90. How do you implement a unique function?
91. How do you implement a groupBy function?
92. How do you implement a chunk function?
93. How do you implement a zip function?
94. How do you implement a unzip function?
95. How do you implement a intersection function?
96. How do you implement a difference function?
97. How do you implement a union function?
98. How do you implement a symmetricDifference function?
99. How do you implement a isEqual function?
100. How do you implement a isEmpty function?
101. How do you implement a isArray function?
102. How do you implement useMemo from scratch?
103. How do you implement useCallback from scratch?
104. What is Compact Number (Intl.NumberFormat)?
105. Explain why the following doesn't work as an IIFE: function foo(){ }();. What needs to be changed to properly make it an IIFE?
106. What are JavaScript object property flags and descriptors?
107. What are server-sent events?
108. What are proxies in JavaScript used for?
109. What are some techniques for reducing reflows and repaints?
110. What are some tools that can be used to measure and analyze JavaScript performance?

## 🔧 9. Web Workers & Service Workers

111. What is a Web Worker and how do you use it?
112. What is the difference between Web Worker and Service Worker?
113. What is the difference between Dedicated Worker and Shared Worker?
114. What are the restrictions on what Web Workers can access?
115. How do Web Workers communicate with the main thread?
116. What is a Service Worker and how do you use it?
117. What is the Service Worker lifecycle?
118. How do you implement offline caching with Service Workers?
119. What is the difference between Web Workers and Service Workers?
120. How do you unregister a Service Worker?

## 🌟 10. Real-World & Edge Topics

121. What is event delegation and how does it work?
122. What is event bubbling and event capturing?
123. What is Shadow DOM and how does it work?
124. What is the difference between `innerHTML`, `textContent`, and `innerText`?
125. What is the difference between `for...in` and `for...of` loops?
126. What are polyfills and how do you create them?
127. What are data attributes and how do you use them?
128. What are pure functions and side effects?
129. What are memory leaks and how do you prevent them?
130. What is tail call optimization?

## 🎯 11. JavaScript Output Questions

131. What will be the output of the following code? (var hoisting)
132. What will be the output of the following code? (let TDZ)
133. What will be the output of the following code? (function hoisting)
134. What will be the output of the following code? (typeof null)
135. What will be the output of the following code? (0.1 + 0.2 == 0.3)
136. What will be the output of the following code? (0.1 + 0.2 === 0.3)
137. What will be the output of the following code? ('5' + 3)
138. What will be the output of the following code? ('5' - 3)
139. What will be the output of the following code? ('5' * 2)
140. What will be the output of the following code? ('5' / 2)
141. What will be the output of the following code? (typeof NaN)
142. What will be the output of the following code? (post-increment)
143. What will be the output of the following code? (pre-increment)
144. What will be the output of the following code? (1 + '1' - 1)
145. What will be the output of the following code? (1 + true)
146. What will be the output of the following code? (1 + false)
147. What will be the output of the following code? ('5' + true)
148. What will be the output of the following code? ('5' - true)
149. What will be the output of the following code? ([] + [])
150. What will be the output of the following code? ([] + {})
151. What will be the output of the following code? ({} + [])
152. What will be the output of the following code? ([1,2,3] + [4,5])
153. What will be the output of the following code? (array destructuring)
154. What will be the output of the following code? (object spread)
155. What will be the output of the following code? (NaN === NaN)
156. What will be the output of the following code? (NaN == NaN)
157. What will be the output of the following code? (null == undefined)
158. What will be the output of the following code? (null === undefined)
159. What will be the output of the following code? (0 == false)
160. What will be the output of the following code? (0 === false)
161. What will be the output of the following code? ('' == false)
162. What will be the output of the following code? ('' === false)
163. What will be the output of the following code? (this in function)
164. What will be the output of the following code? (this in strict mode)
165. What will be the output of the following code? (this in method)
166. What will be the output of the following code? (this in setTimeout callback)
167. What will be the output of the following code? (this in arrow function)
168. What will be the output of the following code? (var in loop with setTimeout)
169. What will be the output of the following code? (let in loop with setTimeout)
170. What will be the output of the following code? (closure)
171. What will be the output of the following code? (IIFE in loop)
172. What will be the output of the following code? (typeof function)
173. What will be the output of the following code? (typeof array)
174. What will be the output of the following code? (Array.isArray)
175. What will be the output of the following code? (instanceof Array)
176. What will be the output of the following code? (array length)
177. What will be the output of the following code? (sparse array)
178. What will be the output of the following code? ([1,2,3] == [1,2,3])
179. What will be the output of the following code? (array reference)
180. What will be the output of the following code? (string split)

---

## 📖 Complete Answer Guide

- [1) Core JavaScript Fundamentals](1%20Core%20JavaScript%20Fundamentals.md) - Q1-15
- [2) Functions, Closures & Execution Context](2%20Functions%2C%20Closures%20%26%20Execution%20Context.md) - Q16-25
- [3) Promises, Async/Await & Event Loop](3%20Promises%2C%20Async-Await%20%26%20Event%20Loop.md) - Q26-51
- [4) Objects, Prototypes & Inheritance](4%20Objects%2C%20Prototypes%20%26%20Inheritance.md) - Q52-71
- [6) ES6+ Features](6%20ES6%2B%20Features.md) - Q72-81
- [8) Practical JavaScript Questions](8%20Practical%20JavaScript%20Questions.md) - Q82-110
- [9) Web Workers & Service Workers](9%20Web%20Workers%20%26%20Service%20Workers.md) - Q111-120
- [10) Real-World & Edge Topics](10%20Real-World%20%26%20Edge%20JavaScript%20Topics.md) - Q121-130
- [11) JavaScript Output Questions](11%20JavaScript%20Output%20Questions.md) - Q131-180

## 📝 Cheatsheet

[JavaScript Interview Cheatsheet](JavaScript%20Interview%20Cheatsheet.md) - Quick reference guide
