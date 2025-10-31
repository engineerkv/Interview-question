# Stacks & Queues

## Q46. Implement Stack using Queues

- Concept: Use one queue; push then rotate elements to bring last pushed to front for pop/top.

```javascript
class MyStack {
  constructor() { this.q = []; }

  push(x) {
    this.q.push(x);
    for (let i = 0; i < this.q.length - 1; i++) this.q.push(this.q.shift());
  }

  pop() { return this.q.shift(); }
  top() { return this.q[0]; }
  empty() { return this.q.length === 0; }
}
```

- Deep Insights:
  - Single queue rotation keeps LIFO order.
  - Alternative: two queues, move all but last.
  - Space O(n), elements unique not required.
  - Operations are integer-agnostic.

## Q47. Implement Queue using Stacks

- Concept: Two stacks: in for push, out for pop/peek. Move only when out is empty.

```javascript
class MyQueue {
  constructor() { this.s1 = []; this.s2 = []; }
  push(x) { this.s1.push(x); }
  pop() {
    if (!this.s2.length) while (this.s1.length) this.s2.push(this.s1.pop());
    return this.s2.pop();
  }
  peek() {
    if (!this.s2.length) while (this.s1.length) this.s2.push(this.s1.pop());
    return this.s2[this.s2.length - 1];
  }
  empty() { return !this.s1.length && !this.s2.length; }
}
```

- Deep Insights:
  - Move elements lazily to maintain O(1) amortized.
  - Peek mirrors pop logic.
  - Space O(n) across stacks.
  - Order preserved FIFO.

## Q48. Min Stack

- Concept: Track current min alongside each push or via auxiliary stack.

```javascript
class MinStack {
  constructor() { this.s = []; this.m = []; }
  push(x) {
    this.s.push(x);
    const curMin = this.m.length ? Math.min(this.m[this.m.length - 1], x) : x;
    this.m.push(curMin);
  }
  pop() { this.m.pop(); return this.s.pop(); }
  top() { return this.s[this.s.length - 1]; }
  getMin() { return this.m[this.m.length - 1]; }
}
```

- Deep Insights:
  - Duplicate mins must be tracked (stack length sync).
  - O(1) extra per element.
  - Variant: store pairs [val,min].
  - Space-time tradeoff acceptable.

## Q49. Valid Parentheses

- Concept: Stack of openers; pop on matching closers and validate empty at end.

```javascript
function isValid(s) {
  const st = [];
  const map = { ')': '(', ']': '[', '}': '{' };
  for (const c of s) {
    if (map[c]) { if (st.pop() !== map[c]) return false; }
    else st.push(c);
  }
  return st.length === 0;
}
```

- Deep Insights:
  - Same as Strings version; O(n) time.
  - Only three bracket types considered.
  - Empty string valid.
  - Push non-closers only.

## Q50. Next Greater Element

- Concept: Monotonic decreasing stack of indices; pop when current is greater.

```javascript
function nextGreaterElements(nums) {
  const res = new Array(nums.length).fill(-1);
  const st = [];
  for (let i = 0; i < nums.length; i++) {
    while (st.length && nums[i] > nums[st[st.length - 1]]) res[st.pop()] = nums[i];
    st.push(i);
  }
  return res;
}
```

- Deep Insights:
  - For circular arrays, sweep twice using i % n.
  - Stack holds decreasing values’ indices.
  - Equal values policy: strictly greater by default.
  - Result default -1.

## Q51. Daily Temperatures

- Concept: Monotonic stack of decreasing temperatures (indices); when warmer found, compute distance.

```javascript
function dailyTemperatures(T) {
  const res = new Array(T.length).fill(0);
  const st = [];
  for (let i = 0; i < T.length; i++) {
    while (st.length && T[i] > T[st[st.length - 1]]) {
      const j = st.pop();
      res[j] = i - j;
    }
    st.push(i);
  }
  return res;
}
```

- Deep Insights:
  - Each index pushed/popped once -> O(n).
  - Works for equal temps (distance 0).
  - Store indices to compute gaps.
  - Same pattern as NGE variant.

## Q52. Evaluate Reverse Polish Notation

- Concept: Stack numbers; on operator, pop two, apply, push back. Watch division truncation toward zero.

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
    } else st.push(Number(t));
  }
  return st.pop();
}
```

- Deep Insights:
  - Use bitwise to truncate toward zero in JS.
  - Validate stack arity for robustness.
  - Supports negative numbers.
  - Extend with more operators if needed.

## Q53. Largest Rectangle in Histogram

- Concept: Monotonic increasing stack; compute area on break. Append sentinel 0 to flush.

```javascript
function largestRectangleArea(heights) {
  const st = [];
  let best = 0;
  const a = [...heights, 0];
  for (let i = 0; i < a.length; i++) {
    while (st.length && a[i] < a[st[st.length - 1]]) {
      const h = a[st.pop()];
      const left = st.length ? st[st.length - 1] + 1 : 0;
      const width = i - left;
      best = Math.max(best, h * width);
    }
    st.push(i);
  }
  return best;
}
```

- Deep Insights:
  - Each index pushed/popped once.
  - Width uses previous lesser index.
  - Sentinel simplifies cleanup.
  - O(n) time.

## Q54. Sliding Window Maximum

- Concept: Monotonic deque of indices (decreasing values). Front always max of window.

```javascript
function maxSlidingWindow(nums, k) {
  const dq = [];
  const res = [];
  for (let i = 0; i < nums.length; i++) {
    while (dq.length && dq[0] <= i - k) dq.shift();
    while (dq.length && nums[dq[dq.length - 1]] <= nums[i]) dq.pop();
    dq.push(i);
    if (i >= k - 1) res.push(nums[dq[0]]);
  }
  return res;
}
```

- Deep Insights:
  - O(n) with each index enqueued/dequeued once.
  - Strictly decreasing ensures correctness.
  - Avoid storing values, store indices.
  - k==1 -> original array.

## Q55. Circular Queue

- Concept: Fixed-size ring buffer with head/tail and size; modulo arithmetic for wrap.

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
  Front() { return this.isEmpty() ? -1 : this.q[this.h]; }
  Rear() { return this.isEmpty() ? -1 : this.q[(this.t - 1 + this.k) % this.k]; }
  isEmpty() { return this.sz === 0; }
  isFull() { return this.sz === this.k; }
}
```

- Deep Insights:
  - Keep size to distinguish full vs empty when h==t.
  - Rear index is (t-1+k)%k.
  - O(1) all operations.
  - Backed by raw array.
