# Graphs

## Q96. DFS / BFS

- Concept: Explore graph via stack/recursion (DFS) or queue (BFS) from a start node.

```javascript
function bfs(g, s){ const q=[s], seen=new Set([s]); while(q.length){ const u=q.shift(); for(const v of g[u]||[]) if(!seen.has(v)){ seen.add(v); q.push(v); } } return seen; }
function dfs(g, s){ const seen=new Set(); (function go(u){ seen.add(u); for(const v of g[u]||[]) if(!seen.has(v)) go(v); })(s); return seen; }
```

- Deep Insights:
  - Use adjacency list for sparse graphs.
  - BFS finds shortest paths in unweighted graphs.
  - DFS useful for components, topological tasks.
  - Track visited to avoid cycles.

## Q97. Detect Cycle (Directed & Undirected)

- Concept: Directed: DFS colors (0,1,2) to catch back-edges. Undirected: DFS track parent.

```javascript
function hasCycleDirected(g){ const n=Object.keys(g).length, col={}; const dfs=u=>{ col[u]=1; for(const v of g[u]||[]){ if(col[v]===1) return true; if(!col[v]&&dfs(v)) return true; } col[u]=2; return false; }; for(const u in g) if(!col[u]&&dfs(u)) return true; return false; }
function hasCycleUndirected(g){ const seen=new Set(); function dfs(u,p){ seen.add(u); for(const v of g[u]||[]) if(v!==p){ if(seen.has(v) || dfs(v,u)) return true; } return false; } for(const u in g) if(!seen.has(u)&&dfs(u,-1)) return true; return false; }
```

- Deep Insights:
  - Colors: 0=unseen,1=visiting,2=done.
  - Parent check prevents trivial back-edge in undirected.
  - Works per component.
  - O(V+E).

## Q98. Topological Sort

- Concept: Kahn’s algorithm with indegrees; pop zeros and decrement neighbors.

```javascript
function topoSort(g){ const indeg={}, q=[]; for(const u in g){ if(!(u in indeg)) indeg[u]=0; for(const v of g[u]) indeg[v]=(indeg[v]||0)+1; } for(const u in indeg) if(indeg[u]===0) q.push(u); const order=[]; while(q.length){ const u=q.shift(); order.push(u); for(const v of g[u]||[]) if(--indeg[v]===0) q.push(v); } return order.length===Object.keys(indeg).length? order : []; }
```

- Deep Insights:
  - Empty result when cycle exists.
  - Multiple valid orders possible.
  - Queue seeds are indegree 0.
  - O(V+E).

## Q99. Number of Islands

- Concept: Count connected components of '1's using DFS/BFS; mark visited.

```javascript
function numIslands(grid){ const m=grid.length, n=grid[0]?.length||0; const seen=Array.from({length:m},()=>Array(n).fill(false)); const dirs=[[1,0],[-1,0],[0,1],[0,-1]]; let cnt=0; const dfs=(r,c)=>{ seen[r][c]=true; for(const [dr,dc] of dirs){ const nr=r+dr,nc=c+dc; if(nr>=0&&nr<m&&nc>=0&&nc<n&&grid[nr][nc]==='1'&&!seen[nr][nc]) dfs(nr,nc); } }; for(let i=0;i<m;i++) for(let j=0;j<n;j++) if(grid[i][j]==='1'&&!seen[i][j]){ cnt++; dfs(i,j); } return cnt; }
```

- Deep Insights:
  - Mutating grid to '0' can save space.
  - 8-direction variant adds diagonals.
  - BFS queue also fine.
  - O(mn).

## Q100. Clone Graph

- Concept: BFS/DFS copy nodes using a map old->new; wire edges as discovered.

```javascript
function cloneGraph(node){ if(!node) return null; const mp=new Map(); const q=[node]; mp.set(node,{val:node.val,neighbors:[]}); while(q.length){ const u=q.shift(); for(const v of u.neighbors){ if(!mp.has(v)){ mp.set(v,{val:v.val,neighbors:[]}); q.push(v); } mp.get(u).neighbors.push(mp.get(v)); } } return mp.get(node); }
```

- Deep Insights:
  - Works for cycles via map.
  - DFS identical with recursion.
  - Maintain neighbor arrays.
  - O(V+E) time/space.

## Q101. Rotten Oranges

- Concept: Multi-source BFS from all rotten; time is levels until no fresh left.

