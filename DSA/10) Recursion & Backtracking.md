# Recursion & Backtracking

## Q193. N-Queens

**Problem:** The n-queens puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other. Given an integer `n`, return all distinct solutions to the n-queens puzzle. You may return the answer in any order. Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space, respectively.

**Approach:** Use backtracking. Place queens row by row. For each row, try each column and check if placing a queen there violates constraints (same column, same diagonal). Use sets to track occupied columns and diagonals.

### Solution 1: Backtracking with Sets (Optimal)
```javascript
function solveNQueens(n) {
  const res = [];
  const col = new Set();  // Occupied columns
  const d1 = new Set();   // Diagonal r - c (main diagonal)
  const d2 = new Set();   // Diagonal r + c (anti-diagonal)
  const board = Array.from({ length: n }, () => '.'.repeat(n).split(''));

  function backtrack(row) {
    // Base case: all queens placed
    if (row === n) {
      res.push(board.map(row => row.join('')));
      return;
    }
    
    // Try each column in current row
    for (let colIdx = 0; colIdx < n; colIdx++) {
      // Check if position is valid
      if (col.has(colIdx) || d1.has(row - colIdx) || d2.has(row + colIdx)) {
        continue;
      }
      
      // Place queen
      col.add(colIdx);
      d1.add(row - colIdx);
      d2.add(row + colIdx);
      board[row][colIdx] = 'Q';
      
      // Recurse
      backtrack(row + 1);
      
      // Backtrack
      board[row][colIdx] = '.';
      col.delete(colIdx);
      d1.delete(row - colIdx);
      d2.delete(row + colIdx);
    }
  }
  
  backtrack(0);
  return res;
}
```

// Test Cases:
// Input: n = 4
// Output: [
// [".Q..","...Q","Q...","..Q."],
// ["..Q.","Q...","...Q",".Q.."]
// ]

// Input: n = 1
// Output: [["Q"]]

// Input: n = 3
// Output: [] (no solution exists for n=3)

// Input: n = 2
// Output: [] (no solution exists for n=2)
```

**Time Complexity:** O(n!) - Backtracking generates all valid queen placements  
**Space Complexity:** O(n²) - Board storage plus O(n) recursion stack

## Q194. Sudoku Solver

**Problem:** Write a program to solve a Sudoku puzzle by filling the empty cells. A sudoku solution must satisfy all of the following rules:
1. Each of the digits 1-9 must occur exactly once in each row.
2. Each of the digits 1-9 must occur exactly once in each column.
3. Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

The `'.'` character indicates empty cells.

**Approach:** Use backtracking. Preprocess to collect empty cells and track constraints (row, column, box). For each empty cell, try digits 1-9 that satisfy all constraints.

### Solution 1: Backtracking with Constraint Tracking (Optimal)
```javascript
function solveSudoku(board) {
  const R = Array.from({ length: 9 }, () => new Set());  // Row constraints
  const C = Array.from({ length: 9 }, () => new Set());  // Column constraints
  const B = Array.from({ length: 9 }, () => new Set());  // Box constraints
  const box = (r, c) => Math.floor(r / 3) * 3 + Math.floor(c / 3);
  const empty = [];
  
  // Preprocess: collect empty cells and track constraints
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
  
  function backtrack(idx) {
    // Base case: all empty cells filled
    if (idx === empty.length) return true;
    
    const [r, c] = empty[idx];
    const b = box(r, c);
    
    // Try digits 1-9
    for (let d = 1; d <= 9; d++) {
      const ch = String(d);
      
      // Check constraints
      if (R[r].has(ch) || C[c].has(ch) || B[b].has(ch)) continue;
      
      // Place digit
      board[r][c] = ch;
      R[r].add(ch);
      C[c].add(ch);
      B[b].add(ch);
      
      // Recurse
      if (backtrack(idx + 1)) return true;
      
      // Backtrack
      board[r][c] = '.';
      R[r].delete(ch);
      C[c].delete(ch);
      B[b].delete(ch);
    }
    
    return false;
  }
  
  backtrack(0);
  return board;
}
```

// Test Cases:
// Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
// Output: Solved Sudoku board (all cells filled with valid numbers)
// Explanation: Backtracking fills all empty cells with valid digits

// Input: board = [["1","2","3","4","5","6","7","8","9"],["4","5","6","7","8","9","1","2","3"],["7","8","9","1","2","3","4","5","6"],["2","3","4","5","6","7","8","9","1"],["5","6","7","8","9","1","2","3","4"],["8","9","1","2","3","4","5","6","7"],["3","4","5","6","7","8","9","1","2"],["6","7","8","9","1","2","3","4","5"],["9","1","2","3","4","5","6","7","8"]]
// Output: Solved Sudoku board (already complete)
```

**Time Complexity:** O(9^m) - Backtracking where m is number of empty cells  
**Space Complexity:** O(1) - Reusing input board, O(81) sets for constraints

## Q195. Permutations / Combinations

**Problem:**
1. **Permutations:** Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in any order.
2. **Combinations:** Given two integers `n` and `k`, return all possible combinations of `k` numbers chosen from the range `[1, n]`.

