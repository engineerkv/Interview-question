# Stacks & Queues

## Q46. Implement Stack using Queues

Concept: Use one queue; push then rotate elements to bring last pushed to front for pop/top.

```javascript
class MyStack {
  constructor() {
    this.q = [];
  }

  push(x) {
    this.q.push(x);
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

**Time Complexity:** O(1) amortized push, O(n) worst-case pop  
**Space Complexity:** O(n) - Queue stores all elements

Deep Insights:
  - Rule: One queue; push then rotate to bring last pushed to front; O(1) amortized push, O(n) worst-case pop.
  - Real-world: Stack implementation using queues, data structure conversions, queue-based algorithms.
  - Common mistake: Rotating too many times; not handling empty queue; forgetting to maintain order.
  - Optimization: Amortized O(1) push with rotation; operations are integer-agnostic; space O(n).
  - Interview tip: Explain rotation technique clearly; mention amortized vs worst-case; ask about two-queue variant.
## Q47. Implement Queue using Stacks

Concept: Two stacks: in for push, out for pop/peek. Move only when out is empty.

```javascript
class MyQueue {
  constructor() {
    this.s1 = [];
    this.s2 = [];
  }

  push(x) {
    this.s1.push(x);
  }

  pop() {
    if (!this.s2.length) {
      while (this.s1.length) {
        this.s2.push(this.s1.pop());
      }
    }
    return this.s2.pop();
  }

