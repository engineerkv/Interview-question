---
sidebar_label: "Cheatsheet"
sidebar_position: 100
---
# 🧠 DSA Interview Cheatsheet

> **⏱️ Review Time: 30-40 minutes** | **Priority: ⭐⭐⭐ Critical** | Essential DSA patterns and templates for interviews
>
> **Coverage: Q1-Q229** (229 problems across 13 categories)

**Quick Review Checklist:**

- [ ] Arrays & Two Pointers (Sliding Window, Prefix Sum)

- [ ] Strings (Pattern Matching, String Manipulation)

- [ ] Linked Lists (Fast/Slow Pointers, Reversal)

- [ ] Stacks & Queues (Monotonic Stack, BFS)

- [ ] Binary Trees (DFS, BFS, Traversal)

- [ ] Binary Search Tree (BST Properties, Inorder)

- [ ] Heaps & Priority Queue (Min/Max Heap, Top K)

- [ ] Graphs (DFS, BFS, Shortest Path, Topological Sort)

- [ ] Dynamic Programming (1D/2D DP, Memoization)

- [ ] Recursion & Backtracking (Subsets, Permutations)

- [ ] Matrix (2D Array Traversal, Spiral)

- [ ] Trie (Prefix Tree, Word Search)

- [ ] Binary Search (Search in Sorted Array, Rotated Array)

- [ ] Bit Manipulation (XOR, AND, OR tricks)

- [ ] Math (GCD, Prime, Number Theory)

---

## 📚 Problem Ranges by Category

- **Arrays**: Q1-Q33 (33 problems)

- **Strings**: Q34-Q55 (22 problems)

- **Linked List**: Q56-Q74 (19 problems)

- **Stacks & Queues**: Q75-Q86 (12 problems)

- **Binary Trees**: Q87-Q113 (27 problems)

- **Binary Search Tree**: Q114-Q123 (10 problems)

- **Heaps & Priority Queue**: Q124-Q135 (12 problems)

- **Graphs**: Q136-Q159 (24 problems)

- **Dynamic Programming**: Q160-Q192 (33 problems)

- **Recursion & Backtracking**: Q193-Q202 (10 problems)

- **Matrix**: Q203-Q207 (5 problems)

- **Trie**: Q208-Q210 (3 problems)

- **Binary Search**: Q211-Q217 (7 problems)

- **Bit Manipulation**: Q218-Q223 (6 problems)

- **Math**: Q224-Q229 (6 problems)

**Total: 229 problems (Q1-Q229)**

---

## Arrays & Two Pointers

**Definition:** Use two pointers (from both ends or same direction) and sliding windows to solve array problems in O(n) time, avoiding nested loops.

- **Patterns:** Two pointers, sliding window, prefix/suffix, partitioning, Kadane.

- **Templates:**

```javascript
// Two pointers from both ends
let l = 0, r = arr.length - 1;
while (l < r) {
  // Move l/r based on condition
  if (arr[l] + arr[r] === target) return [l, r];
  if (arr[l] + arr[r] < target) l++;
  else r--;
}

// Sliding window (variable size)
let l = 0;
for (let r = 0; r < s.length; r++) {
  // Expand window
  while (/* invalid condition */) {
    // Shrink window
    l++;
  }
  // Update answer
}

```

- **Tips:** Normalize k, avoid O(n²) scans, prefer O(n) with hash/sets.

## Hash Map / Set

**Definition:** Data structures providing O(1) average lookup time for frequency counting, index tracking, and duplicate detection in array/string problems.

- Use `Map`/`Set` for O(1) average lookup.

```javascript
// Frequency map
const freq = new Map();
for (const x of arr) {
  freq.set(x, (freq.get(x) || 0) + 1);
}

// Index map
const seen = new Map();
for (let i = 0; i < arr.length; i++) {
  seen.set(arr[i], i);
}

// Set for uniqueness
const set = new Set(arr);
if (set.has(target)) return true;

```

- **Tips:** Pre-seed map (e.g., `{0:1}`) for prefix sums.

## Stack / Monotonic Stack

**Definition:** Stack maintains LIFO order; monotonic stack keeps elements in sorted order to find next/previous greater/smaller elements efficiently.

- **Patterns:** Valid parentheses, next greater, histogram, temperatures.

```javascript
// Monotonic stack (decreasing)
const st = [];
for (let i = 0; i < n; i++) {
  while (st.length && arr[st[st.length - 1]] < arr[i]) {
    const idx = st.pop();
    // Process index idx
  }
  st.push(i);
}

```

