# 🧩 DSA Interview Notes - LeetCode Top 150

## 🟧 Section 2 — Two Pointers / Sliding Window — Q18-Q26

---

### 18. 🟧 Valid Palindrome

**🧠 Concept**

Check if string is palindrome by comparing characters from both ends, skipping non-alphanumeric characters.

**💻 Example**

```javascript
function isPalindrome(s) {
  let left = 0;
  let right = s.length - 1;
  
  while (left < right) {
    while (left < right && !isAlphanumeric(s[left])) {
      left++;
    }
    while (left < right && !isAlphanumeric(s[right])) {
      right--;
    }
    
    if (s[left].toLowerCase() !== s[right].toLowerCase()) {
      return false;
    }
    left++;
    right--;
  }
  return true;
}

function isAlphanumeric(char) {
  return /[a-zA-Z0-9]/.test(char);
}
```

**💬 Explanation + Insight**

- **Two Pointers** - Start from both ends and move inward
- **Character Validation** - Skip non-alphanumeric characters
- **Case Insensitive** - Convert to lowercase for comparison
- **Time Complexity** - O(n) single pass through string
- **Space Complexity** - O(1) constant space

---

### 19. 🟧 Is Subsequence

**🧠 Concept**

Check if one string is subsequence of another by using two pointers to traverse both strings.

**💻 Example**

```javascript
function isSubsequence(s, t) {
  let sIndex = 0;
  let tIndex = 0;
  
  while (sIndex < s.length && tIndex < t.length) {
    if (s[sIndex] === t[tIndex]) {
      sIndex++;
    }
    tIndex++;
  }
  
  return sIndex === s.length;
}
```

**💬 Explanation + Insight**

- **Two Pointers** - One for each string
- **Character Matching** - Move s pointer only when characters match
- **Sequential Check** - Maintain order of characters
- **Time Complexity** - O(n) where n is length of t
- **Space Complexity** - O(1) constant space

---

### 20. 🟧 Two Sum II - Input Array Sorted

**🧠 Concept**

Find two numbers that add up to target in sorted array using two pointers from both ends.

