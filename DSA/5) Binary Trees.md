# Binary Trees

## Q87. Binary Tree Traversals (DFS/BFS)

**Problem:** Implement the fundamental binary tree traversal algorithms: Preorder, Inorder, Postorder (DFS), and Level-order (BFS). Understand when to use each traversal based on problem requirements.

**Approach:** 
- **DFS Traversals:** Use recursion or explicit stack. Preorder: root → left → right. Inorder: left → root → right. Postorder: left → right → root.
- **BFS Traversal:** Use queue for level-order traversal.
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
// Input: root = [1, null, 2, 3]
// Output: Preorder: [1, 2, 3], Inorder: [1, 3, 2], Postorder: [3, 2, 1], Level Order: [[1], [2], [3]]
// Explanation: All traversals (recursive and iterative) produce same results

// Input: root = [3, 9, 20, null, null, 15, 7]
// Output: Preorder: [3, 9, 20, 15, 7], Inorder: [9, 3, 15, 20, 7], Postorder: [9, 15, 7, 20, 3], Level Order: [[3], [9, 20], [15, 7]]
// Explanation: All traversals (recursive and iterative) produce same results

// Input: root = [1]
// Output: All outputs: [1] or [[1]] for level order (same for recursive and iterative)

// Input: root = []
// Output: All outputs: [] (same for recursive and iterative)
```

**Time Complexity:** O(n) - Visit each node once  
**Space Complexity:** O(h) for recursive, O(n) worst-case for iterative - h is tree height, n is number of nodes

**Deep Insights:**
- **Recursive vs Iterative:** Recursive uses call stack (O(h) space), iterative uses explicit stack (O(n) worst-case)
- **Preorder Iterative:** Push right then left to maintain root-left-right order
- **Inorder Iterative:** Requires current pointer—go left until null, then process and go right
- **Postorder Iterative:** Use two stacks or reverse preorder approach
- **BFS Level-Order:** Queue-based—process level by level, useful for shortest path problems
- **Use Cases:** Inorder on BST yields sorted values; preorder for copying trees; postorder for deletion; iterative preferred for deep trees
- **Interview Tip:** Know both recursive and iterative versions; explain when to use iterative (deep trees, production); preorder iterative is easiest; inorder requires current pointer understanding
## Q88. Maximum Depth of Binary Tree

**Problem:** Given the root of a binary tree, return its maximum depth. A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

**Approach:** Height is 1 + max(depth(left), depth(right)). Handle null as 0. DFS recursion is simplest.

### Solution 1: Recursive DFS (Optimal)
```javascript
function maxDepth(root) {
  if (!root) return 0;
  return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
}

// Test Cases:
// Input: root = [3, 9, 20, null, null, 15, 7]
// Output: 3

// Input: root = [1, null, 2]
// Output: 2

// Input: root = []
// Output: 0

// Input: root = [1]
// Output: 1
```

**Time Complexity:** O(n) - Visit each node once  
**Space Complexity:** O(h) - Recursion stack depth, h is tree height

### Solution 2: Iterative BFS (Alternative)
```javascript
function maxDepthBFS(root) {
  if (!root) return 0;
  
  let depth = 0;
  const queue = [root];
  
  while (queue.length) {
    const size = queue.length;
    depth++;
    
    for (let i = 0; i < size; i++) {
      const node = queue.shift();
      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }
  }
  
  return depth;
}
```

**Time Complexity:** O(n) - Visit each node once  
**Space Complexity:** O(n) - Queue storage (worst case: last level)

**Deep Insights:**
- **Optimal Approach:** Recursive DFS achieves O(n) time and O(h) space—optimal for this problem
- **Base Case:** Null node returns 0—handles empty tree and leaf nodes
- **Height Formula:** 1 + max(left, right)—adds current node to maximum subtree height
- **Key Insight:** Post-order processing ensures both subtree heights computed before current node
- **Edge Cases:** Empty tree returns 0; single node returns 1; skewed tree has O(n) height
- **Interview Tip:** Explain base case clearly; mention iterative BFS alternative; ask about skewed trees
## Q89. Diameter of Binary Tree

**Problem:** Given the root of a binary tree, return the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root. The length of a path between two nodes is represented by the number of edges between them.

**Approach:** Longest path through any node = leftHeight + rightHeight. Track global best during post-order traversal.

### Solution 1: Post-Order with Global Tracking (Optimal)
```javascript
function diameterOfBinaryTree(root) {
  let maxDiameter = 0;
  
  function height(node) {
    if (!node) return 0;
    
    const leftHeight = height(node.left);
    const rightHeight = height(node.right);
    
    // Update diameter: path through current node
    maxDiameter = Math.max(maxDiameter, leftHeight + rightHeight);
    
    // Return height of subtree
    return 1 + Math.max(leftHeight, rightHeight);
  }
  
  height(root);
  return maxDiameter;
}

// Test Cases:
// Input: root = [1, 2, 3, 4, 5]
// Output: 3
// Explanation: Longest path is [4, 2, 1, 3] or [5, 2, 1, 3] with length 3

// Input: root = [1, 2]
// Output: 1
// Explanation: Longest path is [2, 1] with length 1

// Input: root = [1]
// Output: 0

// Input: root = []
// Output: 0
```

**Time Complexity:** O(n) - Visit each node once  
**Space Complexity:** O(h) - Recursion stack depth, h is tree height

**Deep Insights:**
- **Optimal Approach:** Post-order traversal achieves O(n) time—optimal for this problem
- **Key Insight:** Longest path through any node = leftHeight + rightHeight—track maximum during traversal
- **Post-Order Processing:** Process children before parent—ensures both heights available when computing diameter
- **Path Length in Edges:** Diameter counts edges, not nodes—empty tree and single node both return 0
- **Global Tracking:** Use closure variable to track maximum diameter across all nodes
- **Edge Cases:** Empty tree returns 0; single node returns 0; path may not pass through root
- **Interview Tip:** Explain path length vs depth clearly; emphasize it's different from max depth; mention post-order necessity
## Q90. Balanced Binary Tree

**Problem:** Given a binary tree, determine if it is height-balanced. A height-balanced binary tree is a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

**Approach:** Use -1 as sentinel value to propagate unbalanced status. Check balance at each node during post-order traversal.

### Solution 1: Post-Order with Sentinel (Optimal)
```javascript
function isBalanced(root) {
  function height(node) {
    if (!node) return 0;
    
    const leftHeight = height(node.left);
    if (leftHeight === -1) return -1;  // Propagate unbalanced
    
    const rightHeight = height(node.right);
    if (rightHeight === -1) return -1;  // Propagate unbalanced
    
    // Check if current node is balanced
    if (Math.abs(leftHeight - rightHeight) > 1) return -1;
    
    // Return height if balanced
    return 1 + Math.max(leftHeight, rightHeight);
  }
  
  return height(root) >= 0;
}

