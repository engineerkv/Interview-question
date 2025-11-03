# Bonus: Important Concepts

## Sliding Window

Concept: Maintain a moving subarray/substring satisfying a property; grow right, shrink left to restore validity.

```javascript
// Longest substring with at most k distinct characters
function lenAtMostK(s, k) {
  const freq = new Map();
  let left = 0;
  let best = 0;

  for (let right = 0; right < s.length; right++) {
    const char = s[right];
    freq.set(char, (freq.get(char) || 0) + 1);

    while (freq.size > k) {
      const drop = s[left++];
      const next = freq.get(drop) - 1;
      if (next === 0) {
        freq.delete(drop);
      } else {
        freq.set(drop, next);
      }
    }

    best = Math.max(best, right - left + 1);
  }
  return best;
}

// Test Cases:
// Input: s = "eceba", k = 2
// Output: 3
// Explanation: Longest substring with at most 2 distinct characters is "ece" with length 3

// Input: s = "aa", k = 1
// Output: 2
// Explanation: Longest substring with at most 1 distinct character is "aa" with length 2

// Input: s = "abcabcbb", k = 3
// Output: 6
// Explanation: Longest substring with at most 3 distinct characters is "abcabc" with length 6

// Input: s = "abacaba", k = 2
// Output: 4
```

**Time Complexity:** O(n) - Single pass with sliding window  
**Space Complexity:** O(k) -Hash map stores up to k distinct characters

Deep Insights:
  - Rule: Maintain a moving subarray/substring satisfying a property; grow right, shrink left to restore validity; O(n) time.
  - Real-world: Sliding window problems, substring problems, subarray problems, window-based algorithms.
  - Common mistake: For fixed-size windows, no inner while; maps/arrays store window state; not shrinking left correctly.
  - Optimization: O(n) time optimal; for fixed-size windows, no inner while; maps/arrays store window state.
  - Interview tip: Explain sliding window clearly; mention fixed vs variable size; ask about state tracking.
## Two Pointer

Concept: Use two indices to traverse from ends or sweep with relative motion to meet constraints.

```javascript
// Two-sum on a sorted array
function twoSumSorted(arr, target) {
  let left = 0;
  let right = arr.length - 1;

  while (left < right) {
    const sum = arr[left] + arr[right];
    if (sum === target) {
      return [left, right];
    }
    if (sum < target) {
      left++;
    } else {
      right--;
    }
  }
  return [-1, -1];
}

// Test Cases:
// Input: arr = [2, 7, 11, 15], target = 9
// Output: [0, 1]

// Input: arr = [2, 3, 4], target = 6
// Output: [0, 2]

// Input: arr = [-1, 0], target = -1
// Output: [0, 1]

// Input: arr = [1, 2, 3, 4], target = 10
// Output: [-1, -1]

// Input: arr = [1], target = 2
// Output: [-1, -1]
```

**Time Complexity:** O(n) -Two pointers traverse from both ends  
**Space Complexity:** O(1) - Only using constant extra variables

Deep Insights:
  - Rule: Use two indices to traverse from ends or sweep with relative motion to meet constraints; O(n) time.
  - Real-world: Two pointer problems, sorted array problems, collision detection, meeting problems.
  - Common mistake: Generalize to 3Sum with inner two-pointer; wrong pointer movement; not handling sorted array.
  - Optimization: O(n) time optimal; two pointers from ends; generalize to 3Sum with inner two-pointer.
  - Interview tip: Explain two-pointer technique clearly; mention sorted array requirement; ask about generalizations.
## Prefix Sum

Concept: Transform range queries to differences of cumulative sums; extend to 2D and counts maps.

```javascript
// Count subarrays with sum equal to k
function subarraySum(nums, k) {
  const count = new Map([[0, 1]]);
  let sum = 0;
  let ans = 0;

  for (const x of nums) {
    sum += x;
    ans += count.get(sum - k) || 0;
    count.set(sum, (count.get(sum) || 0) + 1);
  }
  return ans;
}

// Test Cases:
// Input: nums = [1, 1, 1], k = 2
// Output: 2
// Explanation: Subarrays [1,1] and [1,1] (overlapping) sum to 2

// Input: nums = [1, 2, 3], k = 3
// Output: 2
// Explanation: Subarrays [1,2] and [3] sum to 3

// Input: nums = [1, -1, 0], k = 0
// Output: 3
// Explanation: Subarrays [1,-1], [-1,0], and [0] sum to 0

// Input: nums = [1, 1, 1], k = 0
// Output: 0

// Input: nums = [1], k = 1
// Output: 1
```

**Time Complexity:** O(n) - Single pass through array  
**Space Complexity:** O(n) -Hash map stores prefix sum counts

Deep Insights:
  - Rule: Transform range queries to differences of cumulative sums; extend to 2D and counts maps; O(n) time.
  - Real-world: Prefix sum problems, range queries, subarray sum problems, cumulative problems.
  - Common mistake: 2D prefix for matrix ranges; works with XOR (replace + with ^); wrong prefix calculation.
  - Optimization: O(n) time for preprocessing; O(1) for range queries; 2D prefix for matrix ranges; works with XOR.
  - Interview tip: Explain prefix sum clearly; mention 2D extension; ask about XOR variants.
## Bit Manipulation

Concept: Use bitwise ops to encode sets, parity, and arithmetic tricks efficiently.

