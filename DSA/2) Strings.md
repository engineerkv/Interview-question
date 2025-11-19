# Strings

## Q34. Valid Anagram

**Problem:** Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Approach:** Count character frequencies using a hash map. Strings are anagrams if they have the same length and character frequencies match exactly.

### Solution 1: Hash Map (Optimal)
```javascript
function isAnagram(s, t) {
  if (s.length !== t.length) return false;
  
  const freq = new Map();
  
  // Count characters in s
  for (const c of s) {
    freq.set(c, (freq.get(c) || 0) + 1);
  }
  
  // Decrement counts for characters in t
  for (const c of t) {
    if (!freq.has(c)) return false;
    const count = freq.get(c) - 1;
    if (count === 0) {
      freq.delete(c);
    } else {
      freq.set(c, count);
    }
  }
  
  return freq.size === 0;
}

// Test Cases:
// Input: s = "anagram", t = "nagaram"
// Output: true
// Explanation: Both strings have same character frequencies: 3×a, 1×n, 1×g, 1×r, 1×m

// Input: s = "rat", t = "car"
// Output: false
// Explanation: "rat" has 't' but "car" has 'c'—different characters

// Input: s = "listen", t = "silent"
// Output: true
// Explanation: Both strings contain identical characters with same frequencies
```

**Time Complexity:** O(n) - Single pass through both strings  
**Space Complexity:** O(k) - Hash map stores unique characters (k is character set size, typically 26 for lowercase)

### Solution 2: Sorting (Alternative)
```javascript
function isAnagramSorting(s, t) {
  if (s.length !== t.length) return false;
  return s.split('').sort().join('') === t.split('').sort().join('');
}
```

**Time Complexity:** O(n log n) - Sorting dominates  
**Space Complexity:** O(n) - Creating sorted strings


## Q35. Longest Substring Without Repeating Characters

**Problem:** Given a string `s`, find the length of the longest substring without repeating characters.

**Approach:** Use sliding window technique with a hash map tracking the last-seen index of each character. When a duplicate is found, move the left pointer to the position after the last occurrence.

### Solution 1: Sliding Window with Hash Map (Optimal)
```javascript
function lengthOfLongestSubstring(s) {
  const lastSeen = new Map(); // Map character -> last index
  let left = 0;
  let maxLength = 0;

  for (let right = 0; right < s.length; right++) {
    const char = s[right];
    
    // If character seen before and within current window, move left pointer
    if (lastSeen.has(char) && lastSeen.get(char) >= left) {
      left = lastSeen.get(char) + 1;
    }
    
    lastSeen.set(char, right);
    maxLength = Math.max(maxLength, right - left + 1);
  }
  
  return maxLength;
}

// Test Cases:
// Input: s = "abcabcbb"
// Output: 3
// Explanation: Longest substring without repeating characters is "abc" (length 3)

// Input: s = "bbbbb"
// Output: 1
// Explanation: All characters are 'b', longest valid substring is single "b"

// Input: s = "pwwkew"
// Output: 3
// Explanation: Longest substring is "wke" or "kew" (length 3)

// Input: s = ""
// Output: 0
// Explanation: Empty string has length 0
```

**Time Complexity:** O(n) - Single pass with sliding window, each character visited at most twice  
**Space Complexity:** O(min(n, m)) - Hash map stores unique characters (m is character set size)


## Q36. Valid Palindrome

**Problem:** A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers. Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

**Approach:** Use two pointers from both ends. Skip non-alphanumeric characters and compare characters case-insensitively.

### Solution 1: Two Pointers (Optimal)
```javascript
function isPalindrome(s) {
  let left = 0;
  let right = s.length - 1;
  
  const isAlphanumeric = (c) => /[0-9a-z]/i.test(c);
  
  while (left < right) {
    // Skip non-alphanumeric characters
    while (left < right && !isAlphanumeric(s[left])) left++;
    while (left < right && !isAlphanumeric(s[right])) right--;
    
    // Compare characters (case-insensitive)
    if (s[left].toLowerCase() !== s[right].toLowerCase()) {
      return false;
    }
    
    left++;
    right--;
  }
  
  return true;
}

// Test Cases:
// Input: s = "A man, a plan, a canal: Panama"
// Output: true
// Explanation: After normalization: "amanaplanacanalpanama" - reads same forwards and backwards

// Input: s = "race a car"
// Output: false
// Explanation: After normalization: "raceacar" - r≠e, not a palindrome

// Input: s = " "
// Output: true
// Explanation: Empty string (after removing non-alphanumeric) is a valid palindrome
```

**Time Complexity:** O(n) - Two pointers traverse string once  
**Space Complexity:** O(1) - Only using constant extra variables


