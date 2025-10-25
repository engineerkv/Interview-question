# 🧩 DSA Interview Notes - LeetCode Top 150

## 🌳 Section 10 — Tree / BST — Q97-Q116

---

### 97. 🌳 Maximum Depth of Binary Tree

**🧠 Concept**

Find maximum depth of binary tree using recursive DFS approach with height calculation.

**💻 Example**

```javascript
function maxDepth(root) {
  if (!root) return 0;
  
  const leftDepth = maxDepth(root.left);
  const rightDepth = maxDepth(root.right);
  
  return Math.max(leftDepth, rightDepth) + 1;
}
```

**💬 Explanation + Insight**

- **Recursive DFS** - Explore left and right subtrees
- **Base Case** - Return 0 for null nodes
- **Height Calculation** - Add 1 for current node
- **Time Complexity** - O(n) visit each node once
- **Space Complexity** - O(h) where h is tree height

---

### 98. 🌳 Same Tree

**🧠 Concept**

Check if two binary trees are identical using recursive comparison of structure and values.

**💻 Example**

```javascript
function isSameTree(p, q) {
  if (!p && !q) return true;
  if (!p || !q) return false;
  if (p.val !== q.val) return false;
  
  return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
}
```

**💬 Explanation + Insight**

- **Null Check** - Handle cases where one or both trees are null
- **Value Comparison** - Compare node values
- **Recursive Check** - Check left and right subtrees
- **Time Complexity** - O(min(m,n)) where m,n are tree sizes
- **Space Complexity** - O(min(m,n)) recursion stack

---

### 99. 🌳 Invert Binary Tree

**🧠 Concept**

Invert binary tree by swapping left and right children recursively for all nodes.

**💻 Example**

```javascript
function invertTree(root) {
  if (!root) return null;
  
  const left = invertTree(root.left);
  const right = invertTree(root.right);
  
  root.left = right;
  root.right = left;
  
  return root;
}
```

**💬 Explanation + Insight**

- **Swap Children** - Exchange left and right children
- **Recursive Inversion** - Invert subtrees first
- **In-place Modification** - Modify tree structure directly
- **Time Complexity** - O(n) visit each node once
- **Space Complexity** - O(h) recursion stack

---

### 100. 🌳 Symmetric Tree

**🧠 Concept**

Check if binary tree is symmetric using recursive comparison of left and right subtrees.

**💻 Example**

```javascript
function isSymmetric(root) {
  if (!root) return true;
  
  function isMirror(left, right) {
    if (!left && !right) return true;
    if (!left || !right) return false;
    if (left.val !== right.val) return false;
    
    return isMirror(left.left, right.right) && 
           isMirror(left.right, right.left);
  }
  
  return isMirror(root.left, root.right);
}
```

**💬 Explanation + Insight**

- **Mirror Check** - Compare left subtree with right subtree
- **Cross Comparison** - left.left with right.right, left.right with right.left
- **Recursive Validation** - Check symmetry at each level
- **Time Complexity** - O(n) visit each node once
- **Space Complexity** - O(h) recursion stack

---

### 101. 🌳 Construct Binary Tree from Preorder & Inorder

**🧠 Concept**

Build binary tree from preorder and inorder traversals using root position and recursive construction.

**💻 Example**

```javascript
function buildTree(preorder, inorder) {
  if (preorder.length === 0) return null;
  
  const root = new TreeNode(preorder[0]);
  const rootIndex = inorder.indexOf(preorder[0]);
  
  root.left = buildTree(
    preorder.slice(1, rootIndex + 1),
    inorder.slice(0, rootIndex)
  );
  root.right = buildTree(
    preorder.slice(rootIndex + 1),
    inorder.slice(rootIndex + 1)
  );
  
  return root;
}
```

**💬 Explanation + Insight**

- **Root Identification** - First element in preorder is root
- **Index Finding** - Find root position in inorder
- **Subtree Construction** - Recursively build left and right subtrees
- **Time Complexity** - O(n²) due to indexOf operations
- **Space Complexity** - O(n) recursion stack

---

### 102. 🌳 Construct Binary Tree from Inorder & Postorder

**🧠 Concept**

Build binary tree from inorder and postorder traversals using root position and recursive construction.

