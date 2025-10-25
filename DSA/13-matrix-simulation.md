# 🧩 DSA Interview Notes - LeetCode Top 150

## ⚙️ Section 13 — Matrix / Simulation — Q130-Q134

---

### 130. ⚙️ Valid Sudoku

**🧠 Concept**

Validate Sudoku board by checking rows, columns, and 3x3 boxes for duplicate numbers.

**💻 Example**

```javascript
function isValidSudoku(board) {
  const rows = Array(9).fill().map(() => new Set());
  const cols = Array(9).fill().map(() => new Set());
  const boxes = Array(9).fill().map(() => new Set());
  
  for (let i = 0; i < 9; i++) {
    for (let j = 0; j < 9; j++) {
      const cell = board[i][j];
      if (cell === '.') continue;
      
      const boxIndex = Math.floor(i / 3) * 3 + Math.floor(j / 3);
      
      if (rows[i].has(cell) || cols[j].has(cell) || boxes[boxIndex].has(cell)) {
        return false;
      }
      
      rows[i].add(cell);
      cols[j].add(cell);
      boxes[boxIndex].add(cell);
    }
  }
  
  return true;
}
```

**💬 Explanation + Insight**

- **Three Constraints** - Check rows, columns, and 3x3 boxes
- **Box Index Calculation** - Use formula to map position to box index
- **Set Tracking** - Use sets to track seen numbers
- **Time Complexity** - O(1) since board is always 9x9
- **Space Complexity** - O(1) for fixed-size arrays

---

### 131. ⚙️ Spiral Matrix

**🧠 Concept**

Traverse matrix in spiral order by following right, down, left, up directions with boundary tracking.

**💻 Example**

```javascript
function spiralOrder(matrix) {
  if (!matrix || matrix.length === 0) return [];
  
  const result = [];
  let top = 0, bottom = matrix.length - 1;
  let left = 0, right = matrix[0].length - 1;
  
  while (top <= bottom && left <= right) {
    // Traverse right
    for (let j = left; j <= right; j++) {
      result.push(matrix[top][j]);
    }
    top++;
    
    // Traverse down
    for (let i = top; i <= bottom; i++) {
      result.push(matrix[i][right]);
    }
    right--;
    
    // Traverse left
    if (top <= bottom) {
      for (let j = right; j >= left; j--) {
        result.push(matrix[bottom][j]);
      }
      bottom--;
    }
    
    // Traverse up
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

**💬 Explanation + Insight**

- **Boundary Tracking** - Use four boundaries to track spiral
- **Direction Sequence** - Right, down, left, up in order
- **Boundary Updates** - Shrink boundaries after each direction
- **Time Complexity** - O(m*n) visit each cell once
- **Space Complexity** - O(1) excluding result array

---

### 132. ⚙️ Rotate Image

**🧠 Concept**

Rotate matrix 90 degrees clockwise by transposing and reversing each row.

**💻 Example**

```javascript
function rotate(matrix) {
  const n = matrix.length;
  
  // Transpose matrix
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
```

**💬 Explanation + Insight**

- **Two-Step Process** - Transpose then reverse rows
- **In-place Rotation** - Modify matrix directly
- **Transpose Logic** - Swap elements across diagonal
- **Time Complexity** - O(n²) visit each cell once
- **Space Complexity** - O(1) constant space

---

### 133. ⚙️ Set Matrix Zeroes

**🧠 Concept**

Set entire row and column to zero if any cell in that row/column is zero using in-place marking.

**💻 Example**

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
  
  // Check if first column has zero
  for (let i = 0; i < m; i++) {
    if (matrix[i][0] === 0) {
      firstColZero = true;
      break;
    }
  }
  
  // Use first row and column as markers
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
  
  // Handle first row and column
  if (firstRowZero) {
    for (let j = 0; j < n; j++) {
      matrix[0][j] = 0;
    }
  }
  
  if (firstColZero) {
    for (let i = 0; i < m; i++) {
      matrix[i][0] = 0;
    }
  }
}
```

**💬 Explanation + Insight**

- **Marker Technique** - Use first row and column as markers
- **In-place Solution** - No extra space needed
- **Special Handling** - Handle first row and column separately
- **Time Complexity** - O(m*n) visit each cell multiple times
- **Space Complexity** - O(1) constant space

---

### 134. ⚙️ Game of Life

**🧠 Concept**

Simulate Conway's Game of Life by updating cells based on neighbor count using in-place state encoding.

**💻 Example**

```javascript
function gameOfLife(board) {
  const m = board.length;
  const n = board[0].length;
  
  function countLiveNeighbors(row, col) {
    let count = 0;
    for (let i = -1; i <= 1; i++) {
      for (let j = -1; j <= 1; j++) {
        if (i === 0 && j === 0) continue;
        
        const newRow = row + i;
        const newCol = col + j;
        
        if (newRow >= 0 && newRow < m && newCol >= 0 && newCol < n) {
          if (board[newRow][newCol] === 1 || board[newRow][newCol] === -1) {
            count++;
          }
        }
      }
    }
    return count;
  }
  
  // First pass: mark cells that will change
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      const liveNeighbors = countLiveNeighbors(i, j);
      
      if (board[i][j] === 1) {
        if (liveNeighbors < 2 || liveNeighbors > 3) {
          board[i][j] = -1; // Will die
        }
      } else {
        if (liveNeighbors === 3) {
          board[i][j] = 2; // Will live
        }
      }
    }
  }
  
  // Second pass: update states
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (board[i][j] === -1) {
        board[i][j] = 0;
      } else if (board[i][j] === 2) {
        board[i][j] = 1;
      }
    }
  }
}
```

**💬 Explanation + Insight**

- **State Encoding** - Use -1 for will die, 2 for will live
- **Neighbor Counting** - Count live neighbors in 3x3 area
- **Two Pass Update** - First mark changes, then apply
- **Time Complexity** - O(m*n) visit each cell twice
- **Space Complexity** - O(1) constant space

---

*This comprehensive matrix and simulation section covers essential 2D array operations including traversal, transformation, and state management techniques for efficient matrix processing.*