// Test Cases:
// Input: root = [3, 9, 20, null, null, 15, 7]
// Output: true

// Input: root = [1, 2, 2, 3, 3, null, null, 4, 4]
// Output: false

// Input: root = []
// Output: true

// Input: root = [1, 2, 2, 3, null, null, 3, 4, null, null, 4]
// Output: false
```

**Time Complexity:** O(n) - Visit each node once  
**Space Complexity:** O(h) - Recursion stack depth, h is tree height

**Deep Insights:**
- **Optimal Approach:** Post-order with sentinel achieves O(n) time—optimal for this problem
- **Sentinel Technique:** Use -1 to indicate unbalanced subtree—propagates early exit
- **Balance Check:** Subtrees must differ by <= 1 AND both subtrees must be balanced
- **Early Exit:** Return -1 immediately when imbalance detected—avoids unnecessary computation
- **Key Insight:** Post-order ensures both subtree heights computed before checking balance
- **Edge Cases:** Empty tree returns true; single node returns true; all nodes must be balanced
- **Interview Tip:** Explain -1 sentinel technique clearly; mention AVL tree context; emphasize early exit benefit
## Q91. Invert Binary Tree

**Problem:** Given the root of a binary tree, invert the tree, and return its root. Inverting a binary tree means swapping the left and right children of each node.

**Approach:** Swap left and right children recursively or iteratively. Mirror the tree structure.

### Solution 1: Recursive (Optimal)
```javascript
function invertTree(root) {
  if (!root) return null;
  
  // Swap left and right
  const temp = root.left;
  root.left = root.right;
  root.right = temp;
  
  // Recursively invert subtrees
  invertTree(root.left);
  invertTree(root.right);
  
  return root;
}

// Test Cases:
// Input: root = [4, 2, 7, 1, 3, 6, 9]
// Output: [4, 7, 2, 9, 6, 3, 1]

// Input: root = [2, 1, 3]
// Output: [2, 3, 1]

// Input: root = []
// Output: []

// Input: root = [1]
// Output: [1]
```

**Time Complexity:** O(n) - Visit each node once  
**Space Complexity:** O(h) - Recursion stack depth, h is tree height

### Solution 2: Iterative BFS (Alternative)
```javascript
function invertTreeIterative(root) {
  if (!root) return null;
  
  const queue = [root];
  while (queue.length) {
    const node = queue.shift();
    
    // Swap children
    const temp = node.left;
    node.left = node.right;
    node.right = temp;
    
    if (node.left) queue.push(node.left);
    if (node.right) queue.push(node.right);
  }
  
  return root;
}
```

**Deep Insights:**
- **Optimal Approach:** Recursive achieves O(n) time and O(h) space—optimal for this problem
- **In-Place Modification:** Swap left and right children—modifies tree structure
- **Key Insight:** Swap before or after recursion—both work, but swap before is clearer
- **Idempotent:** Calling twice restores original tree—invert(invert(tree)) = tree
- **Edge Cases:** Empty tree returns null; single node returns itself; structure preserved after inversion
- **Interview Tip:** Explain swapping clearly; mention iterative BFS alternative; ask about in-place requirements
## Q92. Symmetric Tree

**Problem:** Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

**Approach:** Compare left and right subtrees as mirror images. Check `left.left` vs `right.right` and `left.right` vs `right.left` recursively.

### Solution 1: Recursive Mirror Comparison (Optimal)
```javascript
function isSymmetric(root) {
  if (!root) return true;
  
  function isMirror(left, right) {
    // Both null
    if (!left && !right) return true;
    // One null
    if (!left || !right) return false;
    // Values match and subtrees are mirrors
    return left.val === right.val &&
           isMirror(left.left, right.right) &&
           isMirror(left.right, right.left);
  }
  
  return isMirror(root.left, root.right);
}

// Test Cases:
// Input: root = [1, 2, 2, 3, 4, 4, 3]
// Output: true

// Input: root = [1, 2, 2, null, 3, null, 3]
// Output: false

// Input: root = []
// Output: true

// Input: root = [1]
// Output: true
```

**Time Complexity:** O(n) - Visit each node once  
**Space Complexity:** O(h) - Recursion stack depth, h is tree height

**Deep Insights:**
- **Optimal Approach:** Recursive mirror comparison achieves O(n) time—optimal for this problem
- **Mirror Comparison:** Compare `left.left` with `right.right` and `left.right` with `right.left`
- **Key Insight:** Two nodes are symmetric if their values match and their subtrees are mirrors
- **Base Cases:** Both null returns true; one null returns false; values must match
- **Edge Cases:** Empty tree returns true; single node returns true; all nodes must be symmetric
- **Interview Tip:** Explain mirror comparison clearly; mention it's different from identical tree check
## Q93. Path Sum

**Problem:** Given the root of a binary tree and an integer `targetSum`, return `true` if the tree has a root-to-leaf path such that adding up all the values along the path equals `targetSum`. A leaf is a node with no children.

**Approach:** Subtract current node value from target as we traverse. Check if leaf node and remaining sum equals 0.

### Solution 1: Recursive DFS (Optimal)
```javascript
function hasPathSum(root, targetSum) {
  if (!root) return false;
  
  // Leaf node: check if sum matches
  if (!root.left && !root.right) {
    return root.val === targetSum;
  }
  
  // Subtract current value and recurse
  const remaining = targetSum - root.val;
  return hasPathSum(root.left, remaining) || hasPathSum(root.right, remaining);
}

// Test Cases:
// Input: root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1], targetSum = 22
// Output: true
// Explanation: Path 5 -> 4 -> 11 -> 2 has sum = 22

// Input: root = [1, 2, 3], targetSum = 5
// Output: false

// Input: root = [], targetSum = 0
// Output: false

