# Recursion & Backtracking

## Q141. N- Queens

Concept: Place queens row by row, pruning columns and diagonals using sets.

Example:
```javascript
function solveNQueens(n) {
  const res = [];
  const col = new Set();
  const d1 = new Set(); // diagonal r - c
  const d2 = new Set(); // diagonal r + c
  const board = Array.from({ length: n }, () => '.'.repeat(n).split(''));

  function bt(r) {
    if (r === n) {
      res.push(board.map(x => x.join('')));
      return;
    }
    for (let c = 0; c < n; c++) {
      if (col.has(c) || d1.has(r - c) || d2.has(r + c)) continue;
      col.add(c);
      d1.add(r - c);
      d2.add(r + c);
      board[r][c] = 'Q';
      bt(r + 1);
      board[r][c] = '.';
      col.delete(c);
      d1.delete(r - c);
      d2.delete(r + c);
    }
  }
  bt(0);
  return res;
}

// Test Cases:
// Input: n = 4
// Output: [
//   [".Q..","...Q","Q...","..Q."],
//   ["..Q.","Q...","...Q",".Q.."]
// ]

// Input: n = 1
// Output: [["Q"]]

// Input: n = 3
// Output: [] (no solution exists for n=3)

// Input: n = 2
// Output: [] (no solution exists for n=2)
```

**Time Complexity:** O(n!) -Backtracking generates all valid queen placements  
**Space Complexity:** O(n²) - Board storage plus O(n) recursion stack

Deep Insights:
  - Rule: Place queens row by row, pruning columns and diagonals using sets; O(n!) time, O(n²) space.
  - Real-world: N-queens problems, constraint satisfaction, puzzle solving, backtracking algorithms.
  - Common mistake: Symmetry not exploited here; not pruning diagonals correctly; forgetting to backtrack.
  - Optimization: O(n!) time worst-case; pruning reduces search space; symmetry not exploited here.
  - Interview tip: Explain backtracking clearly; mention diagonal pruning; ask about optimization techniques.
## Q142. Sudoku Solver

Concept: Backtrack cell by cell; maintain row/col/box availability.

Example:
```javascript
function solveSudoku(board) {
  const R = Array.from({ length: 9 }, () => new Set());
  const C = Array.from({ length: 9 }, () => new Set());
  const B = Array.from({ length: 9 }, () => new Set());
  const box = (r, c) => Math.floor(r / 3) * 3 + Math.floor(c / 3);
  const empty = [];

  for (let r = 0; r < 9; r++) {
    for (let c = 0; c < 9; c++) {
      const ch = board[r][c];
      if (ch === '.') {
        empty.push([r, c]);
      } else {
        R[r].add(ch);
        C[c].add(ch);
        B[box(r, c)].add(ch);
      }
    }
  }

  function bt(i) {
    if (i === empty.length) return true;
    const [r, c] = empty[i];
    for (let d = 1; d <= 9; d++) {
      const ch = String(d);
      const b = box(r, c);
      if (R[r].has(ch) || C[c].has(ch) || B[b].has(ch)) continue;
      board[r][c] = ch;
      R[r].add(ch);
      C[c].add(ch);
      B[b].add(ch);
      if (bt(i + 1)) return true;
      board[r][c] = '.';
      R[r].delete(ch);
      C[c].delete(ch);
      B[b].delete(ch);
    }
    return false;
  }
  bt(0);
  return board;
}

// Test Cases:
// Input: board = [
//   ["5","3",".",".","7",".",".",".","."],
//   ["6",".",".","1","9","5",".",".","."],
//   [".","9","8",".",".",".",".","6","."],
//   ["8",".",".",".","6",".",".",".","3"],
//   ["4",".",".","8",".","3",".",".","1"],
//   ["7",".",".",".","2",".",".",".","6"],
//   [".","6",".",".",".",".","2","8","."],
//   [".",".",".","4","1","9",".",".","5"],
//   [".",".",".",".","8",".",".","7","9"]
// ]
// Output: Solved Sudoku board (all cells filled with valid numbers)

// Note: Multiple solutions may exist; backtracking finds one valid solution
```

**Time Complexity:** O(9^m) - Backtracking where m is number of empty cells  
**Space Complexity:** O(1) -Reusing input board, O(81) sets for constraints

Deep Insights:
  - Rule: Backtrack cell by cell; maintain row/col/box availability; O(9^m) time where m is empty cells.
  - Real-world: Sudoku solving, constraint satisfaction, puzzle solving, backtracking algorithms.
  - Common mistake: Backtracks on dead ends; valid puzzle assumed; not maintaining constraints correctly.
  - Optimization: Constraint checking reduces search space; backtracks on dead ends; valid puzzle assumed.
  - Interview tip: Explain constraint checking clearly; mention backtracking; ask about puzzle validity.
