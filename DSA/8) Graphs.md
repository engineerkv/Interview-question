# Graphs

---

## 📍 Navigation

<div align="center">

[Heaps & Priority Queue](7%20Heaps%20&%20Priority%20Queue.md) • [Home: README](README.md) • [Dynamic Programming →](9%20Dynamic%20Programming.md)

[📋 Cheatsheet](DSA%20Interview%20Cheatsheet.md]

</div>

---

## Q136. DFS and BFS Traversal

**Problem:** Implement Depth-First Search (DFS) and Breadth-First Search (BFS) algorithms to traverse a graph starting from a given node.

**Approach:**

- **DFS:** Use stack (recursion) to explore deeply before backtracking

- **BFS:** Use queue to explore level by level

### Solution 1: BFS (Breadth-First Search)

```javascript
function bfs(graph, start) {
  const queue = [start];
  const visited = new Set([start]);

  while (queue.length) {
    const node = queue.shift();

    // Process neighbors
    for (const neighbor of graph[node] || []) {
      if (!visited.has(neighbor)) {
        visited.add(neighbor);
        queue.push(neighbor);
      }
    }
  }

  return visited;
}

```

### Solution 2: DFS (Depth-First Search) - Recursive

```javascript
function dfs(graph, start) {
  const visited = new Set();

  function traverse(node) {
    visited.add(node);

    // Process neighbors
    for (const neighbor of graph[node] || []) {
      if (!visited.has(neighbor)) {
        traverse(neighbor);
      }
    }
  }

  traverse(start);
  return visited;
}

```

### Solution 3: DFS (Depth-First Search) - Iterative

```javascript
function dfsIterative(graph, start) {
  const stack = [start];
  const visited = new Set([start]);

  while (stack.length) {
    const node = stack.pop();

    // Process neighbors
    for (const neighbor of graph[node] || []) {
      if (!visited.has(neighbor)) {
        visited.add(neighbor);
        stack.push(neighbor);
      }
    }
  }

  return visited;
}

// Test Cases:
// Input: g = {0: [1, 2], 1: [3], 2: [3], 3: []}, s = 0
// BFS Output: Set {0, 1, 2, 3}
//   DFS Output: Set {0, 1, 3, 2}

// Input: g = {0: [1], 1: [0]}, s = 0
// BFS Output: Set {0, 1}
//   DFS Output: Set {0, 1}

// Input: g = {0: []}, s = 0
// BFS Output: Set {0}
//   DFS Output: Set {0}

```

**Time Complexity:** O(V + E) - Visit each vertex and edge once
**Space Complexity:** O(V) - Store visited set and queue/stack

## Q137. Detect Cycle in Directed and Undirected Graph

**Problem:** Detect if a cycle exists in a directed graph and an undirected graph.

**Approach:**

- **Directed:** Use DFS with color tracking (0=unvisited, 1=visiting, 2=visited). Back edge (gray to gray) indicates cycle.

- **Undirected:** Use DFS tracking parent. If visited neighbor is not parent, cycle exists.

### Solution 1: Detect Cycle in Directed Graph

```javascript
function hasCycleDirected(graph) {
  const color = {};  // 0: unvisited, 1: visiting, 2: visited

  function dfs(node) {
    color[node] = 1;  // Mark as visiting

    for (const neighbor of graph[node] || []) {
      if (color[neighbor] === 1) {
        // Back edge found (gray to gray)
        return true;
      }
      if (!color[neighbor] && dfs(neighbor)) {
        return true;
      }
    }

    color[node] = 2;  // Mark as visited
    return false;
  }

  for (const node in graph) {
    if (!color[node] && dfs(node)) {
      return true;
    }
  }

  return false;
}

```

### Solution 2: Detect Cycle in Undirected Graph

```javascript
function hasCycleUndirected(graph) {
  const visited = new Set();

  function dfs(node, parent) {
    visited.add(node);

    for (const neighbor of graph[node] || []) {
      if (neighbor !== parent) {
        if (visited.has(neighbor) || dfs(neighbor, node)) {
          return true;
        }
      }
    }

    return false;
  }

  for (const node in graph) {
    if (!visited.has(node) && dfs(node, -1)) {
      return true;
    }
  }

  return false;
}

// Test Cases:
//
// hasCycleDirected:
// Input: g = {0: [1], 1: [2], 2: [0]} (directed cycle)
// Output: true

// Input: g = {0: [1], 1: [2], 2: []} (no cycle)
// Output: false
//
// hasCycleUndirected:
// Input: g = {0: [1], 1: [0]} (undirected cycle)
// Output: true

// Input: g = {0: [1], 1: []} (no cycle)
// Output: false

```

**Time Complexity:** O(V + E) - Visit each vertex and edge once
**Space Complexity:** O(V) - Store color/visited information

## Q138. Topological Sort

**Problem:** Given a directed acyclic graph (DAG), return a topological ordering of its vertices. If the graph contains a cycle, return an empty array.

**Approach:** Use Kahn's algorithm: compute indegrees, start with nodes having indegree 0, process them and decrement neighbors' indegrees.

