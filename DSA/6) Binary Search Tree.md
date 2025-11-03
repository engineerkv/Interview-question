# Binary Search Tree

## Q76. Insert/Delete/Search in BST

Concept: BST invariant: left < node < right. Search by comparing; insert by recursion; delete handles 0/1/2 children.

```javascript
function searchBST(root, val) {
  while (root) {
    if (val === root.val) return root;
    root = val < root.val ? root.left : root.right;
  }
  return null;
}

function insertIntoBST(root, val) {
  if (!root) return { val, left: null, right: null };
  if (val < root.val) {
    root.left = insertIntoBST(root.left, val);
  } else {
    root.right = insertIntoBST(root.right, val);
  }
  return root;
}

function deleteNode(root, key) {
  if (!root) return null;
  if (key < root.val) {
    root.left = deleteNode(root.left, key);
  } else if (key > root.val) {
    root.right = deleteNode(root.right, key);
  } else {
    if (!root.left) return root.right;
    if (!root.right) return root.left;
    let s = root.right;
    while (s.left) {
      s = s.left;
    }
    root.val = s.val;
    root.right = deleteNode(root.right, s.val);
  }
  return root;
}

// Test Cases:
//
// searchBST:
// Example 1:
//   Input: root = [4, 2, 7, 1, 3], val = 2
//   Output: node with value 2
//
// Example 2:
//   Input: root = [4, 2, 7, 1, 3], val = 5
//   Output: null
//
// insertIntoBST:
// Example 1:
//   Input: root = [4, 2, 7, 1, 3], val = 5
//   Output: [4, 2, 7, 1, 3, null, null, null, null, null, 5]
//
// deleteNode:
// Example 1:
//   Input: root = [5, 3, 6, 2, 4, null, 7], key = 3
//   Output: [5, 4, 6, 2, null, null, 7] or [5, 2, 6, null, 4, null, 7]
```

Deep Insights:
  - Rule: BST invariant: left < node < right; search by comparing; insert by recursion; delete handles 0/1/2 children.
  - Real-world: BST operations, search trees, sorted data structures, dictionary implementations.
  - Common mistake: Not maintaining BST invariant after ops; duplicate policy must be defined; wrong deletion logic.
  - Optimization: Search O(h) time; insert O(h) time; delete O(h) time with successor finding; maintain BST invariant.
  - Interview tip: Explain BST invariant clearly; mention duplicate handling; ask about balanced vs unbalanced BST.
## Q77. Validate BST

Concept: Node values must lie within (min, max) bounds propagated downwards.

```javascript
function isValidBST(root) {
  function ok(n, lo, hi) {
    if (!n) return true;
    if (!(n.val > lo && n.val < hi)) return false;
    return ok(n.left, lo, n.val) && ok(n.right, n.val, hi);
  }
  return ok(root, -Infinity, Infinity);
}

// Test Cases:
//
// Example 1:
//   Input: root = [2, 1, 3]
//   Output: true
//
// Example 2:
//   Input: root = [5, 1, 4, null, null, 3, 6]
//   Output: false
//
// Example 3:
//   Input: root = [2, 2, 2]
//   Output: false
//
// Example 4:
//   Input: root = []
//   Output: true
```

Deep Insights:
  - Rule: Node values must lie within (min, max) bounds propagated downwards; O(n) time, O(h) space.
  - Real-world: BST validation, tree structure validation, sorted order checking, binary search validation.
  - Common mistake: Duplicates typically invalidate BST; subtree-level constraints matter; wrong bounds propagation.
  - Optimization: O(n) time optimal; early return on invalid; bounds propagation ensures correctness.
  - Interview tip: Explain bounds propagation clearly; mention duplicate handling; ask about inclusive vs exclusive bounds.
## Q78. Lowest Common Ancestor in BST

Concept: Use BST order: if both < node go left; if both > node go right; else node is LCA.

