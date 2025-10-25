# 🧩 DSA Interview Notes - LeetCode Top 150

## 🔗 Section 7 — Linked List — Q61-Q71

---

### 61. 🔗 Add Two Numbers

**🧠 Concept**

Add two numbers represented as linked lists in reverse order. Handle carry and different lengths.

**💻 Example**

```javascript
function addTwoNumbers(l1, l2) {
  const dummy = new ListNode(0);
  let current = dummy;
  let carry = 0;
  
  while (l1 || l2 || carry) {
    const sum = (l1?.val || 0) + (l2?.val || 0) + carry;
    carry = Math.floor(sum / 10);
    current.next = new ListNode(sum % 10);
    current = current.next;
    l1 = l1?.next;
    l2 = l2?.next;
  }
  
  return dummy.next;
}
```

**💬 Explanation + Insight**

- **Dummy Node** - Use dummy head to simplify edge cases
- **Carry Handling** - Track carry from previous addition
- **Length Difference** - Handle lists of different lengths
- **Time Complexity** - O(max(m,n)) where m,n are list lengths
- **Space Complexity** - O(max(m,n)) for result list

---

### 62. 🔗 Remove Nth Node From End of List

**🧠 Concept**

Remove nth node from end using two pointers. Move first pointer n steps ahead, then move both until first reaches end.

**💻 Example**

```javascript
function removeNthFromEnd(head, n) {
  const dummy = new ListNode(0);
  dummy.next = head;
  let first = dummy;
  let second = dummy;
  
  for (let i = 0; i <= n; i++) {
    first = first.next;
  }
  
  while (first) {
    first = first.next;
    second = second.next;
  }
  
  second.next = second.next.next;
  return dummy.next;
}
```

**💬 Explanation + Insight**

- **Two Pointers** - First pointer n steps ahead of second
- **Dummy Head** - Handle edge case of removing first node
- **Gap Maintenance** - Keep n+1 gap between pointers
- **Time Complexity** - O(L) where L is list length
- **Space Complexity** - O(1) constant space

---

### 63. 🔗 Merge Two Sorted Lists

**🧠 Concept**

Merge two sorted linked lists by comparing values and linking nodes in sorted order.

**💻 Example**

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

**💬 Explanation + Insight**

- **Two Pointer Comparison** - Compare values from both lists
- **Dummy Head** - Simplify merging logic
- **Remaining Elements** - Link remaining elements from either list
- **Time Complexity** - O(m+n) where m,n are list lengths
- **Space Complexity** - O(1) constant space

---

### 64. 🔗 Reverse Nodes in k-Group

**🧠 Concept**

Reverse nodes in groups of k. Use recursive approach to reverse each group and connect them.

**💻 Example**

```javascript
function reverseKGroup(head, k) {
  let current = head;
  let count = 0;
  
  while (current && count < k) {
    current = current.next;
    count++;
  }
  
  if (count === k) {
    current = reverseKGroup(current, k);
    while (count > 0) {
      const next = head.next;
      head.next = current;
      current = head;
      head = next;
      count--;
    }
    head = current;
  }
  
  return head;
}
```

**💬 Explanation + Insight**

- **Recursive Approach** - Reverse each group recursively
- **Count Check** - Ensure enough nodes for reversal
- **Group Reversal** - Reverse k nodes in each group
- **Time Complexity** - O(n) where n is list length
- **Space Complexity** - O(n/k) recursion stack

---

### 65. 🔗 Rotate List

**🧠 Concept**

Rotate list to the right by k places. Connect tail to head and break at new tail position.

**💻 Example**

```javascript
function rotateRight(head, k) {
  if (!head || !head.next) return head;
  
  let tail = head;
  let length = 1;
  
  while (tail.next) {
    tail = tail.next;
    length++;
  }
  
  tail.next = head;
  k = k % length;
  
  for (let i = 0; i < length - k; i++) {
    tail = tail.next;
  }
  
  head = tail.next;
  tail.next = null;
  return head;
}
```

**💬 Explanation + Insight**

- **Circular List** - Connect tail to head
- **Modulo Operation** - Handle k > list length
- **New Head** - Find new head position
- **Time Complexity** - O(n) where n is list length
- **Space Complexity** - O(1) constant space

---

### 66. 🔗 Remove Duplicates from Sorted List II

**🧠 Concept**

Remove all duplicates from sorted list, including the original nodes. Use dummy head and check for duplicates.

**💻 Example**

```javascript
function deleteDuplicates(head) {
  const dummy = new ListNode(0);
  dummy.next = head;
  let prev = dummy;
  
  while (head) {
    if (head.next && head.val === head.next.val) {
      const duplicate = head.val;
      while (head && head.val === duplicate) {
        head = head.next;
      }
      prev.next = head;
    } else {
      prev = prev.next;
      head = head.next;
    }
  }
  
  return dummy.next;
}
```

