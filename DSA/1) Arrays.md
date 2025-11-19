# Arrays

## Q1. Two Sum

**Problem:** Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice.

**Approach:** Use a hash map to store each number and its index as we traverse. For each number, check if the complement (target - current number) exists in the map.

### Solution 1: Hash Map (Optimal)
```javascript
function twoSum(nums, target) {
  const seen = new Map();
  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];
    if (seen.has(complement)) {
      return [seen.get(complement), i];
    }
    seen.set(nums[i], i);
  }
  return [];
}

// Test Cases:
// Input: nums = [2, 7, 11, 15], target = 9
// Output: [0, 1]
// Explanation: nums[0] + nums[1] = 2 + 7 = 9

// Input: nums = [3, 2, 4], target = 6
// Output: [1, 2]
// Explanation: nums[1] + nums[2] = 2 + 4 = 6

// Input: nums = [3, 3], target = 6
// Output: [0, 1]
// Explanation: nums[0] + nums[1] = 3 + 3 = 6
```

**Time Complexity:** O(n) - Single pass through array  
**Space Complexity:** O(n) - Hash map stores up to n elements

### Solution 2: Brute Force (Alternative)
```javascript
function twoSumBruteForce(nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) {
        return [i, j];
      }
    }
  }
  return [];
}
```

**Time Complexity:** O(n²) - Nested loops check all pairs  
**Space Complexity:** O(1) - Only using constant extra space

---

## Q2. Best Time to Buy & Sell Stock

**Problem:** You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

**Approach:** Track the minimum price seen so far and calculate profit for each day. Keep the maximum profit found.

### Solution 1: Single Pass (Optimal)
```javascript
function maxProfit(prices) {
  let minPrice = Infinity;
  let maxProfit = 0;
  
  for (const price of prices) {
    minPrice = Math.min(minPrice, price);
    maxProfit = Math.max(maxProfit, price - minPrice);
  }
  
  return maxProfit;
}

// Test Cases:
// Input: prices = [7, 1, 5, 3, 6, 4]
// Output: 5
// Explanation: Buy on day 1 (price = 1) and sell on day 4 (price = 6), profit = 6-1 = 5

// Input: prices = [7, 6, 4, 3, 1]
// Output: 0
// Explanation: Prices only decreasing, no profit possible

// Input: prices = [2, 4, 1]
// Output: 2
// Explanation: Buy on day 0 (price = 2) and sell on day 1 (price = 4), profit = 4-2 = 2
```

**Time Complexity:** O(n) - Single pass through prices array  
**Space Complexity:** O(1) - Only using constant extra variables

### Solution 2: Two Pointers (Alternative)
```javascript
function maxProfitTwoPointers(prices) {
  let buy = 0;
  let sell = 1;
  let maxProfit = 0;
  
  while (sell < prices.length) {
    if (prices[buy] < prices[sell]) {
      maxProfit = Math.max(maxProfit, prices[sell] - prices[buy]);
    } else {
      buy = sell;
    }
    sell++;
  }
  
  return maxProfit;
}
```

**Time Complexity:** O(n) - Single pass through array  
**Space Complexity:** O(1) - Only using constant extra variables


## Q3. Kadane's Algorithm (Maximum Subarray Sum)

**Problem:** Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum. A subarray is a contiguous part of an array.

**Approach:** Use Kadane's algorithm—maintain a running sum and reset it when it becomes negative. Keep track of the maximum sum seen so far.

### Solution 1: Kadane's Algorithm (Optimal)
```javascript
function maxSubArray(nums) {
  let currentSum = nums[0];
  let maxSum = nums[0];
  
  for (let i = 1; i < nums.length; i++) {
    currentSum = Math.max(nums[i], currentSum + nums[i]);
    maxSum = Math.max(maxSum, currentSum);
  }
  
  return maxSum;
}

// Test Cases:
// Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
// Output: 6
// Explanation: Subarray [4, -1, 2, 1] has the largest sum = 6

// Input: nums = [1]
// Output: 1
// Explanation: Single element is the maximum subarray

// Input: nums = [-2, -1, -3]
// Output: -1
// Explanation: All negative, maximum is the least negative element (-1)

// Input: nums = [5, 4, -1, 7, 8]
// Output: 23
// Explanation: Entire array [5, 4, -1, 7, 8] has the largest sum = 23
```

**Time Complexity:** O(n) - Single pass through array  
**Space Complexity:** O(1) - Only using constant extra variables

### Solution 2: Divide and Conquer (Alternative)
```javascript
function maxSubArrayDivideConquer(nums) {
  return maxSubArrayHelper(nums, 0, nums.length - 1);
}

function maxSubArrayHelper(nums, left, right) {
  if (left === right) return nums[left];
  
  const mid = Math.floor((left + right) / 2);
  const leftMax = maxSubArrayHelper(nums, left, mid);
  const rightMax = maxSubArrayHelper(nums, mid + 1, right);
  const crossMax = maxCrossingSubArray(nums, left, mid, right);
  
  return Math.max(leftMax, rightMax, crossMax);
}

function maxCrossingSubArray(nums, left, mid, right) {
  let leftSum = -Infinity;
  let sum = 0;
  for (let i = mid; i >= left; i--) {
    sum += nums[i];
    leftSum = Math.max(leftSum, sum);
  }
  
  let rightSum = -Infinity;
  sum = 0;
  for (let i = mid + 1; i <= right; i++) {
    sum += nums[i];
    rightSum = Math.max(rightSum, sum);
  }
  
  return leftSum + rightSum;
}
```

**Time Complexity:** O(n log n) - Divide and conquer approach  
**Space Complexity:** O(log n) - Recursion stack depth


## Q4. Rotate Array

**Problem:** Given an array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative. You must do this in-place with O(1) extra space.

**Approach:** Use the triple-reverse technique: reverse the entire array, then reverse the first k elements, and finally reverse the remaining elements.

### Solution 1: Triple Reverse (Optimal)
```javascript
function rotate(nums, k) {
  const n = nums.length;
  k %= n; // Normalize k when it's larger than array length
  
  const reverse = (left, right) => {
    while (left < right) {
      [nums[left], nums[right]] = [nums[right], nums[left]];
      left++;
      right--;
    }
  };
  
  // Reverse entire array
  reverse(0, n - 1);
  // Reverse first k elements
  reverse(0, k - 1);
  // Reverse remaining elements
  reverse(k, n - 1);
}

// Test Cases:
// Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
// Output: [5, 6, 7, 1, 2, 3, 4]
// Explanation: Rotate right 3 steps: [5, 6, 7, 1, 2, 3, 4]

// Input: nums = [-1, -100, 3, 99], k = 2
// Output: [3, 99, -1, -100]
// Explanation: Rotate right 2 steps: [3, 99, -1, -100]

// Input: nums = [1, 2], k = 3
// Output: [2, 1]
// Explanation: k = 3 % 2 = 1, rotate right 1 step: [2, 1]
```

**Time Complexity:** O(n) - Each element swapped once during reverse operations  
**Space Complexity:** O(1) - In-place reversal, constant extra space

### Solution 2: Cyclic Replacement (Alternative)
```javascript
function rotateCyclic(nums, k) {
  const n = nums.length;
  k %= n;
  let count = 0;
  
  for (let start = 0; count < n; start++) {
    let current = start;
    let prev = nums[start];
    
    do {
      const next = (current + k) % n;
      const temp = nums[next];
      nums[next] = prev;
      prev = temp;
      current = next;
      count++;
    } while (start !== current);
  }
}
```