### Solution 1: Kahn's Algorithm (Optimal)

```javascript
function topologicalSort(graph) {
  const indegree = {};
  const queue = [];

  // Initialize indegree for all nodes
  for (const node in graph) {
    if (!(node in indegree)) {
      indegree[node] = 0;
    }
    // Count incoming edges
    for (const neighbor of graph[node] || []) {
      indegree[neighbor] = (indegree[neighbor] || 0) + 1;
    }
  }

  // Add nodes with indegree 0 to queue
  for (const node in indegree) {
    if (indegree[node] === 0) {
      queue.push(node);
    }
  }

  const order = [];

  while (queue.length) {
    const node = queue.shift();
    order.push(node);

    // Decrement indegree of neighbors
    for (const neighbor of graph[node] || []) {
      indegree[neighbor]--;
      if (indegree[neighbor] === 0) {
        queue.push(neighbor);
      }
    }
  }

  // If all nodes processed, return order; else cycle exists
  return order.length === Object.keys(indegree).length ? order : [];
}

// Test Cases:
// Input: g = {0: [1, 2], 1: [3], 2: [3], 3: []}
// Output: [0, 1, 2, 3] or [0, 2, 1, 3] (valid topological order)

// Input: g = {0: [1], 1: [0]} (cycle exists)
// Output: [] (empty, indicates cycle)

// Input: g = {0: [], 1: [], 2: []}
// Output: [0, 1, 2] or any permutation

// Input: g = {0: [1, 2], 1: [3], 2: [3], 3: []}
// Output: Valid topological order like [0, 1, 2, 3]

```

**Time Complexity:** O(V + E) - Visit each vertex and edge once
**Space Complexity:** O(V) - Store indegree and queue

## Q139. Number of Islands

**Problem:** Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

**Approach:** Count connected components of '1's using DFS or BFS. Mark visited cells to avoid recounting.

### Solution 1: DFS (Optimal)

```javascript
function numIslands(grid) {
  if (!grid || grid.length === 0) return 0;

  const m = grid.length;
  const n = grid[0].length;
  const visited = Array.from({ length: m }, () => Array(n).fill(false));
  const directions = [1, 0], [-1, 0], [0, 1], [0, -1];
  let count = 0;

  function dfs(row, col) {
    visited[row][col] = true;

    // Explore all 4 directions
    for (const [dr, dc] of directions) {
      const newRow = row + dr;
      const newCol = col + dc;

      if (newRow >= 0 && newRow < m &&
          newCol >= 0 && newCol < n &&
          grid[newRow][newCol] === '1' &&
          !visited[newRow][newCol]) {
        dfs(newRow, newCol);
      }
    }
  }

  // Count islands
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (grid[i][j] === '1' && !visited[i][j]) {
        count++;
        dfs(i, j);  // Mark entire island as visited
      }
    }
  }

  return count;
}

// Test Cases:
// Input: grid = ["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]
// Output: 1
// Explanation: One island of connected 1s

// Input: grid = ["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]
// Output: 3
// Explanation: Three separate islands

// Input: grid = ["1","1","1"],["0","1","0"],["1","1","1"]
// Output: 1
// Explanation: One island with hole in center

```

**Time Complexity:** O(m × n) - Visit each cell once
**Space Complexity:** O(m × n) - Visited array; O(m × n) recursion stack worst case

## Q140. Clone Graph

**Problem:** Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.

**Approach:** Use BFS/DFS to traverse graph. Create new nodes using a map (old → new). Wire edges as nodes are discovered.

### Solution 1: BFS with Mapping (Optimal)

```javascript
function cloneGraph(node) {
  if (!node) return null;

  const map = new Map();  // old -> new mapping
  const queue = [node];
  map.set(node, { val: node.val, neighbors: [] });

  while (queue.length) {
    const oldNode = queue.shift();

    for (const neighbor of oldNode.neighbors) {
      // Create new node if not exists
      if (!map.has(neighbor)) {
        map.set(neighbor, { val: neighbor.val, neighbors: [] });
        queue.push(neighbor);
      }
      // Wire edges
      map.get(oldNode).neighbors.push(map.get(neighbor));
    }
  }

  return map.get(node);
}

// Test Cases:
// Input: adjList = [2,4],[1,3],[2,4],[1,3]
// (Node 1 connects to 2,4; Node 2 connects to 1,3; etc.)
// Output: Deep copy with same structure

// Input: adjList = []
// Output: Deep copy of single node with no neighbors

// Input: adjList = []
// Output: null

// Input: adjList = [2],[1]
// Output: Deep copy of two connected nodes

```

**Time Complexity:** O(V + E) - Visit each vertex and edge once
**Space Complexity:** O(V) - Map stores all nodes

## Q141. Rotting Oranges

**Problem:** You are given an `m x n` grid where each cell can have one of three values:

- `0` representing an empty cell,

- `1` representing a fresh orange,

- `2` representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten. Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return `-1`.

**Approach:** Multi-source BFS from all rotten oranges. Time equals the number of levels until no fresh oranges remain.