  peek() {
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
// Input:
// let queue = new MyQueue();
// queue.push(1);
// queue.push(2);
// queue.push(3);
// queue.peek();  // Output: 1
// queue.pop();   // Output: 1
// queue.pop();   // Output: 2
// queue.empty(); // Output: false
// queue.pop();   // Output: 3
// queue.empty(); // Output: true
```

**Time Complexity:** O(1) amortized all operations  
**Space Complexity:** O(n) - Stacks store elements

Deep Insights:
  - Rule: Two stacks (in for push, out for pop/peek); move only when out is empty; O(1) amortized all operations.
  - Real-world: Queue implementation using stacks, data structure conversions, stack-based algorithms.
  - Common mistake: Moving elements too frequently; not checking if out is empty before moving; wrong move timing.
  - Optimization: Amortized O(1) operations; space O(n) across stacks; order preserved FIFO.
  - Interview tip: Explain lazy movement strategy; mention amortized complexity; ask about alternative approaches.
## Q48. Min Stack

Concept: Track current min alongside each push or via auxiliary stack.

```javascript
class MinStack {
  constructor() {
    this.s = [];
    this.m = [];
  }

  push(x) {
    this.s.push(x);
    const curMin = this.m.length ? Math.min(this.m[this.m.length - 1], x) : x;
    this.m.push(curMin);
  }

  pop() {
    this.m.pop();
    return this.s.pop();
  }

  top() {
    return this.s[this.s.length - 1];
  }

  getMin() {
    return this.m[this.m.length - 1];
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

**Time Complexity:** O(1) all operations  
**Space Complexity:** O(n) - Both stacks store elements

Deep Insights:
  - Rule: Auxiliary stack tracks current min; push min(min, x) on each push; O(1) all operations, O(n) space.
  - Real-world: Stack with minimum tracking, range queries, priority-based stack operations, min tracking systems.
  - Common mistake: Not updating min on pop; wrong min calculation; forgetting to handle empty stack.
  - Optimization: Variant stores pairs [val, min]; space-time tradeoff acceptable; O(1) getMin optimal.
  - Interview tip: Explain auxiliary stack approach; mention pair variant; ask about space optimization.
## Q49. Valid Parentheses

Concept: Stack of openers; pop on matching closers and validate empty at end.

```javascript
function isValid(s) {
  const st = [];
  const map = { ')': '(', ']': '[', '}': '{' };
  for (const c of s) {
    if (map[c]) {
      if (st.pop() !== map[c]) return false;
    } else {
      st.push(c);
    }
  }
  return st.length === 0;
}

// Test Cases:
// Input: s = "()"
// Output: true

// Input: s = "()[]{}"
// Output: true

// Input: s = "(]"
// Output: false

// Input: s = "([)]"
// Output: false

// Input: s = "{[]}"
// Output: true

// Input: s = ""
// Output: true
```

**Time Complexity:** O(n) - Process each character once  
**Space Complexity:** O(n) - Stack stores up to n/2 openers

Deep Insights:
  - Rule: Stack matches opening and closing brackets; push openers, pop and match closers; O(n) time, O(n) space.
  - Real-world: Code syntax validation, expression parsing, bracket matching in editors, syntax checking systems.
  - Common mistake: Not checking stack empty after processing; empty string valid; pushing non-closers only.
  - Optimization: Early return on mismatch; stack stores up to n/2 elements; O(n) time optimal.
  - Interview tip: Explain LIFO property clearly; mention empty string edge case; ask about additional bracket types.
## Q50. Next Greater Element

Concept: Find next greater element for each position using monotonic stack. Two variants: linear (non-circular) and circular arrays.

**Variant 1: Non-Circular (Linear Array)**

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

**Variant 2: Circular Array**

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

Deep Insights:
  - Rule: Traverse right-to-left with monotonic decreasing stack storing values; pop elements <= current; circular variant processes array twice; O(n) time, O(n) space.
  - Real-world: Next greater element queries, monotonic stack patterns, range query problems, element ordering in circular buffers.
  - Common mistake: Not handling equal values correctly (using <= vs <); wrong stack ordering; circular variant needs modulo indexing and condition `i < n` for result assignment; forgetting to update result only in first pass for circular variant.
  - Optimization: Each element pushed/popped once; O(n) time optimal; right-to-left traversal allows seeing future elements; circular variant processes 2n positions but each element handled once; equal values policy: use `<=` to pop equal or smaller values.
  - Interview tip: Explain right-to-left traversal approach clearly; mention circular variant wraps around; ask about equal values handling (`<=` vs `<`); discuss why storing values vs indices works here.
## Q51. Daily Temperatures

Concept: Find days until warmer temperature using monotonic stack. Use reverse loop to process from right to left.

```javascript
function dailyTemperatures(T) {
  const res = new Array(T.length).fill(0);
  const stack = [];
  const n = T.length;

  for (let i = n - 1; i >= 0; i--) {
    while (stack.length && T[stack[stack.length - 1]] <= T[i]) {
      stack.pop();
    }
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

Deep Insights:
  - Rule: Reverse loop (right-to-left) with monotonic decreasing stack of indices; pop when current temperature is >= stack top; compute distance as stack top index - current index; O(n) time, O(n) space.
  - Real-world: Temperature analysis, waiting time problems, next warmer day queries, distance calculations in time series data.
  - Common mistake: Not storing indices to compute gaps; wrong distance calculation (stack index - current index); forgetting to check stack length before accessing; using `<=` vs `<` for comparison.
  - Optimization: Store indices to compute gaps; reverse loop processes future elements first; each element pushed/popped once; O(n) time optimal; right-to-left approach naturally handles distance calculation.
  - Interview tip: Explain reverse loop approach clearly; mention distance calculation formula; ask about equal temperatures handling; discuss why storing indices is necessary for distance.
## Q52. Evaluate Reverse Polish Notation

Concept: Stack numbers; on operator, pop two, apply, push back. Watch division truncation toward zero.

```javascript
function evalRPN(tokens) {
  const st = [];
  const op = {
    '+': (a, b) => a + b,
    '-': (a, b) => a - b,
    '*': (a, b) => a * b,
    '/': (a, b) => (a / b) | 0, // truncate toward zero
  };
  for (const t of tokens) {
    if (t in op) {
      const b = st.pop();
      const a = st.pop();
      st.push(op[t](a, b));
    } else {
      st.push(Number(t));
    }
  }
  return st.pop();
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

Deep Insights:
  - Rule: Stack numbers; on operator, pop two, apply, push back; division truncates toward zero; O(n) time.
  - Real-world: Expression evaluation, calculator systems, postfix notation processing, arithmetic operations.
  - Common mistake: Wrong operand order (a/b vs b/a); division truncation toward zero; not handling division by zero.
  - Optimization: Extend with more operators if needed; stack stores intermediate results; O(n) time optimal.
  - Interview tip: Ask about operator precedence; mention division truncation; clarify operand order.
## Q53. Largest Rectangle in Histogram

Concept: Two-pass approach: find next smaller element on right (reverse loop), then on left (forward loop), then calculate max area using boundaries.

```javascript
function largestRectangleArea(heights) {
  const n = heights.length;
  const left = new Array(n);
  const right = new Array(n);
  const stack = [];

  // 1) Next Smaller Right (reverse loop)
  for (let i = n - 1; i >= 0; i--) {
    while (stack.length && heights[stack[stack.length - 1]] >= heights[i]) {
      stack.pop();
    }
    right[i] = stack.length ? stack[stack.length - 1] : n;
    stack.push(i);
  }

  stack.length = 0; // reset stack

  // 2) Next Smaller Left (forward loop)
  for (let i = 0; i < n; i++) {
    while (stack.length && heights[stack[stack.length - 1]] >= heights[i]) {
      stack.pop();
    }
    left[i] = stack.length ? stack[stack.length - 1] : -1;
    stack.push(i);
  }

  // 3) Calculate max area
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

Deep Insights:
  - Rule: Two-pass approach: find next smaller on right (reverse loop with >= condition), then on left (forward loop with >= condition), calculate area using width = right[i] - left[i] - 1; O(n) time, O(n) space.
  - Real-world: Histogram analysis, rectangle area problems, bar chart calculations, geometric algorithms, building facade analysis, UI layout problems.
  - Common mistake: Wrong comparison operator (>= vs >); not resetting stack between passes; off-by-one in width calculation (right - left - 1); forgetting to handle boundary cases (n and -1).
  - Optimization: Two passes separate boundary finding from area calculation; each bar pushed/popped once per pass; O(n) time optimal; clearer logic than single-pass approach; reset stack between passes.
  - Interview tip: Explain two-pass approach clearly; mention boundary calculation (right[i] - left[i] - 1); discuss why >= vs > matters; ask about edge cases (empty array, single bar, all equal bars).
## Q54. Sliding Window Maximum

Concept: Monotonic deque of indices (decreasing values). Front always max of window.

```javascript
function maxSlidingWindow(nums, k) {
  const dq = [];
  const res = [];
  for (let i = 0; i < nums.length; i++) {
    while (dq.length && dq[0] <= i - k) {
      dq.shift();
    }
    while (dq.length && nums[dq[dq.length - 1]] <= nums[i]) {
      dq.pop();
    }
    dq.push(i);
    if (i >= k - 1) {
      res.push(nums[dq[0]]);
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
**Space Complexity:** O(n) - Deque stores indices

Deep Insights:
  - Rule: Monotonic deque of indices (decreasing values); front always max of window; O(n) time.
  - Real-world: Sliding window maximum, range queries, window-based algorithms, stream processing.
  - Common mistake: Not removing out-of-window elements; wrong deque ordering; k==1 returns original array.
  - Optimization: Deque maintains decreasing order; each element added/removed once; O(n) time optimal.
  - Interview tip: Explain deque ordering clearly; mention k==1 edge case; ask about min variant.
## Q55. Circular Queue

Concept: Fixed-size ring buffer with head/tail and size; modulo arithmetic for wrap.

```javascript
class MyCircularQueue {
  constructor(k) {
    this.q = new Array(k);
    this.k = k;
    this.h = 0;
    this.t = 0;
    this.sz = 0;
  }

  enQueue(x) {
    if (this.isFull()) return false;
    this.q[this.t] = x;
    this.t = (this.t + 1) % this.k;
    this.sz++;
    return true;
  }

  deQueue() {
    if (this.isEmpty()) return false;
    this.h = (this.h + 1) % this.k;
    this.sz--;
    return true;
  }

  Front() {
    return this.isEmpty() ? -1 : this.q[this.h];
  }

  Rear() {
    return this.isEmpty() ? -1 : this.q[(this.t - 1 + this.k) % this.k];
  }

  isEmpty() {
    return this.sz === 0;
  }

  isFull() {
    return this.sz === this.k;
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

**Time Complexity:** O(1) all operations  
**Space Complexity:** O(k) - Fixed-size array of capacity k

Deep Insights:
  - Rule: Fixed-size ring buffer with head/tail and size; modulo arithmetic for wrap; O(1) all operations.
  - Real-world: Circular buffers, ring buffers, fixed-size queues, streaming data structures.
  - Common mistake: Wrong modulo arithmetic; rear index is (t-1+k)%k; not handling full/empty correctly.
  - Optimization: O(1) all operations; backed by raw array; size tracking avoids confusion.
  - Interview tip: Explain modulo arithmetic clearly; mention rear index calculation; ask about resize variant.

## Q56. Simplify Path

Concept:
Simplify Unix-style absolute path; use stack to track directories; handle "." (current), ".." (parent), multiple slashes.

Example:
```javascript
function simplifyPath(path) {
  const stack = [];
  const parts = path.split('/').filter(part => part !== '' && part !== '.');
  
  for (const part of parts) {
    if (part === '..') {
      if (stack.length > 0) {
        stack.pop();
      }
    } else {
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

Deep Insights:
- Split path by '/'; filter empty and '.'; use stack for '..'; join at end; O(n) time, O(n) space.
- Stack simulates directory navigation; '..' pops parent; '..' from root stays at root.
- Filter empty strings and '.' before processing.
- Edge case: Root path returns '/'; all '..' returns '/'.
- Interview tip: Explain stack usage; mention root handling; ask about relative paths.

## Q57. Basic Calculator

Concept:
Evaluate arithmetic expression with +, -, parentheses; use stack for precedence and parentheses handling.

Example:
```javascript
function calculate(s) {
  let result = 0;
  let num = 0;
  let sign = 1;
  const stack = [];
  
  for (let i = 0; i < s.length; i++) {
    const char = s[i];
    
    if (char >= '0' && char <= '9') {
      num = num * 10 + (char.charCodeAt(0) - '0'.charCodeAt(0));
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
      result *= stack.pop(); // sign
      result += stack.pop(); // previous result
    }
  }
  
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
**Space Complexity:** O(n) - Stack for parentheses

Deep Insights:
- Track result, current number, sign; use stack for parentheses; O(n) time, O(n) space.
- When '(': push result and sign; reset result and sign.
- When ')': add current number; multiply by sign from stack; add previous result.
- Edge case: Leading spaces; multiple consecutive operators; nested parentheses.
- Interview tip: Explain sign handling; mention stack for parentheses; ask about multiplication/division.