// Input: root = [1, 2], targetSum = 1
// Output: false
```

**Time Complexity:** O(n) - Visit each node once  
**Space Complexity:** O(h) - Recursion stack depth, h is tree height

**Deep Insights:**
- **Optimal Approach:** Recursive DFS achieves O(n) time—optimal for this problem
- **Leaf Requirement:** Path must end at a leaf node—not just any node with matching sum
- **Backtracking Sum:** Subtract current value as we go—reduces state passing
- **Key Insight:** Check leaf node when `!left && !right`—must have exact sum match
- **Early Return:** Return true immediately when path found—no need to check other paths
- **Edge Cases:** Empty tree returns false; single node is leaf; negative values allowed
- **Interview Tip:** Explain leaf requirement clearly; mention negative values; ask about finding all paths vs any path
## Q94. Lowest Common Ancestor of a Binary Tree

**Problem:** Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree. The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself).

**Approach:** If both nodes are in different subtrees, current node is LCA. Otherwise, pass non-null child up. Post-order returns match or null.

### Solution 1: Post-Order Traversal (Optimal)
```javascript
function lowestCommonAncestor(root, p, q) {
  // Base case: found node or null
  if (!root || root === p || root === q) return root;
  
  // Search in left and right subtrees
  const left = lowestCommonAncestor(root.left, p, q);
  const right = lowestCommonAncestor(root.right, p, q);
  
  // If both found in different subtrees, current is LCA
  if (left && right) return root;
  
  // Otherwise, pass up the non-null result
  return left || right;
}

// Test Cases:
// Input: root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 1
// Output: 3
// Explanation: LCA of nodes 5 and 1 is 3

// Input: root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 4
// Output: 5
// Explanation: LCA of nodes 5 and 4 is 5 (ancestor of itself)

// Input: root = [1, 2], p = 1, q = 2
// Output: 1

// Input: root = [1], p = 1, q = 1
// Output: 1
```

**Time Complexity:** O(n) - Visit each node once in worst case  
**Space Complexity:** O(h) - Recursion stack depth, h is tree height

**Deep Insights:**
- **Optimal Approach:** Post-order traversal achieves O(n) time—optimal for this problem
- **Base Case:** Return node if it's `p` or `q`—handles case where one node is ancestor of other
- **LCA Detection:** If both left and right return non-null, current node is LCA
- **Key Insight:** Post-order ensures both subtrees processed before checking—enables LCA detection
- **Propagation:** Pass up non-null result—indicates subtree contains target node
- **Edge Cases:** One node is ancestor of other; both nodes in same subtree; nodes don't exist (assumed to exist)
- **Interview Tip:** Explain post-order logic clearly; mention BST variant is simpler (can use value comparison); ask about node existence guarantee
## Q95. Serialize and Deserialize Binary Tree

**Problem:** Design an algorithm to serialize and deserialize a binary tree. Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment. Design an algorithm to serialize and deserialize a binary tree.

**Approach:** Use preorder traversal with null markers. Join values with delimiter for serialization. Rebuild tree using index counter during deserialization.

### Solution 1: Preorder with Null Markers (Optimal)
```javascript
function serialize(root) {
  const result = [];
  
  function preorder(node) {
    if (!node) {
      result.push('#');
      return;
    }
    result.push(node.val);
    preorder(node.left);
    preorder(node.right);
  }
  
  preorder(root);
  return result.join(',');
}

function deserialize(data) {
  const values = data.split(',');
  let index = 0;
  
  function build() {
    if (values[index] === '#') {
      index++;
      return null;
    }
    
    const node = new TreeNode(parseInt(values[index]));
    index++;
    node.left = build();
    node.right = build();
    
    return node;
  }
  
  return build();
}

// Test Cases:
//
// Example 1 (serialize):
// Input: root = [1, 2, 3, null, null, 4, 5]
// Output: "1,2,#,#,3,4,#,#,5,#,#"
//
// Example 1 (deserialize):
// Input: data = "1,2,#,#,3,4,#,#,5,#,#"
// Output: root = [1, 2, 3, null, null, 4, 5]

// Input: root = []
// serialize Output: "#"
// deserialize Output: null

// Input: root = [1]
// serialize Output: "1,#,#"
// deserialize Output: [1]
```

**Time Complexity:** O(n) - Visit each node once for both serialize and deserialize  
**Space Complexity:** O(n) - Serialized string and recursion stack

**Deep Insights:**
- **Optimal Approach:** Preorder with null markers achieves O(n) time—optimal for this problem
- **Preorder Choice:** Preorder naturally preserves tree structure—easy to reconstruct
- **Null Markers:** Use sentinel (e.g., '#') to represent null nodes—enables accurate reconstruction
- **Index Counter:** Use global index counter during deserialization—tracks current position
- **Key Insight:** Preorder traversal order matches deserialization order—enables recursive rebuild
- **Edge Cases:** Empty tree serializes to "#"; single node requires null markers for children
- **Interview Tip:** Explain serialization format clearly; mention BFS alternative (level-order); ask about delimiter choice
## Q96. Binary Tree Level Order Traversal

**Problem:** Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

**Approach:** Use BFS with queue. Process nodes level by level, collecting values for each level.

### Solution 1: BFS Queue (Optimal)
```javascript
function levelOrder(root) {
  const result = [];
  if (!root) return result;
  
  const queue = [root];
  
  while (queue.length) {
    const levelSize = queue.length;
    const level = [];
    
    // Process all nodes at current level
    for (let i = 0; i < levelSize; i++) {
      const node = queue.shift();
      level.push(node.val);
      
      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }
    
    result.push(level);
  }
  
  return result;
}

// Test Cases:
// Input: root = [3, 9, 20, null, null, 15, 7]
// Output: [[3], [9, 20], [15, 7]]

// Input: root = [1]
// Output: [[1]]

// Input: root = []
// Output: []

// Input: root = [1, 2, 3, 4, 5, 6, 7]
// Output: [[1], [2, 3], [4, 5, 6, 7]]
```

**Time Complexity:** O(n) - Visit each node once  
**Space Complexity:** O(w) - Queue stores nodes at widest level, w is maximum width

**Deep Insights:**
- **Optimal Approach:** BFS queue achieves O(n) time—optimal for this problem
- **Level-by-Level Processing:** Process all nodes at current level before moving to next—ensures correct order
- **Queue Management:** Use `queue.length` snapshot to process exact level size—avoids mixing levels
- **Key Insight:** BFS naturally processes levels in order—no need for explicit level tracking
- **Space Complexity:** O(w) where w is maximum width—stores nodes at widest level
- **Edge Cases:** Empty tree returns empty array; single node returns single level; all levels collected
- **Interview Tip:** Explain BFS clearly; mention space complexity O(w); ask about flat vs nested output format
## Q97. Binary Tree Zigzag Level Order Traversal

**Problem:** Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

**Approach:** Use BFS to process levels. Reverse level array for odd-indexed levels (1-indexed) or use a flag to alternate direction.

### Solution 1: BFS with Level Reversal (Optimal)
```javascript
function zigzagLevelOrder(root) {
  const result = [];
  if (!root) return result;
  
  const queue = [root];
  let reverse = false;
  
  while (queue.length) {
    const levelSize = queue.length;
    const level = [];
    
    // Process all nodes at current level
    for (let i = 0; i < levelSize; i++) {
      const node = queue.shift();
      level.push(node.val);
      
      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }
    
    // Reverse level for zigzag pattern
    if (reverse) {
      level.reverse();
    }
    
    result.push(level);
    reverse = !reverse;  // Toggle direction
  }
  
  return result;
}