### Solution 1: Multi-Source BFS (Optimal)

```javascript
function orangesRotting(grid) {
  if (!grid || grid.length === 0) return 0;

  const m = grid.length;
  const n = grid[0].length;
  const queue = [];
  let freshCount = 0;
  let time = 0;

  // Add all rotten oranges to queue and count fresh
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (grid[i][j] === 2) {
        queue.push([i, j]);
      } else if (grid[i][j] === 1) {
        freshCount++;
      }
    }
  }

  const directions = [1, 0], [-1, 0], [0, 1], [0, -1];

  // Process level by level
  while (queue.length && freshCount > 0) {
    const levelSize = queue.length;
    time++;

    for (let k = 0; k < levelSize; k++) {
      const [row, col] = queue.shift();

      // Check all 4 directions
      for (const [dr, dc] of directions) {
        const newRow = row + dr;
        const newCol = col + dc;

        if (newRow >= 0 && newRow < m &&
            newCol >= 0 && newCol < n &&
            grid[newRow][newCol] === 1) {
          grid[newRow][newCol] = 2;  // Rot the orange
          freshCount--;
          queue.push([newRow, newCol]);
        }
      }
    }
  }

  return freshCount === 0 ? time : -1;
}

```

**Time Complexity:** O(m × n) - Visit each cell once
**Space Complexity:** O(m × n) - Queue stores cells

## Q142. Course Schedule

**Problem:** There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` before course `ai`. Return `true` if you can finish all courses. Otherwise, return `false`.

**Approach:** Build directed graph from prerequisites. Detect cycle using Kahn's algorithm (topological sort). If all courses processed, no cycle exists.

### Solution 1: Kahn's Algorithm (Topological Sort) (Optimal)

```javascript
function canFinish(numCourses, prerequisites) {
  // Build graph
  const graph = Array.from({ length: numCourses }, () => []);
  for (const [course, prereq] of prerequisites) {
    graph[prereq].push(course);
  }

  // Calculate indegrees
  const indegree = new Array(numCourses).fill(0);
  for (const neighbors of graph) {
    for (const neighbor of neighbors) {
      indegree[neighbor]++;
    }
  }

  // Start with courses having no prerequisites
  const queue = [];
  for (let i = 0; i < numCourses; i++) {
    if (indegree[i] === 0) {
      queue.push(i);
    }
  }

  let processed = 0;

  while (queue.length) {
    const course = queue.shift();
    processed++;

    // Decrement indegree of neighbors
    for (const neighbor of graph[course]) {
      indegree[neighbor]--;
      if (indegree[neighbor] === 0) {
        queue.push(neighbor);
      }
    }
  }

  // If all courses processed, no cycle
  return processed === numCourses;
}

// Test Cases:
// Input: numCourses = 2, prerequisites = [1,0]
// Output: true

// Input: numCourses = 2, prerequisites = [1,0],[0,1]
// Output: false

// Input: numCourses = 3, prerequisites = [1,0],[2,1]
// Output: true

// Input: numCourses = 4, prerequisites = [1,0],[2,0],[3,1],[3,2]
// Output: true

```

**Time Complexity:** O(V + E) - V courses, E prerequisites
**Space Complexity:** O(V + E) - Graph and indegree arrays

## Q143. Is Graph Bipartite?

**Problem:** There is an undirected graph with `n` nodes, where each node is numbered between `0` and `n - 1`. You are given a 2D array `graph`, where `graph[u]` is an array of nodes that node `u` is adjacent to. A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B. Return `true` if and only if it is bipartite.

**Approach:** Use BFS to 2-color the graph. If adjacent nodes have the same color (conflict), graph has odd cycle and is not bipartite.

### Solution 1: BFS with 2-Coloring (Optimal)

```javascript
function isBipartite(graph) {
  const n = graph.length;
  const color = new Array(n).fill(0);  // 0: uncolored, 1: color A, -1: color B

  for (let start = 0; start < n; start++) {
    if (color[start] === 0) {
      // Start BFS from uncolored node
      color[start] = 1;
      const queue = [start];

      while (queue.length) {
        const node = queue.shift();

        for (const neighbor of graph[node]) {
          if (color[neighbor] === 0) {
            // Color neighbor with opposite color
            color[neighbor] = -color[node];
            queue.push(neighbor);
          } else if (color[neighbor] === color[node]) {
            // Conflict: adjacent nodes have same color
            return false;
          }
        }
      }
    }
  }

  return true;
}

// Test Cases:
// Input: graph = [1,2,3],[0,2],[0,1,3],[0,2]
// Output: false

// Input: graph = [1,3],[0,2],[1,3],[0,2]
// Output: true

// Input: graph = [1],[0]
// Output: true

// Input: graph = [],[],[],[]
// Output: true

