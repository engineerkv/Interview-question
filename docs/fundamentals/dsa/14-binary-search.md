---
sidebar_label: "Binary Search"
---
# Binary Search

---

## Q211. 🔎 Search Insert Position

**Problem:** Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. You must write an algorithm with `O(log n)` runtime complexity.

**Approach:** Use binary search. If target found, return index. If not found, `left` index is the insertion position.

### Solution 1: Binary Search (Optimal)

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

  // Insertion position is left
  return left;
}

```

// Test Cases:
// Input: nums = [1,3,5,6], target = 5
// Output: 2

// Input: nums = [1,3,5,6], target = 2
// Output: 1

// Input: nums = [1,3,5,6], target = 7
// Output: 4

// Input: nums = [1,3,5,6], target = 0
// Output: 0

```

**Time Complexity:** O(log n) - Binary search
**Space Complexity:** O(1) - Constant extra space

## Q212. 🔎 Search a 2D Matrix

**Problem:** You are given an `m x n` integer matrix `matrix` with the following two properties:

- Each row is sorted in non-decreasing order.

- The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return `true` if `target` is in `matrix` or `false` otherwise. You must write a solution in `O(log(m * n))` time complexity.

**Approach:** Treat 2D matrix as sorted 1D array. Convert flat index to row/col using: row = mid/n, col = mid%n.

### Solution 1: Binary Search on Flattened Array (Optimal)

```javascript

function searchMatrix(matrix, target) {
  if (!matrix.length || !matrix[0].length) return false;

  const m = matrix.length;
  const n = matrix[0].length;
  let left = 0, right = m * n - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    // Convert flat index to row/col
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

```

// Test Cases:
// Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
// Output: true

// Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
// Output: false

```

**Time Complexity:** O(log(m × n)) - Binary search on flattened array
**Space Complexity:** O(1) - Constant extra space

## Q213. 🔍 Find Peak Element

**Problem:** A peak element is an element that is strictly greater than its neighbors. Given a 0-indexed integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks. You may imagine that `nums[-1] = nums[n] = -∞`. You must write an algorithm that runs in `O(log n)` time.

**Approach:** Use binary search. Compare mid with mid+1. If mid < mid+1, peak is in right half. Otherwise, peak is in left half.

### Solution 1: Binary Search (Optimal)

```javascript
function findPeakElement(nums) {
  let left = 0, right = nums.length - 1;

  while (left < right) {
    const mid = Math.floor((left + right) / 2);

    // If mid < mid+1, peak is in right half
    if (nums[mid] < nums[mid + 1]) {
      left = mid + 1;
    } else {
      // Peak is in left half (including mid)
      right = mid;
    }
  }

  return left;
}

```

// Test Cases:
// Input: nums = [1,2,3,1]
// Output: 2
// Explanation: 3 is a peak element and index is 2

// Input: nums = [1,2,1,3,5,6,4]
// Output: 5
// Explanation: 6 is a peak element and index is 5

```

**Time Complexity:** O(log n) - Binary search
**Space Complexity:** O(1) - Constant extra space

## Q214. 📋 Search in Rotated Sorted Array

**Problem:** There is an integer array `nums` sorted in ascending order (with distinct values). Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index `k` (1 <= k < nums.length) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]` (0-indexed). For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index `3` and become `[4,5,6,7,0,1,2]`. Given the array `nums` after the rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`. You must write an algorithm with `O(log n)` runtime complexity.

**Approach:** Use binary search. Check which half is sorted. If target is in sorted half's range, search there. Otherwise, search the other half.

### Solution 1: Binary Search with Rotation Handling (Optimal)

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
      // Target is in sorted left half
      if (nums[left] <= target && target < nums[mid]) {
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    }
    // Right half is sorted
    else {
      // Target is in sorted right half
      if (nums[mid] < target && target <= nums[right]) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
  }

  return -1;
}

```

// Test Cases:
// Input: nums = [4,5,6,7,0,1,2], target = 0
// Output: 4

// Input: nums = [4,5,6,7,0,1,2], target = 3
// Output: -1

// Input: nums = [1], target = 0
// Output: -1

```

**Time Complexity:** O(log n) - Binary search
**Space Complexity:** O(1) - Constant extra space

## Q215. 📋 Find First and Last Position of Element in Sorted Array

