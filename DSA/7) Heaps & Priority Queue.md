# Heaps / Priority Queue

```javascript
// Minimal binary heap utility
class Heap {
  constructor(cmp){ this.a=[]; this.cmp=cmp; }
  size(){ return this.a.length; }
  peek(){ return this.a[0]; }
  push(v){ this.a.push(v); this._up(this.a.length-1); }
  pop(){ if(!this.a.length) return undefined; const top=this.a[0], last=this.a.pop(); if(this.a.length){ this.a[0]=last; this._down(0); } return top; }
  _up(i){ const a=this.a, cmp=this.cmp; while(i){ const p=(i-1>>1); if(cmp(a[i],a[p])){ [a[i],a[p]]=[a[p],a[i]]; i=p; } else break; }
  _down(i){ const a=this.a, cmp=this.cmp; for(;;){ let l=i*2+1, r=l+1, m=i; if(l<a.length && cmp(a[l],a[m])) m=l; if(r<a.length && cmp(a[r],a[m])) m=r; if(m===i) break; [a[i],a[m]]=[a[m],a[i]]; i=m; }
  }
}
```

## Q86. Kth Largest Element

- Concept: Maintain a min-heap of size k; pop when heap grows, top is kth largest.

```javascript
function findKthLargest(nums, k){ const h=new Heap((x,y)=>x<y); for(const x of nums){ h.push(x); if(h.size()>k) h.pop(); } return h.peek(); }
```

- Deep Insights:
  - O(n log k) time, O(k) space.
  - Quickselect gives average O(n), but heap is simpler and stable.
  - For kth smallest, invert comparator or values.
  - Stream-friendly: process on the fly.

## Q87. Top K Frequent Elements

- Concept: Count with Map, push [freq,val] into min-heap of size k.

```javascript
function topKFrequent(nums, k){ const cnt=new Map(); for(const x of nums) cnt.set(x,(cnt.get(x)||0)+1); const h=new Heap((a,b)=>a[0]<b[0]); for(const [v,f] of cnt){ h.push([f,v]); if(h.size()>k) h.pop(); } const res=[]; while(h.size()) res.push(h.pop()[1]); return res.reverse(); }
```

- Deep Insights:
  - O(n log k). Bucket sort alternative O(n).
  - Ties arbitrary unless specified.
  - Reverse to return highest first.
  - Memory bounded by unique values.

## Q88. Merge K Sorted Lists

- Concept: Push each list head into min-heap by value; pop smallest, push its next.

```javascript
function mergeKLists(lists){ const h=new Heap((a,b)=>a.val<b.val); for(const n of lists) if(n) h.push(n); const d={next:null}; let t=d; while(h.size()){ const n=h.pop(); t.next=n; t=t.next; if(n.next) h.push(n.next); } return d.next; }
```

- Deep Insights:
  - O(N log k), N total nodes.
  - In-place pointer wiring.
  - Works with duplicates naturally.
  - Avoids full array materialization.

## Q89. Find Median from Stream

- Concept: Two heaps: max-heap for lower half, min-heap for upper; balance sizes.

```javascript
class MedianFinder{
  constructor(){ this.lo=new Heap((a,b)=>a>b); this.hi=new Heap((a,b)=>a<b); }
  addNum(num){ if(!this.lo.size() || num<=this.lo.peek()) this.lo.push(num); else this.hi.push(num); if(this.lo.size()>this.hi.size()+1) this.hi.push(this.lo.pop()); if(this.hi.size()>this.lo.size()) this.lo.push(this.hi.pop()); }
  findMedian(){ if(this.lo.size()>this.hi.size()) return this.lo.peek(); return (this.lo.peek()+this.hi.peek())/2; }
}
```

- Deep Insights:
  - O(log n) per insert, O(1) median.
  - Keep lo.size >= hi.size.
  - All integers supported; median can be float.
  - Robust to duplicates.

## Q90. K Closest Points to Origin

- Concept: Max-heap of size k keyed by distance squared; eject farther points.

```javascript
function kClosest(points, k){ const h=new Heap((a,b)=>a[0]>b[0]); for(const [x,y] of points){ const d=x*x+y*y; h.push([d,[x,y]]); if(h.size()>k) h.pop(); } const res=[]; while(h.size()) res.push(h.pop()[1]); return res; }
```

