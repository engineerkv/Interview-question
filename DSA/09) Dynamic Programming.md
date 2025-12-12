# Dynamic Programming

---

## 📍 Navigation

<div align="center">

[← Previous: Graphs](08%29%20Graphs.md) • [Home: README](README.md) • [Next: Recursion & Backtracking →](10%29%20Recursion%20%26%20Backtracking.md)

[📋 Cheatsheet](DSA%20Interview%20Cheatsheet.md)

</div>

---

## Q160. 💡 Fibonacci (Memo & Tabulation)

**Problem:** Calculate the nth Fibonacci number. The Fibonacci sequence is defined as F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n > 1.

**Approach:** Use dynamic programming to avoid recalculating overlapping subproblems. Can use memoization (top-down) or tabulation (bottom-up).

### Solution 1: Tabulation (Bottom-Up) (Optimal)

```javascript
function fib(n) {
  if (n <= 1) return n;

  const dp = new Array(n + 1).fill(0);
  dp[0] = 0;
  dp[1] = 1;

  for (let i = 2; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }

  return dp[n];
}

```

### Solution 2: Space-Optimized Tabulation

```javascript
function fib(n) {
  if (n <= 1) return n;

  let prev2 = 0;
  let prev1 = 1;

  for (let i = 2; i <= n; i++) {
    const curr = prev1 + prev2;
    prev2 = prev1;
    prev1 = curr;
  }

  return prev1;
}

```

### Solution 3: Memoization (Top-Down)

```javascript
function fib(n) {
  const memo = new Map();

  function helper(n) {
    if (n <= 1) return n;
    if (memo.has(n)) return memo.get(n);

    const result = helper(n - 1) + helper(n - 2);
    memo.set(n, result);
    return result;
  }

  return helper(n);
}

// Test Cases:
// Input: n = 2
// Output: 1

// Input: n = 3
// Output: 2

// Input: n = 4
// Output: 3

// Input: n = 10
// Output: 55

```

**Time Complexity:**

- Tabulation: O(n) - Single pass through array

- Space-Optimized: O(n) time, O(1) space

- Memoization: O(n) - Each subproblem computed once

**Space Complexity:**

- Tabulation: O(n) - DP array

- Space-Optimized: O(1) - Only two variables

- Memoization: O(n) - Recursion stack + memo map

## Q161. 💡 Climbing Stairs

**Problem:** You are climbing a staircase. It takes `n` steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

**Approach:** This is identical to Fibonacci. Ways to reach step n = ways to reach step (n-1) + ways to reach step (n-2).

### Solution 1: Tabulation (Bottom-Up) (Optimal)

```javascript
function climbStairs(n) {
  if (n === 1) return 1;
  if (n === 2) return 2;

  const dp = new Array(n + 1).fill(0);
  dp[1] = 1;
  dp[2] = 2;

  for (let i = 3; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }

  return dp[n];
}

```

### Solution 2: Space-Optimized

```javascript
function climbStairs(n) {
  if (n <= 2) return n;

  let prev2 = 1;  // Ways to reach step 1
  let prev1 = 2;  // Ways to reach step 2

  for (let i = 3; i <= n; i++) {
    const curr = prev1 + prev2;
    prev2 = prev1;
    prev1 = curr;
  }

  return prev1;
}

```

// Test Cases:
// Input: n = 2
// Output: 2

// Input: n = 3
// Output: 3

// Input: n = 4
// Output: 5

// Input: n = 5
// Output: 8

```

**Time Complexity:** O(n) - Single pass through steps
**Space Complexity:** O(1) with optimization, O(n) with DP array

## Q162. 💡 Coin Change

**Problem:** You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money. Return the minimum number of coins needed to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

**Approach:** Use dynamic programming. For each amount, try all coins and take minimum. dp[amount] = min(dp[amount], dp[amount - coin] + 1).

### Solution 1: Tabulation (Bottom-Up) (Optimal)

```javascript

function coinChange(coins, amount) {
  const dp = new Array(amount + 1).fill(Infinity);
  dp[0] = 0;  // Base case: 0 coins needed for amount 0

  // For each coin
  for (const coin of coins) {
    // For each amount from coin to target
    for (let currAmount = coin; currAmount <= amount; currAmount++) {
      dp[currAmount] = Math.min(dp[currAmount], dp[currAmount - coin] + 1);
    }
  }

  return dp[amount] === Infinity ? -1 : dp[amount];
}

```

// Test Cases:
// Input: coins = [1, 2, 5], amount = 11
// Output: 3
// Explanation: 11 = 5 + 5 + 1

// Input: coins = [2], amount = 3
// Output: -1
// Explanation: Cannot make amount 3 with only coin 2

// Input: coins = [1], amount = 0
// Output: 0

// Input: coins = [1, 3, 4], amount = 6
// Output: 2
// Explanation: 6 = 3 + 3

```

**Time Complexity:** O(n × amount) - n coins, amount values
**Space Complexity:** O(amount) - DP array

## Q163. 💡 0-1 Knapsack

**Problem:** Given a knapsack with capacity `W` and `n` items, each with weight `wt[i]` and value `val[i]`, determine the maximum value that can be obtained by selecting items such that each item can be used at most once and the total weight doesn't exceed `W`.

