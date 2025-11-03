# Graphs

## Q96. DFS / BFS

Concept: Explore graph via stack/recursion (DFS) or queue (BFS) from a start node.

```javascript
function bfs(g, s) {
  const q = [s];
  const seen = new Set([s]);
  while (q.length) {
    const u = q.shift();
    for (const v of g[u] || []) {
      if (!seen.has(v)) {
        seen.add(v);
        q.push(v);
      }
    }
  }
  return seen;
}

function dfs(g, s) {
  const seen = new Set();
  function go(u) {
    seen.add(u);
    for (const v of g[u] || []) {
      if (!seen.has(v)) {
        go(v);
      }
    }
  }
  go(s);
  return seen;
}

// Test Cases:
//
// Example 1:
//   Input: g = {0: [1, 2], 1: [3], 2: [3], 3: []}, s = 0
//   BFS Output: Set {0, 1, 2, 3}
//   DFS Output: Set {0, 1, 3, 2}
//
// Example 2:
//   Input: g = {0: [1], 1: [0]}, s = 0
//   BFS Output: Set {0, 1}
//   DFS Output: Set {0, 1}
//
// Example 3:
//   Input: g = {0: []}, s = 0
//   BFS Output: Set {0}
//   DFS Output: Set {0}
```

Deep Insights:
  - Rule: Explore graph via stack/recursion (DFS) or queue (BFS) from start node; O(V+E) time, O(V) space.
  - Real-world: Graph traversal, path finding, component detection, connectivity analysis, tree/graph algorithms.
  - Common mistake: Track visited to avoid cycles; DFS useful for components and topological tasks; wrong traversal order.
  - Optimization: BFS finds shortest paths in unweighted graphs; DFS uses less space; choose based on problem needs.
  - Interview tip: Explain DFS vs BFS clearly; mention when to use each; ask about time/space complexity.
## Q97. Detect Cycle (Directed & Undirected)

Concept: Directed: DFS colors (0,1,2) to catch back edges. Undirected: DFS track parent.

```javascript
function hasCycleDirected(g) {
  const n = Object.keys(g).length;
  const col = {};

  const dfs = u => {
    col[u] = 1;
    for (const v of g[u] || []) {
      if (col[v] === 1) return true;
      if (!col[v] && dfs(v)) return true;
    }
    col[u] = 2;
    return false;
  };

  for (const u in g) {
    if (!col[u] && dfs(u)) return true;
  }
  return false;
}

function hasCycleUndirected(g) {
  const seen = new Set();

  function dfs(u, p) {
    seen.add(u);
    for (const v of g[u] || []) {
      if (v !== p) {
        if (seen.has(v) || dfs(v, u)) return true;
      }
    }
    return false;
  }

  for (const u in g) {
    if (!seen.has(u) && dfs(u, -1)) return true;
  }
  return false;
}

// Test Cases:
//
// hasCycleDirected:
// Example 1:
//   Input: g = {0: [1], 1: [2], 2: [0]} (directed cycle)
//   Output: true
//
// Example 2:
//   Input: g = {0: [1], 1: [2], 2: []} (no cycle)
//   Output: false
//
// hasCycleUndirected:
// Example 1:
//   Input: g = {0: [1], 1: [0]} (undirected cycle)
//   Output: true
//
// Example 2:
//   Input: g = {0: [1], 1: []} (no cycle)
//   Output: false
```

Deep Insights:
  - Rule: Directed: DFS colors (0,1,2) to catch back edges; Undirected: DFS track parent; O(V+E) time.
  - Real-world: Cycle detection in graphs, dependency validation, circular reference detection, graph validation.
  - Common mistake: Works per component; O(V+E) time; wrong color handling for directed; forgetting parent in undirected.
  - Optimization: Color tracking for directed; parent tracking for undirected; O(V+E) time optimal.
  - Interview tip: Explain color system clearly; mention parent tracking; ask about cycle type (directed vs undirected).
## Q98. Topological Sort

Concept: Kahn’s algorithm with indegrees; pop zeros and decrement neighbors.

