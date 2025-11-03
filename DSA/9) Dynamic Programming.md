# Dynamic Programming

## Q116. Fibonacci (Memo & Tabulation)

Concept: Overlapping subproblems; memo recursion or bottom-up table.

```javascript
function fib(n) {
  const dp = new Array(n + 1).fill(0);
  dp[1] = 1;
  for (let i = 2; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }
  return dp[n];
}

// Test Cases:
//
// Example 1:
//   Input: n = 2
//   Output: 1
//
// Example 2:
//   Input: n = 3
//   Output: 2
//
// Example 3:
//   Input: n = 4
//   Output: 3
//
// Example 4:
//   Input: n = 10
//   Output: 55
```

Deep Insights:
  - Rule: Overlapping subproblems; memo recursion or bottom-up table; O(n) time, O(n) space (can optimize to O(1)).
  - Real-world: Fibonacci sequence, number sequences, mathematical modeling, recursive computations.
  - Common mistake: Avoid exponential naive recursion; not using memoization; forgetting base cases.
  - Optimization: Bottom-up tabulation avoids recursion overhead; space optimize to O(1); O(n) time optimal.
  - Interview tip: Explain overlapping subproblems clearly; mention memoization vs tabulation; ask about space optimization.
## Q117. Climbing Stairs

Concept: Ways(n)=Ways(n-1)+Ways(n-2) like Fibonacci.

```javascript
function climbStairs(n) {
  if (n === 1) return 1;
  let dp = new Array(n).fill(0);
  dp[0] = 1;
  dp[1] = 2;

  for (let i = 2; i < n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }

  return dp[n - 1];
}

// Test Cases:
//
// Example 1:
//   Input: n = 2
//   Output: 2
//
// Example 2:
//   Input: n = 3
//   Output: 3
//
// Example 3:
//   Input: n = 4
//   Output: 5
//
// Example 4:
//   Input: n = 5
//   Output: 8
```

Deep Insights:
  - Rule: Ways(n)=Ways(n-1)+Ways(n-2) like Fibonacci; O(n) time, O(n) space with DP array.
  - Real-world: Climbing stairs problems, step counting, path counting, recursive counting problems.
  - Common mistake: Handle n=1; forgetting base cases; not using DP for optimization.
  - Optimization: O(n) time, O(n) space with DP array; can optimize to O(1) space with two variables.
  - Interview tip: Explain recurrence relation clearly; mention Fibonacci similarity; ask about step constraints.

Time Complexity: O(n)
Space Complexity: O(n)
## Q118. Coin Change

Concept: Min coins to make amount; dp[a]=min(dp[a], dp[a- coin]+1).

```javascript
function coinChange(coins, amount) {
  const dp = new Array(amount + 1).fill(Infinity);
  dp[0] = 0;
  for (const coin of coins) {
    for (let currAmount = coin; currAmount <= amount; currAmount++) {
      dp[currAmount] = Math.min(dp[currAmount], dp[currAmount - coin] + 1);
    }
  }
  return dp[amount] === Infinity ? -1 : dp[amount];
}

// Test Cases:
//
// Example 1:
//   Input: coins = [1, 2, 5], amount = 11
//   Output: 3
//   Explanation: 11 = 5 + 5 + 1
//
// Example 2:
//   Input: coins = [2], amount = 3
//   Output: -1
//   Explanation: Cannot make amount 3 with only coin 2
//
// Example 3:
//   Input: coins = [1], amount = 0
//   Output: 0
//
// Example 4:
//   Input: coins = [1, 3, 4], amount = 6
//   Output: 2
//   Explanation: 6 = 3 + 3
```

Deep Insights:
  - Rule: Min coins to make amount; dp[a]=min(dp[a], dp[a-coin]+1); O(n×amount) time, O(amount) space.
  - Real-world: Coin change problems, payment systems, currency conversion, minimum count problems.
  - Common mistake: -1 when impossible; not handling infinity correctly; wrong coin iteration order.
  - Optimization: O(n×amount) time; space O(amount); returns -1 when impossible.
  - Interview tip: Explain DP transition clearly; mention impossible cases; ask about coin order impact.
## Q119. 0-1 Knapsack

Concept: Each item once; 1D dp backward loop on weight.

```javascript
function knap01(W, wt, val) {
  const dp = new Array(W + 1).fill(0);
  for (let i = 0; i < wt.length; i++) {
    for (let w = W; w >= wt[i]; w-- ) {
      dp[w] = Math.max(dp[w], dp[w-wt[i]] + val[i]);
    }
  }
  return dp[W];
}

// Test Cases:
//
// Example 1:
//   Input: W = 50, wt = [10, 20, 30], val = [60, 100, 120]
//   Output: 220
//   Explanation: Take items with weight 20 and 30 (value 100 + 120 = 220)
//
// Example 2:
//   Input: W = 10, wt = [5, 4, 6], val = [10, 40, 30]
//   Output: 50
//   Explanation: Take items with weight 4 and 6 (value 40 + 30 = 70) or 5 and 4 (value 10 + 40 = 50)
//
// Example 3:
//   Input: W = 8, wt = [2, 3, 4, 5], val = [1, 2, 5, 6]
//   Output: 8
//   Explanation: Take items with weight 3 and 5 (value 2 + 6 = 8)
```

Deep Insights:
  - Rule: Each item once; 1D dp backward loop on weight; dp[w]=max(dp[w], dp[w-wt[i]]+val[i]); O(n×W) time.
  - Real-world: Knapsack problems, resource allocation, optimization problems, constrained selection.
  - Common mistake: Weight bounded; value maximization; wrong loop direction (must be backward); not handling weights correctly.
  - Optimization: 1D DP backward loop saves space; O(n×W) time, O(W) space; weight bounded optimization.
  - Interview tip: Explain backward loop clearly; mention unbounded variant; ask about space optimization.
## Q120. Longest Increasing Subsequence

Concept: Patience sorting tails array; binary search replace.

