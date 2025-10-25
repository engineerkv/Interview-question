# 🧩 DSA Interview Notes - LeetCode Top 150

## 🌐 Section 11 — Graph / DFS / BFS — Q117-Q125

---

### 117. 🌐 Number of Islands

**🧠 Concept**

Count number of islands in 2D grid using DFS to mark connected land cells as visited.

**💻 Example**

```javascript
function numIslands(grid) {
  if (!grid || grid.length === 0) return 0;
  
  const m = grid.length;
  const n = grid[0].length;
  let count = 0;
  
  function dfs(row, col) {
    if (row < 0 || row >= m || col < 0 || col >= n || grid[row][col] !== '1') {
      return;
    }
    
    grid[row][col] = '0';
    dfs(row + 1, col);
    dfs(row - 1, col);
    dfs(row, col + 1);
    dfs(row, col - 1);
  }
  
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (grid[i][j] === '1') {
        count++;
        dfs(i, j);
      }
    }
  }
  
  return count;
}
```

**💬 Explanation + Insight**

- **DFS Exploration** - Explore all connected land cells
- **Visited Marking** - Mark cells as visited by changing to '0'
- **Island Counting** - Count each unvisited land cell as new island
- **Time Complexity** - O(m*n) visit each cell once
- **Space Complexity** - O(m*n) recursion stack in worst case

---

### 118. 🌐 Surrounded Regions

**🧠 Concept**

Capture surrounded regions by marking border-connected 'O's as safe, then flipping remaining 'O's.

**💻 Example**

```javascript
function solve(board) {
  if (!board || board.length === 0) return;
  
  const m = board.length;
  const n = board[0].length;
  
  function dfs(row, col) {
    if (row < 0 || row >= m || col < 0 || col >= n || board[row][col] !== 'O') {
      return;
    }
    
    board[row][col] = 'T';
    dfs(row + 1, col);
    dfs(row - 1, col);
    dfs(row, col + 1);
    dfs(row, col - 1);
  }
  
  // Mark border-connected 'O's as safe
  for (let i = 0; i < m; i++) {
    dfs(i, 0);
    dfs(i, n - 1);
  }
  for (let j = 0; j < n; j++) {
    dfs(0, j);
    dfs(m - 1, j);
  }
  
  // Flip remaining 'O's to 'X' and restore 'T's to 'O'
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (board[i][j] === 'O') board[i][j] = 'X';
      if (board[i][j] === 'T') board[i][j] = 'O';
    }
  }
}
```

**💬 Explanation + Insight**

- **Border DFS** - Start DFS from all border cells
- **Safe Marking** - Mark border-connected cells as safe
- **Two Pass Approach** - First mark safe, then flip remaining
- **Time Complexity** - O(m*n) visit each cell once
- **Space Complexity** - O(m*n) recursion stack

---

### 119. 🌐 Clone Graph

**🧠 Concept**

Deep clone undirected graph using DFS with visited map to avoid cycles and duplicate nodes.

**💻 Example**

```javascript
function cloneGraph(node) {
  if (!node) return null;
  
  const visited = new Map();
  
  function dfs(original) {
    if (visited.has(original)) {
      return visited.get(original);
    }
    
    const clone = new Node(original.val);
    visited.set(original, clone);
    
    for (const neighbor of original.neighbors) {
      clone.neighbors.push(dfs(neighbor));
    }
    
    return clone;
  }
  
  return dfs(node);
}
```

**💬 Explanation + Insight**

- **Visited Map** - Track original to clone mapping
- **Cycle Handling** - Return existing clone if already visited
- **Neighbor Cloning** - Recursively clone all neighbors
- **Time Complexity** - O(n) where n is number of nodes
- **Space Complexity** - O(n) for visited map and recursion

---

### 120. 🌐 Evaluate Division

**🧠 Concept**

Evaluate division queries using graph representation with DFS to find path between variables.

**💻 Example**

