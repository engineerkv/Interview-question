# Binary Trees

## Q56. Binary Tree Traversals (DFS/BFS)

Concept: Visit nodes in specific orders: DFS (pre/in/post) or BFS (level-order). Choose based on problem needs.

```javascript
// Preorder: root, left, right
function preorder(root) {
  const res = [];
  function dfs(n) {
    if (!n) return;
    res.push(n.val);
    dfs(n.left);
    dfs(n.right);
  }
  dfs(root);
  return res;
}

// Inorder: left, root, right (sorted for BST)
function inorder(root) {
  const res = [];
  function dfs(n) {
    if (!n) return;
    dfs(n.left);
    res.push(n.val);
    dfs(n.right);
  }
  dfs(root);
  return res;
}

// Postorder: left, right, root
function postorder(root) {
  const res = [];
  function dfs(n) {
    if (!n) return;
    dfs(n.left);
    dfs(n.right);
    res.push(n.val);
  }
  dfs(root);
  return res;
}

// Non-recursive (Iterative) Versions:

// Preorder: root, left, right (iterative)
function preorderIter(root) {
  if (!root) return [];
  const res = [];
  const stack = [root];
  while (stack.length) {
    const node = stack.pop();
    res.push(node.val);
    if (node.right) stack.push(node.right);
    if (node.left) stack.push(node.left);
  }
  return res;
}

// Inorder: left, root, right (iterative)
function inorderIter(root) {
  const res = [];
  const stack = [];
  let cur = root;
  while (cur || stack.length) {
    while (cur) {
      stack.push(cur);
      cur = cur.left;
    }
    cur = stack.pop();
    res.push(cur.val);
    cur = cur.right;
  }
  return res;
}

// Postorder: left, right, root (iterative - using two stacks)
function postorderIter(root) {
  if (!root) return [];
  const res = [];
  const stack1 = [root];
  const stack2 = [];
  while (stack1.length) {
    const node = stack1.pop();
    stack2.push(node);
    if (node.left) stack1.push(node.left);
    if (node.right) stack1.push(node.right);
  }
  while (stack2.length) {
    res.push(stack2.pop().val);
  }
  return res;
}

// BFS: level-order with queue
function levelOrder(root) {
  if (!root) return [];
  const res = [];
  const q = [root];
  while (q.length) {
    const level = [];
    const sz = q.length;
    for (let i = 0; i < sz; i++) {
      const n = q.shift();
      level.push(n.val);
      if (n.left) q.push(n.left);
      if (n.right) q.push(n.right);
    }
    res.push(level);
  }
  return res;
}

// Test Cases:
//
// Example 1:
//   Input: root = [1, null, 2, 3]
//   Preorder Output: [1, 2, 3] (recursive and iterative)
//   Inorder Output: [1, 3, 2] (recursive and iterative)
//   Postorder Output: [3, 2, 1] (recursive and iterative)
//   Level Order Output: [[1], [2], [3]]
//
// Example 2:
//   Input: root = [3, 9, 20, null, null, 15, 7]
//   Preorder Output: [3, 9, 20, 15, 7] (recursive and iterative)
//   Inorder Output: [9, 3, 15, 20, 7] (recursive and iterative)
//   Postorder Output: [9, 15, 7, 20, 3] (recursive and iterative)
//   Level Order Output: [[3], [9, 20], [15, 7]]
//
// Example 3:
//   Input: root = [1]
//   All outputs: [1] or [[1]] for level order (same for recursive and iterative)
//
// Example 4:
//   Input: root = []
//   All outputs: [] (same for recursive and iterative)
```

**Time Complexity:** O(n) - Visit each node once  
**Space Complexity:** O(h) for recursive, O(n) worst-case for iterative - h is tree height, n is number of nodes

Deep Insights:
  - Rule: DFS traversals (pre/in/post) have recursive and iterative versions; recursive uses call stack, iterative uses explicit stack; preorder iterative pushes right then left; inorder iterative uses current pointer; postorder iterative uses two stacks; BFS uses queue; O(n) time, O(h) space for recursive, O(n) worst-case for iterative.
  - Real-world: Inorder on BST yields sorted values; preorder useful for copying trees; postorder for deletion; iterative avoids stack overflow in deep trees; both approaches work but iterative preferred for production code.
  - Common mistake: Forgetting null checks; wrong stack order for preorder iterative (push right then left); forgetting to update current pointer in inorder iterative; wrong stack usage in postorder iterative; confusing traversal orders.
  - Optimization: Iterative DFS avoids recursion stack overflow; preorder iterative is straightforward; inorder iterative requires careful pointer management; postorder iterative uses two stacks or reverse preorder; recursive is cleaner but iterative is safer for deep trees; BFS finds shortest paths.
  - Interview tip: Know both recursive and iterative versions; explain when to use iterative (deep trees, production); preorder iterative is easiest; inorder iterative requires understanding current pointer; postorder iterative is trickiest; ask about stack overflow concerns and use cases.
## Q57. Max Depth of Binary Tree

Concept: Height is 1 + max(depth(left), depth(right)); handle null as 0. DFS recursion is simplest.

```javascript
function maxDepth(root) {
  if (!root) return 0;
  return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
}

// Test Cases:
//
// Example 1:
//   Input: root = [3, 9, 20, null, null, 15, 7]
//   Output: 3
//
// Example 2:
//   Input: root = [1, null, 2]
//   Output: 2
//
// Example 3:
//   Input: root = []
//   Output: 0
//
// Example 4:
//   Input: root = [1]
//   Output: 1
```

**Time Complexity:** O(n) - Visit each node once  
**Space Complexity:** O(h) - Recursion stack depth, h is tree height