```javascript
// Single number where every other element appears twice
function singleNumber(arr) {
  let x = 0;
  for (const v of arr) {
    x ^= v;
  }
  return x;
}

// Test Cases:
// Input: arr = [2, 2, 1]
// Output: 1

// Input: arr = [4, 1, 2, 1, 2]
// Output: 4

// Input: arr = [1]
// Output: 1

// Input: arr = [1, 3, 1, 3, 5]
// Output: 5

// Input: arr = [-1, -2, -1, -2, 3]
// Output: 3
```

**Time Complexity:** O(n) -Single pass through array  
**Space Complexity:** O(1) - Only using constant extra variables

Deep Insights:
  - Rule: Use bitwise ops to encode sets, parity, and arithmetic tricks efficiently; O(1) operations typically.
  - Real-world: Bit manipulation problems, set operations, parity checks, arithmetic optimizations.
  - Common mistake: Check bit: (x >> i) & 1; set/clear: x |= 1 << i, x &= ~(1 << i); lowbit: x & -x (Fenwick/BIT); use masks for subsets DP.
  - Optimization: O(1) bit operations; lowbit: x & -x (Fenwick/BIT); use masks for subsets DP.
  - Interview tip: Explain bit operations clearly; mention common tricks; ask about set encoding.## Trie (Autocomplete / Word Dictionary)

Concept: Prefix tree storing characters per edge; supports insert, search, prefix search in O(L).

```javascript
class Trie {
  constructor() {
    this.root = {};
  }

  insert(word) {
    let node = this.root;
    for (const ch of word) {
      node[ch] = node[ch] || {};
      node = node[ch];
    }
    node.$ = true; // end marker
  }

  search(word) {
    let node = this.root;
    for (const ch of word) {
      if (!node[ch]) return false;
      node = node[ch];
    }
    return !!node.$;
  }

  startsWith(prefix) {
    let node = this.root;
    for (const ch of prefix) {
      if (!node[ch]) return false;
      node = node[ch];
    }
    return true;
  }
}

// Test Cases:
// Input:
// let trie = new Trie();
// trie.insert("apple");
// trie.search("apple");   // Output: true
// trie.search("app");     // Output: false
// trie.startsWith("app"); // Output: true
// trie.insert("app");
// trie.search("app");     // Output: true

// Input:
// let trie = new Trie();
// trie.insert("hello");
// trie.insert("world");
// trie.search("hell");     // Output: false
// trie.startsWith("hell"); // Output: true
// trie.search("hello");    // Output: true

// Input:
// let trie = new Trie();
// trie.insert("a");
// trie.search("a");        // Output: true
// trie.startsWith("a");    // Output: true

**Time Complexity:** O(L) -Each operation processes word length L  
**Space Complexity:** O(AL) - Storage for all words where A is alphabet size

Deep Insights:
  - Rule: Prefix tree storing characters per edge; supports insert, search, prefix search in O(L); O(AL) space.
  - Real-world: Trie problems, autocomplete, word dictionary, prefix matching, string search.
  - Common mistake: Wildcards require backtracking; not handling end markers correctly; wrong node traversal.
  - Optimization: O(L) time for each operation; O(AL) space; wildcards require backtracking.
  - Interview tip: Explain trie structure clearly; mention prefix search; ask about wildcard matching.

## Divide & Conquer

### Construct Quad Tree

Concept:
Build quad tree from 2D grid; recursively divide grid into 4 quadrants if values differ.

Example:
```javascript
function construct(grid) {
  function build(rowStart, rowEnd, colStart, colEnd) {
    if (rowStart === rowEnd) {
      return new Node(grid[rowStart][colStart] === 1, true);
    }
    
    const rowMid = Math.floor((rowStart + rowEnd) / 2);
    const colMid = Math.floor((colStart + colEnd) / 2);
    
    const topLeft = build(rowStart, rowMid, colStart, colMid);
    const topRight = build(rowStart, rowMid, colMid + 1, colEnd);
    const bottomLeft = build(rowMid + 1, rowEnd, colStart, colMid);
    const bottomRight = build(rowMid + 1, rowEnd, colMid + 1, colEnd);
    
    // If all children are leaves with same value, merge
    if (topLeft.isLeaf && topRight.isLeaf && 
        bottomLeft.isLeaf && bottomRight.isLeaf &&
        topLeft.val === topRight.val &&
        topRight.val === bottomLeft.val &&
        bottomLeft.val === bottomRight.val) {
      return new Node(topLeft.val, true);
    }
    
    return new Node(false, false, topLeft, topRight, bottomLeft, bottomRight);
  }
  
  return build(0, grid.length - 1, 0, grid[0].length - 1);
}

// Test Cases:
//
// Example 1:
//   Input: grid = [[0,1],[1,0]]
//   Output: Quad tree with root and 4 children
//   Explanation: Root with 4 children (topLeft: 0, topRight: 1, bottomLeft: 1, bottomRight: 0)
//
// Example 2:
//   Input: grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
//   Output: Quad tree with merged nodes
//   Explanation: Regions with same values are merged into single nodes
```

**Time Complexity:** O(n²) - Visit each cell, but merge reduces nodes  
**Space Complexity:** O(log n) - Recursion depth

Deep Insights:
  - Rule: Divide and conquer: split grid into 4 quadrants; merge if all children are same; O(n²) time.
  - Real-world: Image compression, spatial data structures, region representation, hierarchical data.
  - Common mistake: Wrong quadrant boundaries; not checking merge condition correctly; incorrect recursion base case.
  - Optimization: Merge nodes with identical children reduces tree size; O(n²) time, O(log n) space.
  - Interview tip: Explain divide and conquer approach; mention merging optimization; ask about quad tree applications.