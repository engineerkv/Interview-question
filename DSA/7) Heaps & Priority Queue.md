# Heaps / Priority Queue

```javascript
// Minimal binary heap utility
class Heap {
  constructor(cmp) {
    this.a = [];
    this.cmp = cmp;
  }
  
  size() {
    return this.a.length;
  }
  
  peek() {
    return this.a[0];
  }
  
  push(v) {
    this.a.push(v);
    this._up(this.a.length - 1);
  }
  
  pop() {
    if (!this.a.length) return undefined;
    const top = this.a[0];
    const last = this.a.pop();
    if (this.a.length) {
      this.a[0] = last;
      this._down(0);
    }
    return top;
  }
  
  _up(i) {
    const a = this.a;
    const cmp = this.cmp;
    while (i) {
      const p = (i - 1) >> 1;
      if (cmp(a[i], a[p])) {
        [a[i], a[p]] = [a[p], a[i]];
        i = p;
      } else {
        break;
      }
    }
  }
  
  _down(i) {
    const a = this.a;
    const cmp = this.cmp;
    for (;;) {
      let l = i * 2 + 1;
      let r = l + 1;
      let m = i;
      if (l < a.length && cmp(a[l], a[m])) {
        m = l;
      }
      if (r < a.length && cmp(a[r], a[m])) {
        m = r;
      }
      if (m === i) break;
      [a[i], a[m]] = [a[m], a[i]];
      i = m;
    }
  }
}
```

## Q86. Kth Largest Element

Concept: Maintain a min- heap of size k; pop when heap grows, top is kth largest.

```javascript
function findKthLargest(nums, k) {
  const h = new Heap((x, y) => x < y);
  for (const x of nums) {
    h.push(x);
    if (h.size() > k) {
      h.pop();
    }
  }
  return h.peek();
}

// Test Cases:
//
// Example 1:
//   Input: nums = [3, 2, 1, 5, 6, 4], k = 2
//   Output: 5
//
// Example 2:
//   Input: nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
//   Output: 4
//
// Example 3:
//   Input: nums = [1], k = 1
//   Output: 1
//
// Example 4:
//   Input: nums = [7, 10, 4, 3, 20, 15], k = 3
//   Output: 10
```

Deep Insights:
  - Rule: Maintain a min-heap of size k; pop when heap grows, top is kth largest; O(n log k) time, O(k) space.
  - Real-world: Kth largest queries, top-K selection, leaderboard systems, streaming algorithms.
  - Common mistake: Stream-friendly: process on the fly; wrong heap size; not handling k > n correctly.
  - Optimization: O(n log k) vs O(n log n) sort; space O(k) optimal; stream-friendly: process on the fly.
  - Interview tip: Explain min-heap vs max-heap clearly; mention stream processing; ask about k vs n relationship.
## Q87. Top K Frequent Elements

Concept: Count with Map, push [freq,val] into min-heap of size k.

```javascript
function topKFrequent(nums, k) {
  const cnt = new Map();
  for (const x of nums) {
    cnt.set(x, (cnt.get(x) || 0) + 1);
  }
  const h = new Heap((a, b) => a[0] < b[0]);
  for (const [v, f] of cnt) {
    h.push([f, v]);
    if (h.size() > k) {
      h.pop();
    }
  }
  const res = [];
  while (h.size()) {
    res.push(h.pop()[1]);
  }
  return res.reverse();
}

// Test Cases:
//
// Example 1:
//   Input: nums = [1, 1, 1, 2, 2, 3], k = 2
//   Output: [1, 2]
//
// Example 2:
//   Input: nums = [1], k = 1
//   Output: [1]
//
// Example 3:
//   Input: nums = [4, 1, -1, 2, -1, 2, 3], k = 2
//   Output: [-1, 2]
//
// Example 4:
//   Input: nums = [1, 1, 1, 2, 2, 3, 3, 3], k = 2
//   Output: [1, 3]
```

Deep Insights:
  - Rule: Count with Map, push [freq,val] into min-heap of size k; O(n + u log k) time where u is unique elements.
  - Real-world: Top-K frequent queries, frequency analysis, trending items, popularity ranking.
  - Common mistake: Reverse to return highest first; memory bounded by unique values; wrong heap comparator.
  - Optimization: O(n + u log k) time; space O(u) for map + O(k) for heap; memory bounded by unique values.
  - Interview tip: Explain frequency counting clearly; mention heap size optimization; ask about k vs unique count.
## Q88. Merge K Sorted Lists