Deep Insights:
  - Rule: Height is 1 + max(depth(left), depth(right)); handle null as 0; O(n) time, O(h) space.
  - Real-world: Tree height calculation, depth analysis, tree structure validation, hierarchical depth tracking.
  - Common mistake: Not handling null correctly (return 0); forgetting to add 1; tail recursion not guaranteed in JS.
  - Optimization: DFS recursion is simplest; BFS variant counts levels; O(h) space for recursion stack.
  - Interview tip: Explain base case clearly; mention iterative vs recursive; ask about skewed trees.
## Q58. Diameter of Binary Tree

Concept: Longest path through any node = leftHeight + rightHeight. Track global best during post-order.

```javascript
function diameterOfBinaryTree(root) {
  let best = 0;
  function height(n) {
    if (!n) return 0;
    const L = height(n.left);
    const R = height(n.right);
    best = Math.max(best, L + R);
    return 1 + Math.max(L, R);
  }
  height(root);
  return best;
}

// Test Cases:
//
// Example 1:
//   Input: root = [1, 2, 3, 4, 5]
//   Output: 3
//   Explanation: Longest path is [4, 2, 1, 3] or [5, 2, 1, 3] with length 3
//
// Example 2:
//   Input: root = [1, 2]
//   Output: 1
//   Explanation: Longest path is [2, 1] with length 1
//
// Example 3:
//   Input: root = [1]
//   Output: 0
//
// Example 4:
//   Input: root = []
//   Output: 0
```

**Time Complexity:** O(n) - Visit each node once  
**Space Complexity:** O(h) - Recursion stack depth, h is tree height

Deep Insights:
  - Rule: Longest path through any node = leftHeight + rightHeight; track global best during post-order; O(n) time.
  - Real-world: Tree diameter calculation, longest path problems, tree width analysis, path length queries.
  - Common mistake: Confusing with max depth; path length counted in edges; works for empty (0) and single node (0).
  - Optimization: Single traversal O(n); separate from max depth; post-order ensures both heights available.
  - Interview tip: Explain path length vs depth clearly; mention it's different from max depth; ask about edge cases.
## Q59. Balanced Binary Tree

Concept: Height-balanced if each node's subtrees differ by <=1 and subtrees are balanced. Use -1 sentinel to propagate unbalanced.

```javascript
function isBalanced(root) {
  function height(n) {
    if (!n) return 0;
    const L = height(n.left);
    if (L < 0) return -1;
    const R = height(n.right);
    if (R < 0) return -1;
    if (Math.abs(L - R) > 1) return -1;
    return 1 + Math.max(L, R);
  }
  return height(root) >= 0;
}

// Test Cases:
//
// Example 1:
//   Input: root = [3, 9, 20, null, null, 15, 7]
//   Output: true
//
// Example 2:
//   Input: root = [1, 2, 2, 3, 3, null, null, 4, 4]
//   Output: false
//
// Example 3:
//   Input: root = []
//   Output: true
//
// Example 4:
//   Input: root = [1, 2, 2, 3, null, null, 3, 4, null, null, 4]
//   Output: false
```

**Time Complexity:** O(n) - Visit each node once  
**Space Complexity:** O(h) - Recursion stack depth, h is tree height

Deep Insights:
  - Rule: Height-balanced if subtrees differ by <=1 and subtrees are balanced; use -1 sentinel to propagate unbalanced.
  - Real-world: Tree balance validation, AVL tree checking, balanced tree algorithms, structure validation.
  - Common mistake: Early exit on imbalance; edges vs nodes definitions consistent; not handling null correctly.
  - Optimization: O(n) single pass; early exit on imbalance; skewed tree fails quickly.
  - Interview tip: Explain -1 sentinel technique clearly; mention AVL tree context; ask about balance factor.
## Q60. Invert Binary Tree

Concept: Swap left and right recursively or iteratively. Mirror the tree.

```javascript
function invertTree(root) {
  if (!root) return root;
  const tmp = root.left;
  root.left = root.right;
  root.right = tmp;
  invertTree(root.left);
  invertTree(root.right);
  return root;
}

// Test Cases:
//
// Example 1:
//   Input: root = [4, 2, 7, 1, 3, 6, 9]
//   Output: [4, 7, 2, 9, 6, 3, 1]
//
// Example 2:
//   Input: root = [2, 1, 3]
//   Output: [2, 3, 1]
//
// Example 3:
//   Input: root = []
//   Output: []
//
// Example 4:
//   Input: root = [1]
//   Output: [1]
```

**Time Complexity:** O(n) - Visit each node once  
**Space Complexity:** O(h) - Recursion stack depth, h is tree height

Deep Insights:
  - Rule: Swap left and right recursively or iteratively; mirror the tree; O(n) time, O(h) space.
  - Real-world: Tree mirroring, symmetric tree creation, tree transformation, reflection algorithms.
  - Common mistake: Not handling null correctly; forgetting to swap in both subtrees; structure preserved.
  - Optimization: BFS swap by levels works too; O(n) time, O(h) space; idempotent only if called twice.
  - Interview tip: Explain swapping clearly; mention iterative vs recursive; ask about in-place requirements.
## Q61. Symmetric Tree

Concept: Check mirror: left.left vs right.right and left.right vs right.left. Compare pairs recursively.

```javascript
function isSymmetric(root) {
  function eq(a, b) {
    if (!a || !b) return a === b;
    return a.val === b.val && eq(a.left, b.right) && eq(a.right, b.left);
  }
  return eq(root?.left, root?.right);
}

// Test Cases:
//
// Example 1:
//   Input: root = [1, 2, 2, 3, 4, 4, 3]
//   Output: true
//
// Example 2:
//   Input: root = [1, 2, 2, null, 3, null, 3]
//   Output: false
//
// Example 3:
//   Input: root = []
//   Output: true
//
// Example 4:
//   Input: root = [1]
//   Output: true
```

**Time Complexity:** O(n) - Visit each node once  
**Space Complexity:** O(h) - Recursion stack depth, h is tree height