```javascript
function topoSort(g) {
  const indeg = {};
  const q = [];

  for (const u in g) {
    if (!(u in indeg)) indeg[u] = 0;
    for (const v of g[u]) {
      indeg[v] = (indeg[v] || 0) + 1;
    }
  }

  for (const u in indeg) {
    if (indeg[u] === 0) {
      q.push(u);
    }
  }

  const order = [];
  while (q.length) {
    const u = q.shift();
    order.push(u);
    for (const v of g[u] || []) {
      if (--indeg[v] === 0) {
        q.push(v);
      }
    }
  }

  return order.length === Object.keys(indeg).length ? order : [];
}

// Test Cases:
//
// Example 1:
//   Input: g = {0: [1, 2], 1: [3], 2: [3], 3: []}
//   Output: [0, 1, 2, 3] or [0, 2, 1, 3] (valid topological order)
//
// Example 2:
//   Input: g = {0: [1], 1: [0]} (cycle exists)
//   Output: [] (empty, indicates cycle)
//
// Example 3:
//   Input: g = {0: [], 1: [], 2: []}
//   Output: [0, 1, 2] or any permutation
//
// Example 4:
//   Input: g = {0: [1, 2], 1: [3], 2: [3], 3: []}
//   Output: Valid topological order like [0, 1, 2, 3]
```

Deep Insights:
  - Rule: Kahn's algorithm with indegrees; pop zeros and decrement neighbors; O(V+E) time.
  - Real-world: Task scheduling, dependency resolution, build systems, course prerequisites.
  - Common mistake: O(V+E) time; not handling cycles correctly; wrong indegree calculation.
  - Optimization: O(V+E) time optimal; returns empty if cycle exists; efficient for DAGs.
  - Interview tip: Explain Kahn's algorithm clearly; mention cycle detection; ask about ordering variants.
## Q99. Number of Islands

Concept: Count connected components of '1's using DFS/BFS; mark visited.

```javascript
function numIslands(grid) {
  const m = grid.length;
  const n = grid[0]?.length || 0;
  const seen = Array.from({ length: m }, () => Array(n).fill(false));
  const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
  let cnt = 0;

  const dfs = (r, c) => {
    seen[r][c] = true;
    for (const [dr, dc] of dirs) {
      const nr = r + dr;
      const nc = c + dc;
      if (nr >= 0 && nr < m && nc >= 0 && nc < n &&
          grid[nr][nc] === '1' && !seen[nr][nc]) {
        dfs(nr, nc);
      }
    }
  };

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (grid[i][j] === '1' && !seen[i][j]) {
        cnt++;
        dfs(i, j);
      }
    }
  }
  return cnt;
}

// Test Cases:
//
// Example 1:
//   Input: grid = [
//     ["1","1","1","1","0"],
//     ["1","1","0","1","0"],
//     ["1","1","0","0","0"],
//     ["0","0","0","0","0"]
//   ]
//   Output: 1
//
// Example 2:
//   Input: grid = [
//     ["1","1","0","0","0"],
//     ["1","1","0","0","0"],
//     ["0","0","1","0","0"],
//     ["0","0","0","1","1"]
//   ]
//   Output: 3
//
// Example 3:
//   Input: grid = [["1","1","1"],["0","1","0"],["1","1","1"]]
//   Output: 1
```

Deep Insights:
  - Rule: Count connected components of '1's using DFS/BFS; mark visited; O(mn) time, O(mn) space.
  - Real-world: Island counting, connected component detection, grid analysis, matrix traversal.
  - Common mistake: O(mn) time/space; not marking visited correctly; wrong boundary checking.
  - Optimization: In-place marking reduces space; DFS uses less stack space; O(mn) time optimal.
  - Interview tip: Explain component counting clearly; mention DFS vs BFS; ask about in-place marking.
## Q100. Clone Graph

Concept: BFS/DFS copy nodes using a map old- >new; wire edges as discovered.

```javascript
function cloneGraph(node) {
  if (!node) return null;
  const mp = new Map();
  const q = [node];
  mp.set(node, { val: node.val, neighbors: [] });

  while (q.length) {
    const u = q.shift();
    for (const v of u.neighbors) {
      if (!mp.has(v)) {
        mp.set(v, { val: v.val, neighbors: [] });
        q.push(v);
      }
      mp.get(u).neighbors.push(mp.get(v));
    }
  }
  return mp.get(node);
}

// Test Cases:
//
// Example 1:
//   Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
//   (Node 1 connects to 2,4; Node 2 connects to 1,3; etc.)
//   Output: Deep copy with same structure
//
// Example 2:
//   Input: adjList = [[]]
//   Output: Deep copy of single node with no neighbors
//
// Example 3:
//   Input: adjList = []
//   Output: null
//
// Example 4:
//   Input: adjList = [[2],[1]]
//   Output: Deep copy of two connected nodes
```

Deep Insights:
  - Rule: BFS/DFS copy nodes using a map old->new; wire edges as discovered; O(V+E) time/space.
  - Real-world: Graph cloning, deep copying graphs, graph duplication, graph transformation.
  - Common mistake: O(V+E) time/space; not handling null nodes; wrong edge wiring.
  - Optimization: Map stores old->new mapping; wire edges during traversal; O(V+E) optimal.
  - Interview tip: Explain mapping clearly; mention BFS vs DFS; ask about handling cycles.