Concept: Push each list head into min-heap by value; pop smallest, push its next.

```javascript
function mergeKLists(lists) {
  const h = new Heap((a, b) => a.val < b.val);
  for (const n of lists) {
    if (n) {
      h.push(n);
    }
  }
  const d = { next: null };
  let t = d;
  while (h.size()) {
    const n = h.pop();
    t.next = n;
    t = t.next;
    if (n.next) {
      h.push(n.next);
    }
  }
  return d.next;
}

// Test Cases:
//
// Example 1:
//   Input: lists = [[1,4,5],[1,3,4],[2,6]]
//   Output: [1,1,2,3,4,4,5,6]
//
// Example 2:
//   Input: lists = []
//   Output: []
//
// Example 3:
//   Input: lists = [[]]
//   Output: []
//
// Example 4:
//   Input: lists = [[1],[2],[3]]
//   Output: [1,2,3]
```

Deep Insights:
  - Rule: Push each list head into min-heap by value; pop smallest, push its next; O(n log k) time where k is lists.
  - Real-world: Merging sorted lists, external sorting, multi-way merge, sorted data combination.
  - Common mistake: Avoids full array materialization; wrong heap comparator; not handling empty lists.
  - Optimization: O(n log k) time optimal; space O(k) for heap; avoids full array materialization.
  - Interview tip: Explain heap-based merge clearly; mention divide-and-conquer alternative; ask about empty lists.
## Q89. Find Median from Stream

Concept: Two heaps: max-heap for lower half, min-heap for upper; balance sizes.

```javascript
class MedianFinder {
  constructor() {
    this.lo = new Heap((a, b) => a > b);
    this.hi = new Heap((a, b) => a < b);
  }

  addNum(num) {
    if (!this.lo.size() || num <= this.lo.peek()) {
      this.lo.push(num);
    } else {
      this.hi.push(num);
    }
    if (this.lo.size() > this.hi.size() + 1) {
      this.hi.push(this.lo.pop());
    }
    if (this.hi.size() > this.lo.size()) {
      this.lo.push(this.hi.pop());
    }
  }

  findMedian() {
    if (this.lo.size() > this.hi.size()) {
      return this.lo.peek();
    }
    return (this.lo.peek() + this.hi.peek()) / 2;
  }
}

// Test Cases:
//
// Example 1:
//   Input:
//     let mf = new MedianFinder();
//     mf.addNum(1);
//     mf.addNum(2);
//     mf.findMedian(); // Output: 1.5
//     mf.addNum(3);
//     mf.findMedian(); // Output: 2
//
// Example 2:
//   Input:
//     let mf = new MedianFinder();
//     mf.addNum(6);
//     mf.addNum(10);
//     mf.findMedian(); // Output: 8
//     mf.addNum(2);
//     mf.findMedian(); // Output: 6
//     mf.addNum(6);
//     mf.findMedian(); // Output: 6
```

Deep Insights:
  - Rule: Two heaps: max-heap for lower half, min-heap for upper; balance sizes; O(log n) add, O(1) findMedian.
  - Real-world: Running median, streaming statistics, dynamic median queries, online algorithms.
  - Common mistake: All integers supported; median can be float; robust to duplicates; wrong size balance.
  - Optimization: O(log n) add operation; O(1) findMedian; space O(n); robust to duplicates.
  - Interview tip: Explain two-heap approach clearly; mention size balancing; ask about even vs odd counts.
## Q90. K Closest Points to Origin

Concept: Max-heap of size k keyed by distance squared; eject farther points.

```javascript
function kClosest(points, k) {
  const h = new Heap((a, b) => a[0] > b[0]);
  for (const [x, y] of points) {
    const d = x * x + y * y;
    h.push([d, [x, y]]);
    if (h.size() > k) {
      h.pop();
    }
  }
  const res = [];
  while (h.size()) {
    res.push(h.pop()[1]);
  }
  return res;
}

// Test Cases:
//
// Example 1:
//   Input: points = [[1,3],[-2,2]], k = 1
//   Output: [[-2,2]]
//
// Example 2:
//   Input: points = [[3,3],[5,-1],[-2,4]], k = 2
//   Output: [[3,3],[-2,4]]
//
// Example 3:
//   Input: points = [[1,0],[0,1]], k = 2
//   Output: [[1,0],[0,1]]
//
// Example 4:
//   Input: points = [[0,1],[1,0]], k = 2
//   Output: [[0,1],[1,0]]
```

