# Binary Search Tree

---

## 📍 Navigation

<div align="center">

[← Previous: Binary Trees](05%29%20Binary%20Trees.md) • [Home: README](README.md) • [Next: Heaps & Priority Queue →](07%29%20Heaps%20%26%20Priority%20Queue.md)

[📋 Cheatsheet](DSA%20Interview%20Cheatsheet.md)

</div>

---

## Q114. 🔎 Search, Insert, and Delete in BST

**Problem:** Implement the fundamental BST operations: search for a value, insert a new value, and delete a value from a Binary Search Tree while maintaining the BST property (left < node < right).

**Approach:**

- **Search:** Compare value with root, go left if smaller, right if larger

- **Insert:** Recursively find insertion point and create new node

- **Delete:** Handle three cases: 0 children, 1 child, 2 children (replace with successor)

### Solution 1: Search BST

```javascript
function searchBST(root, val) {
  while (root) {
    if (val === root.val) return root;
    root = val < root.val ? root.left : root.right;
  }
  return null;
}

```

**Time Complexity:** O(h) - h is tree height
**Space Complexity:** O(1) - Iterative approach

### Solution 2: Insert into BST

```javascript
function insertIntoBST(root, val) {
  if (!root) return new TreeNode(val);

  if (val < root.val) {
    root.left = insertIntoBST(root.left, val);
  } else {
    root.right = insertIntoBST(root.right, val);
  }

  return root;
}

```

**Time Complexity:** O(h) - h is tree height
**Space Complexity:** O(h) - Recursion stack

### Solution 3: Delete from BST

```javascript
function deleteNode(root, key) {
  if (!root) return null;

  if (key < root.val) {
    root.left = deleteNode(root.left, key);
  } else if (key > root.val) {
    root.right = deleteNode(root.right, key);
  } else {
    // Node to delete found
    // Case 1: No left child
    if (!root.left) return root.right;
    // Case 2: No right child
    if (!root.right) return root.left;
    // Case 3: Two children - find inorder successor
    let successor = root.right;
    while (successor.left) {
      successor = successor.left;
    }
    // Replace value with successor
    root.val = successor.val;
    // Delete successor
    root.right = deleteNode(root.right, successor.val);
  }

  return root;
}

```

**Time Complexity:** O(h) - h is tree height
**Space Complexity:** O(h) - Recursion stack

// Test Cases:
//
// searchBST:
// Input: root = [4, 2, 7, 1, 3], val = 2
// Output: node with value 2

// Input: root = [4, 2, 7, 1, 3], val = 5
// Output: null
//
// insertIntoBST:
// Input: root = [4, 2, 7, 1, 3], val = 5
// Output: [4, 2, 7, 1, 3, null, null, null, null, null, 5]
//
// deleteNode:
// Input: root = [5, 3, 6, 2, 4, null, 7], key = 3
// Output: [5, 4, 6, 2, null, null, 7] or [5, 2, 6, null, 4, null, 7]

```

## Q115. 🌳 Validate Binary Search Tree

**Problem:** Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than the node's key.

- The right subtree of a node contains only nodes with keys greater than the node's key.

- Both the left and right subtrees must also be binary search trees.

**Approach:** Propagate (min, max) bounds downward. Each node must be within bounds. Update bounds for children.

### Solution 1: Bounds Propagation (Optimal)

```javascript
function isValidBST(root) {
  function validate(node, min, max) {
    if (!node) return true;

    // Check if current node violates bounds
    if (node.val <= min || node.val >= max) return false;

    // Validate left and right subtrees with updated bounds
    return validate(node.left, min, node.val) &&
           validate(node.right, node.val, max);
  }

  return validate(root, -Infinity, Infinity);
}

// Test Cases:
// Input: root = [2, 1, 3]
// Output: true

// Input: root = [5, 1, 4, null, null, 3, 6]
// Output: false

// Input: root = [2, 2, 2]
// Output: false

// Input: root = []
// Output: true