**Approach:** Use dynamic programming with 1D array. Iterate backwards on weight to ensure each item is used at most once. dp[w] = max(dp[w], dp[w - wt[i] + val[i]).

### Solution 1: 1D DP with Backward Iteration (Optimal)

```javascript
function knap01(W, wt, val) {
  const dp = new Array(W + 1).fill(0);

  // For each item
  for (let i = 0; i < wt.length; i++) {
    // Iterate backwards to avoid using item twice
    for (let w = W; w >= wt[i]; w--) {
      // Take max of: not taking item, or taking item
      dp[w] = Math.max(dp[w], dp[w - wt[i] + val[i]);
    }
  }

  return dp[W];
}

```

### Solution 2: 2D DP (More Intuitive)

```javascript
function knap01(W, wt, val) {
  const n = wt.length;
  const dp = Array.from({ length: n + 1 }, () => new Array(W + 1).fill(0));

  for (let i = 1; i <= n; i++) {
    for (let w = 1; w <= W; w++) {
      if (wt[i - 1] <= w) {
        // Can take item: max of taking or not taking
        dp[i][w] = Math.max(
          dp[i - 1][w],  // Not take
          dp[i - 1][w - wt[i - 1] + val[i - 1]  // Take
        );
      } else {
        // Cannot take item
        dp[i][w] = dp[i - 1][w];
      }
    }
  }

  return dp[n][W];
}

```

// Test Cases:
// Input: W = 50, wt = [10, 20, 30], val = [60, 100, 120]
// Output: 220
// Explanation: Take items with weight 20 and 30 (value 100 + 120 = 220)

// Input: W = 10, wt = [5, 4, 6], val = [10, 40, 30]
// Output: 50
// Explanation: Take items with weight 4 and 6 (value 40 + 30 = 70) or 5 and 4 (value 10 + 40 = 50)

// Input: W = 8, wt = [2, 3, 4, 5], val = [1, 2, 5, 6]
// Output: 8
// Explanation: Take items with weight 3 and 5 (value 2 + 6 = 8)

```

**Time Complexity:** O(n × W) - n items, W capacity
**Space Complexity:** O(W) with 1D, O(n × W) with 2D

## Q164. 💡 Longest Increasing Subsequence

**Problem:** Given an integer array `nums`, return the length of the longest strictly increasing subsequence. A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.

**Approach:** Use patience sorting with binary search. Maintain a `tails` array where `tails[i]` is the smallest tail element of all increasing subsequences of length `i+1`. Use binary search to find the correct position to insert/update.

### Solution 1: Patience Sorting with Binary Search (Optimal)

```javascript

function lengthOfLIS(nums) {
  const tails = [];

  for (const num of nums) {
    // Binary search for insertion position
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

    // Insert or replace at position left
    if (left === tails.length) {
      tails.push(num);
    } else {
    tails[left] = num;
  }
  }

  return tails.length;
}

```

### Solution 2: DP with O(n²) Time

```javascript

function lengthOfLIS(nums) {
  const n = nums.length;
  const dp = new Array(n).fill(1);

  for (let i = 1; i < n; i++) {
    for (let j = 0; j < i; j++) {
      if (nums[j] < nums[i]) {
        dp[i] = Math.max(dp[i], dp[j] + 1);
      }
    }
  }

  return Math.max(...dp);
}

```

// Test Cases:
// Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]
// Output: 4
// Explanation: Longest increasing subsequence is [2, 3, 7, 101] with length 4

// Input: nums = [0, 1, 0, 3, 2, 3]
// Output: 4
// Explanation: LIS is [0, 1, 2, 3] with length 4

// Input: nums = [7, 7, 7, 7, 7, 7, 7]
// Output: 1

// Input: nums = [1]
// Output: 1

```

**Time Complexity:**

- Solution 1: O(n log n) - Binary search for each element

- Solution 2: O(n²) - Nested loops

**Space Complexity:** O(n) - tails/dp array

## Q165. 💡 Longest Common Subsequence

**Problem:** Given two strings `text1` and `text2`, return the length of their longest common subsequence. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.

**Approach:** Use 2D dynamic programming. If characters match, extend LCS from diagonal. If not, take maximum from top or left.

### Solution 1: 2D DP (Optimal)

```javascript
function longestCommonSubsequence(text1, text2) {
  const m = text1.length;
  const n = text2.length;
  const dp = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));

  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      if (text1[i - 1] === text2[j - 1]) {
        // Characters match: extend LCS
        dp[i][j] = dp[i - 1][j - 1] + 1;
      } else {
        // Characters don't match: take max of top or left
        dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
      }
    }
  }

  return dp[m][n];
}

```

### Solution 2: Space-Optimized (O(min(m,n)))

```javascript
function longestCommonSubsequence(text1, text2) {
  // Use shorter string for DP array
  if (text1.length < text2.length) {
    [text1, text2] = [text2, text1];
  }

  const m = text1.length;
  const n = text2.length;
  let prev = new Array(n + 1).fill(0);
  let curr = new Array(n + 1).fill(0);

  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      if (text1[i - 1] === text2[j - 1]) {
        curr[j] = prev[j - 1] + 1;
      } else {
        curr[j] = Math.max(prev[j], curr[j - 1]);
      }
    }
    [prev, curr] = [curr, prev];
  }

  return prev[n];
}

```

// Test Cases:
// Input: text1 = "abcde", text2 = "ace"
// Output: 3
// Explanation: LCS is "ace" with length 3

// Input: text1 = "abc", text2 = "abc"
// Output: 3
// Explanation: LCS is "abc" with length 3

// Input: text1 = "abc", text2 = "def"
// Output: 0

// Input: text1 = "bl", text2 = "yby"
// Output: 1

```

**Time Complexity:** O(m × n) - Fill DP table
**Space Complexity:** O(m × n) with 2D, O(min(m,n)) with optimization

## Q166. 💡 Edit Distance (Levenshtein Distance)

**Problem:** Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2`. You can perform the following three operations: insert a character, delete a character, or replace a character.

**Approach:** Use 2D dynamic programming. If characters match, no operation needed. If not, take minimum of insert, delete, or replace operations.

### Solution 1: 2D DP (Optimal)

```javascript

function minDistance(word1, word2) {
  const m = word1.length;
  const n = word2.length;
  const dp = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));

  // Base cases: convert empty string to word2 (insert all)
  for (let j = 0; j <= n; j++) {
    dp[0][j] = j;
  }
  // Base cases: convert word1 to empty string (delete all)
  for (let i = 0; i <= m; i++) {
    dp[i][0] = i;
  }

  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      if (word1[i - 1] === word2[j - 1]) {
        // Characters match: no operation needed
        dp[i][j] = dp[i - 1][j - 1];
      } else {
        // Characters don't match: take minimum of three operations
        dp[i][j] = 1 + Math.min(
          dp[i - 1][j],     // Delete from word1
          dp[i][j - 1],     // Insert into word1
          dp[i - 1][j - 1]  // Replace
        );
      }
    }
  }

  return dp[m][n];
}

```

// Test Cases:
// Input: word1 = "horse", word2 = "ros"
// Output: 3
// Explanation: horse -> rorse (replace 'h' with 'r'), rorse -> rose (remove 'r'), rose -> ros (remove 'e')

// Input: word1 = "intention", word2 = "execution"
// Output: 5

// Input: word1 = "", word2 = "a"
// Output: 1

// Input: word1 = "abc", word2 = "abc"
// Output: 0

```

**Time Complexity:** O(m × n) - Fill DP table
**Space Complexity:** O(m × n) - DP table (can optimize to O(min(m,n)))

## Q167. 💡 Rod Cutting

**Problem:** Given a rod of length `n` and an array `price` where `price[i]` represents the price of a rod piece of length `i+1`, find the maximum value obtainable by cutting the rod and selling the pieces.

**Approach:** This is an unbounded knapsack problem. For each length, try all possible cuts and take the maximum value. dp[i] = max(dp[i], price[len-1] + dp[i-len]).

### Solution 1: Unbounded Knapsack DP (Optimal)

```javascript
function rodCutting(price, rodLength) {
  const dp = new Array(rodLength + 1).fill(0);

  // For each possible rod length
  for (let i = 1; i <= rodLength; i++) {
    // Try all possible cuts
    for (let len = 1; len <= i; len++) {
      dp[i] = Math.max(dp[i], price[len - 1] + dp[i - len]);
    }
  }

  return dp[rodLength];
}

```

// Test Cases:
// Input: price = [1, 5, 8, 9, 10, 17, 17, 20], n = 8
// Output: 22
// Explanation: Cut into pieces of length 2 and 6: 5 + 17 = 22

// Input: price = [1, 5, 8], n = 3
// Output: 8
// Explanation: Best is to keep rod uncut: price[3] = 8

// Input: price = [3, 5, 8], n = 3
// Output: 9
// Explanation: Cut into pieces of length 1+1+1: 3*3 = 9

// Input: price = [1], n = 1
// Output: 1

```

**Time Complexity:** O(n²) - For each length, try all cuts
**Space Complexity:** O(n) - DP array

## Q168. ➕ Partition Equal Subset Sum

**Problem:** Given a non-empty array `nums` containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

**Approach:** This reduces to subset sum problem. If total sum is odd, return false. Otherwise, check if we can reach sum/2 using subset sum. Use 1D boolean DP with backward iteration (0-1 knapsack style).

### Solution 1: Subset Sum DP (Optimal)

```javascript

function canPartition(nums) {
  const sum = nums.reduce((acc, num) => acc + num, 0);

  // If sum is odd, cannot partition equally
  if (sum % 2 !== 0) return false;

  const target = sum / 2;
  const dp = new Array(target + 1).fill(false);
  dp[0] = true;  // Base case: sum 0 is always achievable

  // For each number (0-1 knapsack: each number used once)
  for (const num of nums) {
    // Iterate backwards to avoid using same number twice
    for (let j = target; j >= num; j--) {
      dp[j] = dp[j] || dp[j - num];
    }
  }

  return dp[target];
}

```

// Test Cases:
// Input: nums = [1, 5, 11, 5]
// Output: true
// Explanation: Can partition into [1, 5, 5] and [11] (both sum to 11)

// Input: nums = [1, 2, 3, 5]
// Output: false
// Explanation: Total sum is 11 (odd), cannot partition equally

// Input: nums = [1, 2, 3, 4]
// Output: true
// Explanation: Can partition into [1, 4] and [2, 3] (both sum to 5)

// Input: nums = [1, 1]
// Output: true

```

**Time Complexity:** O(n × sum) - n numbers, sum/2 target
**Space Complexity:** O(sum) - DP array

## Q169. 💡 House Robber

**Problem:** You are a robber planning to rob houses along a street. Each house has a certain amount of money stashed. The only constraint stopping you from robbing each of them is that adjacent houses have security systems connected, and they will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

**Approach:** Use dynamic programming. For each house, decide whether to rob it (use previous best from 2 houses back) or skip it (use previous best). dp[i] = max(dp[i-1], dp[i-2] + nums[i]).

### Solution 1: DP Array (Optimal)

```javascript
function rob(nums) {
  if (nums.length === 0) return 0;
  if (nums.length === 1) return nums[0];

  const dp = new Array(nums.length).fill(0);
  dp[0] = nums[0];
  dp[1] = Math.max(nums[0], nums[1]);

  for (let i = 2; i < nums.length; i++) {
    // Max of: skip current (dp[i-1]) or rob current (dp[i-2] + nums[i])
    dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i]);
  }

  return dp[nums.length - 1];
}