**Problem:** Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value. If `target` is not found in the array, return `[-1, -1]`. You must write an algorithm with `O(log n)` runtime complexity.

**Approach:** Use binary search twice: once to find first position (continue searching left when found), once to find last position (continue searching right when found).

### Solution 1: Two Binary Searches (Optimal)

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

```

// Test Cases:
// Input: nums = [5,7,7,8,8,10], target = 8
// Output: [3,4]

// Input: nums = [5,7,7,8,8,10], target = 6
// Output: [-1,-1]

// Input: nums = [], target = 0
// Output: [-1,-1]

```

**Time Complexity:** O(log n) - Two binary searches
**Space Complexity:** O(1) - Constant extra space

## Q216. 📋 Find Minimum in Rotated Sorted Array

**Problem:** Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:

- `[4,5,6,7,0,1,2]` if it was rotated `4` times.

- `[0,1,2,4,5,6,7]` if it was rotated `7` times.

Notice that rotating an array `[a[0], a[1], a[2], ..., a[n-1]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]`. Given the sorted rotated array `nums` of unique elements, return the minimum element of this array. You must write an algorithm that runs in `O(log n)` time.

**Approach:** Use binary search. Compare mid with right. If mid < right, right half is sorted, minimum is in left half. Otherwise, minimum is in right half.

### Solution 1: Binary Search (Optimal)

```javascript

function findMin(nums) {
  let left = 0, right = nums.length - 1;

  while (left < right) {
    const mid = Math.floor((left + right) / 2);

    // Right half is sorted, minimum is in left half (including mid)
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

```

// Test Cases:
// Input: nums = [3,4,5,1,2]
// Output: 1
// Explanation: The original array was [1,2,3,4,5] rotated 3 times

// Input: nums = [4,5,6,7,0,1,2]
// Output: 0

// Input: nums = [11,13,15,17]
// Output: 11
// Explanation: Array not rotated

```

**Time Complexity:** O(log n) - Binary search
**Space Complexity:** O(1) - Constant extra space

## Q217. 📋 Median of Two Sorted Arrays

**Problem:** Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays. The overall run time complexity should be `O(log (m+n))`.

**Approach:** Use binary search on partitions. Partition both arrays such that left halves have same size as right halves. Check if partition is valid (maxLeft <= minRight). If valid, calculate median from partition boundaries.

### Solution 1: Binary Search on Partitions (Optimal)

```javascript
function findMedianSortedArrays(nums1, nums2) {
  // Ensure nums1 is smaller array
  if (nums1.length > nums2.length) {
    [nums1, nums2] = [nums2, nums1];
  }

  const m = nums1.length, n = nums2.length;
  let left = 0, right = m;

  while (left <= right) {
    const partition1 = Math.floor((left + right) / 2);
    const partition2 = Math.floor((m + n + 1) / 2) - partition1;

    // Get boundary elements
    const maxLeft1 = partition1 === 0 ? -Infinity : nums1[partition1 - 1];
    const minRight1 = partition1 === m ? Infinity : nums1[partition1];
    const maxLeft2 = partition2 === 0 ? -Infinity : nums2[partition2 - 1];
    const minRight2 = partition2 === n ? Infinity : nums2[partition2];

    // Check if partition is valid
    if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1) {
      // Valid partition found
      if ((m + n) % 2 === 0) {
        // Even length: average of two middle elements
        return (Math.max(maxLeft1, maxLeft2) + Math.min(minRight1, minRight2)) / 2;
      } else {
        // Odd length: middle element
        return Math.max(maxLeft1, maxLeft2);
      }
    } else if (maxLeft1 > minRight2) {
      // Partition too far right, move left
      right = partition1 - 1;
    } else {
      // Partition too far left, move right
      left = partition1 + 1;
    }
  }
}

```

// Test Cases:
// Input: nums1 = [1,3], nums2 = [2]
// Output: 2.00000
// Explanation: Merged array = [1,2,3] and median is 2

// Input: nums1 = [1,2], nums2 = [3,4]
// Output: 2.50000
// Explanation: Merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5

```

**Time Complexity:** O(log(min(m,n))) - Binary search on smaller array
**Space Complexity:** O(1) - Constant extra space

---

## 📍 Navigation

