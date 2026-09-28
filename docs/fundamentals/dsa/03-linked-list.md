---
sidebar_label: "Linked List"
---
# Linked List

---

## Q56. 🔄 Reverse Linked List

**Problem:** Given the head of a singly linked list, reverse the list, and return the reversed list.

**Problem Explanation:** We need to reverse the direction of all pointers in a linked list. For example, if the list is `1 -> 2 -> 3 -> 4 -> 5`, after reversal it becomes `5 -> 4 -> 3 -> 2 -> 1`. The head of the original list becomes the tail, and the tail becomes the new head.

**Approach:** Use three pointers to track the previous node, current node, and next node. As we traverse, we reverse the link by pointing the current node's `next` to the previous node. We must save the next node before reversing to avoid losing the reference. This iterative approach processes one node at a time.

**Why this works:** By maintaining references to previous, current, and next nodes, we can safely reverse each link without losing track of the rest of the list. The previous pointer eventually becomes the new head.

### Solution 1: Iterative (Optimal)

```javascript
function reverseList(head) {
  let previousNode = null;  // Previous node (starts as null since first node will point to null)
  let currentNode = head;   // Current node being processed

  while (currentNode !== null) {
    const nextNode = currentNode.next;  // Save reference to next node before reversing

    // Reverse the link: point current node to previous
    currentNode.next = previousNode;

    // Move pointers forward
    previousNode = currentNode;  // Previous becomes current
    currentNode = nextNode;      // Current moves to saved next
  }

  return previousNode;  // Previous is now the new head (last node processed)
}

// Test Cases:
// Input: head = [1, 2, 3, 4, 5]
// Output: [5, 4, 3, 2, 1]

// Input: head = [1, 2]
// Output: [2, 1]

// Input: head = []
// Output: []

```

**Time Complexity:** O(n) - Single pass through all nodes
**Space Complexity:** O(1) - Only using constant extra variables

### Solution 2: Recursive (Alternative)

```javascript
function reverseListRecursive(head) {
  // Base case: empty list or single node (already reversed)
  if (head === null || head.next === null) {
    return head;
  }

  // Recursively reverse the rest of the list
  // This returns the new head of the reversed sublist
  const newHead = reverseListRecursive(head.next);

  // Reverse the link: make next node point back to current
  head.next.next = head;

  // Current node becomes tail, so its next should be null
  head.next = null;

  return newHead;  // Return the new head (original tail)
}

```

**Time Complexity:** O(n) - Recursive calls for each of the n nodes
**Space Complexity:** O(n) - Recursion stack depth equals the number of nodes

**When to use:** Recursive approach is more elegant and easier to understand conceptually, but uses O(n) extra space for the call stack. Use when code clarity is preferred and stack depth is not a concern.

## Q57. 💡 Linked List Cycle

**Problem:** Given `head`, the head of a linked list, determine if the linked list has a cycle in it. There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. Note that `pos` is not passed as a parameter. Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

**Problem Explanation:** A cycle exists when a node's `next` pointer points back to a previous node, creating a loop. For example, if we have `1 -> 2 -> 3 -> 4 -> 2` (where 4 points back to 2), there's a cycle. We need to detect this without modifying the list or using extra space proportional to list length.

**Approach:** Use Floyd's Cycle Detection Algorithm (also called "Tortoise and Hare"). Use two pointers moving at different speeds: slow pointer moves one step at a time, fast pointer moves two steps. If there's a cycle, the fast pointer will eventually "lap" the slow pointer and they'll meet. If there's no cycle, the fast pointer will reach the end (null).

**Why this works:** In a cycle, the fast pointer gains one step on the slow pointer per iteration. Eventually, the fast pointer will catch up to the slow pointer, proving a cycle exists. This is mathematically guaranteed.

### Solution 1: Floyd's Cycle Detection (Optimal)

```javascript
function hasCycle(head) {
  // Edge cases: empty list or single node (no cycle possible)
  if (head === null || head.next === null) return false;

  let slowPointer = head;  // Tortoise: moves 1 step at a time
  let fastPointer = head;  // Hare: moves 2 steps at a time

  while (fastPointer !== null && fastPointer.next !== null) {
    slowPointer = slowPointer.next;        // Move slow pointer 1 step
    fastPointer = fastPointer.next.next;   // Move fast pointer 2 steps

    // If pointers meet, cycle exists
    if (slowPointer === fastPointer) {
      return true;
    }
  }

  // Fast pointer reached end, no cycle
  return false;
}

// Test Cases:
// Input: head = [3, 2, 0, -4], pos = 1 (cycle exists at index 1)
// Output: true

// Input: head = [1, 2], pos = 0 (cycle exists at index 0)
// Output: true

// Input: head = [1], pos = -1 (no cycle)
// Output: false

// Input: head = []
// Output: false

```

