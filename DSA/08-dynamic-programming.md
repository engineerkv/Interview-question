# 🧩 DSA Interview Notes - LeetCode Top 150

## 🧠 Section 8 — Dynamic Programming (DP) — Q72-Q88

---

### 72. 🧠 Climbing Stairs

**🧠 Concept**

Find number of ways to climb n stairs where you can take 1 or 2 steps at a time. Use Fibonacci pattern.

**💻 Example**

```javascript
function climbStairs(n) {
  if (n <= 2) return n;
  
  let prev2 = 1;
  let prev1 = 2;
  
  for (let i = 3; i <= n; i++) {
    const current = prev1 + prev2;
    prev2 = prev1;
    prev1 = current;
  }
  
  return prev1;
}
```

**💬 Explanation + Insight**

- **Fibonacci Pattern** - Each step depends on previous two
- **Space Optimization** - Use variables instead of array
- **Base Cases** - Handle n=1 and n=2 separately
- **Time Complexity** - O(n) single pass
- **Space Complexity** - O(1) constant space

---

### 73. 🧠 House Robber

**🧠 Concept**

Maximize money robbed from houses where adjacent houses cannot be robbed. Use DP with previous two states.

**💻 Example**

```javascript
function rob(nums) {
  if (nums.length === 0) return 0;
  if (nums.length === 1) return nums[0];
  
  let prev2 = nums[0];
  let prev1 = Math.max(nums[0], nums[1]);
  
  for (let i = 2; i < nums.length; i++) {
    const current = Math.max(prev1, prev2 + nums[i]);
    prev2 = prev1;
    prev1 = current;
  }
  
  return prev1;
}
```

**💬 Explanation + Insight**

- **Adjacent Constraint** - Cannot rob adjacent houses
- **Two States** - Track previous two maximum values
- **Decision Making** - Choose between current house + prev2 or prev1
- **Time Complexity** - O(n) single pass
- **Space Complexity** - O(1) constant space

---

### 74. 🧠 Maximum Subarray

**🧠 Concept**

Find maximum sum of contiguous subarray using Kadane's algorithm with dynamic programming.

**💻 Example**

```javascript
function maxSubArray(nums) {
  let maxSoFar = nums[0];
  let maxEndingHere = nums[0];
  
  for (let i = 1; i < nums.length; i++) {
    maxEndingHere = Math.max(nums[i], maxEndingHere + nums[i]);
    maxSoFar = Math.max(maxSoFar, maxEndingHere);
  }
  
  return maxSoFar;
}
```

**💬 Explanation + Insight**

- **Kadane's Algorithm** - Track maximum ending at current position
- **Local vs Global** - Compare current maximum with global maximum
- **Reset Logic** - Start new subarray if current element is better
- **Time Complexity** - O(n) single pass
- **Space Complexity** - O(1) constant space

---

### 75. 🧠 Maximum Sum Circular Subarray

**🧠 Concept**

Find maximum sum in circular array by considering both non-circular and circular cases.

**💻 Example**

```javascript
function maxSubarraySumCircular(nums) {
  const maxNonCircular = kadane(nums);
  const totalSum = nums.reduce((sum, num) => sum + num, 0);
  const maxCircular = totalSum - minKadane(nums);
  
  return maxCircular === 0 ? maxNonCircular : Math.max(maxNonCircular, maxCircular);
}

function kadane(nums) {
  let maxSoFar = nums[0];
  let maxEndingHere = nums[0];
  
  for (let i = 1; i < nums.length; i++) {
    maxEndingHere = Math.max(nums[i], maxEndingHere + nums[i]);
    maxSoFar = Math.max(maxSoFar, maxEndingHere);
  }
  
  return maxSoFar;
}
```

**💬 Explanation + Insight**

- **Two Cases** - Non-circular and circular subarrays
- **Circular Logic** - Total sum minus minimum subarray
- **Edge Case** - Handle all negative numbers
- **Time Complexity** - O(n) three passes
- **Space Complexity** - O(1) constant space

---

### 76. 🧠 Longest Increasing Subsequence

**🧠 Concept**

Find length of longest increasing subsequence using binary search for optimization.

**💻 Example**