## Q101. Rotten Oranges

Concept: Multi- source BFS from all rotten; time is levels until no fresh left.

```javascript
function orangesRotting(grid) {
  const m = grid.length, n = grid[0]?.length || 0;
  const q = [];
  let fresh = 0, time = 0;
  
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (grid[i][j] === 2) q.push([i, j]);
      if (grid[i][j] === 1) fresh++;
    }
  }
  
  const dirs = [[1,0], [
  - 1,0], [0,1], [0,-1]];
  while (q.length && fresh) {
    const sz = q.length;
    time++;
    for (let k = 0; k < sz; k++) {
      const [r, c] = q.shift();
      for (const [dr, dc] of dirs) {
        const nr = r + dr, nc = c + dc;
        if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] === 1) {
          grid[nr][nc] = 2;
          fresh-- ;
          q.push([nr, nc]);
        }
      }
    }
  }
  return fresh ? - 1 : time;
}
```

Deep Insights:
  - Rule: Multi-source BFS from all rotten; time is levels until no fresh left; O(mn) time, O(mn) space.
  - Real-world: Propagation problems, multi-source BFS, grid spreading, contamination modeling.
  - Common mistake: O(mn) time/space; in-place updates; not tracking fresh count correctly; wrong level counting.
  - Optimization: Multi-source BFS; in-place updates reduce space; O(mn) time optimal.
  - Interview tip: Explain multi-source BFS clearly; mention level counting; ask about impossible cases.
## Q102. Course Schedule

Concept: Detect cycle in directed graph (prereqs). Return true if acyclic.

```javascript
function canFinish(n, prereq) {
  const g = Array.from({ length: n }, () => []);
  for (const [a, b] of prereq) {
    g[b].push(a);
  }

  const indeg = new Array(n).fill(0);
  g.forEach(nei => nei.forEach(v => indeg[v]++));

  const q = [];
  for (let i = 0; i < n; i++) {
    if (indeg[i] === 0) {
      q.push(i);
    }
  }

  let seen = 0;
  while (q.length) {
    const u = q.shift();
    seen++;
    for (const v of g[u]) {
      if (--indeg[v] === 0) {
        q.push(v);
      }
    }
  }
  return seen === n;
}

// Test Cases:
//
// Example 1:
//   Input: numCourses = 2, prerequisites = [[1,0]]
//   Output: true
//
// Example 2:
//   Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
//   Output: false
//
// Example 3:
//   Input: numCourses = 3, prerequisites = [[1,0],[2,1]]
//   Output: true
//
// Example 4:
//   Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
//   Output: true
```

Deep Insights:
  - Rule: Kahn's algorithm with indegrees; pop zeros and decrement neighbors; O(V+E) time.
  - Real-world: Task scheduling, dependency resolution, build systems, course prerequisites.
  - Common mistake: O(V+E) time; not handling cycles correctly; wrong indegree calculation.
  - Optimization: O(V+E) time optimal; returns empty if cycle exists; efficient for DAGs.
  - Interview tip: Explain Kahn's algorithm clearly; mention cycle detection; ask about ordering variants.
## Q103. Bipartite Graph

Concept: 2-color via BFS; conflict implies odd cycle → not bipartite.

```javascript
function isBipartite(g) {
  const n = g.length;
  const col = new Array(n).fill(0);

  for (let s = 0; s < n; s++) {
    if (!col[s]) {
      col[s] = 1;
      const q = [s];
      while (q.length) {
        const u = q.shift();
        for (const v of g[u]) {
          if (!col[v]) {
            col[v] = -col[u];
            q.push(v);
          } else if (col[v] === col[u]) {
            return false;
          }
        }
      }
    }
  }
  return true;
}

// Test Cases:
//
// Example 1:
//   Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
//   Output: false
//
// Example 2:
//   Input: graph = [[1,3],[0,2],[1,3],[0,2]]
//   Output: true
//
// Example 3:
//   Input: graph = [[1],[0]]
//   Output: true
//
// Example 4:
//   Input: graph = [[],[],[],[]]
//   Output: true
```

Deep Insights:
  - Rule: Color nodes with 1/-1 using BFS; return false if adjacent nodes have same color; O(V+E) time.
  - Real-world: Bipartite graph detection, graph coloring, assignment problems, conflict detection.
  - Common mistake: 1/-1 color convention; not handling disconnected components; wrong color checking.
  - Optimization: O(V+E) time optimal; BFS colors nodes; early return on conflict.
  - Interview tip: Explain coloring clearly; mention disconnected components; ask about odd cycle detection.
## Q104. Dijkstra’s Algorithm