- **Tips:** Store indices, not values; consider sentinel.

## Queue / Deque

**Definition:** Queue follows FIFO order; deque (double-ended queue) allows insertion/deletion from both ends, useful for sliding window maximum problems.

- Sliding window max via decreasing deque of indices.

```javascript
// Decreasing deque for sliding window maximum
const dq = []; // Store indices, keep decreasing values

for (let i = 0; i < arr.length; i++) {
  // Remove indices outside window
  while (dq.length && dq[0] <= i - k) dq.shift();

  // Remove smaller elements from back
  while (dq.length && arr[dq[dq.length - 1]] < arr[i]) dq.pop();

  dq.push(i);
  // dq[0] is index of max in current window
}

```

## Linked List

**Definition:** Linear data structure with nodes connected by pointers; use fast/slow pointers for cycle detection and middle node, reverse in-place for manipulation.

- **Patterns:** Fast/slow, reverse in-place, merge, split.

```javascript
// Reverse linked list
let prev = null, cur = head;
while (cur) {
  const next = cur.next;
  cur.next = prev;
  prev = cur;
  cur = next;
}
return prev;

// Fast/slow pointers (middle node)
let slow = head, fast = head;
while (fast && fast.next) {
  slow = slow.next;
  fast = fast.next.next;
}
return slow;

```

- **Tips:** Use dummy nodes; careful pointer order.

## Trees (Binary Tree / BST)

**Definition:** Hierarchical structure with nodes; binary trees have at most two children; BST maintains sorted property (left < root < right) for efficient search.

- **Traversals:** DFS (pre/in/post), BFS (level-order).

```javascript
// DFS (recursive)
function dfs(node) {
  if (!node) return;
  // Pre-order: process here
  dfs(node.left);
  // In-order: process here
  dfs(node.right);
  // Post-order: process here
}

// BFS (level-order)
const q = [root];
while (q.length) {
  const level = [];
  const n = q.length;
  for (let i = 0; i < n; i++) {
    const x = q.shift();
    level.push(x.val);
    if (x.left) q.push(x.left);
    if (x.right) q.push(x.right);
  }
  // Process level
}

```

- **Tips:** LCA, depth/diameter via post-order; BST uses sorted property.

## Heap / Priority Queue

**Definition:** Complete binary tree maintaining heap property (min/max at root); provides O(log n) insert/extract for top-k, median, and priority-based problems.

- Use Min/Max Binary Heap (custom or library alternative).

```javascript
class MinHeap {
  constructor() {
    this.h = [];
  }

  push(x) {
    this.h.push(x);
    this.heapifyUp(this.h.length - 1);
  }

  pop() {
    if (this.h.length === 0) return null;
    const top = this.h[0];
    this.h[0] = this.h[this.h.length - 1];
    this.h.pop();
    if (this.h.length > 0) this.heapifyDown(0);
    return top;
  }

  peek() {
    return this.h[0];
  }

  heapifyUp(i) {
    // Implementation
  }

  heapifyDown(i) {
    // Implementation
  }
}

```

- **Tips:** k-th, top-k, streaming median (two heaps).

## Graphs

**Definition:** Collection of nodes (vertices) connected by edges; use BFS for shortest paths, DFS for traversal, and topological sort for dependency ordering.

- **Representations:** Adjacency list `{u: [v...]}`.

```javascript
// BFS
const q = [src];
const seen = new Set([src]);
while (q.length) {
  const u = q.shift();
  for (const v of graph[u] || []) {
    if (!seen.has(v)) {
      seen.add(v);
      q.push(v);
    }
  }
}

// DFS (recursive)
const seen = new Set();
function dfs(u) {
  seen.add(u);
  for (const v of graph[u] || []) {
    if (!seen.has(v)) {
      dfs(v);
    }
  }
}

```

- **Tips:** Detect cycles (directed: colors/dfs; undirected: parent check), topo sort via indegree.

## Dynamic Programming

**Definition:** Solve complex problems by breaking into overlapping subproblems, storing results to avoid recomputation, optimizing recursive solutions to polynomial time.

- **Steps:** Define state, recurrence, base cases, order, space-opt.