Deep Insights:
  - Rule: Check mirror: left.left vs right.right and left.right vs right.left; compare pairs recursively; O(n) time.
  - Real-world: Symmetric tree validation, mirror checking, reflection validation, tree symmetry analysis.
  - Common mistake: Null vs non-null mismatch fails; value equality required at mirrors; wrong comparison order.
  - Optimization: BFS with deque pairs works as well; O(n) time; null handling is crucial.
  - Interview tip: Explain mirror comparison clearly; mention BFS alternative; ask about empty tree.
## Q62. Path Sum

Concept: Root-to-leaf path with sum target; subtract as you go. Check leaf when sum matches.

```javascript
function hasPathSum(root, target) {
  if (!root) return false;
  if (!root.left && !root.right) return root.val === target;
  const t = target - root.val;
  return hasPathSum(root.left, t) || hasPathSum(root.right, t);
}

// Test Cases:
//
// Example 1:
//   Input: root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1], targetSum = 22
//   Output: true
//   Explanation: Path 5 -> 4 -> 11 -> 2 has sum = 22
//
// Example 2:
//   Input: root = [1, 2, 3], targetSum = 5
//   Output: false
//
// Example 3:
//   Input: root = [], targetSum = 0
//   Output: false
//
// Example 4:
//   Input: root = [1, 2], targetSum = 1
//   Output: false
```

**Time Complexity:** O(n) - Visit each node once  
**Space Complexity:** O(h) - Recursion stack depth, h is tree height

Deep Insights:
  - Rule: Root-to-leaf path with sum target; subtract as you go; check leaf when sum matches; O(n) time.
  - Real-world: Path sum problems, target sum paths, tree traversal with constraints, sum validation.
  - Common mistake: Exact leaf requirement; negative values allowed; not handling empty tree correctly; multiple paths possible.
  - Optimization: Backtracking sum reduces state; early return possible; O(h) space for recursion.
  - Interview tip: Explain leaf requirement clearly; mention negative values; ask about all paths vs any path.
## Q63. LCA in Binary Tree

Concept: If both nodes are in different subtrees, current is LCA; else pass non-null child up. Post-order returns match or null.

```javascript
function lowestCommonAncestor(root, p, q) {
  if (!root || root === p || root === q) return root;
  const L = lowestCommonAncestor(root.left, p, q);
  const R = lowestCommonAncestor(root.right, p, q);
  if (L && R) return root;
  return L || R;
}

// Test Cases:
//
// Example 1:
//   Input: root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 1
//   Output: 3
//   Explanation: LCA of nodes 5 and 1 is 3
//
// Example 2:
//   Input: root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 4
//   Output: 5
//   Explanation: LCA of nodes 5 and 4 is 5 (ancestor of itself)
//
// Example 3:
//   Input: root = [1, 2], p = 1, q = 2
//   Output: 1
//
// Example 4:
//   Input: root = [1], p = 1, q = 1
//   Output: 1
```

**Time Complexity:** O(n) - Visit each node once in worst case  
**Space Complexity:** O(h) - Recursion stack depth, h is tree height

Deep Insights:
  - Rule: If both nodes in different subtrees, current is LCA; else pass non-null child up; post-order returns match or null.
  - Real-world: Tree LCA queries, genealogical trees, hierarchical systems, common ancestor problems.
  - Common mistake: Works for general binary trees; assumes both nodes exist; not handling null correctly.
  - Optimization: O(n) time; post-order ensures proper handling; for parent pointers, move up with depths.
  - Interview tip: Explain post-order logic clearly; mention BST variant is simpler; ask about node existence guarantee.
## Q64. Serialize & Deserialize

Concept: Preorder with null markers; join/split by delimiter. Rebuild via index counter.

```javascript
function serialize(root) {
  const out = [];
  function pre(node) {
    if (!node) {
      out.push('#');
      return;
    }
    out.push(node.val);
    pre(node.left);
    pre(node.right);
  }
  pre(root);
  return out.join(',');
}

function deserialize(data) {
  const vals = data.split(',');
  let idx = 0;
  function build() {
    if (vals[idx] === '#') {
      idx++;
      return null;
    }
    const node = new TreeNode(parseInt(vals[idx]));
    idx++;
    node.left = build();
    node.right = build();
    return node;
  }
  return build();
}

// Test Cases:
//
// Example 1 (serialize):
//   Input: root = [1, 2, 3, null, null, 4, 5]
//   Output: "1,2,#,#,3,4,#,#,5,#,#"
//
// Example 1 (deserialize):
//   Input: data = "1,2,#,#,3,4,#,#,5,#,#"
//   Output: root = [1, 2, 3, null, null, 4, 5]
//
// Example 2:
//   Input: root = []
//   serialize Output: "#"
//   deserialize Output: null
//
// Example 3:
//   Input: root = [1]
//   serialize Output: "1,#,#"
//   deserialize Output: [1]
```

**Time Complexity:** O(n) - Visit each node once for both serialize and deserialize  
**Space Complexity:** O(n) - Serialized string and recursion stack

Deep Insights:
  - Rule: Preorder with null markers; join/split by delimiter; rebuild via index counter; O(n) time.
  - Real-world: Tree serialization, data persistence, tree storage, network transmission, tree reconstruction.
  - Common mistake: BFS (level-order) alternative common; use sentinel for nulls; ensure consistent delimiter; avoid eval.
  - Optimization: Preorder is compact; parse explicitly; delimiter choice matters; O(n) space for serialized string.
  - Interview tip: Explain serialization format clearly; mention BFS alternative; ask about delimiter choice.
## Q65. Level Order Traversal

Concept: BFS queue by levels; collect values per level. Same as traversal variant.

