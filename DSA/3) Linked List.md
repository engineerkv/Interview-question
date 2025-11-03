# Linked List

## Q31. Reverse Linked List

Concept:
Reverse linked list iteratively by re- pointing each node's next to previous node using three pointers.

Example:
```javascript
function reverseList(head) {
  let prev = null;
  let cur = head;
  while (cur) {
    const next = cur.next;
    cur.next = prev;
    prev = cur;
    cur = next;
  }
  return prev;
}

// Test Cases:
// Input: head = [1, 2, 3, 4, 5]
// Output: [5, 4, 3, 2, 1]

// Input: head = [1, 2]
// Output: [2, 1]

// Input: head = []
// Output: []
```

**Time Complexity:** O(n) 
  -  Single pass through all nodes  
**Space Complexity:** O(1) - Only using constant extra variables

Deep Insights:
  - Rule: Three pointers (prev, cur, next) re-point each node; reverse in-place; O(n) time, O(1) space.
  - Real-world: Linked list reversal, building blocks for complex list operations, in-place list manipulation.
  - Common mistake: Losing reference to next node; forgetting to update prev before cur; returning wrong pointer.
  - Optimization: Iterative uses O(1) space; recursive uses O(n) stack space; three-pointer prevents lost references.
  - Interview tip: Explain three-pointer technique clearly; useful as subroutine in many problems; mention recursive alternative.

## Q32. Detect Cycle

Concept:
Detect cycle in linked list using Floyd's Tortoise and Hare algorithm (two pointers moving at different speeds).

Example:
```javascript
function hasCycle(head) {
  let slow = head;
  let fast = head;
  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
    if (slow === fast) return true;
  }
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
**Space Complexity:** O(1) 
  -  Only using constant extra variables

Deep Insights:
  - Rule: Floyd's cycle detection uses fast/slow pointers (2x speed); if cycle exists, they meet; O(n) time.
  - Real-world: Cycle detection in linked structures, infinite loop detection, circular reference checking.
  - Common mistake: Fast pointer moves before null check; not handling empty list; forgetting fast.next check.
  - Optimization: O(1) space optimal; works regardless of cycle length; extends to finding cycle start.
  - Interview tip: Explain why 2x speed works; mention basis for finding cycle start; ask about proof of correctness.

## Q33. Remove Nth Node From End

Concept:
Remove nth node from end using two pointers with gap of n, dummy head handles edge cases.

Example:
```javascript
function removeNthFromEnd(head, n) {
  const dummy = { next: head };
  let slow = dummy;
  let fast = dummy;
  for (let i = 0; i < n; i++) {
    fast = fast.next;
  }
  while (fast.next) {
    slow = slow.next;
    fast = fast.next;
  }
  slow.next = slow.next.next;
  return dummy.next;
}

// Test Cases:
// Input: head = [1, 2, 3, 4, 5], n = 2
// Output: [1, 2, 3, 5]

// Input: head = [1], n = 1
// Output: []

// Input: head = [1, 2], n = 1
// Output: [1]

// Input: head = [1, 2], n = 2
// Output: [2]
```

**Time Complexity:** O(n) - Single pass with two pointers  
**Space Complexity:** O(1) 
  -  Only using constant extra variables (dummy node)

Deep Insights:
  - Rule: Two pointers with gap of n; dummy head handles edge cases; O(n) time, O(1) space.
  - Real-world: Node removal in linked structures, list manipulation, edge case handling in linked lists.
  - Common mistake: Not using dummy head causes edge case issues; not validating n within length; off-by-one errors.
  - Optimization: Dummy head avoids edge case branching; works for n == length; handles removing head gracefully.
  - Interview tip: Explain gap technique clearly; mention dummy head simplifies edge cases; validate n if needed.

## Q34. Merge Two Sorted Lists

Concept:
Merge two sorted lists iteratively by stitching smaller head each step using tail pointer.

Example:
```javascript
function mergeTwoLists(l1, l2) {
  const dummy = { next: null };
  let tail = dummy;
  while (l1 && l2) {
    if (l1.val <= l2.val) {
      tail.next = l1;
      l1 = l1.next;
    } else {
      tail.next = l2;
      l2 = l2.next;
    }
    tail = tail.next;
  }
  tail.next = l1 || l2;
  return dummy.next;
}