**💻 Example**

```javascript
function buildTree(inorder, postorder) {
  if (inorder.length === 0) return null;
  
  const root = new TreeNode(postorder[postorder.length - 1]);
  const rootIndex = inorder.indexOf(postorder[postorder.length - 1]);
  
  root.left = buildTree(
    inorder.slice(0, rootIndex),
    postorder.slice(0, rootIndex)
  );
  root.right = buildTree(
    inorder.slice(rootIndex + 1),
    postorder.slice(rootIndex, postorder.length - 1)
  );
  
  return root;
}
```

**💬 Explanation + Insight**

- **Root Identification** - Last element in postorder is root
- **Index Finding** - Find root position in inorder
- **Subtree Construction** - Recursively build left and right subtrees
- **Time Complexity** - O(n²) due to indexOf operations
- **Space Complexity** - O(n) recursion stack

---

### 103. 🌳 Populating Next Right Pointers II

**🧠 Concept**

Connect each node to its next right node in same level using level-order traversal with queue.

**💻 Example**

```javascript
function connect(root) {
  if (!root) return null;
  
  let current = root;
  let nextLevel = null;
  let prev = null;
  
  while (current) {
    if (current.left) {
      if (prev) prev.next = current.left;
      else nextLevel = current.left;
      prev = current.left;
    }
    
    if (current.right) {
      if (prev) prev.next = current.right;
      else nextLevel = current.right;
      prev = current.right;
    }
    
    current = current.next;
    if (!current) {
      current = nextLevel;
      nextLevel = null;
      prev = null;
    }
  }
  
  return root;
}
```

**💬 Explanation + Insight**

- **Level Traversal** - Process nodes level by level
- **Next Pointer** - Connect nodes within same level
- **Next Level Tracking** - Track first node of next level
- **Time Complexity** - O(n) visit each node once
- **Space Complexity** - O(1) constant space

---

### 104. 🌳 Flatten Binary Tree to Linked List

**🧠 Concept**

Flatten binary tree to linked list in preorder traversal using recursive approach with right subtree handling.

**💻 Example**

```javascript
function flatten(root) {
  if (!root) return;
  
  flatten(root.left);
  flatten(root.right);
  
  const right = root.right;
  root.right = root.left;
  root.left = null;
  
  while (root.right) {
    root = root.right;
  }
  root.right = right;
}
```

**💬 Explanation + Insight**

- **Preorder Flattening** - Flatten in preorder traversal order
- **Right Subtree Handling** - Attach right subtree to end of left subtree
- **In-place Modification** - Modify tree structure directly
- **Time Complexity** - O(n) visit each node once
- **Space Complexity** - O(h) recursion stack

---

### 105. 🌳 Path Sum

**🧠 Concept**

Check if binary tree has root-to-leaf path with given sum using recursive DFS with sum tracking.

**💻 Example**

```javascript
function hasPathSum(root, targetSum) {
  if (!root) return false;
  if (!root.left && !root.right) {
    return root.val === targetSum;
  }
  
  return hasPathSum(root.left, targetSum - root.val) ||
         hasPathSum(root.right, targetSum - root.val);
}
```

**💬 Explanation + Insight**

- **Leaf Check** - Check if leaf node equals remaining sum
- **Sum Reduction** - Subtract current node value from target
- **Recursive Check** - Check left and right subtrees
- **Time Complexity** - O(n) visit each node once
- **Space Complexity** - O(h) recursion stack

---

### 106. 🌳 Sum Root to Leaf Numbers

**🧠 Concept**

Calculate sum of all root-to-leaf numbers using DFS with number building and sum accumulation.

**💻 Example**

```javascript
function sumNumbers(root) {
  let totalSum = 0;
  
  function dfs(node, currentSum) {
    if (!node) return;
    
    currentSum = currentSum * 10 + node.val;
    
    if (!node.left && !node.right) {
      totalSum += currentSum;
      return;
    }
    
    dfs(node.left, currentSum);
    dfs(node.right, currentSum);
  }
  
  dfs(root, 0);
  return totalSum;
}
```

**💬 Explanation + Insight**

