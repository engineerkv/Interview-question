# 🧩 DSA Interview Notes - LeetCode Top 150

## 🧱 Section 6 — Stack / Queue / Design — Q53-Q60

---

### 53. 🧱 Valid Parentheses

**🧠 Concept**

Check if parentheses are valid using stack to match opening and closing brackets.

**💻 Example**

```javascript
function isValid(s) {
  const stack = [];
  const pairs = { '(': ')', '[': ']', '{': '}' };
  
  for (const char of s) {
    if (pairs[char]) {
      stack.push(char);
    } else if (stack.length === 0 || pairs[stack.pop()] !== char) {
      return false;
    }
  }
  
  return stack.length === 0;
}
```

**💬 Explanation + Insight**

- **Stack Usage** - Push opening brackets, pop on closing
- **Matching Logic** - Check if closing matches opening
- **Empty Stack** - Handle case with no opening bracket
- **Time Complexity** - O(n) single pass through string
- **Space Complexity** - O(n) for stack in worst case

---

### 54. 🧱 Simplify Path

**🧠 Concept**

Simplify Unix-style path by splitting on '/' and using stack to handle '..' and '.' operations.

**💻 Example**

```javascript
function simplifyPath(path) {
  const stack = [];
  const parts = path.split('/');
  
  for (const part of parts) {
    if (part === '..') {
      if (stack.length > 0) stack.pop();
    } else if (part && part !== '.') {
      stack.push(part);
    }
  }
  
  return '/' + stack.join('/');
}
```

**💬 Explanation + Insight**

- **Split Path** - Split on '/' to get path components
- **Stack Operations** - Push directories, pop on '..'
- **Handle Edge Cases** - Ignore '.' and empty parts
- **Time Complexity** - O(n) where n is path length
- **Space Complexity** - O(n) for stack

---

### 55. 🧱 Min Stack

**🧠 Concept**

Design stack that supports push, pop, top, and getMin in O(1) time. Use auxiliary stack for minimum values.

**💻 Example**

```javascript
class MinStack {
  constructor() {
    this.stack = [];
    this.minStack = [];
  }
  
  push(val) {
    this.stack.push(val);
    if (this.minStack.length === 0 || val <= this.minStack[this.minStack.length - 1]) {
      this.minStack.push(val);
    }
  }
  
  pop() {
    const val = this.stack.pop();
    if (val === this.minStack[this.minStack.length - 1]) {
      this.minStack.pop();
    }
  }
  
  top() {
    return this.stack[this.stack.length - 1];
  }
  
  getMin() {
    return this.minStack[this.minStack.length - 1];
  }
}
```

**💬 Explanation + Insight**

- **Two Stacks** - Main stack and min stack
- **Min Tracking** - Push to min stack when value <= current min
- **Pop Synchronization** - Pop from min stack when values match
- **Time Complexity** - O(1) for all operations
- **Space Complexity** - O(n) for auxiliary stack

---

### 56. 🧱 Evaluate Reverse Polish Notation

**🧠 Concept**

Evaluate postfix expression using stack. Push operands, pop and compute when operator encountered.

**💻 Example**

```javascript
function evalRPN(tokens) {
  const stack = [];
  
  for (const token of tokens) {
    if (isOperator(token)) {
      const b = stack.pop();
      const a = stack.pop();
      stack.push(calculate(a, b, token));
    } else {
      stack.push(parseInt(token));
    }
  }
  
  return stack[0];
}

function isOperator(token) {
  return ['+', '-', '*', '/'].includes(token);
}
```

**💬 Explanation + Insight**

- **Stack Evaluation** - Use stack for postfix evaluation
- **Operator Handling** - Pop two operands, compute, push result
- **Operand Push** - Push numbers onto stack
- **Time Complexity** - O(n) single pass through tokens
- **Space Complexity** - O(n) for stack

---

### 57. 🧱 Basic Calculator

**🧠 Concept**

Evaluate basic arithmetic expression with parentheses using stack to handle operator precedence.

**💻 Example**

```javascript
function calculate(s) {
  const stack = [];
  let num = 0;
  let sign = 1;
  let result = 0;
  
  for (let i = 0; i < s.length; i++) {
    const char = s[i];
    
    if (char >= '0' && char <= '9') {
      num = num * 10 + parseInt(char);
    } else if (char === '+') {
      result += sign * num;
      num = 0;
      sign = 1;
    } else if (char === '-') {
      result += sign * num;
      num = 0;
      sign = -1;
    } else if (char === '(') {
      stack.push(result);
      stack.push(sign);
      result = 0;
      sign = 1;
    } else if (char === ')') {
      result += sign * num;
      num = 0;
      result *= stack.pop();
      result += stack.pop();
    }
  }
  
  return result + sign * num;
}
```