// Test Cases:
// Input: root = [3, 9, 20, null, null, 15, 7]
// Output: [[3], [20, 9], [15, 7]]

// Input: root = [1]
// Output: [[1]]

// Input: root = []
// Output: []

// Input: root = [1, 2, 3, 4, null, null, 5]
// Output: [[1], [3, 2], [4, 5]]
```

**Time Complexity:** O(n) - Visit each node once  
**Space Complexity:** O(w) - Queue stores nodes at widest level, w is maximum width

**Deep Insights:**
- **Optimal Approach:** BFS with level reversal achieves O(n) time—optimal for this problem
- **Zigzag Pattern:** Alternate direction per level—reverse array for odd levels (0-indexed)
- **Key Insight:** Process level normally, then reverse if needed—simpler than changing insertion order
- **Flag Toggle:** Use boolean flag to track direction—alternates each level
- **Edge Cases:** Empty tree returns empty array; single level doesn't need reversal; all levels handled
- **Interview Tip:** Explain BFS with reversal clearly; mention alternative (insert from front/back based on level)
## Q98. Binary Tree Right Side View

**Problem:** Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

**Approach:** Use BFS to process levels. Capture the last node (rightmost) at each level for right view, or first node (leftmost) for left view.

### Solution 1: BFS Level Processing (Optimal)
```javascript
function rightSideView(root) {
  const result = [];
  if (!root) return result;
  
  const queue = [root];
  
  while (queue.length) {
    const levelSize = queue.length;
    
    // Process all nodes at current level
    for (let i = 0; i < levelSize; i++) {
      const node = queue.shift();
      
      // Capture rightmost node (last in level)
      if (i === levelSize - 1) {
        result.push(node.val);
      }
      
      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }
  }
  
  return result;
}

// Left Side View variant: capture first node (i === 0)
function leftSideView(root) {
  const result = [];
  if (!root) return result;
  
  const queue = [root];
  
  while (queue.length) {
    const levelSize = queue.length;
    
    for (let i = 0; i < levelSize; i++) {
      const node = queue.shift();
      
      // Capture leftmost node (first in level)
      if (i === 0) {
        result.push(node.val);
      }
      
      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }
  }
  
  return result;
}

// Test Cases:
// Input: root = [1, 2, 3, null, 5, null, 4]
// Output: [1, 3, 4]

// Input: root = [1, null, 3]
// Output: [1, 3]

// Input: root = []
// Output: []

// Input: root = [1, 2]
// Output: [1, 2]
//
// Note: leftSideView (variant - take i === 0):
// Input: root = [1, 2, 3, null, 5, null, 4]
// Output: [1, 2, 5]
```

**Time Complexity:** O(n) - Visit each node once  
**Space Complexity:** O(w) - Queue stores nodes at widest level, w is maximum width

**Deep Insights:**
- **Optimal Approach:** BFS level processing achieves O(n) time—optimal for this problem
- **Right View:** Capture last node (i === levelSize - 1) at each level—rightmost visible node
- **Left View:** Capture first node (i === 0) at each level—leftmost visible node
- **Key Insight:** BFS naturally processes levels—easy to capture first/last node per level
- **Alternative:** DFS variant tracks maximum depth seen—records first node at each depth
- **Edge Cases:** Empty tree returns empty array; single node returns single value; all levels captured
- **Interview Tip:** Explain left vs right view clearly; mention DFS alternative; ask about output format
## Q99. Boundary Traversal of Binary Tree

**Problem:** Given a binary tree, return the boundary traversal. The boundary includes: root (if not leaf), left boundary (excluding leaves), all leaves, and right boundary (excluding leaves, in reverse order).

**Approach:** Process in four parts: root (if not leaf), left boundary (excluding leaves), all leaves, right boundary (excluding leaves, reversed).

### Solution 1: Four-Part Boundary (Optimal)
```javascript
function boundaryOfBinaryTree(root) {
  if (!root) return [];

  function isLeaf(node) {
    return node && !node.left && !node.right;
  }

  const result = [];

  // 1. Add root (only if not leaf)
  if (!isLeaf(root)) {
    result.push(root.val);
  }

  // 2. Add left boundary (excluding leaves)
  function addLeftBoundary(node) {
    while (node) {
      if (!isLeaf(node)) {
        result.push(node.val);
      }
      node = node.left ? node.left : node.right;
    }
  }

  // 3. Add all leaf nodes
  function addLeaves(node) {
    if (!node) return;
    if (isLeaf(node)) {
      result.push(node.val);
      return;
    }
    addLeaves(node.left);
    addLeaves(node.right);
  }

  // 4. Add right boundary (excluding leaves, bottom → top)
  function addRightBoundary(node) {
    const stack = [];
    while (node) {
      if (!isLeaf(node)) {
        stack.push(node.val);
      }
      node = node.right ? node.right : node.left;
    }
    // Reverse by popping from stack
    while (stack.length) {
      result.push(stack.pop());
    }
  }

  addLeftBoundary(root.left);
  addLeaves(root);
  addRightBoundary(root.right);

  return result;
}

// Test Cases:
// Input: root = [1, null, 2, 3, 4]
// Output: [1, 3, 4, 2]

// Input: root = [1, 2, 3, 4, 5, 6, null, null, null, 7, 8, 9, 10]
// Output: [1, 2, 4, 7, 8, 9, 10, 6, 3]

// Input: root = [1]
// Output: [1]

// Input: root = [1, 2, 3]
// Output: [1, 2, 3]
```

**Time Complexity:** O(n) - Visit each node once  
**Space Complexity:** O(h) - Recursion stack for leaves, h is tree height

**Deep Insights:**
- **Optimal Approach:** Four-part boundary processing achieves O(n) time—optimal for this problem
- **Boundary Parts:** Root → left boundary → leaves → right boundary (reversed)
- **Key Insight:** Exclude leaves from left/right boundaries—leaves added separately to avoid duplicates
- **Right Boundary Reversal:** Use stack to reverse right boundary—bottom-to-top order
- **Edge Cases:** Single node returns itself; root is leaf if single node; all parts handled correctly
- **Interview Tip:** Explain four-part boundary clearly; emphasize duplicate avoidance; mention order matters
## Q100. Iterative DFS Traversals (Pre/In/Post Order)

**Problem:** Implement iterative versions of preorder, inorder, and postorder traversals without using recursion.

**Approach:** Use explicit stack to simulate recursion. Different orderings require different stack manipulation strategies.

### Solution 1: Iterative Inorder (Optimal)
```javascript
function inorderIterative(root) {
  const result = [];
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
    result.push(current.val);
    
    // Go right
    current = current.right;
  }
  
  return result;
}

