# 🧩 DSA Interview Notes - LeetCode Top 150

## 🟨 Section 3 — Hash Table / Set — Q27-Q35

---

### 27. 🟨 Two Sum

**🧠 Concept**

Find two numbers that add up to target using hash map to store complements for O(1) lookup.

**💻 Example**

```javascript
function twoSum(nums, target) {
  const map = new Map();
  
  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];
    if (map.has(complement)) {
      return [map.get(complement), i];
    }
    map.set(nums[i], i);
  }
  return [];
}
```

**💬 Explanation + Insight**

- **Hash Map** - Store number and its index
- **Complement Lookup** - Check if complement exists
- **One Pass** - Single iteration through array
- **Time Complexity** - O(n) linear time
- **Space Complexity** - O(n) for hash map

---

### 28. 🟨 Group Anagrams

**🧠 Concept**

Group strings that are anagrams by using sorted string as key in hash map.

**💻 Example**

```javascript
function groupAnagrams(strs) {
  const map = new Map();
  
  for (const str of strs) {
    const sorted = str.split('').sort().join('');
    if (!map.has(sorted)) {
      map.set(sorted, []);
    }
    map.get(sorted).push(str);
  }
  
  return Array.from(map.values());
}
```

**💬 Explanation + Insight**

- **Sorted Key** - Use sorted string as grouping key
- **Hash Map** - Group strings by their sorted form
- **Anagram Detection** - Sorted strings are equal for anagrams
- **Time Complexity** - O(n * m log m) where m is string length
- **Space Complexity** - O(n * m) for storing all strings

---

### 29. 🟨 Longest Consecutive Sequence

**🧠 Concept**

Find longest consecutive sequence using hash set to check for sequence starts and track sequence length.

**💻 Example**

```javascript
function longestConsecutive(nums) {
  const numSet = new Set(nums);
  let longest = 0;
  
  for (const num of numSet) {
    if (!numSet.has(num - 1)) {
      let currentNum = num;
      let currentLength = 1;
      
      while (numSet.has(currentNum + 1)) {
        currentNum++;
        currentLength++;
      }
      
      longest = Math.max(longest, currentLength);
    }
  }
  
  return longest;
}
```

**💬 Explanation + Insight**

- **Hash Set** - O(1) lookup for sequence checking
- **Sequence Start** - Only start counting from sequence beginnings
- **Consecutive Check** - Check if num-1 exists to find sequence start
- **Time Complexity** - O(n) each number visited once
- **Space Complexity** - O(n) for hash set

---

### 30. 🟨 Isomorphic Strings

**🧠 Concept**

Check if two strings are isomorphic by mapping characters and ensuring bidirectional mapping.

**💻 Example**

```javascript
function isIsomorphic(s, t) {
  if (s.length !== t.length) return false;
  
  const sToT = new Map();
  const tToS = new Map();
  
  for (let i = 0; i < s.length; i++) {
    const sChar = s[i];
    const tChar = t[i];
    
    if (sToT.has(sChar) && sToT.get(sChar) !== tChar) {
      return false;
    }
    if (tToS.has(tChar) && tToS.get(tChar) !== sChar) {
      return false;
    }
    
    sToT.set(sChar, tChar);
    tToS.set(tChar, sChar);
  }
  
  return true;
}
```

**💬 Explanation + Insight**

- **Bidirectional Mapping** - Map st and ts
- **Consistency Check** - Ensure mappings are consistent
- **Character Mapping** - Each character maps to exactly one other
- **Time Complexity** - O(n) single pass through strings
- **Space Complexity** - O(1) constant space (max 256 characters)

---

### 31. 🟨 Word Pattern

**🧠 Concept**

Check if string follows pattern by mapping pattern characters to words and ensuring bidirectional mapping.

**💻 Example**

```javascript
function wordPattern(pattern, s) {
  const words = s.split(' ');
  if (pattern.length !== words.length) return false;
  
  const patternToWord = new Map();
  const wordToPattern = new Map();
  
  for (let i = 0; i < pattern.length; i++) {
    const char = pattern[i];
    const word = words[i];
    
    if (patternToWord.has(char) && patternToWord.get(char) !== word) {
      return false;
    }
    if (wordToPattern.has(word) && wordToPattern.get(word) !== char) {
      return false;
    }
    
    patternToWord.set(char, word);
    wordToPattern.set(word, char);
  }
  
  return true;
}
```