```

### Solution 2: Space-Optimized

```javascript
function rob(nums) {
  if (nums.length === 0) return 0;
  if (nums.length === 1) return nums[0];

  let prev2 = nums[0];  // Best from 2 houses back
  let prev1 = Math.max(nums[0], nums[1]);  // Best from 1 house back

  for (let i = 2; i < nums.length; i++) {
    const curr = Math.max(prev1, prev2 + nums[i]);
    prev2 = prev1;
    prev1 = curr;
  }

  return prev1;
}

```

// Test Cases:
// Input: nums = [1, 2, 3, 1]
// Output: 4
// Explanation: Rob houses 1 and 3 (1 + 3 = 4)

// Input: nums = [2, 7, 9, 3, 1]
// Output: 12
// Explanation: Rob houses 1, 3, and 5 (2 + 9 + 1 = 12)

// Input: nums = [2, 1, 1, 2]
// Output: 4
// Explanation: Rob houses 1 and 4 (2 + 2 = 4)

// Input: nums = [1]
// Output: 1

// Input: nums = []
// Output: 0

```

**Time Complexity:** O(n) - Single pass through houses
**Space Complexity:** O(n) with DP array, O(1) with optimization

## Q170. 💡 House Robber II

**Problem:** You are a professional robber planning to rob houses arranged in a circle. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. You cannot rob two adjacent houses. Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

**Approach:** Since houses are in a circle, the first and last houses are adjacent. Solve two linear subproblems: rob houses 0 to n-2, or rob houses 1 to n-1, and take the maximum.

### Solution 1: Dynamic Programming (Optimal)

```javascript

function rob2(nums) {
  if (nums.length === 1) return nums[0];

  const robLinear = arr => {
    if (arr.length === 0) return 0;
    if (arr.length === 1) return arr[0];

    const dp = new Array(arr.length).fill(0);
    dp[0] = arr[0];
    dp[1] = Math.max(arr[0], arr[1]);

    for (let i = 2; i < arr.length; i++) {
      dp[i] = Math.max(dp[i - 1], dp[i - 2] + arr[i]);
    }

    return dp[arr.length - 1];
  };

  return Math.max(robLinear(nums.slice(0, -1)), robLinear(nums.slice(1)));
}

// Test Cases:
// Input: nums = [2, 3, 2]
// Output: 3
// Explanation: Rob house 2 (index 1) since houses are arranged in a circle

// Input: nums = [1, 2, 3, 1]
// Output: 4
// Explanation: Rob houses 1 and 3 (excluding last or first)

// Input: nums = [1, 2, 3]
// Output: 3
// Explanation: Rob house 3 (excluding first or last)

// Input: nums = [1]
// Output: 1

```

**Time Complexity:** O(n) - Two linear robberies
**Space Complexity:** O(n) - DP array (can optimize to O(1))

## Q171. 💡 Decode Ways

**Problem:** A message containing letters from `A-Z` can be encoded into numbers using the following mapping: 'A' -> "1", 'B' -> "2", ..., 'Z' -> "26". Given a string `s` containing only digits, return the number of ways to decode it.

**Approach:** Use dynamic programming. For each position, check if one-digit or two-digit decode is valid. dp[i] = ways to decode up to position i.

### Solution 1: DP Array (Optimal)

```javascript

function numDecodings(s) {
  if (!s || s[0] === '0') return 0;

  const n = s.length;
  const dp = new Array(n + 1).fill(0);
  dp[0] = 1;  // Empty string has 1 way
  dp[1] = s[0] !== '0' ? 1 : 0;

  for (let i = 2; i <= n; i++) {
    // Check one-digit decode
    const oneDigit = s[i - 1];
    if (oneDigit !== '0') {
      dp[i] += dp[i - 1];
    }

    // Check two-digit decode
    const twoDigits = s.slice(i - 2, i);
    if (twoDigits[0] !== '0' && parseInt(twoDigits) <= 26) {
      dp[i] += dp[i - 2];
    }

    // If no valid decode, return 0
    if (dp[i] === 0) return 0;
  }

  return dp[n];
}

```

// Test Cases:
// Input: s = "12"
// Output: 2
// Explanation: "12" can be decoded as "AB" (1 2) or "L" (12)

// Input: s = "226"
// Output: 3
// Explanation: "226" can be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6)

// Input: s = "06"
// Output: 0
// Explanation: Invalid encoding (no leading zeros allowed)

// Input: s = "0"
// Output: 0

// Input: s = "27"
// Output: 1
// Explanation: "27" can only be decoded as "BG" (2 7)

