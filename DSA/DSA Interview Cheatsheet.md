# 🧠 DSA Interview Cheatsheet

## Arrays & Two Pointers
- Patterns: Two pointers, sliding window, prefix/suffix, partitioning, Kadane.
- Templates:
```javascript
// Two pointers
let l=0,r=arr.length-1; while(l<r){ /* move l/r based on condition */ }
// Sliding window (variable size)
let l=0; for(let r=0;r<s.length;r++){ /* expand */ while(/* invalid */){ l++; } }
```
- Tips: Normalize k, avoid O(n^2) scans, prefer O(n) with hash/sets.

## Hash Map / Set
- Use Map/Set for O(1) average lookup.
```javascript
const seen=new Map(); // freq or index
const set=new Set(arr);
```
- Tips: Pre-seed map (e.g., {0:1}) for prefix sums.

## Stack / Monotonic Stack
- Patterns: Valid parentheses, next greater, histogram, temperatures.
```javascript
const st=[]; for(let i=0;i<n;i++){ while(st.length && cond(i,st)) st.pop(); st.push(i); }
```
- Tips: Store indices, not values; consider sentinel.

## Queue / Deque
- Sliding window max via decreasing deque of indices.
```javascript
const dq=[]; // store indices, keep decreasing values
```

## Linked List
- Patterns: Fast/slow, reverse in-place, merge, split.
```javascript
// Reverse
let prev=null,cur=head; while(cur){ const nxt=cur.next; cur.next=prev; prev=cur; cur=nxt; }
```
- Tips: Use dummy nodes; careful pointer order.

## Trees (Binary Tree / BST)
- Traversals: DFS (pre/in/post), BFS (level-order).
```javascript
// DFS
function dfs(node){ if(!node) return; /* pre */ dfs(node.left); /* in */ dfs(node.right); /* post */ }
// BFS
const q=[root]; while(q.length){ const n=q.length; for(let i=0;i<n;i++){ const x=q.shift(); if(x.left) q.push(x.left); if(x.right) q.push(x.right); } }
```
- Tips: LCA, depth/diameter via post-order; BST uses sorted property.

## Heap / Priority Queue
- Use Min/Max Binary Heap (custom or library alternative).
```javascript
class MinHeap{ constructor(){this.h=[];} /* push/pop/peek */ }
```
- Tips: k-th, top-k, streaming median (two heaps).

## Graphs
- Representations: adjacency list `{u:[v...]}`.
```javascript
// BFS
const q=[src], seen=new Set([src]); while(q.length){ const u=q.shift(); for(const v of g[u]||[]){ if(!seen.has(v)){ seen.add(v); q.push(v);} } }
// DFS
function dfs(u){ seen.add(u); for(const v of g[u]||[]) if(!seen.has(v)) dfs(v); }
```
- Tips: Detect cycles (directed: colors/dfs; undirected: parent check), topo sort via indegree.

## Dynamic Programming
- Steps: Define state, recurrence, base cases, order, space-opt.
```javascript
// 1D DP
const dp=new Array(n+1).fill(0); dp[0]=...; for(let i=1;i<=n;i++){ dp[i]=/* rec */ }
// 2D DP
const dp=Array.from({length:m},()=>new Array(n).fill(0));
```
- Tips: Convert recursion to tabulation; optimize to O(1) or O(n) space when possible.

## Backtracking
- Explore, choose, un-choose; prune aggressively.
```javascript
const res=[]; function bt(i,cur){ if(goal) {res.push([...cur]); return;} for(const choice of choices){ cur.push(choice); bt(i+1,cur); cur.pop(); } } bt(0,[]);
```
- Tips: Sort for dedup; use sets for used choices.

## Complexity Reference
- Array scan: O(n)
- Sort: O(n log n)
- Binary search: O(log n)
- Hash ops: O(1) avg
- Heap ops: O(log n)
- DFS/BFS: O(V+E)

## Common Pitfalls
- Off-by-one in windows and indices
- Overflow/precision (use BigInt when needed)
- Mutating inputs unintentionally
- Missing base/null checks

Happy practicing! 🚀