```

**Time Complexity:** O(n) - Visit each node once
**Space Complexity:** O(h) - Recursion stack depth, h is tree height

## Q116. 🌳 Lowest Common Ancestor of a Binary Search Tree

**Problem:** Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST. The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself).

**Approach:** Use BST property. If both values are less than root, go left. If both are greater, go right. Otherwise, root is LCA.

### Solution 1: Iterative with BST Property (Optimal)

```javascript
function lowestCommonAncestor(root, p, q) {
  const pVal = p.val;
  const qVal = q.val;

  while (root) {
    // Both values less than root - LCA in left subtree
    if (pVal < root.val && qVal < root.val) {
      root = root.left;
    }
    // Both values greater than root - LCA in right subtree
    else if (pVal > root.val && qVal > root.val) {
      root = root.right;
    }
    // Values split around root - root is LCA
    else {
      return root;
    }
  }

  return null;
}

// Test Cases:
// Input: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 8
// Output: 6

// Input: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 4
// Output: 2

// Input: root = [2, 1], p = 2, q = 1
// Output: 2

// Input: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 0, q = 5
// Output: 2

```

**Time Complexity:** O(h) - h is tree height
**Space Complexity:** O(1) - Iterative approach

## Q117. 💡 Kth Smallest Element in a BST

**Problem:** Given the root of a binary search tree, and an integer `k`, return the `k`th smallest value (1-indexed) of all the values of the nodes in the tree.

**Approach:** Inorder traversal yields sorted order. Use iterative inorder to find kth element.

### Solution 1: Iterative Inorder (Optimal)

```javascript
function kthSmallest(root, k) {
  const stack = [];
  let current = root;

  while (current || stack.length) {
    // Go left until null
    while (current) {
      stack.push(current);
      current = current.left;
    }

    // Process node
    current = stack.pop();
    if (--k === 0) {
      return current.val;
    }

    // Go right
    current = current.right;
  }
}

// Test Cases:
// Input: root = [3, 1, 4, null, 2], k = 1
// Output: 1

// Input: root = [5, 3, 6, 2, 4, null, null, 1], k = 3
// Output: 3

// Input: root = [1], k = 1
// Output: 1

// Input: root = [5, 3, 6, 2, 4, null, null, 1], k = 4
// Output: 4

```

**Time Complexity:** O(h + k) - h for reaching leftmost, k for processing k nodes
**Space Complexity:** O(h) - Stack stores nodes along path

## Q118. 🌳 Binary Search Tree Iterator

**Problem:** Implement the `BSTIterator` class that represents an iterator over the in-order traversal of a binary search tree (BST):

- `BSTIterator(TreeNode root)` Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor.

- `int next()` Moves the pointer to the right, then returns the smallest number.

- `boolean hasNext()` Returns `true` if there exists a next smallest number, or `false` otherwise.

**Approach:** Use controlled inorder traversal with stack. Maintain stack to track next smallest element.

### Solution 1: Stack-Based Iterator (Optimal)

```javascript
class BSTIterator {
  constructor(root) {
    this.stack = [];
    this.pushLeft(root);
  }

  pushLeft(node) {
    while (node) {
      this.stack.push(node);
      node = node.left;
    }
  }

  next() {
    const node = this.stack.pop();
    // Push left subtree of right child
    if (node.right) {
      this.pushLeft(node.right);
    }
    return node.val;
  }

  hasNext() {
    return this.stack.length > 0;
  }
}

// Test Cases:
// Input:
// let iterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
// iterator.next();    // Output: 3
// iterator.next();    // Output: 7
// iterator.hasNext(); // Output: true
// iterator.next();    // Output: 9
// iterator.hasNext(); // Output: true
// iterator.next();    // Output: 15
// iterator.hasNext(); // Output: true
// iterator.next();    // Output: 20
// iterator.hasNext(); // Output: false

