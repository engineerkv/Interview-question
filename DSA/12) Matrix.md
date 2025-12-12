# Matrix

---

## 📍 Navigation

<div align="center">

[← Previous: Recursion & Backtracking](10%29%20Recursion%20%26%20Backtracking.md) • [Home: README](README.md) • [Next: Trie →](13%29%20Trie.md)

[📋 Cheatsheet](DSA%20Interview%20Cheatsheet.md)

</div>

---

## Q203. ✅ Valid Sudoku

**Problem:** Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

1. Each row must contain the digits `1-9` without repetition.

2. Each column must contain the digits `1-9` without repetition.

3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.

**Approach:** Use sets to track seen values in rows, columns, and boxes. For each cell, check if value already exists in corresponding row, column, or box.

### Solution 1: Set-Based Validation (Optimal)

```javascript
function isValidSudoku(board) {
  const rows = Array.from({ length: 9 }, () => new Set());
  const cols = Array.from({ length: 9 }, () => new Set());
  const boxes = Array.from({ length: 9 }, () => new Set());

  for (let i = 0; i < 9; i++) {
    for (let j = 0; j < 9; j++) {
      const val = board[i][j];
      if (val === '.') continue;

      // Calculate box index
      const boxIndex = Math.floor(i / 3) * 3 + Math.floor(j / 3);

      // Check if value already exists
      if (rows[i].has(val) || cols[j].has(val) || boxes[boxIndex].has(val)) {
        return false;
      }

      // Add to sets
      rows[i].add(val);
      cols[j].add(val);
      boxes[boxIndex].add(val);
    }
  }

  return true;
}

```

// Test Cases:
// Input: board = ["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]
// Output: true

// Input: board = ["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]
// Output: false
// Explanation: Duplicate 8 in first row and first 3x3 box

```

**Time Complexity:** O(1) - Fixed 9×9 grid, 81 cells
**Space Complexity:** O(1) - Fixed size sets for rows, cols, boxes

## Q204. 📐 Spiral Matrix

**Problem:** Given an `m x n` matrix, return all elements of the matrix in spiral order.

**Approach:** Use boundary tracking. Traverse right → down → left → up, adjusting boundaries after each direction. Check boundaries before left and up traversals.

### Solution 1: Boundary Tracking (Optimal)

```javascript

function spiralOrder(matrix) {
  if (!matrix.length || !matrix[0].length) return [];

  const result = [];
  let top = 0, bottom = matrix.length - 1;
  let left = 0, right = matrix[0].length - 1;

  while (top <= bottom && left <= right) {
    // Traverse right
    for (let i = left; i <= right; i++) {
      result.push(matrix[top][i]);
    }
    top++;

    // Traverse down
    for (let i = top; i <= bottom; i++) {
      result.push(matrix[i][right]);
    }
    right--;

    // Traverse left (if still valid)
    if (top <= bottom) {
      for (let i = right; i >= left; i--) {
        result.push(matrix[bottom][i]);
      }
      bottom--;
    }

    // Traverse up (if still valid)
    if (left <= right) {
      for (let i = bottom; i >= top; i--) {
        result.push(matrix[i][left]);
      }
      left++;
    }
  }

  return result;
}

```

// Test Cases:
// Input: matrix = [1,2,3],[4,5,6],[7,8,9]
// Output: [1,2,3,6,9,8,7,4,5]

// Input: matrix = [1,2,3,4],[5,6,7,8],[9,10,11,12]
// Output: [1,2,3,4,8,12,11,10,9,5,6,7]

// Input: matrix = [1]
// Output: [1]

```

**Time Complexity:** O(m × n) - Visit each cell once
**Space Complexity:** O(1) - Excluding output array

## Q205. 💡 Rotate Image

**Problem:** You are given an `n x n` 2D matrix representing an image, rotate the image by 90 degrees (clockwise). You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

**Approach:** Two-step process: transpose the matrix, then reverse each row. This achieves 90° clockwise rotation.

### Solution 1: Transpose + Reverse (Optimal)

```javascript
function rotate(matrix) {
  const n = matrix.length;

  // Step 1: Transpose (swap matrix[i][j] with matrix[j][i])
  for (let i = 0; i < n; i++) {
    for (let j = i; j < n; j++) {
      [matrix[i][j], matrix[j][i] = [matrix[j][i], matrix[i][j];
    }
  }

  // Step 2: Reverse each row
  for (let i = 0; i < n; i++) {
    matrix[i].reverse();
  }
}

```

// Test Cases:
// Input: matrix = [1,2,3],[4,5,6],[7,8,9]
// Output: [7,4,1],[8,5,2],[9,6,3]

// Input: matrix = [5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]
// Output: [15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]