// Test Cases:
// Input: l1 = [1, 2, 4], l2 = [1, 3, 4]
// Output: [1, 1, 2, 3, 4, 4]

// Input: l1 = [], l2 = []
// Output: []

// Input: l1 = [], l2 = [0]
// Output: [0]

// Input: l1 = [1], l2 = [2]
// Output: [1, 2]
```

**Time Complexity:** O(m + n) 
  -  Merge pass through both lists where m and n are list lengths  
**Space Complexity:** O(1) - Only using constant extra variables (dummy node)

Deep Insights:
  - Rule: Dummy head + tail pointer stitches smaller heads; merge in-place; O(m+n) time, O(1) space.
  - Real-world: Merge sort for linked lists, combining sorted lists, in-place list merging, external sorting.
  - Common mistake: Not handling empty lists; forgetting to append remaining list; dummy head technique not used.
  - Optimization: In-place merge optimal; dummy head simplifies edge cases; building block for merge sort.
  - Interview tip: Explain dummy head technique clearly; mention merge sort application; handle remaining list.

## Q35. Middle of Linked List

Concept:
Find middle node using fast pointer (2x speed) and slow pointer, slow ends at middle.

Example:
```javascript
function middleNode(head) {
  let slow = head;
  let fast = head;
  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
  }
  return slow;
}

// Test Cases:
// Input: head = [1, 2, 3, 4, 5]
// Output: [3, 4, 5]

// Input: head = [1, 2, 3, 4, 5, 6]
// Output: [4, 5, 6]

// Input: head = [1]
// Output: [1]

// Input: head = [1, 2]
// Output: [2]
```

Deep Insights:
  - Rule: Fast/slow pointers (2x speed); slow ends at middle when fast reaches end; O(n) time, O(1) space.
  - Real-world: Finding middle element, list splitting, divide-and-conquer operations, list partitioning.
  - Common mistake: Fast pointer moves before null check; not handling empty list; even-length convention unclear.
  - Optimization: O(1) space optimal; single pass solution; even-length returns later middle (standard convention).
  - Interview tip: Explain two-pointer technique clearly; ask about even-length convention; mention list splitting use.

## Q36. Palindrome Linked List

Concept:
Check if linked list is palindrome by finding middle, reversing second half, then comparing halves.

Example:
```javascript
function isPalindrome(head) {
  if (!head || !head.next) return true;

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

  // Find middle using fast/slow pointers
  let slow = head;
  let fast = head;
  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
  }

  // Reverse second half
  let second = reverse(slow);
  let first = head;

  // Compare halves
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

// Input: head = [1, 2]
// Output: false

// Input: head = [1]
// Output: true