```javascript
function lengthOfLIS(nums) {
  const tails = [];
  for (const num of nums) {
    let left = 0, right = tails.length;
    while (left < right) {
      const mid = (left + right) >> 1;
      if (tails[mid] < num) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }
    tails[left] = num;
  }
  return tails.length;
}

// Test Cases:
//
// Example 1:
//   Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]
//   Output: 4
//   Explanation: Longest increasing subsequence is [2, 3, 7, 101] with length 4
//
// Example 2:
//   Input: nums = [0, 1, 0, 3, 2, 3]
//   Output: 4
//   Explanation: LIS is [0, 1, 2, 3] with length 4
//
// Example 3:
//   Input: nums = [7, 7, 7, 7, 7, 7, 7]
//   Output: 1
//
// Example 4:
//   Input: nums = [1]
//   Output: 1
```

Deep Insights:
  - Rule: Patience sorting tails array; binary search replace; O(n log n) time, O(n) space.
  - Real-world: Longest increasing subsequence, sequence analysis, patience sorting, sequence optimization.
  - Common mistake: Strictly increasing; adjust for non-decreasing; wrong binary search logic; not maintaining tails array.
  - Optimization: O(n log n) time optimal; binary search for insertion; strictly increasing (adjust for non-decreasing).
  - Interview tip: Explain patience sorting clearly; mention binary search optimization; ask about strictly vs non-decreasing.
## Q121. Longest Common Subsequence

Concept: dp[i][j] = 1+dp[i-1][j-1] if match else max(top,left).

```javascript
function lcs(text1, text2) {
  const m = text1.length, n = text2.length;
  const dp = Array.from({length: m + 1}, () => new Array(n + 1).fill(0));
  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      dp[i][j] = text1[i - 1] === text2[j - 1] 
        ? dp[i - 1][j - 1] + 1 
        : Math.max(dp[i - 1][j], dp[i][j - 1]);
    }
  }
  return dp[m][n];
}

// Test Cases:
//
// Example 1:
//   Input: text1 = "abcde", text2 = "ace"
//   Output: 3
//   Explanation: LCS is "ace" with length 3
//
// Example 2:
//   Input: text1 = "abc", text2 = "abc"
//   Output: 3
//   Explanation: LCS is "abc" with length 3
//
// Example 3:
//   Input: text1 = "abc", text2 = "def"
//   Output: 0
//
// Example 4:
//   Input: text1 = "bl", text2 = "yby"
//   Output: 1
```

Deep Insights:
  - Rule: dp[i][j] = 1+dp[i-1][j-1] if match else max(top,left); O(mn) time, O(mn) space.
  - Real-world: Longest common subsequence, string comparison, diff algorithms, sequence alignment.
  - Common mistake: Backtrack to get sequence; wrong DP transition; forgetting base cases; off-by-one errors.
  - Optimization: O(mn) time optimal; space optimize to O(min(m,n)); backtrack to get sequence if needed.
  - Interview tip: Explain DP transition clearly; mention backtracking for sequence; ask about space optimization.
## Q122. Edit Distance

Concept: Levenshtein: insert/delete/replace costs; classic 2D DP.

```javascript
function minDistance(word1, word2) {
  const m = word1.length;
  const n = word2.length;
  const dp = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));

  for (let i = 0; i <= m; i++) {
    dp[i][0] = i;
  }
  for (let j = 0; j <= n; j++) {
    dp[0][j] = j;
  }

  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      dp[i][j] = word1[i - 1] === word2[j - 1]
        ? dp[i - 1][j - 1]
        : 1 + Math.min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]);
    }
  }
  return dp[m][n];
}

// Test Cases:
//
// Example 1:
//   Input: word1 = "horse", word2 = "ros"
//   Output: 3
//   Explanation: horse -> rorse (replace 'h' with 'r'), rorse -> rose (remove 'r'), rose -> ros (remove 'e')
//
// Example 2:
//   Input: word1 = "intention", word2 = "execution"
//   Output: 5
//
// Example 3:
//   Input: word1 = "", word2 = "a"
//   Output: 1
//
// Example 4:
//   Input: word1 = "abc", word2 = "abc"
//   Output: 0
```

Deep Insights:
  - Rule: Levenshtein: insert/delete/replace costs; classic 2D DP; if match dp[i][j] = dp[i-1][j-1] else min + 1.
  - Real-world: Edit distance problems, spell checkers, diff algorithms, string similarity.
  - Common mistake: Operations symmetric except costs; base rows/cols are edits from/to empty; wrong operation costs.
  - Optimization: O(mn) time; space optimize to O(min(m,n)); operations symmetric except costs.
  - Interview tip: Explain three operations clearly; mention base cases; ask about operation costs.
## Q123. Rod Cutting

Concept: Unbounded knapsack on length; best price per length.

```javascript
function rodCut(price, rodLength) {
  const dp = new Array(rodLength + 1).fill(0);
  for (let i = 1; i <= rodLength; i++) {
    for (let len = 1; len <= i; len++) {
      dp[i] = Math.max(dp[i], price[len - 1] + dp[i - len]);
    }
  }
  return dp[rodLength];
}

// Test Cases:
//
// Example 1:
//   Input: price = [1, 5, 8, 9, 10, 17, 17, 20], n = 8
//   Output: 22
//   Explanation: Cut into pieces of length 2 and 6: 5 + 17 = 22
//
// Example 2:
//   Input: price = [1, 5, 8], n = 3
//   Output: 8
//   Explanation: Best is to keep rod uncut: price[3] = 8
//
// Example 3:
//   Input: price = [3, 5, 8], n = 3
//   Output: 9
//   Explanation: Cut into pieces of length 1+1+1: 3*3 = 9
//
// Example 4:
//   Input: price = [1], n = 1
//   Output: 1
```

Deep Insights:
  - Rule: Unbounded knapsack on length; best price per length; dp[i]=max(dp[i], price[len-1]+dp[i-len]); O(n^2) time.
  - Real-world: Rod cutting problems, unbounded knapsack, resource optimization, pricing problems.
  - Common mistake: Track cuts to reconstruct; wrong DP transition; not handling unbounded correctly.
  - Optimization: O(n^2) time; unbounded allows repeated cuts; track cuts to reconstruct if needed.
  - Interview tip: Explain unbounded vs 0-1 knapsack clearly; mention reconstruction; ask about optimization.
## Q124. Partition Equal Subset Sum

Concept: Can we reach sum=total/2 via subset? 1D boolean DP.

