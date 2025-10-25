# 🧩 DSA Interview Notes - LeetCode Top 150

## 🟪 Section 5 — Sorting / Binary Search — Q43-Q52

---

### 43. 🟪 Search in Rotated Sorted Array

**🧠 Concept**

Search in rotated sorted array using modified binary search. Determine which half is sorted and search accordingly.

**💻 Example**

```javascript
function search(nums, target) {
  let left = 0, right = nums.length - 1;
  
  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    if (nums[mid] === target) return mid;
    
    if (nums[left] <= nums[mid]) {
      if (target >= nums[left] && target < nums[mid]) {
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    } else {
      if (target > nums[mid] && target <= nums[right]) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
  }
  return -1;
}
```

**💬 Explanation + Insight**

- **Modified Binary Search** - Handle rotated array logic
- **Two Cases** - Left half sorted or right half sorted
- **Target Range** - Check if target is in sorted half
- **Time Complexity** - O(log n) binary search
- **Space Complexity** - O(1) constant space

---

### 44. 🟪 Find First and Last Position in Sorted Array

**🧠 Concept**

Find first and last occurrence of target using binary search. Use helper functions for first and last positions.

**💻 Example**

```javascript
function searchRange(nums, target) {
  const first = findFirst(nums, target);
  if (first === -1) return [-1, -1];
  const last = findLast(nums, target);
  return [first, last];
}

function findFirst(nums, target) {
  let left = 0, right = nums.length - 1;
  while (left < right) {
    const mid = Math.floor((left + right) / 2);
    if (nums[mid] < target) left = mid + 1;
    else right = mid;
  }
  return nums[left] === target ? left : -1;
}
```

**💬 Explanation + Insight**

- **Two Binary Searches** - One for first, one for last occurrence
- **Leftmost Position** - Find first occurrence of target
- **Rightmost Position** - Find last occurrence of target
- **Time Complexity** - O(log n) two binary searches
- **Space Complexity** - O(1) constant space

---

### 45. 🟪 Search Insert Position

**🧠 Concept**

Find position to insert target in sorted array. Use binary search to find leftmost position.

**💻 Example**

```javascript
function searchInsert(nums, target) {
  let left = 0, right = nums.length;
  
  while (left < right) {
    const mid = Math.floor((left + right) / 2);
    if (nums[mid] < target) {
      left = mid + 1;
    } else {
      right = mid;
    }
  }
  return left;
}
```

**💬 Explanation + Insight**

- **Leftmost Position** - Find where target should be inserted
- **Binary Search** - Divide and conquer approach
- **Insertion Point** - Return position for insertion
- **Time Complexity** - O(log n) binary search
- **Space Complexity** - O(1) constant space

---

### 46. 🟪 Search a 2D Matrix

**🧠 Concept**

Search in 2D matrix where each row is sorted and first element of row is greater than last element of previous row.

**💻 Example**

```javascript
function searchMatrix(matrix, target) {
  const m = matrix.length, n = matrix[0].length;
  let left = 0, right = m * n - 1;
  
  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    const midValue = matrix[Math.floor(mid / n)][mid % n];
    
    if (midValue === target) return true;
    if (midValue < target) left = mid + 1;
    else right = mid - 1;
  }
  return false;
}
```

**💬 Explanation + Insight**

- **Flatten Matrix** - Treat 2D as 1D array
- **Row/Column Calculation** - mid/n for row, mid%n for column
- **Binary Search** - Search in flattened array
- **Time Complexity** - O(log(m*n)) binary search
- **Space Complexity** - O(1) constant space

---

### 47. 🟪 Find Peak Element

**🧠 Concept**

Find peak element where element is greater than its neighbors. Use binary search on the slope.

**💻 Example**

```javascript
function findPeakElement(nums) {
  let left = 0, right = nums.length - 1;
  
  while (left < right) {
    const mid = Math.floor((left + right) / 2);
    if (nums[mid] > nums[mid + 1]) {
      right = mid;
    } else {
      left = mid + 1;
    }
  }
  return left;
}
```

**💬 Explanation + Insight**

- **Peak Definition** - Element greater than neighbors
- **Slope Analysis** - Go towards increasing slope
- **Binary Search** - Eliminate half based on slope
- **Time Complexity** - O(log n) binary search
- **Space Complexity** - O(1) constant space

---

### 48. 🟪 Find Minimum in Rotated Sorted Array

**🧠 Concept**

Find minimum element in rotated sorted array. Compare with rightmost element to determine which half to search.

**💻 Example**

