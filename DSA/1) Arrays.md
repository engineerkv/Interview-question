# Arrays

## Q1. Two Sum

Concept:
Find two indices summing to target using hash map to track seen numbers and their indices.

Example:
```javascript
// Return indices of two numbers adding up to target
function twoSum(nums, target) {
  const seen = new Map();
  for (let i = 0; i < nums.length; i++) {
    const x = nums[i];
    if (seen.has(target - x)) return [seen.get(target - x), i];
    seen.set(x, i);
  }
}

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

Deep Insights:
- Use single-pass hash map for O(n) time complexity instead of O(n²) brute force.
- Handle duplicates carefully—store indices in map, not just presence.
- Prefer indices over values when problem asks for positions.
- Watch for negative numbers and zero—hash map handles them naturally.
- Edge case: exactly one solution exists, assume valid input always.

## Q2. Best Time to Buy & Sell Stock

Concept:
Find maximum profit from buying and selling once by tracking minimum price and calculating profit for each day.

Example:
```javascript
function maxProfit(prices) {
  let minPrice = Infinity;
  let best = 0;
  for (const p of prices) {
    minPrice = Math.min(minPrice, p);
    best = Math.max(best, p - minPrice);
  }
  return best;
}

// Input: prices = [7, 1, 5, 3, 6, 4]
// Output: 5
// Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5

// Input: prices = [7, 6, 4, 3, 1]
// Output: 0
// Explanation: Prices only decreasing, no profit possible

// Input: prices = [2, 4, 1]
// Output: 2
// Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2
```

**Time Complexity:** O(n) - Single pass through prices array  
**Space Complexity:** O(1) - Only using constant extra variables

Deep Insights:
- Single pass, O(n) time complexity with O(1) space.
- Profit calculation resets conceptually if price drops below current min.
- Only one transaction allowed—buy once, sell once.
- Edge case: monotonic decreasing arrays return 0 profit.
- Keep global maximum profit, update min price as we iterate.

## Q3. Kadane's Algorithm (Max Subarray Sum)

Concept:
Find maximum subarray sum using Kadane's algorithm by maintaining running sum and resetting when negative.

Example:
```javascript
function maxSubArray(nums) {
  let cur = nums[0];
  let best = nums[0];
  for (let i = 1; i < nums.length; i++) {
    cur = Math.max(nums[i], cur + nums[i]);
    best = Math.max(best, cur);
  }
  return best;
}

// Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
// Output: 6
// Explanation: Subarray [4, -1, 2, 1] has the largest sum = 6

// Input: nums = [1]
// Output: 1
// Explanation: Single element is the maximum subarray

// Input: nums = [-2, -1, -3]
// Output: -1
// Explanation: All negative, maximum is the least negative element (-1)
```

**Time Complexity:** O(n) - Single pass through array  
**Space Complexity:** O(1) - Only using constant extra variables

Deep Insights:
- O(n) time complexity, O(1) space—optimal solution.
- Track both best global sum and current running sum.
- For all-negative arrays, pick the maximum single element.
- Variant: track start and end indices to return the actual subarray.

## Q4. Rotate Array

Concept:
Rotate array right by k using triple-reverse technique (reverse all, reverse first k, reverse remaining).

Example:
```javascript
// Rotate right by k
function rotate(nums, k) {
  const n = nums.length;
  k %= n;

  const reverse = (l, r) => {
    while (l < r) {
      [nums[l], nums[r]] = [nums[r], nums[l]];
      l++;
      r--;
    }
  };

  reverse(0, n -1);
  reverse(0, k -1);
  reverse(k, n -1);
}

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

Deep Insights:
- Use triple-reverse for O(1) extra space complexity.
- k %= n normalizes k when it's larger than array length.
- Be careful with in-place cyclic replacements—triple-reverse is cleaner.
- Left vs right rotation variants—right: k, left: n-k.

## Q5. Merge Intervals

Concept:
Merge overlapping intervals by sorting by start time and merging where start ≤ last interval's end.

Example:
```javascript
function merge(intervals) {
  intervals.sort((a, b) => a[0] - b[0]);
  const res = [];
  for (const [s, e] of intervals) {
    if (!res.length || s > res[res.length -1][1]) res.push([s, e]);
    else res[res.length -1][1] = Math.max(res[res.length -1][1], e);
  }
  return res;
}

// Input: intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
// Output: [[1, 6], [8, 10], [15, 18]]
// Explanation: [1, 3] and [2, 6] overlap, merge to [1, 6]

// Input: intervals = [[1, 4], [4, 5]]
// Output: [[1, 5]]
// Explanation: [1, 4] and [4, 5] overlap, merge to [1, 5]

// Input: intervals = [[1, 4], [0, 4]]
// Output: [[0, 4]]
// Explanation: [1, 4] and [0, 4] overlap, merge to [0, 4]
```

**Time Complexity:** O(n log n) - Sorting dominates, then O(n) merge pass  
**Space Complexity:** O(1) or O(n) - O(1) if modifying input, O(n) for result array

