# 🧩 DSA Interview Notes - LeetCode Top 150

## 🧭 Section 9 — Backtracking — Q89-Q96

---

### 89. 🧭 Letter Combinations of a Phone Number

**🧠 Concept**

Generate all possible letter combinations from phone number using backtracking with DFS exploration.

**💻 Example**

```javascript
function letterCombinations(digits) {
  if (!digits) return [];
  
  const map = {
    '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
    '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
  };
  
  const result = [];
  
  function backtrack(index, current) {
    if (index === digits.length) {
      result.push(current);
      return;
    }
    
    const letters = map[digits[index]];
    for (const letter of letters) {
      backtrack(index + 1, current + letter);
    }
  }
  
  backtrack(0, '');
  return result;
}
```

**💬 Explanation + Insight**

- **DFS Backtracking** - Explore all possible combinations
- **Base Case** - When index equals digits length
- **Character Mapping** - Map digits to corresponding letters
- **Time Complexity** - O(4^n) where n is digits length
- **Space Complexity** - O(n) recursion stack

---

### 90. 🧭 Generate Parentheses

**🧠 Concept**

Generate all valid parentheses combinations using backtracking with open/close count tracking.

**💻 Example**

```javascript
function generateParenthesis(n) {
  const result = [];
  
  function backtrack(current, open, close) {
    if (current.length === 2 * n) {
      result.push(current);
      return;
    }
    
    if (open < n) {
      backtrack(current + '(', open + 1, close);
    }
    if (close < open) {
      backtrack(current + ')', open, close + 1);
    }
  }
  
  backtrack('', 0, 0);
  return result;
}
```

**💬 Explanation + Insight**

- **Valid Parentheses** - Ensure close count never exceeds open count
- **Count Tracking** - Track open and close parentheses
- **Constraint Satisfaction** - Only add ')' when close < open
- **Time Complexity** - O(4^n/√n) Catalan number
- **Space Complexity** - O(n) recursion stack

---

### 91. 🧭 Combination Sum

**🧠 Concept**

Find all unique combinations that sum to target using backtracking with duplicate handling.

**💻 Example**

```javascript
function combinationSum(candidates, target) {
  const result = [];
  candidates.sort((a, b) => a - b);
  
  function backtrack(start, current, remaining) {
    if (remaining === 0) {
      result.push([...current]);
      return;
    }
    
    for (let i = start; i < candidates.length; i++) {
      if (candidates[i] > remaining) break;
      if (i > start && candidates[i] === candidates[i-1]) continue;
      
      current.push(candidates[i]);
      backtrack(i, current, remaining - candidates[i]);
      current.pop();
    }
  }
  
  backtrack(0, [], target);
  return result;
}
```

**💬 Explanation + Insight**

- **Duplicate Handling** - Skip duplicates in sorted array
- **Reuse Elements** - Allow same element multiple times
- **Pruning** - Stop when candidate > remaining
- **Time Complexity** - O(2^target) exponential
- **Space Complexity** - O(target) recursion stack

---

### 92. 🧭 Combinations

**🧠 Concept**

Generate all combinations of k elements from range [1,n] using backtracking with index tracking.

**💻 Example**

```javascript
function combine(n, k) {
  const result = [];
  
  function backtrack(start, current) {
    if (current.length === k) {
      result.push([...current]);
      return;
    }
    
    for (let i = start; i <= n; i++) {
      current.push(i);
      backtrack(i + 1, current);
      current.pop();
    }
  }
  
  backtrack(1, []);
  return result;
}
```

**💬 Explanation + Insight**

- **Index Tracking** - Start from current index to avoid duplicates
- **Size Constraint** - Stop when combination size equals k
- **Backtracking** - Remove element after exploring
- **Time Complexity** - O(C(n,k)) combinations
- **Space Complexity** - O(k) recursion stack

---

### 93. 🧭 Permutations

**🧠 Concept**

Generate all permutations of array using backtracking with visited array to track used elements.

**💻 Example**

```javascript
function permute(nums) {
  const result = [];
  const visited = Array(nums.length).fill(false);
  
  function backtrack(current) {
    if (current.length === nums.length) {
      result.push([...current]);
      return;
    }
    
    for (let i = 0; i < nums.length; i++) {
      if (visited[i]) continue;
      
      visited[i] = true;
      current.push(nums[i]);
      backtrack(current);
      current.pop();
      visited[i] = false;
    }
  }
  
  backtrack([]);
  return result;
}
```