```

**Time Complexity:** O(n) - Single pass through string
**Space Complexity:** O(n) - DP array (can optimize to O(1))

## Q172. 📊 DP on Grid — Min Path Sum / Unique Paths

**Problem:**

1. **Min Path Sum:** Given a `m x n` grid filled with non-negative numbers, find a path from top-left to bottom-right which minimizes the sum of all numbers along its path. You can only move down or right.

2. **Unique Paths:** A robot is located at the top-left corner of a `m x n` grid. The robot can only move either down or right at any point in time. How many unique paths are there to reach the bottom-right corner?

**Approach:** Use grid DP. For each cell, compute value from top or left. Min Path Sum: take minimum cost. Unique Paths: sum paths from top and left.

### Solution 1: Min Path Sum

```javascript
function minPathSum(grid) {
  const m = grid.length;
  const n = grid[0].length;
  const dp = new Array(n).fill(0);

  // Initialize first row
  dp[0] = grid[0][0];
  for (let j = 1; j < n; j++) {
    dp[j] = dp[j - 1] + grid[0][j];
  }

  // Fill remaining rows
  for (let i = 1; i < m; i++) {
    dp[0] += grid[i][0];  // First column
    for (let j = 1; j < n; j++) {
      dp[j] = grid[i][j] + Math.min(dp[j], dp[j - 1]);
    }
  }

  return dp[n - 1];
}

```

### Solution 2: Unique Paths

```javascript
function uniquePaths(m, n) {
  const dp = new Array(n).fill(1);

  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      dp[j] += dp[j - 1];  // Paths from top + paths from left
    }
  }

  return dp[n - 1];
}

```

// Test Cases:
//
// minPathSum:
// Input: grid = [1,3,1],[1,5,1],[4,2,1]
// Output: 7
// Explanation: Path 1 -> 3 -> 1 -> 1 -> 1 has minimum sum = 7

// Input: grid = [1,2,3],[4,5,6]
// Output: 12
// Explanation: Path 1 -> 2 -> 3 -> 6 has minimum sum = 12
//
// uniquePaths:
// Input: m = 3, n = 7
// Output: 28

// Input: m = 3, n = 2
// Output: 3

// Input: m = 7, n = 3
// Output: 28

// Input: m = 3, n = 3
// Output: 6

```

**Time Complexity:** O(m × n) - Visit each cell once
**Space Complexity:** O(n) - Space optimized DP array

## Q173. 🔤 Palindromic Substrings

**Problem:** Given a string `s`, return the number of palindromic substrings in it. A string is a palindrome when it reads the same backward as forward. A substring is a contiguous sequence of characters within the string.

**Approach:** Expand around centers. For each position, expand for odd-length (center at i) and even-length (center between i and i+1) palindromes.

### Solution 1: Expand Around Centers (Optimal)

```javascript

function countSubstrings(s) {
  let count = 0;

  function expandAroundCenter(left, right) {
    while (left >= 0 && right < s.length && s[left] === s[right]) {
      count++;
      left--;
      right++;
    }
  }

  for (let i = 0; i < s.length; i++) {
    expandAroundCenter(i, i);      // Odd-length palindromes
    expandAroundCenter(i, i + 1);  // Even-length palindromes
  }

  return count;
}

```

// Test Cases:
// Input: s = "abc"
// Output: 3
// Explanation: Three palindromic strings: "a", "b", "c"

// Input: s = "aaa"
// Output: 6
// Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa"

// Input: s = "racecar"
// Output: 10

// Input: s = ""
// Output: 0

// Input: s = "a"
// Output: 1

```

**Time Complexity:** O(n²) - Expand around 2n-1 centers
**Space Complexity:** O(1) - Only counter variable

## Q174. 💡 Burst Balloons

**Problem:** You are given `n` balloons, indexed from `0` to `n - 1`. Each balloon is painted with a number on it represented by an array `nums`. You are asked to burst all the balloons. If you burst the `i`th balloon, you will get `nums[i - 1] * nums[i] * nums[i + 1]` coins. If `i - 1` or `i + 1` goes out of bounds of the array, then treat it as if there is a balloon with a `1` painted on it. Return the maximum coins you can collect by bursting the balloons wisely.

**Approach:** Use interval DP. For each interval, try all possible last balloons to burst. dp[left][right] = maximum coins from bursting balloons in (left, right) with last balloon k.

### Solution 1: Interval DP (Optimal)

```javascript
function maxCoins(nums) {
  // Add boundary balloons with value 1
  const arr = [1, ...nums, 1];
  const n = arr.length;
  const dp = Array.from({ length: n }, () => Array(n).fill(0));

  // Length of interval
  for (let len = 2; len < n; len++) {
    // Left boundary
    for (let left = 0; left + len < n; left++) {
      const right = left + len;
      // Try all possible last balloons to burst
      for (let k = left + 1; k < right; k++) {
        dp[left][right] = Math.max(
          dp[left][right],
          arr[left] * arr[k] * arr[right] + dp[left][k] + dp[k][right]
        );
      }
    }
  }

  return dp[0][n - 1];
}

```

// Test Cases:
// Input: nums = [3, 1, 5, 8]
// Output: 167
// Explanation: nums = [3,1,5,8] -> [3,5,8] -> [3,8] -> [8] -> []
// coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 15 + 120 + 24 + 8 = 167

// Input: nums = [1, 5]
// Output: 10
// Explanation: Burst 1 first: coins = 1*1*5 = 5, then burst 5: coins = 1*5*1 = 5. Total = 10

// Input: nums = [7]
// Output: 7

// Input: nums = [1, 2, 3, 4]
// Output: 40

```

**Time Complexity:** O(n³) - Three nested loops
**Space Complexity:** O(n²) - DP table

## Q175. ⬆️ ⬆️ ⬆️ Maximum Profit in Job Scheduling

**Problem:** You're given `n` jobs, where each job has a start time `start[i]`, end time `end[i]`, and profit `profit[i]`. You want to maximize your profit by selecting non-overlapping jobs. Return the maximum profit you can achieve.

**Approach:** Sort jobs by end time. Use DP with binary search. For each job, find the last non-overlapping job and take maximum of: skipping current job or taking current job + best from previous.

### Solution 1: DP with Binary Search (Optimal)

```javascript

function jobScheduling(startTime, endTime, profit) {
  const n = startTime.length;
  const jobs = [];

  // Create job array
  for (let i = 0; i < n; i++) {
    jobs.push([startTime[i], endTime[i], profit[i]);
  }

  // Sort by end time
  jobs.sort((a, b) => a[1] - b[1]);
  const ends = jobs.map(job => job[1]);

  const dp = new Array(n).fill(0);
  dp[0] = jobs[0][2];

  for (let i = 1; i < n; i++) {
    const [start, end, profitVal] = jobs[i];

    // Binary search for last non-overlapping job
    let left = 0, right = i - 1, pos = -1;
    while (left <= right) {
      const mid = Math.floor((left + right) / 2);
      if (ends[mid] <= start) {
        pos = mid;
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }

    // Max of: skip current or take current + best from previous
    dp[i] = Math.max(
      dp[i - 1],
      profitVal + (pos >= 0 ? dp[pos] : 0)
    );
  }

  return dp[n - 1];
}

```

// Test Cases:
// Input: startTime = [1, 2, 3, 3], endTime = [3, 4, 5, 6], profit = [50, 10, 40, 70]
// Output: 120
// Explanation: Take jobs with indices 0 and 3 (profit 50 + 70 = 120)

