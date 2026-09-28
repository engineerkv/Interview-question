---
sidebar_label: "Stacks & Queues"
---
# Stacks & Queues

---

## Q75. 💡 Implement Stack using Queues

**Problem:** Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (`push`, `top`, `pop`, and `empty`).

**Approach:** Use one queue. After pushing, rotate elements to bring the newly pushed element to the front, making it available for `pop`/`top` operations.

### Solution 1: Single Queue with Rotation (Optimal)

```javascript
class MyStack {
  constructor() {
    this.q = [];
  }

  push(x) {
    this.q.push(x);
    // Rotate to bring last pushed element to front
    for (let i = 0; i < this.q.length - 1; i++) {
      this.q.push(this.q.shift());
    }
  }

  pop() {
    return this.q.shift();
  }

  top() {
    return this.q[0];
  }

  empty() {
    return this.q.length === 0;
  }
}

// Test Cases:
// Input:
// let stack = new MyStack();
// stack.push(1);
// stack.push(2);
// stack.push(3);
// stack.top();   // Output: 3
// stack.pop();   // Output: 3
// stack.pop();   // Output: 2
// stack.empty(); // Output: false
// stack.pop();   // Output: 1
// stack.empty(); // Output: true

```

**Time Complexity:** O(n) - Push rotates n-1 elements; O(1) for pop/top/empty
**Space Complexity:** O(n) - Queue stores all elements

## Q76. 💡 Implement Queue using Stacks

**Problem:** Implement a first-in-first-out (FIFO) queue using only two stacks. The implemented queue should support all functions of a normal queue (`push`, `peek`, `pop`, and `empty`).

**Approach:** Use two stacks: `s1` for push operations, `s2` for pop/peek operations. Move elements from `s1` to `s2` only when `s2` is empty (lazy movement).

### Solution 1: Two Stacks with Lazy Movement (Optimal)

```javascript
class MyQueue {
  constructor() {
    this.s1 = [];  // Input stack
    this.s2 = [];  // Output stack
  }

  push(x) {
    this.s1.push(x);
  }

  pop() {
    // Move elements from s1 to s2 if s2 is empty
    if (!this.s2.length) {
      while (this.s1.length) {
        this.s2.push(this.s1.pop());
      }
    }
    return this.s2.pop();
  }

  peek() {
    // Move elements from s1 to s2 if s2 is empty
    if (!this.s2.length) {
      while (this.s1.length) {
        this.s2.push(this.s1.pop());
      }
    }
    return this.s2[this.s2.length - 1];
  }

  empty() {
    return !this.s1.length && !this.s2.length;
  }
}

// Test Cases:
// Input: queue operations: push(1), push(2), push(3), peek(), pop(), pop(), empty(), pop(), empty()
// Output: peek() returns 1, pop() returns 1, pop() returns 2, empty() returns false, pop() returns 3, empty() returns true
// Explanation: Queue operations performed using two stacks

```

**Time Complexity:** O(1) amortized - Each element moved at most once
**Space Complexity:** O(n) - Stacks store elements

## Q77. ⬇️ ⬇️ ⬇️ Min Stack

**Problem:** Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. Implement the `MinStack` class:

- `MinStack()` initializes the stack object.

- `void push(int val)` pushes the element `val` onto the stack.

- `void pop()` removes the element on the top of the stack.

- `int top()` gets the top element of the stack.

- `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with `O(1)` time complexity for each function.

**Approach:** Use an auxiliary stack to track the minimum value at each level. Push the minimum of current min and new value to the auxiliary stack.

### Solution 1: Auxiliary Stack (Optimal)

```javascript
class MinStack {
  constructor() {
    this.stack = [];      // Main stack
    this.minStack = [];   // Auxiliary stack for minimums
  }

  push(val) {
    this.stack.push(val);
    // Track minimum at each level
    const curMin = this.minStack.length
      ? Math.min(this.minStack[this.minStack.length - 1], val)
      : val;
    this.minStack.push(curMin);
  }

  pop() {
    this.minStack.pop();
    return this.stack.pop();
  }

  top() {
    return this.stack[this.stack.length - 1];
  }

  getMin() {
    return this.minStack[this.minStack.length - 1];
  }
}

// Test Cases:
// Input:
// let minStack = new MinStack();
// minStack.push(-2);
// minStack.push(0);
// minStack.push(-3);
// minStack.getMin(); // Output: -3
// minStack.pop();
// minStack.top();    // Output: 0
// minStack.getMin(); // Output: -2