**💻 Example**

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
```

**💬 Explanation + Insight**

- **Sorted Array** - Use two pointers from ends
- **Sum Comparison** - Move pointers based on sum vs target
- **1-indexed Result** - Return indices starting from 1
- **Time Complexity** - O(n) single pass
- **Space Complexity** - O(1) constant space

---

### 21. 🟧 Container With Most Water

**🧠 Concept**

Find maximum area between two lines using two pointers, moving pointer with smaller height.

**💻 Example**

```javascript
function maxArea(height) {
  let left = 0;
  let right = height.length - 1;
  let maxWater = 0;
  
  while (left < right) {
    const width = right - left;
    const minHeight = Math.min(height[left], height[right]);
    const area = width * minHeight;
    maxWater = Math.max(maxWater, area);
    
    if (height[left] < height[right]) {
      left++;
    } else {
      right--;
    }
  }
  
  return maxWater;
}
```

**💬 Explanation + Insight**

- **Two Pointers** - Start from both ends
- **Area Calculation** - Width × minimum height
- **Greedy Approach** - Move pointer with smaller height
- **Time Complexity** - O(n) single pass
- **Space Complexity** - O(1) constant space

---

### 22. 🟧 3Sum

**🧠 Concept**

Find all unique triplets that sum to zero using one pointer and two pointers for remaining elements.

**💻 Example**

```javascript
function threeSum(nums) {
  nums.sort((a, b) => a - b);
  const result = [];
  
  for (let i = 0; i < nums.length - 2; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) continue;
    
    let left = i + 1;
    let right = nums.length - 1;
    
    while (left < right) {
      const sum = nums[i] + nums[left] + nums[right];
      if (sum === 0) {
        result.push([nums[i], nums[left], nums[right]]);
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
```

**💬 Explanation + Insight**

- **Sort First** - Sort array for two pointer technique
- **Skip Duplicates** - Avoid duplicate triplets
- **Three Pointers** - One fixed, two moving
- **Time Complexity** - O(n²) due to sorting
- **Space Complexity** - O(1) excluding result array

---

### 23. 🟧 Minimum Size Subarray Sum

**🧠 Concept**

Find minimum length subarray with sum >= target using sliding window technique.

**💻 Example**

```javascript
function minSubArrayLen(target, nums) {
  let left = 0;
  let sum = 0;
  let minLength = Infinity;
  
  for (let right = 0; right < nums.length; right++) {
    sum += nums[right];
    
    while (sum >= target) {
      minLength = Math.min(minLength, right - left + 1);
      sum -= nums[left];
      left++;
    }
  }
  
  return minLength === Infinity ? 0 : minLength;
}
```

**💬 Explanation + Insight**

- **Sliding Window** - Expand right, contract left
- **Sum Tracking** - Maintain running sum
- **Minimum Length** - Track smallest valid window
- **Time Complexity** - O(n) each element visited twice
- **Space Complexity** - O(1) constant space

---

### 24. 🟧 Longest Substring Without Repeating Characters

**🧠 Concept**

Find longest substring without repeating characters using sliding window with character frequency tracking.

**💻 Example**

```javascript
function lengthOfLongestSubstring(s) {
  const charSet = new Set();
  let left = 0;
  let maxLength = 0;
  
  for (let right = 0; right < s.length; right++) {
    while (charSet.has(s[right])) {
      charSet.delete(s[left]);
      left++;
    }
    charSet.add(s[right]);
    maxLength = Math.max(maxLength, right - left + 1);
  }
  
  return maxLength;
}
```

**💬 Explanation + Insight**

- **Sliding Window** - Expand right, contract left when duplicate
- **Set Tracking** - Use Set to track characters in window
- **Duplicate Handling** - Remove characters until no duplicates
- **Time Complexity** - O(n) each character visited twice
- **Space Complexity** - O(min(m,n)) where m is charset size

---

### 25. 🟧 Substring with Concatenation of All Words

**🧠 Concept**

Find all starting indices of substrings that are concatenation of all words using sliding window with word frequency.

**💻 Example**

```javascript
function findSubstring(s, words) {
  const wordLength = words[0].length;
  const totalLength = words.length * wordLength;
  const result = [];
  
  for (let i = 0; i < wordLength; i++) {
    const wordCount = {};
    let left = i;
    let count = 0;
    
    for (let right = i; right <= s.length - wordLength; right += wordLength) {
      const word = s.substring(right, right + wordLength);
      
      if (wordCount[word]) {
        wordCount[word]++;
      } else {
        wordCount[word] = 1;
      }
      
      if (wordCount[word] <= (words.filter(w => w === word).length)) {
        count++;
      } else {
        while (wordCount[word] > (words.filter(w => w === word).length)) {
          const leftWord = s.substring(left, left + wordLength);
          wordCount[leftWord]--;
          if (wordCount[leftWord] < (words.filter(w => w === leftWord).length)) {
            count--;
          }
          left += wordLength;
        }
      }
      
      if (count === words.length) {
        result.push(left);
        const leftWord = s.substring(left, left + wordLength);
        wordCount[leftWord]--;
        count--;
        left += wordLength;
      }
    }
  }
  
  return result;
}
```

**💬 Explanation + Insight**

- **Sliding Window** - Fixed size window for concatenation
- **Word Frequency** - Track frequency of each word
- **Multiple Starts** - Check all possible starting positions
- **Time Complexity** - O(n * m) where n is string length, m is word length
- **Space Complexity** - O(m) for word frequency map

---

### 26. 🟧 Minimum Window Substring

**🧠 Concept**

Find minimum window in string that contains all characters of another string using sliding window.

**💻 Example**

```javascript
function minWindow(s, t) {
  const need = {};
  const window = {};
  
  for (const char of t) {
    need[char] = (need[char] || 0) + 1;
  }
  
  let left = 0;
  let right = 0;
  let valid = 0;
  let start = 0;
  let len = Infinity;
  
  while (right < s.length) {
    const c = s[right];
    right++;
    
    if (need[c]) {
      window[c] = (window[c] || 0) + 1;
      if (window[c] === need[c]) {
        valid++;
      }
    }
    
    while (valid === Object.keys(need).length) {
      if (right - left < len) {
        start = left;
        len = right - left;
      }
      
      const d = s[left];
      left++;
      
      if (need[d]) {
        if (window[d] === need[d]) {
          valid--;
        }
        window[d]--;
      }
    }
  }
  
  return len === Infinity ? '' : s.substring(start, start + len);
}
```

**💬 Explanation + Insight**

- **Sliding Window** - Expand right, contract left
- **Character Frequency** - Track frequency of target characters
- **Valid Window** - Window contains all required characters
- **Time Complexity** - O(n) where n is string length
- **Space Complexity** - O(k) where k is number of unique characters

---

*This comprehensive two pointers and sliding window section covers essential patterns including palindrome checking, subsequence validation, sum problems, container problems, and advanced sliding window techniques for efficient array and string processing.*