**Time Complexity:** O(n) - Each element visited once  
**Space Complexity:** O(1) - Constant extra space


## Q5. Merge Intervals

**Problem:** Given an array of `intervals` where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

**Approach:** Sort intervals by start time, then iterate through them. If the current interval overlaps with the last merged interval (start ≤ last end), merge by updating the end. Otherwise, add it as a new interval.

### Solution 1: Sort and Merge (Optimal)
```javascript
function merge(intervals) {
  if (intervals.length === 0) return [];
  
  // Sort intervals by start time
  intervals.sort((a, b) => a[0] - b[0]);
  
  const merged = [];
  
  for (const [start, end] of intervals) {
    // If no merged intervals or current doesn't overlap with last
    if (merged.length === 0 || start > merged[merged.length - 1][1]) {
      merged.push([start, end]);
    } else {
      // Merge: update the end of last interval
      merged[merged.length - 1][1] = Math.max(merged[merged.length - 1][1], end);
    }
  }
  
  return merged;
}

// Test Cases:
// Input: intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
// Output: [[1, 6], [8, 10], [15, 18]]
// Explanation: [1, 3] and [2, 6] overlap, merge to [1, 6]

// Input: intervals = [[1, 4], [4, 5]]
// Output: [[1, 5]]
// Explanation: [1, 4] and [4, 5] overlap (touching at 4), merge to [1, 5]

// Input: intervals = [[1, 4], [0, 4]]
// Output: [[0, 4]]
// Explanation: [1, 4] and [0, 4] overlap completely, merge to [0, 4]

// Input: intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
// Output: [[1, 6], [8, 10], [15, 18]]
```

**Time Complexity:** O(n log n) - Sorting dominates, then O(n) merge pass  
**Space Complexity:** O(n) - Result array stores merged intervals (worst case: no overlaps)


## Q6. Largest Element in Array

**Problem:** Given an array `nums`, find and return the largest element in the array.

**Approach:** Traverse the array once, keeping track of the maximum value seen so far.

### Solution 1: Linear Scan (Optimal)
```javascript
function findMax(nums) {
  let max = nums[0];
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] > max) {
      max = nums[i];
    }
  }
  return max;
}

// Test Cases:
// Input: nums = [3, 5, 2, 8, 1]
// Output: 8
// Explanation: Maximum element in array is 8

// Input: nums = [-1, -5, -3]
// Output: -1
// Explanation: Maximum element (least negative) is -1

// Input: nums = [42]
// Output: 42
// Explanation: Single element array, maximum is the element itself
```

**Time Complexity:** O(n) - Single pass through array  
**Space Complexity:** O(1) - Only using one extra variable

### Solution 2: Using Math.max (Alternative)
```javascript
function findMaxMath(nums) {
  return Math.max(...nums);
}
```

**Time Complexity:** O(n) - Math.max scans all elements  
**Space Complexity:** O(1) - Constant space


## Q7. Sort Colors (Dutch National Flag)

**Problem:** Given an array `nums` with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue. We use integers 0, 1, and 2 to represent red, white, and blue respectively.

**Approach:** Use the Dutch National Flag algorithm with three pointers: `low` (0s), `mid` (1s), `high` (2s). Partition the array in a single pass.

### Solution 1: Dutch National Flag (Optimal)
```javascript
function sortColors(nums) {
  let low = 0;        // Pointer for 0s (red)
  let mid = 0;        // Pointer for 1s (white)
  let high = nums.length - 1;  // Pointer for 2s (blue)
  
  while (mid <= high) {
    if (nums[mid] === 0) {
      // Swap with low, move both pointers
      [nums[low], nums[mid]] = [nums[mid], nums[low]];
      low++;
      mid++;
    } else if (nums[mid] === 1) {
      // Already in correct position, just advance mid
      mid++;
    } else {
      // nums[mid] === 2, swap with high
      [nums[mid], nums[high]] = [nums[high], nums[mid]];
      high--;
      // Don't increment mid here, need to check swapped element
    }
  }
}

// Test Cases:
// Input: nums = [2, 0, 2, 1, 1, 0]
// Output: [0, 0, 1, 1, 2, 2]
// Explanation: Sorted array with 0s, then 1s, then 2s

// Input: nums = [2, 0, 1]
// Output: [0, 1, 2]
// Explanation: Sorted array with 0, then 1, then 2

// Input: nums = [0]
// Output: [0]
// Explanation: Single element array already sorted
```

**Time Complexity:** O(n) - Single pass with three pointers  
**Space Complexity:** O(1) - In-place partitioning, constant extra space

### Solution 2: Counting Sort (Alternative)
```javascript
function sortColorsCounting(nums) {
  const count = [0, 0, 0];
  
  // Count occurrences
  for (const num of nums) {
    count[num]++;
  }
  
  // Fill array based on counts
  let idx = 0;
  for (let i = 0; i < 3; i++) {
    while (count[i] > 0) {
      nums[idx++] = i;
      count[i]--;
    }
  }
}
```

**Time Complexity:** O(n) - Two passes through array  
**Space Complexity:** O(1) - Count array of size 3 is constant


## Q8. Product of Array Except Self

**Problem:** Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`. The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer. You must write an algorithm that runs in O(n) time and without using the division operator.

**Approach:** Use two passes: first pass computes prefix products (left to right), second pass multiplies by suffix products (right to left). This avoids division and handles zeros correctly.

### Solution 1: Two Passes with Prefix/Suffix (Optimal)
```javascript
function productExceptSelf(nums) {
  const n = nums.length;
  const result = new Array(n).fill(1);
  
  // First pass: compute prefix products (left to right)
  let prefix = 1;
  for (let i = 0; i < n; i++) {
    result[i] = prefix;
    prefix *= nums[i];
  }
  
  // Second pass: multiply by suffix products (right to left)
  let suffix = 1;
  for (let i = n - 1; i >= 0; i--) {
    result[i] *= suffix;
    suffix *= nums[i];
  }
  
  return result;
}

// Test Cases:
// Input: nums = [1, 2, 3, 4]
// Output: [24, 12, 8, 6]
// Explanation: res[0] = 2*3*4 = 24, res[1] = 1*3*4 = 12, etc.

// Input: nums = [-1, 1, 0, -3, 3]
// Output: [0, 0, 9, 0, 0]
// Explanation: Zeros result in zero products except at zero position

// Input: nums = [2, 3]
// Output: [3, 2]
// Explanation: res[0] = 3, res[1] = 2
```

**Time Complexity:** O(n) - Two passes through array  
**Space Complexity:** O(1) - Excluding output array, only constant extra variables

### Solution 2: Using Division (Not Recommended - Fails with Zeros)
```javascript
function productExceptSelfDivision(nums) {
  const product = nums.reduce((acc, val) => acc * val, 1);
  return nums.map(num => product / num);
}
// Note: This fails when array contains zeros!
```

**Time Complexity:** O(n) - Two passes  
**Space Complexity:** O(1) - Excluding output


## Q9. Find Missing Number

**Problem:** Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

**Approach:** Use XOR to cancel pairs. XOR all numbers from 0 to n with all numbers in the array. The remaining value is the missing number.

### Solution 1: XOR (Optimal)
```javascript
function missingNumber(nums) {
  const n = nums.length;
  let missing = n; // Start with n (since range is [0, n])
  
  for (let i = 0; i < n; i++) {
    missing ^= i ^ nums[i];
  }
  
  return missing;
}