Deep Insights:
  - Rule: Sorting dominates at O(n log n); merge by comparing start with last interval's end.
  - Real-world: Calendar scheduling, meeting room allocation, timeline visualization systems.
  - Common mistake: Not sorting first causes incorrect merging; forgetting to merge overlapping intervals with same start.
  - Optimization: In-place merge possible; sorting by start time only is sufficient (end time ordering not needed).
  - Interview tip: Clarify inclusive vs exclusive endpoints; ask about edge cases like [1,2] and [2,3] merging.

## Q6. Largest Element in Array

Concept:
Find largest element by tracking maximum value in single pass through array.

Example:
```javascript
function arrayMax(nums) {
  let m = nums[0];
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] > m) m = nums[i];
  }
  return m;
}

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

Deep Insights:
  - Rule: O(n) scan for single maximum element is optimal; quickselect for kth largest is O(n) average.
  - Real-world: Leaderboard rankings, top-K queries, streaming analytics, real-time metrics tracking.
  - Common mistake: Using sort for single max is O(n log n) waste; watch for duplicates in selection.
  - Optimization: Maintain max in constant space for streaming; quickselect beats full sort for kth element.
  - Interview tip: Ask about kth largest vs single max; streaming variant requires different approach.

## Q7. Rearrange array by sign / Dutch Flag

Concept:
Sort array of 0s, 1s, and 2s using Dutch National Flag algorithm with three pointers.

Example:
```javascript
function sortColors(nums) {
  let low = 0;
  let mid = 0;
  let high = nums.length -1;

  while (mid <= high) {
    if (nums[mid] === 0) {
      [nums[low], nums[mid]] = [nums[mid], nums[low]];
      low++;
      mid++;
    } else if (nums[mid] === 1) {
      mid++;
    } else {
      [nums[mid], nums[high]] = [nums[high], nums[mid]];
      high--;
    }
  }
}

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

Deep Insights:
  - Rule: Dutch National Flag uses three pointers (low/mid/high) for O(n) time, O(1) space partitioning.
  - Real-world: Sorting by priority levels, multi-way partitioning, color sorting algorithms.
  - Common mistake: Moving mid pointer incorrectly; forgetting to increment mid after swapping with low.
  - Optimization: In-place and unstable but efficient; generalize to k-buckets for k distinct values.
  - Interview tip: Explain three-pointer logic clearly; mention stable vs unstable trade-offs.

## Q8. Product of Array Except Self

Concept:
Return array of products of all other elements using two passes (prefix then suffix products).

Example:
```javascript
function productExceptSelf(nums) {
  const n = nums.length;
  const res = new Array(n).fill(1);

  let pref = 1;
  for (let i = 0; i < n; i++) {
    res[i] = pref;
    pref *= nums[i];
  }

  let suf = 1;
  for (let i = n -1; i >= 0; i--) {
    res[i] *= suf;
    suf *= nums[i];
  }

  return res;
}

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

Deep Insights:
  - Rule: Two passes—left (prefix) then right (suffix) products; O(n) time, O(1) extra space.
  - Real-world: Element-wise calculations excluding self, normalization algorithms, matrix operations.
  - Common mistake: Division by zero when using division approach; forgetting zeros make result zero.
  - Optimization: Avoids division entirely; handles zeros correctly; can't use division with zeros present.
  - Interview tip: Ask about zeros first; division approach fails with zeros; this method always works.

## Q9. Find Missing Number

Concept:
Find missing number in array using XOR to cancel pairs between indices 0..n and array elements.

Example:
```javascript
function missingNumber(nums) {
  const n = nums.length;
  let x = n;
  for (let i = 0; i < n; i++) x ^= i ^ nums[i];
  return x;
}

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

Deep Insights:
  - Rule: XOR cancels pairs between indices 0..n and array elements; avoids overflow without arithmetic.
  - Real-world: Finding missing IDs in sequences, database record validation, completion tracking systems.
  - Common mistake: Using sum-based approach can overflow; sort-based is O(n log n) waste; assumes distinct numbers.
  - Optimization: XOR is O(n) vs O(n log n) sort; works for 0..n range with n distinct numbers and one missing.
  - Interview tip: Ask about duplicates first; XOR only works if numbers are distinct; verify range assumptions.

## Q10. Majority Element (Boyer-Moore)

Concept:
Find majority element using Boyer-Moore voting algorithm by tracking candidate and count.

Example:
```javascript
function majorityElement(nums) {
  let cand = 0;
  let cnt = 0;
  for (const x of nums) {
    if (cnt === 0) {
      cand = x;
      cnt = 1;
    } else if (x === cand) cnt++;
    else cnt--;
  }
  return cand;
}

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

Deep Insights:
  - Rule: Boyer-Moore voting tracks candidate and count; O(n) time, O(1) space optimal solution.
  - Real-world: Leader election in distributed systems, voting systems, finding dominant elements in datasets.
  - Common mistake: Not verifying if majority exists; assuming guarantee; forgetting to handle edge cases.
  - Optimization: Streaming friendly—processes elements one at a time; extend to n/3 with two candidates.
  - Interview tip: Ask if majority guaranteed; if not, add verification pass; explain the voting cancellation logic.

## Q11. Maximum Product Subarray

Concept:
Find maximum product subarray by tracking both max and min products (swap on negative numbers).

Example:
```javascript
function maxProduct(nums) {
  let curMax = nums[0];
  let curMin = nums[0];
  let ans = nums[0];
  for (let i = 1; i < nums.length; i++) {
    const x = nums[i];
    if (x < 0) [curMax, curMin] = [curMin, curMax];
    curMax = Math.max(x, curMax * x);
    curMin = Math.min(x, curMin * x);
    ans = Math.max(ans, curMax);
  }
  return ans;
}

