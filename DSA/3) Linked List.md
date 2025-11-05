# Linked List

## Q56. Reverse Linked List

**Problem:** Given the head of a singly linked list, reverse the list, and return the reversed list.

**Approach:** Use three pointers: `prev`, `cur`, and `next`. Iteratively re-point each node's `next` to the previous node.

### Solution 1: Iterative (Optimal)
```javascript
function reverseList(head) {
  let prev = null;
  let cur = head;
  
  while (cur) {
    const next = cur.next;  // Save next node
    cur.next = prev;        // Reverse pointer
    prev = cur;             // Move prev forward
    cur = next;             // Move cur forward
  }
  
  return prev;  // prev is now the new head
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
  if (!head || !head.next) return head;
  
  const reversed = reverseListRecursive(head.next);
  head.next.next = head;
  head.next = null;
  
  return reversed;
}
```

**Time Complexity:** O(n) - Recursive calls for each node  
**Space Complexity:** O(n) - Recursion stack

**Deep Insights:**
- **Optimal Approach:** Iterative achieves O(n) time and O(1) space—optimal for this problem
- **Three-Pointer Technique:** `prev`, `cur`, `next` prevent lost references during reversal
- **Key Insight:** Save `next` before modifying `cur.next` to avoid losing the reference
- **In-Place Reversal:** No extra space needed for new list—just re-point pointers
- **Edge Cases:** Empty list returns null; single node returns itself
- **Interview Tip:** Explain three-pointer technique clearly; mention this is a building block for many problems; compare iterative vs recursive

## Q57. Linked List Cycle

**Problem:** Given `head`, the head of a linked list, determine if the linked list has a cycle in it. There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. Note that `pos` is not passed as a parameter. Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

**Approach:** Use Floyd's Tortoise and Hare algorithm (two pointers). Fast pointer moves at 2x speed. If cycle exists, pointers will meet.

### Solution 1: Floyd's Cycle Detection (Optimal)
```javascript
function hasCycle(head) {
  if (!head || !head.next) return false;
  
  let slow = head;
  let fast = head;
  
  while (fast && fast.next) {
    slow = slow.next;       // Move 1 step
    fast = fast.next.next;  // Move 2 steps
    
    if (slow === fast) {
      return true;  // Cycle detected
    }
  }
  
  return false;  // No cycle
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
  const seen = new Set();
  let cur = head;
  
  while (cur) {
    if (seen.has(cur)) {
      return true;
    }
    seen.add(cur);
    cur = cur.next;
  }
  
  return false;
}
```

**Time Complexity:** O(n) - Single pass  
**Space Complexity:** O(n) - Hash set storage

**Deep Insights:**
- **Optimal Approach:** Floyd's algorithm achieves O(n) time and O(1) space—optimal for this problem
- **Why 2x Speed Works:** If cycle exists, fast pointer will eventually catch up to slow pointer
- **Mathematical Proof:** Distance between pointers decreases by 1 each iteration when both are in cycle
- **Key Insight:** Fast pointer moves 2 steps, slow moves 1 step—ensures they meet if cycle exists
- **Edge Cases:** Empty list returns false; single node with no cycle returns false
- **Interview Tip:** Explain why 2x speed works; mention this extends to finding cycle start (Q70); ask about proof

## Q58. Remove Nth Node From End of List

**Problem:** Given the head of a linked list, remove the `n`th node from the end of the list and return its head.

**Approach:** Use two pointers with a gap of `n` nodes. Use a dummy head to handle edge cases (like removing the head node).

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

**Deep Insights:**
- **Optimal Approach:** Two pointers with gap achieves O(n) time and O(1) space—optimal for this problem
- **Gap Technique:** Maintain `n` node gap between fast and slow pointers—when fast reaches end, slow is at node before target
- **Dummy Head:** Simplifies edge cases—handles removing head node without special cases
- **Key Insight:** Fast pointer moves `n` steps ahead, then both move together—ensures correct position
- **Edge Cases:** Removing head node (n = length); single node list; n = 1 (remove last node)
- **Interview Tip:** Explain gap technique clearly; emphasize dummy head benefits; mention validation if n > length

## Q59. Merge Two Sorted Lists

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

**Deep Insights:**
- **Optimal Approach:** Iterative merge achieves O(m+n) time and O(1) space—optimal for this problem
- **Dummy Head Technique:** Simplifies edge cases—no need to check if result is empty
- **Tail Pointer:** Maintains reference to end of merged list for O(1) appends
- **In-Place Merge:** Reuses existing nodes—no new nodes created
- **Remaining List:** After one list exhausted, append remaining nodes directly
- **Interview Tip:** Explain dummy head and tail pointer clearly; mention this is building block for merge sort; handle remaining list

## Q60. Middle of the Linked List

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