**💬 Explanation + Insight**

- **Stack for Parentheses** - Handle nested expressions
- **Sign Tracking** - Track positive/negative signs
- **Number Building** - Build multi-digit numbers
- **Time Complexity** - O(n) single pass
- **Space Complexity** - O(n) for stack

---

### 58. 🧱 Insert Delete GetRandom O(1)

**🧠 Concept**

Design data structure with O(1) insert, delete, and getRandom operations using HashMap and Array.

**💻 Example**

```javascript
class RandomizedSet {
  constructor() {
    this.map = new Map();
    this.list = [];
  }
  
  insert(val) {
    if (this.map.has(val)) return false;
    this.map.set(val, this.list.length);
    this.list.push(val);
    return true;
  }
  
  remove(val) {
    if (!this.map.has(val)) return false;
    const index = this.map.get(val);
    const lastElement = this.list[this.list.length - 1];
    this.list[index] = lastElement;
    this.map.set(lastElement, index);
    this.list.pop();
    this.map.delete(val);
    return true;
  }
  
  getRandom() {
    return this.list[Math.floor(Math.random() * this.list.length)];
  }
}
```

**💬 Explanation + Insight**

- **HashMap + Array** - HashMap for O(1) lookup, Array for random access
- **Index Tracking** - Store index of each element in HashMap
- **Swap and Pop** - Move last element to deleted position
- **Time Complexity** - O(1) for all operations
- **Space Complexity** - O(n) for storage

---

### 59. 🧱 Find Median from Data Stream

**🧠 Concept**

Find median from stream of numbers using two heaps - max heap for smaller half, min heap for larger half.

**💻 Example**

```javascript
class MedianFinder {
  constructor() {
    this.maxHeap = []; // smaller half
    this.minHeap = []; // larger half
  }
  
  addNum(num) {
    if (this.maxHeap.length === 0 || num <= this.maxHeap[0]) {
      this.maxHeap.push(num);
      this.maxHeap.sort((a, b) => b - a);
    } else {
      this.minHeap.push(num);
      this.minHeap.sort((a, b) => a - b);
    }
    
    if (this.maxHeap.length > this.minHeap.length + 1) {
      this.minHeap.push(this.maxHeap.shift());
      this.minHeap.sort((a, b) => a - b);
    } else if (this.minHeap.length > this.maxHeap.length) {
      this.maxHeap.push(this.minHeap.shift());
      this.maxHeap.sort((a, b) => b - a);
    }
  }
  
  findMedian() {
    if (this.maxHeap.length > this.minHeap.length) {
      return this.maxHeap[0];
    }
    return (this.maxHeap[0] + this.minHeap[0]) / 2;
  }
}
```

**💬 Explanation + Insight**

- **Two Heaps** - Max heap for smaller half, min heap for larger half
- **Balance Heaps** - Keep heaps balanced in size
- **Median Calculation** - Top of larger heap or average of both tops
- **Time Complexity** - O(log n) for addNum, O(1) for findMedian
- **Space Complexity** - O(n) for heaps

---

### 60. 🧱 LRU Cache

**🧠 Concept**

Design LRU cache using HashMap and Doubly Linked List for O(1) get and put operations.

**💻 Example**

```javascript
class LRUCache {
  constructor(capacity) {
    this.capacity = capacity;
    this.cache = new Map();
  }
  
  get(key) {
    if (this.cache.has(key)) {
      const value = this.cache.get(key);
      this.cache.delete(key);
      this.cache.set(key, value);
      return value;
    }
    return -1;
  }
  
  put(key, value) {
    if (this.cache.has(key)) {
      this.cache.delete(key);
    } else if (this.cache.size >= this.capacity) {
      const firstKey = this.cache.keys().next().value;
      this.cache.delete(firstKey);
    }
    this.cache.set(key, value);
  }
}
```

**💬 Explanation + Insight**

- **HashMap + Order** - Use Map to maintain insertion order
- **Access Update** - Move accessed item to end
- **Capacity Management** - Remove least recently used when full
- **Time Complexity** - O(1) for get and put operations
- **Space Complexity** - O(capacity) for cache storage

---

*This comprehensive stack, queue, and design section covers essential data structures including stack operations, queue implementations, and advanced design patterns for efficient data management.*