```

**Time Complexity:** O(1) - All operations are constant time
**Space Complexity:** O(n) - Both stacks store elements

### Solution 2: Pair Storage (Alternative)

```javascript
class MinStackPairs {
  constructor() {
    this.stack = [];  // Store [value, min] pairs
  }

  push(val) {
    const curMin = this.stack.length
      ? Math.min(this.stack[this.stack.length - 1][1], val)
      : val;
    this.stack.push([val, curMin]);
  }

  pop() {
    return this.stack.pop()[0];
  }

  top() {
    return this.stack[this.stack.length - 1][0];
  }

  getMin() {
    return this.stack[this.stack.length - 1][1];
  }
}

```

## Q78. ✅ Valid Parentheses

**Problem:** Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid. An input string is valid if:

1. Open brackets must be closed by the same type of brackets.

2. Open brackets must be closed in the correct order.

3. Every close bracket has a corresponding open bracket of the same type.

**Approach:** Use a stack to track opening brackets. Push openers, pop and match when encountering closers. Stack should be empty at the end.

### Solution 1: Stack with Mapping (Optimal)

```javascript
function isValid(s) {
  const stack = [];
  const map = { ')': '(', ']': '[', '}': '{' };

  for (const c of s) {
    if (map[c]) {
      // Closing bracket - check if matches last opener
      if (stack.pop() !== map[c]) return false;
    } else {
      // Opening bracket - push to stack
      stack.push(c);
    }
  }

  return stack.length === 0;  // All brackets matched
}

// Test Cases:
// Input: s = "()"
// Output: true

// Input: s = "()[]{}"
// Output: true

// Input: s = "(]"
// Output: false
// Explanation: ']' doesn't match '('

// Input: s = "([)]"
// Output: false
// Explanation: Brackets not closed in correct order

// Input: s = "{[]}"
// Output: true
// Explanation: All brackets properly matched

// Input: s = ""
// Output: true
// Explanation: Empty string is valid

```

**Time Complexity:** O(n) - Process each character once
**Space Complexity:** O(n) - Stack stores up to n/2 openers

## Q79. ▲ ▲ ▲ Next Greater Element

**Problem:** Given an array `nums`, return an array `answer` such that `answer[i]` is the next greater element to the right of `nums[i]` in the array. If no greater element exists, return `-1`.

**Approach:** Use a monotonic decreasing stack. Traverse right-to-left, maintaining elements in decreasing order. For each position, the stack top is the next greater element.

### Solution 1: Monotonic Stack - Non-Circular (Optimal)

```javascript
function nextGreaterElement(nums) {
  const array = new Array(nums.length).fill(-1);
  const stack = [];
  const n = nums.length;

  for (let i = n - 1; i >= 0; i--) {
    while (stack.length && stack[stack.length - 1] <= nums[i]) {
      stack.pop();
    }
    if (stack.length) {
      array[i] = stack[stack.length - 1];
    }
    stack.push(nums[i]);
  }
  return array;
}

// Test Cases:
// Input: nums = [2, 1, 2, 4, 3, 1]
// Output: [4, 2, 4, -1, -1, -1]
// Explanation: For 2 at index 0, next greater is 4 at index 3. For 1 at index 1, next greater is 2 at index 2. For 2 at index 2, next greater is 4. For 4, 3, and 1, no greater element exists to the right.

// Input: nums = [1, 2, 3, 4, 5]
// Output: [2, 3, 4, 5, -1]
// Explanation: Each element has next greater except the last one.

// Input: nums = [5, 4, 3, 2, 1]
// Output: [-1, -1, -1, -1, -1]
// Explanation: Decreasing array has no greater element to the right for any position.

// Input: nums = [1]
// Output: [-1]

```

### Solution 2: Monotonic Stack - Circular Array

```javascript
function nextGreaterElementsCircular(nums) {
  const array = new Array(nums.length).fill(-1);
  const stack = [];
  const n = nums.length;

  for (let i = n * 2 - 1; i >= 0; i--) {
    const idx = i % n;
    while (stack.length && stack[stack.length - 1] <= nums[idx]) {
      stack.pop();
    }
    if (i < n && stack.length) {
      array[idx] = stack[stack.length - 1];
    }
    stack.push(nums[idx]);
  }
  return array;
}

// Test Cases:
// Input: nums = [1, 2, 1]
// Output: [2, -1, 2]
// Explanation: For 1 at index 0, next greater is 2 at index 1. For 2 at index 1, no greater element (wrapping around: 1 < 2). For 1 at index 2, next greater is 2 at index 1 (wrapping to beginning).