```javascript
function levelOrder(root) {
  const res = [];
  if (!root) return res;
  const q = [root];
  while (q.length) {
    const n = q.length;
    const level = [];
    for (let i = 0; i < n; i++) {
      const x = q.shift();
      level.push(x.val);
      if (x.left) {
        q.push(x.left);
      }
      if (x.right) {
        q.push(x.right);
      }
    }
    res.push(level);
  }
  return res;
}

// Test Cases:
//
// Example 1:
//   Input: root = [3, 9, 20, null, null, 15, 7]
//   Output: [[3], [9, 20], [15, 7]]
//
// Example 2:
//   Input: root = [1]
//   Output: [[1]]
//
// Example 3:
//   Input: root = []
//   Output: []
//
// Example 4:
//   Input: root = [1, 2, 3, 4, 5, 6, 7]
//   Output: [[1], [2, 3], [4, 5, 6, 7]]
```

**Time Complexity:** O(n) - Visit each node once  
**Space Complexity:** O(w) - Queue stores nodes at widest level, w is maximum width

Deep Insights:
  - Rule: BFS queue by levels; collect values per level; O(n) time, O(w) space.
  - Real-world: Level-order traversal, tree level analysis, hierarchical processing, breadth-first algorithms.
  - Common mistake: Queue shift is O(n); use head index for perf; not handling empty tree correctly.
  - Optimization: O(n) time, O(w) space (width); variant returns flat list; efficient level collection.
  - Interview tip: Explain BFS clearly; mention space complexity; ask about flat vs nested output.
## Q66. Zigzag Traversal

Concept: Alternate left-to-right and right-to-left per level. Reverse level or use deque.

```javascript
function zigzagLevelOrder(root) {
  const res = [];
  if (!root) return res;
  const q = [root];
  let rev = false;
  while (q.length) {
    const n = q.length;
    const level = [];
    for (let i = 0; i < n; i++) {
      const x = q.shift();
      level.push(x.val);
      if (x.left) {
        q.push(x.left);
      }
      if (x.right) {
        q.push(x.right);
      }
    }
    if (rev) {
      level.reverse();
    }
    res.push(level);
    rev = !rev;
  }
  return res;
}

// Test Cases:
//
// Example 1:
//   Input: root = [3, 9, 20, null, null, 15, 7]
//   Output: [[3], [20, 9], [15, 7]]
//
// Example 2:
//   Input: root = [1]
//   Output: [[1]]
//
// Example 3:
//   Input: root = []
//   Output: []
//
// Example 4:
//   Input: root = [1, 2, 3, 4, null, null, 5]
//   Output: [[1], [3, 2], [4, 5]]
```

**Time Complexity:** O(n) - Visit each node once  
**Space Complexity:** O(w) - Queue stores nodes at widest level, w is maximum width

Deep Insights:
  - Rule: Alternate left-to-right and right-to-left per level; reverse level or use deque; O(n) time.
  - Real-world: Zigzag traversal, alternating tree traversal, snake pattern, level-based algorithms.
  - Common mistake: Reversing per level is fine; O(n) time; deque avoids reverse but more code; same BFS skeleton.
  - Optimization: Track boolean flag per level; reversing is acceptable; O(n) time optimal.
  - Interview tip: Explain alternation clearly; mention deque alternative; ask about output format.
## Q67. Left/Right View of Tree

Concept: Capture first (left view) or last (right view) node at each level via BFS.

```javascript
function rightSideView(root) {
  const res = [];
  if (!root) return res;
  const q = [root];
  while (q.length) {
    const n = q.length;
    for (let i = 0; i < n; i++) {
      const x = q.shift();
      if (i === n - 1) {
        res.push(x.val);
      }
      if (x.left) {
        q.push(x.left);
      }
      if (x.right) {
        q.push(x.right);
      }
    }
  }
  return res;
}

// Test Cases:
//
// Example 1:
//   Input: root = [1, 2, 3, null, 5, null, 4]
//   Output: [1, 3, 4]
//
// Example 2:
//   Input: root = [1, null, 3]
//   Output: [1, 3]
//
// Example 3:
//   Input: root = []
//   Output: []
//
// Example 4:
//   Input: root = [1, 2]
//   Output: [1, 2]
//
// Note: leftSideView (variant - take i === 0):
//   Input: root = [1, 2, 3, null, 5, null, 4]
//   Output: [1, 2, 5]
```

**Time Complexity:** O(n) - Visit each node once  
**Space Complexity:** O(w) - Queue stores nodes at widest level, w is maximum width

Deep Insights:
  - Rule: Capture first (left view) or last (right view) node at each level via BFS; O(n) time, O(w) space.
  - Real-world: Tree views, boundary visualization, side views, hierarchical display systems.
  - Common mistake: For left view, take i===0; DFS variant records first seen depth; width dictates space.
  - Optimization: O(n) time; width dictates space; BFS natural for level-based views.
  - Interview tip: Explain left vs right view clearly; mention DFS alternative; ask about output format.
## Q68. Boundary Traversal

Concept: Root (if not leaf), left boundary (excluding leaves), leaves, right boundary (excluding leaves, reverse).

```javascript
function boundaryOfBinaryTree(root) {
  if (!root) return [];

  // helper to check leaf
  function isLeaf(node) {
    return node && !node.left && !node.right;
  }

  const res = [];

  // 1. Add root (only if not leaf)
  if (!isLeaf(root)) res.push(root.val);

  // 2. Add left boundary (excluding leaves)
  function addLeft(node) {
    while (node) {
      if (!isLeaf(node)) res.push(node.val);
      node = node.left ? node.left : node.right;
    }
  }

  // 3. Add all leaf nodes
  function addLeaves(node) {
    if (!node) return;
    if (isLeaf(node)) {
      res.push(node.val);
      return;
    }
    addLeaves(node.left);
    addLeaves(node.right);
  }

  // 4. Add right boundary (excluding leaves, bottom → top)
  function addRight(node) {
    const stack = [];
    while (node) {
      if (!isLeaf(node)) stack.push(node.val);
      node = node.right ? node.right : node.left;
    }
    while (stack.length) res.push(stack.pop());
  }

  addLeft(root.left);
  addLeaves(root);
  addRight(root.right);

  return res;
}

// Test Cases:
//
// Example 1:
//   Input: root = [1, null, 2, 3, 4]
//   Output: [1, 3, 4, 2]
//
// Example 2:
//   Input: root = [1, 2, 3, 4, 5, 6, null, null, null, 7, 8, 9, 10]
//   Output: [1, 2, 4, 7, 8, 9, 10, 6, 3]
//
// Example 3:
//   Input: root = [1]
//   Output: [1]
//
// Example 4:
//   Input: root = [1, 2, 3]
//   Output: [1, 2, 3]
```