**💬 Explanation + Insight**

- **Visited Tracking** - Prevent using same element twice
- **Complete Permutation** - Stop when all elements used
- **State Restoration** - Reset visited and current after backtrack
- **Time Complexity** - O(n!) factorial time
- **Space Complexity** - O(n) for visited array

---

### 94. 🧭 Word Search

**🧠 Concept**

Find if word exists in 2D board using DFS backtracking with visited tracking and direction exploration.

**💻 Example**

```javascript
function exist(board, word) {
  const m = board.length;
  const n = board[0].length;
  
  function dfs(row, col, index) {
    if (index === word.length) return true;
    if (row < 0 || row >= m || col < 0 || col >= n) return false;
    if (board[row][col] !== word[index]) return false;
    
    const temp = board[row][col];
    board[row][col] = '#';
    
    const found = dfs(row+1, col, index+1) || dfs(row-1, col, index+1) ||
                  dfs(row, col+1, index+1) || dfs(row, col-1, index+1);
    
    board[row][col] = temp;
    return found;
  }
  
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (dfs(i, j, 0)) return true;
    }
  }
  return false;
}
```

**💬 Explanation + Insight**

- **DFS Exploration** - Explore all four directions
- **Visited Marking** - Mark cell as visited during exploration
- **State Restoration** - Restore cell value after backtrack
- **Time Complexity** - O(m*n*4^L) where L is word length
- **Space Complexity** - O(L) recursion stack

---

### 95. 🧭 Word Search II

**🧠 Concept**

Find all words from dictionary in 2D board using Trie and DFS backtracking for optimization.

**💻 Example**

```javascript
function findWords(board, words) {
  const trie = new Trie();
  for (const word of words) {
    trie.insert(word);
  }
  
  const result = new Set();
  const m = board.length;
  const n = board[0].length;
  
  function dfs(row, col, node, path) {
    if (row < 0 || row >= m || col < 0 || col >= n) return;
    if (board[row][col] === '#') return;
    
    const char = board[row][col];
    if (!node.children[char]) return;
    
    const nextNode = node.children[char];
    const newPath = path + char;
    
    if (nextNode.isEnd) {
      result.add(newPath);
    }
    
    board[row][col] = '#';
    dfs(row+1, col, nextNode, newPath);
    dfs(row-1, col, nextNode, newPath);
    dfs(row, col+1, nextNode, newPath);
    dfs(row, col-1, nextNode, newPath);
    board[row][col] = char;
  }
  
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      dfs(i, j, trie.root, '');
    }
  }
  
  return Array.from(result);
}
```

**💬 Explanation + Insight**

- **Trie Optimization** - Use Trie for efficient word lookup
- **Multiple Words** - Find all words simultaneously
- **Early Termination** - Stop when no matching prefix
- **Time Complexity** - O(m*n*4^L) where L is max word length
- **Space Complexity** - O(W*L) for Trie where W is word count

---

### 96. 🧭 N-Queens II

**🧠 Concept**

Count number of solutions for N-Queens problem using backtracking with row, column, and diagonal tracking.

**💻 Example**

```javascript
function totalNQueens(n) {
  let count = 0;
  const cols = new Set();
  const diag1 = new Set();
  const diag2 = new Set();
  
  function backtrack(row) {
    if (row === n) {
      count++;
      return;
    }
    
    for (let col = 0; col < n; col++) {
      if (cols.has(col) || diag1.has(row - col) || diag2.has(row + col)) {
        continue;
      }
      
      cols.add(col);
      diag1.add(row - col);
      diag2.add(row + col);
      
      backtrack(row + 1);
      
      cols.delete(col);
      diag1.delete(row - col);
      diag2.delete(row + col);
    }
  }
  
  backtrack(0);
  return count;
}
```

**💬 Explanation + Insight**

- **Constraint Satisfaction** - Check row, column, and diagonal conflicts
- **Diagonal Tracking** - Use row±col for diagonal identification
- **State Management** - Add/remove constraints during backtrack
- **Time Complexity** - O(N!) factorial time
- **Space Complexity** - O(N) for constraint sets

---

*This comprehensive backtracking section covers essential recursive exploration techniques including constraint satisfaction, state management, and optimization strategies for complex search problems.*