**Time Complexity:** O(n) - Single pass with fast/slow pointers
**Space Complexity:** O(1) - Only using constant extra variables

### Solution 2: Hash Set (Alternative)

```javascript
function hasCycleHashSet(head) {
  const visitedNodes = new Set(); // Track nodes we've seen
  let currentNode = head;

  while (currentNode !== null) {
    // If we've seen this node before, cycle exists
    if (visitedNodes.has(currentNode)) {
      return true;
    }

    // Mark current node as visited
    visitedNodes.add(currentNode);
    currentNode = currentNode.next;
  }

  // Reached end of list, no cycle
  return false;
}

```

**Time Complexity:** O(n) - Visit each node at most once
**Space Complexity:** O(n) - Hash set stores up to n nodes

**When to use:** This approach is more intuitive and easier to understand, but requires O(n) extra space. Use when space is not a constraint and code clarity is important.

**Time Complexity:** O(n) - Single pass
**Space Complexity:** O(n) - Hash set storage

## Q58. 🟢 Remove Nth Node From End of List

**Problem:** Given the head of a linked list, remove the `n`th node from the end of the list and return its head.

**Problem Explanation:** We need to remove a node that is `n` positions from the end. For example, in `[1, 2, 3, 4, 5]` with n=2, we remove node 4 (2nd from end). The challenge is finding this node in one pass without knowing the list length.

**Approach:** Use two pointers with a gap of `n` nodes. Move the fast pointer `n` steps ahead, then move both pointers together. When fast reaches the end, slow is at the node before the one to remove. Use a dummy head to handle edge cases (like removing the head node).

**Why this works:** By maintaining a gap of `n` nodes between the pointers, when the fast pointer reaches the end, the slow pointer is exactly `n` positions from the end. The dummy head simplifies edge cases where we need to remove the head.

### Solution 1: Two Pointers with Gap (Optimal)

```javascript
function removeNthFromEnd(head, n) {
  const dummy = { next: head };  // Dummy head handles edge cases
  let slow = dummy;
  let fast = dummy;

  // Move fast pointer n steps ahead
  for (let i = 0; i < n; i++) {
    fast = fast.next;
  }

  // Move both pointers until fast reaches end
  while (fast.next) {
    slow = slow.next;
    fast = fast.next;
  }

  // Remove nth node from end
  slow.next = slow.next.next;

  return dummy.next;
}

// Test Cases:
// Input: head = [1, 2, 3, 4, 5], n = 2
// Output: [1, 2, 3, 5]
// Explanation: Remove node with value 4 (2nd from end)

// Input: head = [1], n = 1
// Output: []
// Explanation: Remove the only node

// Input: head = [1, 2], n = 1
// Output: [1]
// Explanation: Remove last node

// Input: head = [1, 2], n = 2
// Output: [2]
// Explanation: Remove first node (nth from end = head)

```

**Time Complexity:** O(n) - Single pass with two pointers
**Space Complexity:** O(1) - Only using constant extra variables (dummy node)

## Q59. 🔀 Merge Two Sorted Lists

**Problem:** You are given the heads of two sorted linked lists `list1` and `list2`. Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists. Return the head of the merged linked list.

**Approach:** Use a dummy head and tail pointer. Compare heads of both lists, append the smaller one to the tail. Continue until one list is exhausted, then append the remaining list.

### Solution 1: Iterative Merge (Optimal)

```javascript
function mergeTwoLists(list1, list2) {
  const dummy = { next: null };
  let tail = dummy;

  while (list1 && list2) {
    if (list1.val <= list2.val) {
      tail.next = list1;
      list1 = list1.next;
    } else {
      tail.next = list2;
      list2 = list2.next;
    }
    tail = tail.next;
  }

  // Append remaining list
  tail.next = list1 || list2;

  return dummy.next;
}

// Test Cases:
// Input: list1 = [1, 2, 4], list2 = [1, 3, 4]
// Output: [1, 1, 2, 3, 4, 4]

// Input: list1 = [], list2 = []
// Output: []

// Input: list1 = [], list2 = [0]
// Output: [0]

// Input: list1 = [1], list2 = [2]
// Output: [1, 2]

```