```javascript
// 1D DP
const dp = new Array(n + 1).fill(0);
dp[0] = baseCase;
for (let i = 1; i <= n; i++) {
  dp[i] = recurrence(dp, i);
}
return dp[n];

// 2D DP
const dp = Array.from({length: m}, () => new Array(n).fill(0));
for (let i = 0; i < m; i++) {
  for (let j = 0; j < n; j++) {
    dp[i][j] = recurrence(dp, i, j);
  }
}

```

- **Tips:** Convert recursion to tabulation; optimize to O(1) or O(n) space when possible.

## Backtracking

**Definition:** Systematic search algorithm that builds solutions incrementally, abandons partial solutions (backtracks) when invalid, used for permutations/combinations.

- **Pattern:** Explore, choose, un-choose; prune aggressively.

```javascript
const res = [];
const cur = [];

function bt(i, cur) {
  // Base case
  if (/* goal reached */) {
    res.push([...cur]);
    return;
  }

  // Explore choices
  for (const choice of choices) {
    // Prune invalid choices
    if (/* invalid */) continue;

    // Choose
    cur.push(choice);
    bt(i + 1, cur);
    // Un-choose (backtrack)
    cur.pop();
  }
}

bt(0, []);
return res;

```

- **Tips:** Sort for dedup; use sets for used choices.

## Matrix

**Definition:** 2D array problems involving traversal patterns (spiral, diagonal), transformations (rotation, transpose), and boundary manipulation techniques.

- **Patterns:** Spiral traversal, rotation, zero manipulation, game simulation.

```javascript
// Spiral traversal
let top = 0, bottom = m - 1, left = 0, right = n - 1;
while (top <= bottom && left <= right) {
  // Right → Down → Left → Up
  for (let i = left; i <= right; i++) result.push(matrix[top][i]);
  top++;
  for (let i = top; i <= bottom; i++) result.push(matrix[i][right]);
  right--;
  if (top <= bottom) {
    for (let i = right; i >= left; i--) result.push(matrix[bottom][i]);
    bottom--;
  }
  if (left <= right) {
    for (let i = bottom; i >= top; i--) result.push(matrix[i][left]);
    left++;
  }
}

// Rotate 90° clockwise: transpose then reverse rows
for (let i = 0; i < n; i++) {
  for (let j = i; j < n; j++) {
    [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];
  }
}
for (let i = 0; i < n; i++) matrix[i].reverse();

```

- **Tips:** Use first row/col as markers for O(1) space algorithms; handle boundary checks carefully.

## Trie (Prefix Tree)

**Definition:** Tree-like data structure storing strings with shared prefixes, enabling efficient prefix matching, autocomplete, and word search operations.

```javascript
class Trie {
  constructor() {
    this.root = {};
  }

  insert(word) {
    let node = this.root;
    for (const char of word) {
      if (!node[char]) node[char] = {};
      node = node[char];
    }
    node.isEnd = true;
  }

  search(word) {
    let node = this.root;
    for (const char of word) {
      if (!node[char]) return false;
      node = node[char];
    }
    return node.isEnd === true;
  }

  startsWith(prefix) {
    let node = this.root;
    for (const char of prefix) {
      if (!node[char]) return false;
      node = node[char];
    }
    return true;
  }
}

```

- **Tips:** Use for prefix matching, autocomplete, word dictionaries; DFS for wildcard search.

## Binary Search

**Definition:** Search algorithm for sorted arrays that repeatedly divides search space in half, achieving O(log n) time complexity for finding elements or boundaries.

```javascript
// Basic binary search
let left = 0, right = n - 1;
while (left <= right) {
  const mid = Math.floor((left + right) / 2);
  if (arr[mid] === target) return mid;
  if (arr[mid] < target) left = mid + 1;
  else right = mid - 1;
}
return -1;

// Search in rotated array
if (nums[left] <= nums[mid]) { // Left half sorted
  if (nums[left] <= target && target < nums[mid]) right = mid - 1;
  else left = mid + 1;
} else { // Right half sorted
  if (nums[mid] < target && target <= nums[right]) left = mid + 1;
  else right = mid - 1;
}

// Find insertion position
while (left <= right) {
  const mid = Math.floor((left + right) / 2);
  if (nums[mid] < target) left = mid + 1;
  else right = mid - 1;
}
return left; // Insertion position

```

- **Tips:** Left <= right for exact match; left < right for boundary search; adjust bounds based on sorted half in rotated arrays.

## Bit Manipulation

**Definition:** Operations on binary representations of numbers using bitwise operators (AND, OR, XOR, shifts) for efficient arithmetic and pattern detection.