**Approach:** Use backtracking. For permutations: track used elements. For combinations: control start index to avoid duplicates.

### Solution 1: Permutations
```javascript
function permute(nums) {
  const res = [];
  const used = new Array(nums.length).fill(false);
  const cur = [];
  
  function backtrack() {
    // Base case: permutation complete
    if (cur.length === nums.length) {
      res.push([...cur]);
      return;
    }
    
    // Try each unused element
    for (let i = 0; i < nums.length; i++) {
      if (used[i]) continue;
      
      used[i] = true;
      cur.push(nums[i]);
      backtrack();
      cur.pop();
      used[i] = false;
    }
  }
  
  backtrack();
  return res;
}
```

### Solution 2: Combinations
```javascript
function combine(n, k) {
  const res = [];
  const cur = [];
  
  function backtrack(start) {
    // Base case: combination complete
    if (cur.length === k) {
      res.push([...cur]);
      return;
    }
    
    // Try elements from start to n
    for (let i = start; i <= n; i++) {
      cur.push(i);
      backtrack(i + 1);  // Start from next element
      cur.pop();
    }
  }
  
  backtrack(1);
  return res;
}
```

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

## Q196. Subsets / Power Set

**Problem:** Given an integer array `nums` of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets. Return the solution in any order.

**Approach:** Use iterative approach. For each element, add it to all existing subsets to create new subsets. Alternatively, use backtracking with include/exclude decision.

### Solution 1: Iterative (Optimal)
```javascript
function subsets(nums) {
  const res = [[]];
  
  // For each number, add it to all existing subsets
  for (const num of nums) {
    const newSubsets = res.map(subset => [...subset, num]);
    res.push(...newSubsets);
  }
  
  return res;
}
```

### Solution 2: Backtracking
```javascript
function subsets(nums) {
  const res = [];
  const cur = [];
  
  function backtrack(start) {
    // Add current subset
    res.push([...cur]);
    
    // Try including each remaining element
    for (let i = start; i < nums.length; i++) {
      cur.push(nums[i]);
      backtrack(i + 1);
      cur.pop();
    }
  }
  
  backtrack(0);
  return res;
}
```

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
**Space Complexity:** O(2^n) - Storage for all subsets

## Q197. Generate Parentheses

**Problem:** Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

**Approach:** Use backtracking. Track open and close counts. Add '(' if open < n, add ')' if close < open. This ensures valid parentheses by construction.

### Solution 1: Backtracking (Optimal)
```javascript
function generateParenthesis(n) {
  const res = [];
  
  function backtrack(open, close, str) {
    // Base case: string complete
    if (str.length === 2 * n) {
      res.push(str);
      return;
    }
    
    // Add '(' if we haven't used all open parentheses
    if (open < n) {
      backtrack(open + 1, close, str + '(');
    }
    
    // Add ')' if we have more open than close (valid)
    if (close < open) {
      backtrack(open, close + 1, str + ')');
    }
  }
  
  backtrack(0, 0, '');
  return res;
}
```

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
**Space Complexity:** O(n) - Recursion stack depth

## Q198. Word Search

**Problem:** Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid. The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

**Approach:** Use DFS with backtracking. Start from each cell, match characters sequentially in 4 directions. Mark visited cells and backtrack when path fails.

### Solution 1: DFS with Backtracking (Optimal)
```javascript
function exist(board, word) {
  const m = board.length;
  const n = board[0].length;
  const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
  const seen = Array.from({ length: m }, () => Array(n).fill(false));
  
  function dfs(row, col, idx) {
    // Base case: word found
    if (idx === word.length) return true;
    
    // Boundary and validity checks
    if (row < 0 || col < 0 || row >= m || col >= n || 
        seen[row][col] || board[row][col] !== word[idx]) {
      return false;
    }
    
    // Mark as visited
    seen[row][col] = true;
    
    // Explore 4 directions
    for (const [dr, dc] of dirs) {
      if (dfs(row + dr, col + dc, idx + 1)) {
        return true;
      }
    }
    
    // Backtrack
    seen[row][col] = false;
    return false;
  }
  
  // Try starting from each cell
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (dfs(i, j, 0)) return true;
    }
  }
  
  return false;
}
```

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

**Time Complexity:** O(mn × 4^L) - DFS from each cell, 4 directions, L is word length  
**Space Complexity:** O(L) - Recursion stack depth

## Q199. Rat in a Maze

**Problem:** Consider a rat placed at `(0, 0)` in a square maze of order `N * N`. The maze is represented as a 2D array where `1` represents a valid path and `0` represents a wall. The rat needs to reach the destination at `(N-1, N-1)`. Find all paths that the rat can take to reach the destination. The directions allowed are Up (U), Down (D), Left (L), Right (R).

**Approach:** Use backtracking. Start from (0,0), explore all 4 directions. Mark visited cells and backtrack when path fails or reaches destination.