**Time Complexity:** O(m + n) - Merge pass through both lists where m and n are list lengths
**Space Complexity:** O(1) - Only using constant extra variables (dummy node)

### Solution 2: Recursive (Alternative)

```javascript
function mergeTwoListsRecursive(list1, list2) {
  if (!list1) return list2;
  if (!list2) return list1;

  if (list1.val <= list2.val) {
    list1.next = mergeTwoListsRecursive(list1.next, list2);
    return list1;
  } else {
    list2.next = mergeTwoListsRecursive(list1, list2.next);
    return list2;
  }
}

```

**Time Complexity:** O(m + n) - Recursive calls
**Space Complexity:** O(m + n) - Recursion stack

## Q60. 💡 Middle of the Linked List

**Problem:** Given the head of a singly linked list, return the middle node of the linked list. If there are two middle nodes, return the second middle node.

**Approach:** Use fast and slow pointers. Fast pointer moves at 2x speed. When fast reaches the end, slow is at the middle.

### Solution 1: Fast/Slow Pointers (Optimal)

```javascript
function middleNode(head) {
  let slow = head;
  let fast = head;

  while (fast && fast.next) {
    slow = slow.next;       // Move 1 step
    fast = fast.next.next;  // Move 2 steps
  }

  return slow;  // Slow is at middle
}

// Test Cases:
// Input: head = [1, 2, 3, 4, 5]
// Output: [3, 4, 5]
// Explanation: Middle node is 3 (odd length)

// Input: head = [1, 2, 3, 4, 5, 6]
// Output: [4, 5, 6]
// Explanation: Second middle node is 4 (even length)

// Input: head = [1]
// Output: [1]
// Explanation: Single node is the middle

// Input: head = [1, 2]
// Output: [2]
// Explanation: Second middle node (even length)

```

**Time Complexity:** O(n) - Single pass through list
**Space Complexity:** O(1) - Only using constant extra variables

## Q61. 🔄 Palindrome Linked List

**Problem:** Given the head of a singly linked list, return `true` if it is a palindrome or `false` otherwise.

**Approach:** Find the middle node, reverse the second half, then compare the two halves. If original list should be preserved, restore it after comparison.

### Solution 1: Find Middle + Reverse + Compare (Optimal)

```javascript
function isPalindrome(head) {
  if (!head || !head.next) return true;

  // Helper function to reverse list
  const reverse = (h) => {
    let prev = null;
    let cur = h;
    while (cur) {
      const next = cur.next;
      cur.next = prev;
      prev = cur;
      cur = next;
    }
    return prev;
  };

  // Step 1: Find middle using fast/slow pointers
  let slow = head;
  let fast = head;
  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
  }

  // Step 2: Reverse second half
  let second = reverse(slow);
  let first = head;

  // Step 3: Compare halves
  while (second) {
    if (second.val !== first.val) return false;
    second = second.next;
    first = first.next;
  }

  return true;
}

// Test Cases:
// Input: head = [1, 2, 2, 1]
// Output: true
// Explanation: First half [1,2] matches reversed second half [1,2]

// Input: head = [1, 2]
// Output: false
// Explanation: First half [1] doesn't match second half [2]

// Input: head = [1]
// Output: true
// Explanation: Single node is a palindrome

// Input: head = [1, 2, 3, 2, 1]
// Output: true
// Explanation: Palindrome verified

```

**Time Complexity:** O(n) - Finding middle + reversing + comparing (all O(n))
**Space Complexity:** O(1) - In-place reversal, constant extra space

**Note:** If original list must be preserved, restore it by reversing the second half again after comparison.

## Q62. 💡 Flatten a Multilevel Doubly Linked List

**Problem:** You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional child pointer. This child pointer may or may not point to a separate doubly linked list, also containing these special nodes. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure. Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level, doubly linked list. Let `curr` be a node with a child list. The nodes in the child list should appear after `curr` and before `curr.next` in the flattened list.

**Approach:** Use iterative DFS with a stack to remember deferred `next` nodes when processing `child` pointers. Process children first (pre-order style).

### Solution 1: Iterative DFS with Stack (Optimal)

