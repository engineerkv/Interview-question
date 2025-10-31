# Linked List

## Q31. Reverse Linked List

- Concept: Iteratively re-point `next` to previous node, moving forward one by one. Handles null and single-node lists naturally.

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
```

- Deep Insights:
  - O(n) time, O(1) space.
  - Watch pointer order to avoid losing nodes.
  - Recursive variant uses call stack.
  - Useful as a subroutine in many LL problems.

## Q32. Detect Cycle

- Concept: Floyd’s Tortoise and Hare; fast meets slow if a cycle exists. Use set for simplicity, two pointers for O(1) space.

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
```

- Deep Insights:
  - O(n) time, O(1) space.
  - Meeting guarantees a cycle; otherwise ends at null.
  - Works regardless of cycle length.
  - Basis for finding cycle start.

## Q33. Remove Nth Node From End

- Concept: Two-pointer gap of n; move both until fast hits end, then remove slow.next. Dummy head handles removing the first node.

```javascript
function removeNthFromEnd(head, n) {
  const dummy = { next: head };
  let slow = dummy;
  let fast = dummy;
  for (let i = 0; i < n; i++) fast = fast.next;
  while (fast.next) {
    slow = slow.next;
    fast = fast.next;
  }
  slow.next = slow.next.next;
  return dummy.next;
}
```

- Deep Insights:
  - One pass with O(1) space.
  - Dummy avoids edge-case branching.
  - Validate n within length if needed.
  - Works for n == length (remove head).

## Q34. Merge Two Sorted Lists

- Concept: Iteratively stitch the smaller head each step using a tail pointer. Stable merge, O(m+n) time.

```javascript
function mergeTwoLists(l1, l2) {
  const dummy = { next: null };
  let tail = dummy;
  while (l1 && l2) {
    if (l1.val <= l2.val) { tail.next = l1; l1 = l1.next; }
    else { tail.next = l2; l2 = l2.next; }
    tail = tail.next;
  }
  tail.next = l1 || l2;
  return dummy.next;
}
```

- Deep Insights:
  - In-place: reuse existing nodes.
  - Equal values keep order (stable).
  - Use recursion if acceptable.
  - Building block for sort list.

## Q35. Middle of Linked List