Deep Insights:
  - Rule: Max-heap of size k keyed by distance squared; eject farther points; O(n log k) time, O(k) space.
  - Real-world: K closest queries, nearest neighbors, spatial queries, distance-based selection.
  - Common mistake: For streaming points, same pattern; if need sorted by distance, sort result; wrong heap size.
  - Optimization: O(n log k) vs O(n log n) sort; space O(k) optimal; distance squared avoids sqrt.
  - Interview tip: Explain distance squared optimization; mention streaming variant; ask about sorted output.
## Q91. Connect Ropes to Min Cost

Concept: Always join two shortest first (Huffman-like) using min-heap.

```javascript
function connectSticks(sticks) {
  const h = new Heap((a, b) => a < b);
  for (const x of sticks) {
    h.push(x);
  }
  let cost = 0;
  while (h.size() > 1) {
    const a = h.pop();
    const b = h.pop();
    const c = a + b;
    cost += c;
    h.push(c);
  }
  return cost;
}

// Test Cases:
//
// Example 1:
//   Input: sticks = [2, 4, 3]
//   Output: 14
//   Explanation: Connect 2 and 3 (cost 5), then connect 5 and 4 (cost 9). Total = 5 + 9 = 14
//
// Example 2:
//   Input: sticks = [1, 8, 3, 5]
//   Output: 30
//   Explanation: Connect 1 and 3 (cost 4), then 4 and 5 (cost 9), then 9 and 8 (cost 17). Total = 4 + 9 + 17 = 30
//
// Example 3:
//   Input: sticks = [5]
//   Output: 0
//
// Example 4:
//   Input: sticks = [1, 2]
//   Output: 3
```

Deep Insights:
  - Rule: Always join two shortest first (Huffman-like) using min-heap; O(n log n) time, O(n) space.
  - Real-world: Minimum cost connection, Huffman coding, greedy optimization, cost minimization.
  - Common mistake: Returns 0 for <=1 stick; wrong heap comparator; forgetting to add combined cost.
  - Optimization: Greedy approach optimal; O(n log n) time; space O(n) for heap.
  - Interview tip: Explain Huffman-like approach clearly; mention greedy optimality; ask about edge cases.
## Q92. Reorganize String

Concept: Greedy pick two most frequent different chars from max-heap; push back with decremented counts.

```javascript
function reorganizeString(s) {
  const cnt = new Map();
  for (const c of s) {
    cnt.set(c, (cnt.get(c) || 0) + 1);
  }
  const h = new Heap((a, b) => a[0] > b[0]);
  for (const [c, f] of cnt) {
    h.push([f, c]);
  }
  let res = '';
  let prev = [0, ''];
  while (h.size()) {
    let [f, c] = h.pop();
    res += c;
    f--;
    if (prev[0] > 0) {
      h.push(prev);
    }
    prev = [f, c];
  }
  return res.length === s.length ? res : '';
}

// Test Cases:
//
// Example 1:
//   Input: s = "aab"
//   Output: "aba"
//
// Example 2:
//   Input: s = "aaab"
//   Output: ""
//
// Example 3:
//   Input: s = "aaabbc"
//   Output: "abacab"
//
// Example 4:
//   Input: s = "vvvlo"
//   Output: "vlvov"
```

Deep Insights:
  - Rule: Greedy pick two most frequent different chars from max-heap; push back with decremented counts; O(n log u) time.
  - Real-world: String reorganization, scheduling with constraints, task assignment, conflict resolution.
  - Common mistake: Returns empty if impossible; wrong char selection; not handling prev char correctly.
  - Optimization: Greedy approach; O(n log u) time where u is unique chars; space O(u) for heap.
  - Interview tip: Explain greedy strategy clearly; mention impossibility condition; ask about alternative approaches.
## Q93. Maximum Sliding Window (Heap variant)

Concept: Max- heap with lazy deletion using indices; pop until top inside window.

```javascript
function maxSlidingWindowHeap(nums, k) {
  const h = new Heap((a, b) => a[0] > b[0]);
  let res = [];
  for (let i = 0; i < nums.length; i++) {
    h.push([nums[i], i]);
    while (h.peek() && h.peek()[1] <= i - k) {
      h.pop();
    }
    if (i >= k - 1) {
      res.push(h.peek()[0]);
    }
  }
  return res;
}

// Test Cases:
//
// Example 1:
//   Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
//   Output: [3, 3, 5, 5, 6, 7]
//
// Example 2:
//   Input: nums = [1], k = 1
//   Output: [1]
//
// Example 3:
//   Input: nums = [1, -1], k = 1
//   Output: [1, -1]
//
// Example 4:
//   Input: nums = [9, 11], k = 2
//   Output: [11]
```