- **Number Building** - Build number by multiplying by 10 and adding digit
- **Leaf Accumulation** - Add complete number when reaching leaf
- **DFS Traversal** - Explore all paths from root to leaves
- **Time Complexity** - O(n) visit each node once
- **Space Complexity** - O(h) recursion stack

---

### 107. 🌳 Binary Search Tree Iterator

**🧠 Concept**

Implement iterator for BST using stack to simulate inorder traversal with next() and hasNext() methods.

**💻 Example**

```javascript
class BSTIterator {
  constructor(root) {
    this.stack = [];
    this.pushAll(root);
  }
  
  next() {
    const node = this.stack.pop();
    this.pushAll(node.right);
    return node.val;
  }
  
  hasNext() {
    return this.stack.length > 0;
  }
  
  pushAll(node) {
    while (node) {
      this.stack.push(node);
      node = node.left;
    }
  }
}
```

**💬 Explanation + Insight**

- **Stack Simulation** - Use stack to simulate inorder traversal
- **Left Push** - Push all left nodes onto stack
- **Right Handling** - Push right subtree after processing node
- **Time Complexity** - O(1) amortized for next()
- **Space Complexity** - O(h) for stack

---

### 108. 🌳 Count Complete Tree Nodes

**🧠 Concept**

Count nodes in complete binary tree using binary search on height and node counting.

**💻 Example**

```javascript
function countNodes(root) {
  if (!root) return 0;
  
  const leftHeight = getHeight(root.left);
  const rightHeight = getHeight(root.right);
  
  if (leftHeight === rightHeight) {
    return (1 << leftHeight) + countNodes(root.right);
  } else {
    return (1 << rightHeight) + countNodes(root.left);
  }
}

function getHeight(node) {
  let height = 0;
  while (node) {
    height++;
    node = node.left;
  }
  return height;
}
```

**💬 Explanation + Insight**

- **Height Calculation** - Calculate height by going left
- **Complete Tree Property** - Use height difference to determine structure
- **Binary Search** - Eliminate half of tree at each step
- **Time Complexity** - O(log²n) due to height calculation
- **Space Complexity** - O(log n) recursion stack

---

### 109. 🌳 Lowest Common Ancestor of Binary Tree

**🧠 Concept**

Find lowest common ancestor of two nodes using recursive DFS with path tracking.

**💻 Example**

```javascript
function lowestCommonAncestor(root, p, q) {
  if (!root || root === p || root === q) return root;
  
  const left = lowestCommonAncestor(root.left, p, q);
  const right = lowestCommonAncestor(root.right, p, q);
  
  if (left && right) return root;
  return left || right;
}
```

**💬 Explanation + Insight**

- **Base Cases** - Return root if it's one of the target nodes
- **Recursive Search** - Search left and right subtrees
- **LCA Logic** - Return root if both subtrees contain targets
- **Time Complexity** - O(n) visit each node once
- **Space Complexity** - O(h) recursion stack

---

### 110. 🌳 Right Side View

**🧠 Concept**

Get right side view of binary tree using level-order traversal and track last node of each level.

**💻 Example**

```javascript
function rightSideView(root) {
  if (!root) return [];
  
  const result = [];
  const queue = [root];
  
  while (queue.length > 0) {
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
```

**💬 Explanation + Insight**

- **Level Traversal** - Process tree level by level
- **Rightmost Node** - Track last node of each level
- **Queue Management** - Use queue for level-order traversal
- **Time Complexity** - O(n) visit each node once
- **Space Complexity** - O(w) where w is maximum width

---

### 111. 🌳 Average of Levels in Binary Tree

**🧠 Concept**

Calculate average value of nodes at each level using level-order traversal with sum and count tracking.

**💻 Example**

```javascript
function averageOfLevels(root) {
  if (!root) return [];
  
  const result = [];
  const queue = [root];
  
  while (queue.length > 0) {
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
```

**💬 Explanation + Insight**

- **Level Processing** - Process each level separately
- **Sum Calculation** - Calculate sum of values at each level
- **Average Computation** - Divide sum by number of nodes
- **Time Complexity** - O(n) visit each node once
- **Space Complexity** - O(w) where w is maximum width

---

### 112. 🌳 Binary Tree Level Order Traversal

**🧠 Concept**

Return level order traversal of binary tree using queue-based BFS with level separation.