// Test Cases:
// Input: nums = [3, 0, 1]
// Output: 2
// Explanation: n = 3, array contains 0, 1, 3. Missing number is 2

// Input: nums = [0, 1]
// Output: 2
// Explanation: n = 2, array contains 0, 1. Missing number is 2

// Input: nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
// Output: 8
// Explanation: n = 9, missing number is 8
```

**Time Complexity:** O(n) - Single pass through array  
**Space Complexity:** O(1) - Only using constant extra variables

### Solution 2: Sum Formula (Alternative)
```javascript
function missingNumberSum(nums) {
  const n = nums.length;
  const expectedSum = (n * (n + 1)) / 2;
  const actualSum = nums.reduce((sum, num) => sum + num, 0);
  return expectedSum - actualSum;
}
```

**Time Complexity:** O(n) - Single pass to compute sum  
**Space Complexity:** O(1) - Constant space

**Note:** Sum approach can overflow for large n; XOR avoids overflow.


## Q10. Majority Element (Boyer-Moore)

**Problem:** Given an array `nums` of size `n`, return the majority element. The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

**Approach:** Use Boyer-Moore Voting Algorithm. Track a candidate and its count. When count reaches zero, pick a new candidate. The final candidate is the majority element.

### Solution 1: Boyer-Moore Voting Algorithm (Optimal)
```javascript
function majorityElement(nums) {
  let candidate = null;
  let count = 0;
  
  // Phase 1: Find candidate
  for (const num of nums) {
    if (count === 0) {
      candidate = num;
      count = 1;
    } else if (num === candidate) {
      count++;
    } else {
      count--;
    }
  }
  
  // Phase 2: Verify (if majority not guaranteed)
  // count = 0;
  // for (const num of nums) {
  //   if (num === candidate) count++;
  // }
  // return count > nums.length / 2 ? candidate : null;
  
  return candidate; // Assuming majority always exists
}

// Test Cases:
// Input: nums = [3, 2, 3]
// Output: 3
// Explanation: Element 3 appears 2 times (n/2 = 1.5, 2 > 1.5)

// Input: nums = [2, 2, 1, 1, 1, 2, 2]
// Output: 2
// Explanation: Element 2 appears 4 times (n/2 = 3.5, 4 > 3.5)

// Input: nums = [1]
// Output: 1
// Explanation: Single element is majority
```

**Time Complexity:** O(n) - Single pass through array  
**Space Complexity:** O(1) - Only using constant extra variables

### Solution 2: Hash Map (Alternative)
```javascript
function majorityElementHashMap(nums) {
  const count = new Map();
  const n = nums.length;
  
  for (const num of nums) {
    count.set(num, (count.get(num) || 0) + 1);
    if (count.get(num) > n / 2) {
      return num;
    }
  }
}
```

**Time Complexity:** O(n) - Single pass through array  
**Space Complexity:** O(n) - Hash map stores element counts


## Q11. Maximum Product Subarray

**Problem:** Given an integer array `nums`, find the contiguous subarray within an array (containing at least one number) which has the largest product.

**Approach:** Track both maximum and minimum products at each position. When encountering a negative number, swap max and min (since negative × min = positive max). Keep updating the global maximum.

### Solution 1: Dynamic Programming with Max/Min Tracking (Optimal)
```javascript
function maxProduct(nums) {
  let currentMax = nums[0];
  let currentMin = nums[0];
  let globalMax = nums[0];
  
  for (let i = 1; i < nums.length; i++) {
    const num = nums[i];
    
    // If current number is negative, swap max and min
    if (num < 0) {
      [currentMax, currentMin] = [currentMin, currentMax];
    }
    
    // Update max and min
    currentMax = Math.max(num, currentMax * num);
    currentMin = Math.min(num, currentMin * num);
    
    // Update global maximum
    globalMax = Math.max(globalMax, currentMax);
  }
  
  return globalMax;
}

// Test Cases:
// Input: nums = [2, 3, -2, 4]
// Output: 6
// Explanation: Subarray [2, 3] has maximum product = 6

// Input: nums = [-2, 0, -1]
// Output: 0
// Explanation: Maximum product is 0 (from single element 0)

// Input: nums = [-2, 3, -4]
// Output: 24
// Explanation: Entire array [-2, 3, -4] has maximum product = 24
```

**Time Complexity:** O(n) - Single pass through array  
**Space Complexity:** O(1) - Only using constant extra variables


## Q12. Trapping Rain Water

**Problem:** Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

**Approach:** Use two pointers from both ends. Track maximum heights on left and right. Move the pointer with smaller maximum height—water trapped at that position depends on the smaller of the two maxes.

### Solution 1: Two Pointers (Optimal)
```javascript
function trap(height) {
  let left = 0;
  let right = height.length - 1;
  let leftMax = 0;
  let rightMax = 0;
  let waterTrapped = 0;
  
  while (left < right) {
    if (height[left] < height[right]) {
      // Process left side
      leftMax = Math.max(leftMax, height[left]);
      waterTrapped += leftMax - height[left];
      left++;
    } else {
      // Process right side
      rightMax = Math.max(rightMax, height[right]);
      waterTrapped += rightMax - height[right];
      right--;
    }
  }
  
  return waterTrapped;
}

// Test Cases:
// Input: height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
// Output: 6
// Explanation: Rainwater trapped is 6 units

// Input: height = [4, 2, 0, 3, 2, 5]
// Output: 9
// Explanation: Rainwater trapped is 9 units

