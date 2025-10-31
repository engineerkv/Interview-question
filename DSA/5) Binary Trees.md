# Binary Trees

## Q56. Binary Tree Traversals (DFS/BFS)

- Concept: Visit nodes in specific orders. DFS: pre/in/post-order; BFS: level-order using queue. Choose based on problem needs (order, layers, aggregates).

```javascript
function preorder(root) {
  const res = [];
  (function dfs(n) { if (!n) return; res.push(n.val); dfs(n.left); dfs(n.right); })(root);
  return res;
}
function inorder(root) {
  const res = [];
  (function dfs(n) { if (!n) return; dfs(n.left); res.push(n.val); dfs(n.right); })(root);
  return res;
}
function postorder(root) {
  const res = [];
  (function dfs(n) { if (!n) return; dfs(n.left); dfs(n.right); res.push(n.val); })(root);
  return res;
}
function levelOrder(root) {
  const res = [];
  if (!root) return res;
  const q = [root];
  while (q.length) {
    const len = q.length;
    const level = [];
    for (let i = 0; i < len; i++) {
      const n = q.shift();
      level.push(n.val);
      if (n.left) q.push(n.left);
      if (n.right) q.push(n.right);
    }
    res.push(level);
  }
  return res;
}
```

- Deep Insights:
  - DFS: recursion or explicit stack.
  - BFS: queue by levels.
  - Inorder on BST yields sorted values.
  - Pre/post useful for build/destroy phases.

## Q57. Max Depth of Binary Tree

- Concept: Height is 1 + max(depth(left), depth(right)); handle null as 0. DFS recursion is simplest.

```javascript
function maxDepth(root) {
  if (!root) return 0;
  return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
}
```

- Deep Insights:
  - O(n) time, O(h) space recursion.
  - BFS variant counts levels.
  - Watch stack depth for skewed trees.
  - Tail recursion not guaranteed in JS.

## Q58. Diameter of Binary Tree

- Concept: Longest path through any node = leftHeight + rightHeight. Track global best during post-order.

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
```

- Deep Insights:
  - Path length counted in edges.
  - Single traversal O(n).
  - Works for empty (0) and single node (0).
  - Separate from max depth.

## Q59. Balanced Binary Tree

- Concept: Height-balanced if each node’s subtrees differ by <=1 and subtrees are balanced. Use -1 sentinel to propagate unbalanced.

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
```

- Deep Insights:
  - O(n) single pass.
  - Early exit on imbalance.
  - Edges vs nodes definitions consistent.
  - Skewed tree fails quickly.

## Q60. Invert Binary Tree

- Concept: Swap left and right recursively or iteratively. Mirror the tree.

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
```

- Deep Insights:
  - O(n) time, O(h) space.
  - BFS swap by levels works too.
  - Structure preserved, values unchanged.
  - Idempotent only if called twice.

## Q61. Symmetric Tree

- Concept: Check mirror: left.left vs right.right and left.right vs right.left. Compare pairs recursively.

```javascript
function isSymmetric(root) {
  function eq(a, b) {
    if (!a || !b) return a === b;
    return a.val === b.val && eq(a.left, b.right) && eq(a.right, b.left);
  }
  return eq(root?.left, root?.right);
}
```

- Deep Insights:
  - BFS with deque pairs works as well.
  - Null vs non-null mismatch fails.
  - Value equality required at mirrors.
  - O(n) time.

## Q62. Path Sum

- Concept: Root-to-leaf path with sum target; subtract as you go. Check leaf when sum matches.

```javascript
function hasPathSum(root, target) {
  if (!root) return false;
  if (!root.left && !root.right) return root.val === target;
  const t = target - root.val;
  return hasPathSum(root.left, t) || hasPathSum(root.right, t);
}
```

- Deep Insights:
  - Exact leaf requirement.
  - Negative values allowed.
  - Backtracking sum reduces state.
  - Multiple paths possible.

## Q63. LCA in Binary Tree

- Concept: If both nodes are in different subtrees, current is LCA; else pass non-null child up. Post-order returns match or null.

```javascript
function lowestCommonAncestor(root, p, q) {
  if (!root || root === p || root === q) return root;
  const L = lowestCommonAncestor(root.left, p, q);
  const R = lowestCommonAncestor(root.right, p, q);
  if (L && R) return root;
  return L || R;
}
```

- Deep Insights:
  - Works for general binary trees.
  - Assumes both nodes exist.
  - O(n) time.
  - For parent pointers, move up with depths.

## Q64. Serialize & Deserialize

- Concept: Preorder with null markers; join/split by delimiter. Rebuild via recursive iterator.

```javascript
function serialize(root) {
  const out = [];
  (function pre(n) {
    if (!n) { out.push('#'); return; }
    out.push(String(n.val));
    pre(n.left);
    pre(n.right);
  })(root);
  return out.join(',');
}
function deserialize(data) {
  const it = data.split(',')[Symbol.iterator]();
  function build() {
    const { value } = it.next();
    if (value === '#') return null;
    return { val: +value, left: build(), right: build() };
  }
  return build();
}
```

- Deep Insights:
  - BFS (level-order) alternative common.
  - Use sentinel for nulls.
  - Ensure consistent delimiter.
  - Avoid eval; parse explicitly.

## Q65. Level Order Traversal

- Concept: BFS queue by levels; collect values per level. Same as traversal variant.

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
      if (x.left) q.push(x.left);
      if (x.right) q.push(x.right);
    }
    res.push(level);
  }
  return res;
}
```