```javascript
function lengthOfLIS(nums) {
  const tails = [];
  
  for (const num of nums) {
    let left = 0;
    let right = tails.length;
    
    while (left < right) {
      const mid = Math.floor((left + right) / 2);
      if (tails[mid] < num) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }
    
    if (left === tails.length) {
      tails.push(num);
    } else {
      tails[left] = num;
    }
  }
  
  return tails.length;
}
```

**💬 Explanation + Insight**

- **Binary Search** - Find position to insert/update
- **Tails Array** - Store smallest tail of each length
- **Greedy Approach** - Always try to extend with smaller elements
- **Time Complexity** - O(n log n) with binary search
- **Space Complexity** - O(n) for tails array

---

### 77. 🧠 Unique Paths II

**🧠 Concept**

Count unique paths in grid with obstacles using 2D DP with obstacle handling.

**💻 Example**

```javascript
function uniquePathsWithObstacles(obstacleGrid) {
  const m = obstacleGrid.length;
  const n = obstacleGrid[0].length;
  
  if (obstacleGrid[0][0] === 1) return 0;
  
  const dp = Array(m).fill().map(() => Array(n).fill(0));
  dp[0][0] = 1;
  
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (obstacleGrid[i][j] === 1) {
        dp[i][j] = 0;
        continue;
      }
      
      if (i > 0) dp[i][j] += dp[i-1][j];
      if (j > 0) dp[i][j] += dp[i][j-1];
    }
  }
  
  return dp[m-1][n-1];
}
```

**💬 Explanation + Insight**

- **2D DP Table** - Store number of paths to each cell
- **Obstacle Handling** - Set obstacle cells to 0
- **Path Calculation** - Sum paths from top and left
- **Time Complexity** - O(m*n) fill entire grid
- **Space Complexity** - O(m*n) for DP table

---

### 78. 🧠 Minimum Path Sum

**🧠 Concept**

Find minimum path sum from top-left to bottom-right using 2D DP with path optimization.

**💻 Example**

```javascript
function minPathSum(grid) {
  const m = grid.length;
  const n = grid[0].length;
  
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (i === 0 && j === 0) continue;
      
      const top = i > 0 ? grid[i-1][j] : Infinity;
      const left = j > 0 ? grid[i][j-1] : Infinity;
      grid[i][j] += Math.min(top, left);
    }
  }
  
  return grid[m-1][n-1];
}
```

**💬 Explanation + Insight**

- **In-place DP** - Modify grid directly to save space
- **Min Path** - Choose minimum of top or left path
- **Edge Handling** - Handle first row and column separately
- **Time Complexity** - O(m*n) fill entire grid
- **Space Complexity** - O(1) in-place modification

---

### 79. 🧠 Triangle

**🧠 Concept**

Find minimum path sum in triangle from top to bottom using bottom-up DP approach.

**💻 Example**

```javascript
function minimumTotal(triangle) {
  for (let i = triangle.length - 2; i >= 0; i--) {
    for (let j = 0; j < triangle[i].length; j++) {
      triangle[i][j] += Math.min(
        triangle[i+1][j],
        triangle[i+1][j+1]
      );
    }
  }
  
  return triangle[0][0];
}
```

**💬 Explanation + Insight**

- **Bottom-up Approach** - Start from bottom row
- **Min Choice** - Choose minimum of two children
- **In-place Update** - Modify triangle directly
- **Time Complexity** - O(n²) where n is triangle height
- **Space Complexity** - O(1) in-place modification

---

### 80. 🧠 Maximal Square

**🧠 Concept**

Find area of largest square containing only 1s using 2D DP with square size tracking.

**💻 Example**

```javascript
function maximalSquare(matrix) {
  if (!matrix.length) return 0;
  
  const m = matrix.length;
  const n = matrix[0].length;
  const dp = Array(m+1).fill().map(() => Array(n+1).fill(0));
  let maxSide = 0;
  
  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      if (matrix[i-1][j-1] === '1') {
        dp[i][j] = Math.min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1;
        maxSide = Math.max(maxSide, dp[i][j]);
      }
    }
  }
  
  return maxSide * maxSide;
}
```

**💬 Explanation + Insight**