// Input: nums = [1, 2, 3, 4, 3]
// Output: [2, 3, 4, -1, 4]
// Explanation: For 1→2, 2→3, 3→4, 4→none (after wrapping, no element > 4), 3→4 (wraps back and finds 4 at index 3).

// Input: nums = [5, 4, 3, 2, 1]
// Output: [-1, 5, 5, 5, 5]
// Explanation: Circular array - elements wrap around. For 5 (index 0), no greater. For 4 (index 1), wraps to find 5. For 3, 2, 1, each wraps to find 5.

// Input: nums = [1]
// Output: [-1]

```

**Time Complexity:** O(n) - Each element pushed and popped at most once
**Space Complexity:** O(n) - Stack stores values

## Q80. 💡 Daily Temperatures

**Problem:** Given an array of integers `temperatures` representing the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `i`th day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

**Approach:** Use a monotonic decreasing stack storing indices. Traverse right-to-left, compute distance as stack top index - current index.

### Solution 1: Monotonic Stack with Indices (Optimal)

```javascript
function dailyTemperatures(temperatures) {
  const res = new Array(temperatures.length).fill(0);
  const stack = [];
  const n = temperatures.length;

  for (let i = n - 1; i >= 0; i--) {
    // Pop indices with temperatures <= current
    while (stack.length && temperatures[stack[stack.length - 1]] <= temperatures[i]) {
      stack.pop();
    }
    // If stack has warmer day, compute distance
    if (stack.length) {
      res[i] = stack[stack.length - 1] - i;
    }
    stack.push(i);
  }
  return res;
}

// Test Cases:
// Input: T = [73, 74, 75, 71, 69, 72, 76, 73]
// Output: [1, 1, 4, 2, 1, 1, 0, 0]
// Explanation: For 73 (index 0), next warmer is 74 at index 1 (distance 1). For 74, next warmer is 75 (distance 1). For 75, next warmer is 76 at index 6 (distance 4). For 71, next warmer is 72 (distance 2). For 69, next warmer is 72 (distance 1). For 72, next warmer is 76 (distance 1). For 76 and 73, no warmer days ahead.

// Input: T = [30, 40, 50, 60]
// Output: [1, 1, 1, 0]
// Explanation: Each day has next warmer day exactly one day ahead, except the last day.

// Input: T = [30, 60, 90]
// Output: [1, 1, 0]
// Explanation: 30→60 (distance 1), 60→90 (distance 1), 90 has no warmer day.

// Input: T = [30]
// Output: [0]
// Explanation: Single day has no warmer day ahead.

// Input: T = [73, 73, 75, 71, 69, 72, 76, 73]
// Output: [2, 1, 4, 2, 1, 1, 0, 0]
// Explanation: First 73 (index 0) has next warmer 73 at index 1, but 73 <= 73, so continues to find 75 at index 2 (distance 2).

```

**Time Complexity:** O(n) - Each element pushed and popped at most once
**Space Complexity:** O(n) - Stack stores indices

## Q81. 🔄 Evaluate Reverse Polish Notation

**Problem:** You are given an array of strings `tokens` that represents an arithmetic expression in Reverse Polish Notation. Evaluate the expression and return an integer that represents the value of the expression. Valid operators are `+`, `-`, `*`, and `/`. Each operand may be an integer or another expression. Division should truncate toward zero.

**Approach:** Use a stack to store operands. When encountering an operator, pop two operands, apply the operation, and push the result back.

### Solution 1: Stack-Based Evaluation (Optimal)

```javascript
function evalRPN(tokens) {
  const stack = [];
  const operators = {
    '+': (a, b) => a + b,
    '-': (a, b) => a - b,
    '*': (a, b) => a * b,
    '/': (a, b) => Math.trunc(a / b),  // Truncate toward zero
  };

  for (const token of tokens) {
    if (token in operators) {
      const b = stack.pop();
      const a = stack.pop();
      stack.push(operators[token](a, b));
    } else {
      stack.push(Number(token));
    }
  }

  return stack.pop();
}

// Test Cases:
// Input: tokens = ["2", "1", "+", "3", "*"]
// Output: 9
// Explanation: ((2 + 1) * 3) = 9

// Input: tokens = ["4", "13", "5", "/", "+"]
// Output: 6
// Explanation: (4 + (13 / 5)) = 6

// Input: tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
// Output: 22

// Input: tokens = ["1"]
// Output: 1