- Deep Insights:
  - O(n log k).
  - Use d^2 to avoid sqrt.
  - For streaming points, same pattern.
  - If need sorted by distance, sort result.

## Q91. Connect Ropes to Min Cost

- Concept: Always join two shortest first (Huffman-like) using min-heap.

```javascript
function connectSticks(sticks){ const h=new Heap((a,b)=>a<b); for(const x of sticks) h.push(x); let cost=0; while(h.size()>1){ const a=h.pop(), b=h.pop(), c=a+b; cost+=c; h.push(c); } return cost; }
```

- Deep Insights:
  - Greedy optimality proof via exchange.
  - O(n log n) building and pops.
  - Identical to file merging problem.
  - Returns 0 for <=1 stick.

## Q92. Reorganize String

- Concept: Greedy pick two most frequent different chars from max-heap; push back with decremented counts.

```javascript
function reorganizeString(s){ const cnt=new Map(); for(const c of s) cnt.set(c,(cnt.get(c)||0)+1); const h=new Heap((a,b)=>a[0]>b[0]); for(const [c,f] of cnt) h.push([f,c]); let res=''; let prev=[0,''];
  while(h.size()){ let [f,c]=h.pop(); res+=c; f--; if(prev[0]>0) h.push(prev); prev=[f,c]; }
  return res.length===s.length? res : '';
}
```

- Deep Insights:
  - Fails if a char freq > (n+1)/2.
  - Keep previous char parked to avoid adjacency.
  - O(n log A) where A is alphabet size.
  - Returns empty if impossible.

## Q93. Maximum Sliding Window (Heap variant)

- Concept: Max-heap with lazy deletion using indices; pop until top inside window.

```javascript
function maxSlidingWindowHeap(nums,k){ const h=new Heap((a,b)=>a[0]>b[0]); let res=[]; for(let i=0;i<nums.length;i++){ h.push([nums[i], i]); while(h.peek() && h.peek()[1] <= i-k) h.pop(); if(i>=k-1) res.push(h.peek()[0]); } return res; }
```

- Deep Insights:
  - O(n log n) worst-case; deque O(n) preferred.
  - Keep indices to drop stale entries.
  - Handles duplicates.
  - Use deque version for optimal.

## Q94. Smallest Range Covering Elements (k lists)

- Concept: Min-heap on current heads; track current max; update best range and advance the list of the min.

```javascript
function smallestRange(nums){ const k=nums.length; const h=new Heap((a,b)=>a.val<b.val); let curMax=-Infinity; for(let i=0;i<k;i++){ h.push({val:nums[i][0], i, idx:0}); curMax=Math.max(curMax, nums[i][0]); }
  let best=[-Infinity, Infinity];
  while(h.size()){ const {val,i,idx}=h.pop(); if(curMax - val < best[1]-best[0]) best=[val, curMax]; if(idx+1===nums[i].length) break; const nv=nums[i][idx+1]; h.push({val:nv,i,idx:idx+1}); if(nv>curMax) curMax=nv; }
  return best;
}
```

- Deep Insights:
  - O(N log k), N total elements.
  - Requires each list sorted.
  - Track window [min, curMax].
  - Stop when any list exhausted.

## Q95. Heapsort

- Concept: Build max-heap, repeatedly extract max to the end; in-place O(n log n).

```javascript
function heapSort(arr){ const n=arr.length; const down=(i,sz)=>{ while(true){ let l=i*2+1,r=l+1,m=i; if(l<sz && arr[l]>arr[m]) m=l; if(r<sz && arr[r]>arr[m]) m=r; if(m===i) break; [arr[i],arr[m]]=[arr[m],arr[i]]; i=m; } };
  for(let i=n-1>>1;i>=0;i--) down(i,n);
  for(let end=n-1; end>0; end--){ [arr[0],arr[end]]=[arr[end],arr[0]]; down(0,end); }
  return arr;
}
```

- Deep Insights:
  - Not stable; in-place with O(1) extra.
  - Often slower than quicksort in practice.
  - Good worst-case guarantees.
  - Array-based binary heap.