```javascript
function orangesRotting(grid){ const m=grid.length,n=grid[0]?.length||0, q=[]; let fresh=0, time=0; for(let i=0;i<m;i++) for(let j=0;j<n;j++){ if(grid[i][j]===2) q.push([i,j]); if(grid[i][j]===1) fresh++; }
  const dirs=[[1,0],[-1,0],[0,1],[0,-1]]; while(q.length&&fresh){ const sz=q.length; time++; for(let k=0;k<sz;k++){ const [r,c]=q.shift(); for(const [dr,dc] of dirs){ const nr=r+dr,nc=c+dc; if(nr>=0&&nr<m&&nc>=0&&nc<n&&grid[nr][nc]===1){ grid[nr][nc]=2; fresh--; q.push([nr,nc]); } } } }
  return fresh? -1 : time;
}
```

- Deep Insights:
  - Level count equals minutes.
  - Track fresh count to stop.
  - O(mn).
  - In-place updates.

## Q102. Course Schedule

- Concept: Detect cycle in directed graph (prereqs). Return true if acyclic.

```javascript
function canFinish(n, prereq){ const g=Array.from({length:n},()=>[]); for(const [a,b] of prereq) g[b].push(a); const indeg=new Array(n).fill(0); g.forEach(nei=>nei.forEach(v=>indeg[v]++)); const q=[]; for(let i=0;i<n;i++) if(indeg[i]===0) q.push(i); let seen=0; while(q.length){ const u=q.shift(); seen++; for(const v of g[u]) if(--indeg[v]===0) q.push(v); } return seen===n; }
```

- Deep Insights:
  - Kahn’s algorithm.
  - If all visited, schedule possible.
  - Return order if needed.
  - O(V+E).

## Q103. Bipartite Graph

- Concept: 2-color via BFS; conflict implies odd cycle -> not bipartite.

```javascript
function isBipartite(g){ const n=g.length, col=new Array(n).fill(0); for(let s=0;s<n;s++) if(!col[s]){ col[s]=1; const q=[s]; while(q.length){ const u=q.shift(); for(const v of g[u]){ if(!col[v]){ col[v]=-col[u]; q.push(v);} else if(col[v]===col[u]) return false; } } } return true; }
```

- Deep Insights:
  - Works per component.
  - DFS coloring also fine.
  - O(V+E).
  - 1/-1 color convention.

## Q104. Dijkstra’s Algorithm

- Concept: Shortest paths non-negative weights using min-heap of (dist,node).

```javascript
function dijkstra(n, edges, src){ const g=Array.from({length:n},()=>[]); for(const [u,v,w] of edges){ g[u].push([v,w]); g[v].push([u,w]); }
  const dist=new Array(n).fill(Infinity); dist[src]=0; const h=new (class{constructor(){this.a=[];} push(x){this.a.push(x); this.a.sort((p,q)=>p[0]-q[0]);} pop(){return this.a.shift();} size(){return this.a.length;}})(); h.push([0,src]);
  while(h.size()){ const [d,u]=h.pop(); if(d!==dist[u]) continue; for(const [v,w] of g[u]) if(d+w<dist[v]){ dist[v]=d+w; h.push([dist[v],v]); } }
  return dist;
}
```

- Deep Insights:
  - Use binary heap for O((V+E) log V); simple queue suffices for small inputs.
  - No negative edges.
  - Initialize dist[src]=0.
  - Stop early if target known.

## Q105. Bellman-Ford

- Concept: Relax all edges V-1 times; detect negative cycles on V-th pass.

```javascript
function bellmanFord(n, edges, src){ const dist=new Array(n).fill(Infinity); dist[src]=0; for(let i=0;i<n-1;i++) for(const [u,v,w] of edges) if(dist[u]+w<dist[v]) dist[v]=dist[u]+w; for(const [u,v,w] of edges) if(dist[u]+w<dist[v]) return null; return dist; }
```

- Deep Insights:
  - Works with negative edges.
  - Null indicates negative cycle reachable.
  - O(VE) time.
  - Simple to implement.

## Q106. Floyd-Warshall

- Concept: All-pairs shortest paths via DP over intermediate nodes.

```javascript
function floydWarshall(dist){ const n=dist.length; for(let k=0;k<n;k++) for(let i=0;i<n;i++) for(let j=0;j<n;j++) if(dist[i][k]+dist[k][j]<dist[i][j]) dist[i][j]=dist[i][k]+dist[k][j]; return dist; }
```