```javascript
function lowestCommonAncestor(root, p, q) {
  let a = p.val;
  let b = q.val;
  while (root) {
    if (a < root.val && b < root.val) {
      root = root.left;
    } else if (a > root.val && b > root.val) {
      root = root.right;
    } else {
      return root;
    }
  }
  return null;
}

// Test Cases:
//
// Example 1:
//   Input: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 8
//   Output: 6
//
// Example 2:
//   Input: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 4
//   Output: 2
//
// Example 3:
//   Input: root = [2, 1], p = 2, q = 1
//   Output: 2
//
// Example 4:
//   Input: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 0, q = 5
//   Output: 2
```

Deep Insights:
  - Rule: Use BST order: if both < node go left; if both > node go right; else node is LCA; O(h) time.
  - Real-world: BST LCA queries, tree navigation, hierarchical search, common ancestor problems.
  - Common mistake: Handles when one node is ancestor of the other; requires both nodes exist in tree; wrong order comparison.
  - Optimization: O(h) time optimal; simpler than general binary tree LCA; uses BST property.
  - Interview tip: Explain BST property usage clearly; mention it's simpler than binary tree LCA; ask about node existence.
## Q79. Kth Smallest in BST

Concept: Inorder traversal yields sorted order; pick kth (1-indexed).

```javascript
function kthSmallest(root, k) {
  const st = [];
  let cur = root;
  while (cur || st.length) {
    while (cur) {
      st.push(cur);
      cur = cur.left;
    }
    cur = st.pop();
    if (--k === 0) {
      return cur.val;
    }
    cur = cur.right;
  }
}

// Test Cases:
//
// Example 1:
//   Input: root = [3, 1, 4, null, 2], k = 1
//   Output: 1
//
// Example 2:
//   Input: root = [5, 3, 6, 2, 4, null, null, 1], k = 3
//   Output: 3
//
// Example 3:
//   Input: root = [1], k = 1
//   Output: 1
//
// Example 4:
//   Input: root = [5, 3, 6, 2, 4, null, null, 1], k = 4
//   Output: 4
```

Deep Insights:
  - Rule: Inorder traversal yields sorted order; pick kth (1-indexed); O(h + k) time, O(h) space.
  - Real-world: Kth smallest queries, sorted order selection, rank queries, ordered statistics.
  - Common mistake: Keep k decremented on visit; 1-indexed vs 0-indexed confusion; wrong traversal order.
  - Optimization: Iterative inorder with stack; O(h + k) time; can optimize with Morris traversal.
  - Interview tip: Explain inorder clearly; mention 1-indexed convention; ask about kth largest variant.
## Q80. BST Iterator

Concept: Controlled inorder traversal using a stack; next returns next smallest.

```javascript
class BSTIterator {
  constructor(root) {
    this.st = [];
    this.pushLeft(root);
  }

  pushLeft(n) {
    while (n) {
      this.st.push(n);
      n = n.left;
    }
  }

  next() {
    const n = this.st.pop();
    if (n.right) {
      this.pushLeft(n.right);
    }
    return n.val;
  }

  hasNext() {
    return this.st.length > 0;
  }
}

// Test Cases:
//
// Example 1:
//   Input:
//     let iterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
//     iterator.next();    // Output: 3
//     iterator.next();    // Output: 7
//     iterator.hasNext(); // Output: true
//     iterator.next();    // Output: 9
//     iterator.hasNext(); // Output: true
//     iterator.next();    // Output: 15
//     iterator.hasNext(); // Output: true
//     iterator.next();    // Output: 20
//     iterator.hasNext(); // Output: false
```

Deep Insights:
  - Rule: Controlled inorder traversal using a stack; next returns next smallest; O(1) amortized next, O(h) space.
  - Real-world: BST iteration, controlled traversal, iterator pattern, sequential access to sorted data.
  - Common mistake: Not handling empty stack; pushLeft logic incorrect; works for dynamic traversal; values returned in ascending order.
  - Optimization: Amortized O(1) next operation; O(h) space for stack; efficient for multiple queries.
  - Interview tip: Explain pushLeft clearly; mention amortized complexity; ask about hasNext implementation.
## Q81. Recover BST

Concept: Two nodes swapped; inorder should be sorted—find inversions and swap back.