```

**Time Complexity:** O(n) - Process each token once
**Space Complexity:** O(n) - Stack stores operands

## Q82. 💡 Largest Rectangle in Histogram

**Problem:** Given an array of integers `heights` representing the histogram's bar height where the width of each bar is `1`, return the area of the largest rectangle in the histogram.

**Approach:** Two-pass approach: find next smaller element on right (reverse loop), then on left (forward loop), then calculate max area using boundaries.

### Solution 1: Two-Pass with Monotonic Stack (Optimal)

```javascript
function largestRectangleArea(heights) {
  const n = heights.length;
  const left = new Array(n);   // Next smaller on left
  const right = new Array(n);  // Next smaller on right
  const stack = [];

  // Step 1: Find next smaller on right (reverse loop)
  for (let i = n - 1; i >= 0; i--) {
    while (stack.length && heights[stack[stack.length - 1]] >= heights[i]) {
      stack.pop();
    }
    right[i] = stack.length ? stack[stack.length - 1] : n;  // n if no smaller
    stack.push(i);
  }

  stack.length = 0;  // Reset stack

  // Step 2: Find next smaller on left (forward loop)
  for (let i = 0; i < n; i++) {
    while (stack.length && heights[stack[stack.length - 1]] >= heights[i]) {
      stack.pop();
    }
    left[i] = stack.length ? stack[stack.length - 1] : -1;  // -1 if no smaller
    stack.push(i);
  }

  // Step 3: Calculate max area for each bar
  let maxArea = 0;
  for (let i = 0; i < n; i++) {
    const width = right[i] - left[i] - 1;
    maxArea = Math.max(maxArea, heights[i] * width);
  }

  return maxArea;
}

// Test Cases:
// Input: heights = [2, 1, 5, 6, 2, 3]
// Output: 10
// Explanation: Largest rectangle is from index 2-3 (height 5-6), width 2, area = 10

// Input: heights = [2, 4]
// Output: 4
// Explanation: Largest rectangle is at index 1 (height 4), width 1, area = 4

// Input: heights = [1]
// Output: 1

// Input: heights = [1, 1]
// Output: 2

```

**Time Complexity:** O(n) - Each bar pushed and popped at most once per pass (3 passes total)
**Space Complexity:** O(n) - Arrays `left` and `right` store boundaries, stack stores indices

## Q83. 🪟 🪟 🪟 Sliding Window Maximum

**Problem:** You are given an array of integers `nums`, and there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position. Return the maximum sliding window.

**Approach:** Use a monotonic deque storing indices with decreasing values. Front always contains the maximum of the current window.

### Solution 1: Monotonic Deque (Optimal)

```javascript
function maxSlidingWindow(nums, k) {
  const dq = [];  // Deque stores indices
  const res = [];

  for (let i = 0; i < nums.length; i++) {
    // Remove indices outside current window
    while (dq.length && dq[0] <= i - k) {
      dq.shift();
    }

    // Remove indices with values <= current (maintain decreasing order)
    while (dq.length && nums[dq[dq.length - 1]] <= nums[i]) {
      dq.pop();
    }

    dq.push(i);

    // Add maximum when window is complete
    if (i >= k - 1) {
      res.push(nums[dq[0]]);  // Front is always max
    }
  }

  return res;
}

// Test Cases:
// Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
// Output: [3, 3, 5, 5, 6, 7]

// Input: nums = [1], k = 1
// Output: [1]

// Input: nums = [1, -1], k = 1
// Output: [1, -1]

// Input: nums = [9, 11], k = 2
// Output: [11]

// Input: nums = [4, -2], k = 2
// Output: [4]

```

**Time Complexity:** O(n) - Each element added and removed at most once
**Space Complexity:** O(k) - Deque stores at most k indices

## Q84. 💡 Design Circular Queue

**Problem:** Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer". Implement the `MyCircularQueue` class.

**Approach:** Use a fixed-size array with head and tail pointers. Use modulo arithmetic for wrapping around. Track size to distinguish full from empty.

### Solution 1: Fixed-Size Ring Buffer (Optimal)

```javascript
class MyCircularQueue {
  constructor(k) {
    this.queue = new Array(k);
    this.capacity = k;
    this.head = 0;
    this.tail = 0;
    this.size = 0;
  }

  enQueue(value) {
    if (this.isFull()) return false;

    this.queue[this.tail] = value;
    this.tail = (this.tail + 1) % this.capacity;
    this.size++;
    return true;
  }

  deQueue() {
    if (this.isEmpty()) return false;

    this.head = (this.head + 1) % this.capacity;
    this.size--;
    return true;
  }

  Front() {
    return this.isEmpty() ? -1 : this.queue[this.head];
  }

