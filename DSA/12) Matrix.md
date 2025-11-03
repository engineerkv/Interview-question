# Matrix

## Q151. Valid Sudoku

Concept: Check if 9x9 board follows Sudoku rules: no duplicates in rows, columns, or 3x3 boxes.

```javascript
function isValidSudoku(board) {
  const rows = Array.from({ length: 9 }, () => new Set());
  const cols = Array.from({ length: 9 }, () => new Set());
  const boxes = Array.from({ length: 9 }, () => new Set());

  for (let i = 0; i < 9; i++) {
    for (let j = 0; j < 9; j++) {
      const val = board[i][j];
      if (val === '.') continue;

      const boxIndex = Math.floor(i / 3) * 3 + Math.floor(j / 3);

      if (rows[i].has(val) || cols[j].has(val) || boxes[boxIndex].has(val)) {
        return false;
      }

      rows[i].add(val);
      cols[j].add(val);
      boxes[boxIndex].add(val);
    }
  }
  return true;
}

// Test Cases:
//
// Example 1:
//   Input: board = [["5","3",".",".","7",".",".",".","."],
//                   ["6",".",".","1","9","5",".",".","."],
//                   [".","9","8",".",".",".",".","6","."],
//                   ["8",".",".",".","6",".",".",".","3"],
//                   ["4",".",".","8",".","3",".",".","1"],
//                   ["7",".",".",".","2",".",".",".","6"],
//                   [".","6",".",".",".",".","2","8","."],
//                   [".",".",".","4","1","9",".",".","5"],
//                   [".",".",".",".","8",".",".","7","9"]]
//   Output: true
//
// Example 2:
//   Input: board = [["8","3",".",".","7",".",".",".","."],
//                   ["6",".",".","1","9","5",".",".","."],
//                   [".","9","8",".",".",".",".","6","."],
//                   ["8",".",".",".","6",".",".",".","3"],
//                   ["4",".",".","8",".","3",".",".","1"],
//                   ["7",".",".",".","2",".",".",".","6"],
//                   [".","6",".",".",".",".","2","8","."],
//                   [".",".",".","4","1","9",".",".","5"],
//                   [".",".",".",".","8",".",".","7","9"]]
//   Output: false
//   Explanation: Duplicate 8 in first row and first 3x3 box
```

Deep Insights:
  - Rule: Track seen values in rows, columns, and boxes; O(1) per cell check; O(n²) time.
  - Real-world: Sudoku validation, game validation, constraint checking, grid problems.
  - Common mistake: Box index calculation; forgetting empty cells; wrong validation logic.
  - Optimization: O(1) per cell with sets; box index = Math.floor(i/3)*3 + Math.floor(j/3); handle empty cells.
  - Interview tip: Explain box index calculation clearly; mention three sets per constraint; ask about empty cells.

Time Complexity: O(1) - Fixed 9x9 grid, 81 cells
Space Complexity: O(1) - Fixed size sets for rows, cols, boxes

## Q152. Spiral Matrix

Concept: Traverse matrix in spiral order: right → down → left → up, adjust boundaries after each direction.

```javascript
function spiralOrder(matrix) {
  if (!matrix.length) return [];
  
  const result = [];
  let top = 0, bottom = matrix.length - 1;
  let left = 0, right = matrix[0].length - 1;

  while (top <= bottom && left <= right) {
    // Right
    for (let i = left; i <= right; i++) {
      result.push(matrix[top][i]);
    }
    top++;

    // Down
    for (let i = top; i <= bottom; i++) {
      result.push(matrix[i][right]);
    }
    right--;

    // Left (if still valid)
    if (top <= bottom) {
      for (let i = right; i >= left; i--) {
        result.push(matrix[bottom][i]);
      }
      bottom--;
    }

    // Up (if still valid)
    if (left <= right) {
      for (let i = bottom; i >= top; i--) {
        result.push(matrix[i][left]);
      }
      left++;
    }
  }

  return result;
}

// Test Cases:
//
// Example 1:
//   Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
//   Output: [1,2,3,6,9,8,7,4,5]
//
// Example 2:
//   Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
//   Output: [1,2,3,4,8,12,11,10,9,5,6,7]
//
// Example 3:
//   Input: matrix = [[1]]
//   Output: [1]
```

Deep Insights:
  - Rule: Traverse right → down → left → up; adjust boundaries after each direction; O(mn) time.
  - Real-world: Matrix traversal, spiral patterns, printing matrices, grid problems.
  - Common mistake: Boundary checks after each direction; not checking if row/col exists before traversing.
  - Optimization: O(mn) time optimal; boundary adjustments crucial; check bounds before left/up traversals.
  - Interview tip: Explain boundary management clearly; mention four directions; ask about edge cases.

