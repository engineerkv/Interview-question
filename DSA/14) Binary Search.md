# Binary Search

## Q159. Search Insert Position

Concept: Find insertion position for target using binary search; return index where target would be inserted.

```javascript
function searchInsert(nums, target) {
  let left = 0, right = nums.length - 1;
  
  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    
    if (nums[mid] === target) {
      return mid;
    } else if (nums[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  
  return left;
}

// Test Cases:
//
// Example 1:
//   Input: nums = [1,3,5,6], target = 5
//   Output: 2
//
// Example 2:
//   Input: nums = [1,3,5,6], target = 2
//   Output: 1
//
// Example 3:
//   Input: nums = [1,3,5,6], target = 7
//   Output: 4
//
// Example 4:
//   Input: nums = [1,3,5,6], target = 0
//   Output: 0
```

Deep Insights:
  - Rule: Binary search for target; return left index when not found; O(log n) time.
  - Real-world: Finding insertion position, search in sorted arrays, lower bound problems.
  - Common mistake: Wrong return value when not found; not handling edge cases correctly.
  - Optimization: O(log n) time optimal; left index is insertion position when target not found.
  - Interview tip: Explain binary search clearly; mention insertion position; ask about duplicates.

Time Complexity: O(log n) - Binary search
Space Complexity: O(1) - Constant extra space

## Q160. Search a 2D Matrix

Concept: Treat 2D matrix as sorted 1D array; convert index to row/col; binary search on flattened array.

```javascript
function searchMatrix(matrix, target) {
  if (!matrix.length || !matrix[0].length) return false;
  
  const m = matrix.length;
  const n = matrix[0].length;
  let left = 0, right = m * n - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    const row = Math.floor(mid / n);
    const col = mid % n;
    const val = matrix[row][col];

    if (val === target) {
      return true;
    } else if (val < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return false;
}

// Test Cases:
//
// Example 1:
//   Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
//   Output: true
//
// Example 2:
//   Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
//   Output: false
```

Deep Insights:
  - Rule: Treat 2D as 1D; convert index to row/col; row = mid/n, col = mid%n; O(log(mn)) time.
  - Real-world: Search in sorted 2D arrays, matrix search problems, coordinate conversion.
  - Common mistake: Wrong row/col conversion; not handling empty matrix; wrong binary search bounds.
  - Optimization: O(log(mn)) time optimal; convert index: row = mid/n, col = mid%n.
  - Interview tip: Explain 2D to 1D conversion clearly; mention coordinate conversion; ask about unsorted matrix.

Time Complexity: O(log(mn)) - Binary search on flattened array
Space Complexity: O(1) - Constant extra space

## Q161. Find Peak Element

Concept: Binary search on array; if mid < right, peak is in right half; else peak is in left half.

```javascript
function findPeakElement(nums) {
  let left = 0, right = nums.length - 1;

  while (left < right) {
    const mid = Math.floor((left + right) / 2);
    
    if (nums[mid] < nums[mid + 1]) {
      left = mid + 1;
    } else {
      right = mid;
    }
  }

  return left;
}

// Test Cases:
//
// Example 1:
//   Input: nums = [1,2,3,1]
//   Output: 2
//   Explanation: 3 is a peak element and index is 2
//
// Example 2:
//   Input: nums = [1,2,1,3,5,6,4]
//   Output: 5
//   Explanation: 6 is a peak element and index is 5
```

Deep Insights:
  - Rule: Binary search on array; if mid < mid+1, peak in right; else peak in left; O(log n) time.
  - Real-world: Finding peaks in data, maximum element search, unimodal functions.
  - Common mistake: Wrong comparison logic; not handling edge cases; wrong binary search condition.
  - Optimization: O(log n) time optimal; compare mid with mid+1; always go toward larger neighbor.
  - Interview tip: Explain peak finding logic clearly; mention comparison strategy; ask about multiple peaks.

Time Complexity: O(log n) - Binary search
Space Complexity: O(1) - Constant extra space

## Q162. Search in Rotated Sorted Array

Concept: Binary search with rotation check; if left half sorted and target in range, search left; else search right.

```javascript
function search(nums, target) {
  let left = 0, right = nums.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    if (nums[mid] === target) {
      return mid;
    }

    // Left half is sorted
    if (nums[left] <= nums[mid]) {
      if (nums[left] <= target && target < nums[mid]) {
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    } 
    // Right half is sorted
    else {
      if (nums[mid] < target && target <= nums[right]) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
  }

  return -1;
}

// Test Cases:
//
// Example 1:
//   Input: nums = [4,5,6,7,0,1,2], target = 0
//   Output: 4
//
// Example 2:
//   Input: nums = [4,5,6,7,0,1,2], target = 3
//   Output: -1
//
// Example 3:
//   Input: nums = [1], target = 0
//   Output: -1
```

Deep Insights:
  - Rule: Check which half is sorted; if target in sorted half range, search there; else search other half; O(log n) time.
  - Real-world: Search in rotated arrays, circular buffer search, pivot finding.
  - Common mistake: Wrong sorted half detection; not checking target in range correctly; edge case handling.
  - Optimization: O(log n) time optimal; check sorted half first; target range check crucial.
  - Interview tip: Explain rotation handling clearly; mention sorted half detection; ask about duplicates.

Time Complexity: O(log n) - Binary search
Space Complexity: O(1) - Constant extra space

## Q163. Find First and Last Position of Element in Sorted Array