  Rear() {
    if (this.isEmpty()) return -1;
    const rearIndex = (this.tail - 1 + this.capacity) % this.capacity;
    return this.queue[rearIndex];
  }

  isEmpty() {
    return this.size === 0;
  }

  isFull() {
    return this.size === this.capacity;
  }
}

// Test Cases:
// Input:
// let circularQueue = new MyCircularQueue(3);
// circularQueue.enQueue(1);  // Output: true
// circularQueue.enQueue(2);  // Output: true
// circularQueue.enQueue(3);  // Output: true
// circularQueue.enQueue(4);  // Output: false (queue is full)
// circularQueue.Rear();      // Output: 3
// circularQueue.isFull();     // Output: true
// circularQueue.deQueue();    // Output: true
// circularQueue.enQueue(4);  // Output: true
// circularQueue.Rear();       // Output: 4

```

**Time Complexity:** O(1) - All operations are constant time
**Space Complexity:** O(k) - Fixed-size array of capacity k

## Q85. 💡 Simplify Path

**Problem:** Given a string `path`, which is an absolute path (starting with a slash `'/'`) to a file or directory in a Unix-style file system, convert it to the simplified canonical path. In a Unix-style file system, a period `'.'` refers to the current directory, a double period `'..'` refers to the directory up a level, and any multiple consecutive slashes (i.e. `'//'`) are treated as a single slash `'/'`. For this problem, any other format of periods such as `'...'` are treated as file/directory names.

**Approach:** Split path by `/`, filter out empty strings and `.`. Use a stack to track directories. Pop on `..`, push otherwise.

### Solution 1: Stack-Based Path Processing (Optimal)

```javascript
function simplifyPath(path) {
  const stack = [];
  const parts = path.split('/').filter(part => part !== '' && part !== '.');

  for (const part of parts) {
    if (part === '..') {
      // Go up one directory (pop if not empty)
      if (stack.length > 0) {
        stack.pop();
      }
    } else {
      // Add directory
      stack.push(part);
    }
  }

  return '/' + stack.join('/');
}

// Input: path = "/home/"
// Output: "/home"
// Explanation: Remove trailing slash

// Input: path = "/home//foo/"
// Output: "/home/foo"
// Explanation: Remove multiple slashes

// Input: path = "/a/./b/../../c/"
// Output: "/c"
// Explanation: /a -> /a/b -> /a -> /c

// Input: path = "/../"
// Output: "/"
// Explanation: .. from root stays at root

```

**Time Complexity:** O(n) - Split and process path
**Space Complexity:** O(n) - Stack storage

## Q86. 💡 Basic Calculator

**Problem:** Given a string `s` representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation. The expression may contain digits, `'+'`, `'-'`, `'('`, `')'`, and spaces.

**Approach:** Track result, current number, and sign. Use stack to handle parentheses—push result and sign when opening, pop and combine when closing.

### Solution 1: Stack with Sign Tracking (Optimal)

```javascript
function calculate(s) {
  let result = 0;
  let num = 0;
  let sign = 1;  // 1 for +, -1 for -
  const stack = [];

  for (let i = 0; i < s.length; i++) {
    const char = s[i];

    if (char >= '0' && char <= '9') {
      // Build number from digits
      num = num * 10 + (char.charCodeAt(0) - '0'.charCodeAt(0));
    } else if (char === '+') {
      // Apply current number with sign, reset for next number
      result += sign * num;
      num = 0;
      sign = 1;
    } else if (char === '-') {
      // Apply current number with sign, reset for next number
      result += sign * num;
      num = 0;
      sign = -1;
    } else if (char === '(') {
      // Push current result and sign, start new expression
      stack.push(result);
      stack.push(sign);
      result = 0;
      sign = 1;
    } else if (char === ')') {
      // Apply current number, then combine with parent expression
      result += sign * num;
      num = 0;
      result *= stack.pop();  // Apply sign from stack
      result += stack.pop();  // Add previous result
    }
    // Skip spaces
  }

  // Apply last number
  result += sign * num;
  return result;
}

// Input: s = "1 + 1"
// Output: 2

// Input: s = " 2-1 + 2 "
// Output: 3

// Input: s = "(1+(4+5+2)-3)+(6+8)"
// Output: 23

```

**Time Complexity:** O(n) - Single pass through string
**Space Complexity:** O(n) - Stack for parentheses (worst case: all parentheses)

- **Interview Tip:** Explain sign handling clearly; emphasize stack usage for parentheses; ask about multiplication/division extension

---