```javascript
function flatten(head) {
  if (!head) return head;

  const stack = [];
  let cur = head;

  while (cur) {
    if (cur.child) {
      // Save next node if exists
      if (cur.next) {
        stack.push(cur.next);
      }

      // Flatten child list
      cur.next = cur.child;
      cur.child.prev = cur;
      cur.child = null;
    }

    // If no next and stack has deferred nodes
    if (!cur.next && stack.length > 0) {
      const next = stack.pop();
      cur.next = next;
      next.prev = cur;
    }

    cur = cur.next;
  }

  return head;
}

// Test Cases:
// Input: head = [1, 2, 3, 4, 5, 6, null, null, null, 7, 8, 9, 10, null, null, 11, 12]
// (Represents multilevel structure)
// Output: [1, 2, 3, 7, 8, 11, 12, 9, 10, 4, 5, 6]

// Input: head = [1, 2, null, 3]
// Output: [1, 3, 2]

// Input: head = []
// Output: []

```

**Time Complexity:** O(n) - Single pass through all nodes
**Space Complexity:** O(k) - Stack stores deferred nodes (k is number of child branches)

## Q63. 💡 Intersection of Two Linked Lists

**Problem:** Given the heads of two singly linked lists `headA` and `headB`, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return `null`.

**Approach:** Use two pointers that switch heads when reaching the end. This equalizes path lengths—both pointers traverse the same total distance (m + n), meeting at the intersection if it exists.

### Solution 1: Switch Heads Technique (Optimal)

```javascript
function getIntersectionNode(headA, headB) {
  if (!headA || !headB) return null;

  let p = headA;
  let q = headB;

  // Both pointers traverse m + n nodes total
  // If intersection exists, they meet at intersection
  // If no intersection, both become null simultaneously
  while (p !== q) {
    p = p ? p.next : headB;  // Switch to headB when p reaches end
    q = q ? q.next : headA;  // Switch to headA when q reaches end
  }

  return p;  // p === q (either intersection node or null)
}

// Test Cases:
// Input: intersectVal = 8, listA = [4, 1, 8, 4, 5], listB = [5, 6, 1, 8, 4, 5], skipA = 2, skipB = 3
// Output: Intersected at node with value 8

// Input: intersectVal = 2, listA = [1, 9, 1, 2, 4], listB = [3, 2, 4], skipA = 3, skipB = 1
// Output: Intersected at node with value 2

// Input: intersectVal = 0, listA = [2, 6, 4], listB = [1, 5], skipA = 3, skipB = 2
// Output: null (no intersection)

// Input: listA = [], listB = []
// Output: null

```

**Time Complexity:** O(m + n) - Both pointers traverse m + n nodes total
**Space Complexity:** O(1) - Only using constant extra variables

## Q64. ➕ Add Two Numbers

**Problem:** You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Approach:** Add digits from both lists along with carry, building the result list from least significant digit. Create new nodes for the result.

### Solution 1: Digit-wise Addition with Carry (Optimal)

```javascript
function addTwoNumbers(l1, l2) {
  const dummy = { next: null };
  let tail = dummy;
  let carry = 0;

  while (l1 || l2 || carry) {
    const sum = (l1 ? l1.val : 0) + (l2 ? l2.val : 0) + carry;
    const digit = sum % 10;
    carry = Math.floor(sum / 10);

    tail.next = { val: digit, next: null };
    tail = tail.next;

    if (l1) l1 = l1.next;
    if (l2) l2 = l2.next;
  }

  return dummy.next;
}

// Test Cases:
// Input: l1 = [2, 4, 3], l2 = [5, 6, 4]
// Output: [7, 0, 8]
// Explanation: 342 + 465 = 807

// Input: l1 = [0], l2 = [0]
// Output: [0]
// Explanation: 0 + 0 = 0

// Input: l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9]
// Output: [8, 9, 9, 9, 0, 0, 0, 1]
// Explanation: 9999999 + 9999 = 10009998

```

**Time Complexity:** O(max(m, n)) - Process all digits from longer list
**Space Complexity:** O(max(m, n)) - Result list storage (excluding input)

## Q65. 🔀 Sort List

**Problem:** Given the head of a linked list, return the list after sorting it in ascending order.

**Approach:** Use merge sort: find middle, recursively sort both halves, then merge the sorted halves.

### Solution 1: Merge Sort (Optimal)