// Input: nums = [2, 3, -2, 4]
// Output: 6
// Explanation: Subarray [2, 3] has maximum product = 6

// Input: nums = [-2, 0, -1]
// Output: 0
// Explanation: Maximum product is 0 (from single element or empty subarray)

// Input: nums = [-2, 3, -4]
// Output: 24
// Explanation: Entire array [-2, 3, -4] has maximum product = 24
```

**Time Complexity:** O(n) - Single pass through array  
**Space Complexity:** O(1) - Only using constant extra variables

Deep Insights:
  - Rule: Track both max and min products; swap on negative since negative × min = positive max.
  - Real-world: Maximum profit calculations, signal amplitude detection, financial product analysis.
  - Common mistake: Only tracking max misses cases where two negatives create positive; zero resets product.
  - Optimization: O(n) time, O(1) space optimal; zero resets run; keep global best updated continuously.
  - Interview tip: Ask about negatives and zeros first; explain why we need both max and min products.

## Q12. Trapping Rain Water

Concept:
Calculate trapped rainwater using two pointers tracking left and right max heights.

Example:
```javascript
function trap(height) {
  let left = 0;
  let right = height.length -1;
  let leftMax = 0;
  let rightMax = 0;
  let water = 0;

  while (left < right) {
    if (height[left] < height[right]) {
      leftMax = Math.max(leftMax, height[left]);
      water += leftMax - height[left];
      left++;
    } else {
      rightMax = Math.max(rightMax, height[right]);
      water += rightMax - height[right];
      right--;
    }
  }
  return water;
}

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

Deep Insights:
  - Rule: Two-pointer tracks leftMax/rightMax; move pointer with smaller max; O(n) time, O(1) space.
  - Real-world: Water collection systems, bar chart analysis, elevation mapping, terrain analysis.
  - Common mistake: Using stack adds complexity; DP precompute uses O(n) extra space unnecessarily.
  - Optimization: Two-pointer beats stack for simplicity; cleaner code; DP variant exists but less efficient.
  - Interview tip: Explain why moving smaller-height pointer is safe; ask about edge cases (empty array, all zeros).

## Q13. Subarray Sum Equals K

Concept:
Count subarrays with sum k using prefix sums and hash map tracking running sum counts.

Example:
```javascript
function subarraySum(nums, k) {
  const count = new Map();
  count.set(0, 1);
  let sum = 0;
  let ans = 0;
  for (const x of nums) {
    sum += x;
    if (count.has(sum - k)) ans += count.get(sum - k);
    count.set(sum, (count.get(sum) || 0) + 1);
  }
  return ans;
}

// Input: nums = [1, 1, 1], k = 2
// Output: 2
// Explanation: Subarrays [1,1] and [1,1] (overlapping) sum to 2

// Input: nums = [1, 2, 3], k = 3
// Output: 2
// Explanation: Subarrays [1,2] and [3] sum to 3

// Input: nums = [1, -1, 0], k = 0
// Output: 3
// Explanation: Subarrays [1,-1], [-1,0], and [0] sum to 0
```

**Time Complexity:** O(n) - Single pass through array  
**Space Complexity:** O(n) - Hash map stores up to n prefix sums

Deep Insights:
  - Rule: Prefix sum + hash map; running sum - k matches count; initialize map with {0:1} for subarrays starting at 0.
  - Real-world: Transaction balancing, subarray matching, payment tracking, target sum problems.
  - Common mistake: Forgetting to initialize {0:1}; not handling negative numbers; missing overlapping subarrays.
  - Optimization: O(n) time, O(n) space optimal; handles zeros and negatives; counts all subarrays correctly.
  - Interview tip: Explain why {0:1} initialization is crucial; ask about overlapping subarrays if count is needed.

## Q14. Longest Consecutive Sequence

Concept:
Find longest consecutive sequence using hash set, only expanding from sequence heads (when num-1 not in set).