Deep Insights:
  - Rule: Max-heap with lazy deletion using indices; pop until top inside window; O(n log n) time, O(n) space.
  - Real-world: Sliding window maximum, range queries, window-based algorithms, stream processing.
  - Common mistake: Use deque version for optimal; lazy deletion needed; not handling window boundaries correctly.
  - Optimization: Deque version is O(n) optimal; heap version is simpler but slower; lazy deletion important.
  - Interview tip: Mention deque alternative; explain lazy deletion; ask about time complexity trade-offs.
## Q94. Smallest Range Covering Elements (k lists)

Concept: Min- heap on current heads; track current max; update best range and advance the list of the min.

```javascript
function smallestRange(nums) {
  const k = nums.length;
  const h = new Heap((a, b) => a.val < b.val);
  let curMax = -Infinity;
  for (let i = 0; i < k; i++) {
    h.push({ val: nums[i][0], i, idx: 0 });
    curMax = Math.max(curMax, nums[i][0]);
  }
  let best = [-Infinity, Infinity];
  while (h.size()) {
    const { val, i, idx } = h.pop();
    if (curMax - val < best[1] - best[0]) {
      best = [val, curMax];
    }
    if (idx + 1 === nums[i].length) break;
    const nv = nums[i][idx + 1];
    h.push({ val: nv, i, idx: idx + 1 });
    if (nv > curMax) {
      curMax = nv;
    }
  }
  return best;
}

// Test Cases:
//
// Example 1:
//   Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
//   Output: [20, 24]
//
// Example 2:
//   Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
//   Output: [1, 1]
//
// Example 3:
//   Input: nums = [[10,10],[11,11]]
//   Output: [10, 11]
//
// Example 4:
//   Input: nums = [[1],[2],[3],[4],[5],[6],[7]]
//   Output: [1, 7]
```

Deep Insights:
  - Rule: Min-heap on current heads; track current max; update best range and advance list of min; O(n log k) time.
  - Real-world: Smallest range covering, range queries across lists, multi-list range problems, covering algorithms.
  - Common mistake: Stop when any list exhausted; wrong range update; not tracking current max correctly.
  - Optimization: O(n log k) time where k is lists; space O(k) for heap; stop when any list exhausted.
  - Interview tip: Explain range update logic clearly; mention stopping condition; ask about list sizes.
## Q95. Heapsort

Concept: Build max-heap, repeatedly extract max to the end; in-place O(n log n).

```javascript
function heapSort(arr) {
  const n = arr.length;
  const down = (i, sz) => {
    while (true) {
      let l = i * 2 + 1;
      let r = l + 1;
      let m = i;
      if (l < sz && arr[l] > arr[m]) {
        m = l;
      }
      if (r < sz && arr[r] > arr[m]) {
        m = r;
      }
      if (m === i) break;
      [arr[i], arr[m]] = [arr[m], arr[i]];
      i = m;
    }
  };

  for (let i = (n - 1) >> 1; i >= 0; i--) {
    down(i, n);
  }
  for (let end = n - 1; end > 0; end--) {
    [arr[0], arr[end]] = [arr[end], arr[0]];
    down(0, end);
  }
  return arr;
}

// Test Cases:
//
// Example 1:
//   Input: arr = [4, 10, 3, 5, 1]
//   Output: [1, 3, 4, 5, 10]
//
// Example 2:
//   Input: arr = [64, 34, 25, 12, 22, 11, 90]
//   Output: [11, 12, 22, 25, 34, 64, 90]
//
// Example 3:
//   Input: arr = [1]
//   Output: [1]
//
// Example 4:
//   Input: arr = [5, 2, 8, 1, 9]
//   Output: [1, 2, 5, 8, 9]
```

Deep Insights:
  - Rule: Build max-heap, repeatedly extract max to the end; in-place O(n log n) time, O(1) space.
  - Real-world: In-place sorting, stable worst-case sorting, guaranteed O(n log n), array-based sorting.
  - Common mistake: Often slower than quicksort in practice; good worst-case guarantees; array-based binary heap.
  - Optimization: O(n log n) worst-case; O(1) extra space; often slower than quicksort in practice.
  - Interview tip: Explain heapify process clearly; mention worst-case guarantee; ask about space optimization.

## Q96. IPO

