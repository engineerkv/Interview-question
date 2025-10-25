# 🧩 DSA Interview Notes - LeetCode Top 150

## 🔺 Section 15 — Heap / Priority Queue — Q147-Q150

---

### 147. 🔺 Kth Largest Element in Array

**🧠 Concept**

Find kth largest element using min heap of size k to maintain top k elements.

**💻 Example**

```javascript
function findKthLargest(nums, k) {
  const minHeap = [];
  
  for (const num of nums) {
    if (minHeap.length < k) {
      minHeap.push(num);
      minHeap.sort((a, b) => a - b);
    } else if (num > minHeap[0]) {
      minHeap[0] = num;
      minHeap.sort((a, b) => a - b);
    }
  }
  
  return minHeap[0];
}
```

**💬 Explanation + Insight**

- **Min Heap** - Keep smallest k elements in heap
- **Size Constraint** - Maintain heap size of k
- **Root Access** - Root is kth largest element
- **Time Complexity** - O(n log k) for n elements
- **Space Complexity** - O(k) for heap

---

### 148. 🔺 Find K Pairs with Smallest Sums

**🧠 Concept**

Find k pairs with smallest sums using min heap with pair sum as priority.

**💻 Example**

```javascript
function kSmallestPairs(nums1, nums2, k) {
  const result = [];
  const heap = [];
  
  for (let i = 0; i < Math.min(nums1.length, k); i++) {
    heap.push([nums1[i] + nums2[0], i, 0]);
  }
  
  heap.sort((a, b) => a[0] - b[0]);
  
  while (result.length < k && heap.length > 0) {
    const [sum, i, j] = heap.shift();
    result.push([nums1[i], nums2[j]]);
    
    if (j + 1 < nums2.length) {
      heap.push([nums1[i] + nums2[j + 1], i, j + 1]);
      heap.sort((a, b) => a[0] - b[0]);
    }
  }
  
  return result;
}
```

**💬 Explanation + Insight**

- **Min Heap** - Use sum as priority for heap
- **Pair Generation** - Generate pairs in order of sum
- **Next Pair** - Add next pair from same first array
- **Time Complexity** - O(k log k) for k pairs
- **Space Complexity** - O(k) for heap

---

### 149. 🔺 Find Median from Data Stream

**🧠 Concept**

Find median from stream using two heaps - max heap for smaller half, min heap for larger half.

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
    
    // Balance heaps
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
- **Balance Maintenance** - Keep heaps balanced in size
- **Median Calculation** - Top of larger heap or average of both
- **Time Complexity** - O(log n) for addNum, O(1) for findMedian
- **Space Complexity** - O(n) for heaps

---

### 150. 🔺 IPO

**🧠 Concept**

Maximize capital by selecting projects with highest profit within capital constraint using greedy approach with heaps.

**💻 Example**

```javascript
function findMaximizedCapital(k, w, profits, capital) {
  const projects = [];
  for (let i = 0; i < profits.length; i++) {
    projects.push([capital[i], profits[i]]);
  }
  
  projects.sort((a, b) => a[0] - b[0]);
  
  const maxHeap = [];
  let projectIndex = 0;
  
  for (let i = 0; i < k; i++) {
    while (projectIndex < projects.length && projects[projectIndex][0] <= w) {
      maxHeap.push(projects[projectIndex][1]);
      projectIndex++;
    }
    
    if (maxHeap.length === 0) break;
    
    maxHeap.sort((a, b) => b - a);
    w += maxHeap.shift();
  }
  
  return w;
}
```

**💬 Explanation + Insight**

- **Greedy Selection** - Always choose highest profit project
- **Capital Constraint** - Only consider affordable projects
- **Heap Management** - Use max heap for profit selection
- **Time Complexity** - O(n log n) for sorting and heap operations
- **Space Complexity** - O(n) for heap

---

*This comprehensive heap and priority queue section covers essential heap operations including element selection, median finding, and optimization techniques for efficient data processing.*