## Q143. Permutations / Combinations

Concept: Build paths; for combinations control start index; for permutations use used
  - set or swap.

Example:
```javascript
function permute(nums) {
  const res = [];
  const used = new Array(nums.length).fill(false);
  const cur = [];

  function bt() {
    if (cur.length === nums.length) {
      res.push([...cur]);
      return;
    }
    for (let i = 0; i < nums.length; i++) {
      if (used[i]) continue;
      used[i] = true;
      cur.push(nums[i]);
      bt();
      cur.pop();
      used[i] = false;
    }
  }
  bt();
  return res;
}

function combine(n, k) {
  const res = [];
  const cur = [];

  function bt(s) {
    if (cur.length === k) {
      res.push([...cur]);
      return;
    }
    for (let i = s; i <= n; i++) {
      cur.push(i);
      bt(i + 1);
      cur.pop();
    }
  }
  bt(1);
  return res;
}

// Test Cases:
// permute:
// Input: nums = [1, 2, 3]
// Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

// Input: nums = [0, 1]
// Output: [[0,1],[1,0]]

// Input: nums = [1]
// Output: [[1]]

// combine:
// Input: n = 4, k = 2
// Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

// Input: n = 1, k = 1
// Output: [[1]]

// Input: n = 5, k = 3
// Output: [[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5],[2,4,5],[3,4,5]]
```

**Time Complexity:** O(n!) for permutations, O(C(n,k)) for combinations  
**Space Complexity:** O(n) - Recursion stack plus result storage

Deep Insights:
  - Rule: Build paths; for combinations control start index; for permutations use used-set or swap; O(n!) / O(C(n,k)) time.
  - Real-world: Permutations/combinations generation, arrangement problems, combinatorial generation, backtracking.
  - Common mistake: Iterative variants exist; wrong start index for combinations; not handling duplicates correctly.
  - Optimization: Used-set for permutations; start index for combinations; iterative variants exist.
  - Interview tip: Explain permutations vs combinations clearly; mention iterative variants; ask about duplicates.
## Q144. Subsets / Power Set

Concept: Decide include/exclude per item or iterate size by size.

Example:
```javascript
function subsets(nums) {
  const res = [[]];
  for (const x of nums) {
    const add = res.map(s => [...s, x]);
    res.push(...add);
  }
  return res;
}

// Test Cases:
// Input: nums = [1, 2, 3]
// Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

// Input: nums = [0]
// Output: [[],[0]]

// Input: nums = [1, 2]
// Output: [[],[1],[2],[1,2]]

// Input: nums = []
// Output: [[]]
```

**Time Complexity:** O(2^n) - Generating all 2^n subsets  
**Space Complexity:** O(2^n) -Storage for all subsets

Deep Insights:
  - Rule: Decide include/exclude per item or iterate size by size; O(2^n) time, O(2^n) space.
  - Real-world: Subsets/power set generation, subset problems, combination problems, enumeration.
  - Common mistake: For duplicates, sort and skip same-start; order not important; wrong inclusion logic.
  - Optimization: O(2^n) optimal; for duplicates, sort and skip same-start; order not important.
  - Interview tip: Explain include/exclude clearly; mention duplicate handling; ask about ordered vs unordered.
## Q145. Generate Parentheses

Concept: Backtrack ensuring open used <= n and close <= open.

Example:
```javascript
function generateParenthesis(n) {
  const res = [];

  function bt(o, c, str) {
    if (str.length === 2 * n) {
      res.push(str);
      return;
    }
    if (o < n) {
      bt(o + 1, c, str + '(');
    }
    if (c < o) {
      bt(o, c + 1, str + ')');
    }
  }
  bt(0, 0, '');
  return res;
}

// Test Cases:
// Input: n = 3
// Output: ["((()))","(()())","(())()","()(())","()()()"]

// Input: n = 1
// Output: ["()"]

// Input: n = 2
// Output: ["(())","()()"]

// Input: n = 4
// Output: All valid combinations of 4 pairs of parentheses
```

**Time Complexity:** O(4^n / √n) - Catalan number C(n) ≈ 4^n / (n√(πn))  
**Space Complexity:** O(n) -Recursion stack depth