## Q37. Longest Palindromic Substring

**Problem:** Given a string `s`, return the longest palindromic substring in `s`.

**Approach:** Expand around each possible center. For each position, check both odd-length palindromes (center at i) and even-length palindromes (center between i and i+1). Track the longest found.

### Solution 1: Expand Around Centers (Optimal for Interviews)
```javascript
function longestPalindrome(s) {
  if (s.length < 2) return s;
  
  let start = 0;
  let end = 0;
  
  const expandAroundCenter = (left, right) => {
    while (left >= 0 && right < s.length && s[left] === s[right]) {
      left--;
      right++;
    }
    return [left + 1, right - 1];
  };
  
  for (let i = 0; i < s.length; i++) {
    // Check odd-length palindromes (center at i)
    const [l1, r1] = expandAroundCenter(i, i);
    // Check even-length palindromes (center between i and i+1)
    const [l2, r2] = expandAroundCenter(i, i + 1);
    
    // Update longest palindrome
    if (r1 - l1 > end - start) {
      start = l1;
      end = r1;
    }
    if (r2 - l2 > end - start) {
      start = l2;
      end = r2;
    }
  }
  
  return s.slice(start, end + 1);
}

// Test Cases:
// Input: s = "babad"
// Output: "bab" or "aba"
// Explanation: Both "bab" and "aba" are palindromes of length 3

// Input: s = "cbbd"
// Output: "bb"
// Explanation: Longest palindrome is "bb" (length 2)

// Input: s = "a"
// Output: "a"
// Explanation: Single character is a palindrome
```

**Time Complexity:** O(n²) - Expanding from each of 2n-1 centers, each expansion takes O(n)  
**Space Complexity:** O(1) - Only using constant extra variables

### Solution 2: Manacher's Algorithm (Alternative - O(n) time)

**Note:** Manacher's algorithm achieves O(n) time but is more complex. The expand-around approach is preferred for interviews.


## Q38. Group Anagrams

**Problem:** Given an array of strings `strs`, group the anagrams together. You can return the answer in any order. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Approach:** Generate a unique key for each string based on character frequency counts. Use a hash map to group strings with the same key.

### Solution 1: Frequency Count Key (Optimal)
```javascript
function groupAnagrams(strs) {
  const map = new Map();
  
  for (const str of strs) {
    // Count character frequencies
    const count = new Array(26).fill(0);
    for (const char of str) {
      count[char.charCodeAt(0) - 97]++;
    }
    
    // Create unique key with delimiter to avoid collisions
    const key = count.join('#');
    
    if (!map.has(key)) {
      map.set(key, []);
    }
    map.get(key).push(str);
  }
  
  return Array.from(map.values());
}

// Test Cases:
// Input: strs = ["eat","tea","tan","ate","nat","bat"]
// Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
// Explanation: Anagrams grouped together: "eat", "tea", "ate" have same frequency pattern

// Input: strs = [""]
// Output: [[""]]
// Explanation: Empty string forms its own group

// Input: strs = ["a"]
// Output: [["a"]]
// Explanation: Single string forms its own group
```

**Time Complexity:** O(nk) - n strings, each processed in O(k) time where k is average string length  
**Space Complexity:** O(nk) - Hash map stores all strings

### Solution 2: Sorted String Key (Alternative)
```javascript
function groupAnagramsSorted(strs) {
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

**Time Complexity:** O(nk log k) - Sorting each string takes O(k log k)  
**Space Complexity:** O(nk) - Hash map storage


## Q39. Reverse Words in a String

**Problem:** Given an input string `s`, reverse the order of the words. A word is defined as a sequence of non-space characters. The words in `s` will be separated by at least one space. Return a string of the words in reverse order concatenated by a single space. Note that `s` may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

**Approach:** Split string on whitespace, reverse the array, and join with single space.

### Solution 1: Split/Reverse/Join (Optimal)
```javascript
function reverseWords(s) {
  return s.trim().split(/\s+/).reverse().join(' ');
}

// Test Cases:
// Input: s = "the sky is blue"
// Output: "blue is sky the"
// Explanation: Split: ["the", "sky", "is", "blue"]. Reverse: ["blue", "is", "sky", "the"]. Join: "blue is sky the"

// Input: s = "  hello world  "
// Output: "world hello"
// Explanation: Trim and split handles multiple spaces, reverse and join