// Test Cases:
// Input: root = [1, null, 2, 3]
// Output: [1, 3, 2]

// Input: root = []
// Output: []

// Input: root = [1]
// Output: [1]

// Input: root = [1, 2]
// Output: [2, 1]

// Input: root = [1, null, 2]
// Output: [1, 2]
//
// Note: For preorder, push right then left before pushing node.
//   For postorder, use two stacks or tagged nodes.
```

### Solution 2: Iterative Preorder
```javascript
function preorderIterative(root) {
  if (!root) return [];
  
  const result = [];
  const stack = [root];
  
  while (stack.length) {
    const node = stack.pop();
    result.push(node.val);
    
    // Push right first, then left (stack is LIFO)
    if (node.right) stack.push(node.right);
    if (node.left) stack.push(node.left);
  }
  
  return result;
}
```

### Solution 3: Iterative Postorder
```javascript
function postorderIterative(root) {
  if (!root) return [];
  
  const result = [];
  const stack1 = [root];
  const stack2 = [];
  
  while (stack1.length) {
    const node = stack1.pop();
    stack2.push(node);
    
    if (node.left) stack1.push(node.left);
    if (node.right) stack1.push(node.right);
  }
  
  while (stack2.length) {
    result.push(stack2.pop().val);
  }
  
  return result;
}
```

**Time Complexity:** O(n) - Visit each node once  
**Space Complexity:** O(h) - Stack stores nodes along path, h is tree height

**Deep Insights:**
- **Optimal Approach:** Iterative traversals achieve O(n) time—optimal for avoiding recursion
- **Inorder Pattern:** Go left until null, process, then go right—requires current pointer
- **Preorder Pattern:** Push right then left—stack's LIFO ensures left processed first
- **Postorder Pattern:** Use two stacks—process in reverse order
- **Key Insight:** Explicit stack avoids recursion stack overflow—safer for deep trees
- **Edge Cases:** Empty tree returns empty array; all traversals handle null correctly
- **Interview Tip:** Explain iterative approach clearly; emphasize when to use (deep trees, production); mention all three variants
## Q101. Construct Binary Tree from Preorder and Inorder Traversal

**Problem:** Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return the binary tree.

**Approach:** Preorder gives root. Use root to split inorder into left and right subtrees. Recurse for subtrees. Use index map for O(1) lookups.

### Solution 1: Recursive with Index Map (Optimal)
```javascript
function buildTree(preorder, inorder) {
  // Create map: value -> index in inorder
  const map = new Map();
  for (let i = 0; i < inorder.length; i++) {
    map.set(inorder[i], i);
  }
  
  let preIndex = 0;
  
  function build(left, right) {
    if (left > right) return null;
    
    // Root is first element in preorder
    const rootVal = preorder[preIndex++];
    const root = new TreeNode(rootVal);
    
    // Find root position in inorder
    const mid = map.get(rootVal);
    
    // Build left and right subtrees
    root.left = build(left, mid - 1);
    root.right = build(mid + 1, right);
    
    return root;
  }
  
  return build(0, inorder.length - 1);
}

// Test Cases:
// Input: preorder = [3, 9, 20, 15, 7], inorder = [9, 3, 15, 20, 7]
// Output: [3, 9, 20, null, null, 15, 7]

// Input: preorder = [-1], inorder = [-1]
// Output: [-1]

// Input: preorder = [1, 2], inorder = [2, 1]
// Output: [1, 2]

// Input: preorder = [1, 2, 3], inorder = [2, 1, 3]
// Output: [1, 2, 3]
```

**Time Complexity:** O(n) - Visit each node once during construction  
**Space Complexity:** O(n) - Hash map stores inorder positions, recursion stack O(h)

**Deep Insights:**
- **Optimal Approach:** Recursive with index map achieves O(n) time—optimal for this problem
- **Root Identification:** First element in preorder is always root—use to split inorder
- **Index Map:** O(1) lookup for root position in inorder—avoids O(n) search
- **Key Insight:** Inorder split by root gives left and right subtrees—enables recursive construction
- **Preorder Index:** Increment preIndex for each recursive call—ensures correct root selection
- **Edge Cases:** Empty arrays return null; single element returns single node; unique values assumed
- **Interview Tip:** Explain index map clearly; mention uniqueness requirement; ask about inorder+postorder variant
## Q102. Morris Inorder Traversal

**Problem:** Given the root of a binary tree, return the inorder traversal of its nodes' values using Morris traversal (O(1) space, no recursion or stack).

**Approach:** Thread right pointers temporarily to create links back to ancestors. Process nodes and restore tree structure after visiting.

### Solution 1: Morris Threading (Optimal Space)
```javascript
function morrisInorder(root) {
  const result = [];
  let current = root;
  
  while (current) {
    if (!current.left) {
      // No left subtree, visit current and go right
      result.push(current.val);
      current = current.right;
    } else {
      // Find inorder predecessor (rightmost node in left subtree)
      let predecessor = current.left;
      while (predecessor.right && predecessor.right !== current) {
        predecessor = predecessor.right;
      }
      
      if (!predecessor.right) {
        // Create thread and go left
        predecessor.right = current;
        current = current.left;
      } else {
        // Thread exists, restore and visit current
        predecessor.right = null;
        result.push(current.val);
        current = current.right;
      }
    }
  }
  
  return result;
}

// Test Cases:
// Input: root = [1, null, 2, 3]
// Output: [1, 3, 2]

// Input: root = []
// Output: []

// Input: root = [1]
// Output: [1]

