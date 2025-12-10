# Arrays

---

## 📍 Navigation

<div align="center">

[Home: README](README.md) • [Next: Strings →](02%29%20Strings.md)

[📋 Cheatsheet](DSA%20Interview%20Cheatsheet.md)

</div>

---

## Q1. ➕ Two Sum

**Problem:** Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice.

**Problem Explanation:** We need to find two distinct indices `i` and `j` such that `nums[i] + nums[j] = target`. The key constraint is that we cannot use the same element twice, meaning we need two different positions in the array.

**Approach:** Use a hash map (dictionary) to store each number and its index as we traverse the array. For each number, calculate its complement (target - current number). If the complement exists in our map, we've found our pair. This approach allows us to solve the problem in a single pass by trading space for time.

**Why this works:** By storing numbers we've already seen along with their indices, we can check in O(1) time if the complement exists. This eliminates the need for nested loops.

### Solution 1: Hash Map (Optimal)

```javascript
function twoSum(nums, target) {
  const numToIndex = new Map(); // Maps number -> its index
  
  for (let currentIndex = 0; currentIndex < nums.length; currentIndex++) {
    const currentNum = nums[currentIndex];
    const complement = target - currentNum;
    
    // Check if complement exists in our map
    if (numToIndex.has(complement)) {
      const complementIndex = numToIndex.get(complement);
      return [complementIndex, currentIndex];
    }
    
    // Store current number and its index for future lookups
    numToIndex.set(currentNum, currentIndex);
  }
  
  return []; // No solution found (shouldn't happen per problem constraints)
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
  // Check all possible pairs
  for (let firstIndex = 0; firstIndex < nums.length; firstIndex++) {
    for (let secondIndex = firstIndex + 1; secondIndex < nums.length; secondIndex++) {
      const firstNum = nums[firstIndex];
      const secondNum = nums[secondIndex];
      
      if (firstNum + secondNum === target) {
        return [firstIndex, secondIndex];
      }
    }
  }
  
  return []; // No solution found
}

```

**Time Complexity:** O(n²) - Nested loops check all n(n-1)/2 pairs
**Space Complexity:** O(1) - Only using constant extra space (no additional data structures)

**When to use:** This approach is simpler to understand but inefficient for large arrays. Use only when space is extremely constrained.

---

## Q2. 💰 Best Time to Buy & Sell Stock

**Problem:** You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

**Problem Explanation:** We can only make one transaction (buy once, sell once). We must buy before selling. The goal is to find the maximum difference between a selling price and a buying price, where the selling day comes after the buying day.

**Approach:** As we iterate through prices, we track the minimum price seen so far (best buying opportunity). For each day, we calculate the profit if we sell on that day (current price - minimum price seen). We keep track of the maximum profit encountered. This greedy approach ensures we always consider the best buying price up to any given point.

**Why this works:** We don't need to check all pairs. If we've seen a lower price earlier, that's always a better buy option. We only need to track the minimum price and calculate potential profit at each step.

### Solution 1: Single Pass (Optimal)

```javascript
function maxProfit(prices) {
  let minBuyPrice = Infinity; // Track the lowest price seen so far (best buy price)
  let maxProfitSoFar = 0;     // Track the maximum profit achievable

  for (const currentPrice of prices) {
    // Update minimum buy price if current price is lower
    minBuyPrice = Math.min(minBuyPrice, currentPrice);
    
    // Calculate profit if we sell at current price and update maximum
    const profitIfSellNow = currentPrice - minBuyPrice;
    maxProfitSoFar = Math.max(maxProfitSoFar, profitIfSellNow);
  }

  return maxProfitSoFar;
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
  let buyDayIndex = 0;      // Pointer for buy day
  let sellDayIndex = 1;     // Pointer for sell day
  let maxProfitSoFar = 0;

  while (sellDayIndex < prices.length) {
    const buyPrice = prices[buyDayIndex];
    const sellPrice = prices[sellDayIndex];
    
    // If selling today is profitable, update max profit
    if (buyPrice < sellPrice) {
      const currentProfit = sellPrice - buyPrice;
      maxProfitSoFar = Math.max(maxProfitSoFar, currentProfit);
    } else {
      // If current price is lower, it's a better buy opportunity
      buyDayIndex = sellDayIndex;
    }
    
    sellDayIndex++; // Move to next day
  }

  return maxProfitSoFar;
}

```

**Time Complexity:** O(n) - Single pass through array, each element visited once
**Space Complexity:** O(1) - Only using constant extra variables (two pointers and one counter)

**When to use:** This approach is more intuitive as it explicitly tracks buy and sell days, making it easier to understand the logic flow.

## Q3. ⚙️ Kadane's Algorithm (Maximum Subarray Sum)

**Problem:** Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum. A subarray is a contiguous part of an array.

**Problem Explanation:** We need to find a contiguous segment of the array that has the maximum sum. The subarray must contain at least one element. For example, in `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`, the maximum subarray is `[4, -1, 2, 1]` with sum 6.

**Approach:** Kadane's algorithm uses dynamic programming thinking. At each position, we decide: should we extend the previous subarray or start a new one? We extend if the previous sum is positive (it adds value), otherwise we start fresh. We track the maximum sum encountered throughout.

**Why this works:** If a subarray sum becomes negative, it will only reduce any future sum. It's better to start a new subarray from the next element. This greedy choice leads to the optimal solution.

### Solution 1: Kadane's Algorithm (Optimal)