Deep Insights:
  - Rule: Backtrack ensuring open used <= n and close <= open; O(C(n)) outputs where C(n) is Catalan number.
  - Real-world: Generate parentheses, valid parentheses generation, balanced string generation, Catalan numbers.
  - Common mistake: O(C(n)) outputs; balanced by construction; wrong open/close tracking.
  - Optimization: O(C(n)) outputs optimal; balanced by construction; constraint checking ensures validity.
  - Interview tip: Explain constraint checking clearly; mention Catalan numbers; ask about output format.
## Q146. Word Search

Concept: DFS from each cell matching next character, mark visited and backtrack.

Example:
```javascript
function exist(board, word) {
  const m = board.length;
  const n = board[0].length;
  const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
  const seen = Array.from({ length: m }, () => Array(n).fill(false));

  function dfs(r, c, i) {
    if (i === word.length) return true;
    if (r < 0 || c < 0 || r >= m || c >= n || seen[r][c] || board[r][c] !== word[i]) {
      return false;
    }
    seen[r][c] = true;
    for (const [dr, dc] of dirs) {
      if (dfs(r + dr, c + dc, i + 1)) return true;
    }
    seen[r][c] = false;
    return false;
  }

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (dfs(i, j, 0)) return true;
    }
  }
  return false;
}

// Test Cases:
// Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
// Output: true

// Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
// Output: true

// Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
// Output: false

// Input: board = [["a","b"],["c","d"]], word = "abcd"
// Output: false
```

**Time Complexity:** O(mn × 4^L) -DFS from each cell, 4 directions, L is word length  
**Space Complexity:** O(L) - Recursion stack depth

Deep Insights:
  - Rule: DFS from each cell matching next character, mark visited and backtrack; O(mn × 4^L) time.
  - Real-world: Word search problems, pattern matching in grids, path finding, backtracking algorithms.
  - Common mistake: Prune by first char counts; not marking visited correctly; forgetting to backtrack.
  - Optimization: Prune by first char counts; mark visited during DFS; backtrack to restore state.
  - Interview tip: Explain DFS clearly; mention pruning techniques; ask about optimization strategies.
## Q147. Rat in a Maze

Concept: From start, move in allowed directions marking path; backtrack on walls.

Example:
```javascript
function ratMaze(maze) {
  const m = maze.length;
  const n = maze[0].length;
  const res = [];
  const dirs = [[1, 0, 'D'], [0, 1, 'R'], [-1, 0, 'U'], [0, -1, 'L']];
  const seen = Array.from({ length: m }, () => Array(n).fill(false));

  function bt(r, c, path) {
    if (r === m - 1 && c === n - 1) {
      res.push(path);
      return;
    }
    seen[r][c] = true;
    for (const [dr, dc, ch] of dirs) {
      const nr = r + dr;
      const nc = c + dc;
      if (nr >= 0 && nc >= 0 && nr < m && nc < n && maze[nr][nc] === 1 && !seen[nr][nc]) {
        bt(nr, nc, path + ch);
      }
    }
    seen[r][c] = false;
  }

  if (maze[0][0] === 1) {
    bt(0, 0, '');
  }
  return res;
}

// Test Cases:
// Input: maze = [
//   [1, 0, 0, 0],
//   [1, 1, 0, 1],
//   [0, 1, 0, 0],
//   [1, 1, 1, 1]
// ]
// Output: ["DDRRURRD", "DDRURRRD"] (or similar paths)

// Input: maze = [
//   [1, 1],
//   [1, 1]
// ]
// Output: ["RD", "DR"]

// Input: maze = [
//   [0, 1],
//   [1, 1]
// ]
// Output: [] (no path exists from start)

// Input: maze = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
// Output: Valid paths from (0,0) to (2,2)
```

**Time Complexity:** O(4^(mn)) - Backtracking with 4 directions from each cell  
**Space Complexity:** O(mn) -Visited array plus recursion stack

Deep Insights:
  - Rule: From start, move in allowed directions marking path; backtrack on walls; O(4^(mn)) time worst-case.
  - Real-world: Rat in a maze problems, path finding, maze solving, backtracking algorithms.
  - Common mistake: Multiple paths collected; grid of 0/1; not marking visited correctly; forgetting to backtrack.
  - Optimization: Backtracking explores all paths; multiple paths collected; grid of 0/1 (walls/paths).
  - Interview tip: Explain backtracking clearly; mention path collection; ask about shortest path variant.
## Q148. Combination Sum

Concept: Choose candidate multiple times; backtrack with start index to avoid permutations.

