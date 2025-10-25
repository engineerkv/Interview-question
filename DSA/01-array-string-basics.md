# 🧩 DSA Interview Notes - LeetCode Top 150

## 🟦 Section 1 — Array/String Basics — Q1-Q17

---

### 1. 🟦 Remove Duplicates from Sorted Array

**🧠 Concept**

Remove duplicates from sorted array in-place, returning new length. Use two pointers to track current position and next unique element.

**💻 Example**

```javascript
function removeDuplicates(nums) {
  if (nums.length === 0) return 0;
  
  let i = 0;
  for (let j = 1; j < nums.length; j++) {
    if (nums[j] !== nums[i]) {
      i++;
      nums[i] = nums[j];
    }
  }
  return i + 1;
}
```

**💬 Explanation + Insight**

- **Two Pointers** - One for current position, one for scanning
- **In-place** - Modify array without extra space
- **Sorted Array** - Duplicates are adjacent, easy to detect
- **Time Complexity** - O(n) single pass through array
- **Space Complexity** - O(1) constant extra space

---

### 2. 🟦 Remove Element

**🧠 Concept**

Remove all instances of a value from array in-place, returning new length. Use two pointers to overwrite elements.

**💻 Example**

```javascript
function removeElement(nums, val) {
  let i = 0;
  for (let j = 0; j < nums.length; j++) {
    if (nums[j] !== val) {
      nums[i] = nums[j];
      i++;
    }
  }
  return i;
}
```

**💬 Explanation + Insight**

- **Two Pointers** - One for write position, one for read position
- **In-place** - Overwrite elements instead of creating new array
- **Efficient** - Single pass through array
- **Time Complexity** - O(n) linear time
- **Space Complexity** - O(1) constant space

---

### 3. 🟦 Remove Duplicates from Sorted Array II

**🧠 Concept**

Remove duplicates allowing at most 2 occurrences of each element. Use two pointers with counter for occurrences.

**💻 Example**

```javascript
function removeDuplicates(nums) {
  if (nums.length <= 2) return nums.length;
  
  let i = 1;
  for (let j = 2; j < nums.length; j++) {
    if (nums[j] !== nums[i-1]) {
      i++;
      nums[i] = nums[j];
    }
  }
  return i + 1;
}
```

**💬 Explanation + Insight**

- **Allow Duplicates** - Keep at most 2 occurrences
- **Two Pointers** - Track write position and scan position
- **Comparison** - Compare with element at i-1 position
- **Time Complexity** - O(n) single pass
- **Space Complexity** - O(1) constant space

---

### 4. 🟦 Merge Sorted Array

**🧠 Concept**

Merge two sorted arrays in-place. Start from end of arrays to avoid overwriting elements.

**💻 Example**

```javascript
function merge(nums1, m, nums2, n) {
  let i = m - 1;
  let j = n - 1;
  let k = m + n - 1;
  
  while (i >= 0 && j >= 0) {
    if (nums1[i] > nums2[j]) {
      nums1[k] = nums1[i];
      i--;
    } else {
      nums1[k] = nums2[j];
      j--;
    }
    k--;
  }
  
  while (j >= 0) {
    nums1[k] = nums2[j];
    j--;
    k--;
  }
}
```

**💬 Explanation + Insight**

- **In-place Merge** - Use existing space in nums1
- **Backward Merge** - Start from end to avoid overwriting
- **Three Pointers** - Track positions in both arrays and result
- **Time Complexity** - O(m + n) linear time
- **Space Complexity** - O(1) constant space

---

### 5. 🟦 Product of Array Except Self

**🧠 Concept**

Calculate product of all elements except current element without using division. Use prefix and suffix products.

**💻 Example**

```javascript
function productExceptSelf(nums) {
  const result = new Array(nums.length);
  
  // Calculate prefix products
  result[0] = 1;
  for (let i = 1; i < nums.length; i++) {
    result[i] = result[i-1] * nums[i-1];
  }
  
  // Calculate suffix products and multiply
  let suffix = 1;
  for (let i = nums.length - 1; i >= 0; i--) {
    result[i] *= suffix;
    suffix *= nums[i];
  }
  
  return result;
}
```

**💬 Explanation + Insight**

- **No Division** - Avoid division by zero issues
- **Prefix/Suffix** - Use left and right products
- **Two Passes** - First pass for prefix, second for suffix
- **Time Complexity** - O(n) two passes
- **Space Complexity** - O(1) excluding output array

---

### 6. 🟦 Majority Element

**🧠 Concept**

Find element that appears more than n/2 times. Use Boyer-Moore voting algorithm for O(1) space.