**💬 Explanation + Insight**

- **Pattern Matching** - Map pattern characters to words
- **Bidirectional Mapping** - Ensure consistent mapping both ways
- **Length Check** - Pattern and words must have same length
- **Time Complexity** - O(n) where n is pattern length
- **Space Complexity** - O(n) for hash maps

---

### 32. 🟨 Valid Anagram

**🧠 Concept**

Check if two strings are anagrams by comparing character frequencies using hash map.

**💻 Example**

```javascript
function isAnagram(s, t) {
  if (s.length !== t.length) return false;
  
  const charCount = new Map();
  
  for (const char of s) {
    charCount.set(char, (charCount.get(char) || 0) + 1);
  }
  
  for (const char of t) {
    if (!charCount.has(char)) return false;
    charCount.set(char, charCount.get(char) - 1);
    if (charCount.get(char) === 0) {
      charCount.delete(char);
    }
  }
  
  return charCount.size === 0;
}
```

**💬 Explanation + Insight**

- **Character Frequency** - Count frequency of each character
- **Frequency Comparison** - Decrease count for second string
- **Length Check** - Different lengths cannot be anagrams
- **Time Complexity** - O(n) where n is string length
- **Space Complexity** - O(1) constant space (max 26 characters)

---

### 33. 🟨 Ransom Note

**🧠 Concept**

Check if ransom note can be constructed from magazine by comparing character frequencies.

**💻 Example**

```javascript
function canConstruct(ransomNote, magazine) {
  const charCount = new Map();
  
  for (const char of magazine) {
    charCount.set(char, (charCount.get(char) || 0) + 1);
  }
  
  for (const char of ransomNote) {
    if (!charCount.has(char) || charCount.get(char) === 0) {
      return false;
    }
    charCount.set(char, charCount.get(char) - 1);
  }
  
  return true;
}
```

**💬 Explanation + Insight**

- **Character Availability** - Check if magazine has enough characters
- **Frequency Tracking** - Decrease count as characters are used
- **Sufficient Characters** - Magazine must have all required characters
- **Time Complexity** - O(m + n) where m is magazine length, n is note length
- **Space Complexity** - O(1) constant space (max 26 characters)

---

### 34. 🟨 Contains Duplicate II

**🧠 Concept**

Check if array contains duplicate within k distance using hash map to track last occurrence index.

**💻 Example**

```javascript
function containsNearbyDuplicate(nums, k) {
  const map = new Map();
  
  for (let i = 0; i < nums.length; i++) {
    if (map.has(nums[i]) && i - map.get(nums[i]) <= k) {
      return true;
    }
    map.set(nums[i], i);
  }
  
  return false;
}
```

**💬 Explanation + Insight**

- **Index Tracking** - Store last occurrence index of each number
- **Distance Check** - Check if current index - last index <= k
- **Sliding Window** - Maintain window of size k+1
- **Time Complexity** - O(n) single pass through array
- **Space Complexity** - O(n) for hash map

---

### 35. 🟨 Happy Number

**🧠 Concept**

Check if number is happy by repeatedly replacing with sum of squares of digits until cycle or 1.

**💻 Example**

```javascript
function isHappy(n) {
  const seen = new Set();
  
  while (n !== 1 && !seen.has(n)) {
    seen.add(n);
    n = getSumOfSquares(n);
  }
  
  return n === 1;
}

function getSumOfSquares(n) {
  let sum = 0;
  while (n > 0) {
    const digit = n % 10;
    sum += digit * digit;
    n = Math.floor(n / 10);
  }
  return sum;
}
```

**💬 Explanation + Insight**

- **Cycle Detection** - Use Set to detect cycles
- **Sum of Squares** - Calculate sum of squares of digits
- **Termination** - Stop when 1 is reached or cycle detected
- **Time Complexity** - O(log n) for sum calculation
- **Space Complexity** - O(log n) for storing seen numbers

---

*This comprehensive hash table and set section covers essential patterns including two sum, anagram detection, character frequency tracking, and cycle detection for efficient data processing.*