- Deep Insights:
  - O(n^3) time.
  - Detect negative cycles if dist[i][i]<0.
  - Works on dense graphs.
  - In-place updates.

## Q107. Minimum Spanning Tree (Kruskal/Prim)

- Concept: Kruskal: sort edges, union-find join safe edges. Prim: grow with PQ.

```javascript
function kruskal(n, edges){ edges.sort((a,b)=>a[2]-b[2]); const parent=Array.from({length:n},(_,i)=>i), rank=new Array(n).fill(0); const find=x=> parent[x]===x? x : (parent[x]=find(parent[x])); const union=(a,b)=>{ a=find(a); b=find(b); if(a===b) return false; if(rank[a]<rank[b]) [a,b]=[b,a]; parent[b]=a; if(rank[a]===rank[b]) rank[a]++; return true; }; let cost=0; const mst=[]; for(const [u,v,w] of edges) if(union(u,v)){ cost+=w; mst.push([u,v,w]); } return {cost, mst}; }
```

- Deep Insights:
  - DSU with path compression, union by rank.
  - O(E log E).
  - Prim’s better on dense with PQ.
  - MST unique if weights unique.

## Q108. Bridges in Graph

- Concept: Tarjan’s DFS with discovery time and low-link; edge (u,v) is bridge if low[v] > tin[u].

```javascript
function bridges(n, g){ const tin=new Array(n).fill(-1), low=new Array(n).fill(0); let t=0; const res=[]; function dfs(u,p){ tin[u]=low[u]=t++; for(const v of g[u]) if(v!==p){ if(tin[v]!==-1){ low[u]=Math.min(low[u], tin[v]); } else { dfs(v,u); low[u]=Math.min(low[u], low[v]); if(low[v]>tin[u]) res.push([u,v]); } } } for(let i=0;i<n;i++) if(tin[i]===-1) dfs(i,-1); return res; }
```

- Deep Insights:
  - O(V+E).
  - Undirected graphs.
  - Similar to articulation points.
  - tin/low arrays core idea.

## Q109. Articulation Points

- Concept: Node u is cut-vertex if root has >1 DFS children or exists v with low[v] >= tin[u].

```javascript
function articulationPoints(n,g){ const tin=new Array(n).fill(-1), low=new Array(n).fill(0), is=new Array(n).fill(false); let t=0; function dfs(u,p){ tin[u]=low[u]=t++; let ch=0; for(const v of g[u]) if(v!==p){ if(tin[v]!==-1){ low[u]=Math.min(low[u], tin[v]); } else { dfs(v,u); low[u]=Math.min(low[u], low[v]); if(p!==-1 && low[v]>=tin[u]) is[u]=true; ch++; } } if(p===-1 && ch>1) is[u]=true; } for(let i=0;i<n;i++) if(tin[i]===-1) dfs(i,-1); return is.map((v,i)=>v?i:null).filter(v=>v!==null); }
```

- Deep Insights:
  - O(V+E).
  - Only for undirected connected components.
  - Root special case.
  - Useful for network resilience.

## Q110. Shortest Path in DAG

- Concept: Topo order then relax edges once in order.

```javascript
function dagShortestPath(n, edges, src){ const g=Array.from({length:n},()=>[]), indeg=new Array(n).fill(0); for(const [u,v,w] of edges){ g[u].push([v,w]); indeg[v]++; }
  const q=[], order=[]; for(let i=0;i<n;i++) if(indeg[i]===0) q.push(i); while(q.length){ const u=q.shift(); order.push(u); for(const [v] of g[u]) if(--indeg[v]===0) q.push(v); }
  const dist=new Array(n).fill(Infinity); dist[src]=0; for(const u of order){ if(dist[u]===Infinity) continue; for(const [v,w] of g[u]) dist[v]=Math.min(dist[v], dist[u]+w); }
  return dist;
}
```

- Deep Insights:
  - Linear time O(V+E).
  - Requires DAG; cycles break topo.
  - Works with negative weights.
  - Topo by Kahn or DFS.

## Q111. Detect Cycle in DAG

- Concept: DAG by definition has no cycles; if topo fails (not all nodes output), cycle exists.