Example:
```javascript
function longestConsecutive(nums) {
  const set = new Set(nums);
  let best = 0;
  for (const x of set) {
    if (!set.has(x -1)) {
      let y = x;
      while (set.has(y)) y++;
      best = Math.max(best, y - x);
    }
  }
  return best;
}

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

Deep Insights:
  - Rule: Hash set + expand only from sequence heads (when num-1 not in set); O(n) time expected.
  - Real-world: Consecutive ID sequences, date ranges, ordered lists, continuous number tracking.
  - Common mistake: Sorting leads to O(n log n); expanding from every number causes redundant work.
  - Optimization: Each element visited at most twice; handles gaps efficiently; hash set beats sorting.
  - Interview tip: Explain why we only expand from heads; ask about duplicates (handled by Set naturally).

## Q15. Merge Sorted Arrays

Concept:
Merge two sorted arrays in-place using two pointers from the end, filling from back to avoid shifts.

Example:
```javascript
// Merge array b (length n) into a (size m+n) sorted
function mergeSorted(a, m, b, n) {
  let i = m -1;
  let j = n -1;
  let k = m + n -1;

  while (j >= 0) {
    if (i >= 0 && a[i] > b[j]) {
      a[k] = a[i];
      i--;
    } else {
      a[k] = b[j];
      j--;
    }
    k--;
  }
}

// Input: a = [1, 2, 3, 0, 0, 0], m = 3, b = [2, 5, 6], n = 3
// Output: a = [1, 2, 2, 3, 5, 6]
// Explanation: Merge sorted arrays [1,2,3] and [2,5,6]

// Input: a = [1], m = 1, b = [], n = 0
// Output: a = [1]
// Explanation: Array b is empty, a remains unchanged

// Input: a = [0], m = 0, b = [1], n = 1
// Output: a = [1]
// Explanation: Array a is empty, merge b into a
```

**Time Complexity:** O(m + n) - Merge pass through both arrays  
**Space Complexity:** O(1) - In-place merge, constant extra space

Deep Insights:
  - Rule: Two pointers from end, fill from back; prevents overwriting unprocessed elements; O(m+n) time, O(1) space.
  - Real-world: Merging sorted databases, combining sorted lists, merge sort merge step, external sorting.
  - Common mistake: Merging from front causes shifts and overwrites; not handling empty arrays correctly.
  - Optimization: In-place merge optimal; leftovers handled automatically; stable with <= comparison.
  - Interview tip: Always ask about array sizes and available space; explain why back-to-front is safe.

## Q16. Remove Element

Concept:
Remove all instances of val from array in-place using two pointers; return new length.

Example:
```javascript
function removeElement(nums, val) {
  let writeIndex = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== val) {
      nums[writeIndex++] = nums[i];
    }
  }
  return writeIndex;
}

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

Deep Insights:
- Use write pointer to track position; overwrite only non-val elements; O(n) time, O(1) space.
- In-place modification without shifting elements ahead of write pointer.
- Return new length; elements after length may contain old values (acceptable).
- Edge case: empty array returns 0; all elements removed returns 0.
- Interview tip: Explain two-pointer approach; mention order preservation.

## Q17. Remove Duplicates from Sorted Array

Concept:
Remove duplicates in-place from sorted array; return new length using two pointers.

Example:
```javascript
function removeDuplicates(nums) {
  if (nums.length === 0) return 0;
  
  let writeIndex = 1;
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] !== nums[writeIndex - 1]) {
      nums[writeIndex++] = nums[i];
    }
  }
  return writeIndex;
}

// Input: nums = [1,1,2]
// Output: 2, nums = [1,2,_]
// Explanation: Remove duplicates, new length is 2

// Input: nums = [0,0,1,1,1,2,2,3,3,4]
// Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
// Explanation: Remove duplicates, new length is 5

// Input: nums = [1,1,1]
// Output: 1, nums = [1,_,_]
```

**Time Complexity:** O(n) - Single pass through array  
**Space Complexity:** O(1) - In-place modification

Deep Insights:
- Compare current element with last written element; write only when different; O(n) time, O(1) space.
- Array must be sorted; duplicates appear consecutively.
- Write pointer tracks next position for unique element.
- Edge case: empty array returns 0; single element returns 1.
- Interview tip: Explain sorted property usage; mention consecutive duplicates.

## Q18. Remove Duplicates from Sorted Array II

Concept:
Allow at most two occurrences of each element; remove extras in-place; return new length.

Example:
```javascript
function removeDuplicates(nums) {
  if (nums.length <= 2) return nums.length;
  
  let writeIndex = 2;
  for (let i = 2; i < nums.length; i++) {
    if (nums[i] !== nums[writeIndex - 2]) {
      nums[writeIndex++] = nums[i];
    }
  }
  return writeIndex;
}

// Input: nums = [1,1,1,2,2,3]
// Output: 5, nums = [1,1,2,2,3,_]
// Explanation: Keep at most 2 of each element

// Input: nums = [0,0,1,1,1,1,2,3,3]
// Output: 7, nums = [0,0,1,1,2,3,3,_,_]
// Explanation: Keep at most 2 of each element

// Input: nums = [1,1,1,1]
// Output: 2, nums = [1,1,_,_]
```

**Time Complexity:** O(n) - Single pass through array  
**Space Complexity:** O(1) - In-place modification

Deep Insights:
- Compare with element two positions back; write only when different; O(n) time, O(1) space.
- Generalizes to "allow k duplicates" by comparing with nums[writeIndex - k].
- Write pointer tracks next position; first k elements always written.
- Edge case: length <= k returns length; all elements unique returns length.
- Interview tip: Explain k-duplicate generalization; mention sorted property.

## Q19. Best Time to Buy and Sell Stock II