```

**Time Complexity:** O(1) amortized - Each node pushed/popped once
**Space Complexity:** O(h) - Stack stores nodes along path, h is tree height

## Q119. 🌳 Recover Binary Search Tree

**Problem:** You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

**Approach:** Two nodes are swapped. Inorder traversal should be sorted. Find inversions (where prev.val > current.val) and swap values back.

### Solution 1: Inorder Inversion Detection (Optimal)

```javascript
function recoverTree(root) {
  let prev = null;
  let first = null;  // First swapped node
  let second = null; // Second swapped node

  function inorder(node) {
    if (!node) return;

    inorder(node.left);

    // Detect inversion: prev > current
    if (prev && prev.val > node.val) {
      if (!first) {
        first = prev;  // First inversion: prev is first swapped node
      }
      second = node;   // Second inversion: current is second swapped node
    }

    prev = node;
    inorder(node.right);
  }

  inorder(root);

  // Swap values
  const temp = first.val;
  first.val = second.val;
  second.val = temp;
}

// Test Cases:
// Input: root = [1, 3, null, null, 2] (3 and 2 are swapped)
// Output: [3, 1, null, null, 2] (recovered - values swapped back)

// Input: root = [3, 1, 4, null, null, 2] (2 and 3 are swapped)
// Output: [2, 1, 4, null, null, 3] (recovered)

// Input: root = [2, 3, 1] (1 and 3 are swapped)
// Output: [2, 1, 3] (recovered)

```

**Time Complexity:** O(n) - Visit each node once
**Space Complexity:** O(h) - Recursion stack depth, h is tree height

## Q120. 💡 Floor and Ceil in BST

**Problem:** Find the floor (greatest value <= x) and ceil (smallest value >= x) of a given value `x` in a Binary Search Tree.

**Approach:** Traverse BST while updating candidate. Floor: track greatest value <= x. Ceil: track smallest value >= x.

### Solution 1: Floor in BST

```javascript
function floorBST(root, x) {
  let floor = null;

  while (root) {
    if (root.val === x) {
      return root.val;  // Exact match
    }

    if (root.val < x) {
      // Current value is candidate, search right for better candidate
      floor = root.val;
      root = root.right;
    } else {
      // Current value too large, search left
      root = root.left;
    }
  }

  return floor;
}

```

### Solution 2: Ceil in BST

```javascript
function ceilBST(root, x) {
  let ceil = null;

  while (root) {
    if (root.val === x) {
      return root.val;  // Exact match
    }

    if (root.val > x) {
      // Current value is candidate, search left for better candidate
      ceil = root.val;
      root = root.left;
    } else {
      // Current value too small, search right
      root = root.right;
    }
  }

  return ceil;
}

// Test Cases:
//
// floorBST:
// Input: root = [8, 4, 12, 2, 6, 10, 14], x = 5
// Output: 4 (greatest value <= 5)

// Input: root = [8, 4, 12, 2, 6, 10, 14], x = 4
// Output: 4 (exact match)
//
// ceilBST:
// Input: root = [8, 4, 12, 2, 6, 10, 14], x = 5
// Output: 6 (smallest value >= 5)

// Input: root = [8, 4, 12, 2, 6, 10, 14], x = 15
// Output: null (no value >= 15)

```

**Time Complexity:** O(h) - h is tree height
**Space Complexity:** O(1) - Iterative approach

## Q121. ➕ Range Sum of BST

**Problem:** Given the root node of a binary search tree and two integers `low` and `high`, return the sum of values of all nodes with a value in the inclusive range `[low, high]`.

**Approach:** Prune branches using bounds [low, high]. Only traverse subtrees that can contain values in range.

### Solution 1: Pruned DFS (Optimal)

```javascript
function rangeSumBST(root, low, high) {
  if (!root) return 0;

  let sum = 0;

  // If current value > low, left subtree might have values in range
  if (root.val > low) {
    sum += rangeSumBST(root.left, low, high);
  }

  // If current value is in range, add it
  if (root.val >= low && root.val <= high) {
    sum += root.val;
  }

  // If current value < high, right subtree might have values in range
  if (root.val < high) {
    sum += rangeSumBST(root.right, low, high);
  }

  return sum;
}