// Input: s = "a good   example"
// Output: "example good a"
// Explanation: Multiple spaces handled by regex split
```

**Time Complexity:** O(n) - String operations (split, reverse, join)  
**Space Complexity:** O(n) - Additional space for split array


## Q40. Longest Repeating Character Replacement

**Problem:** You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English letter. You can perform this operation at most `k` times. Return the length of the longest substring containing the same letter you can get after performing the above operations.

**Approach:** Use sliding window technique. Track maximum frequency character in current window. Window is valid when `(length - maxFreq) <= k`. Shrink window when invalid.

### Solution 1: Sliding Window with Max Frequency (Optimal)
```javascript
function characterReplacement(s, k) {
  const freq = new Array(26).fill(0);
  let left = 0;
  let maxLength = 0;
  let maxFreq = 0;
  
  for (let right = 0; right < s.length; right++) {
    const charIdx = s.charCodeAt(right) - 65; // 'A' = 65
    freq[charIdx]++;
    maxFreq = Math.max(maxFreq, freq[charIdx]);
    
    // Shrink window if invalid: (length - maxFreq) > k
    while (right - left + 1 - maxFreq > k) {
      freq[s.charCodeAt(left) - 65]--;
      left++;
    }
    
    maxLength = Math.max(maxLength, right - left + 1);
  }
  
  return maxLength;
}

// Test Cases:
// Input: s = "ABAB", k = 2
// Output: 4
// Explanation: Replace 2 'A's with 'B' → "BBBB" (all same character), length 4

// Input: s = "AABABBA", k = 1
// Output: 4
// Explanation: Best window "AABA": replace 1 'B' with 'A' → "AAAA", length 4

// Input: s = "ABCDE", k = 1
// Output: 2
// Explanation: With k=1, can replace 1 character. Best window length is 2
```

**Time Complexity:** O(n) - Single pass with sliding window  
**Space Complexity:** O(1) - Fixed array of size 26 for uppercase letters

## Q41. Minimum Window Substring

**Problem:** Given two strings `s` and `t` of lengths `m` and `n` respectively, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.

**Approach:** Use sliding window technique. Expand window to cover all characters in `t`, then contract to minimize while maintaining coverage.

### Solution 1: Sliding Window (Optimal)
```javascript
function minWindow(s, t) {
  if (s.length < t.length) return '';
  
  const need = new Map(); // Required characters from t
  const window = new Map(); // Current window characters
  
  // Count required characters
  for (const char of t) {
    need.set(char, (need.get(char) || 0) + 1);
  }
  
  let left = 0;
  let have = 0; // Number of unique characters satisfied
  const needSize = need.size; // Number of unique characters needed
  let minLength = Infinity;
  let minStart = -1;
  
  for (let right = 0; right < s.length; right++) {
    const char = s[right];
    window.set(char, (window.get(char) || 0) + 1);
    
    // Check if current character count matches requirement
    if (need.has(char) && window.get(char) === need.get(char)) {
      have++;
    }
    
    // Try to shrink window when all characters are satisfied
    while (have === needSize) {
      // Update minimum window
      if (right - left + 1 < minLength) {
        minLength = right - left + 1;
        minStart = left;
      }
      
      // Shrink window from left
      const leftChar = s[left];
      window.set(leftChar, window.get(leftChar) - 1);
      
      if (need.has(leftChar) && window.get(leftChar) < need.get(leftChar)) {
        have--;
      }
      
      left++;
    }
  }
  
  return minLength === Infinity ? '' : s.slice(minStart, minStart + minLength);
}

// Test Cases:
// Input: s = "ADOBECODEBANC", t = "ABC"
// Output: "BANC"
// Explanation: Minimum window containing all A, B, C is "BANC" (length 4)

// Input: s = "a", t = "a"
// Output: "a"
// Explanation: Entire string "a" contains required character

// Input: s = "a", t = "aa"
// Output: ""
// Explanation: Need two 'a' but string has only one—no valid window
```

**Time Complexity:** O(n + m) - Each character in s visited at most twice, where n=s.length, m=t.length  
**Space Complexity:** O(m) - Hash maps store characters from t and window


## Q42. Isomorphic Strings

**Problem:** Given two strings `s` and `t`, determine if they are isomorphic. Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`. All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

**Approach:** Use two hash maps to maintain bidirectional character mapping. Each character in `s` must map to exactly one character in `t`, and vice versa.

### Solution 1: Bidirectional Mapping (Optimal)
```javascript
function isIsomorphic(s, t) {
  if (s.length !== t.length) return false;
  
  const sToT = new Map(); // Map s[i] -> t[i]
  const tToS = new Map(); // Map t[i] -> s[i]
  
  for (let i = 0; i < s.length; i++) {
    const charS = s[i];
    const charT = t[i];
    
    // Check if mapping conflicts
    if (sToT.has(charS) && sToT.get(charS) !== charT) return false;
    if (tToS.has(charT) && tToS.get(charT) !== charS) return false;
    
    // Establish bidirectional mapping
    sToT.set(charS, charT);
    tToS.set(charT, charS);
  }
  
  return true;
}

// Test Cases:
// Input: s = "egg", t = "add"
// Output: true
// Explanation: e→a, g→d. Mapping is consistent and bidirectional

// Input: s = "foo", t = "bar"
// Output: false
// Explanation: f→b, o→a, but second o→r conflicts with first o→a

// Input: s = "paper", t = "title"
// Output: true
// Explanation: p→t, a→i, e→l, r→e. All mappings are consistent
```