Concept:
Buy and sell multiple times; track profit from all increasing pairs.

Example:
```javascript
function maxProfit(prices) {
  let profit = 0;
  for (let i = 1; i < prices.length; i++) {
    if (prices[i] > prices[i - 1]) {
      profit += prices[i] - prices[i - 1];
    }
  }
  return profit;
}

// Input: prices = [7,1,5,3,6,4]
// Output: 7
// Explanation: Buy on day 2 (1), sell on day 3 (5), buy on day 4 (3), sell on day 5 (6) = 4+3 = 7

// Input: prices = [1,2,3,4,5]
// Output: 4
// Explanation: Buy on day 1, sell on day 5 = 4

// Input: prices = [7,6,4,3,1]
// Output: 0
// Explanation: No profit possible
```

**Time Complexity:** O(n) - Single pass through prices  
**Space Complexity:** O(1) - Constant extra space

Deep Insights:
- Sum all increasing pairs; no limit on transactions; O(n) time, O(1) space.
- Equivalent to buying every dip and selling every peak.
- Capture all positive price differences.
- Edge case: Monotonic decreasing returns 0; monotonic increasing captures all.
- Interview tip: Explain greedy approach; compare with single transaction variant.

### Jump Game

Concept:
Check if can reach end using max jump from each position; track farthest reachable position.

Example:
```javascript
function canJump(nums) {
  let farthest = 0;
  for (let i = 0; i < nums.length; i++) {
    if (i > farthest) return false;
    farthest = Math.max(farthest, i + nums[i]);
    if (farthest >= nums.length - 1) return true;
  }
  return farthest >= nums.length - 1;
}

// Input: nums = [2,3,1,1,4]
// Output: true
// Explanation: Jump from index 0→1→4

// Input: nums = [3,2,1,0,4]
// Output: false
// Explanation: Stuck at index 3

// Input: nums = [0]
// Output: true
// Explanation: Already at end
```

**Time Complexity:** O(n) - Single pass through array  
**Space Complexity:** O(1) - Constant extra space

Deep Insights:
- Track farthest reachable position; return false if current index exceeds farthest; O(n) time, O(1) space.
- Greedy approach: maximize reach at each step.
- If current index unreachable, end unreachable.
- Edge case: Single element returns true; first element zero and length > 1 returns false.
- Interview tip: Explain greedy strategy; mention early termination optimization.

## Q20. Jump Game

Concept:
Check if can reach end using max jump from each position; track farthest reachable position.

Example:
```javascript
function canJump(nums) {
  let farthest = 0;
  for (let i = 0; i < nums.length; i++) {
    if (i > farthest) return false;
    farthest = Math.max(farthest, i + nums[i]);
    if (farthest >= nums.length - 1) return true;
  }
  return farthest >= nums.length - 1;
}

// Input: nums = [2,3,1,1,4]
// Output: true
// Explanation: Jump from index 0→1→4

// Input: nums = [3,2,1,0,4]
// Output: false
// Explanation: Stuck at index 3

// Input: nums = [0]
// Output: true
// Explanation: Already at end
```

**Time Complexity:** O(n) - Single pass through array  
**Space Complexity:** O(1) - Constant extra space

Deep Insights:
- Track farthest reachable position; return false if current index exceeds farthest; O(n) time, O(1) space.
- Greedy approach: maximize reach at each step.
- If current index unreachable, end unreachable.
- Edge case: Single element returns true; first element zero and length > 1 returns false.
- Interview tip: Explain greedy strategy; mention early termination optimization.

## Q21. Jump Game II

Concept:
Find minimum jumps to reach end; track current jump end and farthest reachable; increment jumps when crossing boundary.

Example:
```javascript
function jump(nums) {
  let jumps = 0;
  let currentEnd = 0;
  let farthest = 0;
  
  for (let i = 0; i < nums.length - 1; i++) {
    farthest = Math.max(farthest, i + nums[i]);
    
    if (i === currentEnd) {
      jumps++;
      currentEnd = farthest;
    }
  }
  
  return jumps;
}

// Input: nums = [2,3,1,1,4]
// Output: 2
// Explanation: Jump from index 0→1→4 (2 jumps)

// Input: nums = [2,3,0,1,4]
// Output: 2
// Explanation: Jump from index 0→1→4 (2 jumps)

// Input: nums = [1,1,1,1]
// Output: 3
```

**Time Complexity:** O(n) - Single pass through array  
**Space Complexity:** O(1) - Constant extra space

Deep Insights:
- Track current jump boundary and farthest reachable; increment jumps when crossing boundary; O(n) time, O(1) space.
- Greedy BFS approach: take maximum jump from each level.
- Current jump ends when reaching currentEnd; update to farthest.
- Edge case: Length 1 returns 0; cannot reach end returns -1 (handle in problem).
- Interview tip: Explain BFS-level analogy; mention greedy choice.

## Q22. H-Index

Concept:
Find maximum h where h papers have at least h citations; sort and find first index where citations >= remaining papers.