// Input: startTime = [1, 2, 3, 4, 6], endTime = [3, 5, 10, 6, 9], profit = [20, 20, 100, 70, 60]
// Output: 150

// Input: startTime = [1, 1, 1], endTime = [2, 3, 4], profit = [5, 6, 4]
// Output: 6

```

**Time Complexity:** O(n log n) - Sorting + binary search per job
**Space Complexity:** O(n) - Jobs array and DP array

## Q176. 💡 Wildcard Matching

**Problem:** Given an input string `s` and a pattern `p`, implement wildcard pattern matching with support for `'?'` and `'*'` where:

- `'?'` matches any single character

- `'*'` matches any sequence of characters (including empty sequence)

Return `true` if the pattern matches the entire input string, `false` otherwise.

**Approach:** Use 2D dynamic programming. `'*'` can match empty sequence (use dp[i][j-1]) or match one or more characters (use dp[i-1][j]). `'?'` matches single character.

### Solution 1: 2D DP (Optimal)

```javascript
function isMatch(s, p) {
  const m = s.length;
  const n = p.length;
  const dp = Array.from({ length: m + 1 }, () => Array(n + 1).fill(false));
  dp[0][0] = true;  // Empty string matches empty pattern

  // Handle '*' matching empty sequence
  for (let j = 1; j <= n; j++) {
    if (p[j - 1] === '*') {
      dp[0][j] = dp[0][j - 1];
    }
  }

  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      if (p[j - 1] === '*') {
        // '*' matches empty or one or more characters
        dp[i][j] = dp[i][j - 1] || dp[i - 1][j];
      } else if (p[j - 1] === '?' || p[j - 1] === s[i - 1]) {
        // '?' or exact match
        dp[i][j] = dp[i - 1][j - 1];
      }
    }
  }

  return dp[m][n];
}

```

// Test Cases:
// Input: s = "aa", p = "a"
// Output: false
// Explanation: 'a' does not match entire string "aa"

// Input: s = "aa", p = "*"
// Output: true
// Explanation: '*' matches any sequence

// Input: s = "cb", p = "?a"
// Output: false
// Explanation: '?' matches 'c', but 'a' does not match 'b'

// Input: s = "adceb", p = "*a*b"
// Output: true

```

**Time Complexity:** O(m × n) - Fill DP table
**Space Complexity:** O(m × n) - DP table (can optimize to O(min(m,n)))

## Q177. ➕ Subset Sum

**Problem:** Given an array of non-negative integers `nums` and a target integer `target`, determine if there is a subset of `nums` that sums to exactly `target`. Each element can be used at most once.

**Approach:** Use boolean DP with 0-1 knapsack pattern. Iterate backwards on target to ensure each number used once. dp[target] = true if target is achievable.

### Solution 1: Boolean DP (0-1 Knapsack) (Optimal)

```javascript

function subsetSum(nums, target) {
  const dp = new Array(target + 1).fill(false);
  dp[0] = true;  // Base case: sum 0 always achievable

  for (const num of nums) {
    // Iterate backwards to avoid using same number twice
    for (let t = target; t >= num; t--) {
      dp[t] = dp[t] || dp[t - num];
    }
  }

  return dp[target];
}

```

// Test Cases:
// Input: nums = [3, 34, 4, 12, 5, 2], target = 9
// Output: true
// Explanation: Subset [4, 5] sums to 9

// Input: nums = [3, 34, 4, 12, 5, 2], target = 30
// Output: false

// Input: nums = [1, 2, 3], target = 5
// Output: true
// Explanation: Subset [2, 3] sums to 5

// Input: nums = [1], target = 1
// Output: true