Concept: Shortest paths non-negative weights using min-heap of (dist,node).

```javascript
function dijkstra(n, edges, src) {
  const g = Array.from({length: n}, () => []);
  for (const [u, v, w] of edges) {
    g[u].push([v, w]);
    g[v].push([u, w]);
  }
  
  const dist = new Array(n).fill(Infinity);
  dist[src] = 0;
  
  // Simple priority queue (min
  - heap alternative)
  const h = new (class {
    constructor() { this.a = []; }
    push(x) {
      this.a.push(x);
      this.a.sort((p, q) => p[0] - q[0]);
    }
    pop() { return this.a.shift(); }
    size() { return this.a.length; }
  })();
  
  h.push([0, src]);
  while (h.size()) {
    const [d, u] = h.pop();
    if (d !== dist[u]) continue;
    for (const [v, w] of g[u]) {
      if (d + w < dist[v]) {
        dist[v] = d + w;
        h.push([dist[v], v]);
      }
    }
  }
  return dist;
}
```

Deep Insights:
  - Rule: Shortest paths non-negative weights using min-heap of (dist,node); O((V+E) log V) time.
  - Real-world: Shortest path problems, routing algorithms, navigation systems, network optimization.
  - Common mistake: Stop early if target known; not handling non-negative weights; wrong heap comparator.
  - Optimization: Min-heap for priority; O((V+E) log V) time; stop early if target known.
  - Interview tip: Explain Dijkstra's clearly; mention non-negative requirement; ask about negative weights.
## Q105. Bellman- Ford

Concept: Relax all edges V-1 times; detect negative cycles on V-th pass.

```javascript
function bellmanFord(n, edges, src) {
  const dist = new Array(n).fill(Infinity);
  dist[src] = 0;
  
  // Relax edges V
  - 1 times
  for (let i = 0; i < n - 1; i++) {
    for (const [u, v, w] of edges) {
      if (dist[u] + w < dist[v]) {
        dist[v] = dist[u] + w;
      }
    }
  }
  
  // Check for negative cycles
  for (const [u, v, w] of edges) {
    if (dist[u] + w < dist[v]) {
      return null; // Negative cycle detected
    }
  }
  return dist;
}
```

Deep Insights:
  - Rule: Relax all edges V-1 times; detect negative cycles on V-th pass; O(VE) time.
  - Real-world: Shortest paths with negative weights, negative cycle detection, graph analysis.
  - Common mistake: Simple to implement; not handling negative cycles correctly; wrong relaxation order.
  - Optimization: O(VE) time; works with negative weights; detects negative cycles.
  - Interview tip: Explain relaxation clearly; mention negative cycle detection; ask about improvement tricks.
## Q106. Floyd- Warshall

Concept: All-pairs shortest paths via DP over intermediate nodes.

```javascript
function floydWarshall(dist) {
  const n = dist.length;
  for (let k = 0; k < n; k++) {
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        if (dist[i][k] + dist[k][j] < dist[i][j]) {
          dist[i][j] = dist[i][k] + dist[k][j];
        }
      }
    }
  }
  return dist;
}
```

Deep Insights:
  - Rule: All-pairs shortest paths via DP over intermediate nodes; O(V^3) time, O(V^2) space.
  - Real-world: All-pairs shortest paths, distance matrices, graph analysis, connectivity analysis.
  - Common mistake: Works on dense graphs; in-place updates; wrong intermediate node order; O(V^3) time.
  - Optimization: O(V^3) time optimal; in-place updates save space; works on dense graphs efficiently.
  - Interview tip: Explain DP approach clearly; mention intermediate nodes; ask about sparse graphs.
## Q107. Minimum Spanning Tree (Kruskal/Prim)

Concept: Kruskal: sort edges, union- find join safe edges. Prim: grow with PQ.

```javascript
function kruskal(n, edges){ edges.sort((a,b)=>a[2]
  - b[2]); const parent=Array.from({length:n},(_,i)=>i), rank=new Array(n).fill(0); const find=x=> parent[x]===x? x : (parent[x]=find(parent[x])); const union=(a,b)=>{ a=find(a); b=find(b); if(a===b) return false; if(rank[a]<rank[b]) [a,b]=[b,a]; parent[b]=a; if(rank[a]===rank[b]) rank[a]++; return true; }; let cost=0; const mst=[]; for(const [u,v,w] of edges) if(union(u,v)){ cost+=w; mst.push([u,v,w]); } return {cost, mst}; }
```