```

**Time Complexity:** O(V + E) - Visit each vertex and edge once
**Space Complexity:** O(V) - Color array and queue

## Q144. Dijkstra's Algorithm

**Problem:** Find the shortest paths from a source node to all other nodes in a weighted graph with non-negative edge weights.

**Approach:** Use min-heap (priority queue) to always process the node with minimum distance. Relax edges to update distances.

### Solution 1: Min-Heap Implementation (Optimal)

```javascript
function dijkstra(n, edges, src) {
  // Build graph
  const graph = Array.from({ length: n }, () => []);
  for (const [u, v, w] of edges) {
    graph[u].push([v, w]);
    // For undirected graph, also add reverse edge
    // graph[v].push([u, w]);
  }

  const dist = new Array(n).fill(Infinity);
  dist[src] = 0;

  // Min-heap: [distance, node]
  const heap = new Heap((a, b) => a[0] < b[0]);
  heap.push([0, src]);

  while (heap.size()) {
    const [d, u] = heap.pop();

    // Skip if outdated (lazy deletion)
    if (d !== dist[u]) continue;

    // Relax edges
    for (const [v, w] of graph[u]) {
      if (dist[u] + w < dist[v]) {
        dist[v] = dist[u] + w;
        heap.push([dist[v], v]);
      }
    }
  }

  return dist;
}

```

**Time Complexity:** O((V + E) log V) - Each vertex and edge processed, heap operations O(log V)
**Space Complexity:** O(V + E) - Graph and heap

## Q145. Bellman-Ford Algorithm

**Problem:** Find shortest paths from a source node to all other nodes in a weighted graph that may contain negative edge weights. Also detect if there are any negative cycles.

**Approach:** Relax all edges V-1 times. If distances can still be improved in V-th pass, negative cycle exists.

### Solution 1: Bellman-Ford (Optimal)

```javascript
function bellmanFord(n, edges, src) {
  const dist = new Array(n).fill(Infinity);
  dist[src] = 0;

  // Relax edges V-1 times
  for (let i = 0; i < n - 1; i++) {
    for (const [u, v, w] of edges) {
      if (dist[u] !== Infinity && dist[u] + w < dist[v]) {
        dist[v] = dist[u] + w;
      }
    }
  }

  // Check for negative cycles (V-th pass)
  for (const [u, v, w] of edges) {
    if (dist[u] !== Infinity && dist[u] + w < dist[v]) {
      return null; // Negative cycle detected
    }
  }

  return dist;
}

```

**Time Complexity:** O(V × E) - Relax edges V-1 times
**Space Complexity:** O(V) - Distance array

## Q146. Floyd-Warshall Algorithm

**Problem:** Find shortest paths between all pairs of vertices in a weighted graph. The graph may contain negative edge weights but no negative cycles.

**Approach:** Dynamic programming over intermediate nodes. For each intermediate node k, update shortest path between i and j using k.

### Solution 1: Floyd-Warshall (Optimal)

```javascript
function floydWarshall(dist) {
  const n = dist.length;

  // For each intermediate node k
  for (let k = 0; k < n; k++) {
    // For each source i
    for (let i = 0; i < n; i++) {
      // For each destination j
      for (let j = 0; j < n; j++) {
        // Update if path through k is shorter
        if (dist[i][k] !== Infinity && dist[k][j] !== Infinity) {
          dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
        }
      }
    }
  }

  return dist;
}

```

**Time Complexity:** O(V³) - Three nested loops over V vertices
**Space Complexity:** O(V²) - Distance matrix

## Q147. Minimum Spanning Tree (Kruskal's & Prim's)

**Problem:** Find the minimum spanning tree (MST) of a connected, undirected, weighted graph. The MST is a subset of edges that connects all vertices with minimum total weight.

**Approach:**

- **Kruskal's:** Sort edges by weight, use union-find to join safe edges (don't create cycles)

- **Prim's:** Start from any vertex, grow MST using priority queue to add minimum-weight edges

### Solution 1: Kruskal's Algorithm

```javascript
function kruskalMST(n, edges) {
  // Sort edges by weight
  edges.sort((a, b) => a[2] - b[2]);

  // Union-Find data structure
  const parent = Array.from({ length: n }, (_, i) => i);
  const rank = new Array(n).fill(0);

  function find(x) {
    if (parent[x] !== x) {
      parent[x] = find(parent[x]); // Path compression
    }
    return parent[x];
  }

  function union(a, b) {
    a = find(a);
    b = find(b);
    if (a === b) return false; // Same component

    // Union by rank
    if (rank[a] < rank[b]) {
      [a, b] = [b, a];
    }
    parent[b] = a;
    if (rank[a] === rank[b]) {
      rank[a]++;
    }
    return true;
  }

  let cost = 0;
  const mst = [];

  for (const [u, v, w] of edges) {
    if (union(u, v)) {
      cost += w;
      mst.push([u, v, w]);
    }
  }

  return { cost, mst };
}