**Time Complexity:** O(n) - Single pass through strings  
**Space Complexity:** O(k) - Hash maps store unique characters from both strings (k is character set size)


## Q43. Count and Say

**Problem:** The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
- `countAndSay(1) = "1"`
- `countAndSay(n)` is the way you would "say" the digit string from `countAndSay(n - 1)`, which is then converted into a different digit string.

To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

Given a positive integer `n`, return the `n`th term of the count-and-say sequence.

**Approach:** Start with "1". For each iteration, use run-length encoding to describe the previous term: count consecutive same digits, then append count and digit.

### Solution 1: Run-Length Encoding (Optimal)
```javascript
function countAndSay(n) {
  let current = '1';
  
  for (let i = 2; i <= n; i++) {
    let next = '';
    let j = 0;
    
    while (j < current.length) {
      let count = 1;
      const digit = current[j];
      
      // Count consecutive same digits
      while (j + count < current.length && current[j + count] === digit) {
        count++;
      }
      
      // Append count and digit
      next += count + digit;
      j += count;
    }
    
    current = next;
  }
  
  return current;
}

// Test Cases:
// Input: n = 1
// Output: "1"
// Explanation: Base case, first term is "1"

// Input: n = 4
// Output: "1211"
// Explanation: 
// Term 1: "1" (one 1)
// Term 2: "11" (one 1 from term 1)
// Term 3: "21" (two 1s from term 2)
// Term 4: "1211" (one 2, one 1 from term 3)

// Input: n = 5
// Output: "111221"
// Explanation: Term 5 describes term 4: one 1, one 1, one 2, two 1s
```

**Time Complexity:** O(2^n) - Exponential growth of string length  
**Space Complexity:** O(2^n) - Space for storing current term


## Q44. Implement strStr() (KMP Algorithm)

**Problem:** Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

**Approach:** Use KMP (Knuth-Morris-Pratt) algorithm with LPS (Longest Proper Prefix which is also Suffix) array to avoid backtracking in the haystack.

### Solution 1: KMP Algorithm (Optimal)
```javascript
function strStr(haystack, needle) {
  if (needle === '') return 0;
  if (needle.length > haystack.length) return -1;
  
  // Build LPS array for pattern
  const lps = buildLPS(needle);
  
  let i = 0; // Pointer for haystack
  let j = 0; // Pointer for needle
  
  while (i < haystack.length) {
    if (haystack[i] === needle[j]) {
      i++;
      j++;
      if (j === needle.length) {
        return i - j; // Found match
      }
    } else if (j > 0) {
      j = lps[j - 1]; // Skip using LPS
    } else {
      i++; // No match, move forward
    }
  }
  
  return -1;
}

function buildLPS(pattern) {
  const lps = new Array(pattern.length).fill(0);
  let len = 0; // Length of previous longest prefix suffix
  let i = 1;
  
  while (i < pattern.length) {
    if (pattern[i] === pattern[len]) {
      len++;
      lps[i] = len;
      i++;
    } else if (len > 0) {
      len = lps[len - 1];
    } else {
      lps[i] = 0;
      i++;
    }
  }
  
  return lps;
}

// Test Cases:
// Input: haystack = "sadbutsad", needle = "sad"
// Output: 0
// Explanation: "sad" found at index 0

// Input: haystack = "leetcode", needle = "leeto"
// Output: -1
// Explanation: "leeto" not found in haystack

// Input: haystack = "mississippi", needle = "issip"
// Output: 4
// Explanation: "issip" found at index 4
```

**Time Complexity:** O(n + m) - Building LPS array (m) + searching (n), where n=haystack.length, m=needle.length  
**Space Complexity:** O(m) - LPS array storage

### Solution 2: Brute Force (Simpler)
```javascript
function strStrBruteForce(haystack, needle) {
  if (needle === '') return 0;
  
  for (let i = 0; i <= haystack.length - needle.length; i++) {
    let j = 0;
    while (j < needle.length && haystack[i + j] === needle[j]) {
      j++;
    }
    if (j === needle.length) return i;
  }
  
  return -1;
}
```

**Time Complexity:** O(m×n) - Worst case  
**Space Complexity:** O(1)