**Time Complexity:** O(n) - Visit each node once  
**Space Complexity:** O(h) - Recursion stack for leaves, h is tree height

Deep Insights:
  - Rule: Left boundary (excluding leaves), leaves, right boundary (excluding leaves, reverse); O(n) time.
  - Real-world: Boundary traversal, tree perimeter, boundary visualization, tree structure analysis.
  - Common mistake: Avoid duplicates for root and leaves; handle skewed trees; order is specific.
  - Optimization: O(n) traversal; order is specific; handles edge cases correctly.
  - Interview tip: Explain three-part boundary clearly; mention duplicate avoidance; ask about edge cases.
## Q69. DFS Pre/In/Post Order

Concept: Standard iterative inorder using stack (avoid recursion).

```javascript
function inorderIter(root) {
  const res = [];
  const st = [];
  let cur = root;
  while (cur || st.length) {
    while (cur) {
      st.push(cur);
      cur = cur.left;
    }
    cur = st.pop();
    res.push(cur.val);
    cur = cur.right;
  }
  return res;
}

// Test Cases:
//
// Example 1:
//   Input: root = [1, null, 2, 3]
//   Output: [1, 3, 2]
//
// Example 2:
//   Input: root = []
//   Output: []
//
// Example 3:
//   Input: root = [1]
//   Output: [1]
//
// Example 4:
//   Input: root = [1, 2]
//   Output: [2, 1]
//
// Example 5:
//   Input: root = [1, null, 2]
//   Output: [1, 2]
//
// Note: For preorder, push right then left before pushing node.
//       For postorder, use two stacks or tagged nodes.
```

**Time Complexity:** O(n) - Visit each node once  
**Space Complexity:** O(h) - Stack stores nodes along path, h is tree height

Deep Insights:
  - Rule: Standard iterative inorder using stack (avoid recursion); O(n) time, O(h) space.
  - Real-world: Iterative tree traversal, stack-based algorithms, avoiding recursion, tree computations.
  - Common mistake: Iterative avoids deep recursion; preorder iterative uses push right then left; wrong stack usage.
  - Optimization: Iterative avoids deep recursion; postorder via two stacks or tagged nodes; use for tree-based computations.
  - Interview tip: Explain iterative approach clearly; mention preorder/postorder variants; ask about recursion vs iteration.
## Q70. Construct Tree from Inorder & Preorder

Concept: Preorder gives root; split inorder around root; recurse for subtrees. Use index map for O(1) splits.

```javascript
function buildTree(preorder, inorder) {
  const map = new Map(); // value -> index in inorder
  for (let i = 0; i < inorder.length; i++) {
    map.set(inorder[i], i);
  }
  let preIndex = 0;
  function build(left, right) {
    if (left > right) return null;
    const rootVal = preorder[preIndex++];
    const root = new TreeNode(rootVal);
    const mid = map.get(rootVal);
    root.left = build(left, mid - 1);
    root.right = build(mid + 1, right);
    return root;
  }
  return build(0, inorder.length - 1);
}

// Test Cases:
//
// Example 1:
//   Input: preorder = [3, 9, 20, 15, 7], inorder = [9, 3, 15, 20, 7]
//   Output: [3, 9, 20, null, null, 15, 7]
//
// Example 2:
//   Input: preorder = [-1], inorder = [-1]
//   Output: [-1]
//
// Example 3:
//   Input: preorder = [1, 2], inorder = [2, 1]
//   Output: [1, 2]
//
// Example 4:
//   Input: preorder = [1, 2, 3], inorder = [2, 1, 3]
//   Output: [1, 2, 3]
```

**Time Complexity:** O(n) - Visit each node once during construction  
**Space Complexity:** O(n) - Hash map stores inorder positions, recursion stack O(h)

Deep Insights:
  - Rule: Preorder gives root; split inorder around root; recurse for subtrees; use index map for O(1) splits.
  - Real-world: Tree construction from traversals, serialization reconstruction, tree building algorithms.
  - Common mistake: O(n) build with index map; unique values assumed; similar for inorder+postorder; avoid slicing arrays.
  - Optimization: Index map for O(1) lookups; avoid slicing arrays for better performance; O(n) time optimal.
  - Interview tip: Explain index map clearly; mention uniqueness requirement; ask about inorder+postorder variant.
## Q71. Morris Traversal

Concept: Inorder without stack/recursion by threading right pointers temporarily. Restore tree after visiting.

```javascript
function morrisInorder(root) {
  const res = [];
  let cur = root;
  while (cur) {
    if (!cur.left) {
      res.push(cur.val);
      cur = cur.right;
    } else {
      let pre = cur.left;
      while (pre.right && pre.right !== cur) {
        pre = pre.right;
      }
      if (!pre.right) {
        pre.right = cur;
        cur = cur.left;
      } else {
        pre.right = null;
        res.push(cur.val);
        cur = cur.right;
      }
    }
  }
  return res;
}

// Test Cases:
//
// Example 1:
//   Input: root = [1, null, 2, 3]
//   Output: [1, 3, 2]
//
// Example 2:
//   Input: root = []
//   Output: []
//
// Example 3:
//   Input: root = [1]
//   Output: [1]
//
// Example 4:
//   Input: root = [4, 2, 5, 1, 3]
//   Output: [2, 4, 1, 5, 3]
//
// Note: O(1) space complexity, tree structure is restored after traversal
```