// Input: head = [1, 2, 3, 2, 1]
// Output: true
```

**Time Complexity:** O(n) - Finding middle + reversing + comparing  
**Space Complexity:** O(1) - In-place reversal, constant extra space

Deep Insights:
  - Rule: Find middle, reverse second half, compare halves; O(n) time, O(1) space if not restoring original.
  - Real-world: Palindrome validation in linked structures, symmetry checking, list validation algorithms.
  - Common mistake: Not handling empty/single node lists; forgetting to restore original list if required; comparing wrong halves.
  - Optimization: O(1) space if not restoring; restore original list after check if needed; avoids array conversion.
  - Interview tip: Explain three-step process clearly; ask if original list should be restored; mention space optimization.

## Q37. Flatten Multilevel LL

Concept:
Flatten multilevel linked list using iterative DFS with stack to remember next nodes when processing child pointers.

```javascript
function flatten(head) {
  if (!head) return head;
  const stack = [];
  let cur = head;
  while (cur) {
    if (cur.child) {
      if (cur.next) {
        stack.push(cur.next);
      }
      cur.next = cur.child;
      cur.child.prev = cur;
      cur.child = null;
    }
    if (!cur.next && stack.length) {
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

Deep Insights:
  - Rule: Iterative DFS with stack stores deferred next nodes; process child first, then next; O(n) time, O(k) space.
  - Real-world: Multilevel list flattening, tree flattening, hierarchical structure processing, nested list handling.
  - Common mistake: Not handling empty list; forgetting to clear child pointers; incorrect stack usage.
  - Optimization: Stack stores k deferred nodes; in-place flattening; pre-order style processing.
  - Interview tip: Explain stack usage clearly; mention pre-order traversal style; ask about restoring original structure.

## Q38. Intersection of Two LL

Concept:
Find intersection node by switching heads when reaching end to equalize path lengths, meeting point is intersection.

```javascript
function getIntersectionNode(a, b) {
  if (!a || !b) return null;
  let p = a;
  let q = b;
  while (p !== q) {
    p = p ? p.next : b;
    q = q ? q.next : a;
  }
  return p;
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

Deep Insights:
  - Rule: Switch heads when reaching end to equalize path lengths; meeting point is intersection; O(m+n) time.
  - Real-world: Finding common nodes in linked structures, shared path detection, intersection algorithms.
  - Common mistake: Not handling null lists; missing intersection detection; incorrect switching logic.
  - Optimization: O(1) space optimal; ends at null when no intersection; both pointers traverse same total distance.
  - Interview tip: Explain why switching works clearly; mention total distance equality; ask about cycle detection.

## Q39. Add Two Numbers (LL)

Concept:
Add two numbers represented as linked lists digit
  - wise with carry, building result list from least significant digit.

```javascript
function addTwoNumbers(l1, l2) {
  const dummy = { next: null };
  let tail = dummy;
  let carry = 0;

  while (l1 || l2 || carry) {
    const v = (l1 ? l1.val : 0) + (l2 ? l2.val : 0) + carry;
    tail.next = { val: v % 10, next: null };
    tail = tail.next;
    carry = Math.floor(v / 10);
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

// Input: l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9]
// Output: [8, 9, 9, 9, 0, 0, 0, 1]
// Explanation: 9999999 + 9999 = 10009998
```

Deep Insights:
  - Rule: Digit-wise addition with carry; dummy head builds result list; O(max(m,n)) time, O(1) space.
  - Real-world: Large number arithmetic, calculator systems, numerical computations, big integer operations.
  - Common mistake: Not handling final carry; forgetting to create new nodes; wrong carry propagation.
  - Optimization: Simple loop covers all cases; handles uneven lengths and final carry automatically; create new nodes.
  - Interview tip: Explain carry handling clearly; mention school addition analogy; ask about negative numbers if needed.

## Q40. Sort LL

Concept:
Sort linked list using merge sort by splitting at middle, recursively sorting halves, then merging.

```javascript
function sortList(head) {
  if (!head || !head.next) return head;

  // Split by mid
  let slow = head;
  let fast = head;
  let prev = null;
  while (fast && fast.next) {
    prev = slow;
    slow = slow.next;
    fast = fast.next.next;
  }
  prev.next = null;

  const left = sortList(head);
  const right = sortList(slow);
  return merge(left, right);

  function merge(a, b) {
    const dummy = { next: null };
    let t = dummy;
    while (a && b) {
      if (a.val <= b.val) {
        t.next = a;
        a = a.next;
      } else {
        t.next = b;
        b = b.next;
      }
      t = t.next;
    }
    t.next = a || b;
    return dummy.next;
  }
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

Deep Insights:
  - Rule: Merge sort: split at middle, recursively sort halves, merge; O(n log n) time, O(log n) stack space.
  - Real-world: Linked list sorting, stable sorting algorithms, divide-and-conquer sorting, in-place sorting.
  - Common mistake: Not handling empty/single node lists; incorrect split logic; forgetting to merge.
  - Optimization: Stable due to merge order; O(log n) stack space vs O(n) array space; no extra array needed.
  - Interview tip: Explain why merge sort is natural for linked lists; mention stability; compare with array sorting.

## Q41. Clone LL with Random Pointer

Concept:
Clone linked list with random pointers by interleaving nodes, setting random pointers, then detaching cloned list.

```javascript
var copyRandomList = function(head) {
  if (!head) return null;

  // 1) Insert cloned nodes after each original node
  let curr = head;
  while (curr) {
    let copy = new Node(curr.val);
    copy.next = curr.next;
    curr.next = copy;
    curr = copy.next;
  }

  // 2) Assign random pointers for cloned nodes
  curr = head;
  while (curr) {
    if (curr.random) {
      curr.next.random = curr.random.next;
    }
    curr = curr.next.next;
  }

  // 3) Separate original & cloned lists
  curr = head;
  let newHead = head.next;
  while (curr) {
    let copy = curr.next;
    curr.next = copy.next;
    if (copy.next) {
      copy.next = copy.next.next;
    }
    curr = curr.next;
  }

  return newHead;
};

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

Deep Insights:
  - Rule: Three-pass approach: interleave nodes, set random pointers, detach cloned list; O(n) time, O(1) space.
  - Real-world: Linked list cloning, deep copying with references, graph cloning, random pointer structures.
  - Common mistake: Not handling null random pointers; incorrect pointer hops during detachment; wrong interleaving.
  - Optimization: O(1) space vs O(n) map-based approach; careful pointer hops needed; three-pass is cleaner.
  - Interview tip: Explain three-pass approach clearly; mention map-based alternative; ask about null random pointers.

## Q42. Reverse Nodes in K- Group

Concept:
Reverse each k
  - length block in- place, leaving last partial block unchanged if less than k nodes.

```javascript
function reverseKGroup(head, k) {
  const dummy = { next: head };
  let groupPrev = dummy;

  while (true) {
    let kth = groupPrev;
    for (let i = 0; i < k && kth; i++) {
      kth = kth.next;
    }
    if (!kth) break;

    const groupNext = kth.next;
    // Reverse group
    let prev = groupNext;
    let cur = groupPrev.next;
    while (cur !== groupNext) {
      const next = cur.next;
      cur.next = prev;
      prev = cur;
      cur = next;
    }
    const tmp = groupPrev.next;
    groupPrev.next = kth;
    groupPrev = tmp;
  }
  return dummy.next;
}

// Test Cases:
// Input: head = [1, 2, 3, 4, 5], k = 2
// Output: [2, 1, 4, 3, 5]

// Input: head = [1, 2, 3, 4, 5], k = 3
// Output: [3, 2, 1, 4, 5]

// Input: head = [1, 2, 3, 4, 5], k = 1
// Output: [1, 2, 3, 4, 5]

// Input: head = [1], k = 1
// Output: [1]
```

Deep Insights:
  - Rule: Reverse each k-length block in-place; check if k nodes exist before reversing; O(n) time, O(1) space.
  - Real-world: Block-wise list operations, k-group transformations, pattern matching in linked lists.
  - Common mistake: Not handling partial groups; incorrect boundary handling; forgetting to check k nodes.
  - Optimization: In-place reversal; last partial group untouched; careful boundary handling needed.
  - Interview tip: Explain boundary handling clearly; mention reverse process within k-length window; ask about partial groups.

## Q43. Rotate List

Concept:
Rotate list right by k by connecting tail to head (circle), finding new tail position, then breaking circle.

```javascript
function rotateRight(head, k) {
  if (!head || !head.next || k === 0) return head;

  // Get length and tail
  let len = 1;
  let tail = head;
  while (tail.next) {
    tail = tail.next;
    len++;
  }

  k %= len;
  if (k === 0) return head;

  tail.next = head; // Create circle
  let steps = len - k - 1;
  let newTail = head;
  while (steps--) {
    newTail = newTail.next;
  }

  const newHead = newTail.next;
  newTail.next = null;
  return newHead;
}

// Test Cases:
// Input: head = [1, 2, 3, 4, 5], k = 2
// Output: [4, 5, 1, 2, 3]

// Input: head = [0, 1, 2], k = 4
// Output: [2, 0, 1]

// Input: head = [1, 2], k = 1
// Output: [2, 1]

// Input: head = [1, 2, 3], k = 0
// Output: [1, 2, 3]
```

Deep Insights:
  - Rule: Connect tail to head (circle), find new tail position, break circle; O(n) time, O(1) space.
  - Real-world: List rotation, circular buffer operations, rotation algorithms, cyclic list operations.
  - Common mistake: Not handling k==0; incorrect circle breaking; forgetting to normalize k %= len.
  - Optimization: Early return for k==0; temporary cycle makes rotation straightforward; O(1) space optimal.
  - Interview tip: Explain circle technique clearly; mention k normalization; ask about left vs right rotation.

## Q44. Delete Node w/o Head Pointer

Concept:
Delete node without head pointer by copying next node's value to current node and bypassing next node.

```javascript
function deleteNode(node) {
  node.val = node.next.val;
  node.next = node.next.next;
}

// Test Cases:
// Input: head = [4, 5, 1, 9], node = 5 (node to delete)
// Output: [4, 1, 9]

// Input: head = [4, 5, 1, 9], node = 1 (node to delete)
// Output: [4, 5, 9]

// Note: The input node is the node itself (not a value), and it's guaranteed
// that the node is not the tail node of the list.
```

Deep Insights:
  - Rule: Copy next node's value to current node, bypass next node; O(1) time, O(1) space.
  - Real-world: Node deletion without head, in-place node removal, pointer manipulation tricks.
  - Common mistake: Not handling tail node (assumes non-tail); forgetting to bypass next node.
  - Optimization: O(1) time optimal; simple trick but limited to non-tail nodes; problem constraint ensures validity.
  - Interview tip: Explain limitation clearly; mention only works for non-tail nodes; ask about tail node handling.

## Q45. Find Start Node of Cycle

Concept:
Find cycle start by first detecting cycle with Floyd's algorithm, then moving one pointer to head and stepping both to meet.

```javascript
function detectCycle(head) {
  let slow = head;
  let fast = head;
  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
    if (slow === fast) break;
  }
  if (!fast || !fast.next) return null;
  slow = head;
  while (slow !== fast) {
    slow = slow.next;
    fast = fast.next;
  }
  return slow;
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

Deep Insights:
  - Rule: Detect cycle with Floyd's, then move one pointer to head, step both to meet; O(n) time, O(1) space.
  - Real-world: Cycle detection in linked structures, circular reference finding, loop identification.
  - Common mistake: Not handling null lists; incorrect meet point calculation; forgetting to move pointer to head.
  - Optimization: O(1) space optimal; works regardless of cycle length; returns null when no cycle.
  - Interview tip: Explain mathematical proof clearly; mention distance equality; ask about correctness proof.

## Q46. Reverse Linked List II

Concept:
Reverse portion of list from position left to right; use dummy node and four pointers.

Example:
```javascript
function reverseBetween(head, left, right) {
  const dummy = new ListNode(0);
  dummy.next = head;
  
  let prev = dummy;
  for (let i = 0; i < left - 1; i++) {
    prev = prev.next;
  }
  
  let curr = prev.next;
  for (let i = 0; i < right - left; i++) {
    const next = curr.next;
    curr.next = next.next;
    next.next = prev.next;
    prev.next = next;
  }
  
  return dummy.next;
}

// Input: head = [1,2,3,4,5], left = 2, right = 4
// Output: [1,4,3,2,5]
// Explanation: Reverse nodes 2-4

// Input: head = [5], left = 1, right = 1
// Output: [5]

// Input: head = [1,2,3,4,5], left = 1, right = 5
// Output: [5,4,3,2,1]
```

**Time Complexity:** O(n) - Traverse to right position  
**Space Complexity:** O(1) - Constant extra space

Deep Insights:
- Use dummy node for edge cases; reverse nodes one by one; O(n) time, O(1) space.
- Move curr forward while inserting next at front of reversed portion.
- Four pointers: prev (before reversed), curr (last in reversed), next (to insert).
- Edge case: left = 1 reverses from head; left = right returns unchanged.
- Interview tip: Explain pointer manipulation clearly; mention dummy node usage.

## Q47. Remove Duplicates from Sorted List II

Concept:
Remove all duplicates (including original) from sorted list; track prev pointer and compare three consecutive nodes.

Example:
```javascript
function deleteDuplicates(head) {
  const dummy = new ListNode(0);
  dummy.next = head;
  
  let prev = dummy;
  let curr = head;
  
  while (curr && curr.next) {
    if (curr.val === curr.next.val) {
      const duplicateVal = curr.val;
      while (curr && curr.val === duplicateVal) {
        curr = curr.next;
      }
      prev.next = curr;
    } else {
      prev = prev.next;
      curr = curr.next;
    }
  }
  
  return dummy.next;
}

// Input: head = [1,2,3,3,4,4,5]
// Output: [1,2,5]
// Explanation: Remove all nodes with duplicates (3 and 4)

// Input: head = [1,1,1,2,3]
// Output: [2,3]
// Explanation: Remove all 1s

// Input: head = [1,2,2]
// Output: [1]
```

**Time Complexity:** O(n) - Single pass through list  
**Space Complexity:** O(1) - Constant extra space

Deep Insights:
- Use dummy node; skip all nodes with duplicate values; connect prev to next non-duplicate; O(n) time, O(1) space.
- When duplicates found, skip all nodes with that value; don't move prev until unique.
- Compare current with next; if equal, skip all consecutive duplicates.
- Edge case: All duplicates returns null; no duplicates returns original.
- Interview tip: Explain dummy node usage; mention skipping all duplicates.

## Q48. Partition List

Concept:
Partition list such that all nodes < x come before nodes >= x; maintain relative order within each partition.

Example:
```javascript
function partition(head, x) {
  const beforeDummy = new ListNode(0);
  const afterDummy = new ListNode(0);
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
  
  after.next = null;
  before.next = afterDummy.next;
  
  return beforeDummy.next;
}

// Input: head = [1,4,3,2,5,2], x = 3
// Output: [1,2,2,4,3,5]
// Explanation: Nodes < 3: [1,2,2]; nodes >= 3: [4,3,5]

// Input: head = [2,1], x = 2
// Output: [1,2]
// Explanation: Nodes < 2: [1]; nodes >= 2: [2]

// Input: head = [1,4,3,2,5,2], x = 0
// Output: [1,4,3,2,5,2]
// Explanation: All nodes >= 0
```

**Time Complexity:** O(n) - Single pass through list  
**Space Complexity:** O(1) - Constant extra space

Deep Insights:
- Use two dummy lists: before (val < x) and after (val >= x); merge at end; O(n) time, O(1) space.
- Maintain two lists separately; connect after next to null; link before to after.
- Preserves relative order within each partition.
- Edge case: All nodes < x or all >= x; empty list returns null.
- Interview tip: Explain two-list approach; mention order preservation.

## Q49. LRU Cache

Concept:
Design LRU cache with O(1) get and put; use doubly linked list + hash map for O(1) operations.

Example:
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
//
// Example 1:
//   Input: ["LRUCache","put","put","get","put","get","put","get","get","get"]
//          [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
//   Output: [null,null,null,1,null,-1,null,-1,3,4]
//   Explanation: 
//     LRUCache lRUCache = new LRUCache(2);
//     lRUCache.put(1, 1); // cache: {1=1}
//     lRUCache.put(2, 2); // cache: {1=1, 2=2}
//     lRUCache.get(1);    // returns 1
//     lRUCache.put(3, 3); // evicts key 2, cache: {1=1, 3=3}
//     lRUCache.get(2);    // returns -1 (not found)
//     lRUCache.put(4, 4); // evicts key 1, cache: {4=4, 3=3}
//     lRUCache.get(1);    // returns -1 (not found)
//     lRUCache.get(3);    // returns 3
//     lRUCache.get(4);    // returns 4
```

**Time Complexity:** O(1) - All operations average case  
**Space Complexity:** O(capacity) - Map and list storage

Deep Insights:
- Use doubly linked list for O(1) remove/insert; hash map for O(1) lookup; O(1) operations.
- Move accessed node to head; remove from tail when full; maintain order with doubly linked list.
- Head = most recently used; tail = least recently used.
- Edge case: Capacity 0; empty cache get returns -1.
- Interview tip: Explain doubly linked list choice; mention head/tail sentinels; describe eviction strategy.
