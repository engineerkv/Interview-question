# 🧩 DSA Cheatsheet - LeetCode Top 150

## 🚀 Quick Reference Guide

### 🟦 Array/String Basics (Q1-Q17)
- **Two Pointers**: Remove duplicates, merge arrays
- **In-place Operations**: Modify arrays without extra space
- **String Manipulation**: Roman numerals, text justification
- **Key Patterns**: Sliding window, prefix/suffix products

### 🟧 Two Pointers/Sliding Window (Q18-Q26)
- **Valid Palindrome**: Compare from both ends
- **Container With Most Water**: Two pointers from ends
- **3Sum**: Sort + two pointers for O(n²)
- **Sliding Window**: Longest substring, minimum window

### 🟨 Hash Table/Set (Q27-Q35)
- **Two Sum**: Hash map for O(1) lookup
- **Group Anagrams**: Sorted string as key
- **Longest Consecutive**: Set for O(1) lookup
- **Pattern Matching**: Character frequency maps

### 🟩 Greedy (Q36-Q42)
- **Stock Trading**: Buy before every increase
- **Gas Station**: Track surplus/deficit
- **Jump Game**: Greedy reachability
- **Interval Scheduling**: Sort by end time

### 🟪 Sorting/Binary Search (Q43-Q52)
- **Rotated Array**: Modified binary search
- **Search Range**: Find first/last occurrence
- **2D Matrix**: Treat as 1D array
- **Kth Element**: Quick select algorithm

### 🧱 Stack/Queue/Design (Q53-Q60)
- **Valid Parentheses**: Stack for matching
- **Min Stack**: Auxiliary stack for minimum
- **LRU Cache**: HashMap + Doubly Linked List
- **Data Stream**: Two heaps for median

### 🔗 Linked List (Q61-Q71)
- **Add Two Numbers**: Reverse order addition
- **Merge Lists**: Two pointers comparison
- **Reverse in Groups**: Recursive/iterative
- **Cycle Detection**: Floyd's algorithm

### 🧠 Dynamic Programming (Q72-Q88)
- **Climbing Stairs**: Fibonacci pattern
- **House Robber**: Adjacent constraint
- **Longest Subsequence**: 2D DP table
- **Edit Distance**: 2D DP for string comparison

### 🧭 Backtracking (Q89-Q96)
- **Phone Combinations**: DFS with backtracking
- **Generate Parentheses**: Valid parentheses generation
- **Word Search**: 2D grid DFS
- **N-Queens**: Constraint satisfaction

### 🌳 Tree/BST (Q97-Q116)
- **Tree Traversal**: Pre/In/Post order
- **BST Validation**: Inorder gives sorted array
- **LCA**: Lowest common ancestor
- **Tree Construction**: Preorder + Inorder

### 🌐 Graph/DFS/BFS (Q117-Q125)
- **Number of Islands**: DFS on 2D grid
- **Clone Graph**: DFS with visited set
- **Course Schedule**: Topological sort
- **Word Ladder**: BFS shortest path

### 🔍 Divide & Conquer (Q126-Q129)
- **Merge K Lists**: Divide into pairs
- **Sorted Array to BST**: Recursive construction
- **Sort List**: Merge sort on linked list
- **Quad Tree**: Recursive subdivision

### ⚙️ Matrix/Simulation (Q130-Q134)
- **Valid Sudoku**: Row/column/box validation
- **Spiral Matrix**: Layer by layer traversal
- **Rotate Image**: Transpose + reverse
- **Game of Life**: In-place state update

### 💡 Math/Bit Manipulation (Q135-Q146)
- **Palindrome Number**: Reverse number
- **Pow(x, n)**: Binary exponentiation
- **Single Number**: XOR for duplicates
- **Bit Operations**: AND, OR, XOR patterns

### 🔺 Heap/Priority Queue (Q147-Q150)
- **Kth Largest**: Min heap of size k
- **Median Stream**: Two heaps (min/max)
- **K Pairs**: Min heap for smallest sums
- **IPO**: Greedy with heap

## 🎯 Common Patterns