```javascript
function isDAG(g){ const indeg={}; const q=[]; for(const u in g){ if(!(u in indeg)) indeg[u]=0; for(const v of g[u]) indeg[v]=(indeg[v]||0)+1; } for(const u in indeg) if(indeg[u]===0) q.push(u); let seen=0; while(q.length){ const u=q.shift(); seen++; for(const v of g[u]||[]) if(--indeg[v]===0) q.push(v); } return seen===Object.keys(indeg).length; }
```

- Deep Insights:
  - Kahn’s is a cycle detector.
  - DFS color also applicable.
  - Return false => has cycle.
  - O(V+E).

## Q112. Word Ladder

- Concept: BFS over patterns (* wildcard) to neighbors; track steps until target.

```javascript
function ladderLength(beginWord, endWord, wordList){ const set=new Set(wordList); if(!set.has(endWord)) return 0; const pat=new Map(); const add=(w,i)=>{ const p=w.slice(0,i)+'*'+w.slice(i+1); if(!pat.has(p)) pat.set(p,[]); pat.get(p).push(w); };
  for(const w of set) for(let i=0;i<w.length;i++) add(w,i);
  const q=[[beginWord,1]], seen=new Set([beginWord]);
  while(q.length){ const [w,d]=q.shift(); if(w===endWord) return d; for(let i=0;i<w.length;i++){ const p=w.slice(0,i)+'*'+w.slice(i+1); for(const nb of pat.get(p)||[]) if(!seen.has(nb)){ seen.add(nb); q.push([nb,d+1]); } }
  }
  return 0;
}
```

- Deep Insights:
  - Pattern graph reduces edges.
  - Each word expands O(L) patterns.
  - Bidirectional BFS speeds up.
  - O(N·L^2) typical.

## Q113. Snake & Ladder Problem

- Concept: BFS on board indices; edges via dice to next square, apply snakes/ladders mapping.

```javascript
function snakesAndLadders(board){ const n=board.length; const id=i=>{ const r=Math.floor((i-1)/n), c=(i-1)%n; const rr=n-1-r, cc=r%2? n-1-c : c; return [rr,cc]; };
  const target=n*n; const q=[[1,0]], seen=new Set([1]);
  while(q.length){ const [u,d]=q.shift(); if(u===target) return d; for(let k=1;k<=6&&u+k<=target;k++){ let v=u+k; const [r,c]=id(v); if(board[r][c]!==-1) v=board[r][c]; if(!seen.has(v)){ seen.add(v); q.push([v,d+1]); } }
  }
  return -1;
}
```

- Deep Insights:
  - Zig-zag index mapping.
  - BFS gives min moves.
  - Snakes/ladders override position.
  - O(n^2).

## Q114. DSU (Union-Find)

- Concept: Disjoint Set Union supports union/find with path compression and union by rank.

```javascript
class DSU{ constructor(n){ this.p=Array.from({length:n},(_,i)=>i); this.r=new Array(n).fill(0); } find(x){ return this.p[x]===x? x : (this.p[x]=this.find(this.p[x])); } union(a,b){ a=this.find(a); b=this.find(b); if(a===b) return false; if(this.r[a]<this.r[b]) [a,b]=[b,a]; this.p[b]=a; if(this.r[a]===this.r[b]) this.r[a]++; return true; } }
```

- Deep Insights:
  - Near-constant amortized time.
  - Basis for Kruskal, connectivity.
  - Path compression critical.
  - Rank/size heuristic balances.

## Q115. Tarjan’s Algorithm for SCC

- Concept: DFS stack with ids/low-link; on root, pop stack to form SCC.

```javascript
function tarjansSCC(n, g){ const id=new Array(n).fill(-1), low=new Array(n).fill(0), on=new Array(n).fill(false), st=[]; let cur=0; const comp=[];
  function dfs(u){ id[u]=low[u]=cur++; st.push(u); on[u]=true; for(const v of g[u]||[]){ if(id[v]===-1){ dfs(v); low[u]=Math.min(low[u], low[v]); } else if(on[v]) low[u]=Math.min(low[u], id[v]); }
    if(low[u]===id[u]){ const s=[]; while(true){ const x=st.pop(); on[x]=false; s.push(x); if(x===u) break; } comp.push(s); }
  }
  for(let i=0;i<n;i++) if(id[i]===-1) dfs(i);
  return comp;
}
```

- Deep Insights:
  - O(V+E).
  - Works on directed graphs.
  - Strongly connected components partition nodes.
  - Stack tracks current DFS path.