- **Square DP** - Track maximum square ending at each cell
- **Min Neighbors** - Square size depends on minimum of three neighbors
- **Area Calculation** - Return side length squared
- **Time Complexity** - O(m*n) fill entire matrix
- **Space Complexity** - O(m*n) for DP table

---

### 81. 🧠 Longest Palindromic Substring

**🧠 Concept**

Find longest palindromic substring using expand around centers approach.

**💻 Example**

```javascript
function longestPalindrome(s) {
  let start = 0;
  let maxLen = 1;
  
  for (let i = 0; i < s.length; i++) {
    const len1 = expandAroundCenter(s, i, i);
    const len2 = expandAroundCenter(s, i, i + 1);
    const len = Math.max(len1, len2);
    
    if (len > maxLen) {
      start = i - Math.floor((len - 1) / 2);
      maxLen = len;
    }
  }
  
  return s.substring(start, start + maxLen);
}

function expandAroundCenter(s, left, right) {
  while (left >= 0 && right < s.length && s[left] === s[right]) {
    left--;
    right++;
  }
  return right - left - 1;
}
```

**💬 Explanation + Insight**

- **Center Expansion** - Expand from each possible center
- **Two Cases** - Odd length (center) and even length (between chars)
- **Palindrome Check** - Expand while characters match
- **Time Complexity** - O(n²) for each center
- **Space Complexity** - O(1) constant space

---

### 82. 🧠 Interleaving String

**🧠 Concept**

Check if string is interleaving of two other strings using 2D DP with character matching.

**💻 Example**

```javascript
function isInterleave(s1, s2, s3) {
  if (s1.length + s2.length !== s3.length) return false;
  
  const dp = Array(s1.length + 1).fill().map(() => Array(s2.length + 1).fill(false));
  dp[0][0] = true;
  
  for (let i = 0; i <= s1.length; i++) {
    for (let j = 0; j <= s2.length; j++) {
      if (i > 0 && s1[i-1] === s3[i+j-1]) {
        dp[i][j] = dp[i][j] || dp[i-1][j];
      }
      if (j > 0 && s2[j-1] === s3[i+j-1]) {
        dp[i][j] = dp[i][j] || dp[i][j-1];
      }
    }
  }
  
  return dp[s1.length][s2.length];
}
```

**💬 Explanation + Insight**

- **2D DP Table** - Track interleaving possibilities
- **Character Matching** - Check if characters match from either string
- **Path Validation** - Ensure valid path through both strings
- **Time Complexity** - O(m*n) where m,n are string lengths
- **Space Complexity** - O(m*n) for DP table

---

### 83. 🧠 Edit Distance

**🧠 Concept**

Find minimum operations to convert one string to another using 2D DP with insert, delete, replace operations.

**💻 Example**

```javascript
function minDistance(word1, word2) {
  const m = word1.length;
  const n = word2.length;
  const dp = Array(m+1).fill().map(() => Array(n+1).fill(0));
  
  for (let i = 0; i <= m; i++) dp[i][0] = i;
  for (let j = 0; j <= n; j++) dp[0][j] = j;
  
  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      if (word1[i-1] === word2[j-1]) {
        dp[i][j] = dp[i-1][j-1];
      } else {
        dp[i][j] = 1 + Math.min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]);
      }
    }
  }
  
  return dp[m][n];
}
```

**💬 Explanation + Insight**

- **Three Operations** - Insert, delete, replace
- **Base Cases** - Empty string conversions
- **Min Operations** - Choose minimum of three operations
- **Time Complexity** - O(m*n) fill entire table
- **Space Complexity** - O(m*n) for DP table

---

### 84. 🧠 Word Break

**🧠 Concept**

Check if string can be segmented into dictionary words using DP with substring validation.

**💻 Example**

```javascript
function wordBreak(s, wordDict) {
  const dp = Array(s.length + 1).fill(false);
  dp[0] = true;
  
  for (let i = 1; i <= s.length; i++) {
    for (let j = 0; j < i; j++) {
      if (dp[j] && wordDict.includes(s.substring(j, i))) {
        dp[i] = true;
        break;
      }
    }
  }
  
  return dp[s.length];
}
```

**💬 Explanation + Insight**