```javascript
// Remove rightmost set bit
n = n & (n - 1);

// Check if bit is set
if (n & (1 << i)) { /* i-th bit is set */ }

// Set i-th bit
n |= (1 << i);

// Clear i-th bit
n &= ~(1 << i);

// XOR: duplicates cancel out
let result = 0;
for (const num of nums) result ^= num;

// Count set bits (Hamming weight)
let count = 0;
while (n !== 0) {
  n = n & (n - 1); // Remove rightmost set bit
  count++;
}

// Reverse bits
let result = 0;
for (let i = 0; i < 32; i++) {
  result = (result << 1) | (n & 1);
  n = n >>> 1;
}

```

- **Tips:** n & (n-1) removes rightmost set bit; XOR cancels duplicates; use >>> for unsigned right shift.

## Math

**Definition:** Mathematical algorithms including GCD (Euclidean), fast exponentiation, palindrome checks, and number theory concepts for efficient computation.

```javascript
// Check palindrome number (reverse half)
let reversed = 0, original = x;
while (x > reversed) {
  reversed = reversed * 10 + x % 10;
  x = Math.floor(x / 10);
}
return x === reversed || x === Math.floor(reversed / 10);

// Binary exponentiation (fast power)
function pow(x, n) {
  if (n < 0) { x = 1/x; n = -n; }
  let result = 1;
  while (n > 0) {
    if (n % 2 === 1) result *= x;
    x *= x;
    n = Math.floor(n / 2);
  }
  return result;
}

// GCD (Euclidean algorithm)
function gcd(a, b) {
  while (b !== 0) [a, b] = [b, a % b];
  return a;
}

// Square root (binary search)
let left = 2, right = Math.floor(x / 2);
while (left <= right) {
  const mid = Math.floor((left + right) / 2);
  const square = mid * mid;
  if (square === x) return mid;
  if (square < x) left = mid + 1;
  else right = mid - 1;
}
return right;

```

- **Tips:** Reverse half for palindrome check; binary exponentiation for O(log n) power; GCD via Euclidean algorithm.

---

## Complexity Reference

| Operation | Time Complexity |
|-----------|----------------|
| Array scan | **O(n)** |
| Sort | **O(n log n)** |
| Binary search | **O(log n)** |
| Hash operations | **O(1)** avg |
| Heap operations | **O(log n)** |
| Trie operations | **O(m)** where m is word length |
| DFS/BFS | **O(V + E)** |
| Tree traversal | **O(n)** where n is nodes |
| DP table fill | **O(states × transitions)** |
| Matrix operations | **O(mn)** |
| Binary exponentiation | **O(log n)** |
| GCD calculation | **O(log(min(a,b)))** |

## Common Pitfalls

- Off-by-one in windows and indices

- Overflow/precision (use `BigInt` when needed)

- Mutating inputs unintentionally

- Missing base/null checks

- Forgetting to backtrack in recursive solutions

- Not handling edge cases (empty arrays, single element, etc.)

- Wrong loop bounds in matrix operations

- Forgetting unsigned conversion in bit manipulation (>>>)

- Not normalizing slopes in geometry problems

## Quick Pattern Checklist

### Arrays & Strings

- [ ] Two pointers (opposite ends or same direction)

- [ ] Sliding window (variable or fixed size)

- [ ] Hash map for frequency/index tracking

- [ ] Prefix/suffix arrays

### Trees

- [ ] DFS (pre/in/post order)

- [ ] BFS (level-order)

- [ ] Fast/slow pointers for middle node

- [ ] Recursive structure for LCA/diameter

### Graphs

- [ ] DFS with visited set

- [ ] BFS with queue

- [ ] Topological sort (Kahn's algorithm)

- [ ] Union-Find for connectivity

### Dynamic Programming

- [ ] Define state and recurrence

- [ ] Initialize base cases

- [ ] Fill table in correct order

- [ ] Optimize space if possible

### Backtracking

- [ ] Choose, explore, un-choose pattern

- [ ] Prune invalid paths early

- [ ] Mark visited/unvisited correctly

### Binary Search

- [ ] Left <= right for exact match

- [ ] Left < right for boundary search

- [ ] Check sorted half in rotated arrays

### Bit Manipulation

- [ ] XOR for duplicate cancellation

- [ ] n & (n-1) for rightmost set bit

- [ ] Use >>> for unsigned shift

Happy practicing!