```javascript
function sortList(head) {
  // Base case: empty or single node
  if (!head || !head.next) return head;

  // Step 1: Find middle and split
  let slow = head;
  let fast = head;
  let prev = null;

  while (fast && fast.next) {
    prev = slow;
    slow = slow.next;
    fast = fast.next.next;
  }

  prev.next = null;  // Split list

  // Step 2: Recursively sort halves
  const left = sortList(head);
  const right = sortList(slow);

  // Step 3: Merge sorted halves
  return merge(left, right);
}

function merge(list1, list2) {
  const dummy = { next: null };
  let tail = dummy;

  while (list1 && list2) {
    if (list1.val <= list2.val) {
      tail.next = list1;
      list1 = list1.next;
    } else {
      tail.next = list2;
      list2 = list2.next;
    }
    tail = tail.next;
  }

  tail.next = list1 || list2;
  return dummy.next;
}

// Test Cases:
// Input: head = [4, 2, 1, 3]
// Output: [1, 2, 3, 4]

// Input: head = [-1, 5, 3, 4, 0]
// Output: [-1, 0, 3, 4, 5]

// Input: head = []
// Output: []

// Input: head = [1]
// Output: [1]

```

**Time Complexity:** O(n log n) - Merge sort complexity
**Space Complexity:** O(log n) - Recursion stack space

## Q66. 💡 Copy List with Random Pointer

**Problem:** A linked list of length `n` is given such that each node contains an additional random pointer, which could point to any node in the list, or `null`. Construct a deep copy of the list. The deep copy should consist of exactly `n` brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the `next` and `random` pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

**Approach:** Use three-pass approach: interleave cloned nodes, set random pointers, then detach cloned list.

### Solution 1: Three-Pass Interleaving (Optimal)

```javascript
function copyRandomList(head) {
  if (!head) return null;

  // Pass 1: Insert cloned nodes after each original node
  let curr = head;
  while (curr) {
    const copy = new Node(curr.val);
    copy.next = curr.next;
    curr.next = copy;
    curr = copy.next;
  }

  // Pass 2: Assign random pointers for cloned nodes
  curr = head;
  while (curr) {
    if (curr.random) {
      curr.next.random = curr.random.next;  // Clone's random = original's random's clone
    }
    curr = curr.next.next;  // Skip cloned node
  }

  // Pass 3: Separate original & cloned lists
  curr = head;
  const newHead = head.next;
  while (curr) {
    const copy = curr.next;
    curr.next = copy.next;  // Restore original next
    if (copy.next) {
      copy.next = copy.next.next;  // Clone's next = next clone
    }
    curr = curr.next;
  }

  return newHead;
}

// Test Cases:
// Input: head = [[7, null], [13, 0], [11, 4], [10, 2], [1, 0]]
// (First value is node value, second is random pointer index)
// Output: Deep copy with same structure and random pointers

// Input: head = [[1, 1], [2, 1]]
// Output: Deep copy with random pointers

// Input: head = [[3, null], [3, 0], [3, null]]
// Output: Deep copy

// Input: head = []
// Output: null

```

**Time Complexity:** O(n) - Three passes through list
**Space Complexity:** O(1) - Only using constant extra variables (excluding result)

### Solution 2: Hash Map (Alternative)

```javascript
function copyRandomListHashMap(head) {
  if (!head) return null;

  const map = new Map();
  let curr = head;

  // First pass: create all nodes
  while (curr) {
    map.set(curr, new Node(curr.val));
    curr = curr.next;
  }

  // Second pass: set next and random pointers
  curr = head;
  while (curr) {
    const copy = map.get(curr);
    copy.next = map.get(curr.next) || null;
    copy.random = map.get(curr.random) || null;
    curr = curr.next;
  }

  return map.get(head);
}

```

**Time Complexity:** O(n) - Two passes
**Space Complexity:** O(n) - Hash map storage

## Q67. 🟢 Reverse Nodes in k-Group

**Problem:** Given the head of a linked list, reverse the nodes of the list `k` at a time, and return the modified list. `k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of `k` then left-out nodes, in the end, should remain as it is. You may not alter the values in the list's nodes, only nodes themselves may be changed.

**Approach:** Check if `k` nodes exist. If yes, reverse the group in-place. Continue for each group. Leave partial groups unchanged.

### Solution 1: Group-by-Group Reversal (Optimal)

```javascript
function reverseKGroup(head, k) {
  const dummy = { next: head };
  let groupPrev = dummy;

  while (true) {
    // Check if k nodes exist
    let kth = groupPrev;
    for (let i = 0; i < k && kth; i++) {
      kth = kth.next;
    }

    if (!kth) break;  // Less than k nodes remaining

    const groupNext = kth.next;  // Save node after group

    // Reverse the k-length group
    let prev = groupNext;
    let cur = groupPrev.next;

    while (cur !== groupNext) {
      const next = cur.next;
      cur.next = prev;
      prev = cur;
      cur = next;
    }

    // Update groupPrev to point to reversed group
    const tmp = groupPrev.next;
    groupPrev.next = kth;  // kth is now head of reversed group
    groupPrev = tmp;  // Move to next group
  }

  return dummy.next;
}