Deep Insights:
  - Rule: Kruskal: sort edges, union-find join safe edges; Prim: grow with PQ; O(E log E) time.
  - Real-world: Minimum spanning trees, network design, clustering, graph connectivity.
  - Common mistake: Prim's better on dense with PQ; MST unique if weights unique; wrong edge selection.
  - Optimization: Kruskal O(E log E); Prim O(E log V) with PQ; MST unique if weights unique.
  - Interview tip: Explain Kruskal vs Prim clearly; mention union-find; ask about dense vs sparse graphs.
## Q108. Bridges in Graph

Concept: Tarjan's DFS with discovery time and low-link; edge (u,v) is bridge if low[v] > tin[u].

```javascript
function bridges(n, g){ const tin=new Array(n).fill(- 1), low=new Array(n).fill(0); let t=0; const res=[]; function dfs(u,p){ tin[u]=low[u]=t++; for(const v of g[u]) if(v!==p){ if(tin[v]!==
  - 1){ low[u]=Math.min(low[u], tin[v]); } else { dfs(v,u); low[u]=Math.min(low[u], low[v]); if(low[v]>tin[u]) res.push([u,v]); } } } for(let i=0;i<n;i++) if(tin[i]===- 1) dfs(i,
  - 1); return res; }
```

Deep Insights:
  - Rule: Tarjan's DFS with discovery time and low-link; edge (u,v) is bridge if low[v] > tin[u]; O(V+E) time.
  - Real-world: Bridge detection, network resilience, critical edge identification, graph analysis.
  - Common mistake: Similar to articulation points; tin/low arrays core idea; wrong low-link calculation.
  - Optimization: O(V+E) time optimal; DFS tracks discovery and low-link; similar to articulation points.
  - Interview tip: Explain Tarjan's clearly; mention tin/low arrays; ask about articulation points variant.
## Q109. Articulation Points

Concept: Node u is cut-vertex if root has >1 DFS children or exists v with low[v] >= tin[u].

```javascript
function articulationPoints(n,g){ const tin=new Array(n).fill(- 1), low=new Array(n).fill(0), is=new Array(n).fill(false); let t=0; function dfs(u,p){ tin[u]=low[u]=t++; let ch=0; for(const v of g[u]) if(v!==p){ if(tin[v]!==
  - 1){ low[u]=Math.min(low[u], tin[v]); } else { dfs(v,u); low[u]=Math.min(low[u], low[v]); if(p!==- 1 && low[v]>=tin[u]) is[u]=true; ch++; } } if(p===
  - 1 && ch>1) is[u]=true; } for(let i=0;i<n;i++) if(tin[i]===- 1) dfs(i,
  - 1); return is.map((v,i)=>v?i:null).filter(v=>v!==null); }
```

Deep Insights:
  - Rule: Node u is cut-vertex if root has >1 DFS children or exists v with low[v] >= tin[u]; O(V+E) time.
  - Real-world: Articulation point detection, network resilience, critical node identification, graph analysis.
  - Common mistake: Root special case; useful for network resilience; wrong low-link comparison; forgetting root case.
  - Optimization: O(V+E) time optimal; DFS tracks discovery and low-link; root special case handled separately.
  - Interview tip: Explain cut-vertex clearly; mention root special case; ask about network resilience applications.
## Q110. Shortest Path in DAG

Concept: Topo order then relax edges once in order.

```javascript
function dagShortestPath(n, edges, src){ const g=Array.from({length:n},()=>[]), indeg=new Array(n).fill(0); for(const [u,v,w] of edges){ g[u].push([v,w]); indeg[v]++; }
  const q=[], order=[]; for(let i=0;i<n;i++) if(indeg[i]===0) q.push(i); while(q.length){ const u=q.shift(); order.push(u); for(const [v] of g[u]) if(-- indeg[v]===0) q.push(v); }
  const dist=new Array(n).fill(Infinity); dist[src]=0; for(const u of order){ if(dist[u]===Infinity) continue; for(const [v,w] of g[u]) dist[v]=Math.min(dist[v], dist[u]+w); }
  return dist;
}
```

Deep Insights:
  - Rule: Topo order then relax edges once in order; O(V+E) time for topo + edge relaxation.
  - Real-world: Shortest paths in DAGs, task scheduling, dependency resolution, topological algorithms.
  - Common mistake: Topo by Kahn or DFS; wrong topo ordering; not relaxing edges correctly.
  - Optimization: O(V+E) time optimal; topo ensures correct order; single pass relaxation sufficient.
  - Interview tip: Explain topo ordering clearly; mention Kahn vs DFS; ask about negative weights.
## Q111. Detect Cycle in DAG

Concept: DAG by definition has no cycles; if topo fails (not all nodes output), cycle exists.