## Q45. Roman to Integer / Integer to Roman

**Problem:** 
- **Roman to Integer:** Given a roman numeral, convert it to an integer.
- **Integer to Roman:** Given an integer, convert it to a roman numeral.

**Approach:** 
- **Roman to Integer:** Scan left-to-right, subtract if current value < next value (subtractive notation).
- **Integer to Roman:** Use greedy approach—always use largest possible value-symbol pair first.

### Solution 1: Roman to Integer
```javascript
function romanToInt(s) {
  const values = new Map([
    ['I', 1], ['V', 5], ['X', 10], ['L', 50],
    ['C', 100], ['D', 500], ['M', 1000]
  ]);
  
  let result = 0;
  
  for (let i = 0; i < s.length; i++) {
    const current = values.get(s[i]);
    const next = i + 1 < s.length ? values.get(s[i + 1]) : 0;
    
    // Subtractive notation: if current < next, subtract
    if (current < next) {
      result -= current;
    } else {
      result += current;
    }
  }
  
  return result;
}

// Test Cases:
// Input: s = "III"
// Output: 3
// Explanation: I + I + I = 1 + 1 + 1 = 3

// Input: s = "LVIII"
// Output: 58
// Explanation: L + V + I + I + I = 50 + 5 + 1 + 1 + 1 = 58

// Input: s = "MCMXCIV"
// Output: 1994
// Explanation: M + CM + XC + IV = 1000 + (1000-100) + (100-10) + (5-1) = 1994
```

### Solution 2: Integer to Roman
```javascript
function intToRoman(num) {
  const pairs = [
    [1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'],
    [100, 'C'], [90, 'XC'], [50, 'L'], [40, 'XL'],
    [10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']
  ];
  
  let result = '';
  
  for (const [value, symbol] of pairs) {
    while (num >= value) {
      result += symbol;
      num -= value;
    }
  }
  
  return result;
}

// Test Cases:
// Input: num = 3
// Output: "III"
// Explanation: 3 = 1 + 1 + 1

// Input: num = 58
// Output: "LVIII"
// Explanation: 58 = 50 + 5 + 1 + 1 + 1

// Input: num = 1994
// Output: "MCMXCIV"
// Explanation: 1994 = 1000 + 900 + 90 + 4
```

**Time Complexity:** 
- Roman to Integer: O(n) - Single pass through string
- Integer to Roman: O(1) - Fixed number of symbols (13 pairs)

**Space Complexity:** O(1) - Constant extra space


## Q46. Longest Common Prefix

**Problem:** Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string `""`.

**Approach:** Start with the first string as prefix. For each subsequent string, trim the prefix until it matches the start of that string.

### Solution 1: Trim Prefix (Optimal)
```javascript
function longestCommonPrefix(strs) {
  if (strs.length === 0) return '';
  
  let prefix = strs[0];
  
  for (let i = 1; i < strs.length; i++) {
    // Trim prefix until it matches start of current string
    while (strs[i].indexOf(prefix) !== 0) {
      prefix = prefix.slice(0, -1);
      if (prefix === '') return '';
    }
  }
  
  return prefix;
}

// Test Cases:
// Input: strs = ["flower","flow","flight"]
// Output: "fl"
// Explanation: Common prefix is "fl"

// Input: strs = ["dog","racecar","car"]
// Output: ""
// Explanation: No common prefix exists

// Input: strs = ["ab","a"]
// Output: "a"
// Explanation: Common prefix is "a"
```

**Time Complexity:** O(nk) - n strings, each compared with prefix where k is average string length  
**Space Complexity:** O(1) - Only using constant extra variables (excluding input)

### Solution 2: Character-by-Character (Alternative)
```javascript
function longestCommonPrefixCharByChar(strs) {
  if (strs.length === 0) return '';
  
  for (let i = 0; i < strs[0].length; i++) {
    const char = strs[0][i];
    for (let j = 1; j < strs.length; j++) {
      if (i >= strs[j].length || strs[j][i] !== char) {
        return strs[0].slice(0, i);
      }
    }
  }
  
  return strs[0];
}
```


## Q47. Length of Last Word

**Problem:** Given a string `s` consisting of words and spaces, return the length of the last word in the string. A word is a maximal substring consisting of non-space characters only.

**Approach:** Traverse from the end of the string. Skip trailing spaces, then count characters until a space or the beginning of the string.