**Time Complexity:** O(n) - Visit each node at most twice  
**Space Complexity:** O(1) - Only uses existing tree pointers, no extra space

Deep Insights:
  - Rule: Inorder without stack/recursion by threading right pointers temporarily; restore tree after visiting.
  - Real-world: O(1) space traversal, memory-efficient tree traversal, constant space algorithms, threading techniques.
  - Common mistake: O(n) time, O(1) space; tree restored at end; subtle pointer logic; only inorder shown (preorder similar).
  - Optimization: O(1) space optimal; tree restored at end; subtle pointer logic needed; preorder similar.
  - Interview tip: Explain threading technique clearly; mention tree restoration; ask about preorder variant.
## Q72. Maximum Path Sum

Concept: Path can bend at a node; gain = max(0,left) + node + max(0,right). Track best.

```javascript
function maxPathSum(root) {
  let maxSum = -Infinity;
  function dfs(node) {
    if (!node) return 0;

    // only take positive contributions
    const left = Math.max(dfs(node.left), 0);
    const right = Math.max(dfs(node.right), 0);
    // compute max path using this node as highest point
    const localMax = node.val + left + right;
    // update global result
    maxSum = Math.max(maxSum, localMax);
    // return best single-branch path upward
    return node.val + Math.max(left, right);
  }
  dfs(root);
  return maxSum;
}

// Test Cases:
//
// Example 1:
//   Input: root = [1, 2, 3]
//   Output: 6
//   Explanation: Path 2 -> 1 -> 3 has sum = 6
//
// Example 2:
//   Input: root = [-10, 9, 20, null, null, 15, 7]
//   Output: 42
//   Explanation: Path 15 -> 20 -> 7 has sum = 42
//
// Example 3:
//   Input: root = [-3]
//   Output: -3
//
// Example 4:
//   Input: root = [2, -1]
//   Output: 2
```

**Time Complexity:** O(n) - Visit each node once  
**Space Complexity:** O(h) - Recursion stack depth, h is tree height

Deep Insights:
  - Rule: Path can bend at a node; gain = max(0,left) + node + max(0,right); track best; post-order traversal.
  - Real-world: Maximum path problems, tree path optimization, constrained path algorithms, tree traversal.
  - Common mistake: Handles negatives by clamping to 0; best is across all nodes; return upward only one-side gain.
  - Optimization: Post-order traversal ensures proper calculation; clamping to 0 handles negatives; O(n) time.
  - Interview tip: Explain path bending clearly; mention negative handling; ask about path requirements.
## Q73. Vertical Order Traversal

Concept: BFS with column and row indices; sort by column, row, value; group by column.

```javascript
function verticalTraversal(root) {
  if (!root) return [];

  const nodes = []; // store [col, row, val]
  const queue = [[root, 0, 0]]; // [node, col, row]
  while (queue.length) {
    const [node, col, row] = queue.shift();
    nodes.push([col, row, node.val]);
    if (node.left) queue.push([node.left, col - 1, row + 1]);
    if (node.right) queue.push([node.right, col + 1, row + 1]);
  }

  // sort by: col asc, row asc, value asc
  nodes.sort((a, b) => {
    if (a[0] !== b[0]) return a[0] - b[0]; // col
    if (a[1] !== b[1]) return a[1] - b[1]; // row
    return a[2] - b[2]; // value
  });

  const map = new Map();
  for (const [col, row, val] of nodes) {
    if (!map.has(col)) map.set(col, []);
    map.get(col).push(val);
  }
  return [...map.values()];
}

// Test Cases:
//
// Example 1:
//   Input: root = [3, 9, 20, null, null, 15, 7]
//   Output: [[9], [3, 15], [20], [7]]
//
// Example 2:
//   Input: root = [3, 9, 8, 4, 0, 1, 7]
//   Output: [[4], [9], [3, 0, 1], [8], [7]]
//
// Example 3:
//   Input: root = [1]
//   Output: [[1]]
//
// Example 4:
//   Input: root = []
//   Output: []
```

**Time Complexity:** O(n log n) - Visit each node once, then sort n nodes  
**Space Complexity:** O(n) - Store all nodes with positions, map stores column groups

Deep Insights:
  - Rule: BFS with column and row indices; sort by column, then row, then value; group by column; O(n log n) time.
  - Real-world: Vertical order traversal, column-based tree views with proper ordering, tree visualization, hierarchical sorting.
  - Common mistake: Must sort when nodes share same position; ordering is column → row → value; BFS naturally assigns row indices.
  - Optimization: Sort after collection is cleaner; O(n log n) due to sorting; handles overlapping nodes correctly.
  - Interview tip: Explain sorting requirement clearly; mention why sorting is needed (same position nodes); ask about ordering rules.
## Q74. Count Nodes in Complete Tree

Concept: Use left/right heights to detect perfect subtrees: nodes = 2^h - 1. Recurse on incomplete side.

```javascript
function countNodes(root) {
  if (!root) return 0;

  function leftHeight(node) {
    let h = 0;
    while (node) {
      h++;
      node = node.left;
    }
    return h;
  }

  function rightHeight(node) {
    let h = 0;
    while (node) {
      h++;
      node = node.right;
    }
    return h;
  }

  const leftH = leftHeight(root);
  const rightH = rightHeight(root);

  // if both heights are equal, it's a perfect tree
  if (leftH === rightH) {
    return (1 << leftH) - 1; // 2^h - 1
  }

  // otherwise count nodes recursively
  return 1 + countNodes(root.left) + countNodes(root.right);
}

// Test Cases:
//
// Example 1:
//   Input: root = [1, 2, 3, 4, 5, 6]
//   Output: 6
//
// Example 2:
//   Input: root = []
//   Output: 0
//
// Example 3:
//   Input: root = [1]
//   Output: 1
//
// Example 4:
//   Input: root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
//   Output: 12
//
// Note: Assumes complete binary tree for optimization
```