```javascript
function isDAG(g){ const indeg={}; const q=[]; for(const u in g){ if(!(u in indeg)) indeg[u]=0; for(const v of g[u]) indeg[v]=(indeg[v]||0)+1; } for(const u in indeg) if(indeg[u]===0) q.push(u); let seen=0; while(q.length){ const u=q.shift(); seen++; for(const v of g[u]||[]) if(-- indeg[v]===0) q.push(v); } return seen===Object.keys(indeg).length; }
```

Deep Insights:
  - Rule: Kahn's algorithm with indegrees; pop zeros and decrement neighbors; O(V+E) time.
  - Real-world: Task scheduling, dependency resolution, build systems, course prerequisites.
  - Common mistake: O(V+E) time; not handling cycles correctly; wrong indegree calculation.
  - Optimization: O(V+E) time optimal; returns empty if cycle exists; efficient for DAGs.
  - Interview tip: Explain Kahn's algorithm clearly; mention cycle detection; ask about ordering variants.
## Q112. Word Ladder

Concept: BFS over patterns (* wildcard) to neighbors; track steps until target.

```javascript
function ladderLength(beginWord, endWord, wordList){ const set=new Set(wordList); if(!set.has(endWord)) return 0; const pat=new Map(); const add=(w,i)=>{ const p=w.slice(0,i)+'*'+w.slice(i+1); if(!pat.has(p)) pat.set(p,[]); pat.get(p).push(w); };
  for(const w of set) for(let i=0;i<w.length;i++) add(w,i);
  const q=[[beginWord,1]], seen=new Set([beginWord]);
  while(q.length){ const [w,d]=q.shift(); if(w===endWord) return d; for(let i=0;i<w.length;i++){ const p=w.slice(0,i)+'*'+w.slice(i+1); for(const nb of pat.get(p)||[]) if(!seen.has(nb)){ seen.add(nb); q.push([nb,d+1]); } }
  }
  return 0;
}
```

Deep Insights:
  - Rule: BFS over patterns (* wildcard) to neighbors; track steps until target; O(N·L^2) time where L is word length.
  - Real-world: Word ladder problems, string transformation, path finding in word graphs, transformation algorithms.
  - Common mistake: Bidirectional BFS speeds up; O(N·L^2) typical; wrong pattern generation; not tracking steps.
  - Optimization: Pattern-based neighbors efficient; bidirectional BFS speeds up; O(N·L^2) time typical.
  - Interview tip: Explain pattern approach clearly; mention bidirectional BFS; ask about optimization techniques.
## Q113. Snake & Ladder Problem

Concept: BFS on board indices; edges via dice to next square, apply snakes/ladders mapping.

```javascript
function snakesAndLadders(board){ const n=board.length; const id=i=>{ const r=Math.floor((i
  - 1)/n), c=(i- 1)%n; const rr=n
  - 1- r, cc=r%2? n
  - 1- c : c; return [rr,cc]; };
  const target=n*n; const q=[[1,0]], seen=new Set([1]);
  while(q.length){ const [u,d]=q.shift(); if(u===target) return d; for(let k=1;k<=6&&u+k<=target;k++){ let v=u+k; const [r,c]=id(v); if(board[r][c]!==
  - 1) v=board[r][c]; if(!seen.has(v)){ seen.add(v); q.push([v,d+1]); } }
  }
  return - 1;
}
```

Deep Insights:
  - Rule: BFS on board indices; edges via dice to next square, apply snakes/ladders mapping; O(n^2) time.
  - Real-world: Board games, shortest path in grid, game solving, graph-based puzzles.
  - Common mistake: O(n^2) time; not handling board indexing correctly; wrong snakes/ladders application.
  - Optimization: BFS finds shortest path; O(n^2) time for n×n board; handles snakes/ladders correctly.
  - Interview tip: Explain board indexing clearly; mention BFS approach; ask about board size limits.
## Q114. DSU (Union- Find)

Concept: Disjoint Set Union supports union/find with path compression and union by rank.

```javascript
class DSU{ constructor(n){ this.p=Array.from({length:n},(_,i)=>i); this.r=new Array(n).fill(0); } find(x){ return this.p[x]===x? x : (this.p[x]=this.find(this.p[x])); } union(a,b){ a=this.find(a); b=this.find(b); if(a===b) return false; if(this.r[a]<this.r[b]) [a,b]=[b,a]; this.p[b]=a; if(this.r[a]===this.r[b]) this.r[a]++; return true; } }
```

Deep Insights:
  - Rule: Disjoint Set Union supports union/find with path compression and union by rank; O(α(n)) amortized.
  - Real-world: Union-find problems, connectivity queries, dynamic connectivity, graph components.
  - Common mistake: Rank/size heuristic balances; wrong union logic; forgetting path compression.
  - Optimization: Path compression and union by rank; O(α(n)) amortized time; rank/size heuristic balances.
  - Interview tip: Explain union-find clearly; mention path compression; ask about amortized complexity.