Time Complexity: O(mn) - Visit each cell once
Space Complexity: O(1) - Excluding output array

## Q153. Rotate Image

Concept: Rotate matrix 90° clockwise: transpose then reverse each row (or reverse each column then transpose).

```javascript
function rotate(matrix) {
  const n = matrix.length;
  
  // Transpose
  for (let i = 0; i < n; i++) {
    for (let j = i; j < n; j++) {
      [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];
    }
  }
  
  // Reverse each row
  for (let i = 0; i < n; i++) {
    matrix[i].reverse();
  }
}

// Test Cases:
//
// Example 1:
//   Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
//   Output: [[7,4,1],[8,5,2],[9,6,3]]
//
// Example 2:
//   Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
//   Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```

Deep Insights:
  - Rule: Transpose then reverse rows; or reverse columns then transpose; O(n²) time.
  - Real-world: Image rotation, matrix transformations, 2D array manipulation.
  - Common mistake: Wrong transpose loop bounds (j starts at i); forgetting to reverse rows.
  - Optimization: O(n²) time optimal; in-place modification; transpose loop: j starts at i.
  - Interview tip: Explain transpose clearly; mention two-step process; ask about in-place requirement.

Time Complexity: O(n²) - Transpose and reverse each row
Space Complexity: O(1) - In-place modification

## Q154. Set Matrix Zeroes

Concept: Mark rows/cols to zero out; use first row/col as markers, handle (0,0) separately.

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

  // Mark zeros in first row/col
  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      if (matrix[i][j] === 0) {
        matrix[i][0] = 0;
        matrix[0][j] = 0;
      }
    }
  }

  // Set zeros based on markers
  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      if (matrix[i][0] === 0 || matrix[0][j] === 0) {
        matrix[i][j] = 0;
      }
    }
  }

  // Set first row
  if (firstRowZero) {
    for (let j = 0; j < n; j++) {
      matrix[0][j] = 0;
    }
  }

  // Set first col
  if (firstColZero) {
    for (let i = 0; i < m; i++) {
      matrix[i][0] = 0;
    }
  }
}

// Test Cases:
//
// Example 1:
//   Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
//   Output: [[1,0,1],[0,0,0],[1,0,1]]
//
// Example 2:
//   Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
//   Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

Deep Insights:
  - Rule: Use first row/col as markers; handle (0,0) separately; O(mn) time, O(1) space.
  - Real-world: Matrix manipulation, zero propagation, in-place algorithms.
  - Common mistake: Overwriting markers before using them; not handling first row/col separately.
  - Optimization: O(mn) time, O(1) space optimal; first row/col as markers; handle (0,0) separately.
  - Interview tip: Explain marker strategy clearly; mention separate handling for first row/col; ask about space constraint.

Time Complexity: O(mn) - Three passes through matrix
Space Complexity: O(1) - Using first row/col as markers

## Q155. Game of Life

Concept: Apply Conway's rules with state encoding: 0→0=0, 0→1=2, 1→0=3, 1→1=1; decode after processing.

```javascript
function gameOfLife(board) {
  const m = board.length;
  const n = board[0].length;

  const directions = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]];

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      let liveNeighbors = 0;

      for (const [di, dj] of directions) {
        const ni = i + di, nj = j + dj;
        if (ni >= 0 && ni < m && nj >= 0 && nj < n) {
          if (board[ni][nj] === 1 || board[ni][nj] === 3) {
            liveNeighbors++;
          }
        }
      }

      if (board[i][j] === 1) {
        if (liveNeighbors < 2 || liveNeighbors > 3) {
          board[i][j] = 3; // 1 → 0 (currently alive, will die)
        }
      } else {
        if (liveNeighbors === 3) {
          board[i][j] = 2; // 0 → 1 (currently dead, will live)
        }
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

// Test Cases:
//
// Example 1:
//   Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
//   Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
//
// Example 2:
//   Input: board = [[1,1],[1,0]]
//   Output: [[1,1],[1,1]]
```

Deep Insights:
  - Rule: Encode state transitions: 0→0=0, 0→1=2, 1→0=3, 1→1=1; decode after; O(mn) time.
  - Real-world: Cellular automata, Conway's Game of Life, simulation problems, state transitions.
  - Common mistake: Simultaneous updates require encoding; not decoding final states; wrong neighbor counting.
  - Optimization: O(mn) time, O(1) space; state encoding allows in-place; count neighbors from 8 directions.
  - Interview tip: Explain state encoding clearly; mention simultaneous update constraint; ask about boundary handling.

Time Complexity: O(mn) - Visit each cell and check 8 neighbors
Space Complexity: O(1) - In-place state encoding