**Deep Insights:**
- **Optimal Approach:** Fast/slow pointers achieve O(n) time and O(1) space—optimal for this problem
- **Why It Works:** Fast pointer moves 2x speed—when it reaches end, slow is at middle
- **Even Length Convention:** Returns second middle node when even length (standard convention)
- **Key Insight:** Fast pointer checks `fast && fast.next` to handle both odd and even lengths
- **Edge Cases:** Single node returns itself; empty list handled by while condition
- **Interview Tip:** Explain two-pointer technique clearly; ask about even-length convention; mention list splitting applications

## Q61. Palindrome Linked List

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

**Deep Insights:**
- **Optimal Approach:** Three-step process achieves O(n) time and O(1) space—optimal for this problem
- **Three Steps:** Find middle, reverse second half, compare halves
- **Key Insight:** Only need to compare first half with reversed second half—no need to reverse entire list
- **Space Optimization:** O(1) space if not restoring original list; O(1) to restore if needed
- **Edge Cases:** Empty list returns true; single node returns true; odd length handled correctly
- **Interview Tip:** Explain three-step process clearly; ask if original list should be restored; mention space optimization vs array conversion

## Q62. Flatten a Multilevel Doubly Linked List

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

**Deep Insights:**
- **Optimal Approach:** Iterative DFS achieves O(n) time—optimal for this problem
- **Stack Usage:** Stack stores deferred `next` nodes when processing `child` pointers
- **Pre-Order Style:** Process child first, then continue with next—similar to pre-order traversal
- **Key Insight:** When `child` exists, save `next` to stack, flatten child, then process deferred nodes
- **In-Place Flattening:** Modifies list in-place—clear `child` pointers after flattening
- **Interview Tip:** Explain stack usage clearly; mention pre-order traversal style; ask about restoring original structure

## Q63. Intersection of Two Linked Lists

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

**Deep Insights:**
- **Optimal Approach:** Switch heads technique achieves O(m+n) time and O(1) space—optimal for this problem
- **Why It Works:** Both pointers traverse same total distance (m + n)—ensures they meet at intersection if it exists
- **Path Equalization:** Switching heads when reaching end equalizes path lengths without calculating lengths
- **Key Insight:** If intersection exists, pointers meet at intersection; if not, both become null simultaneously
- **Edge Cases:** Empty lists return null; no intersection returns null; single node intersection works
- **Interview Tip:** Explain why switching works (total distance equality); mention this is more elegant than calculating lengths

## Q64. Add Two Numbers

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

**Deep Insights:**
- **Optimal Approach:** Digit-wise addition achieves O(max(m,n)) time—optimal for this problem
- **Carry Handling:** Add carry from previous digit, compute new digit and carry for next iteration
- **Key Insight:** Loop continues while `l1`, `l2`, or `carry` exists—handles final carry automatically
- **New Nodes:** Create new nodes for result—don't modify input lists
- **Edge Cases:** Final carry creates new node; uneven lengths handled with null checks; zero sum returns [0]
- **Interview Tip:** Explain carry handling clearly; mention school addition analogy; ask about negative numbers if needed

## Q65. Sort List

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

**Deep Insights:**
- **Optimal Approach:** Merge sort achieves O(n log n) time—optimal for comparison-based sorting
- **Why Merge Sort:** Natural for linked lists—no random access needed, efficient merging
- **Three Steps:** Split at middle, recursively sort halves, merge sorted halves
- **Stability:** Merge sort is stable—preserves relative order of equal elements
- **Space Advantage:** O(log n) stack space vs O(n) array space for array merge sort
- **Interview Tip:** Explain why merge sort is natural for linked lists; mention stability; compare with array sorting

## Q66. Copy List with Random Pointer

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

**Deep Insights:**
- **Optimal Approach:** Three-pass interleaving achieves O(n) time and O(1) space—optimal for this problem
- **Key Trick:** Interleave cloned nodes to maintain relationship between original and clone
- **Random Pointer:** `curr.next.random = curr.random.next`—clone's random points to clone of original's random
- **Separation:** Carefully restore original list and connect cloned nodes
- **Edge Cases:** Null random pointers handled correctly; empty list returns null
- **Interview Tip:** Explain three-pass approach clearly; mention hash map alternative (O(n) space); emphasize pointer manipulation

## Q67. Reverse Nodes in k-Group

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
// Explanation: Reverse groups of 2: [1,2] → [2,1], [3,4] → [4,3], [5] unchanged

// Input: head = [1, 2, 3, 4, 5], k = 3
// Output: [3, 2, 1, 4, 5]
// Explanation: Reverse first 3: [1,2,3] → [3,2,1], [4,5] unchanged (< k)

// Input: head = [1, 2, 3, 4, 5], k = 1
// Output: [1, 2, 3, 4, 5]
// Explanation: k=1 means no reversal needed