// Test Cases:
// Input: root = [10, 5, 15, 3, 7, null, 18], L = 7, R = 15
// Output: 32
// Explanation: Sum of nodes with values in range [7, 15]: 7 + 10 + 15 = 32

// Input: root = [10, 5, 15, 3, 7, 13, 18, 1, null, 6], L = 6, R = 10
// Output: 23
// Explanation: Sum of nodes with values in range [6, 10]: 6 + 7 + 10 = 23

// Input: root = [5, 3, 7], L = 1, R = 10
// Output: 15

// Input: root = [10], L = 5, R = 15
// Output: 10

```

**Time Complexity:** O(n) worst case, O(k) best case where k is nodes in range
**Space Complexity:** O(h) - Recursion stack depth, h is tree height

## Q122. 💡 Predecessor and Successor in BST

**Problem:** Find the predecessor (greatest value < key) and successor (smallest value > key) of a given key in a Binary Search Tree.

**Approach:**

- **Predecessor:** Max in left subtree OR last smaller ancestor when going left

- **Successor:** Min in right subtree OR last greater ancestor when going right

### Solution 1: Predecessor in BST

```javascript
function predecessor(root, key) {
  let pred = null;

  while (root) {
    if (key <= root.val) {
      // Predecessor must be in left subtree
      root = root.left;
    } else {
      // Current node is candidate, search right for better candidate
      pred = root.val;
      root = root.right;
    }
  }

  return pred;
}

```

### Solution 2: Successor in BST

```javascript
function successor(root, key) {
  let succ = null;

  while (root) {
    if (key >= root.val) {
      // Successor must be in right subtree
      root = root.right;
    } else {
      // Current node is candidate, search left for better candidate
      succ = root.val;
      root = root.left;
    }
  }

  return succ;
}

// Test Cases:
//
// predecessor:
// Input: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], key = 4
// Output: 3 (predecessor of 4 is 3)

// Input: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], key = 5
// Output: 4 (predecessor of 5 is 4)
//
// successor:
// Input: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], key = 4
// Output: 5 (successor of 4 is 5)

// Input: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], key = 5
// Output: 6 (successor of 5 is 6)

```

**Time Complexity:** O(h) - h is tree height
**Space Complexity:** O(1) - Iterative approach

## Q123. 📋 Convert Sorted Array to Binary Search Tree

**Problem:** Given an integer array `nums` where the elements are sorted in ascending order, convert it to a height-balanced binary search tree. A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than 1.

**Approach:** Build balanced BST by picking middle element as root and recursing on left and right halves.

### Solution 1: Divide and Conquer (Optimal)

```javascript
function sortedArrayToBST(nums) {
  function build(left, right) {
    if (left > right) return null;

    // Pick middle element as root
    const mid = Math.floor((left + right) / 2);
    const root = new TreeNode(nums[mid]);

    // Recursively build left and right subtrees
    root.left = build(left, mid - 1);
    root.right = build(mid + 1, right);

    return root;
  }

  return build(0, nums.length - 1);
}

// Test Cases:
// Input: nums = [-10, -3, 0, 5, 9]
// Output: [0, -3, 9, -10, null, 5] or [0, -10, 5, null, -3, null, 9]
// (balanced BST structure, multiple valid outputs)

// Input: nums = [1, 3]
// Output: [3, 1] or [1, null, 3]

// Input: nums = [1]
// Output: [1]

// Input: nums = [-10, -3, 0, 5, 9, 10]
// Output: Balanced BST with root at mid element

```

**Time Complexity:** O(n) - Visit each element once
**Space Complexity:** O(log n) - Recursion stack depth for balanced tree

- **Interview Tip:** Explain divide and conquer clearly; emphasize balanced tree guarantee; mention multiple valid trees

---

## 📍 Navigation

<div align="center">

[← Previous: Binary Trees](05%29%20Binary%20Trees.md) • [Home: README](README.md) • [Next: Heaps & Priority Queue →](07%29%20Heaps%20%26%20Priority%20Queue.md)

[📋 Cheatsheet](DSA%20Interview%20Cheatsheet.md)

</div>