```

**Time Complexity:** O(n × target) - n numbers, target values
**Space Complexity:** O(target) - DP array

## Q178. 💡 Unbounded Knapsack

**Problem:** Given a knapsack with capacity `W` and `n` items, each with weight `wt[i]` and value `val[i]`, determine the maximum value that can be obtained. Unlike 0-1 knapsack, each item can be used unlimited times.

**Approach:** Use dynamic programming with forward iteration on weight. Forward iteration allows reusing items. dp[w] = max(dp[w], dp[w - wt[i] + val[i]).

### Solution 1: Forward Iteration DP (Optimal)

```javascript
function unboundedKnapsack(W, wt, val) {
  const dp = new Array(W + 1).fill(0);

  // For each item
  for (let i = 0; i < wt.length; i++) {
    // Forward iteration allows reuse
    for (let w = wt[i]; w <= W; w++) {
      dp[w] = Math.max(dp[w], dp[w - wt[i] + val[i]);
    }
  }

  return dp[W];
}

```

// Test Cases:
// Input: W = 100, wt = [1, 50], val = [1, 30]
// Output: 100
// Explanation: Take 100 items of weight 1 (value 1 each) = 100

// Input: W = 8, wt = [3, 2, 5], val = [10, 7, 15]
// Output: 28
// Explanation: Take 4 items of weight 2 (value 7 each) = 28

// Input: W = 10, wt = [5], val = [10]
// Output: 20
// Explanation: Take 2 items of weight 5 (value 10 each) = 20

```

**Time Complexity:** O(n × W) - n items, W capacity
**Space Complexity:** O(W) - DP array

## Q179. ⬆️ ⬆️ ⬆️ Maximal Rectangle

**Problem:** Given a rows x cols binary `matrix` filled with `0`'s and `1`'s, find the largest rectangle containing only `1`'s and return its area.

**Approach:** For each row, build a histogram of consecutive `1`'s from top. Use largest rectangle in histogram algorithm (monotonic stack) to find maximum area for each row.

### Solution 1: Histogram + Monotonic Stack (Optimal)

```javascript

function maximalRectangle(matrix) {
  if (!matrix.length || !matrix[0].length) return 0;

  const m = matrix.length;
  const n = matrix[0].length;
  const heights = new Array(n).fill(0);
  let maxArea = 0;

  // Largest rectangle in histogram
  function largestRectangleArea(heights) {
    const stack = [];
    const arrWithSentinel = [...heights, 0];
    let maxArea = 0;

    for (let i = 0; i < arrWithSentinel.length; i++) {
      while (stack.length && arrWithSentinel[i] < arrWithSentinel[stack[stack.length - 1]) {
        const height = arrWithSentinel[stack.pop()];
        const left = stack.length ? stack[stack.length - 1] + 1 : 0;
        maxArea = Math.max(maxArea, height * (i - left));
      }
      stack.push(i);
    }

    return maxArea;
  }

  // For each row, build histogram and find max area
  for (let row = 0; row < m; row++) {
    for (let col = 0; col < n; col++) {
      heights[col] = matrix[row][col] === '1' ? heights[col] + 1 : 0;
    }
    maxArea = Math.max(maxArea, largestRectangleArea(heights));
  }

  return maxArea;
}

```

// Test Cases:
// Input: matrix = ["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]
// Output: 6
// Explanation: Maximal rectangle has area 6

// Input: matrix = ["0"]
// Output: 0

// Input: matrix = ["1"]
// Output: 1

// Input: matrix = ["1","1"],["1","1"]
// Output: 4

```

**Time Complexity:** O(m × n) - Build histogram for each row, stack operations O(n)
**Space Complexity:** O(n) - Heights array and stack

## Q180. 💡 Trapping Rain Water

**Problem:** Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

**Approach:** Precompute leftMax and rightMax arrays. Water trapped at position i = min(leftMax[i], rightMax[i]) - height[i].

### Solution 1: Precompute Arrays (DP) (Optimal)

```javascript
function trap(height) {
  const n = height.length;
  if (n === 0) return 0;

  const leftMax = new Array(n);
  const rightMax = new Array(n);

  // Compute leftMax: maximum height from left
  leftMax[0] = height[0];
  for (let i = 1; i < n; i++) {
    leftMax[i] = Math.max(leftMax[i - 1], height[i]);
  }

  // Compute rightMax: maximum height from right
  rightMax[n - 1] = height[n - 1];
  for (let i = n - 2; i >= 0; i--) {
    rightMax[i] = Math.max(rightMax[i + 1], height[i]);
  }

  // Calculate trapped water
  let water = 0;
  for (let i = 0; i < n; i++) {
    water += Math.min(leftMax[i], rightMax[i]) - height[i];
  }

  return water;
}

```

### Solution 2: Two Pointers (Space Optimized)

```javascript
function trap(height) {
  let left = 0, right = height.length - 1;
  let leftMax = 0, rightMax = 0;
  let water = 0;

  while (left < right) {
    if (height[left] < height[right]) {
      if (height[left] >= leftMax) {
        leftMax = height[left];
      } else {
        water += leftMax - height[left];
      }
      left++;
    } else {
      if (height[right] >= rightMax) {
        rightMax = height[right];
      } else {
        water += rightMax - height[right];
      }
      right--;
    }
  }

  return water;
}

```

// Test Cases:
// Input: height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
// Output: 6
// Explanation: Trapped water units = 6

// Input: height = [4, 2, 0, 3, 2, 5]
// Output: 9

// Input: height = [1, 0, 1]
// Output: 1

// Input: height = [3, 0, 2, 0, 4]
// Output: 7

```

**Time Complexity:** O(n) - Single pass for precompute, single pass for calculation
**Space Complexity:** O(n) with precompute, O(1) with two pointers

## Q181. 💡 Super Egg Drop

**Problem:** You are given `k` identical eggs and you have access to a building with `n` floors labeled from `1` to `n`. You know that there exists a floor `f` where `0 <= f <= n` such that any egg dropped at a floor higher than `f` will break, and any egg dropped at or below floor `f` will not break. Each move, you may take an unbroken egg and drop it from any floor `x` (where `1 <= x <= n`). If the egg breaks, you can no longer use it. However, if the egg does not break, you may reuse it in future moves. Return the minimum number of moves that you need to determine with certainty what the value of `f` is.

**Approach:** Use optimized DP. Instead of dp[k][m] = floors solvable, use dp[k] = floors solvable with current moves. Increase moves until dp[k] >= n.

### Solution 1: Optimized DP (Optimal)

```javascript

function superEggDrop(k, n) {
  const dp = new Array(k + 1).fill(0);
  let moves = 0;

  while (dp[k] < n) {
    moves++;
    // Update backwards to use previous values
    for (let eggs = k; eggs >= 1; eggs--) {
      // dp[eggs] = floors solvable with eggs eggs and moves moves
      // = floors if egg breaks + floors if egg doesn't break + current floor
      dp[eggs] = dp[eggs] + dp[eggs - 1] + 1;
    }
  }

  return moves;
}

```

// Test Cases:
// Input: k = 1, n = 2
// Output: 2
// Explanation: With 1 egg, need 2 moves to find the critical floor

// Input: k = 2, n = 6
// Output: 3

// Input: k = 3, n = 14
// Output: 4

// Input: k = 2, n = 1
// Output: 1

```

**Time Complexity:** O(k × m) - m moves, k eggs (m << n typically)
**Space Complexity:** O(k) - DP array

## Q182. 📐 Matrix Chain Multiplication

**Problem:** Given an array `p` of `n` integers representing the dimensions of `n-1` matrices such that matrix `Ai` has dimensions `p[i-1] × p[i]`, find the minimum number of scalar multiplications needed to compute the product of all matrices.

**Approach:** Use interval DP. For each interval, try all possible split points and take minimum cost. dp[i][j] = minimum cost to multiply matrices from i to j.

### Solution 1: Interval DP (Optimal)

```javascript
function matrixChainMultiplication(p) {
  const n = p.length - 1;  // Number of matrices
  const dp = Array.from({ length: n }, () => Array(n).fill(0));

  // Length of chain
  for (let len = 2; len <= n; len++) {
    // Starting index
    for (let i = 0; i + len - 1 < n; i++) {
      const j = i + len - 1;
      dp[i][j] = Infinity;

      // Try all split points
      for (let k = i; k < j; k++) {
        // Cost = cost of left chain + cost of right chain + cost of multiplying them
        const cost = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1];
        dp[i][j] = Math.min(dp[i][j], cost);
      }
    }
  }

  return dp[0][n - 1];
}

```

// Test Cases:
// Input: p = [1, 2, 3, 4, 3]
// Output: 30
// Explanation: Optimal parenthesization: ((A1(A2A3))A4) requires 30 multiplications

// Input: p = [10, 20, 30, 40, 30]
// Output: 30000

// Input: p = [40, 20, 30, 10, 30]
// Output: 26000

// Input: p = [1, 2, 3]
// Output: 6

```

**Time Complexity:** O(n³) - Three nested loops
**Space Complexity:** O(n²) - DP table

## Q183. ⬇️ ⬇️ ⬇️ Min Cost Climbing Stairs

**Problem:** You are given an integer array `cost` where `cost[i]` is the cost of `i`th step on a staircase. Once you pay the cost, you can either climb one or two steps. You can either start from the step with index `0`, or the step with index `1`. Return the minimum cost to reach the top of the floor (beyond the last index).

**Approach:** Use dynamic programming similar to Climbing Stairs, but include cost. dp[i] = minimum cost to reach step i. Can start from step 0 or 1 (both cost 0).

### Solution 1: DP Array (Optimal)

```javascript

function minCostClimbingStairs(cost) {
  const n = cost.length;
  const dp = new Array(n + 1).fill(0);
  dp[0] = 0;  // Can start from step 0
  dp[1] = 0;  // Can start from step 1

  for (let i = 2; i <= n; i++) {
    // Min cost to reach step i = min of:
    // - Coming from step i-1: dp[i-1] + cost[i-1]
    // - Coming from step i-2: dp[i-2] + cost[i-2]
    dp[i] = Math.min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]);
  }

  return dp[n];
}

```

### Solution 2: Space-Optimized

```javascript

function minCostClimbingStairs(cost) {
  let prev2 = 0;  // Cost to reach step 0
  let prev1 = 0;  // Cost to reach step 1

  for (let i = 2; i <= cost.length; i++) {
    const curr = Math.min(prev1 + cost[i - 1], prev2 + cost[i - 2]);
    prev2 = prev1;
    prev1 = curr;
  }

  return prev1;
}

```

// Test Cases:
// Input: cost = [10, 15, 20]
// Output: 15
// Explanation: Start at index 1 (cost 15), go to top (total 15)

// Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
// Output: 6
// Explanation: Start at index 0, skip 100s, pay minimum cost

// Input: cost = [10, 15]
// Output: 10

// Input: cost = [0, 0, 0, 0]
// Output: 0

```

**Time Complexity:** O(n) - Single pass through steps
**Space Complexity:** O(n) with DP array, O(1) with optimization

## Q184. 💰 Best Time to Buy and Sell Stock with Cooldown

**Problem:** You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day. Find the maximum profit you can achieve. You may complete as many transactions as you like (buy one and sell one share of the stock multiple times) with the following constraints:

- After you sell your stock, you cannot buy stock on the next day (cooldown period).

**Approach:** Track two states: `hold` (holding stock) and `cash` (not holding stock). With cooldown, when buying, use cash from 2 days ago.

### Solution 1: State DP (Optimal)

```javascript
function maxProfit(prices) {
  if (prices.length === 0) return 0;

  const n = prices.length;
  const hold = new Array(n + 1).fill(0);
  const cash = new Array(n + 1).fill(0);

  hold[0] = -Infinity;  // Cannot hold stock initially
  cash[0] = 0;          // No cash initially

  for (let i = 1; i <= n; i++) {
    // cash[i] = max of: keep cash or sell stock
    cash[i] = Math.max(cash[i - 1], hold[i - 1] + prices[i - 1]);
    // hold[i] = max of: keep holding or buy (with cooldown: use cash[i-2])
    hold[i] = Math.max(hold[i - 1], (i >= 2 ? cash[i - 2] : 0) - prices[i - 1]);
  }

  return cash[n];
}

```

// Test Cases:
// Input: prices = [1, 2, 3, 0, 2]
// Output: 3
// Explanation: Buy on day 1 (price 1), sell on day 2 (price 2), cooldown, buy on day 4 (price 0), sell on day 5 (price 2)
// Profit: (2-1) + (2-0) = 3

// Input: prices = [1]
// Output: 0

// Input: prices = [1, 2, 4]
// Output: 3
// Explanation: Buy on day 1 (price 1), sell on day 3 (price 4), profit = 3

// Input: prices = [3, 3, 5, 0, 0, 3, 1, 4]
// Output: 6

```

**Time Complexity:** O(n) - Single pass through prices
**Space Complexity:** O(n) - DP arrays (can optimize to O(1))

## Q185. 💡 Word Break

**Problem:** Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words. Note that the same word in the dictionary may be reused multiple times in the segmentation.

**Approach:** Use dynamic programming. dp[i] = true if s[0..i) can be segmented. For each position, check all possible prefixes that form valid words.

### Solution 1: DP (Optimal)

```javascript

function wordBreak(s, wordDict) {
  const wordSet = new Set(wordDict);
  const dp = new Array(s.length + 1).fill(false);
  dp[0] = true;  // Empty string can always be segmented

  for (let i = 1; i <= s.length; i++) {
    for (let j = 0; j < i; j++) {
      // Check if s[0..j) can be segmented and s[j..i) is a word
      if (dp[j] && wordSet.has(s.substring(j, i))) {
        dp[i] = true;
        break;  // Early break once found
      }
    }
  }

  return dp[s.length];
}

```

// Input: s = "leetcode", wordDict = ["leet","code"]
// Output: true
// Explanation: "leetcode" can be segmented as "leet code"

// Input: s = "applepenapple", wordDict = ["apple","pen"]
// Output: true
// Explanation: "applepenapple" can be segmented as "apple pen apple"

// Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
// Output: false
// Explanation: Cannot be segmented

```

**Time Complexity:** O(n² × m) - n string length, m average word length
**Space Complexity:** O(n) - DP array

## Q186. 💡 Triangle

**Problem:** Given a `triangle` array, return the minimum path sum from top to bottom. For each step, you may move to an adjacent number of the row below. More formally, if you are on index `i` on the current row, you may move to either index `i` or index `i + 1` on the next row.

**Approach:** Use bottom-up dynamic programming. Start from bottom row and work upward, choosing minimum from adjacent positions below.

### Solution 1: Bottom-Up DP (Optimal)

```javascript
function minimumTotal(triangle) {
  const n = triangle.length;
  // Start with bottom row
  const dp = [...triangle[n - 1];

  // Work upward
  for (let i = n - 2; i >= 0; i--) {
    for (let j = 0; j <= i; j++) {
      // Choose minimum from two adjacent positions below
      dp[j] = triangle[i][j] + Math.min(dp[j], dp[j + 1]);
    }
  }

  return dp[0];
}

```

// Input: triangle = [2],[3,4],[6,5,7],[4,1,8,3]
// Output: 11
// Explanation: Path 2 -> 3 -> 5 -> 1 = 11

// Input: triangle = [-10]
// Output: -10

// Input: triangle = [2],[3,4],[6,5,9],[4,1,8,3]
// Output: 14

```

**Time Complexity:** O(n²) - n rows, each row has n elements
**Space Complexity:** O(n) - DP array (reuses last row)

## Q187. 💡 Unique Paths II

**Problem:** You are given an `m x n` integer array `grid`. There is a robot initially located at the top-left corner (i.e., `grid[0][0]`). The robot tries to move to the bottom-right corner (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time. An obstacle and space are marked as `1` and `0` respectively in `grid`. A path that the robot takes cannot include any square that is an obstacle. Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

**Approach:** Use dynamic programming similar to Unique Paths, but skip obstacles. If a cell is an obstacle, set paths to 0.

### Solution 1: Space-Optimized DP (Optimal)

```javascript

function uniquePathsWithObstacles(obstacleGrid) {
  const m = obstacleGrid.length;
  const n = obstacleGrid[0].length;

  // Obstacle at start or end
  if (obstacleGrid[0][0] === 1 || obstacleGrid[m - 1][n - 1] === 1) return 0;

  const dp = new Array(n).fill(0);
  dp[0] = 1;  // Starting position

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (obstacleGrid[i][j] === 1) {
        dp[j] = 0;  // Obstacle: no paths
      } else if (j > 0) {
        dp[j] += dp[j - 1];  // Paths from left
      }
    }
  }

  return dp[n - 1];
}

```

// Input: obstacleGrid = [0,0,0],[0,1,0],[0,0,0]
// Output: 2
// Explanation: Two paths avoiding obstacle at (1,1)

// Input: obstacleGrid = [0,1],[0,0]
// Output: 1

// Input: obstacleGrid = [1,0]
// Output: 0

```

**Time Complexity:** O(m × n) - Visit each cell once
**Space Complexity:** O(n) - Space optimized DP array

## Q188. 🔤 Interleaving String

**Problem:** Given strings `s1`, `s2`, and `s3`, find whether `s3` is formed by an interleaving of `s1` and `s2`. An interleaving of two strings `s` and `t` is a configuration where `s` and `t` are divided into `n` and `m` non-empty substrings respectively, such that:

- `s = s1 + s2 + ... + sn`

- `t = t1 + t2 + ... + tm`

- `|n - m| <= 1`

- The interleaving is `s1 + t1 + s2 + t2 + ...` or `t1 + s1 + t2 + s2 + ...`

**Approach:** Use 2D dynamic programming. dp[i][j] = true if s1[0..i) and s2[0..j) can form s3[0..i+j).

### Solution 1: 2D DP (Optimal)

```javascript
function isInterleave(s1, s2, s3) {
  if (s1.length + s2.length !== s3.length) return false;

  const m = s1.length;
  const n = s2.length;
  const dp = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(false));
  dp[0][0] = true;  // Empty strings form empty interleaving

  // Initialize first row: s2 only
  for (let j = 1; j <= n; j++) {
    dp[0][j] = dp[0][j - 1] && s2[j - 1] === s3[j - 1];
  }

  // Initialize first column: s1 only
  for (let i = 1; i <= m; i++) {
    dp[i][0] = dp[i - 1][0] && s1[i - 1] === s3[i - 1];
  }

  // Fill DP table
  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      // Character from s1
      if (s1[i - 1] === s3[i + j - 1]) {
        dp[i][j] = dp[i][j] || dp[i - 1][j];
      }
      // Character from s2
      if (s2[j - 1] === s3[i + j - 1]) {
        dp[i][j] = dp[i][j] || dp[i][j - 1];
      }
    }
  }

  return dp[m][n];
}