```javascript
function canPartition(nums) {
  const sum = nums.reduce((acc, num) => acc + num, 0);
  if (sum % 2) return false;
  const target = sum >> 1;
  const dp = new Array(target + 1).fill(false);
  dp[0] = true;
  for (const num of nums) {
    for (let j = target; j >= num; j--) {
      dp[j] = dp[j] || dp[j - num];
    }
  }
  return dp[target];
}

// Test Cases:
//
// Example 1:
//   Input: nums = [1, 5, 11, 5]
//   Output: true
//   Explanation: Can partition into [1, 5, 5] and [11] (both sum to 11)
//
// Example 2:
//   Input: nums = [1, 2, 3, 5]
//   Output: false
//   Explanation: Total sum is 11 (odd), cannot partition equally
//
// Example 3:
//   Input: nums = [1, 2, 3, 4]
//   Output: true
//   Explanation: Can partition into [1, 4] and [2, 3] (both sum to 5)
//
// Example 4:
//   Input: nums = [1, 1]
//   Output: true
```

Deep Insights:
  - Rule: Can we reach sum=total/2 via subset? 1D boolean DP; dp[j] = dp[j] || dp[j-x]; O(n×sum/2) time.
  - Real-world: Partition problems, subset sum problems, equal partition, balanced partitioning.
  - Common mistake: O(n×sum/2) time; exact half only; wrong loop direction (must be backward); not handling odd sum.
  - Optimization: Backward loop for 0-1 knapsack pattern; O(n×sum/2) time; exact half only.
  - Interview tip: Explain subset sum clearly; mention 0-1 knapsack similarity; ask about odd sum.
## Q125. House Robber

Concept: dp[i] = max(dp[i-1], dp[i-2]+nums[i]).

```javascript
function rob(nums) {
  if (nums.length === 0) return 0;
  if (nums.length === 1) return nums[0];
  
  const dp = new Array(nums.length).fill(0);
  dp[0] = nums[0];
  dp[1] = Math.max(nums[0], nums[1]);
  
  for (let i = 2; i < nums.length; i++) {
    dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i]);
  }
  
  return dp[nums.length - 1];
}

// Test Cases:
//
// Example 1:
//   Input: nums = [1, 2, 3, 1]
//   Output: 4
//   Explanation: Rob houses 1 and 3 (1 + 3 = 4)
//
// Example 2:
//   Input: nums = [2, 7, 9, 3, 1]
//   Output: 12
//   Explanation: Rob houses 1, 3, and 5 (2 + 9 + 1 = 12)
//
// Example 3:
//   Input: nums = [2, 1, 1, 2]
//   Output: 4
//   Explanation: Rob houses 1 and 4 (2 + 2 = 4)
//
// Example 4:
//   Input: nums = [1]
//   Output: 1
//
// Example 5:
//   Input: nums = []
//   Output: 0
```

Deep Insights:
  - Rule: dp[i] = max(dp[i-1], dp[i-2]+nums[i]); track include/exclude; O(n) time, O(n) space.
  - Real-world: House robber problems, non-adjacent selection, optimization with constraints, selection problems.
  - Common mistake: Adjacent constraint; negative values unusual; wrong DP transition; not handling empty array.
  - Optimization: O(n) time, O(n) space with DP array; can optimize to O(1) space; track include/exclude; adjacent constraint enforced.
  - Interview tip: Explain include/exclude clearly; mention adjacent constraint; ask about circular variant.

Time Complexity: O(n)
Space Complexity: O(n)
## Q126. House Robber II

Concept: Circle → rob max of linear(0..n-2) or linear(1..n-1).

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
//
// Example 1:
//   Input: nums = [2, 3, 2]
//   Output: 3
//   Explanation: Rob house 2 (index 1) since houses are arranged in a circle
//
// Example 2:
//   Input: nums = [1, 2, 3, 1]
//   Output: 4
//   Explanation: Rob houses 1 and 3 (excluding last or first)
//
// Example 3:
//   Input: nums = [1, 2, 3]
//   Output: 3
//   Explanation: Rob house 3 (excluding first or last)
//
// Example 4:
//   Input: nums = [1]
//   Output: 1
```

Deep Insights:
  - Rule: Circle → rob max of linear(0..n-2) or linear(1..n-1); same recurrence as Rob I; O(n) time.
  - Real-world: Circular house robber, circular constraints, wrap-around problems, cyclic optimization.
  - Common mistake: Same recurrence as Rob I; not handling circular correctly; forgetting to exclude last or first.
  - Optimization: O(n) time, O(n) space with DP array; solve two linear cases; take maximum; same recurrence as Rob I.
  - Interview tip: Explain circular handling clearly; mention two linear cases; ask about wrap-around logic.

Time Complexity: O(n)
Space Complexity: O(n)
## Q127. Decode Ways

Concept: dp[i]=ways up to i; use one/two- digit valid decodes.

```javascript
function numDecodings(s) {
  if (!s || s[0] === '0') return 0;
  
  const dp = new Array(s.length + 1).fill(0);
  dp[0] = 1;
  dp[1] = 1;
  
  for (let i = 2; i <= s.length; i++) {
    const oneDigit = s[i - 1] !== '0';
    const twoDigits = s[i - 2] !== '0' && Number(s.slice(i - 2, i)) <= 26;
    
    if (oneDigit) {
      dp[i] += dp[i - 1];
    }
    if (twoDigits) {
      dp[i] += dp[i - 2];
    }
    
    if (dp[i] === 0) return 0;
  }
  
  return dp[s.length];
}