```javascript
function calcEquation(equations, values, queries) {
  const graph = new Map();
  
  // Build graph
  for (let i = 0; i < equations.length; i++) {
    const [a, b] = equations[i];
    const value = values[i];
    
    if (!graph.has(a)) graph.set(a, []);
    if (!graph.has(b)) graph.set(b, []);
    
    graph.get(a).push([b, value]);
    graph.get(b).push([a, 1 / value]);
  }
  
  function dfs(start, end, visited) {
    if (start === end) return 1;
    if (!graph.has(start)) return -1;
    
    visited.add(start);
    for (const [neighbor, value] of graph.get(start)) {
      if (visited.has(neighbor)) continue;
      
      const result = dfs(neighbor, end, visited);
      if (result !== -1) return value * result;
    }
    
    return -1;
  }
  
  return queries.map(([a, b]) => dfs(a, b, new Set()));
}
```

**💬 Explanation + Insight**

- **Graph Construction** - Build bidirectional graph with weights
- **DFS Path Finding** - Find path between variables
- **Weight Multiplication** - Multiply weights along path
- **Time Complexity** - O(q*n) where q is queries, n is variables
- **Space Complexity** - O(n) for graph and recursion

---

### 121. 🌐 Course Schedule

**🧠 Concept**

Check if course schedule is possible using topological sort with cycle detection.

**💻 Example**

```javascript
function canFinish(numCourses, prerequisites) {
  const graph = Array(numCourses).fill().map(() => []);
  const inDegree = Array(numCourses).fill(0);
  
  // Build graph and calculate in-degrees
  for (const [course, prereq] of prerequisites) {
    graph[prereq].push(course);
    inDegree[course]++;
  }
  
  const queue = [];
  for (let i = 0; i < numCourses; i++) {
    if (inDegree[i] === 0) {
      queue.push(i);
    }
  }
  
  let completed = 0;
  while (queue.length > 0) {
    const course = queue.shift();
    completed++;
    
    for (const nextCourse of graph[course]) {
      inDegree[nextCourse]--;
      if (inDegree[nextCourse] === 0) {
        queue.push(nextCourse);
      }
    }
  }
  
  return completed === numCourses;
}
```

**💬 Explanation + Insight**

- **Topological Sort** - Use Kahn's algorithm for cycle detection
- **In-degree Tracking** - Track number of prerequisites for each course
- **Queue Processing** - Process courses with no prerequisites first
- **Time Complexity** - O(V + E) where V is courses, E is prerequisites
- **Space Complexity** - O(V + E) for graph and in-degree array

---

### 122. 🌐 Course Schedule II

**🧠 Concept**

Return valid course ordering using topological sort with result tracking.

**💻 Example**

```javascript
function findOrder(numCourses, prerequisites) {
  const graph = Array(numCourses).fill().map(() => []);
  const inDegree = Array(numCourses).fill(0);
  
  for (const [course, prereq] of prerequisites) {
    graph[prereq].push(course);
    inDegree[course]++;
  }
  
  const queue = [];
  const result = [];
  
  for (let i = 0; i < numCourses; i++) {
    if (inDegree[i] === 0) {
      queue.push(i);
    }
  }
  
  while (queue.length > 0) {
    const course = queue.shift();
    result.push(course);
    
    for (const nextCourse of graph[course]) {
      inDegree[nextCourse]--;
      if (inDegree[nextCourse] === 0) {
        queue.push(nextCourse);
      }
    }
  }
  
  return result.length === numCourses ? result : [];
}
```

**💬 Explanation + Insight**

- **Result Tracking** - Track completed courses in order
- **Valid Ordering** - Return empty array if cycle detected
- **Topological Sort** - Process courses in dependency order
- **Time Complexity** - O(V + E) where V is courses, E is prerequisites
- **Space Complexity** - O(V + E) for graph and result

---

### 123. 🌐 Snakes and Ladders

**🧠 Concept**