**Time Complexity:** O(log² n) - Average case, O(n) worst case for skewed tree  
**Space Complexity:** O(log n) - Recursion stack depth for complete tree

Deep Insights:
  - Rule: Use left/right heights to detect perfect subtrees: nodes = 2^h - 1; recurse on incomplete side.
  - Real-world: Complete tree counting, efficient tree node counting, tree size queries, height-based algorithms.
  - Common mistake: O(log^2 n) average; complete tree property critical; bit shift for 2^h; avoid full traversal.
  - Optimization: O(log^2 n) average time; bit shift for 2^h calculation; avoids full traversal.
  - Interview tip: Explain perfect subtree detection clearly; mention bit shift optimization; ask about complete vs full tree.
## Q75. Binary Tree to DLL

Concept: Inorder traversal linking nodes as doubly linked list in-place. Keep prev pointer across calls.

```javascript
function treeToDoublyList(root) {
  if (!root) return null;
  let head = null;
  let prev = null;
  (function dfs(n) {
    if (!n) return;
    dfs(n.left);
    if (!head) {
      head = n;
    }
    if (prev) {
      prev.right = n;
      n.left = prev;
    }
    prev = n;
    dfs(n.right);
  })(root);
  // Optionally make circular:
  // head.left = prev; prev.right = head;
  return head;
}

// Test Cases:
//
// Example 1:
//   Input: root = [4, 2, 5, 1, 3]
//   Output: Doubly linked list: 1 <-> 2 <-> 3 <-> 4 <-> 5 (inorder order)
//
// Example 2:
//   Input: root = [2, 1, 3]
//   Output: Doubly linked list: 1 <-> 2 <-> 3
//
// Example 3:
//   Input: root = [1]
//   Output: Doubly linked list with single node
//
// Example 4:
//   Input: root = []
//   Output: null
//
// Note: For BST, this creates a sorted doubly linked list.
//       If circular required, uncomment the last two lines.
```

**Time Complexity:** O(n) - Visit each node once during inorder traversal  
**Space Complexity:** O(h) - Recursion stack depth, h is tree height

Deep Insights:
  - Rule: Inorder traversal linking nodes as doubly linked list in-place; keep prev pointer across calls.
  - Real-world: Tree to DLL conversion, in-place tree transformation, linked list construction, tree flattening.
  - Common mistake: Inorder preserves sorted order for BST; make circular if required by spec; in-place links, no extra nodes.
  - Optimization: Maintain prev across recursion; O(n) time, O(h) space; in-place transformation.
  - Interview tip: Explain inorder linking clearly; mention circular variant; ask about preserving original tree.

## Q76. Same Tree

Concept:
Check if two binary trees are identical using recursive comparison.

Example:
```javascript
function isSameTree(p, q) {
  if (!p && !q) return true;
  if (!p || !q) return false;
  if (p.val !== q.val) return false;
  
  return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
}

// Input: p = [1,2,3], q = [1,2,3]
// Output: true
// Explanation: Both trees are identical

// Input: p = [1,2], q = [1,null,2]
// Output: false
// Explanation: Trees have different structure

// Input: p = [1,2,1], q = [1,1,2]
// Output: false
// Explanation: Trees have different values
```

**Time Complexity:** O(min(m,n)) - Visit minimum nodes between two trees  
**Space Complexity:** O(min(h1,h2)) - Recursion stack depth

Deep Insights:
- Recursive comparison: check null cases, values, then recursively check left and right; O(min(m,n)) time.
- Base cases: both null returns true; one null returns false; values different returns false.
- Recursive case: check both subtrees.
- Edge case: Both empty trees returns true; one empty returns false.
- Interview tip: Explain recursive structure; mention base cases clearly.

## Q77. Construct Binary Tree from Inorder and Postorder Traversal

Concept:
Build binary tree from inorder and postorder traversals; use postorder last element as root.

Example:
```javascript
function buildTree(inorder, postorder) {
  if (inorder.length === 0) return null;
  
  const rootVal = postorder[postorder.length - 1];
  const root = new TreeNode(rootVal);
  
  const rootIndex = inorder.indexOf(rootVal);
  
  const leftInorder = inorder.slice(0, rootIndex);
  const rightInorder = inorder.slice(rootIndex + 1);
  
  const leftPostorder = postorder.slice(0, leftInorder.length);
  const rightPostorder = postorder.slice(leftInorder.length, postorder.length - 1);
  
  root.left = buildTree(leftInorder, leftPostorder);
  root.right = buildTree(rightInorder, rightPostorder);
  
  return root;
}

// Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
// Output: [3,9,20,null,null,15,7]
// Explanation: Root 3, left [9], right [15,20,7]

// Input: inorder = [-1], postorder = [-1]
// Output: [-1]
// Explanation: Single node tree
```

**Time Complexity:** O(n²) - indexOf in each recursion, can optimize to O(n) with hash map  
**Space Complexity:** O(n) - Recursion stack + array slices

Deep Insights:
- Postorder last element is root; find root in inorder; split arrays; O(n²) time without optimization.
- Use postorder last element as root; find root in inorder; split arrays at root position.
- Optimize to O(n) using hash map for inorder positions.
- Edge case: Empty arrays return null; single element returns node.
- Interview tip: Explain root finding; mention optimization possibility; ask about preorder variant.

## Q78. Populating Next Right Pointers in Each Node II

Concept:
Connect each node's next pointer to its right neighbor at same level; use BFS or iterative approach.