```

// Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
// Output: true

// Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
// Output: false

// Input: s1 = "", s2 = "", s3 = ""
// Output: true

```

**Time Complexity:** O(m × n) - Fill DP table
**Space Complexity:** O(m × n) - DP table (can optimize to O(min(m,n)))

## Q189. 💰 Best Time to Buy and Sell Stock III

**Problem:** You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day. Find the maximum profit you can achieve with at most two transactions. You may complete at most two transactions (buy one and sell one share of the stock).

**Approach:** Track four states: buy1, sell1, buy2, sell2 representing the maximum profit after first buy, first sell, second buy, and second sell. Update states greedily to maximize profit at each transaction.

### Solution 1: State Tracking (Optimal)

```javascript

function maxProfit(prices) {
  if (prices.length === 0) return 0;

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

// Input: prices = [3,3,5,0,0,3,1,4]
// Output: 6

// Input: prices = [1,2,3,4,5]
// Output: 4

// Input: prices = [7,6,4,3,1]
// Output: 0

```

**Time Complexity:** O(n) - Single pass through prices
**Space Complexity:** O(1) - Constant extra space

---

## Q190. 💰 Best Time to Buy and Sell Stock IV

**Problem:** You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `i`th day, and an integer `k`. Find the maximum profit you can achieve with at most `k` transactions. You may complete at most `k` transactions (buy one and sell one share of the stock).

**Approach:** Use dynamic programming to track states for k transactions. If k >= n/2, treat as unlimited transactions (greedy approach). Otherwise, use DP table to track maximum profit for each transaction.

### Solution 1: Dynamic Programming (Optimal)

```javascript

function maxProfit(k, prices) {
  if (prices.length === 0 || k === 0) return 0;

  const n = prices.length;

  // If k >= n/2, can make unlimited transactions
  if (k >= Math.floor(n / 2)) {
    let profit = 0;
    for (let i = 1; i < n; i++) {
      if (prices[i] > prices[i - 1]) {
        profit += prices[i] - prices[i - 1];
      }
    }
    return profit;
  }

  const dp = Array.from({length: k + 1}, () => new Array(n).fill(0));

  for (let i = 1; i <= k; i++) {
    let maxDiff = -prices[0];
    for (let j = 1; j < n; j++) {
      dp[i][j] = Math.max(dp[i][j - 1], prices[j] + maxDiff);
      maxDiff = Math.max(maxDiff, dp[i - 1][j] - prices[j]);
    }
  }

  return dp[k][n - 1];
}

// Input: k = 2, prices = [2,4,1]
// Output: 2

// Input: k = 2, prices = [3,2,6,5,0,3]
// Output: 7

// Input: k = 0, prices = [1,2]
// Output: 0

```

**Time Complexity:** O(n×k) - Fill DP table
**Space Complexity:** O(n×k) - DP table, can optimize to O(n)

---

## Q191. ⬆️ ⬆️ ⬆️ Maximal Square

**Problem:** Given an `m x n` binary `matrix` filled with `0`'s and `1`'s, find the largest square containing only `1`'s and return its area.

**Approach:** Use dynamic programming where `dp[i][j]` represents the side length of the largest square ending at position (i,j). For each '1', take the minimum of three neighbors (top, left, top-left) plus 1 to ensure square shape.

### Solution 1: Dynamic Programming (Optimal)

```javascript

function maximalSquare(matrix) {
  if (matrix.length === 0) return 0;

  const m = matrix.length;
  const n = matrix[0].length;
  const dp = Array.from({length: m}, () => new Array(n).fill(0));
  let maxSide = 0;

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (matrix[i][j] === '1') {
        if (i === 0 || j === 0) {
          dp[i][j] = 1;
        } else {
          dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1;
        }
        maxSide = Math.max(maxSide, dp[i][j]);
      }
    }
  }

  return maxSide * maxSide;
}

// Input: matrix = ["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]
// Output: 4
// Explanation: Largest square of side 2 (area 4)

// Input: matrix = ["0","1"],["1","0"]
// Output: 1

// Input: matrix = ["0"]
// Output: 0

```

**Time Complexity:** O(m×n) - Visit each cell once
**Space Complexity:** O(m×n) - DP table, can optimize to O(n)

---

## Q192. 📋 Maximum Sum Circular Subarray

**Problem:** Given a circular integer array `nums` of length `n`, return the maximum possible sum of a non-empty subarray of `nums`. A circular array means the end of the array connects to the beginning of the array.

**Approach:** Use Kadane's algorithm for both wrapped and unwrapped cases. The maximum can be either the maximum subarray sum (unwrapped) or total sum minus minimum subarray sum (wrapped). Handle the case where all numbers are negative.

### Solution 1: Kadane's Algorithm (Optimal)

```javascript

function maxSubarraySumCircular(nums) {
  let total = 0;
  let maxSum = nums[0];
  let minSum = nums[0];
  let currMax = 0;
  let currMin = 0;

  for (const num of nums) {
    total += num;
    currMax = Math.max(currMax + num, num);
    currMin = Math.min(currMin + num, num);
    maxSum = Math.max(maxSum, currMax);
    minSum = Math.min(minSum, currMin);
  }

  return maxSum > 0 ? Math.max(maxSum, total - minSum) : maxSum;
}

// Input: nums = [1,-2,3,-2]
// Output: 3

// Input: nums = [5,-3,5]
// Output: 10
// Explanation: Maximum circular subarray sum is 10 (5 + 5)

// Input: nums = [-3,-2,-3]
// Output: -2

```

**Time Complexity:** O(n) - Single pass through array
**Space Complexity:** O(1) - Constant extra space

- **Interview Tip:** Explain two cases clearly; emphasize circular wraparound; mention Kadane's algorithm

---

## 📍 Navigation

<div align="center">

[← Previous: Graphs](08%29%20Graphs.md) • [Home: README](README.md) • [Next: Recursion & Backtracking →](10%29%20Recursion%20%26%20Backtracking.md)

[📋 Cheatsheet](DSA%20Interview%20Cheatsheet.md)

</div>