- **Substring Validation** - Check if substring is in dictionary
- **DP State** - Track if prefix can be segmented
- **Early Break** - Stop checking once valid segmentation found
- **Time Complexity** - O(n²) for each position
- **Space Complexity** - O(n) for DP array

---

### 85. 🧠 Best Time to Buy and Sell Stock

**🧠 Concept**

Find maximum profit from buying and selling stock once using DP with minimum price tracking.

**💻 Example**

```javascript
function maxProfit(prices) {
  let minPrice = prices[0];
  let maxProfit = 0;
  
  for (let i = 1; i < prices.length; i++) {
    maxProfit = Math.max(maxProfit, prices[i] - minPrice);
    minPrice = Math.min(minPrice, prices[i]);
  }
  
  return maxProfit;
}
```

**💬 Explanation + Insight**

- **Single Transaction** - Buy once, sell once
- **Minimum Tracking** - Keep track of minimum price seen
- **Profit Calculation** - Calculate profit at each day
- **Time Complexity** - O(n) single pass
- **Space Complexity** - O(1) constant space

---

### 86. 🧠 Best Time to Buy and Sell Stock III

**🧠 Concept**

Find maximum profit with at most two transactions using DP with state machine approach.

**💻 Example**

```javascript
function maxProfit(prices) {
  let buy1 = -prices[0];
  let sell1 = 0;
  let buy2 = -prices[0];
  let sell2 = 0;
  
  for (let i = 1; i < prices.length; i++) {
    buy1 = Math.max(buy1, -prices[i]);
    sell1 = Math.max(sell1, buy1 + prices[i]);
    buy2 = Math.max(buy2, sell1 - prices[i]);
    sell2 = Math.max(sell2, buy2 + prices[i]);
  }
  
  return sell2;
}
```

**💬 Explanation + Insight**

- **State Machine** - Track four states for two transactions
- **Transaction Logic** - Buy before sell, second after first
- **Max Profit** - Update maximum profit at each state
- **Time Complexity** - O(n) single pass
- **Space Complexity** - O(1) constant space

---

### 87. 🧠 Best Time to Buy and Sell Stock IV

**🧠 Concept**

Find maximum profit with at most k transactions using DP with transaction tracking.

**💻 Example**

```javascript
function maxProfit(k, prices) {
  if (k >= prices.length / 2) {
    return maxProfitUnlimited(prices);
  }
  
  const buy = Array(k + 1).fill(-prices[0]);
  const sell = Array(k + 1).fill(0);
  
  for (let i = 1; i < prices.length; i++) {
    for (let j = k; j >= 1; j--) {
      sell[j] = Math.max(sell[j], buy[j] + prices[i]);
      buy[j] = Math.max(buy[j], sell[j-1] - prices[i]);
    }
  }
  
  return sell[k];
}
```

**💬 Explanation + Insight**

- **K Transactions** - Track profit for each transaction count
- **Optimization** - Handle case where k >= n/2
- **State Update** - Update buy and sell states
- **Time Complexity** - O(n*k) for each price and transaction
- **Space Complexity** - O(k) for state arrays

---

### 88. 🧠 Binary Tree Maximum Path Sum

**🧠 Concept**

Find maximum path sum in binary tree where path can start and end anywhere using DFS with path tracking.

**💻 Example**

```javascript
function maxPathSum(root) {
  let maxSum = -Infinity;
  
  function dfs(node) {
    if (!node) return 0;
    
    const leftSum = Math.max(0, dfs(node.left));
    const rightSum = Math.max(0, dfs(node.right));
    
    const currentSum = node.val + leftSum + rightSum;
    maxSum = Math.max(maxSum, currentSum);
    
    return node.val + Math.max(leftSum, rightSum);
  }
  
  dfs(root);
  return maxSum;
}
```

**💬 Explanation + Insight**

- **DFS Traversal** - Recursively explore all paths
- **Path Combination** - Combine left and right paths through root
- **Negative Handling** - Ignore negative path contributions
- **Time Complexity** - O(n) visit each node once
- **Space Complexity** - O(h) recursion stack height

---

*This comprehensive dynamic programming section covers essential DP patterns including optimization problems, sequence problems, and advanced state management techniques.*