```javascript
function maxSubArray(nums) {
  let currentSubarraySum = nums[0]; // Sum of current subarray ending at current index
  let maxSubarraySum = nums[0];     // Maximum sum found so far

  for (let i = 1; i < nums.length; i++) {
    const currentNum = nums[i];
    
    // Either extend previous subarray or start new one
    // Start new if previous sum is negative (would reduce total)
    currentSubarraySum = Math.max(currentNum, currentSubarraySum + currentNum);
    
    // Update global maximum
    maxSubarraySum = Math.max(maxSubarraySum, currentSubarraySum);
  }

  return maxSubarraySum;
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

## Q4. 📋 Rotate Array

**Problem:** Given an array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative. You must do this in-place with O(1) extra space.

**Problem Explanation:** Rotating right by `k` means moving the last `k` elements to the front. For example, rotating `[1, 2, 3, 4, 5]` right by 2 gives `[4, 5, 1, 2, 3]`. We need to do this without using extra space proportional to the array size.

**Approach:** Use the triple-reverse trick! First reverse the entire array, then reverse the first `k` elements, and finally reverse the remaining elements. This magically gives us the rotated array.

**Why this works:** Reversing the whole array puts the last `k` elements at the front, but in reverse order. Reversing the first `k` elements fixes their order. Reversing the rest fixes the order of the remaining elements. It's like flipping a sandwich to get the right order!

### Solution 1: Triple Reverse (Optimal)

```javascript
function rotate(nums, k) {
  const arrayLength = nums.length;
  k %= arrayLength; // Handle cases where k > array length

  const reverse = (startIndex, endIndex) => {
    while (startIndex < endIndex) {
      [nums[startIndex], nums[endIndex] = [nums[endIndex], nums[startIndex];
      startIndex++;
      endIndex--;
    }
  };

  // Step 1: Reverse entire array
  reverse(0, arrayLength - 1);
  // Step 2: Reverse first k elements
  reverse(0, k - 1);
  // Step 3: Reverse remaining elements
  reverse(k, arrayLength - 1);
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
  const arrayLength = nums.length;
  k %= arrayLength;
  let elementsProcessed = 0;

  // Process each cycle until all elements are moved
  for (let cycleStart = 0; elementsProcessed < arrayLength; cycleStart++) {
    let currentIndex = cycleStart;
    let previousValue = nums[cycleStart];

    // Move elements in a cycle
    do {
      const nextIndex = (currentIndex + k) % arrayLength;
      const temp = nums[nextIndex];
      nums[nextIndex] = previousValue;
      previousValue = temp;
      currentIndex = nextIndex;
      elementsProcessed++;
    } while (cycleStart !== currentIndex); // Stop when cycle completes
  }
}

```

**Time Complexity:** O(n) - Each element visited exactly once
**Space Complexity:** O(1) - Only using constant extra variables

**When to use:** This approach directly moves elements to their final positions. Use when you want to understand the rotation process step-by-step.

## Q5. 🔀 Merge Intervals

**Problem:** Given an array of `intervals` where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

**Problem Explanation:** Two intervals overlap if one starts before or at the same time the other ends. For example, `[1, 3]` and `[2, 6]` overlap because 2 ≤ 3. We merge them into `[1, 6]`. We want to combine all overlapping intervals into single intervals.

**Approach:** Sort intervals by their start time first. Then go through them one by one. If the current interval overlaps with the last merged interval (its start is ≤ the last interval's end), merge them by extending the end. Otherwise, add it as a new interval.

**Why this works:** Sorting ensures we process intervals in order. Once sorted, we only need to check if the current interval overlaps with the last merged one. If it does, we merge; if not, we start a new interval. This greedy approach works because all previous intervals are already merged.

### Solution 1: Sort and Merge (Optimal)

```javascript
function merge(intervals) {
  if (intervals.length === 0) return [];

  // Sort by start time so we can process in order
  intervals.sort((a, b) => a[0] - b[0]);

  const mergedIntervals = [];

  for (const [currentStart, currentEnd] of intervals) {
    const lastMerged = mergedIntervals[mergedIntervals.length - 1];
    
    // If no previous interval or current doesn't overlap with last
    if (mergedIntervals.length === 0 || currentStart > lastMerged[1]) {
      mergedIntervals.push([currentStart, currentEnd]);
    } else {
      // Merge: extend the end of last interval
      lastMerged[1] = Math.max(lastMerged[1], currentEnd);
    }
  }

  return mergedIntervals;
}

// Test Cases:
// Input: intervals = [1, 3], [2, 6], [8, 10], [15, 18]
// Output: [1, 6], [8, 10], [15, 18]
// Explanation: [1, 3] and [2, 6] overlap, merge to [1, 6]

// Input: intervals = [1, 4], [4, 5]
// Output: [1, 5]
// Explanation: [1, 4] and [4, 5] overlap (touching at 4), merge to [1, 5]

// Input: intervals = [1, 4], [0, 4]
// Output: [0, 4]
// Explanation: [1, 4] and [0, 4] overlap completely, merge to [0, 4]

// Input: intervals = [1, 3], [2, 6], [8, 10], [15, 18]
// Output: [1, 6], [8, 10], [15, 18]

```

**Time Complexity:** O(n log n) - Sorting dominates, then O(n) merge pass
**Space Complexity:** O(n) - Result array stores merged intervals (worst case: no overlaps)

## Q6. 📋 Largest Element in Array

**Problem:** Given an array `nums`, find and return the largest element in the array.

**Problem Explanation:** Simple problem - just find the biggest number in the array. For `[3, 5, 2, 8, 1]`, the answer is `8`.

**Approach:** Go through the array once, keeping track of the maximum value we've seen so far. Update it whenever we find a larger number.

**Why this works:** We only need to see each element once. By comparing each element with our current maximum, we ensure we always have the largest value found so far.

### Solution 1: Linear Scan (Optimal)

```javascript
function findMax(nums) {
  let maximumValue = nums[0];
  
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] > maximumValue) {
      maximumValue = nums[i];
    }
  }
  
  return maximumValue;
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

## Q7. 🔀 Sort Colors (Dutch National Flag)

**Problem:** Given an array `nums` with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue. We use integers 0, 1, and 2 to represent red, white, and blue respectively.

**Problem Explanation:** We need to sort an array containing only 0s, 1s, and 2s in-place without using a sorting library. The result should have all 0s first, then 1s, then 2s. For example, `[2, 0, 2, 1, 1, 0]` should become `[0, 0, 1, 1, 2, 2]`.