- Deep Insights:
  - O(n) time, O(w) space (width).
  - Use for shortest path in unweighted trees.
  - Queue shift is O(n); use head index for perf.
  - Variant: return flat list.

## Q66. Zigzag Traversal

- Concept: Alternate left-to-right and right-to-left per level. Reverse level or use deque.

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
      if (x.left) q.push(x.left);
      if (x.right) q.push(x.right);
    }
    if (rev) level.reverse();
    res.push(level);
    rev = !rev;
  }
  return res;
}
```

- Deep Insights:
  - Reversing per level is fine; O(n).
  - Deque avoids reverse but more code.
  - Track boolean flag per level.
  - Same BFS skeleton.

## Q67. Left/Right View of Tree

- Concept: Capture first (left view) or last (right view) node at each level via BFS.

```javascript
function rightSideView(root) {
  const res = [];
  if (!root) return res;
  const q = [root];
  while (q.length) {
    const n = q.length;
    for (let i = 0; i < n; i++) {
      const x = q.shift();
      if (i === n - 1) res.push(x.val);
      if (x.left) q.push(x.left);
      if (x.right) q.push(x.right);
    }
  }
  return res;
}
```

- Deep Insights:
  - For left view, take i===0.
  - DFS variant: record first seen depth.
  - O(n) time.
  - Width dictates space.

## Q68. Boundary Traversal

- Concept: Left boundary (excluding leaves), leaves, right boundary (excluding leaves, reverse).

```javascript
function boundaryOfBinaryTree(root) {
  if (!root) return [];
  const res = [root.val];
  const isLeaf = (n) => n && !n.left && !n.right;

  // left boundary
  let cur = root.left;
  while (cur) {
    if (!isLeaf(cur)) res.push(cur.val);
    cur = cur.left ? cur.left : cur.right;
  }

  // leaves
  function addLeaves(n) {
    if (!n) return;
    if (isLeaf(n)) { if (n !== root) res.push(n.val); return; }
    addLeaves(n.left);
    addLeaves(n.right);
  }
  addLeaves(root);

  // right boundary
  const right = [];
  cur = root.right;
  while (cur) {
    if (!isLeaf(cur)) right.push(cur.val);
    cur = cur.right ? cur.right : cur.left;
  }
  right.reverse();
  res.push(...right);
  return res;
}
```

- Deep Insights:
  - Avoid duplicates for root and leaves.
  - Handle skewed trees.
  - O(n) traversal.
  - Order is specific.

## Q69. DFS Pre/In/Post Order

- Concept: Standard iterative inorder using stack (avoid recursion).

```javascript
function inorderIter(root) {
  const res = [];
  const st = [];
  let cur = root;
  while (cur || st.length) {
    while (cur) { st.push(cur); cur = cur.left; }
    cur = st.pop();
    res.push(cur.val);
    cur = cur.right;
  }
  return res;
}
```

- Deep Insights:
  - Iterative avoids deep recursion.
  - Preorder iterative uses push right then left.
  - Postorder via two stacks or tagged nodes.
  - Use for tree-based computations.

## Q70. Construct Tree from Inorder & Preorder

- Concept: Preorder gives root; split inorder around root; recurse for subtrees. Use index map for O(1) splits.

```javascript
function buildTree(preorder, inorder) {
  const pos = new Map();
  inorder.forEach((v, i) => pos.set(v, i));
  let pi = 0;
  function build(l, r) {
    if (l > r) return null;
    const val = preorder[pi++];
    const k = pos.get(val);
    const n = { val, left: null, right: null };
    n.left = build(l, k - 1);
    n.right = build(k + 1, r);
    return n;
  }
  return build(0, inorder.length - 1);
}
```

- Deep Insights:
  - O(n) build with index map.
  - Unique values assumed.
  - Similar for inorder+postorder.
  - Avoid slicing arrays.

## Q71. Morris Traversal

- Concept: Inorder without stack/recursion by threading right pointers temporarily. Restore tree after visiting.

```javascript
function morrisInorder(root) {
  const res = [];
  let cur = root;
  while (cur) {
    if (!cur.left) { res.push(cur.val); cur = cur.right; }
    else {
      let pre = cur.left;
      while (pre.right && pre.right !== cur) pre = pre.right;
      if (!pre.right) { pre.right = cur; cur = cur.left; }
      else { pre.right = null; res.push(cur.val); cur = cur.right; }
    }
  }
  return res;
}
```

- Deep Insights:
  - O(n) time, O(1) space.
  - Tree restored at end.
  - Subtle pointer logic.
  - Only inorder shown; preorder similar.

## Q72. Maximum Path Sum

- Concept: Path can bend at a node; gain = max(0,left) + node + max(0,right). Track best.

```javascript
function maxPathSum(root) {
  let best = -Infinity;
  function gain(n) {
    if (!n) return 0;
    const L = Math.max(0, gain(n.left));
    const R = Math.max(0, gain(n.right));
    best = Math.max(best, L + R + n.val);
    return n.val + Math.max(L, R);
  }
  gain(root);
  return best;
}
```

- Deep Insights:
  - Handles negatives by clamping to 0.
  - Post-order traversal.
  - best is across all nodes.
  - Return upward only one-side gain.

## Q73. Vertical Order Traversal

- Concept: BFS with column index; group by column, simple collection.

```javascript
function verticalOrder(root) {
  if (!root) return [];
  const map = new Map();
  const q = [[root, 0]];
  let min = 0, max = 0;
  while (q.length) {
    const [n, c] = q.shift();
    if (!map.has(c)) map.set(c, []);
    map.get(c).push(n.val);
    min = Math.min(min, c);
    max = Math.max(max, c);
    if (n.left) q.push([n.left, c - 1]);
    if (n.right) q.push([n.right, c + 1]);
  }
  const res = [];
  for (let c = min; c <= max; c++) res.push(map.get(c) || []);
  return res;
}
```

- Deep Insights:
  - If ordering by row/val needed, track (row,val) and sort.
  - Column span tracked by min/max.
  - BFS natural for rows.
  - Map from col->values.

## Q74. Count Nodes in Complete Tree

- Concept: Use left/right heights to detect perfect subtrees: nodes = 2^h - 1. Recurse on incomplete side.

```javascript
function countNodes(root) {
  function height(n, goLeft) {
    let d = 0;
    while (n) { d++; n = goLeft ? n.left : n.right; }
    return d;
  }
  function solve(n) {
    if (!n) return 0;
    const lh = height(n, true);
    const rh = height(n, false);
    if (lh === rh) return (1 << lh) - 1;
    return 1 + solve(n.left) + solve(n.right);
  }
  return solve(root);
}
```

- Deep Insights:
  - O(log^2 n) average.
  - Complete tree property critical.
  - Bit shift for 2^h.
  - Avoid full traversal.

## Q75. Binary Tree to DLL

- Concept: Inorder traversal linking nodes as doubly linked list in-place. Keep prev pointer across calls.

```javascript
function treeToDoublyList(root) {
  if (!root) return null;
  let head = null;
  let prev = null;
  (function dfs(n) {
    if (!n) return;
    dfs(n.left);
    if (!head) head = n;
    if (prev) { prev.right = n; n.left = prev; }
    prev = n;
    dfs(n.right);
  })(root);
  // Optionally make circular:
  // head.left = prev; prev.right = head;
  return head;
}
```

- Deep Insights:
  - Inorder preserves sorted order for BST.
  - Make circular if required by spec.
  - In-place links, no extra nodes.
  - Maintain prev across recursion.