Concept: Binary search twice: once for first position, once for last position; adjust bounds accordingly.

```javascript
function searchRange(nums, target) {
  const first = findFirst(nums, target);
  if (first === -1) return [-1, -1];
  const last = findLast(nums, target);
  return [first, last];
}

function findFirst(nums, target) {
  let left = 0, right = nums.length - 1;
  let result = -1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    
    if (nums[mid] === target) {
      result = mid;
      right = mid - 1; // Continue searching left
    } else if (nums[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return result;
}

function findLast(nums, target) {
  let left = 0, right = nums.length - 1;
  let result = -1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    
    if (nums[mid] === target) {
      result = mid;
      left = mid + 1; // Continue searching right
    } else if (nums[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return result;
}

// Test Cases:
//
// Example 1:
//   Input: nums = [5,7,7,8,8,10], target = 8
//   Output: [3,4]
//
// Example 2:
//   Input: nums = [5,7,7,8,8,10], target = 6
//   Output: [-1,-1]
//
// Example 3:
//   Input: nums = [], target = 0
//   Output: [-1,-1]
```

Deep Insights:
  - Rule: Binary search twice for first and last; continue searching left/right when found; O(log n) time.
  - Real-world: Finding range of duplicates, count occurrences, range queries.
  - Common mistake: Not continuing search when found; wrong binary search bounds; edge cases.
  - Optimization: O(log n) time optimal; two binary searches; continue in one direction when found.
  - Interview tip: Explain two-pass search clearly; mention continuing search strategy; ask about optimization.

Time Complexity: O(log n) - Two binary searches
Space Complexity: O(1) - Constant extra space

## Q164. Find Minimum in Rotated Sorted Array

Concept: Binary search for minimum; if mid < right, minimum in left half; else minimum in right half.

```javascript
function findMin(nums) {
  let left = 0, right = nums.length - 1;

  while (left < right) {
    const mid = Math.floor((left + right) / 2);

    // Right half is sorted, minimum is in left half
    if (nums[mid] < nums[right]) {
      right = mid;
    } 
    // Left half is sorted, minimum is in right half
    else {
      left = mid + 1;
    }
  }

  return nums[left];
}

// Test Cases:
//
// Example 1:
//   Input: nums = [3,4,5,1,2]
//   Output: 1
//   Explanation: The original array was [1,2,3,4,5] rotated 3 times
//
// Example 2:
//   Input: nums = [4,5,6,7,0,1,2]
//   Output: 0
//
// Example 3:
//   Input: nums = [11,13,15,17]
//   Output: 11
//   Explanation: Array not rotated
```

Deep Insights:
  - Rule: Binary search for minimum; if mid < right, min in left; else min in right; O(log n) time.
  - Real-world: Finding minimum in rotated arrays, pivot finding, circular buffer problems.
  - Common mistake: Wrong comparison logic; not handling unrotated arrays; edge cases.
  - Optimization: O(log n) time optimal; compare mid with right; minimum always in unsorted half.
  - Interview tip: Explain minimum finding logic clearly; mention comparison strategy; ask about duplicates.

Time Complexity: O(log n) - Binary search
Space Complexity: O(1) - Constant extra space

## Q165. Median of Two Sorted Arrays

Concept: Binary search on smaller array partition; balance left and right halves; median is max of left or avg of max/min.

```javascript
function findMedianSortedArrays(nums1, nums2) {
  if (nums1.length > nums2.length) {
    [nums1, nums2] = [nums2, nums1];
  }

  const m = nums1.length, n = nums2.length;
  let left = 0, right = m;

  while (left <= right) {
    const partition1 = Math.floor((left + right) / 2);
    const partition2 = Math.floor((m + n + 1) / 2) - partition1;

    const maxLeft1 = partition1 === 0 ? -Infinity : nums1[partition1 - 1];
    const minRight1 = partition1 === m ? Infinity : nums1[partition1];
    const maxLeft2 = partition2 === 0 ? -Infinity : nums2[partition2 - 1];
    const minRight2 = partition2 === n ? Infinity : nums2[partition2];

    if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1) {
      if ((m + n) % 2 === 0) {
        return (Math.max(maxLeft1, maxLeft2) + Math.min(minRight1, minRight2)) / 2;
      } else {
        return Math.max(maxLeft1, maxLeft2);
      }
    } else if (maxLeft1 > minRight2) {
      right = partition1 - 1;
    } else {
      left = partition1 + 1;
    }
  }
}

// Test Cases:
//
// Example 1:
//   Input: nums1 = [1,3], nums2 = [2]
//   Output: 2.00000
//   Explanation: Merged array = [1,2,3] and median is 2
//
// Example 2:
//   Input: nums1 = [1,2], nums2 = [3,4]
//   Output: 2.50000
//   Explanation: Merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5
```

Deep Insights:
  - Rule: Binary search on partitions; balance left/right halves; check valid partition; O(log(min(m,n))) time.
  - Real-world: Finding median of two arrays, statistical analysis, divide and conquer.
  - Common mistake: Wrong partition calculation; not handling edge cases; wrong median calculation.
  - Optimization: O(log(min(m,n))) time optimal; binary search on smaller array; partition balancing crucial.
  - Interview tip: Explain partition strategy clearly; mention edge cases; ask about optimization.

Time Complexity: O(log(min(m,n))) - Binary search on smaller array
Space Complexity: O(1) - Constant extra space