// Test Cases:
//
// Example 1:
//   Input: s = "12"
//   Output: 2
//   Explanation: "12" can be decoded as "AB" (1 2) or "L" (12)
//
// Example 2:
//   Input: s = "226"
//   Output: 3
//   Explanation: "226" can be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6)
//
// Example 3:
//   Input: s = "06"
//   Output: 0
//   Explanation: Invalid encoding (no leading zeros allowed)
//
// Example 4:
//   Input: s = "0"
//   Output: 0
//
// Example 5:
//   Input: s = "27"
//   Output: 1
//   Explanation: "27" can only be decoded as "BG" (2 7)
```

Deep Insights:
  - Rule: dp[i]=ways up to i; use one/two-digit valid decodes; O(n) time, O(n) space.
  - Real-world: Decode ways problems, string decoding, valid sequence counting, encoding validation.
  - Common mistake: Digit check <=26 and not leading zero; early return when dead; wrong validity checking.
  - Optimization: O(n) time, O(n) space with DP array; can optimize to O(1) space; digit check <=26 and not leading zero.
  - Interview tip: Explain validity checks clearly; mention early return; ask about edge cases.

Time Complexity: O(n)
Space Complexity: O(n)
## Q128. DP on Grid — Min Path / Unique Paths

Concept: Grid DP with from-top/from-left transitions (blockers optional).

```javascript
function minPathSum(g) {
  const m = g.length;
  const n = g[0].length;
  const dp = new Array(n).fill(0);
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      dp[j] = g[i][j] + Math.min(
        j ? dp[j - 1] : Infinity,
        i ? dp[j] : Infinity
      );
    }
  }
  return dp[n - 1];
}

function uniquePaths(m, n) {
  const dp = new Array(n).fill(1);
  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      dp[j] += dp[j - 1];
    }
  }
  return dp[n - 1];
}

// Test Cases:
//
// minPathSum:
// Example 1:
//   Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
//   Output: 7
//   Explanation: Path 1 -> 3 -> 1 -> 1 -> 1 has minimum sum = 7
//
// Example 2:
//   Input: grid = [[1,2,3],[4,5,6]]
//   Output: 12
//   Explanation: Path 1 -> 2 -> 3 -> 6 has minimum sum = 12
//
// uniquePaths:
// Example 1:
//   Input: m = 3, n = 7
//   Output: 28
//
// Example 2:
//   Input: m = 3, n = 2
//   Output: 3
//
// Example 3:
//   Input: m = 7, n = 3
//   Output: 28
//
// Example 4:
//   Input: m = 3, n = 3
//   Output: 6
```

Deep Insights:
  - Rule: Grid DP with from-top/from-left transitions; minPathSum: minimize path; uniquePaths: count paths; O(mn) time.
  - Real-world: Grid path problems, path finding in grids, shortest paths, path counting.
  - Common mistake: O(mn) time; not handling blockers correctly; wrong boundary initialization; forgetting blockers.
  - Optimization: O(mn) time; space optimize to O(min(m,n)); handle blockers in transitions.
  - Interview tip: Explain grid DP clearly; mention blockers; ask about space optimization.
## Q129. Palindromic Substrings

Concept: Expand around centers O(n^2) to count palindromes.

```javascript
function countSubstrings(s) {
  let ans = 0;
  const expandPalindrome = (left, right) => {
    while (left >= 0 && right < s.length && s[left] === s[right]) {
      ans++;
      left--;
      right++;
    }
  };
  for (let i = 0; i < s.length; i++) {
    expandPalindrome(i, i);
    expandPalindrome(i, i + 1);
  }
  return ans;
}