// Input: height = [3, 0, 2, 0, 4]
// Output: 7
// Explanation: Rainwater trapped is 7 units
```

**Time Complexity:** O(n) - Single pass with two pointers  
**Space Complexity:** O(1) - Only using constant extra variables

### Solution 2: Dynamic Programming (Alternative - Uses O(n) Space)
```javascript
function trapDP(height) {
  const n = height.length;
  if (n === 0) return 0;
  
  const leftMax = new Array(n);
  const rightMax = new Array(n);
  
  // Compute left max for each position
  leftMax[0] = height[0];
  for (let i = 1; i < n; i++) {
    leftMax[i] = Math.max(leftMax[i - 1], height[i]);
  }
  
  // Compute right max for each position
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

**Time Complexity:** O(n) - Three passes through array  
**Space Complexity:** O(n) - Two arrays for left and right maxes


## Q13. Subarray Sum Equals K

**Problem:** Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals `k`.

**Approach:** Use prefix sums with a hash map. For each prefix sum, check if `prefixSum - k` exists in the map. If it does, there are subarrays ending at current position with sum k.

### Solution 1: Prefix Sum with Hash Map (Optimal)
```javascript
function subarraySum(nums, k) {
  const prefixSumCount = new Map();
  prefixSumCount.set(0, 1); // Initialize with {0:1} for subarrays starting at index 0
  let runningSum = 0;
  let count = 0;
  
  for (const num of nums) {
    runningSum += num;
    
    // Check if prefixSum - k exists
    if (prefixSumCount.has(runningSum - k)) {
      count += prefixSumCount.get(runningSum - k);
    }
    
    // Update prefix sum count
    prefixSumCount.set(runningSum, (prefixSumCount.get(runningSum) || 0) + 1);
  }
  
  return count;
}

// Test Cases:
// Input: nums = [1, 1, 1], k = 2
// Output: 2
// Explanation: Subarrays [1,1] (indices 0-1) and [1,1] (indices 1-2) sum to 2

// Input: nums = [1, 2, 3], k = 3
// Output: 2
// Explanation: Subarrays [1,2] and [3] sum to 3

// Input: nums = [1, -1, 0], k = 0
// Output: 3
// Explanation: Subarrays [1,-1], [-1,0], and [0] sum to 0
```

**Time Complexity:** O(n) - Single pass through array  
**Space Complexity:** O(n) - Hash map stores up to n distinct prefix sums


## Q14. Longest Consecutive Sequence

**Problem:** Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence. You must write an algorithm that runs in O(n) time.

**Approach:** Use a hash set to store all numbers. Only expand sequences from sequence heads (numbers where `num - 1` is not in the set). This ensures each element is visited at most twice.

### Solution 1: Hash Set with Sequence Head Detection (Optimal)
```javascript
function longestConsecutive(nums) {
  if (nums.length === 0) return 0;
  
  const numSet = new Set(nums);
  let longest = 0;
  
  for (const num of numSet) {
    // Only expand from sequence heads (num - 1 not in set)
    if (!numSet.has(num - 1)) {
      let currentNum = num;
      let currentLength = 1;
      
      // Expand sequence forward
      while (numSet.has(currentNum + 1)) {
        currentNum++;
        currentLength++;
      }
      
      longest = Math.max(longest, currentLength);
    }
  }
  
  return longest;
}

// Test Cases:
// Input: nums = [100, 4, 200, 1, 3, 2]
// Output: 4
// Explanation: Longest consecutive sequence is [1, 2, 3, 4] with length 4

// Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
// Output: 9
// Explanation: Longest consecutive sequence is [0, 1, 2, 3, 4, 5, 6, 7, 8] with length 9

// Input: nums = [1]
// Output: 1
// Explanation: Single element sequence has length 1
```

**Time Complexity:** O(n) - Each element visited at most twice  
**Space Complexity:** O(n) - Hash set stores all elements

### Solution 2: Sorting (Alternative - O(n log n))
```javascript
function longestConsecutiveSorting(nums) {
  if (nums.length === 0) return 0;
  
  nums.sort((a, b) => a - b);
  let longest = 1;
  let current = 1;
  
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] === nums[i - 1]) continue; // Skip duplicates
    if (nums[i] === nums[i - 1] + 1) {
      current++;
    } else {
      longest = Math.max(longest, current);
      current = 1;
    }
  }
  
  return Math.max(longest, current);
}
```

**Time Complexity:** O(n log n) - Sorting dominates  
**Space Complexity:** O(1) - If sorting is in-place


## Q15. Merge Sorted Arrays

**Problem:** You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively. Merge `nums2` into `nums1` as one sorted array. The final sorted array should not be returned by the function, but instead be stored inside the array `nums1`. `nums1` has a length of `m + n`, where the last `n` elements are set to 0 and should be ignored.

**Approach:** Use two pointers from the end of both arrays. Fill from the back of `nums1` to avoid overwriting unprocessed elements in `nums1`.

### Solution 1: Two Pointers from End (Optimal)
```javascript
function merge(nums1, m, nums2, n) {
  let i = m - 1;      // Pointer for nums1
  let j = n - 1;      // Pointer for nums2
  let k = m + n - 1;  // Pointer for merged result
  
  // Merge from the end
  while (j >= 0) {
    if (i >= 0 && nums1[i] > nums2[j]) {
      nums1[k] = nums1[i];
      i--;
    } else {
      nums1[k] = nums2[j];
      j--;
    }
    k--;
  }
  // Note: If i >= 0, remaining elements are already in correct position
}

// Test Cases:
// Input: nums1 = [1, 2, 3, 0, 0, 0], m = 3, nums2 = [2, 5, 6], n = 3
// Output: nums1 = [1, 2, 2, 3, 5, 6]
// Explanation: Merge sorted arrays [1,2,3] and [2,5,6]

// Input: nums1 = [1], m = 1, nums2 = [], n = 0
// Output: nums1 = [1]
// Explanation: Array nums2 is empty, nums1 remains unchanged

// Input: nums1 = [0], m = 0, nums2 = [1], n = 1
// Output: nums1 = [1]
// Explanation: Array nums1 is empty, merge nums2 into nums1
```

**Time Complexity:** O(m + n) - Merge pass through both arrays  
**Space Complexity:** O(1) - In-place merge, constant extra space

### Solution 2: Using Extra Space (Alternative)
```javascript
function mergeWithExtraSpace(nums1, m, nums2, n) {
  const result = [];
  let i = 0, j = 0;
  
  while (i < m && j < n) {
    if (nums1[i] <= nums2[j]) {
      result.push(nums1[i++]);
    } else {
      result.push(nums2[j++]);
    }
  }
  
  // Add remaining elements
  while (i < m) result.push(nums1[i++]);
  while (j < n) result.push(nums2[j++]);
  
  // Copy back to nums1
  for (let i = 0; i < result.length; i++) {
    nums1[i] = result[i];
  }
}
```

**Time Complexity:** O(m + n) - Merge pass  
**Space Complexity:** O(m + n) - Extra array for result


## Q16. Remove Element

**Problem:** Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` in-place. The relative order of the elements may be changed. Return `k` after placing the final result in the first `k` slots of `nums`.

**Approach:** Use two pointers: one for reading (i) and one for writing (writeIndex). Only write elements that are not equal to `val`.

### Solution 1: Two Pointers (Optimal)
```javascript
function removeElement(nums, val) {
  let writeIndex = 0;
  
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== val) {
      nums[writeIndex] = nums[i];
      writeIndex++;
    }
  }
  
  return writeIndex;
}

// Test Cases:
// Input: nums = [3,2,2,3], val = 3
// Output: 2, nums = [2,2,_,_]
// Explanation: Remove all 3s, new length is 2

// Input: nums = [0,1,2,2,3,0,4,2], val = 2
// Output: 5, nums = [0,1,3,0,4,_,_,_]
// Explanation: Remove all 2s, new length is 5

// Input: nums = [2,2,2], val = 2
// Output: 0, nums = []
// Explanation: All elements removed
```

**Time Complexity:** O(n) - Single pass through array  
**Space Complexity:** O(1) - In-place modification, constant extra space


## Q17. Remove Duplicates from Sorted Array

**Problem:** Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Return `k` after placing the final result in the first `k` slots of `nums`.

**Approach:** Use two pointers. Since the array is sorted, duplicates appear consecutively. Compare current element with the last written unique element.

### Solution 1: Two Pointers (Optimal)
```javascript
function removeDuplicates(nums) {
  if (nums.length === 0) return 0;
  
  let writeIndex = 1; // First element is always unique
  
  for (let i = 1; i < nums.length; i++) {
    // Compare with last written unique element
    if (nums[i] !== nums[writeIndex - 1]) {
      nums[writeIndex] = nums[i];
      writeIndex++;
    }
  }
  
  return writeIndex;
}

// Test Cases:
// Input: nums = [1,1,2]
// Output: 2, nums = [1,2,_]
// Explanation: Remove duplicates, new length is 2

// Input: nums = [0,0,1,1,1,2,2,3,3,4]
// Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
// Explanation: Remove duplicates, new length is 5