**💻 Example**

```javascript
function majorityElement(nums) {
  let candidate = nums[0];
  let count = 1;
  
  for (let i = 1; i < nums.length; i++) {
    if (count === 0) {
      candidate = nums[i];
      count = 1;
    } else if (nums[i] === candidate) {
      count++;
    } else {
      count--;
    }
  }
  
  return candidate;
}
```

**💬 Explanation + Insight**

- **Boyer-Moore** - Voting algorithm for majority element
- **Cancel Out** - Different elements cancel each other
- **Guaranteed** - Majority element will survive
- **Time Complexity** - O(n) single pass
- **Space Complexity** - O(1) constant space

---

### 7. 🟦 Rotate Array

**🧠 Concept**

Rotate array to the right by k steps. Use reverse technique: reverse entire array, then reverse first k and last n-k elements.

**💻 Example**

```javascript
function rotate(nums, k) {
  k = k % nums.length;
  reverse(nums, 0, nums.length - 1);
  reverse(nums, 0, k - 1);
  reverse(nums, k, nums.length - 1);
}

function reverse(nums, start, end) {
  while (start < end) {
    [nums[start], nums[end]] = [nums[end], nums[start]];
    start++;
    end--;
  }
}
```

**💬 Explanation + Insight**

- **Reverse Technique** - Three reverses to rotate array
- **Modulo** - Handle k > array length
- **In-place** - No extra space needed
- **Time Complexity** - O(n) linear time
- **Space Complexity** - O(1) constant space

---

### 8. 🟦 H-Index

**🧠 Concept**

H-index is the maximum value h such that h papers have at least h citations each. Sort array and find first position where citation >= position.