**💬 Explanation + Insight**

- **Dummy Head** - Handle edge case of removing first node
- **Duplicate Detection** - Check consecutive nodes for duplicates
- **Skip All Duplicates** - Remove all nodes with duplicate value
- **Time Complexity** - O(n) single pass through list
- **Space Complexity** - O(1) constant space

---

### 67. 🔗 Partition List

**🧠 Concept**

Partition list around value x. Create two lists - one for nodes < x, one for nodes >= x, then concatenate.

**💻 Example**

```javascript
function partition(head, x) {
  const beforeHead = new ListNode(0);
  const afterHead = new ListNode(0);
  let before = beforeHead;
  let after = afterHead;
  
  while (head) {
    if (head.val < x) {
      before.next = head;
      before = before.next;
    } else {
      after.next = head;
      after = after.next;
    }
    head = head.next;
  }
  
  after.next = null;
  before.next = afterHead.next;
  return beforeHead.next;
}
```

**💬 Explanation + Insight**

- **Two Lists** - Separate nodes based on value comparison
- **Dummy Heads** - Simplify concatenation logic
- **Concatenation** - Connect before list to after list
- **Time Complexity** - O(n) single pass through list
- **Space Complexity** - O(1) constant space

---

### 68. 🔗 Reverse Linked List II

**🧠 Concept**

Reverse portion of list between positions left and right. Use dummy head and reverse sublist.

**💻 Example**

```javascript
function reverseBetween(head, left, right) {
  const dummy = new ListNode(0);
  dummy.next = head;
  let prev = dummy;
  
  for (let i = 0; i < left - 1; i++) {
    prev = prev.next;
  }
  
  let current = prev.next;
  for (let i = 0; i < right - left; i++) {
    const next = current.next;
    current.next = next.next;
    next.next = prev.next;
    prev.next = next;
  }
  
  return dummy.next;
}
```

**💬 Explanation + Insight**

- **Dummy Head** - Handle edge case of reversing from beginning
- **Position Tracking** - Find start position of reversal
- **Sublist Reversal** - Reverse nodes within specified range
- **Time Complexity** - O(n) where n is list length
- **Space Complexity** - O(1) constant space

---

### 69. 🔗 Copy List with Random Pointer

**🧠 Concept**

Deep copy linked list with random pointers using HashMap to map original nodes to copied nodes.

**💻 Example**

```javascript
function copyRandomList(head) {
  if (!head) return null;
  
  const map = new Map();
  let current = head;
  
  while (current) {
    map.set(current, new Node(current.val));
    current = current.next;
  }
  
  current = head;
  while (current) {
    map.get(current).next = map.get(current.next) || null;
    map.get(current).random = map.get(current.random) || null;
    current = current.next;
  }
  
  return map.get(head);
}
```

**💬 Explanation + Insight**

- **HashMap Mapping** - Map original nodes to copied nodes
- **Two Passes** - First pass creates nodes, second pass links them
- **Random Pointer** - Copy random pointers using map
- **Time Complexity** - O(n) two passes through list
- **Space Complexity** - O(n) for HashMap

---

### 70. 🔗 Linked List Cycle

**🧠 Concept**

Detect cycle in linked list using Floyd's cycle detection algorithm (tortoise and hare).

**💻 Example**

```javascript
function hasCycle(head) {
  if (!head || !head.next) return false;
  
  let slow = head;
  let fast = head.next;
  
  while (fast && fast.next) {
    if (slow === fast) return true;
    slow = slow.next;
    fast = fast.next.next;
  }
  
  return false;
}
```

**💬 Explanation + Insight**

- **Floyd's Algorithm** - Use two pointers with different speeds
- **Cycle Detection** - Fast pointer will catch slow pointer if cycle exists
- **Speed Difference** - Slow moves 1 step, fast moves 2 steps
- **Time Complexity** - O(n) where n is list length
- **Space Complexity** - O(1) constant space

---

### 71. 🔗 Sort List

**🧠 Concept**

Sort linked list using merge sort. Split list into halves, sort recursively, then merge.

**💻 Example**

```javascript
function sortList(head) {
  if (!head || !head.next) return head;
  
  const mid = findMiddle(head);
  const left = head;
  const right = mid.next;
  mid.next = null;
  
  return merge(sortList(left), sortList(right));
}

function findMiddle(head) {
  let slow = head;
  let fast = head.next;
  
  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
  }
  
  return slow;
}
```

**💬 Explanation + Insight**

- **Merge Sort** - Divide and conquer approach
- **Middle Finding** - Use slow/fast pointers to find middle
- **Recursive Sorting** - Sort halves recursively
- **Time Complexity** - O(n log n) merge sort
- **Space Complexity** - O(log n) recursion stack

---

*This comprehensive linked list section covers essential operations including merging, reversing, cycle detection, and advanced manipulation techniques for efficient list processing.*