```javascript
function recoverTree(root) {
  let prev = null;
  let a = null;
  let b = null;

  function dfs(n) {
    if (!n) return;
    dfs(n.left);
    if (prev && prev.val > n.val) {
      if (!a) {
        a = prev;
      }
      b = n;
    }
    prev = n;
    dfs(n.right);
  }

  dfs(root);
  const t = a.val;
  a.val = b.val;
  b.val = t;
}

// Test Cases:
//
// Example 1:
//   Input: root = [1, 3, null, null, 2] (3 and 2 are swapped)
//   Output: [3, 1, null, null, 2] (recovered - values swapped back)
//
// Example 2:
//   Input: root = [3, 1, 4, null, null, 2] (2 and 3 are swapped)
//   Output: [2, 1, 4, null, null, 3] (recovered)
//
// Example 3:
//   Input: root = [2, 3, 1] (1 and 3 are swapped)
//   Output: [2, 1, 3] (recovered)
```

Deep Insights:
  - Rule: Two nodes swapped; inorder should be sorted—find inversions and swap back; O(n) time, O(h) space.
  - Real-world: BST recovery, tree corruption fixing, sorted order restoration, tree validation and repair.
  - Common mistake: Not finding both swapped nodes correctly; do not change structure, only values; wrong inversion detection.
  - Optimization: Inorder traversal finds inversions; swap values only; O(n) time optimal.
  - Interview tip: Explain inversion detection clearly; mention structure preservation; ask about multiple swaps.
## Q82. Floor and Ceil in BST

Concept: Floor is greatest <= x; Ceil is smallest >= x. Walk BST updating candidate.

```javascript
function floorBST(root, x) {
  let ans = null;
  while (root) {
    if (root.val === x) {
      return root.val;
    }
    if (root.val < x) {
      ans = root.val;
      root = root.right;
    } else {
      root = root.left;
    }
  }
  return ans;
}

function ceilBST(root, x) {
  let ans = null;
  while (root) {
    if (root.val === x) {
      return root.val;
    }
    if (root.val > x) {
      ans = root.val;
      root = root.left;
    } else {
      root = root.right;
    }
  }
  return ans;
}

// Test Cases:
//
// floorBST:
// Example 1:
//   Input: root = [8, 4, 12, 2, 6, 10, 14], x = 5
//   Output: 4 (greatest value <= 5)
//
// Example 2:
//   Input: root = [8, 4, 12, 2, 6, 10, 14], x = 4
//   Output: 4 (exact match)
//
// ceilBST:
// Example 1:
//   Input: root = [8, 4, 12, 2, 6, 10, 14], x = 5
//   Output: 6 (smallest value >= 5)
//
// Example 2:
//   Input: root = [8, 4, 12, 2, 6, 10, 14], x = 15
//   Output: null (no value >= 15)
```

Deep Insights:
  - Rule: Floor is greatest <= x; Ceil is smallest >= x; walk BST updating candidate; O(h) time.
  - Real-world: Range queries, nearest value search, boundary queries, value approximation.
  - Common mistake: Candidates updated along the path; works with duplicates if policy defined; wrong comparison logic.
  - Optimization: O(h) time optimal; candidates updated during traversal; handles exact matches.
  - Interview tip: Explain floor vs ceil clearly; mention duplicate handling; ask about exact match behavior.
## Q83. Range Sum in BST

Concept: Prune branches using bounds [L,R]; sum only nodes within range.

```javascript
function rangeSumBST(root, L, R) {
  if (!root) return 0;
  let sum = 0;
  if (root.val > L) {
    sum += rangeSumBST(root.left, L, R);
  }
  if (root.val >= L && root.val <= R) {
    sum += root.val;
  }
  if (root.val < R) {
    sum += rangeSumBST(root.right, L, R);
  }
  return sum;
}

// Test Cases:
//
// Example 1:
//   Input: root = [10, 5, 15, 3, 7, null, 18], L = 7, R = 15
//   Output: 32
//   Explanation: Sum of nodes with values in range [7, 15]: 7 + 10 + 15 = 32
//
// Example 2:
//   Input: root = [10, 5, 15, 3, 7, 13, 18, 1, null, 6], L = 6, R = 10
//   Output: 23
//   Explanation: Sum of nodes with values in range [6, 10]: 6 + 7 + 10 = 23
//
// Example 3:
//   Input: root = [5, 3, 7], L = 1, R = 10
//   Output: 15
//
// Example 4:
//   Input: root = [10], L = 5, R = 15
//   Output: 10
```