Example:
```javascript
function hIndex(citations) {
  citations.sort((a, b) => b - a);
  
  for (let i = 0; i < citations.length; i++) {
    if (citations[i] < i + 1) {
      return i;
    }
  }
  
  return citations.length;
}

// Input: citations = [3,0,6,1,5]
// Output: 3
// Explanation: 3 papers have at least 3 citations

// Input: citations = [1,3,1]
// Output: 1
// Explanation: 1 paper has at least 1 citation

// Input: citations = [100]
// Output: 1
```

**Time Complexity:** O(n log n) - Sorting dominates  
**Space Complexity:** O(1) - In-place sort

Deep Insights:
- Sort descending; find first index where citations[i] < i+1; O(n log n) time.
- H-index is maximum h where h papers have ≥h citations.
- After sorting, check if citations[i] >= i+1 (i+1 papers with at least citations[i]).
- Edge case: All zeros returns 0; all high citations returns n.
- Interview tip: Explain h-index concept; mention sorting approach; ask about optimization.

## Q23. Insert Delete GetRandom O(1)

Concept:
Design data structure with O(1) insert, delete, and getRandom; use array + hash map mapping values to indices.

Example:
```javascript
class RandomizedSet {
  constructor() {
    this.arr = [];
    this.map = new Map(); // value -> index
  }

  insert(val) {
    if (this.map.has(val)) return false;
    this.map.set(val, this.arr.length);
    this.arr.push(val);
    return true;
  }

  remove(val) {
    if (!this.map.has(val)) return false;
    const index = this.map.get(val);
    const lastVal = this.arr[this.arr.length - 1];
    
    this.arr[index] = lastVal;
    this.map.set(lastVal, index);
    
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
//
// Example 1:
//   Input: ["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]
//          [[],[1],[2],[2],[],[1],[2],[]]
//   Output: [null,true,false,true,2,true,false,2]
```

**Time Complexity:** O(1) - All operations average case  
**Space Complexity:** O(n) - Array and map storage

Deep Insights:
- Use array for random access; map for O(1) lookup; swap with last element for O(1) delete; O(1) operations.
- Key insight: swap element to delete with last element, then pop.
- Update map when swapping; maintain value→index mapping.
- Edge case: Empty set getRandom undefined; duplicate insert returns false.
- Interview tip: Explain swap-with-last trick; mention map update requirement.

## Q24. Gas Station

Concept:
Find starting gas station to complete circuit; track total gas and current tank; if tank negative, reset start.

Example:
```javascript
function canCompleteCircuit(gas, cost) {
  let totalGas = 0;
  let currentTank = 0;
  let start = 0;
  
  for (let i = 0; i < gas.length; i++) {
    const diff = gas[i] - cost[i];
    totalGas += diff;
    currentTank += diff;
    
    if (currentTank < 0) {
      start = i + 1;
      currentTank = 0;
    }
  }
  
  return totalGas >= 0 ? start : -1;
}

// Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
// Output: 3
// Explanation: Start at station 3, total gas: -2-2-2+3+3 = 0

// Input: gas = [2,3,4], cost = [3,4,3]
// Output: -1
// Explanation: Cannot complete circuit

// Input: gas = [5,1,2,3,4], cost = [4,4,1,5,1]
// Output: 4
```

**Time Complexity:** O(n) - Single pass through stations  
**Space Complexity:** O(1) - Constant extra space

Deep Insights:
- Track total gas surplus; reset start when tank goes negative; O(n) time, O(1) space.
- If total gas < total cost, impossible; otherwise, start exists.
- When tank goes negative, all previous stations cannot be start.
- Edge case: All gas = all cost returns 0; impossible case returns -1.
- Interview tip: Explain greedy reset strategy; mention total surplus check.

## Q25. Candy

Concept:
Distribute candy to children; each child gets at least 1; adjacent higher rating gets more candy; minimize total.

Example:
```javascript
function candy(ratings) {
  const n = ratings.length;
  const candies = new Array(n).fill(1);
  
  // Left to right: if rating higher, give more candy
  for (let i = 1; i < n; i++) {
    if (ratings[i] > ratings[i - 1]) {
      candies[i] = candies[i - 1] + 1;
    }
  }
  
  // Right to left: if rating higher, ensure more candy
  for (let i = n - 2; i >= 0; i--) {
    if (ratings[i] > ratings[i + 1]) {
      candies[i] = Math.max(candies[i], candies[i + 1] + 1);
    }
  }
  
  return candies.reduce((sum, val) => sum + val, 0);
}

// Input: ratings = [1,0,2]
// Output: 5
// Explanation: [2,1,2] = 5 candies

// Input: ratings = [1,2,2]
// Output: 4
// Explanation: [1,2,1] = 4 candies

// Input: ratings = [1,3,4,5,2]
// Output: 11
// Explanation: [1,2,3,4,1] = 11 candies
```

**Time Complexity:** O(n) - Two passes through array  
**Space Complexity:** O(n) - Candies array

Deep Insights:
- Two-pass greedy: left→right for left neighbor constraint; right→left for right neighbor; O(n) time, O(n) space.
- First pass ensures left constraint; second pass ensures right constraint without breaking left.
- Use Math.max to preserve first pass results.
- Edge case: All same ratings returns n; decreasing ratings returns n*(n+1)/2.
- Interview tip: Explain two-pass necessity; mention constraint satisfaction.