### Solution 1: Backtracking (Optimal)
```javascript
function ratMaze(maze) {
  const m = maze.length;
  const n = maze[0].length;
  const res = [];
  const dirs = [[1, 0, 'D'], [0, 1, 'R'], [-1, 0, 'U'], [0, -1, 'L']];
  const seen = Array.from({ length: m }, () => Array(n).fill(false));
  
  function backtrack(row, col, path) {
    // Base case: reached destination
    if (row === m - 1 && col === n - 1) {
      res.push(path);
      return;
    }
    
    // Mark as visited
    seen[row][col] = true;
    
    // Explore 4 directions
    for (const [dr, dc, dir] of dirs) {
      const nr = row + dr;
      const nc = col + dc;
      
      // Check validity
      if (nr >= 0 && nc >= 0 && nr < m && nc < n && 
          maze[nr][nc] === 1 && !seen[nr][nc]) {
        backtrack(nr, nc, path + dir);
      }
    }
    
    // Backtrack
    seen[row][col] = false;
  }
  
  // Start from (0,0) if valid
  if (maze[0][0] === 1) {
    backtrack(0, 0, '');
  }
  
  return res;
}
```

// Test Cases:
// Input: maze = [[1, 0, 0, 0],[1, 1, 0, 1],[0, 1, 0, 0],[1, 1, 1, 1]]
// Output: ["DDRRURRD", "DDRURRRD"] (or similar paths)
// Explanation: Rat finds all paths from (0,0) to (3,3)

// Input: maze = [[1, 1],[1, 1]]
// Output: ["RD", "DR"]
// Explanation: Two valid paths from (0,0) to (1,1)

// Input: maze = [[0, 1],[1, 1]]
// Output: []
// Explanation: No path exists from start (start cell is blocked)

// Input: maze = [[1, 1, 1],[1, 0, 1],[1, 1, 1]]
// Output: Valid paths from (0,0) to (2,2)
```

**Time Complexity:** O(4^(mn)) - Backtracking with 4 directions from each cell  
**Space Complexity:** O(mn) - Visited array plus recursion stack

## Q200. Combination Sum

**Problem:** Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. You may return the combinations in any order. The same number may be chosen from `candidates` an unlimited number of times.

**Approach:** Use backtracking. Sort candidates first. Use start index to avoid duplicates. Allow reusing same candidate (start from `k`, not `k+1`).

### Solution 1: Backtracking (Optimal)
```javascript
function combinationSum(candidates, target) {
  candidates.sort((a, b) => a - b);
  const res = [];
  const cur = [];
  
  function backtrack(start, sum) {
    // Base case: target reached
    if (sum === target) {
      res.push([...cur]);
      return;
    }
    
    // Try each candidate from start
    for (let i = start; i < candidates.length; i++) {
      const num = candidates[i];
      
      // Pruning: if sum exceeds target, no need to continue (sorted)
      if (sum + num > target) break;
      
      // Choose candidate
      cur.push(num);
      // Recurse with same start (allows reuse)
      backtrack(i, sum + num);
      // Backtrack
      cur.pop();
    }
  }
  
  backtrack(0, 0);
  return res;
}
```

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
**Space Complexity:** O(target) - Recursion stack depth

## Q201. Letter Combinations of a Phone Number

**Problem:** Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in any order. A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

**Approach:** Use backtracking. Map each digit to its letters. For each digit, try all possible letters and recurse.

### Solution 1: Backtracking (Optimal)
```javascript
function letterCombinations(digits) {
  if (!digits || digits.length === 0) return [];
  
  const map = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
  };
  
  const res = [];
  const cur = [];
  
  function backtrack(idx) {
    // Base case: all digits processed
    if (idx === digits.length) {
      res.push(cur.join(''));
      return;
    }
    
    // Try each letter for current digit
    const letters = map[digits[idx]];
    for (const ch of letters) {
      cur.push(ch);
      backtrack(idx + 1);
      cur.pop();
    }
  }
  
  backtrack(0);
  return res;
}
```

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

**Time Complexity:** O(4^n) - Each digit maps to 3-4 letters  
**Space Complexity:** O(n) - Recursion stack depth

## Q202. Palindrome Partitioning

**Problem:** Given a string `s`, partition `s` such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of `s`.

**Approach:** Use backtracking. For each position, try all possible substrings ending at that position. If substring is palindrome, add it and recurse.

### Solution 1: Backtracking (Optimal)
```javascript
function partition(s) {
  const res = [];
  const cur = [];
  
  // Check if substring is palindrome
  function isPalindrome(left, right) {
    while (left < right) {
      if (s[left] !== s[right]) return false;
      left++;
      right--;
    }
    return true;
  }
  
  function backtrack(start) {
    // Base case: entire string processed
    if (start === s.length) {
      res.push([...cur]);
      return;
    }
    
    // Try all possible substrings starting at 'start'
    for (let end = start; end < s.length; end++) {
      // If substring is palindrome, add it
      if (isPalindrome(start, end)) {
        cur.push(s.slice(start, end + 1));
        backtrack(end + 1);
        cur.pop();
      }
    }
  }
  
  backtrack(0);
  return res;
}
```

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

**Time Complexity:** O(n × 2^n) - Backtracking with palindrome checks  
**Space Complexity:** O(n) - Recursion stack depth

- **Interview Tip:** Explain palindrome checking clearly; mention DP optimization; compare with cut problems