### Two Pointers
```javascript
let left = 0, right = array.length - 1;
while (left < right) {
  // Process elements
  left++; right--;
}
```

### Sliding Window
```javascript
let left = 0;
for (let right = 0; right < array.length; right++) {
  // Expand window
  while (condition) {
    // Shrink window
    left++;
  }
}
```

### Hash Map
```javascript
const map = new Map();
for (const item of array) {
  if (map.has(item)) {
    // Found duplicate
  }
  map.set(item, value);
}
```

### Binary Search
```javascript
let left = 0, right = array.length - 1;
while (left <= right) {
  const mid = Math.floor((left + right) / 2);
  if (array[mid] === target) return mid;
  if (array[mid] < target) left = mid + 1;
  else right = mid - 1;
}
```

### DFS
```javascript
function dfs(node, visited) {
  if (visited.has(node)) return;
  visited.add(node);
  for (const neighbor of node.neighbors) {
    dfs(neighbor, visited);
  }
}
```

### BFS
```javascript
const queue = [start];
const visited = new Set([start]);
while (queue.length > 0) {
  const node = queue.shift();
  for (const neighbor of node.neighbors) {
    if (!visited.has(neighbor)) {
      visited.add(neighbor);
      queue.push(neighbor);
    }
  }
}
```

## 📊 Time Complexity Cheatsheet

| Algorithm | Time | Space | Notes |
|-----------|------|-------|-------|
| Two Pointers | O(n) | O(1) | Linear scan |
| Sliding Window | O(n) | O(1) | Each element visited twice |
| Hash Map | O(n) | O(n) | Trade space for time |
| Binary Search | O(log n) | O(1) | Divide and conquer |
| DFS/BFS | O(V + E) | O(V) | Graph traversal |
| DP | O(n²) | O(n) | Bottom-up approach |
| Sorting | O(n log n) | O(1) | In-place sorting |

## 🔧 Common Data Structures

### Stack
```javascript
const stack = [];
stack.push(item);    // O(1)
stack.pop();         // O(1)
stack[stack.length - 1]; // O(1)
```

### Queue
```javascript
const queue = [];
queue.push(item);    // O(1)
queue.shift();       // O(n) - use deque for O(1)
```

### Heap
```javascript
// Min heap
const heap = new MinHeap();
heap.insert(item);   // O(log n)
heap.extractMin();   // O(log n)
heap.peek();         // O(1)
```

### Trie
```javascript
class TrieNode {
  constructor() {
    this.children = {};
    this.isEnd = false;
  }
}
```

## 🎯 Interview Tips

1. **Clarify the Problem**: Ask about constraints, edge cases
2. **Think Out Loud**: Explain your approach
3. **Start Simple**: Brute force first, then optimize
4. **Test Edge Cases**: Empty arrays, single elements
5. **Optimize**: Look for better time/space complexity
6. **Code Cleanly**: Use meaningful variable names
7. **Handle Errors**: Check for invalid inputs

## 🚀 Quick Solutions

### Two Sum
```javascript
function twoSum(nums, target) {
  const map = new Map();
  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];
    if (map.has(complement)) return [map.get(complement), i];
    map.set(nums[i], i);
  }
}
```

### Valid Parentheses
```javascript
function isValid(s) {
  const stack = [];
  const pairs = { '(': ')', '[': ']', '{': '}' };
  for (const char of s) {
    if (pairs[char]) stack.push(char);
    else if (stack.length === 0 || pairs[stack.pop()] !== char) return false;
  }
  return stack.length === 0;
}
```

### Merge Two Sorted Lists
```javascript
function mergeTwoLists(l1, l2) {
  const dummy = new ListNode(0);
  let current = dummy;
  while (l1 && l2) {
    if (l1.val <= l2.val) {
      current.next = l1;
      l1 = l1.next;
    } else {
      current.next = l2;
      l2 = l2.next;
    }
    current = current.next;
  }
  current.next = l1 || l2;
  return dummy.next;
}
```

---

*This cheatsheet covers all 150 LeetCode problems with quick reference patterns, time complexities, and common interview solutions.*