```

**Time Complexity:** O(n²) - Transpose and reverse each row
**Space Complexity:** O(1) - In-place modification

## Q206. 📐 Set Matrix Zeroes

**Problem:** Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`'s. You must do it in place.

**Approach:** Use first row and first column as markers. Handle (0,0) separately to avoid overwriting markers. Mark zeros first, then set zeros based on markers.

### Solution 1: Marker-Based (Space Optimized) (Optimal)

```javascript

function setZeroes(matrix) {
  const m = matrix.length;
  const n = matrix[0].length;
  let firstRowZero = false;
  let firstColZero = false;

  // Check if first row has zero
  for (let j = 0; j < n; j++) {
    if (matrix[0][j] === 0) {
      firstRowZero = true;
      break;
    }
  }

  // Check if first col has zero
  for (let i = 0; i < m; i++) {
    if (matrix[i][0] === 0) {
      firstColZero = true;
      break;
    }
  }

  // Mark zeros in first row/col (skip first row/col)
  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      if (matrix[i][j] === 0) {
        matrix[i][0] = 0;  // Mark row
        matrix[0][j] = 0;  // Mark column
      }
    }
  }

  // Set zeros based on markers (skip first row/col)
  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      if (matrix[i][0] === 0 || matrix[0][j] === 0) {
        matrix[i][j] = 0;
      }
    }
  }

  // Set first row if needed
  if (firstRowZero) {
    for (let j = 0; j < n; j++) {
      matrix[0][j] = 0;
    }
  }

  // Set first col if needed
  if (firstColZero) {
    for (let i = 0; i < m; i++) {
      matrix[i][0] = 0;
    }
  }
}

```

// Test Cases:
// Input: matrix = [1,1,1],[1,0,1],[1,1,1]
// Output: [1,0,1],[0,0,0],[1,0,1]

// Input: matrix = [0,1,2,0],[3,4,5,2],[1,3,1,5]
// Output: [0,0,0,0],[0,4,5,0],[0,3,1,0]

```

**Time Complexity:** O(m × n) - Three passes through matrix
**Space Complexity:** O(1) - Using first row/col as markers

## Q207. 💡 Game of Life

**Problem:** According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970." The board is made up of an `m x n` grid of cells, where each cell has an initial state: live (represented by a `1`) or dead (represented by a `0`). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules:

1. Any live cell with fewer than two live neighbors dies (underpopulation).

2. Any live cell with two or three live neighbors lives on (survival).

3. Any live cell with more than three live neighbors dies (overpopulation).

4. Any dead cell with exactly three live neighbors becomes a live cell (reproduction).

The next state is created by applying the above rules simultaneously to every cell in the current state. You must solve it in-place.

**Approach:** Use state encoding to handle simultaneous updates. Encode: 0→0=0, 0→1=2, 1→0=3, 1→1=1. After processing, decode: 2→1, 3→0.

### Solution 1: State Encoding (Optimal)

```javascript
function gameOfLife(board) {
  const m = board.length;
  const n = board[0].length;
  const directions = [-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1];

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      let liveNeighbors = 0;

      // Count live neighbors (check for 1 or 3 - currently alive)
      for (const [di, dj] of directions) {
        const ni = i + di, nj = j + dj;
        if (ni >= 0 && ni < m && nj >= 0 && nj < n) {
          if (board[ni][nj] === 1 || board[ni][nj] === 3) {
            liveNeighbors++;
          }
        }
      }

      // Apply rules with state encoding
      if (board[i][j] === 1) {
        // Currently alive
        if (liveNeighbors < 2 || liveNeighbors > 3) {
          board[i][j] = 3; // 1 → 0 (will die)
        }
        // else stays 1 (1 → 1)
      } else {
        // Currently dead
        if (liveNeighbors === 3) {
          board[i][j] = 2; // 0 → 1 (will live)
        }
        // else stays 0 (0 → 0)
      }
    }
  }

  // Decode: 2 → 1, 3 → 0
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (board[i][j] === 2) board[i][j] = 1;
      else if (board[i][j] === 3) board[i][j] = 0;
    }
  }
}

```

// Test Cases:
// Input: board = [0,1,0],[0,0,1],[1,1,1],[0,0,0]
// Output: [0,0,0],[1,0,1],[0,1,1],[0,1,0]

// Input: board = [1,1],[1,0]
// Output: [1,1],[1,1]

```

**Time Complexity:** O(m × n) - Visit each cell and check 8 neighbors
**Space Complexity:** O(1) - In-place state encoding

---

## 📍 Navigation

<div align="center">

[← Previous: Recursion & Backtracking](10%29%20Recursion%20%26%20Backtracking.md) • [Home: README](README.md) • [Next: Trie →](13%29%20Trie.md)

[📋 Cheatsheet](DSA%20Interview%20Cheatsheet.md)

</div>