// Input: root = [4, 2, 5, 1, 3]
// Output: [2, 4, 1, 5, 3]
//
// Note: O(1) space complexity, tree structure is restored after traversal
```

**Time Complexity:** O(n) - Visit each node at most twice (once to create thread, once to remove)  
**Space Complexity:** O(1) - Only uses existing tree pointers, no extra space

**Deep Insights:**
- **Optimal Space:** Morris traversal achieves O(1) space—optimal for space-constrained scenarios
- **Threading Technique:** Temporarily link rightmost node in left subtree to current—enables backtracking
- **Two Passes:** First pass creates thread, second pass removes thread and processes node
- **Key Insight:** Tree structure is restored after traversal—no permanent modification
- **Time Trade-off:** O(n) time (each node visited at most twice) for O(1) space
- **Edge Cases:** Empty tree returns empty array; single node handled correctly; tree fully restored
- **Interview Tip:** Explain threading technique clearly; emphasize tree restoration; mention this is advanced technique
## Q103. Binary Tree Maximum Path Sum

**Problem:** A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root. The path sum of a path is the sum of the node values in the path. Given the root of a binary tree, return the maximum path sum of any non-empty path.

**Approach:** Path can bend at any node. For each node, compute maximum path sum with node as highest point. Use post-order traversal. Return upward only single-branch contribution.

### Solution 1: Post-Order with Global Tracking (Optimal)
```javascript
function maxPathSum(root) {
  let maxSum = -Infinity;
  
  function dfs(node) {
    if (!node) return 0;
    
    // Only take positive contributions from children
    const left = Math.max(dfs(node.left), 0);
    const right = Math.max(dfs(node.right), 0);
    
    // Compute max path using this node as highest point (bending path)
    const pathSum = node.val + left + right;
    
    // Update global maximum
    maxSum = Math.max(maxSum, pathSum);
    
    // Return best single-branch path upward (for parent)
    return node.val + Math.max(left, right);
  }
  
  dfs(root);
  return maxSum;
}

// Test Cases:
// Input: root = [1, 2, 3]
// Output: 6
// Explanation: Path 2 -> 1 -> 3 has sum = 6

// Input: root = [-10, 9, 20, null, null, 15, 7]
// Output: 42
// Explanation: Path 15 -> 20 -> 7 has sum = 42

// Input: root = [-3]
// Output: -3

// Input: root = [2, -1]
// Output: 2
```

**Time Complexity:** O(n) - Visit each node once  
**Space Complexity:** O(h) - Recursion stack depth, h is tree height

**Deep Insights:**
- **Optimal Approach:** Post-order traversal achieves O(n) time—optimal for this problem
- **Path Bending:** Path can bend at any node—combine left + node + right for maximum
- **Positive Clamping:** Only take positive contributions from children—clamp negative paths to 0
- **Key Insight:** Two calculations: path through node (for global max) and single branch upward (for parent)
- **Global Tracking:** Use closure variable to track maximum across all nodes
- **Edge Cases:** All negative values handled; single node returns its value; path doesn't need to pass through root
- **Interview Tip:** Explain path bending clearly; emphasize negative handling with Math.max(0, ...); mention two calculations
## Q104. Vertical Order Traversal of a Binary Tree

**Problem:** Given the root of a binary tree, calculate the vertical order traversal of the binary tree. For each node at position `(row, col)`, its left and right children will be at positions `(row + 1, col - 1)` and `(row + 1, col + 1)` respectively. The root of the tree is at `(0, 0)`. The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

**Approach:** Use BFS to assign column and row indices. Sort nodes by column, then row, then value. Group by column.

### Solution 1: BFS with Sorting (Optimal)
```javascript
function verticalTraversal(root) {
  if (!root) return [];
  
  const nodes = [];  // Store [col, row, val]
  const queue = [[root, 0, 0]];  // [node, col, row]
  
  // BFS to collect all nodes with positions
  while (queue.length) {
    const [node, col, row] = queue.shift();
    nodes.push([col, row, node.val]);
    
    if (node.left) queue.push([node.left, col - 1, row + 1]);
    if (node.right) queue.push([node.right, col + 1, row + 1]);
  }
  
  // Sort by: column asc, row asc, value asc
  nodes.sort((a, b) => {
    if (a[0] !== b[0]) return a[0] - b[0];  // Column
    if (a[1] !== b[1]) return a[1] - b[1];  // Row
    return a[2] - b[2];  // Value
  });
  
  // Group by column
  const map = new Map();
  for (const [col, row, val] of nodes) {
    if (!map.has(col)) map.set(col, []);
    map.get(col).push(val);
  }
  
  return Array.from(map.values());
}

// Test Cases:
// Input: root = [3, 9, 20, null, null, 15, 7]
// Output: [[9], [3, 15], [20], [7]]

// Input: root = [3, 9, 8, 4, 0, 1, 7]
// Output: [[4], [9], [3, 0, 1], [8], [7]]

// Input: root = [1]
// Output: [[1]]

// Input: root = []
// Output: []
```

**Time Complexity:** O(n log n) - Visit each node once, then sort n nodes  
**Space Complexity:** O(n) - Store all nodes with positions, map stores column groups

**Deep Insights:**
- **Optimal Approach:** BFS with sorting achieves correct ordering—optimal for this problem
- **Position Assignment:** BFS assigns row indices naturally—increment row for each level
- **Sorting Requirement:** Sort by column → row → value—handles nodes at same position
- **Key Insight:** Multiple nodes can share same (row, col)—must sort by value
- **Grouping:** Group sorted nodes by column—creates final vertical order
- **Edge Cases:** Empty tree returns empty array; single node returns single column; overlapping nodes handled
- **Interview Tip:** Explain sorting requirement clearly; emphasize why sorting is needed (same position); mention ordering rules
## Q105. Count Complete Tree Nodes

**Problem:** Given the root of a complete binary tree, return the number of the nodes in the tree. A complete binary tree has every level, except possibly the last, completely filled, and all nodes in the last level are as far left as possible.

**Approach:** Use left/right heights to detect perfect subtrees. If heights equal, use formula 2^h - 1. Otherwise, recurse on incomplete side.

### Solution 1: Height-Based Optimization (Optimal)
```javascript
function countNodes(root) {
  if (!root) return 0;

  function leftHeight(node) {
    let height = 0;
    while (node) {
      height++;
      node = node.left;
    }
    return height;
  }

  function rightHeight(node) {
    let height = 0;
    while (node) {
      height++;
      node = node.right;
    }
    return height;
  }

  const leftH = leftHeight(root);
  const rightH = rightHeight(root);

  // If both heights are equal, it's a perfect tree
  if (leftH === rightH) {
    return (1 << leftH) - 1;  // 2^h - 1 using bit shift
  }

  // Otherwise, count nodes recursively
  return 1 + countNodes(root.left) + countNodes(root.right);
}

// Test Cases:
// Input: root = [1, 2, 3, 4, 5, 6]
// Output: 6

// Input: root = []
// Output: 0

// Input: root = [1]
// Output: 1