```

### Solution 2: Prim's Algorithm

```javascript
function primMST(n, edges) {
  // Build graph
  const graph = Array.from({ length: n }, () => []);
  for (const [u, v, w] of edges) {
    graph[u].push([v, w]);
    graph[v].push([u, w]);
  }

  const heap = new Heap((a, b) => a[0] < b[0]); // Min-heap: [weight, node]
  const visited = new Set();
  let cost = 0;
  const mst = [];

  // Start from node 0
  heap.push([0, 0, -1]); // [weight, node, parent]

  while (heap.size() && visited.size < n) {
    const [w, u, parent] = heap.pop();

    if (visited.has(u)) continue;

    visited.add(u);
    cost += w;
    if (parent !== -1) {
      mst.push([parent, u, w]);
    }

    // Add neighbors to heap
    for (const [v, weight] of graph[u]) {
      if (!visited.has(v)) {
        heap.push([weight, v, u]);
      }
    }
  }

  return { cost, mst };
}

```

**Time Complexity:** Kruskal: O(E log E), Prim: O(E log V)
**Space Complexity:** O(V + E) - Graph and union-find/heap

## Q148. Bridges in Graph

**Problem:** Find all bridges (critical edges) in an undirected graph. A bridge is an edge whose removal increases the number of connected components in the graph.

**Approach:** Use Tarjan's algorithm with DFS. Track discovery time (tin) and low-link value. Edge (u,v) is a bridge if low[v] > tin[u].

### Solution 1: Tarjan's Algorithm (Optimal)

```javascript
function findBridges(n, graph) {
  const tin = new Array(n).fill(-1);  // Discovery time
  const low = new Array(n).fill(0);   // Low-link value
  let time = 0;
  const bridges = [];

  function dfs(u, parent) {
    tin[u] = low[u] = time++;

    for (const v of graph[u] || []) {
      if (v === parent) continue;  // Skip parent

      if (tin[v] !== -1) {
        // Back edge: update low-link
        low[u] = Math.min(low[u], tin[v]);
      } else {
        // Tree edge: explore
        dfs(v, u);
        low[u] = Math.min(low[u], low[v]);

        // Bridge condition: low[v] > tin[u]
        if (low[v] > tin[u]) {
          bridges.push([u, v]);
        }
      }
    }
  }

  for (let i = 0; i < n; i++) {
    if (tin[i] === -1) {
      dfs(i, -1);
    }
  }

  return bridges;
}

```

**Time Complexity:** O(V + E) - Visit each vertex and edge once
**Space Complexity:** O(V) - Arrays and recursion stack

## Q149. Articulation Points (Cut Vertices)

**Problem:** Find all articulation points (cut vertices) in an undirected graph. An articulation point is a vertex whose removal increases the number of connected components.

**Approach:** Use Tarjan's algorithm. Node u is articulation point if: (1) root with >1 DFS children, or (2) non-root with child v where low[v] >= tin[u].

### Solution 1: Tarjan's Algorithm (Optimal)

```javascript
function findArticulationPoints(n, graph) {
  const tin = new Array(n).fill(-1);  // Discovery time
  const low = new Array(n).fill(0);   // Low-link value
  const isArticulation = new Array(n).fill(false);
  let time = 0;

  function dfs(u, parent) {
    tin[u] = low[u] = time++;
    let children = 0;

    for (const v of graph[u] || []) {
      if (v === parent) continue;

      if (tin[v] !== -1) {
        // Back edge: update low-link
        low[u] = Math.min(low[u], tin[v]);
      } else {
        // Tree edge: explore
        children++;
        dfs(v, u);
        low[u] = Math.min(low[u], low[v]);

        // Articulation point condition: low[v] >= tin[u]
        if (parent !== -1 && low[v] >= tin[u]) {
          isArticulation[u] = true;
        }
      }
    }

    // Root special case: >1 children
    if (parent === -1 && children > 1) {
      isArticulation[u] = true;
    }
  }

  for (let i = 0; i < n; i++) {
    if (tin[i] === -1) {
      dfs(i, -1);
    }
  }

  return isArticulation.map((is, i) => is ? i : null).filter(v => v !== null);
}

```

**Time Complexity:** O(V + E) - Visit each vertex and edge once
**Space Complexity:** O(V) - Arrays and recursion stack

## Q150. Shortest Path in DAG

**Problem:** Find shortest paths from a source node to all other nodes in a directed acyclic graph (DAG). The graph may contain negative edge weights.

**Approach:** First perform topological sort to get linear ordering. Then relax edges once in topological order.

### Solution 1: Topological Sort + Edge Relaxation (Optimal)

```javascript
function dagShortestPath(n, edges, src) {
  // Build graph and calculate indegree
  const graph = Array.from({ length: n }, () => []);
  const indegree = new Array(n).fill(0);

  for (const [u, v, w] of edges) {
    graph[u].push([v, w]);
    indegree[v]++;
  }

  // Topological sort using Kahn's algorithm
  const queue = [];
  const order = [];

  for (let i = 0; i < n; i++) {
    if (indegree[i] === 0) {
      queue.push(i);
    }
  }

  while (queue.length) {
    const u = queue.shift();
    order.push(u);

    for (const [v, w] of graph[u]) {
      indegree[v]--;
      if (indegree[v] === 0) {
        queue.push(v);
      }
    }
  }

  // Relax edges in topological order
  const dist = new Array(n).fill(Infinity);
  dist[src] = 0;

  for (const u of order) {
    if (dist[u] === Infinity) continue;

    for (const [v, w] of graph[u]) {
      dist[v] = Math.min(dist[v], dist[u] + w);
    }
  }

  return dist;
}