// Test Cases:
// Input: head = [1, 2, 3, 4, 5], k = 2
// Output: [2, 1, 4, 3, 5]
// Explanation: Reverse groups of 2: [1,2] → [[2,1], [3,4]] → [[4,3], [5]] unchanged

// Input: head = [1, 2, 3, 4, 5], k = 3
// Output: [3, 2, 1, 4, 5]
// Explanation: Reverse first 3: [1,2,3] → [[3,2,1], [4,5]] unchanged (< k)

// Input: head = [1, 2, 3, 4, 5], k = 1
// Output: [1, 2, 3, 4, 5]
// Explanation: k=1 means no reversal needed

// Input: head = [1], k = 1
// Output: [1]

```

**Time Complexity:** O(n) - Each node visited at most twice
**Space Complexity:** O(1) - Only using constant extra variables

## Q68. 💡 Rotate List

**Problem:** Given the head of a linked list, rotate the list to the right by `k` places.

**Approach:** Connect tail to head to form a circle, find the new tail position (len - k from start), then break the circle.

### Solution 1: Circle Technique (Optimal)

```javascript
function rotateRight(head, k) {
  if (!head || !head.next || k === 0) return head;

  // Step 1: Get length and find tail
  let len = 1;
  let tail = head;
  while (tail.next) {
    tail = tail.next;
    len++;
  }

  // Step 2: Normalize k
  k %= len;
  if (k === 0) return head;

  // Step 3: Create circle
  tail.next = head;

  // Step 4: Find new tail (len - k - 1 steps from head)
  let newTail = head;
  for (let i = 0; i < len - k - 1; i++) {
    newTail = newTail.next;
  }

  // Step 5: Break circle and return new head
  const newHead = newTail.next;
  newTail.next = null;
  return newHead;
}

// Test Cases:
// Input: head = [1, 2, 3, 4, 5], k = 2
// Output: [4, 5, 1, 2, 3]
// Explanation: Rotate right by 2: last 2 nodes move to front

// Input: head = [0, 1, 2], k = 4
// Output: [2, 0, 1]
// Explanation: k=4 % 3 = 1, rotate right by 1

// Input: head = [1, 2], k = 1
// Output: [2, 1]
// Explanation: Rotate right by 1

// Input: head = [1, 2, 3], k = 0
// Output: [1, 2, 3]
// Explanation: k=0 means no rotation

```

**Time Complexity:** O(n) - Get length + find new tail
**Space Complexity:** O(1) - Only using constant extra variables

## Q69. 🟢 Delete Node in a Linked List

**Problem:** There is a singly-linked list `head` and we want to delete a node `node` in it. You are given the node to be deleted directly. You will not be given access to the first node of `head`. All the values of the linked list are unique, and it is guaranteed that the given node `node` is not the last node in the linked list. Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:

- The value of the given node should not exist in the linked list.

- The number of nodes in the linked list should decrease by one.

- All the values before `node` should be in the same order.

- All the values after `node` should be in the same order.

**Approach:** Since we can't access the previous node, copy the next node's value to the current node, then bypass the next node.

### Solution 1: Copy Value and Bypass (Optimal)

```javascript
function deleteNode(node) {
  // Copy next node's value to current node
  node.val = node.next.val;
  // Bypass next node
  node.next = node.next.next;
}

// Test Cases:
// Input: head = [4, 5, 1, 9], node = 5 (node to delete)
// Output: [4, 1, 9]
// Explanation: Copy 1 to node 5, bypass node 1

// Input: head = [4, 5, 1, 9], node = 1 (node to delete)
// Output: [4, 5, 9]
// Explanation: Copy 9 to node 1, bypass node 9

// Note: The input node is the node itself (not a value), and it's guaranteed
// that the node is not the tail node of the list.