## Q115. Tarjan’s Algorithm for SCC

Concept: DFS stack with ids/low- link; on root, pop stack to form SCC.

```javascript
function tarjansSCC(n, g){ const id=new Array(n).fill(
  - 1), low=new Array(n).fill(0), on=new Array(n).fill(false), st=[]; let cur=0; const comp=[];
  function dfs(u){ id[u]=low[u]=cur++; st.push(u); on[u]=true; for(const v of g[u]||[]){ if(id[v]===- 1){ dfs(v); low[u]=Math.min(low[u], low[v]); } else if(on[v]) low[u]=Math.min(low[u], id[v]); }
    if(low[u]===id[u]){ const s=[]; while(true){ const x=st.pop(); on[x]=false; s.push(x); if(x===u) break; } comp.push(s); }
  }
  for(let i=0;i<n;i++) if(id[i]===
  - 1) dfs(i);
  return comp;
}
```

Deep Insights:
  - Rule: DFS stack with ids/low-link; on root, pop stack to form SCC; O(V+E) time.
  - Real-world: Strongly connected components, graph analysis, component detection, graph partitioning.
  - Common mistake: Strongly connected components partition nodes; stack tracks current DFS path; wrong id/low-link.
  - Optimization: O(V+E) time optimal; DFS with stack tracks SCC; low-link identifies roots.
  - Interview tip: Explain Tarjan's clearly; mention stack usage; ask about SCC applications.

## Q116. Surrounded Regions

Concept:
Mark 'O' cells connected to border; flip remaining 'O' to 'X'; use DFS/BFS from border.

Example:
```javascript
function solve(board) {
  if (!board.length || !board[0].length) return;
  
  const m = board.length;
  const n = board[0].length;
  
  // Mark border-connected 'O' with DFS
  function dfs(i, j) {
    if (i < 0 || i >= m || j < 0 || j >= n || board[i][j] !== 'O') return;
    board[i][j] = '#';
    dfs(i + 1, j);
    dfs(i - 1, j);
    dfs(i, j + 1);
    dfs(i, j - 1);
  }
  
  // Mark from borders
  for (let i = 0; i < m; i++) {
    if (board[i][0] === 'O') dfs(i, 0);
    if (board[i][n - 1] === 'O') dfs(i, n - 1);
  }
  for (let j = 0; j < n; j++) {
    if (board[0][j] === 'O') dfs(0, j);
    if (board[m - 1][j] === 'O') dfs(m - 1, j);
  }
  
  // Flip remaining 'O' to 'X', restore '#' to 'O'
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (board[i][j] === 'O') board[i][j] = 'X';
      if (board[i][j] === '#') board[i][j] = 'O';
    }
  }
}

// Test Cases:
//
// Example 1:
//   Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
//   Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
//   Explanation: Border-connected 'O' at (3,1) remains; others flipped
//
// Example 2:
//   Input: board = [["X"]]
//   Output: [["X"]]
```

Deep Insights:
  - Rule: Mark border-connected 'O' with DFS; flip remaining 'O' to 'X'; O(mn) time.
  - Real-world: Flood fill, region marking, image processing, boundary detection.
  - Common mistake: Not marking border-connected; wrong DFS logic; not restoring marked cells.
  - Optimization: O(mn) time optimal; mark border-connected first; restore marked cells.
  - Interview tip: Explain border DFS strategy; mention region marking; ask about space optimization.

Time Complexity: O(mn) - Visit each cell once
Space Complexity: O(mn) - DFS recursion depth

## Q117. Evaluate Division

Concept:
Build graph from equations/values; use DFS/BFS to find path and multiply values.

Example:
```javascript
function calcEquation(equations, values, queries) {
  const graph = new Map();
  
  // Build graph
  for (let i = 0; i < equations.length; i++) {
    const [a, b] = equations[i];
    const val = values[i];
    
    if (!graph.has(a)) graph.set(a, new Map());
    if (!graph.has(b)) graph.set(b, new Map());
    
    graph.get(a).set(b, val);
    graph.get(b).set(a, 1 / val);
  }
  
  // DFS to find path
  function dfs(start, end, visited) {
    if (!graph.has(start) || !graph.has(end)) return -1.0;
    if (start === end) return 1.0;
    
    visited.add(start);
    
    for (const [neighbor, value] of graph.get(start)) {
      if (!visited.has(neighbor)) {
        const result = dfs(neighbor, end, visited);
        if (result !== -1.0) {
          return value * result;
        }
      }
    }
    
    visited.delete(start);
    return -1.0;
  }
  
  // Process queries
  const results = [];
  for (const [start, end] of queries) {
    results.push(dfs(start, end, new Set()));
  }
  
  return results;
}

// Test Cases:
//
// Example 1:
//   Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], 
//          queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
//   Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
//   Explanation: 
//     a / b = 2.0, b / c = 3.0
//     a / c = 6.0, b / a = 0.5
//     a / e = -1.0 (not found), a / a = 1.0, x / x = -1.0 (not found)
```