**Approach:** Use the Dutch National Flag algorithm with three pointers. Maintain three regions: `[0, low)` for 0s, `[low, mid)` for 1s, and `(high, n-1]` for 2s. The `mid` pointer scans through the array. When we encounter 0, swap with `low` and advance both. When we encounter 1, just advance `mid`. When we encounter 2, swap with `high` and decrement `high` (but don't advance `mid` since we need to check the swapped element).

**Why this works:** The three-pointer approach maintains three partitions simultaneously. By carefully managing swaps and pointer movements, we can sort in a single pass without extra space.

### Solution 1: Dutch National Flag (Optimal)

```javascript
function sortColors(nums) {
  let zeroPointer = 0;                    // Boundary for 0s (red) - end of 0s region
  let currentPointer = 0;                 // Current element being processed
  let twoPointer = nums.length - 1;       // Boundary for 2s (blue) - start of 2s region

  while (currentPointer <= twoPointer) {
    if (nums[currentPointer] === 0) {
      // Swap 0 to the beginning, expand 0s region
      [nums[zeroPointer], nums[currentPointer] = [nums[currentPointer], nums[zeroPointer];
      zeroPointer++;
      currentPointer++;
    } else if (nums[currentPointer] === 1) {
      // 1 is in correct position, just move forward
      currentPointer++;
    } else {
      // nums[currentPointer] === 2, swap to the end
      [nums[currentPointer], nums[twoPointer] = [nums[twoPointer], nums[currentPointer];
      twoPointer--;
      // Don't increment currentPointer - need to check swapped element
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
  const colorCount = [0, 0, 0]; // Count of 0s, 1s, and 2s

  // Count occurrences of each color
  for (const color of nums) {
    colorCount[color]++;
  }

  // Rebuild array with sorted colors
  let currentIndex = 0;
  for (let colorValue = 0; colorValue <= 2; colorValue++) {
    while (colorCount[colorValue] > 0) {
      nums[currentIndex] = colorValue;
      currentIndex++;
      colorCount[colorValue]--;
    }
  }
}

```

**Time Complexity:** O(n) - Two passes: one to count, one to rebuild
**Space Complexity:** O(1) - Only using constant extra space (array of size 3)

**When to use:** This approach is simpler to understand and implement, but requires two passes. Use when code clarity is more important than minimizing passes.

**Time Complexity:** O(n) - Two passes through array
**Space Complexity:** O(1) - Count array of size 3 is constant

## Q8. 📋 Product of Array Except Self

**Problem:** Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`. The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer. You must write an algorithm that runs in O(n) time and without using the division operator.

**Problem Explanation:** For each position `i`, we need the product of all elements except `nums[i]`. For example, if `nums = [1, 2, 3, 4]`, then `answer[0] = 2×3×4 = 24`, `answer[1] = 1×3×4 = 12`, etc. We cannot use division because it fails when zeros are present.

**Approach:** Use two passes with prefix and suffix products. In the first pass (left to right), store prefix products (product of all elements to the left). In the second pass (right to left), multiply by suffix products (product of all elements to the right). This gives us the product of all elements except the current one.

**Why this works:** `answer[i] = (product of elements before i) × (product of elements after i)`. By computing prefix and suffix products separately, we can construct the answer without division and handle zeros correctly.

### Solution 1: Two Passes with Prefix/Suffix (Optimal)

```javascript
function productExceptSelf(nums) {
  const arrayLength = nums.length;
  const result = new Array(arrayLength).fill(1);

  // First pass: compute prefix products (product of all elements to the left)
  let prefixProduct = 1;
  for (let currentIndex = 0; currentIndex < arrayLength; currentIndex++) {
    result[currentIndex] = prefixProduct;  // Store prefix product
    prefixProduct *= nums[currentIndex];   // Update prefix for next iteration
  }

  // Second pass: multiply by suffix products (product of all elements to the right)
  let suffixProduct = 1;
  for (let currentIndex = arrayLength - 1; currentIndex >= 0; currentIndex--) {
    result[currentIndex] *= suffixProduct;  // Multiply by suffix product
    suffixProduct *= nums[currentIndex];    // Update suffix for next iteration
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

## Q9. 🔍 Find Missing Number

**Problem:** Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

**Problem Explanation:** We have an array of `n` distinct numbers from the range `[0, n]`, which means there are `n+1` possible numbers but only `n` are present. We need to find the one missing number. For example, if `nums = [3, 0, 1]` and `n = 3`, the range is `[0, 3]` and the missing number is `2`.

**Approach:** Use XOR's property that `a ^ a = 0` and `a ^ 0 = a`. XOR all numbers from `0` to `n` with all numbers in the array. All pairs will cancel out, leaving only the missing number. Start with `n` since it's in the range but might not be in the array.

**Why this works:** XOR is commutative and associative. When we XOR all numbers from `0` to `n` with all numbers in the array, every number except the missing one appears twice and cancels out, leaving only the missing number.

### Solution 1: XOR (Optimal)

```javascript
function missingNumber(nums) {
  const arrayLength = nums.length;
  let missingNumber = arrayLength; // Start with n (since range is [0, n])

  // XOR all indices and array values
  // All pairs cancel out except the missing number
  for (let index = 0; index < arrayLength; index++) {
    missingNumber ^= index ^ nums[index];
  }

  return missingNumber;
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

## Q10. 💡 Majority Element (Boyer-Moore)

**Problem:** Given an array `nums` of size `n`, return the majority element. The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

**Problem Explanation:** A majority element appears more than half the time. For example, in `[2, 2, 1, 1, 1, 2, 2]` with `n = 7`, element `2` appears 4 times, which is more than `⌊7/2⌋ = 3`, so `2` is the majority element.

**Approach:** Use Boyer-Moore Voting Algorithm. Think of it as a voting process: each element votes for itself, and votes against others. Track a candidate and a vote count. When count reaches zero, pick a new candidate. Since the majority element appears more than half the time, it will survive this process and be the final candidate.

**Why this works:** If we cancel out each occurrence of the majority element with one occurrence of any other element, the majority element will still remain because it appears more than `n/2` times. The algorithm simulates this cancellation process.

### Solution 1: Boyer-Moore Voting Algorithm (Optimal)

```javascript
function majorityElement(nums) {
  let majorityCandidate = null;
  let voteCount = 0;

  // Phase 1: Find the majority candidate
  for (const currentNum of nums) {
    if (voteCount === 0) {
      // No current candidate or votes exhausted, pick new candidate
      majorityCandidate = currentNum;
      voteCount = 1;
    } else if (currentNum === majorityCandidate) {
      // Current number matches candidate, increment votes
      voteCount++;
    } else {
      // Current number differs, decrement votes (cancellation)
      voteCount--;
    }
  }

  // Phase 2: Verify (only needed if majority not guaranteed)
  // voteCount = 0;
  // for (const num of nums) {
  //   if (num === majorityCandidate) voteCount++;
  // }
  // return voteCount > nums.length / 2 ? majorityCandidate : null;

  return majorityCandidate; // Assuming majority always exists per problem
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
  const elementCount = new Map(); // Maps element -> its count
  const arrayLength = nums.length;
  const majorityThreshold = arrayLength / 2;

  for (const currentNum of nums) {
    const currentCount = (elementCount.get(currentNum) || 0) + 1;
    elementCount.set(currentNum, currentCount);
    
    // Early return when we find majority
    if (currentCount > majorityThreshold) {
      return currentNum;
    }
  }
  
  return null; // Should not reach here if majority exists
}

```

**Time Complexity:** O(n) - Single pass through array (with early return)
**Space Complexity:** O(n) - Hash map stores up to n distinct element counts

**When to use:** This approach is more intuitive and easier to understand. Use when code clarity is preferred and space is not a constraint.

## Q11. 📋 Maximum Product Subarray

**Problem:** Given an integer array `nums`, find the contiguous subarray within an array (containing at least one number) which has the largest product.

**Problem Explanation:** We need to find a contiguous subarray that has the maximum product. Unlike sum, product can become very large or very small quickly, and negative numbers can flip the sign. For example, in `[2, 3, -2, 4]`, the maximum product subarray is `[2, 3]` with product 6.

**Approach:** Track both maximum and minimum products ending at each position. When we encounter a negative number, the current maximum becomes the new minimum (since negative × max = negative), and the current minimum becomes the new maximum (since negative × min = positive). This handles sign flips correctly.

**Why this works:** A negative number can turn a small negative product into a large positive one. By tracking both max and min, we can capture this behavior and ensure we don't miss optimal subarrays.

### Solution 1: Dynamic Programming with Max/Min Tracking (Optimal)

```javascript
function maxProduct(nums) {
  let maxProductEndingHere = nums[0];  // Maximum product ending at current position
  let minProductEndingHere = nums[0];  // Minimum product ending at current position
  let globalMaxProduct = nums[0];      // Overall maximum product found

  for (let i = 1; i < nums.length; i++) {
    const currentNum = nums[i];

    // If current number is negative, swap max and min
    // (negative × max = negative, negative × min = positive)
    if (currentNum < 0) {
      [maxProductEndingHere, minProductEndingHere] = [minProductEndingHere, maxProductEndingHere];
    }

    // Update max and min products ending at current position
    maxProductEndingHere = Math.max(currentNum, maxProductEndingHere * currentNum);
    minProductEndingHere = Math.min(currentNum, minProductEndingHere * currentNum);

    // Update global maximum
    globalMaxProduct = Math.max(globalMaxProduct, maxProductEndingHere);
  }

  return globalMaxProduct;
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

## Q12. 💡 Trapping Rain Water

**Problem:** Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

**Problem Explanation:** Imagine bars of different heights. Water gets trapped between bars. At any position, water trapped equals the minimum of the maximum height to the left and right, minus the current bar height. For example, if heights are `[0,1,0,2,1,0,1,3,2,1,2,1]`, water gets trapped in the valleys.

**Approach:** Use two pointers from both ends. The key insight: water at a position is limited by the smaller of the two maximum heights (left and right). So we move the pointer with the smaller maximum height, because we know the water trapped there is determined by that smaller maximum.

**Why this works:** We always know the limiting factor (the smaller max). By processing from the side with the smaller max, we can calculate water trapped there immediately, since we're guaranteed the other side has at least that height.

### Solution 1: Two Pointers (Optimal)

```javascript
function trap(height) {
  let leftPointer = 0;
  let rightPointer = height.length - 1;
  let leftMaxHeight = 0;
  let rightMaxHeight = 0;
  let totalWaterTrapped = 0;

  while (leftPointer < rightPointer) {
    if (height[leftPointer] < height[rightPointer]) {
      // Process left side - right side is guaranteed to be at least this tall
      leftMaxHeight = Math.max(leftMaxHeight, height[leftPointer]);
      totalWaterTrapped += leftMaxHeight - height[leftPointer];
      leftPointer++;
    } else {
      // Process right side - left side is guaranteed to be at least this tall
      rightMaxHeight = Math.max(rightMaxHeight, height[rightPointer]);
      totalWaterTrapped += rightMaxHeight - height[rightPointer];
      rightPointer--;
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

## Q13. 📋 Subarray Sum Equals K

**Problem:** Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals `k`.

**Problem Explanation:** We need to count all contiguous subarrays whose sum equals `k`. For example, in `[1, 1, 1]` with `k = 2`, there are 2 subarrays: `[1, 1]` at indices 0-1 and `[1, 1]` at indices 1-2.

**Approach:** Use prefix sums with a hash map. The key insight is: if `prefixSum[i] - prefixSum[j] = k`, then the subarray from `j+1` to `i` has sum `k`. For each prefix sum, check if `prefixSum - k` exists in the map. The count of such prefix sums tells us how many subarrays ending at the current position have sum `k`.

**Why this works:** By storing prefix sums and their frequencies, we can quickly find how many previous prefix sums differ by `k` from the current one, which directly gives us the number of valid subarrays.

### Solution 1: Prefix Sum with Hash Map (Optimal)

```javascript
function subarraySum(nums, k) {
  const prefixSumFrequency = new Map(); // Maps prefix sum -> its frequency
  prefixSumFrequency.set(0, 1); // Initialize: empty subarray has sum 0
  let currentPrefixSum = 0;
  let subarrayCount = 0;

  for (const currentNum of nums) {
    currentPrefixSum += currentNum;
    const targetPrefixSum = currentPrefixSum - k;

    // If target prefix sum exists, we found subarrays with sum k
    if (prefixSumFrequency.has(targetPrefixSum)) {
      subarrayCount += prefixSumFrequency.get(targetPrefixSum);
    }

    // Update frequency of current prefix sum
    const currentFrequency = prefixSumFrequency.get(currentPrefixSum) || 0;
    prefixSumFrequency.set(currentPrefixSum, currentFrequency + 1);
  }

  return subarrayCount;
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

## Q14. 💡 Longest Consecutive Sequence

**Problem:** Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence. You must write an algorithm that runs in O(n) time.

**Problem Explanation:** We need to find the longest sequence of consecutive integers. For example, in `[100, 4, 200, 1, 3, 2]`, the longest consecutive sequence is `[1, 2, 3, 4]` with length 4. The numbers don't need to be in order in the original array.

**Approach:** Use a hash set for O(1) lookups. The key optimization is to only start expanding sequences from "sequence heads" - numbers where `num - 1` is not in the set. This ensures each element is visited at most twice (once to check if it's a head, once during expansion), giving us O(n) time complexity.

**Why this works:** By only expanding from sequence heads, we avoid redundant work. If we expanded from every number, we'd visit elements multiple times. Starting only from heads ensures each consecutive sequence is explored exactly once.

### Solution 1: Hash Set with Sequence Head Detection (Optimal)

```javascript
function longestConsecutive(nums) {
  if (nums.length === 0) return 0;

  const numberSet = new Set(nums); // O(1) lookup for numbers
  let longestSequenceLength = 0;

  for (const currentNum of numberSet) {
    // Only expand from sequence heads (start of a consecutive sequence)
    // A number is a head if (num - 1) is not in the set
    if (!numberSet.has(currentNum - 1)) {
      let sequenceStart = currentNum;
      let currentSequenceLength = 1;

      // Expand sequence forward as long as consecutive numbers exist
      while (numberSet.has(sequenceStart + 1)) {
        sequenceStart++;
        currentSequenceLength++;
      }

      longestSequenceLength = Math.max(longestSequenceLength, currentSequenceLength);
    }
  }

  return longestSequenceLength;
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

## Q15. 📋 Merge Sorted Arrays

**Problem:** You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively. Merge `nums2` into `nums1` as one sorted array. The final sorted array should not be returned by the function, but instead be stored inside the array `nums1`. `nums1` has a length of `m + n`, where the last `n` elements are set to 0 and should be ignored.

**Problem Explanation:** We need to merge two sorted arrays into one sorted array, but we must do it in-place in `nums1`. The trick is that `nums1` has extra space at the end (filled with zeros). We can't merge from the front because we'd overwrite unprocessed elements in `nums1`.

**Approach:** Merge from the back! Start from the end of both arrays and fill `nums1` from right to left. This way, we use the empty space at the end and never overwrite unprocessed elements.

**Why this works:** By working backwards, we use the extra space in `nums1` first. Since we're placing the largest elements first, we never overwrite elements we haven't processed yet. It's like filling a container from the bottom up!

### Solution 1: Two Pointers from End (Optimal)

```javascript
function merge(nums1, m, nums2, n) {
  let nums1Pointer = m - 1;      // Last element in nums1
  let nums2Pointer = n - 1;      // Last element in nums2
  let mergePosition = m + n - 1; // Position to fill in merged array

  // Merge from the end, placing largest elements first
  while (nums2Pointer >= 0) {
    if (nums1Pointer >= 0 && nums1[nums1Pointer] > nums2[nums2Pointer]) {
      nums1[mergePosition] = nums1[nums1Pointer];
      nums1Pointer--;
    } else {
      nums1[mergePosition] = nums2[nums2Pointer];
      nums2Pointer--;
    }
    mergePosition--;
  }
  // If nums1Pointer >= 0, remaining elements are already in correct position
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

## Q16. 🗑️ Remove Element

**Problem:** Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` in-place. The relative order of the elements may be changed. Return `k` after placing the final result in the first `k` slots of `nums`.

**Problem Explanation:** We need to remove all instances of `val` from the array in-place. For example, removing `3` from `[3, 2, 2, 3]` should give us `[2, 2]` with length 2. We don't care about what's left after the valid elements.

**Approach:** Use two pointers - one reads through the array, one writes only valid elements. When we find an element that's not `val`, we write it to the write position and advance both pointers. When we find `val`, we skip it (only advance the read pointer).

**Why this works:** By keeping a separate write pointer, we can overwrite the array as we go. Valid elements get written to their final positions in one pass, and we don't need to shift elements.

### Solution 1: Two Pointers (Optimal)

```javascript
function removeElement(nums, val) {
  let writeIndex = 0; // Position to write next valid element

  for (let readIndex = 0; readIndex < nums.length; readIndex++) {
    // Only write elements that are not equal to val
    if (nums[readIndex] !== val) {
      nums[writeIndex] = nums[readIndex];
      writeIndex++;
    }
    // If nums[readIndex] === val, we skip it (don't write, don't advance writeIndex)
  }

  return writeIndex; // New length of array
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

## Q17. 📋 Remove Duplicates from Sorted Array

**Problem:** Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Return `k` after placing the final result in the first `k` slots of `nums`.

**Problem Explanation:** Since the array is sorted, duplicates appear next to each other. We need to keep only one copy of each unique element. For example, `[1, 1, 2]` becomes `[1, 2]` with length 2.

**Approach:** Use two pointers. The write pointer tracks where to place the next unique element. The read pointer scans through the array. Since it's sorted, we know we've seen a new unique element when `nums[readIndex] !== nums[writeIndex - 1]`.

**Why this works:** Because the array is sorted, all duplicates are adjacent. We only need to check if the current element is different from the last unique element we wrote. This makes it a simple one-pass solution.

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

## Q18. 📋 Remove Duplicates from Sorted Array II

**Problem:** Given an integer array `nums` sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same. Return `k` after placing the final result in the first `k` slots of `nums`.

**Problem Explanation:** Similar to Q17, but now we can keep up to 2 copies of each element. For example, `[1, 1, 1, 2, 2, 3]` becomes `[1, 1, 2, 2, 3]` with length 5.

**Approach:** Use two pointers. The key is to compare the current element with the element two positions back in our written array. If they're different, we can safely write the current element (it won't create more than 2 duplicates).

**Why this works:** By checking two positions back, we ensure that if we write the current element, we'll have at most 2 copies total. If `nums[i] === nums[writeIndex - 2]`, writing it would create a third copy, so we skip it.

### Solution 1: Two Pointers with K=2 Check (Optimal)

```javascript
function removeDuplicates(nums) {
  if (nums.length <= 2) return nums.length;

  let writeIndex = 2; // First two elements are always valid

  for (let readIndex = 2; readIndex < nums.length; readIndex++) {
    // Compare with element two positions back in written array
    // If different, safe to write (won't create more than 2 duplicates)
    if (nums[readIndex] !== nums[writeIndex - 2]) {
      nums[writeIndex] = nums[readIndex];
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

## Q19. 💰 Best Time to Buy and Sell Stock II

**Problem:** You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `i`th day. On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day. Find and return the maximum profit you can achieve.

**Problem Explanation:** Unlike Q2 where we can only buy and sell once, here we can make multiple transactions. We want to maximize total profit by buying low and selling high as many times as possible.

**Approach:** Use a greedy strategy - capture every price increase! If the price goes up from day to day, that's profit we can capture. Sum all positive differences between consecutive days. This is like buying every dip and selling every peak.

**Why this works:** If prices go up, we profit. If they go down, we don't lose money (we just don't buy). By capturing every increase, we get maximum profit. We don't need to worry about when to buy/sell - just capture all the ups!

### Solution 1: Greedy - Sum All Positive Differences (Optimal)

```javascript
function maxProfit(prices) {
  let totalProfit = 0;

  for (let day = 1; day < prices.length; day++) {
    const priceIncrease = prices[day] - prices[day - 1];
    
    // Capture all positive price increases
    if (priceIncrease > 0) {
      totalProfit += priceIncrease;
    }
  }

  return totalProfit;
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

## Q20. 💡 Jump Game

**Problem:** You are given an integer array `nums`. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position. Return `true` if you can reach the last index, or `false` otherwise.

**Problem Explanation:** Starting at index 0, we can jump up to `nums[i]` positions forward from index `i`. We need to check if we can reach the last index. For example, with `[2, 3, 1, 1, 4]`, we can jump from 0→1→4, so we can reach the end.

**Approach:** Use a greedy approach - track the farthest position we can reach. As we go through the array, if we ever reach an index that's beyond our farthest reachable position, we're stuck and can't reach the end. Otherwise, keep updating the farthest position we can reach.

**Why this works:** We don't need to know the exact path - we just need to know if we can reach each position. By tracking the farthest reachable position, we can determine if the end is reachable without exploring all paths.

### Solution 1: Greedy - Track Farthest Reachable (Optimal)

```javascript
function canJump(nums) {
  let farthestReachable = 0; // Farthest index we can reach

  for (let currentIndex = 0; currentIndex < nums.length; currentIndex++) {
    // If current index is beyond our reach, we're stuck
    if (currentIndex > farthestReachable) return false;

    // Update farthest position we can reach from current index
    const reachableFromHere = currentIndex + nums[currentIndex];
    farthestReachable = Math.max(farthestReachable, reachableFromHere);

    // Early exit: if we can reach the end, we're done
    if (farthestReachable >= nums.length - 1) return true;
  }

  return farthestReachable >= nums.length - 1;
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

## Q21. 💡 Jump Game II

**Problem:** You are given a 0-indexed array of integers `nums` of length `n`. You are initially positioned at `nums[0]`. Each element `nums[i]` represents the maximum length of a forward jump from index `i`. Return the minimum number of jumps to reach `nums[n - 1]`. The test cases are generated such that you can reach `nums[n - 1]`.

**Problem Explanation:** Similar to Q20, but now we need the minimum number of jumps to reach the end. For example, with `[2, 3, 1, 1, 4]`, we can reach the end in 2 jumps: 0→1→4.

**Approach:** Think of it like BFS levels. Each "level" represents positions reachable with the same number of jumps. Track the boundary of the current level (`currentEnd`) and the farthest we can reach in the next level. When we cross the current boundary, we've taken one jump and move to the next level.

**Why this works:** This greedy approach always jumps as far as possible at each level, which minimizes the number of jumps. We don't need to explore all paths - we just need to know the farthest we can reach with each jump.

### Solution 1: Greedy BFS (Optimal)

```javascript
function jump(nums) {
  let jumpCount = 0;
  let currentLevelEnd = 0;  // Boundary of current jump level
  let farthestInNextLevel = 0;  // Farthest position reachable in next level

  for (let currentIndex = 0; currentIndex < nums.length - 1; currentIndex++) {
    // Update farthest position reachable in next level
    const reachableFromHere = currentIndex + nums[currentIndex];
    farthestInNextLevel = Math.max(farthestInNextLevel, reachableFromHere);

    // When we reach the end of current level, take a jump
    if (currentIndex === currentLevelEnd) {
      jumpCount++;
      currentLevelEnd = farthestInNextLevel; // Move to next level
    }
  }

  return jumpCount;
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

## Q22. 📇 H-Index

**Problem:** Given an array of integers `citations` where `citations[i]` is the number of citations a researcher received for their `i`th paper, return the researcher's h-index. The h-index is defined as the maximum value of `h` such that the given researcher has published at least `h` papers that have each been cited at least `h` times.

**Problem Explanation:** The h-index measures research impact. If a researcher has h-index of 3, it means they have at least 3 papers with at least 3 citations each. For example, with citations `[3, 0, 6, 1, 5]`, the h-index is 3 because there are 3 papers (with 3, 5, 6 citations) that have at least 3 citations.

**Approach:** Sort citations in descending order. Then find the largest position `i` where `citations[i] >= i + 1`. This means we have at least `i + 1` papers with at least `i + 1` citations each.

**Why this works:** After sorting, `citations[i]` represents the `(i+1)`th most cited paper. If `citations[i] >= i + 1`, we have at least `i + 1` papers with at least `i + 1` citations, so h-index is at least `i + 1`.

### Solution 1: Sorting (Optimal)

```javascript
function hIndex(citations) {
  // Sort in descending order
  citations.sort((a, b) => b - a);

  for (let index = 0; index < citations.length; index++) {
    const paperCount = index + 1; // Number of papers we're considering
    const citationCount = citations[index]; // Citations of current paper
    
    // If this paper has fewer citations than paper count, h-index is previous count
    if (citationCount < paperCount) {
      return index; // h-index is the number of papers before this one
    }
  }

  // All papers qualify - h-index equals total number of papers
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

## Q23. 🗑️ Insert Delete GetRandom O(1)

**Problem:** Implement the `RandomizedSet` class:

- `RandomizedSet()` Initializes the `RandomizedSet` object.
- `bool insert(int val)` Inserts an item `val` into the set if not present. Returns `true` if the item was not present, `false` otherwise.
- `bool remove(int val)` Removes an item `val` from the set if present. Returns `true` if the item was present, `false` otherwise.
- `int getRandom()` Returns a random element from the current set of elements. Each element must have the same probability of being returned.

**Problem Explanation:** We need a data structure that supports O(1) insert, delete, and getRandom operations. The challenge is that hash sets give O(1) insert/delete but not random access, while arrays give O(1) random access but O(n) delete.

**Approach:** Combine both! Use an array for O(1) random access and a hash map to track each value's index. For deletion, swap the element with the last element, then pop - this keeps deletion O(1) while maintaining array integrity.

**Why this works:** Arrays give us O(1) random access. Hash maps give us O(1) lookup. By swapping with the last element before deletion, we avoid shifting all elements, keeping deletion O(1).

### Solution 1: Array + Hash Map (Optimal)

```javascript
class RandomizedSet {
  constructor() {
    this.values = [];              // Array for O(1) random access
    this.valueToIndex = new Map(); // Map value -> its index in array
  }

  insert(val) {
    // If value already exists, return false
    if (this.valueToIndex.has(val)) return false;

    // Add to end of array and track its index
    this.valueToIndex.set(val, this.values.length);
    this.values.push(val);
    return true;
  }

  remove(val) {
    // If value doesn't exist, return false
    if (!this.valueToIndex.has(val)) return false;

    const indexToRemove = this.valueToIndex.get(val);
    const lastValue = this.values[this.values.length - 1];

    // Swap with last element to avoid shifting
    this.values[indexToRemove] = lastValue;
    this.valueToIndex.set(lastValue, indexToRemove);

    // Remove last element (now the duplicate)
    this.values.pop();
    this.valueToIndex.delete(val);
    return true;
  }

  getRandom() {
    const randomIndex = Math.floor(Math.random() * this.values.length);
    return this.values[randomIndex];
  }
}

// Test Cases:
// Input: ["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"], [],[1],[2],[2],[],[1],[2],[]
// Output: [null,true,false,true,2,true,false,2]

```

**Time Complexity:** O(1) - All operations average case
**Space Complexity:** O(n) - Array and map storage

## Q24. 💡 Gas Station

**Problem:** There are `n` gas stations along a circular route, where the amount of gas at the `i`th station is `gas[i]`. You have a car with an unlimited gas tank and it costs `cost[i]` of gas to travel from the `i`th station to its next `(i + 1)`th station. You begin the journey with an empty tank at one of the gas stations. Given two integer arrays `gas` and `cost`, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return `-1`. If there exists a solution, it is guaranteed to be unique.

**Problem Explanation:** We need to find a starting gas station that allows us to complete a full circle. At each station, we get `gas[i]` and spend `cost[i]` to reach the next station. If we can't make it from a station, we need to try starting from a later station.

**Approach:** First check if total gas >= total cost (otherwise impossible). Then use a greedy approach: if our tank goes negative starting from a station, all stations before that can't be valid starts (we'd run out of gas even earlier). So we reset the start to the next station whenever the tank goes negative.

**Why this works:** If we can't reach station `j` starting from station `i`, we also can't reach `j` starting from any station between `i` and `j` (we'd have even less gas). This allows us to skip checking those stations.

### Solution 1: Greedy with Total Surplus Check (Optimal)

```javascript
function canCompleteCircuit(gas, cost) {
  let totalSurplus = 0;    // Total gas surplus (gas - cost)
  let currentTank = 0;     // Current tank level
  let startStation = 0;    // Potential starting station

  for (let station = 0; station < gas.length; station++) {
    const netGas = gas[station] - cost[station]; // Gas gained/lost at this station
    totalSurplus += netGas;
    currentTank += netGas;

    // If tank goes negative, we can't reach here from current start
    // Reset start to next station (all previous stations are invalid)
    if (currentTank < 0) {
      startStation = station + 1;
      currentTank = 0; // Reset tank
    }
  }

  // If total surplus is negative, no solution exists
  return totalSurplus >= 0 ? startStation : -1;
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

## Q25. 💡 Candy

**Problem:** There are `n` children standing in a line. Each child is assigned a rating value given in the integer array `ratings`. You are giving candies to these children subjected to the following requirements:

- Each child must have at least one candy.
- Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the candies to the children.

**Problem Explanation:** We need to give candies such that higher-rated children get more than their neighbors. For example, with ratings `[1, 0, 2]`, we need `[2, 1, 2]` candies (child 0 needs more than child 1, child 2 needs more than child 1).

**Approach:** Use two passes. First pass (left to right): if a child has higher rating than left neighbor, give them one more candy. Second pass (right to left): if a child has higher rating than right neighbor, give them at least one more than the right neighbor (use `Math.max` to preserve first pass results).

**Why this works:** The two constraints (left and right neighbors) are independent. We satisfy them separately in two passes, then take the maximum to satisfy both constraints simultaneously.

### Solution 1: Two-Pass Greedy (Optimal)

```javascript
function candy(ratings) {
  const childCount = ratings.length;
  const candies = new Array(childCount).fill(1); // Everyone gets at least 1

  // Pass 1: Left to right - satisfy "higher than left neighbor" constraint
  for (let i = 1; i < childCount; i++) {
    if (ratings[i] > ratings[i - 1]) {
      candies[i] = candies[i - 1] + 1;
    }
  }

  // Pass 2: Right to left - satisfy "higher than right neighbor" constraint
  for (let i = childCount - 2; i >= 0; i--) {
    if (ratings[i] > ratings[i + 1]) {
      // Use max to preserve first pass results
      candies[i] = Math.max(candies[i], candies[i + 1] + 1);
    }
  }

  return candies.reduce((total, count) => total + count, 0);
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

## Q26. 📋 Two Sum II - Input Array Is Sorted

**Problem:** Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`. Return the indices of the two numbers, `index1` and `index2`, added by one as an integer array `[index1, index2]` of length 2.

**Problem Explanation:** Same as Q1, but the array is sorted! This makes it easier - we can use two pointers instead of a hash map. For example, in `[2, 7, 11, 15]` with target 9, we find `[2, 7]` at indices 1 and 2 (1-indexed).

**Approach:** Use two pointers from both ends. Since the array is sorted, if the sum is too small, we need a larger number (move left pointer right). If the sum is too large, we need a smaller number (move right pointer left).

**Why this works:** The sorted property allows us to make intelligent decisions. We can eliminate half the search space with each comparison, making it O(n) instead of O(n²).

### Solution 1: Two Pointers (Optimal)

```javascript
function twoSum(numbers, target) {
  let leftPointer = 0;
  let rightPointer = numbers.length - 1;

  while (leftPointer < rightPointer) {
    const currentSum = numbers[leftPointer] + numbers[rightPointer];

    if (currentSum === target) {
      // Return 1-indexed positions
      return [leftPointer + 1, rightPointer + 1];
    } else if (currentSum < target) {
      // Sum too small, need larger number - move left pointer right
      leftPointer++;
    } else {
      // Sum too large, need smaller number - move right pointer left
      rightPointer--;
    }
  }

  return []; // Should not reach here (problem guarantees solution)
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

## Q27. 💡 Container With Most Water

**Problem:** You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`th line are `(i, 0)` and `(i, height[i])`. Find two lines that together with the x-axis form a container, such that the container contains the most water. Return the maximum amount of water a container can store.

**Problem Explanation:** We need to find two vertical lines that form a container holding the most water. The water area is `min(height[left], height[right]) × width`. For example, with heights `[1,8,6,2,5,4,8,3,7]`, the maximum area is 49 (between indices 1 and 8).

**Approach:** Use two pointers from both ends. The area is limited by the shorter line. Move the pointer with the smaller height because: (1) area is limited by the smaller height, (2) width decreases, so we need to try to find a taller line, and (3) keeping the taller line gives us a chance at a better area.

**Why this works:** If we move the pointer with the larger height, the area can only decrease (width decreases, height stays same or decreases). By moving the smaller height pointer, we might find a taller line that compensates for the width loss.

### Solution 1: Two Pointers (Optimal)

```javascript
function maxArea(height) {
  let leftPointer = 0;
  let rightPointer = height.length - 1;
  let maxWaterArea = 0;

  while (leftPointer < rightPointer) {
    const containerWidth = rightPointer - leftPointer;
    const containerHeight = Math.min(height[leftPointer], height[rightPointer]);
    const currentArea = containerWidth * containerHeight;
    maxWaterArea = Math.max(maxWaterArea, currentArea);

    // Move pointer with smaller height (area is limited by smaller height)
    if (height[leftPointer] < height[rightPointer]) {
      leftPointer++;
    } else {
      rightPointer--;
    }
  }

  return maxWaterArea;
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

## Q28. ➕ 3Sum

**Problem:** Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`. Notice that the solution set must not contain duplicate triplets.

**Problem Explanation:** We need to find all unique triplets that sum to zero. For example, in `[-1, 0, 1, 2, -1, -4]`, we have triplets `[-1, -1, 2]` and `[-1, 0, 1]`. We can't have duplicate triplets (same numbers in same order).

**Approach:** Sort the array first. Fix the first element, then use two pointers (like Two Sum) for the remaining two elements. Skip duplicates for all three positions to avoid duplicate triplets.

**Why this works:** Sorting allows us to use two pointers and skip duplicates efficiently. By fixing one element and using two pointers for the rest, we reduce the problem from O(n³) to O(n²).

### Solution 1: Sort + Two Pointers (Optimal)

```javascript
function threeSum(nums) {
  nums.sort((a, b) => a - b); // Sort to enable two pointers and duplicate skipping
  const triplets = [];

  for (let firstIndex = 0; firstIndex < nums.length - 2; firstIndex++) {
    // Skip duplicate first elements
    if (firstIndex > 0 && nums[firstIndex] === nums[firstIndex - 1]) continue;

    let leftPointer = firstIndex + 1;
    let rightPointer = nums.length - 1;

    while (leftPointer < rightPointer) {
      const currentSum = nums[firstIndex] + nums[leftPointer] + nums[rightPointer];

      if (currentSum === 0) {
        triplets.push([nums[firstIndex], nums[leftPointer], nums[rightPointer]);

        // Skip duplicates for second and third elements
        while (leftPointer < rightPointer && nums[leftPointer] === nums[leftPointer + 1]) {
          leftPointer++;
        }
        while (leftPointer < rightPointer && nums[rightPointer] === nums[rightPointer - 1]) {
          rightPointer--;
        }

        leftPointer++;
        rightPointer--;
      } else if (currentSum < 0) {
        leftPointer++; // Need larger sum
      } else {
        rightPointer--; // Need smaller sum
      }
    }
  }

  return triplets;
}

// Test Cases:
// Input: nums = [-1,0,1,2,-1,-4]
// Output: [-1,-1,2],[-1,0,1]
// Explanation: Triplets that sum to zero

// Input: nums = [0,1,1]
// Output: []
// Explanation: No triplets sum to zero

// Input: nums = [0,0,0]
// Output: [0,0,0]
// Explanation: Single triplet with all zeros

```

**Time Complexity:** O(n²) - Sort O(n log n) + nested loop O(n²)
**Space Complexity:** O(1) - Excluding result array (or O(n) for sorting if not in-place)

## Q29. 💡 Is Subsequence

**Problem:** Given two strings `s` and `t`, return `true` if `s` is a subsequence of `t`, or `false` otherwise. A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.

**Problem Explanation:** A subsequence means we can delete some characters from `t` to get `s`, but we must keep the relative order. For example, "abc" is a subsequence of "ahbgdc" because we can delete 'h', 'g', 'd' to get "abc".

**Approach:** Use two pointers - one for each string. Greedily match characters of `s` in order within `t`. Move the `s` pointer only when we find a match, always move the `t` pointer.

**Why this works:** We're looking for characters of `s` in order within `t`. By moving through `t` and matching characters of `s` as we find them, we verify if `s` is a subsequence. If we match all characters of `s`, it's a subsequence.

### Solution 1: Two Pointers (Optimal)

```javascript
function isSubsequence(s, t) {
  let sPointer = 0; // Pointer for string s
  let tPointer = 0; // Pointer for string t

  while (sPointer < s.length && tPointer < t.length) {
    // If characters match, move s pointer (found one character of s)
    if (s[sPointer] === t[tPointer]) {
      sPointer++;
    }
    // Always move t pointer (scanning through t)
    tPointer++;
  }

  // If we matched all characters of s, it's a subsequence
  return sPointer === s.length;
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

## Q30. 📋 Minimum Size Subarray Sum

**Problem:** Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a subarray whose sum is greater than or equal to `target`. If there is no such subarray, return `0`.

**Problem Explanation:** We need to find the shortest contiguous subarray whose sum is at least `target`. For example, with `nums = [2, 3, 1, 2, 4, 3]` and `target = 7`, the answer is 2 (subarray `[4, 3]`).

**Approach:** Use a sliding window. Expand the window by moving the right pointer until the sum >= target. Then shrink from the left while the sum is still >= target, tracking the minimum length.

**Why this works:** Once we have a valid window, we try to make it smaller by moving the left pointer. This ensures we find the minimum length subarray. The sliding window technique efficiently explores all possible subarrays.

### Solution 1: Sliding Window (Optimal)

```javascript
function minSubArrayLen(target, nums) {
  let windowStart = 0;
  let windowSum = 0;
  let minSubarrayLength = Infinity;

  for (let windowEnd = 0; windowEnd < nums.length; windowEnd++) {
    windowSum += nums[windowEnd]; // Expand window

    // Shrink window while sum is still >= target
    while (windowSum >= target) {
      const currentWindowLength = windowEnd - windowStart + 1;
      minSubarrayLength = Math.min(minSubarrayLength, currentWindowLength);
      windowSum -= nums[windowStart]; // Remove leftmost element
      windowStart++; // Shrink window
    }
  }

  return minSubarrayLength === Infinity ? 0 : minSubarrayLength;
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

## Q31. ➕ Summary Ranges

**Problem:** You are given a sorted unique integer array `nums`. A range `[a,b]` is the set of all integers from `a` to `b` (inclusive). Return the smallest sorted list of ranges that cover all the numbers in the array exactly. Each range `[a,b]` in the list should be output as:

- `"a->b"` if `a != b`
- `"a"` if `a == b`

**Problem Explanation:** We need to represent consecutive numbers as ranges. For example, `[0, 1, 2, 4, 5, 7]` becomes `["0->2", "4->5", "7"]` - consecutive numbers are grouped into ranges, single numbers are shown as-is.

**Approach:** Track the start and end of the current range. As we iterate, if the next number is consecutive (end + 1), extend the range. Otherwise, add the current range and start a new one.

**Why this works:** Since the array is sorted and unique, we can detect gaps by checking if `nums[i] === end + 1`. This allows us to group consecutive numbers efficiently.

### Solution 1: Range Tracking (Optimal)

```javascript
function summaryRanges(nums) {
  if (nums.length === 0) return [];

  const ranges = [];
  let rangeStart = nums[0];
  let rangeEnd = nums[0];

  for (let i = 1; i < nums.length; i++) {
    if (nums[i] === rangeEnd + 1) {
      // Consecutive number, extend current range
      rangeEnd = nums[i];
    } else {
      // Gap found, add current range and start new one
      if (rangeStart === rangeEnd) {
        ranges.push(`${rangeStart}`);
      } else {
        ranges.push(`${rangeStart}->${rangeEnd}`);
      }
      rangeStart = rangeEnd = nums[i];
    }
  }

  // Add the last range
  if (rangeStart === rangeEnd) {
    ranges.push(`${rangeStart}`);
  } else {
    ranges.push(`${rangeStart}->${rangeEnd}`);
  }

  return ranges;
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

## Q32. 💡 Insert Interval

**Problem:** You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [starti, endi]` represent the start and the end of the `i`th interval and `intervals` is sorted in ascending order by `starti`. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval. Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `starti` and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary). Return `intervals` after the insertion.

**Problem Explanation:** We need to insert a new interval into a sorted list of non-overlapping intervals, merging any overlapping intervals. For example, inserting `[2, 5]` into `[1, 3], [6, 9]` gives `[1, 5], [6, 9]` because `[2, 5]` overlaps with `[1, 3]`.

**Approach:** Three phases: (1) Add all intervals that end before the new interval starts, (2) Merge all intervals that overlap with the new interval, (3) Add all remaining intervals.

**Why this works:** Since intervals are sorted, we can process them in order. Intervals before the new one don't overlap. Intervals that overlap with the new one can be merged by taking the minimum start and maximum end. Remaining intervals come after.

### Solution 1: Three-Phase Approach (Optimal)

```javascript
function insert(intervals, newInterval) {
  const result = [];
  let currentIndex = 0;

  // Phase 1: Add intervals that end before newInterval starts (no overlap)
  while (currentIndex < intervals.length && intervals[currentIndex][1] < newInterval[0]) {
    result.push(intervals[currentIndex]);
    currentIndex++;
  }

  // Phase 2: Merge all intervals that overlap with newInterval
  while (currentIndex < intervals.length && intervals[currentIndex][0] <= newInterval[1]) {
    // Merge by taking minimum start and maximum end
    newInterval[0] = Math.min(newInterval[0], intervals[currentIndex][0]);
    newInterval[1] = Math.max(newInterval[1], intervals[currentIndex][1]);
    currentIndex++;
  }
  result.push(newInterval); // Add merged interval

  // Phase 3: Add remaining intervals (all come after newInterval)
  while (currentIndex < intervals.length) {
    result.push(intervals[currentIndex]);
    currentIndex++;
  }

  return result;
}

// Test Cases:
// Input: intervals = [1,3],[6,9], newInterval = [2,5]
// Output: [1,5],[6,9]
// Explanation: Merge [1,3] and [2,5] into [1,5]

// Input: intervals = [1,2],[3,5],[6,7],[8,10],[12,16], newInterval = [4,8]
// Output: [1,2],[3,10],[12,16]
// Explanation: Merge [3,5], [6,7], [8,10] and [4,8] into [3,10]

// Input: intervals = [], newInterval = [5,7]
// Output: [5,7]
// Explanation: Empty intervals, just add newInterval

```

**Time Complexity:** O(n) - Single pass through intervals
**Space Complexity:** O(n) - Result array storage

## Q33. ➡️ Minimum Number of Arrows to Burst Balloons

**Problem:** There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D array `points` where `points[i] = [xstart, xend]` denotes a balloon whose horizontal diameter stretches between `xstart` and `xend`. You do not know the exact y-coordinates of the balloons. Arrows can be shot directly up (vertically) from different points along the x-axis. A balloon with `xstart` and `xend` is burst by an arrow shot at `x` if `xstart <= x <= xend`. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path. Given the array `points`, return the minimum number of arrows that must be shot to burst all balloons.

**Problem Explanation:** This is essentially the interval scheduling problem. We want to find the minimum number of points (arrows) needed to cover all intervals (balloons). For example, with balloons `[10,16],[2,8],[1,6],[7,12]`, we need 2 arrows (at x=6 and x=11).

**Approach:** Sort balloons by their end position. Use a greedy strategy: shoot an arrow at the end of the first balloon. This arrow will burst all balloons that start before or at this position. When we encounter a balloon that starts after the arrow position, we need a new arrow.

**Why this works:** By shooting at the end of a balloon, we maximize the number of overlapping balloons we can burst. This greedy choice (shoot as far right as possible while still hitting the current balloon) leads to the minimum number of arrows.

### Solution 1: Greedy - Sort by End (Optimal)

```javascript
function findMinArrowShots(points) {
  if (points.length === 0) return 0;

  // Sort balloons by end position
  points.sort((a, b) => a[1] - b[1]);

  let arrowCount = 1;
  let currentArrowPosition = points[0][1]; // Shoot first arrow at end of first balloon

  for (let i = 1; i < points.length; i++) {
    const balloonStart = points[i][0];
    const balloonEnd = points[i][1];

    // If balloon starts after current arrow position, need new arrow
    if (balloonStart > currentArrowPosition) {
      arrowCount++;
      currentArrowPosition = balloonEnd; // Shoot new arrow at end of this balloon
    }
    // Otherwise, current arrow can burst this balloon (it overlaps)
  }

  return arrowCount;
}

// Test Cases:
// Input: points = [10,16],[2,8],[1,6],[7,12]
// Output: 2
// Explanation: Shoot arrows at x=6 and x=11 to burst all balloons

// Input: points = [1,2],[3,4],[5,6],[7,8]
// Output: 4
// Explanation: Each balloon requires separate arrow (no overlap)

// Input: points = [1,2],[2,3],[3,4],[4,5]
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
  const count = new Map([0, 1]);
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
// Input: grid = [0,1],[1,0]
// Output: Quad tree with root and 4 children
// Explanation: Root with 4 children (topLeft: 0, topRight: 1, bottomLeft: 1, bottomRight: 0)

// Input: grid = [1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]
// Output: Quad tree with merged nodes
// Explanation: Regions with same values are merged into single nodes

```

**Time Complexity:** O(n²) - Visit each cell, but merge reduces nodes
**Space Complexity:** O(log n) - Recursion depth

---

## 📍 Navigation

<div align="center">

[Home: README](README.md) • [Next: Strings →](02%29%20Strings.md)

[📋 Cheatsheet](DSA%20Interview%20Cheatsheet.md)

</div>