// Input: nums = [1,1,1]
// Output: 1, nums = [1,_,_]
// Explanation: All duplicates removed, only one unique element
```

**Time Complexity:** O(n) - Single pass through array  
**Space Complexity:** O(1) - In-place modification


## Q18. Remove Duplicates from Sorted Array II

**Problem:** Given an integer array `nums` sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same. Return `k` after placing the final result in the first `k` slots of `nums`.

**Approach:** Use two pointers. Compare current element with the element two positions back in the written array. This ensures at most two occurrences of each element.

### Solution 1: Two Pointers with K=2 Check (Optimal)
```javascript
function removeDuplicates(nums) {
  if (nums.length <= 2) return nums.length;
  
  let writeIndex = 2; // First two elements are always valid
  
  for (let i = 2; i < nums.length; i++) {
    // Compare with element two positions back
    if (nums[i] !== nums[writeIndex - 2]) {
      nums[writeIndex] = nums[i];
      writeIndex++;
    }
  }
  
  return writeIndex;
}

// Test Cases:
// Input: nums = [1,1,1,2,2,3]
// Output: 5, nums = [1,1,2,2,3,_]
// Explanation: Keep at most 2 of each element

// Input: nums = [0,0,1,1,1,1,2,3,3]
// Output: 7, nums = [0,0,1,1,2,3,3,_,_]
// Explanation: Keep at most 2 of each element

// Input: nums = [1,1,1,1]
// Output: 2, nums = [1,1,_,_]
// Explanation: Keep at most 2 occurrences
```

**Time Complexity:** O(n) - Single pass through array  
**Space Complexity:** O(1) - In-place modification


## Q19. Best Time to Buy and Sell Stock II

**Problem:** You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `i`th day. On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day. Find and return the maximum profit you can achieve.

**Approach:** Use greedy strategy. Sum all positive price differences between consecutive days. This is equivalent to buying every dip and selling every peak.

### Solution 1: Greedy - Sum All Positive Differences (Optimal)
```javascript
function maxProfit(prices) {
  let profit = 0;
  
  for (let i = 1; i < prices.length; i++) {
    // Capture all positive price differences
    if (prices[i] > prices[i - 1]) {
      profit += prices[i] - prices[i - 1];
    }
  }
  
  return profit;
}

// Test Cases:
// Input: prices = [7,1,5,3,6,4]
// Output: 7
// Explanation: Buy on day 1 (1), sell on day 2 (5), buy on day 3 (3), sell on day 4 (6) = 4+3 = 7

// Input: prices = [1,2,3,4,5]
// Output: 4
// Explanation: Buy on day 0, sell on day 4 = 4, or buy/sell each day = 1+1+1+1 = 4

// Input: prices = [7,6,4,3,1]
// Output: 0
// Explanation: No profit possible (monotonic decreasing)
```

**Time Complexity:** O(n) - Single pass through prices  
**Space Complexity:** O(1) - Constant extra space


## Q20. Jump Game

**Problem:** You are given an integer array `nums`. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position. Return `true` if you can reach the last index, or `false` otherwise.

**Approach:** Use greedy algorithm. Track the farthest reachable position. If we can't reach the current index, we can't reach the end. Update the farthest position at each step.

### Solution 1: Greedy - Track Farthest Reachable (Optimal)
```javascript
function canJump(nums) {
  let farthest = 0;
  
  for (let i = 0; i < nums.length; i++) {
    // If current index is unreachable, end is unreachable
    if (i > farthest) return false;
    
    // Update farthest reachable position
    farthest = Math.max(farthest, i + nums[i]);
    
    // Early termination: if we can reach end, return true
    if (farthest >= nums.length - 1) return true;
  }
  
  return farthest >= nums.length - 1;
}

// Test Cases:
// Input: nums = [2,3,1,1,4]
// Output: true
// Explanation: Jump from index 0→1→4 (can reach end)

// Input: nums = [3,2,1,0,4]
// Output: false
// Explanation: Stuck at index 3 (can't reach end)

// Input: nums = [0]
// Output: true
// Explanation: Already at end (single element)
```

**Time Complexity:** O(n) - Single pass through array  
**Space Complexity:** O(1) - Constant extra space


## Q21. Jump Game II

**Problem:** You are given a 0-indexed array of integers `nums` of length `n`. You are initially positioned at `nums[0]`. Each element `nums[i]` represents the maximum length of a forward jump from index `i`. Return the minimum number of jumps to reach `nums[n - 1]`. The test cases are generated such that you can reach `nums[n - 1]`.

**Approach:** Use greedy BFS-like approach. Track the current jump boundary (`currentEnd`) and farthest reachable position. Increment jumps when crossing the current boundary, then update the boundary to the farthest reachable.

### Solution 1: Greedy BFS (Optimal)
```javascript
function jump(nums) {
  let jumps = 0;
  let currentEnd = 0;  // End of current jump level
  let farthest = 0;    // Farthest reachable position
  
  for (let i = 0; i < nums.length - 1; i++) {
    // Update farthest reachable position
    farthest = Math.max(farthest, i + nums[i]);
    
    // When reaching current jump boundary, take a jump
    if (i === currentEnd) {
      jumps++;
      currentEnd = farthest;
    }
  }
  
  return jumps;
}

// Test Cases:
// Input: nums = [2,3,1,1,4]
// Output: 2
// Explanation: Jump from index 0→1→4 (2 jumps)

// Input: nums = [2,3,0,1,4]
// Output: 2
// Explanation: Jump from index 0→1→4 (2 jumps)

// Input: nums = [1,1,1,1]
// Output: 3
// Explanation: Jump from index 0→1→2→3 (3 jumps)
```

**Time Complexity:** O(n) - Single pass through array  
**Space Complexity:** O(1) - Constant extra space


## Q22. H-Index

**Problem:** Given an array of integers `citations` where `citations[i]` is the number of citations a researcher received for their `i`th paper, return the researcher's h-index. The h-index is defined as the maximum value of `h` such that the given researcher has published at least `h` papers that have each been cited at least `h` times.

**Approach:** Sort citations in descending order. Find the first position where `citations[i] < i + 1`. The h-index is `i` at that point (or `n` if all papers qualify).

### Solution 1: Sorting (Optimal)
```javascript
function hIndex(citations) {
  citations.sort((a, b) => b - a);
  
  for (let i = 0; i < citations.length; i++) {
    // If citations[i] < i+1, then h-index is i
    if (citations[i] < i + 1) {
      return i;
    }
  }
  
  // All papers have enough citations
  return citations.length;
}

// Test Cases:
// Input: citations = [3,0,6,1,5]
// Output: 3
// Explanation: 3 papers have at least 3 citations (papers with 3, 5, 6 citations)

// Input: citations = [1,3,1]
// Output: 1
// Explanation: 1 paper has at least 1 citation

// Input: citations = [100]
// Output: 1
// Explanation: 1 paper with 100 citations, h-index is 1
```

**Time Complexity:** O(n log n) - Sorting dominates  
**Space Complexity:** O(1) - In-place sort (or O(n) if we need to preserve original)


## Q23. Insert Delete GetRandom O(1)

**Problem:** Implement the `RandomizedSet` class:
- `RandomizedSet()` Initializes the `RandomizedSet` object.
- `bool insert(int val)` Inserts an item `val` into the set if not present. Returns `true` if the item was not present, `false` otherwise.
- `bool remove(int val)` Removes an item `val` from the set if present. Returns `true` if the item was present, `false` otherwise.
- `int getRandom()` Returns a random element from the current set of elements. Each element must have the same probability of being returned.

**Approach:** Use an array for O(1) random access and a hash map to map values to their indices. For deletion, swap the element to delete with the last element, then pop.

### Solution 1: Array + Hash Map (Optimal)
```javascript
class RandomizedSet {
  constructor() {
    this.arr = [];                    // Store values for random access
    this.map = new Map();             // Map value -> index in array
  }