```

**Time Complexity:** O(V + E) - Topological sort + edge relaxation
**Space Complexity:** O(V + E) - Graph and distance array

## Q151. Detect Cycle in Directed Graph (DAG Check)

**Problem:** Determine if a directed graph is acyclic (DAG). Return `true` if no cycles exist, `false` otherwise.

**Approach:** Use topological sort (Kahn's algorithm). If all nodes processed, graph is DAG. If not all nodes processed, cycle exists.

### Solution 1: Kahn's Algorithm (Topological Sort) (Optimal)

```javascript
function isDAG(n, edges) {
  // Build graph
  const graph = Array.from({ length: n }, () => []);
  const indegree = new Array(n).fill(0);

  for (const [u, v] of edges) {
    graph[u].push(v);
    indegree[v]++;
  }

  // Kahn's algorithm
  const queue = [];
  for (let i = 0; i < n; i++) {
    if (indegree[i] === 0) {
      queue.push(i);
    }
  }

  let processed = 0;

  while (queue.length) {
    const u = queue.shift();
    processed++;

    for (const v of graph[u]) {
      indegree[v]--;
      if (indegree[v] === 0) {
        queue.push(v);
      }
    }
  }

  // If all nodes processed, no cycle (DAG)
  return processed === n;
}

```

**Time Complexity:** O(V + E) - Visit each vertex and edge once
**Space Complexity:** O(V + E) - Graph and indegree arrays

## Q152. Word Ladder

**Problem:** A transformation sequence from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words such that:

- The first word in the sequence is `beginWord`

- The last word in the sequence is `endWord`

- Only one letter can be changed at a time

- Each transformed word must exist in `wordList`

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return the number of words in the shortest transformation sequence from `beginWord` to `endWord`, or `0` if no such sequence exists.

**Approach:** Use BFS with pattern matching. Generate patterns with wildcards (*) to find neighbors efficiently. Track steps (level) until target is reached.

### Solution 1: BFS with Pattern Matching (Optimal)

```javascript
function ladderLength(beginWord, endWord, wordList) {
  const wordSet = new Set(wordList);
  if (!wordSet.has(endWord)) return 0;

  // Build pattern map: pattern -> words
  const patternMap = new Map();

  function addPattern(word, index) {
    const pattern = word.slice(0, index) + '*' + word.slice(index + 1);
    if (!patternMap.has(pattern)) {
      patternMap.set(pattern, []);
    }
    patternMap.get(pattern).push(word);
  }

  // Build pattern map for all words
  for (const word of wordSet) {
    for (let i = 0; i < word.length; i++) {
      addPattern(word, i);
    }
  }

  // BFS
  const queue = [beginWord, 1];
  const visited = new Set([beginWord]);

  while (queue.length) {
    const [word, steps] = queue.shift();

    if (word === endWord) return steps;

    // Generate all patterns for current word
    for (let i = 0; i < word.length; i++) {
      const pattern = word.slice(0, i) + '*' + word.slice(i + 1);

      // Get neighbors from pattern
      for (const neighbor of patternMap.get(pattern) || []) {
        if (!visited.has(neighbor)) {
          visited.add(neighbor);
          queue.push([neighbor, steps + 1]);
        }
      }
    }
  }

  return 0;
}

```

**Time Complexity:** O(N × L²) - N words, L length, pattern generation O(L)
**Space Complexity:** O(N × L) - Pattern map and queue

## Q153. Snakes and Ladders

**Problem:** You are given an `n x n` board. You start at square `1` and move to square `n²` by rolling a die. On each square, if there's a snake or ladder, you move to the destination. Return the minimum number of moves required to reach square `n²`, or `-1` if it is not possible.

**Approach:** Use BFS on board indices. For each square, try all 6 dice moves. Apply snake/ladder mapping if present.

### Solution 1: BFS with Board Mapping (Optimal)

```javascript
function snakesAndLadders(board) {
  const n = board.length;
  const target = n * n;

  // Convert square number to board coordinates
  function getCoordinates(square) {
    const row = Math.floor((square - 1) / n);
    const col = (square - 1) % n;
    // Reverse row for Boustrophedon style
    const r = n - 1 - row;
    // Reverse col for odd rows
    const c = row % 2 === 0 ? col : n - 1 - col;
    return [r, c];
  }

  const queue = [1, 0];  // [square, moves]
  const visited = new Set([1]);

  while (queue.length) {
    const [square, moves] = queue.shift();

    if (square === target) return moves;

    // Try all 6 dice moves
    for (let k = 1; k <= 6 && square + k <= target; k++) {
      let nextSquare = square + k;

      // Check for snake or ladder
      const [r, c] = getCoordinates(nextSquare);
      if (board[r][c] !== -1) {
        nextSquare = board[r][c];
      }

      if (!visited.has(nextSquare)) {
        visited.add(nextSquare);
        queue.push([nextSquare, moves + 1]);
      }
    }
  }

  return -1;
}