// Input: root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
// Output: 12
//
// Note: Assumes complete binary tree for optimization
```

**Time Complexity:** O(log² n) - Average case for complete tree, O(n) worst case for skewed tree  
**Space Complexity:** O(log n) - Recursion stack depth for complete tree

**Deep Insights:**
- **Optimal Approach:** Height-based optimization achieves O(log² n) average—optimal for complete trees
- **Perfect Tree Detection:** If left and right heights equal, tree is perfect—use formula 2^h - 1
- **Bit Shift Optimization:** Use `1 << h` for 2^h—faster than Math.pow(2, h)
- **Key Insight:** Only recurse on incomplete side—most of tree uses O(1) formula
- **Complete Tree Property:** Assumes complete binary tree—allows height-based optimization
- **Edge Cases:** Empty tree returns 0; single node returns 1; skewed tree falls back to O(n)
- **Interview Tip:** Explain perfect subtree detection clearly; emphasize bit shift optimization; mention complete vs full tree difference
## Q106. Convert Binary Search Tree to Sorted Doubly Linked List

**Problem:** Convert a Binary Search Tree to a sorted Doubly Linked List in place. The left and right pointers in nodes are to be used as previous and next pointers respectively in converted DLL. The order of nodes in DLL must be same as Inorder of the given Binary Search Tree.

**Approach:** Use inorder traversal to link nodes as doubly linked list in-place. Keep prev pointer across recursive calls.

### Solution 1: Inorder with Prev Pointer (Optimal)
```javascript
function treeToDoublyList(root) {
  if (!root) return null;
  
  let head = null;
  let prev = null;
  
  function inorder(node) {
    if (!node) return;
    
    inorder(node.left);
    
    // Set head to first node (leftmost)
    if (!head) {
      head = node;
    }
    
    // Link previous node to current
    if (prev) {
      prev.right = node;
      node.left = prev;
    }
    
    prev = node;
    inorder(node.right);
  }
  
  inorder(root);
  
  // Make circular (optional)
  if (head && prev) {
    head.left = prev;
    prev.right = head;
  }
  
  return head;
}

// Test Cases:
// Input: root = [4, 2, 5, 1, 3]
// Output: Doubly linked list: 1 <-> 2 <-> 3 <-> 4 <-> 5 (inorder order)

// Input: root = [2, 1, 3]
// Output: Doubly linked list: 1 <-> 2 <-> 3

// Input: root = [1]
// Output: Doubly linked list with single node