// Test Cases:
//
// Example 1:
//   Input: s = "abc"
//   Output: 3
//   Explanation: Three palindromic strings: "a", "b", "c"
//
// Example 2:
//   Input: s = "aaa"
//   Output: 6
//   Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa"
//
// Example 3:
//   Input: s = "racecar"
//   Output: 10
//
// Example 4:
//   Input: s = ""
//   Output: 0
//
// Example 5:
//   Input: s = "a"
//   Output: 1
```

Deep Insights:
  - Rule: Expand around centers O(n^2) to count palindromes; O(n^2) time, O(1) space.
  - Real-world: Palindromic substring counting, palindrome detection, string analysis.
  - Common mistake: Works for empty as 0; wrong expansion logic; not handling odd/even centers correctly.
  - Optimization: O(n^2) time; O(1) space; expand around 2n-1 centers; works for empty as 0.
  - Interview tip: Explain expansion clearly; mention odd/even centers; ask about longest variant.
## Q130. Burst Balloons

Concept: Interval DP; dp[l][r] = best bursting (l,r) with last balloon k.

```javascript
function maxCoins(nums) {
  const arr = [1, ...nums, 1];
  const n = arr.length;
  const dp = Array.from({length: n}, () => Array(n).fill(0));
  
  for (let len = 2; len < n; len++) {
    for (let left = 0; left + len < n; left++) {
      const right = left + len;
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

// Test Cases:
//
// Example 1:
//   Input: nums = [3, 1, 5, 8]
//   Output: 167
//   Explanation: nums = [3,1,5,8] -> [3,5,8] -> [3,8] -> [8] -> []
//                coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 15 + 120 + 24 + 8 = 167
//
// Example 2:
//   Input: nums = [1, 5]
//   Output: 10
//   Explanation: Burst 1 first: coins = 1*1*5 = 5, then burst 5: coins = 1*5*1 = 5. Total = 10
//
// Example 3:
//   Input: nums = [7]
//   Output: 7
//
// Example 4:
//   Input: nums = [1, 2, 3, 4]
//   Output: 40
```

Deep Insights:
  - Rule: Interval DP; dp[l][r] = best bursting (l,r) with last balloon k; O(n^3) time, O(n^2) space.
  - Real-world: Burst balloons problems, interval DP, optimization problems, game theory.
  - Common mistake: Classic interval DP; wrong interval length handling; not tracking last balloon correctly.
  - Optimization: O(n^3) time for n balloons; O(n^2) space; classic interval DP pattern.
  - Interview tip: Explain interval DP clearly; mention last balloon choice; ask about DP order.
## Q131. Job Scheduling

Concept: Sort by end time; dp[i]=max(profit up to i, profit[i]+dp[prevNonOverlap]).

```javascript
function jobScheduling(start, end, profit) {
  const n = start.length;
  const jobs = [];
  for (let i = 0; i < n; i++) {
    jobs.push([start[i], end[i], profit[i]]);
  }
  jobs.sort((a, b) => a[1] - b[1]);
  const ends = jobs.map(job => job[1]);
  const dp = new Array(n).fill(0);
  
  for (let i = 0; i < n; i++) {
    const [startTime, endTime, profitVal] = jobs[i];
    let left = 0, right = i - 1, pos = -1;
    while (left <= right) {
      const mid = (left + right) >> 1;
      if (ends[mid] <= startTime) {
        pos = mid;
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
    dp[i] = Math.max(i ? dp[i - 1] : 0, profitVal + (pos >= 0 ? dp[pos] : 0));
  }
  return dp[n - 1];
}

// Test Cases:
//
// Example 1:
//   Input: startTime = [1, 2, 3, 3], endTime = [3, 4, 5, 6], profit = [50, 10, 40, 70]
//   Output: 120
//   Explanation: Take jobs with indices 0 and 3 (profit 50 + 70 = 120)
//
// Example 2:
//   Input: startTime = [1, 2, 3, 4, 6], endTime = [3, 5, 10, 6, 9], profit = [20, 20, 100, 70, 60]
//   Output: 150
//
// Example 3:
//   Input: startTime = [1, 1, 1], endTime = [2, 3, 4], profit = [5, 6, 4]
//   Output: 6
```

Deep Insights:
  - Rule: Sort by end time; dp[i]=max(profit up to i, profit[i]+dp[prevNonOverlap]); O(n log n) time.
  - Real-world: Weighted interval scheduling, job scheduling, resource allocation, optimization problems.
  - Common mistake: Binary search for previous non-overlap; sort by end time; wrong DP transition.
  - Optimization: O(n log n) for sorting + O(n log n) for binary search; weighted interval scheduling.
  - Interview tip: Explain binary search clearly; mention sorting by end time; ask about overlap handling.
## Q132. Wildcard Matching

Concept: DP over i,j with '*' matching any sequence and '?' any char.

```javascript
function isMatch(s, p) {
  const m = s.length, n = p.length;
  const dp = Array.from({length: m + 1}, () => Array(n + 1).fill(false));
  dp[0][0] = true;
  
  for (let j = 1; j <= n; j++) {
    if (p[j - 1] === '*') dp[0][j] = dp[0][j - 1];
  }
  
  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      dp[i][j] = p[j - 1] === '*'
        ? dp[i][j - 1] || dp[i - 1][j]
        : (p[j - 1] === '?' || p[j - 1] === s[i - 1]) && dp[i - 1][j - 1];
    }
  }
  return dp[m][n];
}

// Test Cases:
//
// Example 1:
//   Input: s = "aa", p = "a"
//   Output: false
//   Explanation: 'a' does not match entire string "aa"
//
// Example 2:
//   Input: s = "aa", p = "*"
//   Output: true
//   Explanation: '*' matches any sequence
//
// Example 3:
//   Input: s = "cb", p = "?a"
//   Output: false
//   Explanation: '?' matches 'c', but 'a' does not match 'b'
//
// Example 4:
//   Input: s = "adceb", p = "*a*b"
//   Output: true
```

Deep Insights:
  - Rule: DP over i,j with '*' matching any sequence and '?' any char; dp[i][j] = '*' ? dp[i][j-1] || dp[i-1][j] : match && dp[i-1][j-1].
  - Real-world: Wildcard matching, pattern matching, string matching, glob patterns.
  - Common mistake: Greedy two-pointer alternative exists; careful with multiple '*'; wrong DP transition.
  - Optimization: O(mn) time, O(mn) space; greedy two-pointer alternative exists; careful with multiple '*'.
  - Interview tip: Explain wildcard matching clearly; mention greedy alternative; ask about multiple '*' handling.
## Q133. Subset Sum

Concept: Classic boolean DP to target sum using 0-1 items.

```javascript
function subsetSum(nums, target) {
  const dp = new Array(target + 1).fill(false);
  dp[0] = true;
  for (const x of nums) {
    for (let t = target; t >= x; t-- ) {
      dp[t] = dp[t] || dp[t -x];
    }
  }
  return dp[target];
}

// Test Cases:
//
// Example 1:
//   Input: nums = [3, 34, 4, 12, 5, 2], target = 9
//   Output: true
//   Explanation: Subset [4, 5] sums to 9
//
// Example 2:
//   Input: nums = [3, 34, 4, 12, 5, 2], target = 30
//   Output: false
//
// Example 3:
//   Input: nums = [1, 2, 3], target = 5
//   Output: true
//   Explanation: Subset [2, 3] sums to 5
//
// Example 4:
//   Input: nums = [1], target = 1
//   Output: true
```

Deep Insights:
  - Rule: Classic boolean DP to target sum using 0-1 items; dp[t] = dp[t] || dp[t-x]; O(n×target) time.
  - Real-world: Subset sum problems, target sum queries, boolean knapsack, selection problems.
  - Common mistake: Early break if dp[target] true; wrong loop direction (must be backward); not handling target correctly.
  - Optimization: Backward loop for 0-1 knapsack; O(n×target) time; early break if dp[target] true.
  - Interview tip: Explain subset sum clearly; mention 0-1 knapsack similarity; ask about early termination.
## Q134. Unbounded Knapsack

Concept: Items unlimited; forward loop on weight to allow reuse.

```javascript
function unboundedKnapsack(W, wt, val) {
  const dp = new Array(W + 1).fill(0);
  for (let i = 0; i < wt.length; i++) {
    for (let w = wt[i]; w <= W; w++) {
      dp[w] = Math.max(dp[w], dp[w - wt[i]] + val[i]);
    }
  }
  return dp[W];
}

// Test Cases:
//
// Example 1:
//   Input: W = 100, wt = [1, 50], val = [1, 30]
//   Output: 100
//   Explanation: Take 100 items of weight 1 (value 1 each) = 100
//
// Example 2:
//   Input: W = 8, wt = [3, 2, 5], val = [10, 7, 15]
//   Output: 28
//   Explanation: Take 4 items of weight 2 (value 7 each) = 28
//
// Example 3:
//   Input: W = 10, wt = [5], val = [10]
//   Output: 20
//   Explanation: Take 2 items of weight 5 (value 10 each) = 20
```

Deep Insights:
  - Rule: Items unlimited; forward loop on weight to allow reuse; dp[w] = max(dp[w], dp[w-wt[i]]+val[i]); O(n×W) time.
  - Real-world: Unbounded knapsack, resource allocation, repeated item selection, optimization problems.
  - Common mistake: Items infinite; wrong loop direction (must be forward); not allowing reuse correctly.
  - Optimization: Forward loop allows reuse; O(n×W) time; items infinite.
  - Interview tip: Explain unbounded vs 0-1 clearly; mention forward loop; ask about item limits.
## Q135. Maximum Rectangle

Concept: For each row as histogram, use largest- rectangle stack.

```javascript
function maximalRectangle(mat) {
  if (!mat.length) return 0;
  const m = mat.length, n = mat[0].length;
  const heights = new Array(n).fill(0);
  let best = 0;
  
  const area = arr => {
    const stack = [];
    const arrWithSentinel = [...arr, 0];
    let res = 0;
    for (let i = 0; i < arrWithSentinel.length; i++) {
      while (stack.length && arrWithSentinel[i] < arrWithSentinel[stack[stack.length - 1]]) {
        const height = arrWithSentinel[stack.pop()];
        const left = stack.length ? stack[stack.length - 1] + 1 : 0;
        res = Math.max(res, height * (i - left));
      }
      stack.push(i);
    }
    return res;
  };
  
  for (let row = 0; row < m; row++) {
    for (let col = 0; col < n; col++) {
      heights[col] = mat[row][col] === '1' ? heights[col] + 1 : 0;
    }
    best = Math.max(best, area(heights));
  }
  return best;
}

// Test Cases:
//
// Example 1:
//   Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
//   Output: 6
//   Explanation: Maximal rectangle has area 6
//
// Example 2:
//   Input: matrix = [["0"]]
//   Output: 0
//
// Example 3:
//   Input: matrix = [["1"]]
//   Output: 1
//
// Example 4:
//   Input: matrix = [["1","1"],["1","1"]]
//   Output: 4
```

Deep Insights:
  - Rule: For each row as histogram, use largest-rectangle stack; O(mn) time, O(n) space.
  - Real-world: Maximum rectangle problems, histogram analysis, grid problems, geometric optimization.
  - Common mistake: Binary matrix of '1'/'0'; stack pattern crucial; not building histogram correctly.
  - Optimization: O(mn) time; O(n) space for histogram; stack pattern crucial for area calculation.
  - Interview tip: Explain histogram approach clearly; mention stack pattern; ask about matrix constraints.
## Q136. Rain Water with DP

Concept: Precompute leftMax/rightMax arrays; water at i = min(L,R) - h[i].

```javascript
function trapDP(height) {
  const n = height.length;
  const leftMax = new Array(n);
  const rightMax = new Array(n);
  
  for (let i = 0, max = 0; i < n; i++) {
    max = Math.max(max, height[i]);
    leftMax[i] = max;
  }
  
  for (let i = n - 1, max = 0; i >= 0; i--) {
    max = Math.max(max, height[i]);
    rightMax[i] = max;
  }
  
  let water = 0;
  for (let i = 0; i < n; i++) {
    water += Math.min(leftMax[i], rightMax[i]) - height[i];
  }
  return water;
}

// Test Cases:
//
// Example 1:
//   Input: height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
//   Output: 6
//   Explanation: Trapped water units = 6
//
// Example 2:
//   Input: height = [4, 2, 0, 3, 2, 5]
//   Output: 9
//
// Example 3:
//   Input: height = [1, 0, 1]
//   Output: 1
//
// Example 4:
//   Input: height = [3, 0, 2, 0, 4]
//   Output: 7
```

Deep Insights:
  - Rule: Precompute leftMax/rightMax arrays; water at i = min(L,R) - h[i]; O(n) time, O(n) space (can optimize).
  - Real-world: Rain water trapping, elevation analysis, water collection, geometric calculations.
  - Common mistake: Negative heights; classic DP precompute; wrong water calculation; pointer reduces to O(1) space.
  - Optimization: Two-pointer reduces to O(1) space; classic DP precompute is O(n) space; O(n) time optimal.
  - Interview tip: Explain precompute clearly; mention two-pointer optimization; ask about space optimization.
## Q137. Egg Dropping

Concept: dp[k][m]=max floors solvable with k eggs and m moves; increase m until >= N.

```javascript
function superEggDrop(k, n) {
  const dp = new Array(k + 1).fill(0);
  let moves = 0;
  while (dp[k] < n) {
    moves++;
    for (let eggs = k; eggs >= 1; eggs--) {
      dp[eggs] = dp[eggs] + dp[eggs - 1] + 1;
    }
  }
  return moves;
}

// Test Cases:
//
// Example 1:
//   Input: k = 1, n = 2
//   Output: 2
//   Explanation: With 1 egg, need 2 moves to find the critical floor
//
// Example 2:
//   Input: k = 2, n = 6
//   Output: 3
//
// Example 3:
//   Input: k = 3, n = 14
//   Output: 4
//
// Example 4:
//   Input: k = 2, n = 1
//   Output: 1
```

Deep Insights:
  - Rule: dp[k][m]=max floors solvable with k eggs and m moves; increase m until >= N; O(k×m) time.
  - Real-world: Egg dropping problems, optimal testing, search problems, optimization with constraints.
  - Common mistake: Much faster than O(kn) DP; monotonic m increases; wrong DP transition; not handling eggs correctly.
  - Optimization: O(k×m) time where m is moves; much faster than O(kn) DP; monotonic m increases.
  - Interview tip: Explain egg dropping clearly; mention optimal strategy; ask about complexity.
## Q138. Matrix Chain Multiplication

Concept: Interval DP; dp[i][j]=min over k of dp[i][k]+dp[k][j]+cost.

```javascript
function matrixChainOrder(p) {
  const n = p.length - 1;
  const dp = Array.from({length: n}, () => Array(n).fill(0));
  
  for (let len = 2; len <= n; len++) {
    for (let i = 0; i + len - 1 < n; i++) {
      const j = i + len - 1;
      dp[i][j] = Infinity;
      for (let k = i; k < j; k++) {
        dp[i][j] = Math.min(
          dp[i][j],
          dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
        );
      }
    }
  }
  return dp[0][n - 1];
}

// Test Cases:
//
// Example 1:
//   Input: p = [1, 2, 3, 4, 3]
//   Output: 30
//   Explanation: Optimal parenthesization: ((A1(A2A3))A4) requires 30 multiplications
//
// Example 2:
//   Input: p = [10, 20, 30, 40, 30]
//   Output: 30000
//
// Example 3:
//   Input: p = [40, 20, 30, 10, 30]
//   Output: 26000
//
// Example 4:
//   Input: p = [1, 2, 3]
//   Output: 6
```

Deep Insights:
  - Rule: Interval DP; dp[i][j]=min over k of dp[i][k]+dp[k][j]+cost; O(n^3) time, O(n^2) space.
  - Real-world: Matrix chain multiplication, parenthesization optimization, expression optimization, interval DP.
  - Common mistake: Parenthesization optimization; no actual multiplication; wrong interval length handling.
  - Optimization: O(n^3) time for n matrices; O(n^2) space; parenthesization optimization; no actual multiplication.
  - Interview tip: Explain interval DP clearly; mention parenthesization; ask about matrix dimensions.
## Q139. Min Cost Climbing Stairs

Concept: dp[i]=cost[i]+min(dp[i-1], dp[i-2]); answer min of last two.

```javascript
function minCostClimbingStairs(cost) {
  const n = cost.length;
  const dp = new Array(n + 1).fill(0);
  dp[0] = 0;
  dp[1] = 0;
  
  for (let i = 2; i <= n; i++) {
    dp[i] = Math.min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]);
  }
  
  return dp[n];
}

// Test Cases:
//
// Example 1:
//   Input: cost = [10, 15, 20]
//   Output: 15
//   Explanation: Start at index 1 (cost 15), go to top (total 15)
//
// Example 2:
//   Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
//   Output: 6
//   Explanation: Start at index 0, skip 100s, pay minimum cost
//
// Example 3:
//   Input: cost = [10, 15]
//   Output: 10
//
// Example 4:
//   Input: cost = [0, 0, 0, 0]
//   Output: 0
```

Deep Insights:
  - Rule: dp[i]=cost[i]+min(dp[i-1], dp[i-2]); answer min of last two; O(n) time, O(n) space.
  - Real-world: Min cost climbing stairs, cost optimization, path cost problems, step cost problems.
  - Common mistake: Similar to climb stairs; not handling cost correctly; wrong base cases.
  - Optimization: O(n) time, O(n) space with DP array; can optimize to O(1) space; similar to climb stairs; handle cost correctly.
  - Interview tip: Explain cost handling clearly; mention climb stairs similarity; ask about starting position.

Time Complexity: O(n)
Space Complexity: O(n)
## Q140. Buy & Sell Stock DP (multiple variants)

Concept: Track states: hold/cash with constraints (k, cooldown, fee).

```javascript
function maxProfitCooldown(prices) {
  if (prices.length === 0) return 0;
  
  const n = prices.length;
  const hold = new Array(n + 1).fill(0);
  const cash = new Array(n + 1).fill(0);
  
  hold[0] = -Infinity;
  cash[0] = 0;
  
  for (let i = 1; i <= n; i++) {
    cash[i] = Math.max(cash[i - 1], hold[i - 1] + prices[i - 1]);
    hold[i] = Math.max(hold[i - 1], (i >= 2 ? cash[i - 2] : 0) - prices[i - 1]);
  }
  
  return cash[n];
}

// Test Cases:
//
// Example 1:
//   Input: prices = [1, 2, 3, 0, 2]
//   Output: 3
//   Explanation: Buy on day 1 (price 1), sell on day 2 (price 2), cooldown, buy on day 4 (price 0), sell on day 5 (price 2)
//                Profit: (2-1) + (2-0) = 3
//
// Example 2:
//   Input: prices = [1]
//   Output: 0
//
// Example 3:
//   Input: prices = [1, 2, 4]
//   Output: 3
//   Explanation: Buy on day 1 (price 1), sell on day 3 (price 4), profit = 3
//
// Example 4:
//   Input: prices = [3, 3, 5, 0, 0, 3, 1, 4]
//   Output: 6
```

Deep Insights:
  - Rule: Track states: hold/cash with constraints (k, cooldown, fee); O(n) time, O(n) space per variant.
  - Real-world: Stock trading problems, profit maximization, trading strategies, optimization problems.
  - Common mistake: O(n) time; initialize carefully per variant; wrong state transitions; not handling constraints.
  - Optimization: O(n) time optimal; space O(n) with DP arrays or can optimize to O(1) depending on variant; initialize carefully per variant.
  - Interview tip: Explain state transitions clearly; mention variant differences; ask about constraints.

Time Complexity: O(n)
Space Complexity: O(n)

## Q141. Word Break

Concept:
Check if string can be segmented into dictionary words using DP; dp[i] = true if s[0..i) can be segmented.

Example:
```javascript
function wordBreak(s, wordDict) {
  const wordSet = new Set(wordDict);
  const dp = new Array(s.length + 1).fill(false);
  dp[0] = true;
  
  for (let i = 1; i <= s.length; i++) {
    for (let j = 0; j < i; j++) {
      if (dp[j] && wordSet.has(s.substring(j, i))) {
        dp[i] = true;
        break;
      }
    }
  }
  
  return dp[s.length];
}

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

**Time Complexity:** O(n²×m) - n string length, m word length  
**Space Complexity:** O(n) - DP array

Deep Insights:
- DP tracks if prefix can be segmented; check all possible splits; O(n²×m) time, O(n) space.
- dp[i] = true if s[0..i) can be segmented; check all prefixes ending at i.
- Use word set for O(1) lookup; break early when found.
- Edge case: Empty string returns true; no valid segmentation returns false.
- Interview tip: Explain DP state; mention word set optimization; ask about all solutions variant.

## Q142. Triangle

Concept:
Find minimum path sum from top to bottom in triangle using DP; update each position with minimum sum.

Example:
```javascript
function minimumTotal(triangle) {
  const n = triangle.length;
  const dp = [...triangle[n - 1]];
  
  for (let i = n - 2; i >= 0; i--) {
    for (let j = 0; j <= i; j++) {
      dp[j] = triangle[i][j] + Math.min(dp[j], dp[j + 1]);
    }
  }
  
  return dp[0];
}

// Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
// Output: 11
// Explanation: Path 2 -> 3 -> 5 -> 1 = 11

// Input: triangle = [[-10]]
// Output: -10

// Input: triangle = [[2],[3,4],[6,5,9],[4,1,8,3]]
// Output: 14
```

**Time Complexity:** O(n²) - n is number of rows  
**Space Complexity:** O(n) - DP array

Deep Insights:
- Bottom-up DP: start from bottom row, update each position with minimum; O(n²) time, O(n) space.
- Use bottom row as base; work upward; each position chooses minimum from below.
- Space optimization: reuse triangle last row instead of new array.
- Edge case: Single row returns that value; single element returns its value.
- Interview tip: Explain bottom-up approach; mention space optimization; ask about top-down variant.

## Q143. Unique Paths II

Concept:
Find number of unique paths from top-left to bottom-right with obstacles using DP; skip obstacles.

Example:
```javascript
function uniquePathsWithObstacles(obstacleGrid) {
  const m = obstacleGrid.length;
  const n = obstacleGrid[0].length;
  
  if (obstacleGrid[0][0] === 1 || obstacleGrid[m - 1][n - 1] === 1) return 0;
  
  const dp = new Array(n).fill(0);
  dp[0] = 1;
  
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (obstacleGrid[i][j] === 1) {
        dp[j] = 0;
      } else if (j > 0) {
        dp[j] += dp[j - 1];
      }
    }
  }
  
  return dp[n - 1];
}

// Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
// Output: 2
// Explanation: Two paths avoiding obstacle at (1,1)

// Input: obstacleGrid = [[0,1],[0,0]]
// Output: 1

// Input: obstacleGrid = [[1,0]]
// Output: 0
```

**Time Complexity:** O(m×n) - Visit each cell once  
**Space Complexity:** O(n) - DP array

Deep Insights:
- DP tracks paths to each cell; skip obstacles (set to 0); O(m×n) time, O(n) space.
- Base case: starting cell; obstacles set paths to 0.
- Recurrence: paths[i][j] = paths[i-1][j] + paths[i][j-1] if no obstacle.
- Edge case: Obstacle at start or end returns 0; single cell returns 1 if no obstacle.
- Interview tip: Explain obstacle handling; mention space optimization; ask about multiple obstacles.

## Q144. Interleaving String

Concept:
Check if string c is interleaving of strings a and b using DP; dp[i][j] = true if a[0..i) and b[0..j) form c[0..i+j).

Example:
```javascript
function isInterleave(s1, s2, s3) {
  if (s1.length + s2.length !== s3.length) return false;
  
  const m = s1.length;
  const n = s2.length;
  const dp = Array.from({length: m + 1}, () => new Array(n + 1).fill(false));
  dp[0][0] = true;
  
  for (let i = 0; i <= m; i++) {
    for (let j = 0; j <= n; j++) {
      if (i > 0 && s1[i - 1] === s3[i + j - 1]) {
        dp[i][j] = dp[i][j] || dp[i - 1][j];
      }
      if (j > 0 && s2[j - 1] === s3[i + j - 1]) {
        dp[i][j] = dp[i][j] || dp[i][j - 1];
      }
    }
  }
  
  return dp[m][n];
}

// Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
// Output: true

// Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
// Output: false

// Input: s1 = "", s2 = "", s3 = ""
// Output: true
```

**Time Complexity:** O(m×n) - Fill DP table  
**Space Complexity:** O(m×n) - DP table, can optimize to O(n)

Deep Insights:
- DP tracks if prefixes of s1 and s2 can form prefix of s3; O(m×n) time, O(m×n) space.
- Check if current character in s3 matches s1 or s2; update DP accordingly.
- Base case: empty strings form empty interleaving.
- Edge case: Length mismatch returns false; all empty returns true.
- Interview tip: Explain DP state clearly; mention character matching; ask about optimization.

## Q145. Best Time to Buy and Sell Stock III

Concept:
Find maximum profit with at most two transactions using DP; track states for transactions.

Example:
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

Deep Insights:
- Track states for two transactions: buy1, sell1, buy2, sell2; O(n) time, O(1) space.
- Update states greedily: maximize profit at each transaction.
- buy2 uses profit from sell1; sell2 uses buy2.
- Edge case: No profit returns 0; single transaction may be better.
- Interview tip: Explain state tracking; mention k transactions generalization; ask about constraints.

## Q146. Best Time to Buy and Sell Stock IV

Concept:
Find maximum profit with at most k transactions using DP; track states for k transactions.

Example:
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

Deep Insights:
- DP tracks profit for k transactions; optimize if k >= n/2 (unlimited); O(n×k) time, O(n×k) space.
- Track maxDiff to optimize: avoid recalculating max(dp[i-1][j] - prices[j]).
- Special case: k >= n/2 allows unlimited transactions (greedy approach).
- Edge case: k = 0 or empty prices returns 0; large k reduces to unlimited.
- Interview tip: Explain DP state; mention optimization cases; ask about constraints.

## Q147. Maximal Square

Concept:
Find largest square containing only 1s in binary matrix using DP; track maximum square side length.

Example:
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

// Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
// Output: 4
// Explanation: Largest square of side 2 (area 4)

// Input: matrix = [["0","1"],["1","0"]]
// Output: 1

// Input: matrix = [["0"]]
// Output: 0
```

**Time Complexity:** O(m×n) - Visit each cell once  
**Space Complexity:** O(m×n) - DP table, can optimize to O(n)

Deep Insights:
- DP tracks square side length ending at each cell; take minimum of three neighbors + 1; O(m×n) time, O(m×n) space.
- dp[i][j] = side length of largest square ending at (i,j); minimum ensures square shape.
- Base case: edge cells have side length 1 if '1'.
- Edge case: No '1' returns 0; single '1' returns 1.
- Interview tip: Explain minimum logic; mention square shape requirement; ask about rectangle variant.

## Q148. Maximum Sum Circular Subarray

Concept:
Find maximum sum subarray in circular array using Kadane's algorithm; consider wrapped and unwrapped cases.

Example:
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

Deep Insights:
- Two cases: maximum subarray (normal Kadane) or circular (total - minimum subarray); O(n) time, O(1) space.
- Circular case: maximum sum = total - minimum subarray sum (wraps around).
- Handle all negative case: return maximum element.
- Edge case: All negative returns maximum element; all positive returns total sum.
- Interview tip: Explain two cases clearly; mention circular wraparound; ask about minimum subarray variant.