Concept:
Choose k projects with max profit; sort projects by capital; use max-heap for profits within capital budget.

Example:
```javascript
function findMaximizedCapital(k, w, profits, capital) {
  const n = profits.length;
  const projects = [];
  
  for (let i = 0; i < n; i++) {
    projects.push([capital[i], profits[i]]);
  }
  
  projects.sort((a, b) => a[0] - b[0]);
  
  let availableProjects = [];
  let projectIndex = 0;
  let currentCapital = w;
  
  for (let i = 0; i < k; i++) {
    // Add all projects we can afford
    while (projectIndex < n && projects[projectIndex][0] <= currentCapital) {
      availableProjects.push(projects[projectIndex][1]);
      projectIndex++;
    }
    
    if (availableProjects.length === 0) break;
    
    // Use max-heap to get highest profit
    availableProjects.sort((a, b) => b - a);
    const maxProfit = availableProjects.shift();
    currentCapital += maxProfit;
  }
  
  return currentCapital;
}

// Using proper max-heap implementation:
function findMaximizedCapital(k, w, profits, capital) {
  const n = profits.length;
  const projects = [];
  
  for (let i = 0; i < n; i++) {
    projects.push([capital[i], profits[i]]);
  }
  
  projects.sort((a, b) => a[0] - b[0]);
  
  const maxHeap = new MaxHeap();
  let projectIndex = 0;
  let currentCapital = w;
  
  for (let i = 0; i < k; i++) {
    while (projectIndex < n && projects[projectIndex][0] <= currentCapital) {
      maxHeap.push(projects[projectIndex][1]);
      projectIndex++;
    }
    
    if (maxHeap.isEmpty()) break;
    
    currentCapital += maxHeap.pop();
  }
  
  return currentCapital;
}

// Test Cases:
//
// Example 1:
//   Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
//   Output: 4
//   Explanation: Start with capital 0, choose project 0 (capital=0, profit=1), then project 2 (capital=1, profit=3)
//
// Example 2:
//   Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
//   Output: 6
//   Explanation: Choose all three projects
```

**Time Complexity:** O(n log n + k log n) - Sort projects + k heap operations  
**Space Complexity:** O(n) - Heap storage

Deep Insights:
- Sort projects by capital; use max-heap for profits within budget; O(n log n + k log n) time.
- Greedy: choose highest profit from affordable projects each step.
- Sort once; maintain heap of affordable projects.
- Edge case: No affordable projects returns current capital; k = 0 returns initial capital.
- Interview tip: Explain greedy strategy; mention sorting + heap combination; ask about optimization.

## Q97. Find K Pairs with Smallest Sums

Concept:
Generate pairs from two sorted arrays; use min-heap to find k smallest sums; track indices to avoid duplicates.

Example:
```javascript
function kSmallestPairs(nums1, nums2, k) {
  const result = [];
  const minHeap = new MinHeap();
  
  // Initialize heap with first k pairs from nums1[0]
  for (let i = 0; i < Math.min(nums1.length, k); i++) {
    minHeap.push([nums1[i] + nums2[0], i, 0]);
  }
  
  while (result.length < k && !minHeap.isEmpty()) {
    const [sum, i, j] = minHeap.pop();
    result.push([nums1[i], nums2[j]]);
    
    // Add next pair from same nums1[i]
    if (j + 1 < nums2.length) {
      minHeap.push([nums1[i] + nums2[j + 1], i, j + 1]);
    }
  }
  
  return result;
}

// Test Cases:
//
// Example 1:
//   Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
//   Output: [[1,2],[1,4],[1,6]]
//   Explanation: Smallest sums: 1+2=3, 1+4=5, 1+6=7
//
// Example 2:
//   Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
//   Output: [[1,1],[1,1]]
//   Explanation: Smallest sums: 1+1=2, 1+1=2
//
// Example 3:
//   Input: nums1 = [1,2], nums2 = [3], k = 3
//   Output: [[1,3],[2,3]]
//   Explanation: Only 2 pairs possible
```

**Time Complexity:** O(k log k) - k heap operations  
**Space Complexity:** O(k) - Heap storage

Deep Insights:
- Initialize heap with (nums1[i] + nums2[0]) for each i; extract min and add next from same i; O(k log k) time.
- Track indices (i,j) to generate pairs systematically.
- When extracting (i,j), add (i,j+1) if exists.
- Edge case: k larger than total pairs; return all pairs.
- Interview tip: Explain heap initialization; mention index tracking; ask about duplicate handling.