Example:
```javascript
function combinationSum(cands, target) {
  cands.sort((a, b) => a - b);
  const res = [];
  const cur = [];

  function bt(i, sum) {
    if (sum === target) {
      res.push([...cur]);
      return;
    }
    for (let k = i; k < cands.length; k++) {
      const x = cands[k];
      if (sum + x > target) break;
      cur.push(x);
      bt(k, sum + x);
      cur.pop();
    }
  }
  bt(0, 0);
  return res;
}

// Test Cases:
// Input: candidates = [2, 3, 6, 7], target = 7
// Output: [[2,2,3],[7]]

// Input: candidates = [2, 3, 5], target = 8
// Output: [[2,2,2,2],[2,3,3],[3,5]]

// Input: candidates = [2], target = 1
// Output: []

// Input: candidates = [1], target = 1
// Output: [[1]]

// Input: candidates = [1], target = 2
// Output: [[1,1]]
```

**Time Complexity:** O(2^target) - Exponential backtracking  
**Space Complexity:** O(target) -Recursion stack depth

Deep Insights:
  - Rule: Choose candidate multiple times; backtrack with start index to avoid permutations; O(2^target) time.
  - Real-world: Combination sum problems, target sum problems, subset sum variants, backtracking.
  - Common mistake: No duplicates by non-decreasing picks; target sums only; wrong start index handling.
  - Optimization: Start index prevents duplicates; no duplicates by non-decreasing picks; target sums only.
  - Interview tip: Explain start index clearly; mention duplicate avoidance; ask about target constraints.
## Q149. Letter combinations of Phone Number

Concept: Map digits to letters; backtrack by appending choices per digit.

Example:
```javascript
function letterCombinations(d) {
  if (!d) return [];
  const map = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz'
  };
  const res = [];
  const cur = [];

  function bt(i) {
    if (i === d.length) {
      res.push(cur.join(''));
      return;
    }
    for (const ch of map[d[i]]) {
      cur.push(ch);
      bt(i + 1);
      cur.pop();
    }
  }
  bt(0);
  return res;
}

// Test Cases:
// Input: digits = "23"
// Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

// Input: digits = ""
// Output: []

// Input: digits = "2"
// Output: ["a","b","c"]

// Input: digits = "234"
// Output: All combinations of letters for digits 2, 3, 4
```

**Time Complexity:** O(4^n) - Each digit maps to 3
  - 4 letters  
**Space Complexity:** O(n) - Recursion stack depth

Deep Insights:
  - Rule: Map digits to letters; backtrack by appending choices per digit; O(4^n) time where n is digits.
  - Real-world: Phone number letter combinations, digit mapping, string generation, backtracking.
  - Common mistake: Iterative queue variant exists; wrong digit mapping; not handling empty input.
  - Optimization: O(4^n) time for n digits; iterative queue variant exists; backtracking generates all combinations.
  - Interview tip: Explain digit mapping clearly; mention iterative variant; ask about empty input handling.
## Q150. Palindrome Partitioning

Concept: Backtrack split string; add substring if palindrome.

Example:
```javascript
function partition(s) {
  const res = [];
  const cur = [];

  const isPal = (l, r) => {
    while (l < r) {
      if (s[l++] !== s[r--]) return false;
    }
    return true;
  };

  function bt(i) {
    if (i === s.length) {
      res.push([...cur]);
      return;
    }
    for (let j = i; j < s.length; j++) {
      if (isPal(i, j)) {
        cur.push(s.slice(i, j + 1));
        bt(j + 1);
        cur.pop();
      }
    }
  }
  bt(0);
  return res;
}

// Test Cases:
// Input: s = "aab"
// Output: [["a","a","b"],["aa","b"]]

// Input: s = "a"
// Output: [["a"]]

// Input: s = "racecar"
// Output: [["r","a","c","e","c","a","r"],["r","a","ce","c","a","r"],["r","a","c","ec","a","r"],["r","aceca","r"],["racecar"]]

// Input: s = "aba"
// Output: [["a","b","a"],["aba"]]
```

**Time Complexity:** O(n × 2^n) -Backtracking with palindrome checks  
**Space Complexity:** O(n) - Recursion stack depth

Deep Insights:
  - Rule: Backtrack split string; add substring if palindrome; O(n × 2^n) time, O(n) space.
  - Real-world: Palindrome partitioning, string cutting, palindrome problems, backtracking.
  - Common mistake: Useful for cut problems; not checking palindrome correctly; wrong splitting logic.
  - Optimization: O(n × 2^n) time; palindrome checking is O(n); useful for cut problems.
  - Interview tip: Explain palindrome checking clearly; mention cut problems; ask about optimization.