```

**Time Complexity:** O(1) - Constant time operation
**Space Complexity:** O(1) - Only using constant extra variables

## Q70. 💡 Linked List Cycle II

**Problem:** Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return `null`. There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer.

**Approach:** First detect cycle using Floyd's algorithm. If cycle exists, move one pointer to head and step both pointers at same speed—they meet at cycle start.

### Solution 1: Floyd's Algorithm Extension (Optimal)

```javascript
function detectCycle(head) {
  if (!head || !head.next) return null;

  // Step 1: Detect cycle using Floyd's algorithm
  let slow = head;
  let fast = head;

  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
    if (slow === fast) break;  // Cycle detected
  }

  // No cycle found
  if (!fast || !fast.next) return null;

  // Step 2: Find cycle start
  // Move slow to head, step both at same speed
  slow = head;
  while (slow !== fast) {
    slow = slow.next;
    fast = fast.next;
  }

  return slow;  // Meeting point is cycle start
}

// Test Cases:
// Input: head = [3, 2, 0, -4], pos = 1 (cycle at index 1)
// Output: tail connects to node index 1

// Input: head = [1, 2], pos = 0 (cycle at index 0)
// Output: tail connects to node index 0

// Input: head = [1], pos = -1 (no cycle)
// Output: null

// Input: head = []
// Output: null

```

**Time Complexity:** O(n) - Detect cycle + find start
**Space Complexity:** O(1) - Only using constant extra variables

## Q71. 🔄 Reverse Linked List II

**Problem:** Given the head of a singly linked list and two integers `left` and `right` where `left <= right`, reverse the nodes of the list from position `left` to position `right`, and return the reversed list.

**Approach:** Use a dummy node to handle edge cases. Reverse nodes one by one by inserting the next node at the front of the reversed portion.

### Solution 1: Insert at Front Technique (Optimal)

```javascript
function reverseBetween(head, left, right) {
  const dummy = { next: head };

  // Step 1: Move to node before left position
  let prev = dummy;
  for (let i = 0; i < left - 1; i++) {
    prev = prev.next;
  }

  // Step 2: Reverse nodes from left to right
  let curr = prev.next;
  for (let i = 0; i < right - left; i++) {
    const next = curr.next;
    curr.next = next.next;      // Remove next from its position
    next.next = prev.next;      // Insert next at front of reversed portion
    prev.next = next;           // Update prev to point to new front
  }

  return dummy.next;
}

// Test Cases:
// Input: head = [1,2,3,4,5], left = 2, right = 4
// Output: [1,4,3,2,5]
// Explanation: Reverse nodes 2-4: [1,2,3,4,5] → [1,4,3,2,5]

// Input: head = [5], left = 1, right = 1
// Output: [5]
// Explanation: left = right, no reversal needed

// Input: head = [1,2,3,4,5], left = 1, right = 5
// Output: [5,4,3,2,1]
// Explanation: Reverse entire list

```

**Time Complexity:** O(n) - Traverse to right position
**Space Complexity:** O(1) - Constant extra space

## Q72. 🔀 Remove Duplicates from Sorted List II

**Problem:** Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

**Approach:** Use a dummy head. When duplicates are found, skip all nodes with that value. Only move `prev` when a unique node is found.

### Solution 1: Skip Duplicates (Optimal)

```javascript
function deleteDuplicates(head) {
  const dummy = { next: head };
  let prev = dummy;
  let curr = head;

  while (curr && curr.next) {
    if (curr.val === curr.next.val) {
      // Duplicate found - skip all nodes with this value
      const duplicateVal = curr.val;
      while (curr && curr.val === duplicateVal) {
        curr = curr.next;
      }
      // Connect prev to next non-duplicate (or null)
      prev.next = curr;
    } else {
      // Unique node - move prev forward
      prev = prev.next;
      curr = curr.next;
    }
  }

  return dummy.next;
}

// Test Cases:
// Input: head = [1,2,3,3,4,4,5]
// Output: [1,2,5]
// Explanation: Remove all nodes with duplicates (3 and 4), keep unique nodes

// Input: head = [1,1,1,2,3]
// Output: [2,3]
// Explanation: Remove all 1s (they have duplicates)

// Input: head = [1,2,2]
// Output: [1]
// Explanation: Remove all 2s, keep 1

// Input: head = [1,1,1]
// Output: []
// Explanation: All nodes are duplicates