Deep Insights:
  - Rule: Build directed graph with values; DFS to find path; multiply values along path; O(n×q) time.
  - Real-world: Unit conversion, equation solving, ratio calculations, weighted graphs.
  - Common mistake: Not building bidirectional graph; wrong path multiplication; not handling disconnected nodes.
  - Optimization: O(n×q) time where q is queries; DFS finds path; cache results for optimization.
  - Interview tip: Explain graph building; mention bidirectional edges; ask about caching.

Time Complexity: O(n×q) - n equations, q queries
Space Complexity: O(n) - Graph storage

## Q118. Course Schedule II

Concept:
Find valid course order (topological sort); return course order or empty array if cycle exists.

Example:
```javascript
function findOrder(numCourses, prerequisites) {
  const graph = Array.from({length: numCourses}, () => []);
  const indegree = new Array(numCourses).fill(0);
  
  // Build graph and calculate indegree
  for (const [course, prereq] of prerequisites) {
    graph[prereq].push(course);
    indegree[course]++;
  }
  
  // Kahn's algorithm
  const queue = [];
  for (let i = 0; i < numCourses; i++) {
    if (indegree[i] === 0) {
      queue.push(i);
    }
  }
  
  const result = [];
  while (queue.length) {
    const course = queue.shift();
    result.push(course);
    
    for (const next of graph[course]) {
      indegree[next]--;
      if (indegree[next] === 0) {
        queue.push(next);
      }
    }
  }
  
  return result.length === numCourses ? result : [];
}

// Test Cases:
//
// Example 1:
//   Input: numCourses = 2, prerequisites = [[1,0]]
//   Output: [0,1]
//   Explanation: Take course 0 then course 1
//
// Example 2:
//   Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
//   Output: [0,2,1,3]
//   Explanation: Valid order: 0, then 1 or 2, then 3
//
// Example 3:
//   Input: numCourses = 1, prerequisites = []
//   Output: [0]
```

Deep Insights:
  - Rule: Topological sort with Kahn's algorithm; return order or empty if cycle; O(V+E) time.
  - Real-world: Course scheduling, task scheduling, dependency resolution, build systems.
  - Common mistake: Not detecting cycles; wrong topological sort; not handling all nodes.
  - Optimization: O(V+E) time optimal; Kahn's algorithm; return empty if result length != numCourses.
  - Interview tip: Explain topological sort clearly; mention cycle detection; compare with DFS approach.

Time Complexity: O(V+E) - Build graph + Kahn's algorithm
Space Complexity: O(V+E) - Graph and indegree arrays

## Q119. Minimum Genetic Mutation

Concept:
Find minimum mutations to transform start gene into end gene; use BFS to find shortest path.

Example:
```javascript
function minMutation(start, end, bank) {
  const bankSet = new Set(bank);
  if (!bankSet.has(end)) return -1;
  
  const choices = ['A', 'C', 'G', 'T'];
  const queue = [[start, 0]];
  const visited = new Set([start]);
  
  while (queue.length) {
    const [current, mutations] = queue.shift();
    
    if (current === end) return mutations;
    
    for (let i = 0; i < current.length; i++) {
      for (const choice of choices) {
        if (choice === current[i]) continue;
        
        const next = current.substring(0, i) + choice + current.substring(i + 1);
        
        if (bankSet.has(next) && !visited.has(next)) {
          visited.add(next);
          queue.push([next, mutations + 1]);
        }
      }
    }
  }
  
  return -1;
}

// Input: start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
// Output: 1
// Explanation: Change T to A at position 7

// Input: start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
// Output: 2
// Explanation: AACCGGTT -> AACCGGTA -> AAACGGTA

// Input: start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
// Output: 3
```

**Time Complexity:** O(bank.length × gene_length × 4) - BFS through valid mutations  
**Space Complexity:** O(bank.length) - Queue and visited set

Deep Insights:
- BFS shortest path: generate all valid mutations; use bank as graph; O(bank.length × gene_length × 4) time.
- Generate mutations by changing one character at a time; check if in bank.
- Use BFS to find minimum mutations (shortest path).
- Edge case: End not in bank returns -1; start equals end returns 0.
- Interview tip: Explain BFS approach; mention graph construction; ask about optimization.