### Solution 1: Traverse from End (Optimal)
```javascript
function lengthOfLastWord(s) {
  let length = 0;
  let i = s.length - 1;
  
  // Skip trailing spaces
  while (i >= 0 && s[i] === ' ') {
    i--;
  }
  
  // Count characters of last word
  while (i >= 0 && s[i] !== ' ') {
    length++;
    i--;
  }
  
  return length;
}

// Test Cases:
// Input: s = "Hello World"
// Output: 5
// Explanation: Last word is "World" with length 5

// Input: s = "   fly me   to   the moon  "
// Output: 4
// Explanation: Last word is "moon" with length 4

// Input: s = "luffy is still joyboy"
// Output: 6
// Explanation: Last word is "joyboy" with length 6
```

**Time Complexity:** O(n) - Single pass from end  
**Space Complexity:** O(1) - Constant extra space


## Q48. ZigZag Conversion

**Problem:** The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this:
```
P   A   H   N
A P L S I I G
Y   I   R
```
And then read line by line: `"PAHNAPLSIIGYIR"`

Write the code that will take a string and make this conversion given a number of rows.

**Approach:** Simulate the zigzag movement by tracking current row and direction. Change direction at top and bottom rows.

### Solution 1: Simulate Zigzag (Optimal)
```javascript
function convert(s, numRows) {
  if (numRows === 1) return s;
  
  const rows = Array(numRows).fill('');
  let currentRow = 0;
  let goingDown = false;
  
  for (const char of s) {
    rows[currentRow] += char;
    
    // Change direction at top or bottom
    if (currentRow === 0 || currentRow === numRows - 1) {
      goingDown = !goingDown;
    }
    
    // Move to next row
    currentRow += goingDown ? 1 : -1;
  }
  
  return rows.join('');
}

// Test Cases:
// Input: s = "PAYPALISHIRING", numRows = 3
// Output: "PAHNAPLSIIGYIR"
// Explanation: 
// P   A   H   N
// A P L S I I G
// Y   I   R

// Input: s = "PAYPALISHIRING", numRows = 4
// Output: "PINALSIGYAHRPI"
// Explanation:
// P     I    N
// A   L S  I G
// Y A   H R
// P     I

// Input: s = "A", numRows = 1
// Output: "A"
// Explanation: Single row returns original string
```

**Time Complexity:** O(n) - Single pass through string  
**Space Complexity:** O(n) - Storage for all rows


## Q49. Find the Index of the First Occurrence in a String

**Problem:** Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

**Approach:** Check each starting position in haystack. For each position, check if needle matches starting from that position.

### Solution 1: Brute Force (Simple)
```javascript
function strStr(haystack, needle) {
  if (needle.length === 0) return 0;
  if (needle.length > haystack.length) return -1;
  
  for (let i = 0; i <= haystack.length - needle.length; i++) {
    let j = 0;
    while (j < needle.length && haystack[i + j] === needle[j]) {
      j++;
    }
    if (j === needle.length) return i;
  }
  
  return -1;
}

// Test Cases:
// Input: haystack = "sadbutsad", needle = "sad"
// Output: 0
// Explanation: "sad" occurs at index 0

// Input: haystack = "leetcode", needle = "leeto"
// Output: -1
// Explanation: "leeto" not found

// Input: haystack = "hello", needle = "ll"
// Output: 2
// Explanation: "ll" occurs at index 2
```

**Time Complexity:** O(m×n) - For each position (n) check needle (m)  
**Space Complexity:** O(1) - Constant extra space

**Note:** For optimal O(m+n) solution, see Q44 (KMP Algorithm).


## Q50. Text Justification

**Problem:** Given an array of strings `words` and a width `maxWidth`, format the text such that each line has exactly `maxWidth` characters and is fully (left and right) justified. You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces `' '` when necessary so that each line has exactly `maxWidth` characters. Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right. For the last line of text, it should be left-justified, and no extra space is inserted between words.

**Approach:** Group words into lines. For middle lines, distribute spaces evenly. For last line, left-justify with single spaces.

### Solution 1: Greedy Line Packing (Optimal)
```javascript
function fullJustify(words, maxWidth) {
  const result = [];
  let currentLine = [];
  let currentLength = 0;
  
  for (const word of words) {
    // Check if word fits in current line
    // currentLength (word lengths) + currentLine.length (spaces) + word.length (new word)
    if (currentLength + currentLine.length + word.length > maxWidth) {
      // Format current line
      if (currentLine.length === 1) {
        // Single word: left-justify
        result.push(currentLine[0] + ' '.repeat(maxWidth - currentLength));
      } else {
        // Multiple words: distribute spaces evenly
        const totalSpaces = maxWidth - currentLength;
        const gaps = currentLine.length - 1;
        const spacesPerGap = Math.floor(totalSpaces / gaps);
        const extraSpaces = totalSpaces % gaps;
        
        let line = currentLine[0];
        for (let i = 1; i < currentLine.length; i++) {
          const spaces = spacesPerGap + (i <= extraSpaces ? 1 : 0);
          line += ' '.repeat(spaces) + currentLine[i];
        }
        result.push(line);
      }
      
      // Start new line
      currentLine = [];
      currentLength = 0;
    }
    
    currentLine.push(word);
    currentLength += word.length;
  }
  
  // Last line: left-justified
  const lastLine = currentLine.join(' ');
  result.push(lastLine + ' '.repeat(maxWidth - lastLine.length));
  
  return result;
}

// Test Cases:
// Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
// Output: [
// "This    is    an",
// "example  of text",
// "justification.  "
// ]

// Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
// Output: [
// "What   must   be",
// "acknowledgment  ",
// "shall be        "
// ]
```