- Concept: Fast pointer moves 2×; when it ends, slow is at middle. Return second middle for even length per common spec.

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
```

- Deep Insights:
  - O(n) time, O(1) space.
  - Works in single pass.
  - Used in split operations.
  - Even-length returns later middle.

## Q36. Palindrome Linked List

- Concept: Find middle, reverse second half, compare halves, optional restore. No extra array for O(1) space.

```javascript
function isPalindrome(head) {
  if (!head || !head.next) return true;

  const reverse = (h) => {
    let prev = null;
    let cur = h;
    while (cur) { const next = cur.next; cur.next = prev; prev = cur; cur = next; }
    return prev;
  };

  let slow = head;
  let fast = head;
  while (fast && fast.next) { slow = slow.next; fast = fast.next.next; }

  let second = reverse(slow);
  let first = head;
  let ok = true;
  let cur = second;
  while (cur) {
    if (cur.val !== first.val) { ok = false; break; }
    cur = cur.next;
    first = first.next;
  }
  // optional restore: reverse(second)
  return ok;
}
```

- Deep Insights:
  - O(n) time, O(1) extra space.
  - Careful with odd length (middle skip ok).
  - Restoration is optional.
  - Avoid converting to array if memory constrained.

## Q37. Flatten Multilevel LL

- Concept: DFS through child pointers, splice child list between node and next. Use stack to remember next nodes.

```javascript
function flatten(head) {
  if (!head) return head;
  const stack = [];
  let cur = head;
  while (cur) {
    if (cur.child) {
      if (cur.next) stack.push(cur.next);
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
```

- Deep Insights:
  - Iterative DFS avoids recursion depth.
  - Maintain prev pointers if doubly-linked.
  - Clear child pointers to flatten.
  - Order is pre-order style.

## Q38. Intersection of Two LL

- Concept: Two pointers traverse both lists; meeting point is intersection. Switch heads when reaching end to equalize path lengths.

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
```

- Deep Insights:
  - O(m+n) time, O(1) space.
  - Works without length computation.
  - Requires exact node reference equality.
  - Ends at null when no intersection.

## Q39. Add Two Numbers (LL)

- Concept: Digit-wise sum with carry using two pointers; build result list. Handles uneven lengths and final carry.

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
```

- Deep Insights:
  - Forward order variant needs stacks.
  - No integer overflow risk.
  - Simple loop covers all cases.
  - Keep nodes immutable if required by spec.

## Q40. Sort LL

- Concept: Merge sort for linked lists: split at middle, recursively sort, merge. O(n log n) time, O(log n) stack space.

```javascript
function sortList(head) {
  if (!head || !head.next) return head;

  // split by mid
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
      if (a.val <= b.val) { t.next = a; a = a.next; }
      else { t.next = b; b = b.next; }
      t = t.next;
    }
    t.next = a || b;
    return dummy.next;
  }
}
```

- Deep Insights:
  - Arrays can use quicksort; LL favors mergesort.
  - Splitting via slow/fast then cut.
  - Stable due to merge order.
  - Extra stack but no extra array.

## Q41. Clone LL with Random Pointer

- Concept: Interleave cloned nodes, set randoms, then detach cloned list. Avoids extra hash map space.

```javascript
function copyRandomList(head) {
  if (!head) return null;

  // 1) interleave
  for (let cur = head; cur; cur = cur.next.next) {
    const node = { val: cur.val, next: cur.next };
    cur.next = node;
  }

  // 2) randoms
  for (let cur = head; cur; cur = cur.next.next) {
    if (cur.random) cur.next.random = cur.random.next;
  }

  // 3) detach
  const pseudo = { next: null };
  let copy = pseudo;
  let cur = head;
  while (cur) {
    const next = cur.next.next;
    const cloned = cur.next;
    copy.next = cloned;
    copy = cloned;
    cur.next = next;
    cur = next;
  }
  return pseudo.next;
}
```

- Deep Insights:
  - O(n) time, O(1) extra space.
  - Interleaving preserves mapping.
  - Careful pointer hops.
  - Map-based approach is simpler but O(n) space.

## Q42. Reverse Nodes in K-Group

- Concept: Reverse each k-length block in-place; leave last block if < k. Use helpers to check k nodes ahead and reverse.

```javascript
function reverseKGroup(head, k) {
  const dummy = { next: head };
  let groupPrev = dummy;

  while (true) {
    let kth = groupPrev;
    for (let i = 0; i < k && kth; i++) kth = kth.next;
    if (!kth) break;

    const groupNext = kth.next;
    // reverse group
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
```

- Deep Insights:
  - In-place O(1) extra space.
  - Requires careful boundary handling.
  - Common in list-block transforms.
  - Verify last partial group untouched.

## Q43. Rotate List

- Concept: Connect tail to head (circle), find new tail at (n - k%n - 1), break. Compute length with one pass.

```javascript
function rotateRight(head, k) {
  if (!head || !head.next || k === 0) return head;

  // get length and tail
  let len = 1;
  let tail = head;
  while (tail.next) { tail = tail.next; len++; }

  k %= len;
  if (k === 0) return head;

  tail.next = head; // circle
  let steps = len - k - 1;
  let newTail = head;
  while (steps--) newTail = newTail.next;

  const newHead = newTail.next;
  newTail.next = null;
  return newHead;
}
```

- Deep Insights:
  - O(n) time, O(1) space.
  - Circle trick simplifies pointer math.
  - k may exceed length; normalize.
  - Handles k==0 quickly.

## Q44. Delete Node w/o Head Pointer

- Concept: Copy next node’s value to current, bypass next. Not possible for tail node.

```javascript
function deleteNode(node) {
  node.val = node.next.val;
  node.next = node.next.next;
}
```

- Deep Insights:
  - Tail cannot be deleted with this method.
  - Mutates node content.
  - O(1) time.
  - Assumes node is valid and non-tail.

## Q45. Find Start Node of Cycle

- Concept: After Floyd meet, move one pointer to head; step both 1× to meet at cycle start. Distance head->start equals meet->start.

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
```

- Deep Insights:
  - O(n) time, O(1) space.
  - Requires first detecting cycle.
  - Works regardless of cycle length.
  - Returns null when no cycle.