**💻 Example**

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
```

**💬 Explanation + Insight**

- **Sort Descending** - Arrange citations in descending order
- **Linear Search** - Find first position where citation < position
- **H-index Logic** - Position represents number of papers
- **Time Complexity** - O(n log n) due to sorting
- **Space Complexity** - O(1) constant space

---

### 9. 🟦 Trapping Rain Water

**🧠 Concept**

Calculate trapped water between bars. Use two pointers from both ends, track max height on each side.

**💻 Example**

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

**💬 Explanation + Insight**

- **Two Pointers** - Start from both ends
- **Max Height Tracking** - Track maximum height on each side
- **Water Calculation** - Water trapped = min(leftMax, rightMax) - current height
- **Time Complexity** - O(n) single pass
- **Space Complexity** - O(1) constant space

---

### 10. 🟦 Roman to Integer

**🧠 Concept**

Convert Roman numerals to integer. Handle subtractive cases (IV, IX, XL, XC, CD, CM) by checking if current value is less than next value.

**💻 Example**

```javascript
function romanToInt(s) {
  const roman = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 };
  let result = 0;
  
  for (let i = 0; i < s.length; i++) {
    if (i < s.length - 1 && roman[s[i]] < roman[s[i + 1]]) {
      result -= roman[s[i]];
    } else {
      result += roman[s[i]];
    }
  }
  return result;
}
```

**💬 Explanation + Insight**

- **Subtractive Cases** - IV = 4, IX = 9, XL = 40, etc.
- **Look Ahead** - Check if current value < next value
- **Subtract or Add** - Subtract if subtractive, add otherwise
- **Time Complexity** - O(n) single pass
- **Space Complexity** - O(1) constant space

---

### 11. 🟦 Integer to Roman

**🧠 Concept**

Convert integer to Roman numerals. Use array of values and symbols, subtract largest possible value at each step.

**💻 Example**

```javascript
function intToRoman(num) {
  const values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
  const symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'];
  let result = '';
  
  for (let i = 0; i < values.length; i++) {
    while (num >= values[i]) {
      result += symbols[i];
      num -= values[i];
    }
  }
  return result;
}
```

**💬 Explanation + Insight**

- **Greedy Approach** - Use largest possible value at each step
- **Predefined Values** - Include subtractive cases in values array
- **While Loop** - Keep subtracting same value until impossible
- **Time Complexity** - O(1) constant time (max 13 iterations)
- **Space Complexity** - O(1) constant space

---

### 12. 🟦 Length of Last Word

**🧠 Concept**

Find length of last word in string. Trim whitespace and find last space, or use split and get last element.

**💻 Example**

```javascript
function lengthOfLastWord(s) {
  s = s.trim();
  let length = 0;
  
  for (let i = s.length - 1; i >= 0; i--) {
    if (s[i] === ' ') {
      break;
    }
    length++;
  }
  return length;
}
```

**💬 Explanation + Insight**

- **Trim Whitespace** - Remove leading and trailing spaces
- **Backward Iteration** - Start from end of string
- **Count Characters** - Count until space is found
- **Time Complexity** - O(n) linear time
- **Space Complexity** - O(1) constant space

---

### 13. 🟦 Longest Common Prefix

**🧠 Concept**

Find longest common prefix among all strings. Compare characters position by position across all strings.

**💻 Example**

```javascript
function longestCommonPrefix(strs) {
  if (strs.length === 0) return '';
  
  for (let i = 0; i < strs[0].length; i++) {
    const char = strs[0][i];
    for (let j = 1; j < strs.length; j++) {
      if (i >= strs[j].length || strs[j][i] !== char) {
        return strs[0].substring(0, i);
      }
    }
  }
  return strs[0];
}
```

**💬 Explanation + Insight**

- **Character by Character** - Compare each position across all strings
- **Early Termination** - Stop when mismatch found
- **First String** - Use first string as reference
- **Time Complexity** - O(S) where S is sum of all characters
- **Space Complexity** - O(1) constant space

---

### 14. 🟦 Reverse Words in a String

**🧠 Concept**

Reverse order of words in string. Split into words, reverse array, join with spaces.

**💻 Example**

```javascript
function reverseWords(s) {
  return s.trim().split(/\s+/).reverse().join(' ');
}
```

**💬 Explanation + Insight**

- **Trim Whitespace** - Remove leading and trailing spaces
- **Split by Spaces** - Use regex to handle multiple spaces
- **Reverse Array** - Reverse order of words
- **Join with Spaces** - Reconstruct string
- **Time Complexity** - O(n) linear time
- **Space Complexity** - O(n) for split array

---

### 15. 🟦 Zigzag Conversion

**🧠 Concept**

Convert string to zigzag pattern and read row by row. Use array of strings for each row, track direction.

**💻 Example**

```javascript
function convert(s, numRows) {
  if (numRows === 1) return s;
  
  const rows = new Array(numRows).fill('');
  let currentRow = 0;
  let goingDown = false;
  
  for (const char of s) {
    rows[currentRow] += char;
    if (currentRow === 0 || currentRow === numRows - 1) {
      goingDown = !goingDown;
    }
    currentRow += goingDown ? 1 : -1;
  }
  
  return rows.join('');
}
```

**💬 Explanation + Insight**

- **Row Tracking** - Use array to store each row
- **Direction Change** - Toggle direction at top and bottom
- **Zigzag Pattern** - Move down then up
- **Time Complexity** - O(n) single pass
- **Space Complexity** - O(n) for row arrays

---

### 16. 🟦 Find Index of First Occurrence in String

**🧠 Concept**

Find first occurrence of needle in haystack. Use sliding window to compare substrings.

**💻 Example**

```javascript
function strStr(haystack, needle) {
  if (needle.length === 0) return 0;
  
  for (let i = 0; i <= haystack.length - needle.length; i++) {
    if (haystack.substring(i, i + needle.length) === needle) {
      return i;
    }
  }
  return -1;
}
```

**💬 Explanation + Insight**

- **Sliding Window** - Check each possible starting position
- **Substring Comparison** - Compare needle with haystack substring
- **Early Return** - Return first match found
- **Time Complexity** - O(n*m) where n=haystack, m=needle
- **Space Complexity** - O(1) constant space

---

### 17. 🟦 Text Justification

**🧠 Concept**

Justify text by distributing spaces evenly. Handle last line separately, distribute spaces between words.

**💻 Example**

```javascript
function fullJustify(words, maxWidth) {
  const result = [];
  let currentLine = [];
  let currentLength = 0;
  
  for (const word of words) {
    if (currentLength + word.length + currentLine.length > maxWidth) {
      result.push(justifyLine(currentLine, currentLength, maxWidth));
      currentLine = [word];
      currentLength = word.length;
    } else {
      currentLine.push(word);
      currentLength += word.length;
    }
  }
  
  if (currentLine.length > 0) {
    result.push(currentLine.join(' ') + ' '.repeat(maxWidth - currentLength - currentLine.length + 1));
  }
  
  return result;
}
```

**💬 Explanation + Insight**

- **Line Building** - Add words until line is full
- **Space Distribution** - Distribute spaces evenly between words
- **Last Line** - Handle last line with left justification
- **Time Complexity** - O(n) where n is total characters
- **Space Complexity** - O(n) for result array

---

*This comprehensive array and string basics section covers essential patterns including two pointers, in-place operations, string manipulation, and common algorithms for array processing.*