## Q26. Two Sum II - Input Array Is Sorted

Concept:
Find two indices in sorted array summing to target using two pointers from both ends.

Example:
```javascript
function twoSum(numbers, target) {
  let left = 0;
  let right = numbers.length - 1;
  
  while (left < right) {
    const sum = numbers[left] + numbers[right];
    if (sum === target) {
      return [left + 1, right + 1]; // 1-indexed
    } else if (sum < target) {
      left++;
    } else {
      right--;
    }
  }
  
  return [];
}

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

Deep Insights:
- Use two pointers from both ends; move left if sum too small, right if too large; O(n) time, O(1) space.
- Array is sorted; exploit sorted property for optimal solution.
- Return 1-indexed positions as specified.
- Edge case: No solution returns empty array; exactly one solution exists.
- Interview tip: Explain sorted property usage; mention 1-indexed requirement.

## Q27. Container With Most Water

Concept:
Find two lines that together with x-axis form container with most water; use two pointers from both ends.

Example:
```javascript
function maxArea(height) {
  let left = 0;
  let right = height.length - 1;
  let maxArea = 0;
  
  while (left < right) {
    const width = right - left;
    const area = Math.min(height[left], height[right]) * width;
    maxArea = Math.max(maxArea, area);
    
    if (height[left] < height[right]) {
      left++;
    } else {
      right--;
    }
  }
  
  return maxArea;
}

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

Deep Insights:
- Use two pointers from both ends; move pointer with smaller height; O(n) time, O(1) space.
- Greedy approach: move smaller height pointer since area is limited by smaller height.
- Width decreases as pointers move closer.
- Edge case: Single element returns 0; all heights equal returns area.
- Interview tip: Explain greedy choice; mention why move smaller height pointer.

## Q28. 3Sum

Concept:
Find all unique triplets that sum to zero; sort array, fix one element, use two pointers for remaining.

Example:
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
        
        // Skip duplicates
        while (left < right && nums[left] === nums[left + 1]) left++;
        while (left < right && nums[right] === nums[right - 1]) right--;
        
        left++;
        right--;
      } else if (sum < 0) {
        left++;
      } else {
        right--;
      }
    }
  }
  
  return result;
}

// Input: nums = [-1,0,1,2,-1,-4]
// Output: [[-1,-1,2],[-1,0,1]]
// Explanation: Triplets that sum to zero

// Input: nums = [0,1,1]
// Output: []
// Explanation: No triplets sum to zero

// Input: nums = [0,0,0]
// Output: [[0,0,0]]
```

**Time Complexity:** O(n²) - Sort O(n log n) + nested loop O(n²)  
**Space Complexity:** O(1) - Excluding result array

Deep Insights:
- Sort array first; fix first element, use two pointers for remaining; skip duplicates; O(n²) time.
- Sort enables two-pointer technique; duplicates handled by skipping.
- Skip duplicates for all three positions.
- Edge case: Less than 3 elements returns empty; all zeros returns one triplet.
- Interview tip: Explain sorting necessity; mention duplicate handling; ask about k-sum generalization.

## Q29. Is Subsequence

Concept:
Check if string s is subsequence of string t using two pointers; greedy approach.

Example:
```javascript
function isSubsequence(s, t) {
  let i = 0;
  let j = 0;
  
  while (i < s.length && j < t.length) {
    if (s[i] === t[j]) {
      i++;
    }
    j++;
  }
  
  return i === s.length;
}

// Input: s = "abc", t = "ahbgdc"
// Output: true
// Explanation: "abc" is subsequence of "ahbgdc"

// Input: s = "axc", t = "ahbgdc"
// Output: false
// Explanation: "axc" is not subsequence of "ahbgdc"

// Input: s = "", t = "ahbgdc"
// Output: true
// Explanation: Empty string is subsequence of any string
```

**Time Complexity:** O(n) - Single pass through t  
**Space Complexity:** O(1) - Constant extra space

Deep Insights:
- Use two pointers; match characters greedily; O(n) time, O(1) space.
- Greedy: match earliest occurrence of each character.
- Move pointer in t forward always; move pointer in s only when match found.
- Edge case: Empty s returns true; s longer than t returns false.
- Interview tip: Explain greedy approach; mention subsequence vs substring.

## Q30. Minimum Size Subarray Sum

Concept:
Find minimum length subarray with sum >= target; use sliding window technique.

Example:
```javascript
function minSubArrayLen(target, nums) {
  let left = 0;
  let minLength = Infinity;
  let currentSum = 0;
  
  for (let right = 0; right < nums.length; right++) {
    currentSum += nums[right];
    
    while (currentSum >= target) {
      minLength = Math.min(minLength, right - left + 1);
      currentSum -= nums[left];
      left++;
    }
  }
  
  return minLength === Infinity ? 0 : minLength;
}

// Input: target = 7, nums = [2,3,1,2,4,3]
// Output: 2
// Explanation: Subarray [4,3] has minimum length 2