```

**Time Complexity:** O(n²) - Visit each square at most once
**Space Complexity:** O(n²) - Queue and visited set

## Q154. Disjoint Set Union (Union-Find)

**Problem:** Implement a Disjoint Set Union (DSU) data structure that supports efficient union and find operations with path compression and union by rank optimizations.

**Approach:** Use parent array and rank array. Path compression flattens tree during find. Union by rank attaches smaller tree to larger tree.

### Solution 1: Union-Find with Optimizations (Optimal)

```javascript
class DSU {
  constructor(n) {
    this.parent = Array.from({ length: n }, (_, i) => i);
    this.rank = new Array(n).fill(0);
  }

  find(x) {
    // Path compression
    if (this.parent[x] !== x) {
      this.parent[x] = this.find(this.parent[x]);
    }
    return this.parent[x];
  }

  union(a, b) {
    a = this.find(a);
    b = this.find(b);

    if (a === b) return false;  // Already in same set

    // Union by rank: attach smaller tree to larger
    if (this.rank[a] < this.rank[b]) {
      [a, b] = [b, a];
    }

    this.parent[b] = a;

    // Increase rank if ranks are equal
    if (this.rank[a] === this.rank[b]) {
      this.rank[a]++;
    }

    return true;
  }

  connected(a, b) {
    return this.find(a) === this.find(b);
  }
}

```

**Time Complexity:** O(α(n)) amortized - Inverse Ackermann function (nearly constant)
**Space Complexity:** O(n) - Parent and rank arrays

## Q155. Tarjan's Algorithm for Strongly Connected Components

**Problem:** Find all strongly connected components (SCCs) in a directed graph. A strongly connected component is a maximal set of vertices where every vertex can reach every other vertex.

**Approach:** Use Tarjan's algorithm with DFS. Track discovery time (id) and low-link value. Use stack to track current DFS path. When low[u] === id[u], pop stack to form SCC.

### Solution 1: Tarjan's Algorithm (Optimal)

```javascript
function tarjansSCC(n, graph) {
  const id = new Array(n).fill(-1);      // Discovery time
  const low = new Array(n).fill(0);      // Low-link value
  const onStack = new Array(n).fill(false);  // On DFS stack
  const stack = [];
  let currentId = 0;
  const components = [];

  function dfs(u) {
    id[u] = low[u] = currentId++;
    stack.push(u);
    onStack[u] = true;

    for (const v of graph[u] || []) {
      if (id[v] === -1) {
        // Unvisited: explore
        dfs(v);
        low[u] = Math.min(low[u], low[v]);
      } else if (onStack[v]) {
        // Back edge: update low-link
        low[u] = Math.min(low[u], id[v]);
      }
    }

    // Root of SCC: pop stack to form component
    if (low[u] === id[u]) {
      const component = [];
      while (true) {
        const x = stack.pop();
        onStack[x] = false;
        component.push(x);
        if (x === u) break;
      }
      components.push(component);
    }
  }

  for (let i = 0; i < n; i++) {
    if (id[i] === -1) {
      dfs(i);
    }
  }

  return components;
}

```

**Time Complexity:** O(V + E) - Visit each vertex and edge once
**Space Complexity:** O(V) - Arrays and stack

## Q156. Surrounded Regions

**Problem:** Given an `m x n` matrix `board` containing `'X'` and `'O'`, capture all regions that are 4-directionally surrounded by `'X'`. A region is captured by flipping all `'O'`s into `'X'`s in that surrounded region. Note that `'O'`s connected to the border are not captured.

**Approach:** Mark all 'O' cells connected to border using DFS/BFS. Then flip remaining 'O' to 'X'. Restore marked cells back to 'O'.

### Solution 1: DFS from Borders (Optimal)

```javascript
function solve(board) {
  if (!board.length || !board[0].length) return;

  const m = board.length;
  const n = board[0].length;

  // Mark border-connected 'O' with DFS
  function dfs(row, col) {
    if (row < 0 || row >= m || col < 0 || col >= n || board[row][col] !== 'O') {
      return;
    }

    board[row][col] = '#';  // Mark as border-connected

    // Explore 4 directions
    dfs(row + 1, col);
    dfs(row - 1, col);
    dfs(row, col + 1);
    dfs(row, col - 1);
  }

  // Mark from all borders
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
      if (board[i][j] === 'O') {
        board[i][j] = 'X';
      } else if (board[i][j] === '#') {
        board[i][j] = 'O';
      }
    }
  }
}

// Test Cases:
// Input: board = ["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]
// Output: ["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]
// Explanation: Border-connected 'O' at (3,1) remains; others flipped

// Input: board = ["X"]
// Output: ["X"]