```

**Time Complexity:** O(n) - Single pass through list
**Space Complexity:** O(1) - Constant extra space

## Q73. 💡 Partition List

**Problem:** Given the head of a linked list and a value `x`, partition it such that all nodes less than `x` come before nodes greater than or equal to `x`. You should preserve the original relative order of the nodes in each of the two partitions.

**Approach:** Use two dummy lists: one for nodes < x, one for nodes >= x. Traverse the list, appending nodes to appropriate list. Merge lists at the end.

### Solution 1: Two-List Approach (Optimal)

```javascript
function partition(head, x) {
  const beforeDummy = { next: null };
  const afterDummy = { next: null };
  let before = beforeDummy;
  let after = afterDummy;

  let curr = head;
  while (curr) {
    if (curr.val < x) {
      before.next = curr;
      before = before.next;
    } else {
      after.next = curr;
      after = after.next;
    }
    curr = curr.next;
  }

  // Connect lists and terminate
  after.next = null;  // Terminate after list
  before.next = afterDummy.next;  // Connect before to after

  return beforeDummy.next;
}

// Test Cases:
// Input: head = [1,4,3,2,5,2], x = 3
// Output: [1,2,2,4,3,5]
// Explanation: Nodes < 3: [1,2,2]; nodes >= 3: [4,3,5]

// Input: head = [2,1], x = 2
// Output: [1,2]
// Explanation: Nodes < 2: [1]; nodes >= 2: [2]

// Input: head = [1,4,3,2,5,2], x = 0
// Output: [1,4,3,2,5,2]
// Explanation: All nodes >= 0, so no change

```

**Time Complexity:** O(n) - Single pass through list
**Space Complexity:** O(1) - Constant extra space (dummy nodes)

## Q74. 💡 LRU Cache

**Problem:** Design a data structure that follows the constraints of a Least Recently Used (LRU) cache. Implement the `LRUCache` class:

- `LRUCache(int capacity)` Initialize the LRU cache with positive size `capacity`.

- `int get(int key)` Return the value of the `key` if the key exists, otherwise return `-1`.

- `void put(int key, int value)` Update the value of the `key` if the `key` exists. Otherwise, add the `key-value` pair to the cache. If the number of keys exceeds the `capacity` from this operation, evict the least recently used key.

The functions `get` and `put` must each run in `O(1)` average time complexity.

**Approach:** Use a doubly linked list to maintain order (most recent at head, least recent at tail) and a hash map for O(1) lookup. Move accessed nodes to head, remove tail when capacity exceeded.

### Solution 1: Doubly Linked List + Hash Map (Optimal)

```javascript
class LRUCache {
  constructor(capacity) {
    this.capacity = capacity;
    this.map = new Map();
    this.head = new Node(0, 0);
    this.tail = new Node(0, 0);
    this.head.next = this.tail;
    this.tail.prev = this.head;
  }

  get(key) {
    if (!this.map.has(key)) return -1;

    const node = this.map.get(key);
    this.moveToHead(node);
    return node.value;
  }

  put(key, value) {
    if (this.map.has(key)) {
      const node = this.map.get(key);
      node.value = value;
      this.moveToHead(node);
    } else {
      if (this.map.size === this.capacity) {
        this.removeTail();
      }
      const node = new Node(key, value);
      this.map.set(key, node);
      this.addToHead(node);
    }
  }

  addToHead(node) {
    node.prev = this.head;
    node.next = this.head.next;
    this.head.next.prev = node;
    this.head.next = node;
  }

  removeNode(node) {
    node.prev.next = node.next;
    node.next.prev = node.prev;
  }

  moveToHead(node) {
    this.removeNode(node);
    this.addToHead(node);
  }

  removeTail() {
    const last = this.tail.prev;
    this.removeNode(last);
    this.map.delete(last.key);
  }
}

class Node {
  constructor(key, value) {
    this.key = key;
    this.value = value;
    this.prev = null;
    this.next = null;
  }
}

// Test Cases:
// Input: [["LRUCache","put","put","get","put","get","put","get","get","get"], [2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
// Output: [null,null,null,1,null,-1,null,-1,3,4]
// Explanation:
// LRUCache lRUCache = new LRUCache(2);
// lRUCache.put(1, 1); // cache: {1=1}
// lRUCache.put(2, 2); // cache: {1=1, 2=2}
// lRUCache.get(1);    // returns 1
// lRUCache.put(3, 3); // evicts key 2, cache: {1=1, 3=3}
// lRUCache.get(2);    // returns -1 (not found)
// lRUCache.put(4, 4); // evicts key 1, cache: {4=4, 3=3}
// lRUCache.get(1);    // returns -1 (not found)
// lRUCache.get(3);    // returns 3
// lRUCache.get(4);    // returns 4

```

**Time Complexity:** O(1) - All operations average case
**Space Complexity:** O(capacity) - Map and doubly linked list storage

---