```javascript
function findMin(nums) {
  let left = 0, right = nums.length - 1;
  
  while (left < right) {
    const mid = Math.floor((left + right) / 2);
    if (nums[mid] > nums[right]) {
      left = mid + 1;
    } else {
      right = mid;
    }
  }
  return nums[left];
}
```

**💬 Explanation + Insight**

- **Minimum Element** - Find smallest element in rotated array
- **Right Comparison** - Compare with rightmost element
- **Binary Search** - Eliminate half based on comparison
- **Time Complexity** - O(log n) binary search
- **Space Complexity** - O(1) constant space

---

### 49. 🟪 Kth Largest Element in Array

**🧠 Concept**

Find kth largest element using quick select algorithm. Partition array around pivot and recurse on appropriate half.

**💻 Example**

```javascript
function findKthLargest(nums, k) {
  const quickSelect = (arr, left, right, k) => {
    const pivotIndex = partition(arr, left, right);
    if (pivotIndex === k) return arr[pivotIndex];
    if (pivotIndex < k) return quickSelect(arr, pivotIndex + 1, right, k);
    return quickSelect(arr, left, pivotIndex - 1, k);
  };
  
  return quickSelect(nums, 0, nums.length - 1, nums.length - k);
}
```

**💬 Explanation + Insight**

- **Quick Select** - Modified quicksort for finding kth element
- **Partition** - Rearrange array around pivot
- **Recursive** - Recurse on appropriate half
- **Time Complexity** - O(n) average case
- **Space Complexity** - O(log n) recursion stack

---

### 50. 🟪 Median of Two Sorted Arrays

**🧠 Concept**

Find median of two sorted arrays using binary search. Partition both arrays to find median position.

**💻 Example**

```javascript
function findMedianSortedArrays(nums1, nums2) {
  if (nums1.length > nums2.length) {
    return findMedianSortedArrays(nums2, nums1);
  }
  
  const m = nums1.length, n = nums2.length;
  let left = 0, right = m;
  
  while (left <= right) {
    const partitionX = Math.floor((left + right) / 2);
    const partitionY = Math.floor((m + n + 1) / 2) - partitionX;
    
    const maxLeftX = partitionX === 0 ? -Infinity : nums1[partitionX - 1];
    const minRightX = partitionX === m ? Infinity : nums1[partitionX];
    const maxLeftY = partitionY === 0 ? -Infinity : nums2[partitionY - 1];
    const minRightY = partitionY === n ? Infinity : nums2[partitionY];
    
    if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
      if ((m + n) % 2 === 0) {
        return (Math.max(maxLeftX, maxLeftY) + Math.min(minRightX, minRightY)) / 2;
      } else {
        return Math.max(maxLeftX, maxLeftY);
      }
    } else if (maxLeftX > minRightY) {
      right = partitionX - 1;
    } else {
      left = partitionX + 1;
    }
  }
}
```

**💬 Explanation + Insight**

- **Binary Search** - Search for correct partition
- **Partition Logic** - Ensure left elements <= right elements
- **Median Calculation** - Handle odd/even length cases
- **Time Complexity** - O(log(min(m,n))) binary search
- **Space Complexity** - O(1) constant space

---

### 51. 🟪 Merge Intervals

**🧠 Concept**

Merge overlapping intervals by sorting and merging adjacent intervals that overlap.

**💻 Example**

```javascript
function merge(intervals) {
  if (intervals.length <= 1) return intervals;
  
  intervals.sort((a, b) => a[0] - b[0]);
  const result = [intervals[0]];
  
  for (let i = 1; i < intervals.length; i++) {
    const current = intervals[i];
    const last = result[result.length - 1];
    
    if (current[0] <= last[1]) {
      last[1] = Math.max(last[1], current[1]);
    } else {
      result.push(current);
    }
  }
  
  return result;
}
```

**💬 Explanation + Insight**

- **Sort by Start** - Sort intervals by start time
- **Overlap Check** - Check if current start <= last end
- **Merge Logic** - Update end time to maximum
- **Time Complexity** - O(n log n) due to sorting
- **Space Complexity** - O(1) excluding result array

---

### 52. 🟪 Insert Interval

**🧠 Concept**

Insert new interval into sorted intervals, merging overlapping intervals.

**💻 Example**

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
```

**💬 Explanation + Insight**

- **Three Phases** - Before, merge, after newInterval
- **Overlap Detection** - Check if intervals overlap
- **Merge Logic** - Update start and end times
- **Time Complexity** - O(n) single pass
- **Space Complexity** - O(1) excluding result array

---

*This comprehensive sorting and binary search section covers essential algorithms including rotated array search, interval merging, and advanced binary search techniques.*