**Time Complexity:** O(n×maxWidth) - Process each word and format lines  
**Space Complexity:** O(n×maxWidth) - Result array storage


## Q51. Ransom Note

**Problem:** Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise. Each letter in `magazine` can only be used once in `ransomNote`.

**Approach:** Count character frequencies in magazine. For each character in ransom note, check if it's available and decrement the count.

### Solution 1: Character Frequency Count (Optimal)
```javascript
function canConstruct(ransomNote, magazine) {
  const freq = new Map();
  
  // Count characters in magazine
  for (const char of magazine) {
    freq.set(char, (freq.get(char) || 0) + 1);
  }
  
  // Check ransom note characters
  for (const char of ransomNote) {
    const count = freq.get(char) || 0;
    if (count === 0) return false; // Character not available
    freq.set(char, count - 1); // Use one character
  }
  
  return true;
}

// Test Cases:
// Input: ransomNote = "a", magazine = "b"
// Output: false
// Explanation: Missing character 'a' in magazine

// Input: ransomNote = "aa", magazine = "ab"
// Output: false
// Explanation: Only one 'a' in magazine, need two

// Input: ransomNote = "aa", magazine = "aab"
// Output: true
// Explanation: Two 'a's available in magazine
```

**Time Complexity:** O(m + n) - Pass through both strings, where m=magazine.length, n=ransomNote.length  
**Space Complexity:** O(m) - Frequency map storage (k unique characters, typically k << m)


## Q52. Word Pattern

**Problem:** Given a `pattern` and a string `s`, find if `s` follows the same pattern. Here follow means a full match, such that there is a bijection between a letter in `pattern` and a non-empty word in `s`.

**Approach:** Use bidirectional mapping between pattern characters and words. Each pattern character must map to exactly one word, and vice versa.

### Solution 1: Bidirectional Mapping (Optimal)
```javascript
function wordPattern(pattern, s) {
  const words = s.split(' ');
  if (pattern.length !== words.length) return false;
  
  const patternToWord = new Map();
  const wordToPattern = new Map();
  
  for (let i = 0; i < pattern.length; i++) {
    const char = pattern[i];
    const word = words[i];
    
    // Check if mapping conflicts
    if (patternToWord.has(char) && patternToWord.get(char) !== word) {
      return false;
    }
    if (wordToPattern.has(word) && wordToPattern.get(word) !== char) {
      return false;
    }
    
    // Establish bidirectional mapping
    patternToWord.set(char, word);
    wordToPattern.set(word, char);
  }
  
  return true;
}

// Test Cases:
// Input: pattern = "abba", s = "dog cat cat dog"
// Output: true
// Explanation: a -> dog, b -> cat. Mapping is consistent

// Input: pattern = "abba", s = "dog cat cat fish"
// Output: false
// Explanation: a -> dog, b -> cat, but b should map to fish (conflict)

// Input: pattern = "aaaa", s = "dog cat cat dog"
// Output: false
// Explanation: a should map to same word always (a -> dog, but third word is cat)
```

**Time Complexity:** O(n) - Single pass through pattern and words  
**Space Complexity:** O(n) - Map storage (k unique characters/words, typically k << n)


## Q53. Happy Number

**Problem:** Write an algorithm to determine if a number `n` is happy. A happy number is a number defined by the following process:
- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
- Those numbers for which this process ends in 1 are happy.

Return `true` if `n` is a happy number, and `false` if not.

**Approach:** Use Floyd's cycle detection algorithm. Calculate sum of squares of digits repeatedly. If we reach 1, it's happy. If we enter a cycle, it's not happy.