**💻 Example**

```javascript
function levelOrder(root) {
  if (!root) return [];
  
  const result = [];
  const queue = [root];
  
  while (queue.length > 0) {
    const levelSize = queue.length;
    const level = [];
    
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
```

**💬 Explanation + Insight**

- **BFS Traversal** - Use queue for level-order traversal
- **Level Separation** - Process each level separately
- **Queue Management** - Add children to queue for next level
- **Time Complexity** - O(n) visit each node once
- **Space Complexity** - O(w) where w is maximum width

---

### 113. 🌳 Zigzag Level Order Traversal

**🧠 Concept**

Return zigzag level order traversal alternating between left-to-right and right-to-left directions.

**💻 Example**

```javascript
function zigzagLevelOrder(root) {
  if (!root) return [];
  
  const result = [];
  const queue = [root];
  let leftToRight = true;
  
  while (queue.length > 0) {
    const levelSize = queue.length;
    const level = [];
    
    for (let i = 0; i < levelSize; i++) {
      const node = queue.shift();
      
      if (leftToRight) {
        level.push(node.val);
      } else {
        level.unshift(node.val);
      }
      
      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }
    
    result.push(level);
    leftToRight = !leftToRight;
  }
  
  return result;
}
```

**💬 Explanation + Insight**

- **Direction Alternation** - Alternate between left-to-right and right-to-left
- **Array Manipulation** - Use push/unshift based on direction
- **Level Processing** - Process each level with appropriate direction
- **Time Complexity** - O(n) visit each node once
- **Space Complexity** - O(w) where w is maximum width

---

### 114. 🌳 Validate Binary Search Tree

**🧠 Concept**

Check if binary tree is valid BST using inorder traversal or recursive bounds checking.

**💻 Example**

```javascript
function isValidBST(root) {
  function validate(node, min, max) {
    if (!node) return true;
    
    if (node.val <= min || node.val >= max) {
      return false;
    }
    
    return validate(node.left, min, node.val) &&
           validate(node.right, node.val, max);
  }
  
  return validate(root, -Infinity, Infinity);
}
```

**💬 Explanation + Insight**

- **Bounds Checking** - Check if node value is within valid range
- **Recursive Validation** - Validate left and right subtrees
- **Range Updates** - Update bounds for subtrees
- **Time Complexity** - O(n) visit each node once
- **Space Complexity** - O(h) recursion stack

---

### 115. 🌳 Kth Smallest Element in BST

**🧠 Concept**

Find kth smallest element in BST using inorder traversal with counter.

**💻 Example**

```javascript
function kthSmallest(root, k) {
  let count = 0;
  let result = null;
  
  function inorder(node) {
    if (!node || result !== null) return;
    
    inorder(node.left);
    count++;
    if (count === k) {
      result = node.val;
      return;
    }
    inorder(node.right);
  }
  
  inorder(root);
  return result;
}
```

**💬 Explanation + Insight**

- **Inorder Traversal** - Visit nodes in sorted order
- **Counter Tracking** - Track number of nodes visited
- **Early Termination** - Stop when kth element found
- **Time Complexity** - O(h + k) where h is tree height
- **Space Complexity** - O(h) recursion stack

---

### 116. 🌳 Minimum Absolute Difference in BST

**🧠 Concept**

Find minimum absolute difference between any two nodes in BST using inorder traversal.

**💻 Example**

```javascript
function getMinimumDifference(root) {
  let minDiff = Infinity;
  let prev = null;
  
  function inorder(node) {
    if (!node) return;
    
    inorder(node.left);
    
    if (prev !== null) {
      minDiff = Math.min(minDiff, node.val - prev);
    }
    prev = node.val;
    
    inorder(node.right);
  }
  
  inorder(root);
  return minDiff;
}
```

**💬 Explanation + Insight**

- **Inorder Traversal** - Visit nodes in sorted order
- **Adjacent Comparison** - Compare consecutive nodes
- **Minimum Tracking** - Track minimum difference found
- **Time Complexity** - O(n) visit each node once
- **Space Complexity** - O(h) recursion stack

---

*This comprehensive tree and BST section covers essential tree operations including traversal, construction, validation, and advanced tree algorithms for efficient tree processing.*