  insert(val) {
    if (this.map.has(val)) return false;
    
    // Add to array and map
    this.map.set(val, this.arr.length);
    this.arr.push(val);
    return true;
  }

  remove(val) {
    if (!this.map.has(val)) return false;
    
    const index = this.map.get(val);
    const lastVal = this.arr[this.arr.length - 1];
    
    // Swap with last element
    this.arr[index] = lastVal;
    this.map.set(lastVal, index);
    
    // Remove last element
    this.arr.pop();
    this.map.delete(val);
    return true;
  }

  getRandom() {
    const randomIndex = Math.floor(Math.random() * this.arr.length);
    return this.arr[randomIndex];
  }
}

// Test Cases:
// Input: ["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"], [[],[1],[2],[2],[],[1],[2],[]]
// Output: [null,true,false,true,2,true,false,2]
```

**Time Complexity:** O(1) - All operations average case  
**Space Complexity:** O(n) - Array and map storage


## Q24. Gas Station

**Problem:** There are `n` gas stations along a circular route, where the amount of gas at the `i`th station is `gas[i]`. You have a car with an unlimited gas tank and it costs `cost[i]` of gas to travel from the `i`th station to its next `(i + 1)`th station. You begin the journey with an empty tank at one of the gas stations. Given two integer arrays `gas` and `cost`, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return `-1`. If there exists a solution, it is guaranteed to be unique.

**Approach:** Track total gas surplus and current tank. If total gas < total cost, return -1. Otherwise, use greedy: reset start when current tank goes negative—all previous stations cannot be valid starts.

### Solution 1: Greedy with Total Surplus Check (Optimal)
```javascript
function canCompleteCircuit(gas, cost) {
  let totalGas = 0;      // Total gas surplus
  let currentTank = 0;   // Current tank level
  let start = 0;         // Potential starting station
  
  for (let i = 0; i < gas.length; i++) {
    const diff = gas[i] - cost[i];
    totalGas += diff;
    currentTank += diff;
    
    // If tank goes negative, reset start
    if (currentTank < 0) {
      start = i + 1;
      currentTank = 0;
    }
  }
  
  // If total gas >= total cost, solution exists
  return totalGas >= 0 ? start : -1;
}

// Test Cases:
// Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
// Output: 3
// Explanation: Start at station 3, total gas: -2-2-2+3+3 = 0 (can complete circuit)

// Input: gas = [2,3,4], cost = [3,4,3]
// Output: -1
// Explanation: Total gas (9) < total cost (10), cannot complete circuit

// Input: gas = [5,1,2,3,4], cost = [4,4,1,5,1]
// Output: 4
// Explanation: Start at station 4, can complete circuit
```

**Time Complexity:** O(n) - Single pass through stations  
**Space Complexity:** O(1) - Constant extra space


## Q25. Candy

**Problem:** There are `n` children standing in a line. Each child is assigned a rating value given in the integer array `ratings`. You are giving candies to these children subjected to the following requirements:
- Each child must have at least one candy.
- Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the candies to the children.

**Approach:** Use two passes: left-to-right ensures left neighbor constraint, right-to-left ensures right neighbor constraint. Use `Math.max` in second pass to preserve first pass results.

### Solution 1: Two-Pass Greedy (Optimal)
```javascript
function candy(ratings) {
  const n = ratings.length;
  const candies = new Array(n).fill(1);
  
  // Pass 1: Left to right - satisfy left neighbor constraint
  for (let i = 1; i < n; i++) {
    if (ratings[i] > ratings[i - 1]) {
      candies[i] = candies[i - 1] + 1;
    }
  }
  
  // Pass 2: Right to left - satisfy right neighbor constraint
  for (let i = n - 2; i >= 0; i--) {
    if (ratings[i] > ratings[i + 1]) {
      candies[i] = Math.max(candies[i], candies[i + 1] + 1);
    }
  }
  
  return candies.reduce((sum, val) => sum + val, 0);
}

// Test Cases:
// Input: ratings = [1,0,2]
// Output: 5
// Explanation: [2,1,2] = 5 candies (child 0 needs 2, child 1 needs 1, child 2 needs 2)

// Input: ratings = [1,2,2]
// Output: 4
// Explanation: [1,2,1] = 4 candies (equal ratings don't require more candy)

// Input: ratings = [1,3,4,5,2]
// Output: 11
// Explanation: [1,2,3,4,1] = 11 candies
```

**Time Complexity:** O(n) - Two passes through array  
**Space Complexity:** O(n) - Candies array


## Q26. Two Sum II - Input Array Is Sorted

**Problem:** Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`. Return the indices of the two numbers, `index1` and `index2`, added by one as an integer array `[index1, index2]` of length 2.

**Approach:** Use two pointers from both ends. Since the array is sorted, we can move pointers based on the sum comparison with target.

### Solution 1: Two Pointers (Optimal)
```javascript
function twoSum(numbers, target) {
  let left = 0;
  let right = numbers.length - 1;
  
  while (left < right) {
    const sum = numbers[left] + numbers[right];
    
    if (sum === target) {
      return [left + 1, right + 1]; // 1-indexed
    } else if (sum < target) {
      left++; // Need larger sum
    } else {
      right--; // Need smaller sum
    }
  }
  
  return []; // No solution (problem guarantees solution exists)
}

// Test Cases:
// Input: numbers = [2,7,11,15], target = 9
// Output: [1,2]
// Explanation: numbers[0] + numbers[1] = 2 + 7 = 9

// Input: numbers = [2,3,4], target = 6
// Output: [1,3]
// Explanation: numbers[0] + numbers[2] = 2 + 4 = 6

// Input: numbers = [-1,0], target = -1
// Output: [1,2]
// Explanation: numbers[0] + numbers[1] = -1 + 0 = -1
```

**Time Complexity:** O(n) - Single pass through array  
**Space Complexity:** O(1) - Constant extra space


## Q27. Container With Most Water

**Problem:** You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`th line are `(i, 0)` and `(i, height[i])`. Find two lines that together with the x-axis form a container, such that the container contains the most water. Return the maximum amount of water a container can store.

**Approach:** Use two pointers from both ends. Move the pointer with smaller height—area is limited by the smaller height, and width decreases as pointers converge.

### Solution 1: Two Pointers (Optimal)
```javascript
function maxArea(height) {
  let left = 0;
  let right = height.length - 1;
  let maxArea = 0;
  
  while (left < right) {
    const width = right - left;
    const area = Math.min(height[left], height[right]) * width;
    maxArea = Math.max(maxArea, area);
    
    // Move pointer with smaller height
    if (height[left] < height[right]) {
      left++;
    } else {
      right--;
    }
  }
  
  return maxArea;
}

// Test Cases:
// Input: height = [1,8,6,2,5,4,8,3,7]
// Output: 49
// Explanation: Lines at index 1 and 8, area = min(8,7) × 7 = 49

// Input: height = [1,1]
// Output: 1
// Explanation: Lines at index 0 and 1, area = min(1,1) × 1 = 1

// Input: height = [1,2,1]
// Output: 2
// Explanation: Lines at index 0 and 1, area = min(1,2) × 1 = 2
```

**Time Complexity:** O(n) - Single pass through array  
**Space Complexity:** O(1) - Constant extra space


## Q28. 3Sum

**Problem:** Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`. Notice that the solution set must not contain duplicate triplets.

