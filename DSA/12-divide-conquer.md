# 🧩 DSA Interview Notes - LeetCode Top 150

## 🔍 Section 12 — Divide & Conquer — Q126-Q129

---

### 126. 🔍 Merge k Sorted Lists

**🧠 Concept**

Merge k sorted linked lists using divide and conquer approach by recursively merging pairs of lists.

**💻 Example**

```javascript
function mergeKLists(lists) {
  if (!lists || lists.length === 0) return null;
  
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
  
  function divideAndConquer(lists, start, end) {
    if (start === end) return lists[start];
    if (start > end) return null;
    
    const mid = Math.floor((start + end) / 2);
    const left = divideAndConquer(lists, start, mid);
    const right = divideAndConquer(lists, mid + 1, end);
    
    return mergeTwoLists(left, right);
  }
  
  return divideAndConquer(lists, 0, lists.length - 1);
}
```

**💬 Explanation + Insight**

- **Divide and Conquer** - Split lists into halves recursively
- **Pair Merging** - Merge two lists at a time
- **Base Case** - Handle single list or empty range
- **Time Complexity** - O(n log k) where n is total nodes, k is number of lists
- **Space Complexity** - O(log k) recursion stack

---

### 127. 🔍 Convert Sorted Array to BST

**🧠 Concept**

Convert sorted array to balanced BST using divide and conquer with middle element as root.

**💻 Example**

```javascript
function sortedArrayToBST(nums) {
  if (!nums || nums.length === 0) return null;
  
  function buildBST(left, right) {
    if (left > right) return null;
    
    const mid = Math.floor((left + right) / 2);
    const root = new TreeNode(nums[mid]);
    
    root.left = buildBST(left, mid - 1);
    root.right = buildBST(mid + 1, right);
    
    return root;
  }
  
  return buildBST(0, nums.length - 1);
}
```

**💬 Explanation + Insight**

- **Middle Element** - Use middle element as root for balance
- **Recursive Construction** - Build left and right subtrees recursively
- **Balanced BST** - Ensures O(log n) height
- **Time Complexity** - O(n) visit each element once
- **Space Complexity** - O(log n) recursion stack

---

### 128. 🔍 Sort List

**🧠 Concept**

Sort linked list using merge sort with divide and conquer approach.

**💻 Example**

```javascript
function sortList(head) {
  if (!head || !head.next) return head;
  
  function findMiddle(head) {
    let slow = head;
    let fast = head.next;
    
    while (fast && fast.next) {
      slow = slow.next;
      fast = fast.next.next;
    }
    
    return slow;
  }
  
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
  
  const mid = findMiddle(head);
  const right = mid.next;
  mid.next = null;
  
  const left = sortList(head);
  const sortedRight = sortList(right);
  
  return mergeTwoLists(left, sortedRight);
}
```

**💬 Explanation + Insight**

- **Merge Sort** - Divide list into halves, sort, then merge
- **Middle Finding** - Use slow/fast pointers to find middle
- **List Splitting** - Split list at middle point
- **Time Complexity** - O(n log n) merge sort
- **Space Complexity** - O(log n) recursion stack

---

### 129. 🔍 Construct Quad Tree

**🧠 Concept**

Build quad tree from 2D grid using divide and conquer with recursive subdivision.

**💻 Example**

```javascript
function construct(grid) {
  function buildQuadTree(row, col, size) {
    if (size === 1) {
      return new Node(grid[row][col] === 1, true);
    }
    
    const halfSize = size / 2;
    const topLeft = buildQuadTree(row, col, halfSize);
    const topRight = buildQuadTree(row, col + halfSize, halfSize);
    const bottomLeft = buildQuadTree(row + halfSize, col, halfSize);
    const bottomRight = buildQuadTree(row + halfSize, col + halfSize, halfSize);
    
    const allSame = topLeft.isLeaf && topRight.isLeaf && 
                   bottomLeft.isLeaf && bottomRight.isLeaf &&
                   topLeft.val === topRight.val &&
                   topRight.val === bottomLeft.val &&
                   bottomLeft.val === bottomRight.val;
    
    if (allSame) {
      return new Node(topLeft.val, true);
    }
    
    return new Node(false, false, topLeft, topRight, bottomLeft, bottomRight);
  }
  
  return buildQuadTree(0, 0, grid.length);
}
```

**💬 Explanation + Insight**

- **Recursive Subdivision** - Divide grid into four quadrants
- **Leaf Detection** - Check if all quadrants have same value
- **Tree Construction** - Build internal nodes when values differ
- **Time Complexity** - O(n²) where n is grid size
- **Space Complexity** - O(log n) recursion stack

---

*This comprehensive divide and conquer section covers essential algorithms including merge operations, tree construction, and recursive problem-solving techniques for efficient data processing.*