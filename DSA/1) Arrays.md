# Arrays

## Q1. Two Sum

- Concept: Identify two indices summing to target using hash map.

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
```

- Deep Insights:
  - Use single-pass hash map for O(n).
  - Handle duplicates carefully.
  - Prefer indices over values.
  - Watch for negative numbers and zero.

## Q2. Best Time to Buy & Sell Stock

- Concept: Track min price so far; maximize profit.

```javascript
// Example: [7,1,5,3,6,4] -> 5
function maxProfit(prices) {
  let minPrice = Infinity;
  let best = 0;
  for (const p of prices) {
    minPrice = Math.min(minPrice, p);
    best = Math.max(best, p - minPrice);
  }
  return best;
}
```

- Deep Insights:
  - Single pass, O(n) time.
  - Profit resets if price drops below min.
  - No multiple transactions here.
  - Edge: monotonic decreasing arrays.

## Q3. Kadane’s Algorithm (Max Subarray Sum)

- Concept: Dynamic running sum; reset when negative.

```javascript
// Example: [-2,1,-3,4,-1,2,1,-5,4] -> 6
function maxSubArray(nums) {
  let cur = nums[0];
  let best = nums[0];
  for (let i = 1; i < nums.length; i++) {
    cur = Math.max(nums[i], cur + nums[i]);
    best = Math.max(best, cur);
  }
  return best;
}
```

- Deep Insights:
  - O(n) time, O(1) space.
  - Track best and current sums.
  - For all-negative, pick max element.
  - Variant: track indices for subarray.

## Q4. Rotate Array

- Concept: Reverse parts or use cyclic replacements.

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

  reverse(0, n - 1);
  reverse(0, k - 1);
  reverse(k, n - 1);
}
```

- Deep Insights:
  - Use triple-reverse for O(1) space.
  - k %= n to normalize.
  - Be careful with in-place cycles.
  - Left vs right rotation variants.

## Q5. Merge Intervals

- Concept: Sort by start; sweep and merge overlapping intervals.

```javascript
// [[1,3],[2,6],[8,10],[15,18]] -> [[1,6],[8,10],[15,18]]
function merge(intervals) {
  intervals.sort((a, b) => a[0] - b[0]);
  const res = [];
  for (const [s, e] of intervals) {
    if (!res.length || s > res[res.length - 1][1]) res.push([s, e]);
    else res[res.length - 1][1] = Math.max(res[res.length - 1][1], e);
  }
  return res;
}
```

- Deep Insights:
  - Sorting dominates: O(n log n).
  - Merge by comparing with last added.
  - Inclusive vs exclusive endpoints.
  - Stable ordering not required.

## Q6. Largest Element in Array

- Concept: One pass track max or use heap for top-k.

```javascript
function arrayMax(nums) {
  let m = nums[0];
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] > m) m = nums[i];
  }
  return m;
}
```

- Deep Insights:
  - O(n) scan for single max.
  - Quickselect for kth largest.
  - Watch for duplicates.
  - Consider streaming variants.

## Q7. Rearrange array by sign / Dutch Flag

- Concept: Three-way partition by value (0,1,2) using low/mid/high pointers.

```javascript
function sortColors(nums) {
  let low = 0;
  let mid = 0;
  let high = nums.length - 1;

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
```

- Deep Insights:
  - DNF: low/mid/high pointers.
  - In-place, O(1) space.
  - Stable vs unstable partitions.
  - Generalize to k-buckets.

## Q8. Product of Array Except Self

- Concept: Prefix and suffix products without division.

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
  for (let i = n - 1; i >= 0; i--) {
    res[i] *= suf;
    suf *= nums[i];
  }

  return res;
}
```

- Deep Insights:
  - Two passes: left then right.
  - Handle zeros carefully.
  - O(n) time, O(1) extra space.
  - Division version has zero pitfalls.

## Q9. Find Missing Number

- Concept: Use XOR to cancel pairs; works on range 0..n.

```javascript
function missingNumber(nums) {
  const n = nums.length;
  let x = n;
  for (let i = 0; i < n; i++) x ^= i ^ nums[i];
  return x;
}
```

- Deep Insights:
  - XOR avoids overflow.
  - Works for 0..n range.
  - Sort-based is slower O(n log n).
  - Consider duplicates check.

## Q10. Majority Element (Boyer-Moore)

- Concept: Voting algorithm to find > n/2 element.

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
```

- Deep Insights:
  - O(n) time, O(1) space.
  - Verify pass if required.
  - Extend to n/3 with two candidates.
  - Streaming friendly.

## Q11. Maximum Product Subarray

- Concept: Track max/min due to negative flips; swap on negative.

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
```

- Deep Insights:
  - Swap on negative numbers.
  - O(n) time, O(1) space.
  - Zero resets run.
  - Keep global best.

## Q12. Trapping Rain Water

- Concept: Two pointers with left/right max trackers.

```javascript
function trap(height) {
  let left = 0;
  let right = height.length - 1;
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
```

- Deep Insights:
  - O(n) two-pointer beats stacks for simplicity.
  - LeftMax/RightMax comparisons decide moves.
  - Stack solution tracks bars.
  - DP precompute variant exists.

## Q13. Subarray Sum Equals K

- Concept: Prefix sums with hashmap counts.

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
```

- Deep Insights:
  - O(n) time, O(n) space.
  - Zero and negatives supported.
  - Use running sum - k matches.
  - Initialize map with {0:1}.

## Q14. Longest Consecutive Sequence

- Concept: Hash set; start only at sequence heads.

```javascript
function longestConsecutive(nums) {
  const set = new Set(nums);
  let best = 0;
  for (const x of set) {
    if (!set.has(x - 1)) {
      let y = x;
      while (set.has(y)) y++;
      best = Math.max(best, y - x);
    }
  }
  return best;
}
```

- Deep Insights:
  - O(n) expected with set.
  - Only expand when num-1 not in set.
  - Handles gaps efficiently.
  - Avoid sorting O(n log n).

## Q15. Merge Sorted Arrays

- Concept: Two pointers from end for in-place merge.

```javascript
// Merge array b (length n) into a (size m+n) sorted
function mergeSorted(a, m, b, n) {
  let i = m - 1;
  let j = n - 1;
  let k = m + n - 1;

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
```

- Deep Insights:
  - Fill from the back to avoid shifts.
  - Handle leftovers cleanly.
  - Edge: one array empty.
  - Stable if comparing <=.