// Input: target = 4, nums = [1,4,4]
// Output: 1
// Explanation: Subarray [4] has minimum length 1

// Input: target = 11, nums = [1,1,1,1,1,1,1,1]
// Output: 0
// Explanation: No subarray sums to >= 11
```

**Time Complexity:** O(n) - Each element visited at most twice  
**Space Complexity:** O(1) - Constant extra space

Deep Insights:
- Use sliding window; expand window, shrink when sum >= target; O(n) time, O(1) space.
- Expand window by moving right pointer; shrink by moving left pointer.
- Track minimum length while window sum >= target.
- Edge case: No valid subarray returns 0; sum of all elements < target returns 0.
- Interview tip: Explain sliding window technique; mention two-pointer approach.

## Q31. Summary Ranges

Concept:
Find smallest sorted list of ranges that cover all numbers in array; use two pointers to track ranges.

Example:
```javascript
function summaryRanges(nums) {
  if (nums.length === 0) return [];
  
  const result = [];
  let start = nums[0];
  let end = nums[0];
  
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] === end + 1) {
      end = nums[i];
    } else {
      if (start === end) {
        result.push(`${start}`);
      } else {
        result.push(`${start}->${end}`);
      }
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

// Input: nums = [0,1,2,4,5,7]
// Output: ["0->2","4->5","7"]
// Explanation: Ranges [0,1,2], [4,5], [7]

// Input: nums = [0,2,3,4,6,8,9]
// Output: ["0","2->4","6","8->9"]
// Explanation: Ranges [0], [2,3,4], [6], [8,9]

// Input: nums = []
// Output: []
```

**Time Complexity:** O(n) - Single pass through array  
**Space Complexity:** O(n) - Result array storage

Deep Insights:
- Track start and end of consecutive ranges; format single number or range; O(n) time, O(n) space.
- Check if current number continues range or starts new range.
- Format single number as string; range as "start->end".
- Edge case: Empty array returns empty array; single element returns array with that element.
- Interview tip: Explain range tracking; mention format requirements.

## Q32. Insert Interval

Concept:
Insert new interval into sorted non-overlapping intervals; merge overlapping intervals.

Example:
```javascript
function insert(intervals, newInterval) {
  const result = [];
  let i = 0;
  
  // Add all intervals before newInterval
  while (i < intervals.length && intervals[i][1] < newInterval[0]) {
    result.push(intervals[i]);
    i++;
  }
  
  // Merge overlapping intervals
  while (i < intervals.length && intervals[i][0] <= newInterval[1]) {
    newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
    newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
    i++;
  }
  
  result.push(newInterval);
  
  // Add remaining intervals
  while (i < intervals.length) {
    result.push(intervals[i]);
    i++;
  }
  
  return result;
}

// Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
// Output: [[1,5],[6,9]]
// Explanation: Merge [1,3] and [2,5] into [1,5]

// Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
// Output: [[1,2],[3,10],[12,16]]
// Explanation: Merge [3,5], [6,7], [8,10] and [4,8] into [3,10]

// Input: intervals = [], newInterval = [5,7]
// Output: [[5,7]]
```

**Time Complexity:** O(n) - Single pass through intervals  
**Space Complexity:** O(n) - Result array storage

Deep Insights:
- Three phases: before, merge overlapping, after; O(n) time, O(n) space.
- Before: add intervals ending before newInterval starts.
- Merge: extend newInterval with overlapping intervals.
- After: add remaining intervals.
- Edge case: Empty intervals returns newInterval; no overlap returns intervals with newInterval inserted.
- Interview tip: Explain three-phase approach; mention merge logic.

## Q33. Minimum Number of Arrows to Burst Balloons

Concept:
Find minimum arrows to burst all balloons; sort by end position, greedy approach.

Example:
```javascript
function findMinArrowShots(points) {
  if (points.length === 0) return 0;
  
  points.sort((a, b) => a[1] - b[1]);
  
  let arrows = 1;
  let end = points[0][1];
  
  for (let i = 1; i < points.length; i++) {
    if (points[i][0] > end) {
      arrows++;
      end = points[i][1];
    }
  }
  
  return arrows;
}

// Input: points = [[10,16],[2,8],[1,6],[7,12]]
// Output: 2
// Explanation: Shoot arrows at x=6 and x=11 to burst all balloons

// Input: points = [[1,2],[3,4],[5,6],[7,8]]
// Output: 4
// Explanation: Each balloon requires separate arrow

// Input: points = [[1,2],[2,3],[3,4],[4,5]]
// Output: 2
// Explanation: Shoot arrows at x=2 and x=4
```

**Time Complexity:** O(n log n) - Sorting dominates  
**Space Complexity:** O(1) - Constant extra space

Deep Insights:
- Sort by end position; greedy: shoot arrow at end of first balloon; O(n log n) time.
- Greedy choice: shoot at rightmost end position to burst maximum balloons.
- Increment arrows when balloon starts after current end.
- Edge case: Empty array returns 0; single balloon returns 1.
- Interview tip: Explain greedy strategy; mention sorting by end position.
