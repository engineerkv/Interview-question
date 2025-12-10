# Heaps / Priority Queue

---

## 📍 Navigation

<div align="center">

[← Previous: Binary Search Tree](06%29%20Binary%20Search%20Tree.md) • [Home: README](README.md) • [Next: Graphs →](08%29%20Graphs.md)

[📋 Cheatsheet](DSA%20Interview%20Cheatsheet.md)

</div>

---

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
        [a[i], a[p] = [a[p], a[i];
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
      [a[i], a[m] = [a[m], a[i];
      i = m;
    }
  }
}

```

## Q124. 📋 Kth Largest Element in an Array

**Problem:** Given an integer array `nums` and an integer `k`, return the `k`th largest element in the array. Note that it is the `k`th largest element in the sorted order, not the `k`th distinct element.

**Approach:** Maintain a min-heap of size k. When heap size exceeds k, pop the smallest. Top of heap is kth largest.

### Solution 1: Min-Heap of Size K (Optimal)

```javascript
function findKthLargest(nums, k) {
  const heap = new Heap((a, b) => a < b);  // Min-heap

  for (const num of nums) {
    heap.push(num);
    // Keep heap size at k
    if (heap.size() > k) {
      heap.pop();  // Remove smallest
    }
  }

  return heap.peek();  // Kth largest is at top
}

// Test Cases:
// Input: nums = [3, 2, 1, 5, 6, 4], k = 2
// Output: 5

// Input: nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
// Output: 4

// Input: nums = [1], k = 1
// Output: 1

// Input: nums = [7, 10, 4, 3, 20, 15], k = 3
// Output: 10

```

**Time Complexity:** O(n log k) - n insertions, each O(log k)
**Space Complexity:** O(k) - Heap stores k elements

## Q125. 💡 Top K Frequent Elements

**Problem:** Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

**Approach:** Count frequencies with map, then use min-heap of size k to track top k frequent elements.

### Solution 1: Frequency Count + Min-Heap (Optimal)

```javascript
function topKFrequent(nums, k) {
  // Count frequencies
  const frequency = new Map();
  for (const num of nums) {
    frequency.set(num, (frequency.get(num) || 0) + 1);
  }

  // Min-heap: [frequency, value]
  const heap = new Heap((a, b) => a[0] < b[0]);

  for (const [value, freq] of frequency) {
    heap.push([freq, value]);
    // Keep heap size at k
    if (heap.size() > k) {
      heap.pop();  // Remove least frequent
    }
  }

  // Extract results
  const result = [];
  while (heap.size()) {
    result.push(heap.pop()[1]);
  }

  return result.reverse();  // Reverse to get descending order
}

// Test Cases:
// Input: nums = [1, 1, 1, 2, 2, 3], k = 2
// Output: [1, 2]

// Input: nums = [1], k = 1
// Output: [1]

// Input: nums = [4, 1, -1, 2, -1, 2, 3], k = 2
// Output: [-1, 2]

// Input: nums = [1, 1, 1, 2, 2, 3, 3, 3], k = 2
// Output: [1, 3]

```

**Time Complexity:** O(n + u log k) - n for counting, u log k for heap operations (u is unique elements)
**Space Complexity:** O(u) - Map stores unique elements, heap stores k elements

## Q126. 🔀 Merge k Sorted Lists

**Problem:** You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.

**Approach:** Push each list head into min-heap. Pop smallest, append to result, push its next node.

### Solution 1: Min-Heap Merge (Optimal)

```javascript
function mergeKLists(lists) {
  const heap = new Heap((a, b) => a.val < b.val);  // Min-heap by value

  // Push all list heads
  for (const list of lists) {
    if (list) {
      heap.push(list);
    }
  }

  const dummy = { next: null };
  let tail = dummy;

  while (heap.size()) {
    const node = heap.pop();
    tail.next = node;
    tail = tail.next;

    // Push next node from same list
    if (node.next) {
      heap.push(node.next);
    }
  }

  return dummy.next;
}

// Test Cases:
// Input: lists = [1,4,5],[1,3,4],[2,6]
// Output: [1,1,2,3,4,4,5,6]

// Input: lists = []
// Output: []

// Input: lists = []
// Output: []

// Input: lists = [1],[2],[3]
// Output: [1,2,3]

```

**Time Complexity:** O(n log k) - n total nodes, k lists, each operation O(log k)
**Space Complexity:** O(k) - Heap stores at most k list heads

## Q127. 🌊 Find Median from Data Stream

**Problem:** The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values. Implement the MedianFinder class:

- `MedianFinder()` initializes the MedianFinder object.

- `void addNum(int num)` adds the integer `num` from the data stream to the data structure.

- `double findMedian()` returns the median of all elements so far.

**Approach:** Use two heaps: max-heap for lower half, min-heap for upper half. Balance sizes to maintain median property.

### Solution 1: Two Heaps (Optimal)

```javascript
class MedianFinder {
  constructor() {
    this.lower = new Heap((a, b) => a > b);  // Max-heap for lower half
    this.upper = new Heap((a, b) => a < b);  // Min-heap for upper half
  }

  addNum(num) {
    // Add to appropriate heap
    if (!this.lower.size() || num <= this.lower.peek()) {
      this.lower.push(num);
    } else {
      this.upper.push(num);
    }

    // Balance heaps: lower can have at most 1 more element
    if (this.lower.size() > this.upper.size() + 1) {
      this.upper.push(this.lower.pop());
    }
    if (this.upper.size() > this.lower.size()) {
      this.lower.push(this.upper.pop());
    }
  }

  findMedian() {
    if (this.lower.size() > this.upper.size()) {
      // Odd count: median is top of lower heap
      return this.lower.peek();
    }
    // Even count: median is average of both tops
    return (this.lower.peek() + this.upper.peek()) / 2;
  }
}

// Test Cases:
// Input:
// let mf = new MedianFinder();
// mf.addNum(1);
// mf.addNum(2);
// mf.findMedian(); // Output: 1.5
// mf.addNum(3);
// mf.findMedian(); // Output: 2

// Input:
// let mf = new MedianFinder();
// mf.addNum(6);
// mf.addNum(10);
// mf.findMedian(); // Output: 8
// mf.addNum(2);
// mf.findMedian(); // Output: 6
// mf.addNum(6);
// mf.findMedian(); // Output: 6

```

**Time Complexity:** O(log n) - addNum, O(1) - findMedian
**Space Complexity:** O(n) - Both heaps store elements

## Q128. 💡 K Closest Points to Origin

**Problem:** Given an array of `points` where `points[i] = [xi, yi]` represents a point on the X-Y plane and an integer `k`, return the `k` closest points to the origin `(0, 0)`. The distance between two points on the X-Y plane is the Euclidean distance.

**Approach:** Use max-heap of size k keyed by distance squared. When heap size exceeds k, pop farthest point.

### Solution 1: Max-Heap of Size K (Optimal)

```javascript
function kClosest(points, k) {
  const heap = new Heap((a, b) => a[0] > b[0]);  // Max-heap by distance

  for (const [x, y] of points) {
    const distSq = x * x + y * y;  // Distance squared (avoid sqrt)
    heap.push([distSq, [x, y]);

    // Keep heap size at k
    if (heap.size() > k) {
      heap.pop();  // Remove farthest
    }
  }

  // Extract results
  const result = [];
  while (heap.size()) {
    result.push(heap.pop()[1]);
  }

  return result;
}

// Test Cases:
// Input: points = [1,3],[-2,2], k = 1
// Output: [-2,2]

// Input: points = [3,3],[5,-1],[-2,4], k = 2
// Output: [3,3],[-2,4]

// Input: points = [1,0],[0,1], k = 2
// Output: [1,0],[0,1]

// Input: points = [0,1],[1,0], k = 2
// Output: [0,1],[1,0]

```

**Time Complexity:** O(n log k) - n insertions, each O(log k)
**Space Complexity:** O(k) - Heap stores k elements

## Q129. ⬇️ ⬇️ ⬇️ Minimum Cost to Connect Sticks

**Problem:** You have some sticks with positive integer lengths. You can connect any two sticks of lengths `x` and `y` into one stick by paying a cost of `x + y`. You must connect all the sticks into one stick. Return the minimum cost of connecting all the given sticks into one stick in this way.

**Approach:** Always join two shortest sticks first (Huffman-like greedy approach) using min-heap.

### Solution 1: Greedy with Min-Heap (Optimal)

```javascript
function connectSticks(sticks) {
  const heap = new Heap((a, b) => a < b);  // Min-heap

  // Push all sticks
  for (const stick of sticks) {
    heap.push(stick);
  }

  let totalCost = 0;

  // Connect until one stick remains
  while (heap.size() > 1) {
    const first = heap.pop();
    const second = heap.pop();
    const cost = first + second;
    totalCost += cost;
    heap.push(cost);  // Push combined stick back
  }

  return totalCost;
}

// Test Cases:
// Input: sticks = [2, 4, 3]
// Output: 14
// Explanation: Connect 2 and 3 (cost 5), then connect 5 and 4 (cost 9). Total = 5 + 9 = 14

// Input: sticks = [1, 8, 3, 5]
// Output: 30
// Explanation: Connect 1 and 3 (cost 4), then 4 and 5 (cost 9), then 9 and 8 (cost 17). Total = 4 + 9 + 17 = 30

// Input: sticks = [5]
// Output: 0

// Input: sticks = [1, 2]
// Output: 3

```

**Time Complexity:** O(n log n) - n operations on heap
**Space Complexity:** O(n) - Heap stores sticks

## Q130. 🔤 Reorganize String

**Problem:** Given a string `s`, rearrange the characters of `s` so that any two adjacent characters are not the same. Return any possible rearrangement of `s` or return `""` if it is not possible to rearrange the string.

**Approach:** Greedy approach: pick two most frequent different characters from max-heap. Push back with decremented counts to avoid adjacent duplicates.

### Solution 1: Greedy with Max-Heap (Optimal)

```javascript
function reorganizeString(s) {
  // Count character frequencies
  const frequency = new Map();
  for (const char of s) {
    frequency.set(char, (frequency.get(char) || 0) + 1);
  }

  // Max-heap: [frequency, character]
  const heap = new Heap((a, b) => a[0] > b[0]);
  for (const [char, freq] of frequency) {
    heap.push([freq, char]);
  }

  let result = '';
  let prev = [0, ''];  // Previous character used

  while (heap.size()) {
    let [freq, char] = heap.pop();
    result += char;
    freq--;

    // Push previous character back if still has count
    if (prev[0] > 0) {
      heap.push(prev);
    }

    // Store current character as previous (with decremented count)
    prev = [freq, char];
  }

  // Return result if valid, else empty string
  return result.length === s.length ? result : '';
}

// Test Cases:
// Input: s = "aab"
// Output: "aba"

// Input: s = "aaab"
// Output: ""

// Input: s = "aaabbc"
// Output: "abacab"

// Input: s = "vvvlo"
// Output: "vlvov"

```

**Time Complexity:** O(n log u) - n characters, u unique chars, each heap operation O(log u)
**Space Complexity:** O(u) - Heap stores unique characters

## Q131. 🪟 🪟 🪟 Sliding Window Maximum (Heap Variant)

**Problem:** You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position. Return the maximum element in each sliding window.

**Approach:** Use max-heap with lazy deletion using indices. When top element is outside window, pop until top is inside window.

### Solution 1: Max-Heap with Lazy Deletion

```javascript
function maxSlidingWindowHeap(nums, k) {
  const heap = new Heap((a, b) => a[0] > b[0]);  // Max-heap: [value, index]
  const result = [];

  for (let i = 0; i < nums.length; i++) {
    // Add current element
    heap.push([nums[i], i]);

    // Lazy deletion: remove elements outside window
    while (heap.peek() && heap.peek()[1] <= i - k) {
      heap.pop();
    }

    // Add maximum when window is complete
    if (i >= k - 1) {
      result.push(heap.peek()[0]);
    }
  }

  return result;
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

```

**Time Complexity:** O(n log n) - Worst case when all elements popped
**Space Complexity:** O(n) - Heap stores elements

## Q132. 💡 Smallest Range Covering Elements from K Lists

**Problem:** You have `k` lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the `k` lists.

**Approach:** Use min-heap on current heads of all lists. Track current maximum. Update best range and advance the list of the minimum element.

### Solution 1: Min-Heap with Range Tracking (Optimal)

```javascript
function smallestRange(nums) {
  const k = nums.length;
  const heap = new Heap((a, b) => a.val < b.val);  // Min-heap
  let currentMax = -Infinity;

  // Initialize heap with first element of each list
  for (let i = 0; i < k; i++) {
    heap.push({ val: nums[i][0], listIndex: i, elementIndex: 0 });
    currentMax = Math.max(currentMax, nums[i][0]);
  }

  let bestRange = [-Infinity, Infinity];

  while (heap.size()) {
    const { val, listIndex, elementIndex } = heap.pop();

    // Update best range if current range is smaller
    if (currentMax - val < bestRange[1] - bestRange[0]) {
      bestRange = [val, currentMax];
    }

    // Stop if any list is exhausted
    if (elementIndex + 1 === nums[listIndex].length) break;

    // Advance to next element in same list
    const nextVal = nums[listIndex][elementIndex + 1];
    heap.push({ val: nextVal, listIndex, elementIndex: elementIndex + 1 });

    // Update current maximum
    if (nextVal > currentMax) {
      currentMax = nextVal;
    }
  }

  return bestRange;
}

// Test Cases:
// Input: nums = [4,10,15,24,26],[0,9,12,20],[5,18,22,30]
// Output: [20, 24]

// Input: nums = [1,2,3],[1,2,3],[1,2,3]
// Output: [1, 1]

// Input: nums = [10,10],[11,11]
// Output: [10, 11]

// Input: nums = [1],[2],[3],[4],[5],[6],[7]
// Output: [1, 7]

```

**Time Complexity:** O(n log k) - n total elements, k lists, each heap operation O(log k)
**Space Complexity:** O(k) - Heap stores k list heads

## Q133. 🔀 Heapsort

**Problem:** Implement heapsort algorithm to sort an array in ascending order. Heapsort is an in-place sorting algorithm with O(n log n) worst-case time complexity.

**Approach:** Build max-heap from array, then repeatedly extract maximum to the end. Heapify down to maintain heap property.

### Solution 1: In-Place Heapsort (Optimal)

```javascript
function heapSort(arr) {
  const n = arr.length;

  // Heapify down function
  function heapifyDown(i, size) {
    while (true) {
      let left = i * 2 + 1;
      let right = left + 1;
      let max = i;

      if (left < size && arr[left] > arr[max]) {
        max = left;
      }
      if (right < size && arr[right] > arr[max]) {
        max = right;
      }

      if (max === i) break;

      [arr[i], arr[max] = [arr[max], arr[i];
      i = max;
    }
  }

  // Build max-heap (heapify from bottom up)
  for (let i = Math.floor((n - 1) / 2); i >= 0; i--) {
    heapifyDown(i, n);
  }

  // Extract max to end repeatedly
  for (let end = n - 1; end > 0; end--) {
    [arr[0], arr[end] = [arr[end], arr[0];  // Swap max to end
    heapifyDown(0, end);  // Heapify down excluding sorted part
  }

  return arr;
}

// Test Cases:
// Input: arr = [4, 10, 3, 5, 1]
// Output: [1, 3, 4, 5, 10]

// Input: arr = [64, 34, 25, 12, 22, 11, 90]
// Output: [11, 12, 22, 25, 34, 64, 90]

// Input: arr = [1]
// Output: [1]

// Input: arr = [5, 2, 8, 1, 9]
// Output: [1, 2, 5, 8, 9]

```

**Time Complexity:** O(n log n) - Build heap O(n), extract n times O(log n) each
**Space Complexity:** O(1) - In-place sorting, only swap operations

## Q134. 💡 IPO (Initial Public Offering)

**Problem:** You are given several projects with their capital requirements and profits. You can start with initial capital `w`. For each project, you need capital to start it, and you'll get profit. You can choose at most `k` projects. Return the maximum capital you can accumulate.

**Approach:** Sort projects by capital. Use max-heap to track profits of affordable projects. Greedily choose highest profit project each step.

### Solution 1: Greedy with Max-Heap (Optimal)

```javascript
function findMaximizedCapital(k, w, profits, capital) {
  const n = profits.length;
  const projects = [];

  // Create [capital, profit] pairs
  for (let i = 0; i < n; i++) {
    projects.push([capital[i], profits[i]);
  }

  // Sort by capital requirement
  projects.sort((a, b) => a[0] - b[0]);

  const maxHeap = new Heap((a, b) => a > b);  // Max-heap for profits
  let projectIndex = 0;
  let currentCapital = w;

  for (let i = 0; i < k; i++) {
    // Add all affordable projects to heap
    while (projectIndex < n && projects[projectIndex][0] <= currentCapital) {
      maxHeap.push(projects[projectIndex][1]);
      projectIndex++;
    }

    // No affordable projects
    if (!maxHeap.size()) break;

    // Choose highest profit project
    currentCapital += maxHeap.pop();
  }

  return currentCapital;
}

// Test Cases:
// Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
// Output: 4
// Explanation: Start with capital 0, choose project 0 (capital=0, profit=1), then project 2 (capital=1, profit=3)

// Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
// Output: 6
// Explanation: Choose all three projects

```

**Time Complexity:** O(n log n + k log n) - Sort projects O(n log n) + k heap operations O(k log n)
**Space Complexity:** O(n) - Heap stores profits

## Q135. ➕ Find K Pairs with Smallest Sums

**Problem:** You are given two integer arrays `nums1` and `nums2` sorted in non-decreasing order and an integer `k`. Define a pair `(u, v)` which consists of one element from the first array and one element from the second array. Return the `k` pairs `(u1, v1), (u2, v2), ..., (uk, vk)` with the smallest sums.

**Approach:** Use min-heap to track pairs with smallest sums. Initialize with first element of nums2 paired with each element of nums1. Then expand by moving forward in nums2.

### Solution 1: Min-Heap with Index Tracking (Optimal)

```javascript
function kSmallestPairs(nums1, nums2, k) {
  const heap = new Heap((a, b) => a[0] < b[0]);  // Min-heap: [sum, i, j]
  const result = [];

  // Initialize heap with first element of nums2 paired with each element of nums1
  for (let i = 0; i < Math.min(nums1.length, k); i++) {
    heap.push([nums1[i] + nums2[0], i, 0]);
  }

  while (result.length < k && heap.size()) {
    const [sum, i, j] = heap.pop();
    result.push([nums1[i], nums2[j]);

    // Add next pair from same nums1[i] (move forward in nums2)
    if (j + 1 < nums2.length) {
      heap.push([nums1[i] + nums2[j + 1], i, j + 1]);
    }
  }

  return result;
}

// Test Cases:
// Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
// Output: [1,2],[1,4],[1,6]
// Explanation: Smallest sums: 1+2=3, 1+4=5, 1+6=7

// Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
// Output: [1,1],[1,1]
// Explanation: Smallest sums: 1+1=2, 1+1=2

// Input: nums1 = [1,2], nums2 = [3], k = 3
// Output: [1,3],[2,3]
// Explanation: Only 2 pairs possible

```

**Time Complexity:** O(k log k) - k heap operations, each O(log k)
**Space Complexity:** O(k) - Heap stores k pairs

- **Interview Tip:** Explain initialization strategy clearly; emphasize index tracking; ask about duplicate handling

---

## 📍 Navigation

<div align="center">

[← Previous: Binary Search Tree](06%29%20Binary%20Search%20Tree.md) • [Home: README](README.md) • [Next: Graphs →](08%29%20Graphs.md)

[📋 Cheatsheet](DSA%20Interview%20Cheatsheet.md)

</div>