Example:
```javascript
function connect(root) {
  if (!root) return root;
  
  let head = root;
  
  while (head) {
    const dummy = new Node(0);
    let current = dummy;
    
    while (head) {
      if (head.left) {
        current.next = head.left;
        current = current.next;
      }
      if (head.right) {
        current.next = head.right;
        current = current.next;
      }
      head = head.next;
    }
    
    head = dummy.next;
  }
  
  return root;
}

// Input: root = [1,2,3,4,5,null,7]
// Output: [1,#,2,3,#,4,5,7,#]
// Explanation: Connect nodes at same level

// Input: root = []
// Output: []
```

**Time Complexity:** O(n) - Visit each node once  
**Space Complexity:** O(1) - Constant extra space

Deep Insights:
- Use dummy node for level traversal; connect children iteratively; O(n) time, O(1) space.
- Traverse level by level using next pointers; connect children of current level.
- Use dummy node to simplify connection logic.
- Edge case: Empty tree returns null; single node returns unchanged.
- Interview tip: Explain level traversal; mention dummy node usage; compare with perfect tree variant.

## Q79. Flatten Binary Tree to Linked List

Concept:
Flatten tree to linked list in-place using right child pointers; use postorder traversal.

Example:
```javascript
function flatten(root) {
  if (!root) return;
  
  let prev = null;
  
  function dfs(node) {
    if (!node) return;
    
    dfs(node.right);
    dfs(node.left);
    
    node.right = prev;
    node.left = null;
    prev = node;
  }
  
  dfs(root);
}

// Input: root = [1,2,5,3,4,null,6]
// Output: [1,null,2,null,3,null,4,null,5,null,6]
// Explanation: Flatten to linked list

// Input: root = []
// Output: []
```

**Time Complexity:** O(n) - Visit each node once  
**Space Complexity:** O(h) - Recursion stack depth

Deep Insights:
- Postorder traversal: process right, then left, then current; link in reverse order; O(n) time, O(h) space.
- Use postorder to process children before parent; link from right to left.
- Set left to null; link right to previous node.
- Edge case: Empty tree returns null; single node returns unchanged.
- Interview tip: Explain postorder approach; mention in-place transformation.

## Q80. Sum Root to Leaf Numbers

Concept:
Calculate sum of all root-to-leaf numbers; use DFS with path sum tracking.

Example:
```javascript
function sumNumbers(root) {
  let sum = 0;
  
  function dfs(node, pathSum) {
    if (!node) return;
    
    pathSum = pathSum * 10 + node.val;
    
    if (!node.left && !node.right) {
      sum += pathSum;
      return;
    }
    
    dfs(node.left, pathSum);
    dfs(node.right, pathSum);
  }
  
  dfs(root, 0);
  return sum;
}

// Input: root = [1,2,3]
// Output: 25
// Explanation: Path 1->2 = 12, path 1->3 = 13, sum = 12 + 13 = 25

// Input: root = [4,9,0,5,1]
// Output: 1026
// Explanation: 495 + 491 + 40 = 1026

// Input: root = [1]
// Output: 1
```

**Time Complexity:** O(n) - Visit each node once  
**Space Complexity:** O(h) - Recursion stack depth

Deep Insights:
- DFS with path sum tracking; multiply by 10 and add current value; accumulate at leaves; O(n) time, O(h) space.
- Build number from root to leaf; multiply path sum by 10, add node value.
- Add to total when reaching leaf.
- Edge case: Empty tree returns 0; single node returns its value.
- Interview tip: Explain path sum building; mention multiplication by 10.

## Q81. Binary Tree Right Side View

Concept:
Return values of nodes visible from right side; use BFS to get last node of each level.

Example:
```javascript
function rightSideView(root) {
  if (!root) return [];
  
  const result = [];
  const queue = [root];
  
  while (queue.length) {
    const levelSize = queue.length;
    
    for (let i = 0; i < levelSize; i++) {
      const node = queue.shift();
      
      if (i === levelSize - 1) {
        result.push(node.val);
      }
      
      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }
  }
  
  return result;
}

// Input: root = [1,2,3,null,5,null,4]
// Output: [1,3,4]
// Explanation: Rightmost nodes at each level

// Input: root = [1,null,3]
// Output: [1,3]

// Input: root = []
// Output: []
```

**Time Complexity:** O(n) - Visit each node once  
**Space Complexity:** O(w) - Queue storage, w is maximum width

Deep Insights:
- BFS level-order traversal; capture last node of each level; O(n) time, O(w) space.
- Use queue for level-order; track level size; capture rightmost node.
- Alternative: DFS with depth tracking, keep only rightmost value per depth.
- Edge case: Empty tree returns empty array; single node returns its value.
- Interview tip: Explain BFS approach; mention DFS alternative; ask about left side view.

## Q82. Average of Levels in Binary Tree

Concept:
Calculate average value of nodes at each level; use BFS level-order traversal.

Example:
```javascript
function averageOfLevels(root) {
  if (!root) return [];
  
  const result = [];
  const queue = [root];
  
  while (queue.length) {
    const levelSize = queue.length;
    let sum = 0;
    
    for (let i = 0; i < levelSize; i++) {
      const node = queue.shift();
      sum += node.val;
      
      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }
    
    result.push(sum / levelSize);
  }
  
  return result;
}

// Input: root = [3,9,20,null,null,15,7]
// Output: [3.00000,14.50000,11.00000]
// Explanation: Level 0: [3], average = 3; Level 1: [9,20], average = 14.5; Level 2: [15,7], average = 11

// Input: root = [3,9,20,15,7]
// Output: [3.00000,14.50000,11.00000]

// Input: root = [1]
// Output: [1.0]
```

**Time Complexity:** O(n) - Visit each node once  
**Space Complexity:** O(w) - Queue storage, w is maximum width

Deep Insights:
- BFS level-order traversal; sum values at each level; divide by level size; O(n) time, O(w) space.
- Use queue for level-order; track level size; sum all values in level.
- Calculate average: sum / levelSize.
- Edge case: Empty tree returns empty array; single node returns its value.
- Interview tip: Explain BFS approach; mention level tracking; ask about integer overflow.