```

**Time Complexity:** O(m × n) - Visit each cell once
**Space Complexity:** O(m × n) - DFS recursion depth (worst case)

## Q157. Evaluate Division

**Problem:** You are given an array of variable pairs `equations` and an array of real numbers `values`, where `equations[i] = [Ai, Bi]` and `values[i]` represent the equation `Ai / Bi = values[i]`. You are also given some queries, where `queries[j] = [Cj, Dj]` represents the jth query where you must find the answer for `Cj / Dj = ?`.

Return the answers to all queries. If a single answer cannot be determined, return `-1.0`.

**Approach:** Build weighted directed graph from equations. Use DFS/BFS to find path from numerator to denominator, multiplying values along path.

### Solution 1: Graph Construction + DFS (Optimal)

```javascript
function calcEquation(equations, values, queries) {
  // Build graph: node -> {neighbor: value}
  const graph = new Map();

  for (let i = 0; i < equations.length; i++) {
    const [a, b] = equations[i];
    const val = values[i];

    if (!graph.has(a)) graph.set(a, new Map());
    if (!graph.has(b)) graph.set(b, new Map());

    // a / b = val, so edge a->b has weight val
    graph.get(a).set(b, val);
    // b / a = 1/val, so edge b->a has weight 1/val
    graph.get(b).set(a, 1 / val);
  }

  // DFS to find path and compute result
  function dfs(start, end, visited) {
    // Nodes don't exist
    if (!graph.has(start) || !graph.has(end)) return -1.0;

    // Same node
    if (start === end) return 1.0;

    visited.add(start);

    // Explore neighbors
    for (const [neighbor, value] of graph.get(start)) {
      if (!visited.has(neighbor)) {
        const result = dfs(neighbor, end, visited);
        if (result !== -1.0) {
          // Found path: multiply values along path
          return value * result;
        }
      }
    }

    visited.delete(start);
    return -1.0;
  }

  // Process all queries
  const results = [];
  for (const [start, end] of queries) {
    results.push(dfs(start, end, new Set()));
  }

  return results;
}

// Test Cases:
// Input: equations = ["a","b"],["b","c"], values = [2.0,3.0],
// queries = ["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]
// Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
// Explanation:
// a / b = 2.0, b / c = 3.0
// a / c = 6.0, b / a = 0.5
// a / e = -1.0 (not found), a / a = 1.0, x / x = -1.0 (not found)

```

**Time Complexity:** O(n × q) - n equations, q queries, each query may visit all nodes
**Space Complexity:** O(n) - Graph storage

## Q158. Course Schedule II

**Problem:** There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` before course `ai`. Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

**Approach:** Use topological sort (Kahn's algorithm). If all courses processed, return order. If not all processed, cycle exists—return empty array.

### Solution 1: Kahn's Algorithm (Topological Sort) (Optimal)

```javascript
function findOrder(numCourses, prerequisites) {
  // Build graph
  const graph = Array.from({ length: numCourses }, () => []);
  const indegree = new Array(numCourses).fill(0);

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

  // If all courses processed, return order; else cycle exists
  return result.length === numCourses ? result : [];
}

// Test Cases:
// Input: numCourses = 2, prerequisites = [1,0]
// Output: [0,1]
// Explanation: Take course 0 then course 1

// Input: numCourses = 4, prerequisites = [1,0],[2,0],[3,1],[3,2]
// Output: [0,2,1,3]
// Explanation: Valid order: 0, then 1 or 2, then 3

// Input: numCourses = 1, prerequisites = []
// Output: [0]

```

**Time Complexity:** O(V + E) - Build graph + Kahn's algorithm
**Space Complexity:** O(V + E) - Graph and indegree arrays

## Q159. Minimum Genetic Mutation

**Problem:** A gene string can be represented by an 8-character long string, with choices from `'A'`, `'C'`, `'G'`, and `'T'`. Suppose we need to investigate a mutation from a gene string `start` to a gene string `end` where one mutation is defined as one single character changed in the gene string. Given the two gene strings `start` and `end` and the gene bank `bank`, return the minimum number of mutations needed to mutate from `start` to `end`. If there is no such a mutation, return `-1`.

**Approach:** Use BFS to find shortest path. Generate all valid mutations (one character change) and check if in bank.

### Solution 1: BFS with Mutation Generation (Optimal)

```javascript
function minMutation(start, end, bank) {
  const bankSet = new Set(bank);
  if (!bankSet.has(end)) return -1;

  const choices = ['A', 'C', 'G', 'T'];
  const queue = [start, 0];  // [gene, mutations]
  const visited = new Set([start]);

  while (queue.length) {
    const [current, mutations] = queue.shift();

    if (current === end) return mutations;

    // Generate all possible mutations
    for (let i = 0; i < current.length; i++) {
      for (const choice of choices) {
        if (choice === current[i]) continue;  // Skip same character

        // Create mutation
        const next = current.substring(0, i) + choice + current.substring(i + 1);

        // Check if valid and not visited
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

---

## 📍 Navigation

<div align="center">

[Heaps & Priority Queue](7%20Heaps%20&%20Priority%20Queue.md) • [Home: README](README.md) • [Dynamic Programming →](9%20Dynamic%20Programming.md)

[📋 Cheatsheet](DSA%20Interview%20Cheatsheet.md]

</div>