Find minimum moves to reach end of board game using BFS with dice roll simulation.

**💻 Example**

```javascript
function snakesAndLadders(board) {
  const n = board.length;
  const target = n * n;
  
  function getPosition(square) {
    const row = Math.floor((square - 1) / n);
    const col = (square - 1) % n;
    return row % 2 === 0 ? [n - 1 - row, col] : [n - 1 - row, n - 1 - col];
  }
  
  const queue = [[1, 0]];
  const visited = new Set([1]);
  
  while (queue.length > 0) {
    const [square, moves] = queue.shift();
    
    if (square === target) return moves;
    
    for (let i = 1; i <= 6; i++) {
      let nextSquare = square + i;
      
      if (nextSquare > target) break;
      
      const [row, col] = getPosition(nextSquare);
      if (board[row][col] !== -1) {
        nextSquare = board[row][col];
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

**💬 Explanation + Insight**

- **BFS Shortest Path** - Find minimum moves using BFS
- **Dice Simulation** - Try all possible dice rolls (1-6)
- **Snake/Ladder Handling** - Follow snake/ladder if present
- **Time Complexity** - O(n²) where n is board size
- **Space Complexity** - O(n²) for queue and visited set

---

### 124. 🌐 Minimum Genetic Mutation

**🧠 Concept**

Find minimum mutations to transform start gene to end gene using BFS with valid mutation checking.

**💻 Example**

```javascript
function minMutation(start, end, bank) {
  const bankSet = new Set(bank);
  if (!bankSet.has(end)) return -1;
  
  const queue = [[start, 0]];
  const visited = new Set([start]);
  
  while (queue.length > 0) {
    const [gene, mutations] = queue.shift();
    
    if (gene === end) return mutations;
    
    for (let i = 0; i < gene.length; i++) {
      for (const char of 'ACGT') {
        if (gene[i] === char) continue;
        
        const newGene = gene.substring(0, i) + char + gene.substring(i + 1);
        
        if (bankSet.has(newGene) && !visited.has(newGene)) {
          visited.add(newGene);
          queue.push([newGene, mutations + 1]);
        }
      }
    }
  }
  
  return -1;
}
```

**💬 Explanation + Insight**

- **BFS Shortest Path** - Find minimum mutations using BFS
- **Mutation Generation** - Try all possible single character changes
- **Bank Validation** - Only consider mutations in bank
- **Time Complexity** - O(bank_size * gene_length * 4)
- **Space Complexity** - O(bank_size) for queue and visited

---

### 125. 🌐 Word Ladder

**🧠 Concept**

Find shortest transformation sequence from begin word to end word using BFS with word variation.

**💻 Example**

```javascript
function ladderLength(beginWord, endWord, wordList) {
  const wordSet = new Set(wordList);
  if (!wordSet.has(endWord)) return 0;
  
  const queue = [[beginWord, 1]];
  const visited = new Set([beginWord]);
  
  while (queue.length > 0) {
    const [word, length] = queue.shift();
    
    if (word === endWord) return length;
    
    for (let i = 0; i < word.length; i++) {
      for (let j = 0; j < 26; j++) {
        const newWord = word.substring(0, i) + 
                       String.fromCharCode(97 + j) + 
                       word.substring(i + 1);
        
        if (wordSet.has(newWord) && !visited.has(newWord)) {
          visited.add(newWord);
          queue.push([newWord, length + 1]);
        }
      }
    }
  }
  
  return 0;
}
```

**💬 Explanation + Insight**

- **BFS Shortest Path** - Find minimum transformations using BFS
- **Word Variation** - Try all possible single character changes
- **Dictionary Validation** - Only consider words in word list
- **Time Complexity** - O(M²*N) where M is word length, N is word count
- **Space Complexity** - O(M*N) for queue and visited set

---

*This comprehensive graph, DFS, and BFS section covers essential graph algorithms including traversal, shortest path finding, cycle detection, and advanced graph processing techniques.*