### Solution 1: Floyd's Cycle Detection (Optimal)
```javascript
function isHappy(n) {
  function getNext(num) {
    let sum = 0;
    while (num > 0) {
      const digit = num % 10;
      sum += digit * digit;
      num = Math.floor(num / 10);
    }
    return sum;
  }
  
  let slow = n;
  let fast = getNext(n);
  
  // Detect cycle
  while (fast !== 1 && slow !== fast) {
    slow = getNext(slow);
    fast = getNext(getNext(fast));
  }
  
  return fast === 1;
}

// Test Cases:
// Input: n = 19
// Output: true
// Explanation: 19 -> 82 -> 68 -> 100 -> 1

// Input: n = 2
// Output: false
// Explanation: Enters cycle: 2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4

// Input: n = 1
// Output: true
// Explanation: Already 1, so happy
```

**Time Complexity:** O(log n) - Digits in number  
**Space Complexity:** O(1) - Constant extra space

### Solution 2: Hash Set (Alternative)
```javascript
function isHappyHashSet(n) {
  const seen = new Set();
  
  function getNext(num) {
    let sum = 0;
    while (num > 0) {
      const digit = num % 10;
      sum += digit * digit;
      num = Math.floor(num / 10);
    }
    return sum;
  }
  
  while (n !== 1 && !seen.has(n)) {
    seen.add(n);
    n = getNext(n);
  }
  
  return n === 1;
}
```

**Time Complexity:** O(log n) - Digits in number  
**Space Complexity:** O(log n) - Hash set storage


## Q54. Contains Duplicate II

**Problem:** Given an integer array `nums` and an integer `k`, return `true` if there are two distinct indices `i` and `j` in the array such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

**Approach:** Use a hash map to track the last index of each value. For each element, check if it was seen before within distance k.

### Solution 1: Hash Map with Last Index (Optimal)
```javascript
function containsNearbyDuplicate(nums, k) {
  const seen = new Map();
  
  for (let i = 0; i < nums.length; i++) {
    if (seen.has(nums[i])) {
      const prevIndex = seen.get(nums[i]);
      if (i - prevIndex <= k) {
        return true;
      }
    }
    // Update last seen index
    seen.set(nums[i], i);
  }
  
  return false;
}

// Test Cases:
// Input: nums = [1,2,3,1], k = 3
// Output: true
// Explanation: nums[0] = nums[3] = 1, distance = 3 <= 3

// Input: nums = [1,0,1,1], k = 1
// Output: true
// Explanation: nums[2] = nums[3] = 1, distance = 1 <= 1

// Input: nums = [1,2,3,1,2,3], k = 2
// Output: false
// Explanation: Duplicates exist but distance > 2
```

**Time Complexity:** O(n) - Single pass through array  
**Space Complexity:** O(min(n,k)) - Map storage (at most k distinct values if using sliding window)


## Q55. Substring with Concatenation of All Words

**Problem:** You are given a string `s` and an array of strings `words`. All the strings of `words` are of the same length. A concatenated substring in `s` is a substring that contains all the strings of any permutation of `words` concatenated. For example, if `words = ["ab","cd","ef"]`, then `"abcdef"`, `"abefcd"`, `"cdabef"`, `"cdefab"`, `"efabcd"`, and `"efcdab"` are all concatenated strings. Return the starting indices of all the concatenated substrings in `s`. You can return the answer in any order.

**Approach:** For each starting position, extract words of fixed length and check if they match the word count from the input array.

### Solution 1: Sliding Window with Word Matching (Optimal)
```javascript
function findSubstring(s, words) {
  if (words.length === 0 || s.length === 0) return [];
  
  const wordLength = words[0].length;
  const totalLength = words.length * wordLength;
  const wordCount = new Map();
  
  // Count words in input
  for (const word of words) {
    wordCount.set(word, (wordCount.get(word) || 0) + 1);
  }
  
  const result = [];
  
  // Check each starting position
  for (let i = 0; i <= s.length - totalLength; i++) {
    const seen = new Map();
    let j = 0;
    
    // Extract words from substring
    while (j < words.length) {
      const start = i + j * wordLength;
      const word = s.substring(start, start + wordLength);
      
      // Check if word exists in input
      if (!wordCount.has(word)) break;
      
      // Count seen words
      seen.set(word, (seen.get(word) || 0) + 1);
      
      // Check if count exceeds expected
      if (seen.get(word) > wordCount.get(word)) break;
      
      j++;
    }
    
    // If all words matched
    if (j === words.length) {
      result.push(i);
    }
  }
  
  return result;
}

// Test Cases:
// Input: s = "barfoothefoobarman", words = ["foo","bar"]
// Output: [0,9]
// Explanation: "barfoo" at index 0, "foobar" at index 9

// Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
// Output: []
// Explanation: No valid concatenation found

// Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
// Output: [6,9,12]
// Explanation: Multiple valid concatenations found
```

**Time Complexity:** O(n×m×k) - n positions, m words, k word length, where n=s.length, m=words.length, k=words[0].length  
**Space Complexity:** O(m) - Word count maps storage