// Input: root = []
// Output: null
//
// Note: For BST, this creates a sorted doubly linked list.
//   If circular required, uncomment the last two lines.
```

**Time Complexity:** O(n) - Visit each node once during inorder traversal  
**Space Complexity:** O(h) - Recursion stack depth, h is tree height

**Deep Insights:**
- **Optimal Approach:** Inorder traversal achieves sorted order—optimal for BST to DLL conversion
- **In-Place Linking:** Use existing left/right pointers as prev/next—no extra nodes created
- **Prev Pointer:** Maintain prev across recursion—enables linking current to previous node
- **Head Tracking:** First node (leftmost) becomes head—preserves sorted order
- **Circular Variant:** Link head and tail to make circular—optional based on requirements
- **Edge Cases:** Empty tree returns null; single node returns itself; tree structure preserved conceptually
- **Interview Tip:** Explain inorder linking clearly; emphasize in-place transformation; mention circular variant

## Q107. Same Tree

**Problem:** Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not. Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

**Approach:** Check if two binary trees are identical using recursive comparison. Compare values and structure recursively.

### Solution 1: Recursive Comparison (Optimal)
```javascript
function isSameTree(p, q) {
  // Both null
  if (!p && !q) return true;
  
  // One null
  if (!p || !q) return false;
  
  // Values different
  if (p.val !== q.val) return false;
  
  // Recursively check subtrees
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

**Deep Insights:**
- **Optimal Approach:** Recursive comparison achieves O(min(m,n)) time—optimal for this problem
- **Base Cases:** Both null returns true; one null returns false; values different returns false
- **Recursive Case:** Check both left and right subtrees—all must match
- **Key Insight:** Early return on any mismatch—no need to check further
- **Edge Cases:** Both empty trees return true; one empty returns false; structure and values must match
- **Interview Tip:** Explain recursive structure clearly; emphasize base cases; mention early return optimization

## Q108. Construct Binary Tree from Inorder and Postorder Traversal

**Problem:** Given two integer arrays `inorder` and `postorder` where `inorder` is the inorder traversal of a binary tree and `postorder` is the postorder traversal of the same tree, construct and return the binary tree.

**Approach:** Postorder last element is root. Find root in inorder to split into left and right subtrees. Recurse for subtrees.

### Solution 1: Recursive with Index Map (Optimal)
```javascript
function buildTree(inorder, postorder) {
  // Create map: value -> index in inorder
  const map = new Map();
  for (let i = 0; i < inorder.length; i++) {
    map.set(inorder[i], i);
  }
  
  let postIndex = postorder.length - 1;
  
  function build(left, right) {
    if (left > right) return null;
    
    // Root is last element in postorder
    const rootVal = postorder[postIndex--];
    const root = new TreeNode(rootVal);
    
    // Find root position in inorder
    const mid = map.get(rootVal);
    
    // Build right subtree first (postorder processes right before left)
    root.right = build(mid + 1, right);
    root.left = build(left, mid - 1);
    
    return root;
  }
  
  return build(0, inorder.length - 1);
}

// Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
// Output: [3,9,20,null,null,15,7]
// Explanation: Root 3, left [9], right [15,20,7]

// Input: inorder = [-1], postorder = [-1]
// Output: [-1]
// Explanation: Single node tree
```

**Time Complexity:** O(n) - Visit each node once during construction  
**Space Complexity:** O(n) - Hash map stores inorder positions, recursion stack O(h)

**Deep Insights:**
- **Optimal Approach:** Recursive with index map achieves O(n) time—optimal for this problem
- **Root Identification:** Last element in postorder is always root—use to split inorder
- **Index Map:** O(1) lookup for root position in inorder—avoids O(n) search
- **Build Order:** Build right subtree first—postorder processes right before left
- **Key Insight:** Decrement postIndex for each recursive call—ensures correct root selection
- **Edge Cases:** Empty arrays return null; single element returns single node; unique values assumed
- **Interview Tip:** Explain index map optimization clearly; mention build order (right then left); ask about preorder variant

## Q109. Populating Next Right Pointers in Each Node II

**Problem:** Given a binary tree, populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to `NULL`. Initially, all next pointers are set to `NULL`.

**Approach:** Use level-by-level traversal with dummy node. Connect children of current level using next pointers from previous level.

### Solution 1: Level-by-Level with Dummy Node (Optimal)
```javascript
function connect(root) {
  if (!root) return root;
  
  let head = root;  // Head of current level
  
  while (head) {
    const dummy = new Node(0);  // Dummy node for next level
    let current = dummy;
    
    // Connect children of current level
    while (head) {
      if (head.left) {
        current.next = head.left;
        current = current.next;
      }
      if (head.right) {
        current.next = head.right;
        current = current.next;
      }
      head = head.next;  // Move to next node in current level
    }
    
    head = dummy.next;  // Move to next level
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
**Space Complexity:** O(1) - Constant extra space (only dummy node)

**Deep Insights:**
- **Optimal Approach:** Level-by-level with dummy node achieves O(1) space—optimal for this problem
- **Dummy Node Technique:** Use dummy to simplify connection logic—eliminates edge cases
- **Level Traversal:** Use next pointers to traverse current level—no queue needed
- **Key Insight:** Connect children of current level while traversing—builds next level structure
- **Space Efficiency:** O(1) space by using existing next pointers—better than BFS queue
- **Edge Cases:** Empty tree returns null; single node returns unchanged; all levels connected
- **Interview Tip:** Explain dummy node technique clearly; emphasize O(1) space advantage; compare with BFS approach

## Q110. Flatten Binary Tree to Linked List

**Problem:** Given the root of a binary tree, flatten the tree into a "linked list". The "linked list" should use the same `TreeNode` class where the `right` child pointer points to the next node in the list and the `left` child pointer is always `null`. The "linked list" should be in the same order as a pre-order traversal of the binary tree.

**Approach:** Use postorder traversal (right, left, root). Link nodes in reverse order, then reverse the links.

### Solution 1: Postorder Traversal (Optimal)
```javascript
function flatten(root) {
  if (!root) return;
  
  let prev = null;
  
  function postorder(node) {
    if (!node) return;
    
    // Process right first, then left (reverse order)
    postorder(node.right);
    postorder(node.left);
    
    // Link current node to previous
    node.right = prev;
    node.left = null;
    prev = node;
  }
  
  postorder(root);
}

// Input: root = [1,2,5,3,4,null,6]
// Output: [1,null,2,null,3,null,4,null,5,null,6]
// Explanation: Flatten to linked list

// Input: root = []
// Output: []
```

**Time Complexity:** O(n) - Visit each node once  
**Space Complexity:** O(h) - Recursion stack depth, h is tree height

**Deep Insights:**
- **Optimal Approach:** Postorder traversal achieves O(n) time—optimal for this problem
- **Reverse Processing:** Process right, then left, then root—builds list from end to start
- **Prev Pointer:** Maintain prev across recursion—enables linking current to previous
- **In-Place Transformation:** Use existing nodes—no extra space for new nodes
- **Key Insight:** Postorder ensures children processed before parent—enables correct linking
- **Edge Cases:** Empty tree does nothing; single node links correctly; all nodes flattened
- **Interview Tip:** Explain postorder approach clearly; emphasize in-place transformation; mention reverse order processing

## Q111. Sum Root to Leaf Numbers

**Problem:** You are given the root of a binary tree containing digits from `0` to `9` only. Each root-to-leaf path in the tree represents a number. Return the total sum of all root-to-leaf numbers.

**Approach:** Use DFS with path sum tracking. Multiply by 10 and add current value as we traverse. Accumulate sum at leaf nodes.

### Solution 1: DFS with Path Sum (Optimal)
```javascript
function sumNumbers(root) {
  let totalSum = 0;
  
  function dfs(node, pathSum) {
    if (!node) return;
    
    // Build number: multiply by 10 and add current value
    pathSum = pathSum * 10 + node.val;
    
    // Leaf node: add to total sum
    if (!node.left && !node.right) {
      totalSum += pathSum;
      return;
    }
    
    // Recurse on children
    dfs(node.left, pathSum);
    dfs(node.right, pathSum);
  }
  
  dfs(root, 0);
  return totalSum;
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
**Space Complexity:** O(h) - Recursion stack depth, h is tree height

**Deep Insights:**
- **Optimal Approach:** DFS with path sum tracking achieves O(n) time—optimal for this problem
- **Number Building:** Multiply path sum by 10 and add current value—builds number digit by digit
- **Leaf Accumulation:** Add path sum to total when reaching leaf—only leaves contribute to sum
- **Key Insight:** Pass path sum down the tree—no need to store full paths
- **Base-10 Arithmetic:** Each level multiplies by 10—standard decimal number construction
- **Edge Cases:** Empty tree returns 0; single node returns its value; all paths contribute
- **Interview Tip:** Explain path sum building clearly; emphasize multiplication by 10; mention base-10 arithmetic

## Q112. Binary Tree Right Side View

**Problem:** Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

**Approach:** Use BFS to process levels. Capture the last node (rightmost) at each level.

### Solution 1: BFS Level Processing (Optimal)
```javascript
function rightSideView(root) {
  if (!root) return [];
  
  const result = [];
  const queue = [root];
  
  while (queue.length) {
    const levelSize = queue.length;
    
    // Process all nodes at current level
    for (let i = 0; i < levelSize; i++) {
      const node = queue.shift();
      
      // Capture rightmost node (last in level)
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
**Space Complexity:** O(w) - Queue stores nodes at widest level, w is maximum width

**Deep Insights:**
- **Optimal Approach:** BFS level processing achieves O(n) time—optimal for this problem
- **Rightmost Node:** Capture last node (i === levelSize - 1) at each level—rightmost visible node
- **Level Processing:** Process all nodes at current level before moving to next—ensures correct order
- **Alternative:** DFS variant tracks maximum depth seen—records rightmost node at each depth
- **Edge Cases:** Empty tree returns empty array; single node returns single value; all levels captured
- **Interview Tip:** Explain BFS approach clearly; mention DFS alternative; ask about left side view variant

## Q113. Average of Levels in Binary Tree

**Problem:** Given the root of a binary tree, return the average value of the nodes on each level in the form of an array.

**Approach:** Use BFS level-order traversal. Sum values at each level and divide by level size.

### Solution 1: BFS with Level Sum (Optimal)
```javascript
function averageOfLevels(root) {
  if (!root) return [];
  
  const result = [];
  const queue = [root];
  
  while (queue.length) {
    const levelSize = queue.length;
    let sum = 0;
    
    // Sum all values at current level
    for (let i = 0; i < levelSize; i++) {
      const node = queue.shift();
      sum += node.val;
      
      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }
    
    // Calculate and store average
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
**Space Complexity:** O(w) - Queue stores nodes at widest level, w is maximum width

**Deep Insights:**
- **Optimal Approach:** BFS level-order traversal achieves O(n) time—optimal for this problem
- **Level Sum:** Sum all values at current level—then divide by level size for average
- **Level Processing:** Process all nodes at current level before moving to next—ensures correct averaging
- **Key Insight:** BFS naturally processes levels—easy to calculate per-level averages
- **Average Calculation:** `sum / levelSize` gives average—handle floating point precision if needed
- **Edge Cases:** Empty tree returns empty array; single node returns its value; all levels processed
- **Interview Tip:** Explain BFS approach clearly; mention level tracking; ask about integer overflow for large sums