Deep Insights:
  - Rule: Prune branches using bounds [L,R]; sum only nodes within range; O(n) time worst, O(k) best.
  - Real-world: Range sum queries, range aggregation, filtered tree traversal, range statistics.
  - Common mistake: Not pruning correctly; wrong bounds checking; iterative stack works too; missing nodes in range.
  - Optimization: Pruning reduces complexity; O(k) time where k is nodes in range; O(h) space.
  - Interview tip: Explain pruning clearly; mention iterative variant; ask about range size impact.
## Q84. Predecessor & Successor

Concept: In BST, predecessor is max in left subtree or last smaller ancestor; successor is min in right or last greater ancestor.

```javascript
function predecessor(root, key) {
  let ans = null;
  while (root) {
    if (key <= root.val) {
      root = root.left;
    } else {
      ans = root.val;
      root = root.right;
    }
  }
  return ans;
}

function successor(root, key) {
  let ans = null;
  while (root) {
    if (key >= root.val) {
      root = root.right;
    } else {
      ans = root.val;
      root = root.left;
    }
  }
  return ans;
}

// Test Cases:
//
// predecessor:
// Example 1:
//   Input: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], key = 4
//   Output: 3 (predecessor of 4 is 3)
//
// Example 2:
//   Input: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], key = 5
//   Output: 4 (predecessor of 5 is 4)
//
// successor:
// Example 1:
//   Input: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], key = 4
//   Output: 5 (successor of 4 is 5)
//
// Example 2:
//   Input: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], key = 5
//   Output: 6 (successor of 5 is 6)
```

Deep Insights:
  - Rule: Predecessor is max in left subtree or last smaller ancestor; successor is min in right or last greater ancestor.
  - Real-world: Predecessor/successor queries, ordered operations, sorted sequence navigation, tree navigation.
  - Common mistake: Requires handling when none exists; node reference variants exist; wrong ancestor tracking.
  - Optimization: O(h) time optimal; handles cases where subtree is empty; efficient for multiple queries.
  - Interview tip: Explain predecessor vs successor clearly; mention null handling; ask about node reference variant.
## Q85. Convert Sorted Array to BST

Concept: Build balanced BST by picking mid as root and recursing on halves.

```javascript
function sortedArrayToBST(nums) {
  function build(l, r) {
    if (l > r) return null;
    const m = (l + r) >> 1;
    const n = { val: nums[m], left: null, right: null };
    n.left = build(l, m - 1);
    n.right = build(m + 1, r);
    return n;
  }
  return build(0, nums.length - 1);
}

// Test Cases:
//
// Example 1:
//   Input: nums = [-10, -3, 0, 5, 9]
//   Output: [0, -3, 9, -10, null, 5] or [0, -10, 5, null, -3, null, 9]
//   (balanced BST structure, multiple valid outputs)
//
// Example 2:
//   Input: nums = [1, 3]
//   Output: [3, 1] or [1, null, 3]
//
// Example 3:
//   Input: nums = [1]
//   Output: [1]
//
// Example 4:
//   Input: nums = [-10, -3, 0, 5, 9, 10]
//   Output: Balanced BST with root at mid element
```

Deep Insights:
  - Rule: Build balanced BST by picking mid as root and recursing on halves; O(n) time, O(log n) space.
  - Real-world: Balanced BST construction, sorted array to tree, balanced tree building, height optimization.
  - Common mistake: Wrong mid calculation; not handling empty array; works with duplicates but balance may vary.
  - Optimization: O(n) time optimal; balanced tree ensures O(log n) height; O(log n) recursion stack.
  - Interview tip: Explain mid selection clearly; mention balance guarantee; ask about duplicate handling.