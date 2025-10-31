# Binary Search Tree

## Q76. Insert/Delete/Search in BST

- Concept: BST invariant: left < node < right. Search by comparing; insert by recursion; delete handles 0/1/2 children.

```javascript
function searchBST(root, val){ while(root){ if(val===root.val) return root; root = val<root.val? root.left : root.right; } return null; }
function insertIntoBST(root, val){ if(!root) return {val, left:null, right:null}; if(val<root.val) root.left=insertIntoBST(root.left,val); else root.right=insertIntoBST(root.right,val); return root; }
function deleteNode(root, key){ if(!root) return null; if(key<root.val) root.left=deleteNode(root.left,key); else if(key>root.val) root.right=deleteNode(root.right,key); else { if(!root.left) return root.right; if(!root.right) return root.left; let s=root.right; while(s.left) s=s.left; root.val=s.val; root.right=deleteNode(root.right,s.val);} return root; }
```

- Deep Insights:
  - Delete with two children: replace by inorder successor.
  - Iterative variants avoid recursion.
  - Maintain BST invariant after ops.
  - Duplicate policy must be defined.

## Q77. Validate BST

- Concept: Node values must lie within (min, max) bounds propagated downwards.

```javascript
function isValidBST(root){ function ok(n,lo,hi){ if(!n) return true; if(!(n.val>lo && n.val<hi)) return false; return ok(n.left,lo,n.val) && ok(n.right,n.val,hi); } return ok(root,-Infinity,Infinity); }
```

- Deep Insights:
  - Inorder should be strictly increasing.
  - Watch for integer limits; use Infinity.
  - Duplicates typically invalidate.
  - Subtree-level constraints matter.

## Q78. Lowest Common Ancestor in BST

- Concept: Use BST order: if both < node go left; if both > node go right; else node is LCA.

```javascript
function lowestCommonAncestor(root, p, q){ let a=p.val,b=q.val; while(root){ if(a<root.val && b<root.val) root=root.left; else if(a>root.val && b>root.val) root=root.right; else return root; } return null; }
```

- Deep Insights:
  - O(h) time.
  - No need to search all nodes.
  - Handles when one node is ancestor of the other.
  - Requires both nodes exist in tree.

## Q79. Kth Smallest in BST

- Concept: Inorder traversal yields sorted order; pick kth (1-indexed).

```javascript
function kthSmallest(root, k){ const st=[]; let cur=root; while(cur||st.length){ while(cur){ st.push(cur); cur=cur.left; } cur=st.pop(); if(--k===0) return cur.val; cur=cur.right; } }
```

- Deep Insights:
  - O(h+k) time.
  - Augment nodes with subtree sizes for faster queries.
  - Iterative avoids deep recursion.
  - Keep k decremented on visit.

## Q80. BST Iterator

- Concept: Controlled inorder traversal using a stack; next returns next smallest.

```javascript
class BSTIterator{ constructor(root){ this.st=[]; this.pushLeft(root); } pushLeft(n){ while(n){ this.st.push(n); n=n.left; } } next(){ const n=this.st.pop(); if(n.right) this.pushLeft(n.right); return n.val; } hasNext(){ return this.st.length>0; } }
```

- Deep Insights:
  - O(h) memory, O(1) amortized per op.
  - Left spine preload.
  - Works for dynamic traversal.
  - Values returned in ascending order.

## Q81. Recover BST

- Concept: Two nodes swapped; inorder should be sorted—find inversions and swap back.

```javascript
function recoverTree(root){ let prev=null, a=null, b=null; (function dfs(n){ if(!n) return; dfs(n.left); if(prev && prev.val>n.val){ if(!a) a=prev; b=n; } prev=n; dfs(n.right); })(root); const t=a.val; a.val=b.val; b.val=t; }
```

- Deep Insights:
  - Two inversions if non-adjacent; one if adjacent.
  - O(n) time, O(h) stack.
  - Morris inorder reduces space to O(1).
  - Do not change structure, only values.

## Q82. Floor and Ceil in BST

- Concept: Floor is greatest <= x; Ceil is smallest >= x. Walk BST updating candidate.

```javascript
function floorBST(root, x){ let ans=null; while(root){ if(root.val===x) return root.val; if(root.val<x){ ans=root.val; root=root.right; } else root=root.left; } return ans; }
function ceilBST(root, x){ let ans=null; while(root){ if(root.val===x) return root.val; if(root.val>x){ ans=root.val; root=root.left; } else root=root.right; } return ans; }
```

- Deep Insights:
  - O(h) time.
  - Return null if not found.
  - Candidates updated along the path.
  - Works with duplicates if policy defined.

## Q83. Range Sum in BST

- Concept: Prune branches using bounds [L,R]; sum only nodes within range.

```javascript
function rangeSumBST(root, L, R){ if(!root) return 0; let sum=0; if(root.val>L) sum+=rangeSumBST(root.left,L,R); if(root.val>=L && root.val<=R) sum+=root.val; if(root.val<R) sum+=rangeSumBST(root.right,L,R); return sum; }
```

- Deep Insights:
  - O(k + pruned) where k is nodes in range.
  - Pruning is key for performance.
  - Inclusive range.
  - Iterative stack works too.

## Q84. Predecessor & Successor

- Concept: In BST, predecessor is max in left subtree or last smaller ancestor; successor is min in right or last greater ancestor.

```javascript
function predecessor(root, key){ let ans=null; while(root){ if(key<=root.val) root=root.left; else { ans=root.val; root=root.right; } } return ans; }
function successor(root, key){ let ans=null; while(root){ if(key>=root.val) root=root.right; else { ans=root.val; root=root.left; } } return ans; }
```

- Deep Insights:
  - O(h) time each.
  - Useful for delete/find operations.
  - Requires handling when none exists.
  - Node reference variants exist.

## Q85. Convert Sorted Array to BST

- Concept: Build balanced BST by picking mid as root and recursing on halves.

```javascript
function sortedArrayToBST(nums){ function build(l,r){ if(l>r) return null; const m=(l+r>>1); const n={val:nums[m],left:null,right:null}; n.left=build(l,m-1); n.right=build(m+1,r); return n; } return build(0,nums.length-1); }
```

- Deep Insights:
  - Height-balanced O(log n) depth.
  - Inorder equals original array.
  - Use bit shift for floor mid.
  - Works with duplicates, but balance may vary.