**Approach:** Sort the array first. Fix the first element, then use two pointers for the remaining elements. Skip duplicates to avoid duplicate triplets.

### Solution 1: Sort + Two Pointers (Optimal)
```javascript
function threeSum(nums) {
  nums.sort((a, b) => a - b);
  const result = [];
  
  for (let i = 0; i < nums.length - 2; i++) {
    // Skip duplicates for first element
    if (i > 0 && nums[i] === nums[i - 1]) continue;
    
    let left = i + 1;
    let right = nums.length - 1;
    
    while (left < right) {
      const sum = nums[i] + nums[left] + nums[right];
      
      if (sum === 0) {
        result.push([nums[i], nums[left], nums[right]]);
        
        // Skip duplicates for left and right
        while (left < right && nums[left] === nums[left + 1]) left++;
        while (left < right && nums[right] === nums[right - 1]) right--;
        
        left++;
        right--;
      } else if (sum < 0) {
        left++; // Need larger sum
      } else {
        right--; // Need smaller sum
      }
    }
  }
  
  return result;
}

// Test Cases:
// Input: nums = [-1,0,1,2,-1,-4]
// Output: [[-1,-1,2],[-1,0,1]]
// Explanation: Triplets that sum to zero

// Input: nums = [0,1,1]
// Output: []
// Explanation: No triplets sum to zero

// Input: nums = [0,0,0]
// Output: [[0,0,0]]
// Explanation: Single triplet with all zeros
```

**Time Complexity:** O(n²) - Sort O(n log n) + nested loop O(n²)  
**Space Complexity:** O(1) - Excluding result array (or O(n) for sorting if not in-place)


## Q29. Is Subsequence

**Problem:** Given two strings `s` and `t`, return `true` if `s` is a subsequence of `t`, or `false` otherwise. A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.

**Approach:** Use two pointers—one for `s` and one for `t`. Greedily match characters in order. Move `s` pointer only when match is found.

### Solution 1: Two Pointers (Optimal)
```javascript
function isSubsequence(s, t) {
  let i = 0; // Pointer for s
  let j = 0; // Pointer for t
  
  while (i < s.length && j < t.length) {
    if (s[i] === t[j]) {
      i++; // Match found, move s pointer
    }
    j++; // Always move t pointer
  }
  
  return i === s.length; // Check if all characters in s were matched
}

// Test Cases:
// Input: s = "abc", t = "ahbgdc"
// Output: true
// Explanation: "abc" is subsequence of "ahbgdc" (can delete 'h', 'g', 'd')

// Input: s = "axc", t = "ahbgdc"
// Output: false
// Explanation: "axc" is not subsequence (can't find 'x' after 'a')

// Input: s = "", t = "ahbgdc"
// Output: true
// Explanation: Empty string is subsequence of any string
```

**Time Complexity:** O(n) - Single pass through t (where n = t.length)  
**Space Complexity:** O(1) - Constant extra space


## Q30. Minimum Size Subarray Sum

**Problem:** Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a subarray whose sum is greater than or equal to `target`. If there is no such subarray, return `0`.

**Approach:** Use sliding window technique. Expand window by moving right pointer, shrink by moving left pointer when sum >= target. Track minimum length.

### Solution 1: Sliding Window (Optimal)
```javascript
function minSubArrayLen(target, nums) {
  let left = 0;
  let minLength = Infinity;
  let currentSum = 0;
  
  for (let right = 0; right < nums.length; right++) {
    currentSum += nums[right];
    
    // Shrink window while sum >= target
    while (currentSum >= target) {
      minLength = Math.min(minLength, right - left + 1);
      currentSum -= nums[left];
      left++;
    }
  }
  
  return minLength === Infinity ? 0 : minLength;
}

// Test Cases:
// Input: target = 7, nums = [2,3,1,2,4,3]
// Output: 2
// Explanation: Subarray [4,3] has minimum length 2 (sum = 7)

// Input: target = 4, nums = [1,4,4]
// Output: 1
// Explanation: Subarray [4] has minimum length 1 (sum = 4)

// Input: target = 11, nums = [1,1,1,1,1,1,1,1]
// Output: 0
// Explanation: No subarray sums to >= 11 (max sum = 8)
```

**Time Complexity:** O(n) - Each element visited at most twice (once by right, once by left)  
**Space Complexity:** O(1) - Constant extra space


## Q31. Summary Ranges

**Problem:** You are given a sorted unique integer array `nums`. A range `[a,b]` is the set of all integers from `a` to `b` (inclusive). Return the smallest sorted list of ranges that cover all the numbers in the array exactly. Each range `[a,b]` in the list should be output as:
- `"a->b"` if `a != b`
- `"a"` if `a == b`

**Approach:** Track start and end of consecutive ranges. When a gap is found, add the current range and start a new one.

### Solution 1: Range Tracking (Optimal)
```javascript
function summaryRanges(nums) {
  if (nums.length === 0) return [];
  
  const result = [];
  let start = nums[0];
  let end = nums[0];
  
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] === end + 1) {
      // Continue current range
      end = nums[i];
    } else {
      // Gap found, add current range
      if (start === end) {
        result.push(`${start}`);
      } else {
        result.push(`${start}->${end}`);
      }
      // Start new range
      start = end = nums[i];
    }
  }
  
  // Add last range
  if (start === end) {
    result.push(`${start}`);
  } else {
    result.push(`${start}->${end}`);
  }
  
  return result;
}

// Test Cases:
// Input: nums = [0,1,2,4,5,7]
// Output: ["0->2","4->5","7"]
// Explanation: Ranges [0,1,2], [4,5], [7]

// Input: nums = [0,2,3,4,6,8,9]
// Output: ["0","2->4","6","8->9"]
// Explanation: Ranges [0], [2,3,4], [6], [8,9]

// Input: nums = []
// Output: []
// Explanation: Empty array returns empty array
```

**Time Complexity:** O(n) - Single pass through array  
**Space Complexity:** O(n) - Result array storage


## Q32. Insert Interval

**Problem:** You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [starti, endi]` represent the start and the end of the `i`th interval and `intervals` is sorted in ascending order by `starti`. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval. Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `starti` and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary). Return `intervals` after the insertion.

**Approach:** Three phases: add intervals before newInterval, merge overlapping intervals with newInterval, add remaining intervals.

### Solution 1: Three-Phase Approach (Optimal)
```javascript
function insert(intervals, newInterval) {
  const result = [];
  let i = 0;
  
  // Phase 1: Add all intervals before newInterval
  while (i < intervals.length && intervals[i][1] < newInterval[0]) {
    result.push(intervals[i]);
    i++;
  }
  
  // Phase 2: Merge overlapping intervals
  while (i < intervals.length && intervals[i][0] <= newInterval[1]) {
    newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
    newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
    i++;
  }
  
  // Add merged newInterval
  result.push(newInterval);
  
  // Phase 3: Add remaining intervals
  while (i < intervals.length) {
    result.push(intervals[i]);
    i++;
  }
  
  return result;
}

// Test Cases:
// Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
// Output: [[1,5],[6,9]]
// Explanation: Merge [1,3] and [2,5] into [1,5]

// Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
// Output: [[1,2],[3,10],[12,16]]
// Explanation: Merge [3,5], [6,7], [8,10] and [4,8] into [3,10]