// Input: head = [1], k = 1
// Output: [1]
```

**Time Complexity:** O(n) - Each node visited at most twice  
**Space Complexity:** O(1) - Only using constant extra variables

**Deep Insights:**
- **Optimal Approach:** Group-by-group reversal achieves O(n) time and O(1) space—optimal for this problem
- **Boundary Check:** Always check if `k` nodes exist before reversing—partial groups remain unchanged
- **In-Place Reversal:** Reverse each group in-place using standard three-pointer technique
- **Key Insight:** After reversing, `kth` becomes head of reversed group—connect previous group to it
- **Edge Cases:** k=1 returns original list; k >= length reverses entire list; partial groups unchanged
- **Interview Tip:** Explain boundary handling clearly; mention reverse process within k-length window; ask about partial groups

## Q68. Rotate List

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

**Deep Insights:**
- **Optimal Approach:** Circle technique achieves O(n) time and O(1) space—optimal for this problem
- **Circle Trick:** Temporarily connect tail to head—makes rotation straightforward
- **Key Insight:** New tail is at position `len - k - 1` from head—new head is next node
- **K Normalization:** Use `k %= len` to handle k >= length—avoid unnecessary rotations
- **Edge Cases:** k=0 returns original list; k=length returns original list; single node returns itself
- **Interview Tip:** Explain circle technique clearly; mention k normalization; ask about left vs right rotation

## Q69. Delete Node in a Linked List

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

**Deep Insights:**
- **Optimal Approach:** Copy and bypass achieves O(1) time—optimal for this problem
- **Key Trick:** Copy next node's value, then bypass next node—effectively deletes current node
- **Limitation:** Only works for non-tail nodes—problem guarantees node is not tail
- **Why It Works:** We can't delete the node itself (no access to previous), but we can make it "become" the next node
- **Edge Cases:** Problem guarantees node is not tail; single node list not possible (node would be tail)
- **Interview Tip:** Explain limitation clearly; mention this trick only works for non-tail nodes; ask about tail node handling

## Q70. Linked List Cycle II

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

**Deep Insights:**
- **Optimal Approach:** Floyd's algorithm extension achieves O(n) time and O(1) space—optimal for this problem
- **Mathematical Proof:** When fast and slow meet, distance from head to cycle start equals distance from meet point to cycle start
- **Two Steps:** First detect cycle, then find cycle start by moving one pointer to head
- **Key Insight:** After meeting, moving slow to head and stepping both at same speed ensures they meet at cycle start
- **Edge Cases:** No cycle returns null; cycle at head returns head; single node cycle works
- **Interview Tip:** Explain mathematical proof clearly; mention distance equality; ask about correctness proof

## Q71. Reverse Linked List II

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

**Deep Insights:**
- **Optimal Approach:** Insert-at-front technique achieves O(n) time and O(1) space—optimal for this problem
- **Key Technique:** Move `curr` forward while inserting `next` at the front of the reversed portion
- **Four Pointers:** `prev` (before reversed), `curr` (last in reversed), `next` (to insert), `dummy` (handles edge cases)
- **Dummy Node:** Simplifies edge cases—handles reversing from head (left = 1)
- **Edge Cases:** left = 1 reverses from head; left = right returns unchanged; reversing entire list works
- **Interview Tip:** Explain pointer manipulation clearly; mention dummy node benefits; emphasize insert-at-front technique

## Q72. Remove Duplicates from Sorted List II

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

**Deep Insights:**
- **Optimal Approach:** Skip duplicates technique achieves O(n) time and O(1) space—optimal for this problem
- **Key Strategy:** When duplicate found, skip all consecutive nodes with that value—don't move `prev` until unique node
- **Dummy Head:** Simplifies edge cases—handles removing head node gracefully
- **Comparison:** Compare `curr.val` with `curr.next.val`—if equal, all nodes with this value are duplicates
- **Edge Cases:** All duplicates returns null; no duplicates returns original; single node returns itself
- **Interview Tip:** Explain dummy node usage; emphasize skipping all duplicates (not just one); mention difference from Remove Duplicates I

## Q73. Partition List

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

**Deep Insights:**
- **Optimal Approach:** Two-list approach achieves O(n) time and O(1) space—optimal for this problem
- **Two Lists:** Maintain separate lists for nodes < x and nodes >= x—preserves relative order
- **Key Insight:** Traverse once, append to appropriate list—no need to sort or rearrange
- **Termination:** Set `after.next = null` to terminate the after list
- **Edge Cases:** All nodes < x returns original; all nodes >= x returns original; empty list returns null
- **Interview Tip:** Explain two-list approach clearly; emphasize order preservation within partitions

## Q74. LRU Cache

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
// Input: ["LRUCache","put","put","get","put","get","put","get","get","get"], [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
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

**Deep Insights:**
- **Optimal Approach:** Doubly linked list + hash map achieves O(1) for all operations—optimal for this problem
- **Why Doubly Linked List:** Enables O(1) insertion and deletion at both ends (head and tail)
- **Hash Map:** Provides O(1) lookup to find nodes quickly
- **Order Maintenance:** Most recently used at head, least recently used at tail
- **Key Operations:** Move to head on access, remove tail when capacity exceeded
- **Edge Cases:** Capacity = 1 works; get non-existent key returns -1; update existing key moves to head
- **Interview Tip:** Explain doubly linked list benefits; mention why singly linked list won't work (can't remove from tail in O(1)); emphasize O(1) requirement