// Input: intervals = [], newInterval = [5,7]
// Output: [[5,7]]
// Explanation: Empty intervals, just add newInterval
```

**Time Complexity:** O(n) - Single pass through intervals  
**Space Complexity:** O(n) - Result array storage


## Q33. Minimum Number of Arrows to Burst Balloons

**Problem:** There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D array `points` where `points[i] = [xstart, xend]` denotes a balloon whose horizontal diameter stretches between `xstart` and `xend`. You do not know the exact y-coordinates of the balloons. Arrows can be shot directly up (vertically) from different points along the x-axis. A balloon with `xstart` and `xend` is burst by an arrow shot at `x` if `xstart <= x <= xend`. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path. Given the array `points`, return the minimum number of arrows that must be shot to burst all balloons.

**Approach:** Sort balloons by end position. Use greedy strategy: shoot arrow at the end of first balloon, which will burst all overlapping balloons. Increment arrows when a balloon starts after current arrow position.

### Solution 1: Greedy - Sort by End (Optimal)
```javascript
function findMinArrowShots(points) {
  if (points.length === 0) return 0;
  
  // Sort by end position
  points.sort((a, b) => a[1] - b[1]);
  
  let arrows = 1;
  let arrowPos = points[0][1]; // Shoot arrow at end of first balloon
  
  for (let i = 1; i < points.length; i++) {
    // If balloon starts after arrow position, need new arrow
    if (points[i][0] > arrowPos) {
      arrows++;
      arrowPos = points[i][1]; // Shoot new arrow at end of this balloon
    }
  }
  
  return arrows;
}

// Test Cases:
// Input: points = [[10,16],[2,8],[1,6],[7,12]]
// Output: 2
// Explanation: Shoot arrows at x=6 and x=11 to burst all balloons

// Input: points = [[1,2],[3,4],[5,6],[7,8]]
// Output: 4
// Explanation: Each balloon requires separate arrow (no overlap)

// Input: points = [[1,2],[2,3],[3,4],[4,5]]
// Output: 2
// Explanation: Shoot arrows at x=2 and x=4 (some overlap)
```

**Time Complexity:** O(n log n) - Sorting dominates  
**Space Complexity:** O(1) - Constant extra space (or O(n) for sorting if not in-place)


---

## Bonus: Important Array Techniques

### Sliding Window

**Concept:** Maintain a moving subarray/substring satisfying a property; grow right, shrink left to restore validity.

```javascript
// Longest substring with at most k distinct characters
function lenAtMostK(s, k) {
  const freq = new Map();
  let left = 0;
  let best = 0;

  for (let right = 0; right < s.length; right++) {
    const char = s[right];
    freq.set(char, (freq.get(char) || 0) + 1);

    while (freq.size > k) {
      const drop = s[left++];
      const next = freq.get(drop) - 1;
      if (next === 0) {
        freq.delete(drop);
      } else {
        freq.set(drop, next);
      }
    }

    best = Math.max(best, right - left + 1);
  }
  return best;
}

// Test Cases:
// Input: s = "eceba", k = 2
// Output: 3
// Explanation: Longest substring with at most 2 distinct characters is "ece" with length 3

// Input: s = "aa", k = 1
// Output: 2
// Explanation: Longest substring with at most 1 distinct character is "aa" with length 2

// Input: s = "abcabcbb", k = 3
// Output: 6
// Explanation: Longest substring with at most 3 distinct characters is "abcabc" with length 6

// Input: s = "abacaba", k = 2
// Output: 4
```

**Time Complexity:** O(n) - Single pass with sliding window  
**Space Complexity:** O(k) - Hash map stores up to k distinct characters


### Two Pointer

**Concept:** Use two indices to traverse from ends or sweep with relative motion to meet constraints.

```javascript
// Two-sum on a sorted array
function twoSumSorted(arr, target) {
  let left = 0;
  let right = arr.length - 1;

  while (left < right) {
    const sum = arr[left] + arr[right];
    if (sum === target) {
      return [left, right];
    }
    if (sum < target) {
      left++;
    } else {
      right--;
    }
  }
  return [-1, -1];
}

// Test Cases:
// Input: arr = [2, 7, 11, 15], target = 9
// Output: [0, 1]

// Input: arr = [2, 3, 4], target = 6
// Output: [0, 2]

// Input: arr = [-1, 0], target = -1
// Output: [0, 1]

// Input: arr = [1, 2, 3, 4], target = 10
// Output: [-1, -1]

// Input: arr = [1], target = 2
// Output: [-1, -1]
```

**Time Complexity:** O(n) - Two pointers traverse from both ends  
**Space Complexity:** O(1) - Only using constant extra variables


### Prefix Sum

**Concept:** Transform range queries to differences of cumulative sums; extend to 2D and counts maps.

```javascript
// Count subarrays with sum equal to k
function subarraySum(nums, k) {
  const count = new Map([[0, 1]]);
  let sum = 0;
  let ans = 0;

  for (const x of nums) {
    sum += x;
    ans += count.get(sum - k) || 0;
    count.set(sum, (count.get(sum) || 0) + 1);
  }
  return ans;
}

// Test Cases:
// Input: nums = [1, 1, 1], k = 2
// Output: 2
// Explanation: Subarrays [1,1] and [1,1] (overlapping) sum to 2

// Input: nums = [1, 2, 3], k = 3
// Output: 2
// Explanation: Subarrays [1,2] and [3] sum to 3

// Input: nums = [1, -1, 0], k = 0
// Output: 3
// Explanation: Subarrays [1,-1], [-1,0], and [0] sum to 0

// Input: nums = [1, 1, 1], k = 0
// Output: 0

// Input: nums = [1], k = 1
// Output: 1
```

**Time Complexity:** O(n) - Single pass through array  
**Space Complexity:** O(n) - Hash map stores prefix sum counts


### Divide & Conquer

**Concept:** Build quad tree from 2D grid; recursively divide grid into 4 quadrants if values differ.

```javascript
function construct(grid) {
  function build(rowStart, rowEnd, colStart, colEnd) {
    if (rowStart === rowEnd) {
      return new Node(grid[rowStart][colStart] === 1, true);
    }
    
    const rowMid = Math.floor((rowStart + rowEnd) / 2);
    const colMid = Math.floor((colStart + colEnd) / 2);
    
    const topLeft = build(rowStart, rowMid, colStart, colMid);
    const topRight = build(rowStart, rowMid, colMid + 1, colEnd);
    const bottomLeft = build(rowMid + 1, rowEnd, colStart, colMid);
    const bottomRight = build(rowMid + 1, rowEnd, colMid + 1, colEnd);
    
    // If all children are leaves with same value, merge
    if (topLeft.isLeaf && topRight.isLeaf && 
        bottomLeft.isLeaf && bottomRight.isLeaf &&
        topLeft.val === topRight.val &&
        topRight.val === bottomLeft.val &&
        bottomLeft.val === bottomRight.val) {
      return new Node(topLeft.val, true);
    }
    
    return new Node(false, false, topLeft, topRight, bottomLeft, bottomRight);
  }
  
  return build(0, grid.length - 1, 0, grid[0].length - 1);
}

// Test Cases:
// Input: grid = [[0,1],[1,0]]
// Output: Quad tree with root and 4 children
// Explanation: Root with 4 children (topLeft: 0, topRight: 1, bottomLeft: 1, bottomRight: 0)

// Input: grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
// Output: Quad tree with merged nodes
// Explanation: Regions with same values are merged into single nodes
```

**Time Complexity:** O(n²) - Visit each cell, but merge reduces nodes  
**Space Complexity:** O(log n) - Recursion depth

