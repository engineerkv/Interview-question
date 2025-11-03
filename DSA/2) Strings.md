# Strings

## Q16. Valid Anagram

Concept:
Check if two strings are anagrams by counting character frequencies using a hash map—strings are anagrams if character counts match.

Example:
```javascript
function isAnagram(s, t) {
  if (s.length !== t.length) return false;
  const freq = new Map();
  for (const c of s) freq.set(c, (freq.get(c) || 0) + 1);
  for (const c of t) {
    if (!freq.has(c)) return false;
    const next = freq.get(c) - 1;
    if (next === 0) freq.delete(c);
    else freq.set(c, next);
  }
  return freq.size === 0;
}

// Input: s = "anagram", t = "nagaram"
// Output: true
// Explanation: "anagram" has: 3×a, 1×n, 1×g, 1×r, 1×m. "nagaram" has: 3×a, 1×n, 1×g, 1×r, 1×m. Character frequencies match exactly.

// Input: s = "rat", t = "car"
// Output: false
// Explanation: "rat" has: 1×r, 1×a, 1×t. "car" has: 1×c, 1×a, 1×r. 't' and 'c' are different, so not anagrams.

// Input: s = "listen", t = "silent"
// Output: true
// Explanation: Both strings contain identical characters (l, i, s, t, e, n) with same frequencies, making them perfect anagrams.
```

**Time Complexity:** O(n) -Single pass through both strings  
**Space Complexity:** O(k) - Hash map stores unique characters (k is character set size, typically 26 for lowercase)

Deep Insights:
  - Rule: Count character frequencies using hash map; strings are anagrams if character counts match exactly.
  - Real-world: Anagram checking in word games, spell checkers, cryptographic hash verification where order doesn't matter.
  - Common mistake: Not checking length mismatch first; using fixed array for Unicode; forgetting to handle character deletion when count reaches zero.
  - Optimization: Early exit on length mismatch; fixed array of size 26 for lowercase only; Map for Unicode strings.
  - Interview tip: Ask about character set first (ASCII vs Unicode); explain why we delete from map when count reaches zero.

## Q17. Longest Substring Without Repeating Characters

Concept:
Find longest substring without repeating characters using sliding window with hash map tracking last-seen index of each character.

Example:
```javascript
function lengthOfLongestSubstring(s) {
  const last = new Map();
  let left = 0;
  let best = 0;

  for (let right = 0; right < s.length; right++) {
    const ch = s[right];
    if (last.has(ch)) left = Math.max(left, last.get(ch) + 1);
    last.set(ch, right);
    best = Math.max(best, right - left + 1);
  }
  return best;
}

// Input: s = "abcabcbb"
// Output: 3
// Explanation: Window expands: "abc" (length 3) → "bca" (length 3) → "cab" (length 3) → "abc" (length 3) → "cb" (length 2) → "b" (length 1). Maximum length is 3.

// Input: s = "bbbbb"
// Output: 1
// Explanation: All characters are 'b', so any substring longer than 1 character contains repeats. Longest valid substring is single "b".

// Input: s = "pwwkew"
// Output: 3
// Explanation: Window: "p" → "pw" → "w" (repeat detected, move left) → "wk" → "wke" (length 3) → "kew" (length 3). Maximum is 3.
```

**Time Complexity:** O(n) -Single pass with sliding window, each character visited at most twice  
**Space Complexity:** O(min(n, m)) - Hash map stores unique characters (m is character set size)

Deep Insights:
  - Rule: Sliding window with hash map tracking last seen index; move left to last occurrence + 1 on duplicate; O(n) time.
  - Real-world: Longest unique substring problems, window size optimization, character-based analytics, string processing.
  - Common mistake: Forgetting Math.max when updating left pointer; left should never move backwards; empty string returns 0.
  - Optimization: Works with any charset using Map; supports Unicode without pre-allocating arrays; each character visited at most twice.
  - Interview tip: Explain why Math.max is needed; ask about character set first; mention Manacher's for palindrome variants.

## Q18. Palindrome Check

Concept:
Check if string is palindrome using two pointers from both ends, ignoring non- alphanumeric characters and case differences.

Example:
```javascript
function isPalindrome(s) {
  let l = 0;
  let r = s.length - 1;
  const isA = (c) => /[0-9a-z]/i.test(c);

  while (l < r) {
    while (l < r && !isA(s[l])) l++;
    while (l < r && !isA(s[r])) r--;
    if (s[l].toLowerCase() !== s[r].toLowerCase()) return false;
    l++;
    r--;
  }
  return true;
}

// Input: s = "A man, a plan, a canal: Panama"
// Output: true
// Explanation: After removing non-alphanumeric and converting to lowercase: "amanaplanacanalpanama". Reads same forwards and backwards: a- m-a- n-a- p-l- a-n- a-c- a-n- a-l- p-a- n-a- m-a.

// Input: s = "race a car"
// Output: false
// Explanation: After normalization: "raceacar". Left to right: r- a-c- e-a- c-a- r, but comparing ends: r≠e, so not a palindrome.

// Input: s = " "
// Output: true
// Explanation: After removing non-alphanumeric characters, we get an empty string. An empty string is considered a valid palindrome (reads same forwards and backwards).
```

**Time Complexity:** O(n) - Two pointers traverse string once  
**Space Complexity:** O(1) -Only using constant extra variables

Deep Insights:
  - Rule: Two pointers from ends, skip non-alphanumeric; ignore case for comparison; O(n) time, O(1) space.
  - Real-world: Phrase palindrome validation, text normalization, string cleaning algorithms, palindrome detection systems.
  - Common mistake: Not handling empty strings and single characters (both valid palindromes); forgetting to skip non-alphanumeric.
  - Optimization: Two pointers converge; O(n/2) average comparisons; use proper Unicode category checks for international characters.
  - Interview tip: Ask about case sensitivity and special characters first; clarify empty string handling; mention regex alternatives.

## Q19. Longest Palindromic Substring

Concept:
Find longest palindromic substring by expanding around each center (odd and even length palindromes), tracking longest found.

Example:
```javascript
function longestPalindrome(s) {
  if (s.length < 2) return s;
  let start = 0;
  let end = 0;

  const expand = (l, r) => {
    while (l >= 0 && r < s.length && s[l] === s[r]) {
      l--;
      r++;
    }
    return [l + 1, r - 1];
  };

  for (let i = 0; i < s.length; i++) {
    const [l1, r1] = expand(i, i);
    const [l2, r2] = expand(i, i + 1);
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

// Input: s = "babad"
// Output: "bab" or "aba"
// Explanation: Expanding from center 'b' at index 1: "bab" (length 3). Expanding from 'a' at index 2: "aba" (length 3). Both have length 3, either is valid.

// Input: s = "cbbd"
// Output: "bb"
// Explanation: Expanding from center between 'b' at index 1 and 'b' at index 2: "bb" (length 2). This is the longest palindrome found.

// Input: s = "a"
// Output: "a"
// Explanation: Single character string is inherently a palindrome (reads same forwards and backwards).
```

**Time Complexity:** O(n²) - Expanding from each of 2n
  - 1 centers, each expansion takes O(n)  
**Space Complexity:** O(1) - Only using constant extra variables

Deep Insights:
  - Rule: Expand around centers (odd and even); track start/end indices not strings; O(n²) time, O(1) space.
  - Real-world: Palindrome detection, DNA sequence analysis, longest symmetric substring problems, pattern matching.
  - Common mistake: Slicing strings during iteration is expensive; track indices instead; forgetting to handle even-length palindromes.
  - Optimization: Manacher's gives O(n) but complex; expand-around simpler for interviews; handle ties consistently.
  - Interview tip: Mention Manacher's exists but use expand-around for simplicity; explain odd vs even center expansion.

## Q20. Group Anagrams

Concept:
Group anagrams together by generating unique key from character frequency counts for each string, using hash map to group.

Example:
```javascript
function groupAnagrams(strs) {
  const map = new Map();
  for (const s of strs) {
    const cnt = new Array(26).fill(0);
    for (const ch of s) cnt[ch.charCodeAt(0) - 97]++;
    const key = cnt.join('#');
    if (!map.has(key)) map.set(key, []);
    map.get(key).push(s);
  }
  return Array.from(map.values());
}

// Input: strs = ["eat","tea","tan","ate","nat","bat"]
// Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
// Explanation: "eat", "tea", "ate" all have frequency [1×e, 1×a, 1×t] → grouped together. "tan", "nat" have [1×t, 1×a, 1×n] → grouped. "bat" has [1×b, 1×a, 1×t] → separate group.

// Input: strs = [""]
// Output: [[""]]
// Explanation: Empty string has frequency count of all zeros, forming its own group.

// Input: strs = ["a"]
// Output: [["a"]]
// Explanation: Single string "a" has frequency [1×a] and forms its own group since no other string matches this frequency pattern.
```

**Time Complexity:** O(nk) - n strings, each processed in O(k) time where k is average string length  
**Space Complexity:** O(nk) -Hash map stores all strings

Deep Insights:
  - Rule: Generate unique key from character frequency counts; join with delimiter to avoid collisions; O(nk) time.
  - Real-world: Anagram grouping in word games, text analysis, document clustering, string categorization systems.
  - Common mistake: Key collisions without delimiter ("1,2,3" vs "12,3"); not handling empty strings correctly.
  - Optimization: Fixed array of size 26 for lowercase-only saves space; Map for Unicode flexibility; delimiter prevents collisions.
  - Interview tip: Ask about character set first; explain delimiter necessity; mention sorted string as alternative key approach.

## Q21. String Rotation / Reverse Words

Concept:
Reverse words by splitting on whitespace and reversing order. Check rotation by doubling first string—all rotations appear as substrings.

Example:
```javascript
function reverseWords(s) {
  return s.trim().split(/\s+/).reverse().join(' ');
}
function isRotation(a, b) {
  return a.length === b.length && (a + a).includes(b);
}

// reverseWords:
// Input: s = "the sky is blue"
// Output: "blue is sky the"
// Explanation: Split: ["the", "sky", "is", "blue"]. Reverse: ["blue", "is", "sky", "the"]. Join: "blue is sky the".

// Input: s = "  hello world  "
// Output: "world hello"
// Explanation: Split on whitespace (multiple spaces handled): ["hello", "world"]. Reverse: ["world", "hello"]. Join: "world hello" (leading/trailing spaces trimmed).

// isRotation:
// Input: a = "waterbottle", b = "erbottlewat"
// Output: true
// Explanation: Doubling "waterbottle" → "waterbottlewaterbottle". "erbottlewat" appears starting at index 2, confirming it's a rotation (erbottlewat = rotation starting from 'e').

// Input: a = "abc", b = "bca"
// Output: true
// Explanation: Doubling "abc" → "abcabc". "bca" appears at index 1, confirming rotation (bca = rotation starting from 'b').
```

**Time Complexity:** reverseWords: O(n), isRotation: O(n) -String operations  
**Space Complexity:** reverseWords: O(n), isRotation: O(n) - Additional space for split/concatenation

Deep Insights:
  - Rule: Reverse words by split/reverse/join; check rotation by doubling first string and checking substring; O(n) time.
  - Real-world: Text processing, string manipulation, rotation detection in circular buffers, word reordering.
  - Common mistake: Not handling multiple spaces correctly; empty strings after trim; rotation check needs length match first.
  - Optimization: String concatenation is immutable but includes() is efficient; split/join handles whitespace; doubling trick avoids nested loops.
  - Interview tip: Ask about whitespace handling first; explain why doubling works for rotation check; mention in-place reversal alternative.

## Q22. Longest Repeating Character Replacement

Concept:
Find longest substring with repeating chars after k replacements using sliding window tracking max frequency—window valid when (length-maxFreq) <= k.

Example:
```javascript
function characterReplacement(s, k) {
  const freq = new Array(26).fill(0);
  let left = 0;
  let best = 0;
  let maxF = 0;

  for (let right = 0; right < s.length; right++) {
    const idx = s.charCodeAt(right) - 65;
    freq[idx]++;
    maxF = Math.max(maxF, freq[idx]);

    while (right-left + 1 - maxF > k) {
      freq[s.charCodeAt(left) - 65]-- ;
      left++;
    }
    best = Math.max(best, right-left + 1);
  }
  return best;
}

// Input: s = "ABAB", k = 2
// Output: 4
// Explanation: Entire string "ABAB" can be converted: replace 2×'A' with 'B' → "BBBB" (all same). Window length 4, max frequency 2 (two 'B's), replacements needed: 4- 2=2 ≤ k=2. Valid window length 4.

// Input: s = "AABABBA", k = 1
// Output: 4
// Explanation: Best window: "AABA" or "ABBA". For "AABA": length 4, max frequency 3 (three 'A's), replace 1 'B' → "AAAA". For "ABBA": length 4, max frequency 2, replace 2 'B's → not valid with k=1. Best is 4.

// Input: s = "ABCDE", k = 1
// Output: 2
// Explanation: With k=1, we can replace only 1 character. Best window: "AB" (replace 'B' with 'A' → "AA") or "BC" (replace 'C' with 'B' → "BB"). Maximum length is 2.
```

**Time Complexity:** O(n) -Single pass with sliding window  
**Space Complexity:** O(1) - Fixed array of size 26 for lowercase letters

Deep Insights:
  - Rule: Sliding window with max frequency tracking; window valid when (length - maxFreq) <= k; O(n) time.
  - Real-world: Character replacement optimization, string modification problems, character frequency analysis.
  - Common mistake: maxF may be stale when window shrinks but acceptable; forgetting to handle empty string edge case.
  - Optimization: Fixed array of size 26 for lowercase-only; Map for Unicode flexibility; stale maxF doesn't affect correctness.
  - Interview tip: Explain why stale maxF is okay; ask about character set first; clarify that we only need maxF, not exact frequencies.
## Q23. Minimum Window Substring

Concept:
Find minimum window substring containing all characters of t using sliding window—expand to cover, then contract to minimize.

Example:
```javascript
function minWindow(s, t) {
  const need = new Map(), window = new Map();
  for (const c of t) need.set(c, (need.get(c) || 0) + 1);
  let left = 0, have = 0, needSize = need.size, bestLen = Infinity, best = [-1, -1];
  for (let right = 0; right < s.length; right++) {
    window.set(s[right], (window.get(s[right]) || 0) + 1);
    if (need.has(s[right]) && window.get(s[right]) === need.get(s[right])) have++;
    while (have === needSize) {
      if (right - left + 1 < bestLen) {
        bestLen = right - left + 1;
        best = [left, right];
      }
      window.set(s[left], window.get(s[left]) - 1);
      if (need.has(s[left]) && window.get(s[left]) < need.get(s[left])) {
        have--;
      }
      left++;
    }
  }
  return bestLen === Infinity ? '' : s.slice(best[0], best[1] + 1);
}

// Input: s = "ADOBECODEBANC", t = "ABC"
// Output: "BANC"
// Explanation: Need A, B, C each once. Window expands: "ADOBEC" (has A,B,C but length 6) → contract to "BECODEBA" → contract to "CODEBA" → expand to "CODEBANC" (length 7) → contract to "BANC" (length 4, has all A,B,C). Minimum is "BANC".

// Input: s = "a", t = "a"
// Output: "a"
// Explanation: String "a" contains character 'a' required by t. Minimum window is the entire string "a".

// Input: s = "a", t = "aa"
// Output: ""
// Explanation: Need two 'a' characters, but string s has only one 'a'. No valid window exists, return empty string.
```

**Time Complexity:** O(n + m) -Each character in s visited at most twice, where n=s.length, m=t.length  
**Space Complexity:** O(m) - Hash maps store characters from t and window

Deep Insights:
  - Rule: Sliding window expand to cover all characters, then contract to minimize; track best length and indices; O(n+m) time.
  - Real-world: Minimum substring search, text matching, window optimization problems, string containment checks.
  - Common mistake: Not tracking best length separately; slicing strings during iteration is expensive; forgetting to handle empty result.
  - Optimization: Track indices not strings; each character visited at most twice; O(n+m) time with hash maps.
  - Interview tip: Explain "have === needSize" clearly; ask about multiple valid windows; mention empty string edge case.

## Q24. Isomorphic Strings

Concept:
Check if strings are isomorphic using bidirectional character mapping tracked in two hash maps—one- to-one mapping required both ways.

Example:
```javascript
function isIsomorphic(s, t) {
  if (s.length !== t.length) return false;
  const m1 = new Map(), m2 = new Map();
  for (let i = 0; i < s.length; i++) {
    const a = s[i], b = t[i];
    if ((m1.has(a) && m1.get(a) !== b) || (m2.has(b) && m2.get(b) !== a)) return false;
    m1.set(a, b); m2.set(b, a);
  }
  return true;
}

// Input: s = "egg", t = "add"
// Output: true
// Explanation: e→a (forward), a→e (backward). First g→d (forward), d→g (backward). Second g→d (consistent with first g). Mapping is bidirectional and consistent.

// Input: s = "foo", t = "bar"
// Output: false
// Explanation: f→b, b→f (ok). First o→a, a→o (ok). Second o→r (but we already have o→a from first o). Conflict: 'o' cannot map to both 'a' and 'r'. Also, 'a' cannot map to both 'o' and 'r'. Not isomorphic.

// Input: s = "paper", t = "title"
// Output: true
// Explanation: p→t, t→p. a→i, i→a. p→t (consistent). e→l, l→e. r→e, e→r. Each character maps uniquely both ways without conflicts.
```

**Time Complexity:** O(n) - Single pass through strings  
**Space Complexity:** O(k) -Hash maps store unique characters from both strings (k is character set size)

Deep Insights:
  - Rule: Bidirectional character mapping with two maps (s→t and t→s); one-to-one mapping required both ways; O(n) time.
  - Real-world: String pattern matching, character encoding validation, isomorphic structure checking, pattern analysis.
  - Common mistake: Using only one map allows false positives; same character must map consistently; forgetting bidirectional check.
  - Optimization: Two maps ensure bidirectional consistency; works with any character set including Unicode; Map handles all characters.
  - Interview tip: Explain why two maps are needed; ask about Unicode support; mention that same character must map consistently.

## Q25. Count & Say

Concept:
Generate nth term of count- and-say sequence using run-length encoding on previous term—start with "1", describe each run as count+digit.

Example:
```javascript
function countAndSay(n) {
  let s = '1';
  while (n-- > 1) {
    let cur = '', i = 0;
    while (i < s.length) {
      let j = i;
      while (j < s.length && s[j] === s[i]) j++;
      cur += (j-i) + s[i]; i = j;
    }
    s = cur;
  }
  return s;
}

// Input: n = 1
// Output: "1"
// Explanation: Base case: first term is always "1" (no previous term to describe).

// Input: n = 4
// Output: "1211"
// Explanation: Term 1: "1" (one 1). Term 2: "11" (one 1 from term 1). Term 3: "21" (two 1s from term 2). Term 4: "1211" (one 2, one 1 from term 3). Final answer is "1211".

// Input: n = 5
// Output: "111221"
// Explanation: Term 4: "1211" (one 2, one 1, one 2, two 1s? Actually: one 1, one 2, two 1s). Term 5: "111221" (one 1, one 1, one 2, two 1s from term 4). Process: describe each run in order.
```

**Time Complexity:** O(2^n) - Exponential growth of string length  
**Space Complexity:** O(2^n) -Space for storing current term

Deep Insights:
  - Rule: Run-length encoding on previous term; start with "1"; describe each run as count+digit; O(2^n) space growth.
  - Real-world: Sequence generation, pattern description algorithms, recursive string building, mathematical sequences.
  - Common mistake: Not handling base case n=1 correctly; misunderstanding sequence generation; exponential space growth catches people off guard.
  - Optimization: String concatenation creates new strings; exponential growth is inherent; not true RLE compression.
  - Interview tip: Explain sequence clearly: "1"→"11"→"21"→"1211"; mention exponential growth; ask about n limits.

## Q26. Rabin
  - Karp / KMP Pattern Match

Concept:
Find pattern in string using KMP algorithm with LPS array to avoid backtracking—LPS stores longest prefix- suffix for each pattern position.

Example:
```javascript
function strStr(h, p) {
  if (p === '') return 0;
  const lps = new Array(p.length).fill(0);
  for (let i = 1, len = 0; i < p.length;) {
    if (p[i] === p[len]) lps[i++] = ++len;
    else if (len) len = lps[len - 1];
    else i++;
  }
  for (let i = 0, j = 0; i < h.length;) {
    if (h[i] === p[j]) {
      i++;
      j++;
      if (j === p.length) return i - j;
    } else if (j) {
      j = lps[j - 1];
    } else {
      i++;
    }
  }
  return -1;
}

// Input: haystack = "sadbutsad", needle = "sad"
// Output: 0
// Explanation: Pattern "sad" matches at index 0 of haystack "sadbutsad". Comparison: s=s, a=a, d=d. Match found immediately.

// Input: haystack = "leetcode", needle = "leeto"
// Output: -1
// Explanation: Pattern "leeto" does not exist in haystack "leetcode". Comparison: l=l, e=e, e=e, but t≠t (actually t≠c at index 3). LPS helps skip but no match found. Return - 1.

// Input: haystack = "mississippi", needle = "issip"
// Output: 4
// Explanation: Pattern "issip" found starting at index 4. LPS array for "issip": [0,0,0,1,0]. When mismatch at index 5, LPS[4]=0 allows skipping to next position. Match found at index 4: i-s- s-i- p.
```

**Time Complexity:** O(n + m) -Building LPS array (m) + searching (n), where n=haystack.length, m=needle.length  
**Space Complexity:** O(m) - LPS array storage

Deep Insights:
  - Rule: KMP uses LPS array to avoid backtracking; LPS stores longest prefix-suffix for each position; O(n+m) time.
  - Real-world: String search algorithms, pattern matching in text editors, DNA sequence analysis, search engines.
  - Common mistake: LPS array construction is tricky; forgetting that LPS avoids moving haystack pointer back; off-by-one errors in LPS.
  - Optimization: KMP preferred for single pattern; Rabin-Karp useful for multiple patterns with rolling hash; LPS avoids backtracking.
  - Interview tip: Explain how LPS avoids backtracking; mention haystack pointer never moves back; explain prefix-suffix overlap concept.

## Q27. Roman to Integer / Integer to Roman

Concept:
Convert Roman to integer handling subtractive pairs (IV, IX, etc.) by scanning left- to-right with lookahead. Convert integer to Roman using greedy value- symbol pairs.

Example:
```javascript
function romanToInt(s) {
  const val = new Map([['I',1],['V',5],['X',10],['L',50],['C',100],['D',500],['M',1000]]);
  let ans = 0;
  for (let i = 0; i < s.length; i++) {
    const v = val.get(s[i]), n = i + 1 < s.length ? val.get(s[i + 1]) : 0;
    ans += v < n ?-v : v;
  }
  return ans;
}

function intToRoman(num) {
  const pairs = [[1000,'M'],[900,'CM'],[500,'D'],[400,'CD'],[100,'C'],[90,'XC'],[50,'L'],[40,'XL'],[10,'X'],[9,'IX'],[5,'V'],[4,'IV'],[1,'I']];
  let s = '';
  for (const [v, ch] of pairs) {
    while (num >= v) {
      s += ch;
      num -= v;
    }
  }
  return s;
}

// romanToInt:
// Input: s = "III"
// Output: 3
// Explanation: I=1, next I=1 (1<1? no), add 1. I=1, next I=1 (1<1? no), add 1. I=1, no next, add 1. Total: 1+1+1=3.

// Input: s = "LVIII"
// Output: 58
// Explanation: L=50, next V=5 (50<5? no), add 50. V=5, next I=1 (5<1? no), add 5. I=1, next I=1 (1<1? no), add 1. I=1, next I=1 (1<1? no), add 1. I=1, no next, add 1. Total: 50+5+1+1+1=58.

// Input: s = "MCMXCIV"
// Output: 1994
// Explanation: M=1000, next C=100 (1000<100? no), add 1000. C=100, next M=1000 (100<1000? yes), subtract 100. M=1000, no subtract applied here. Process continues: +1000, - 100, +1000, - 10, +100, - 1, +5. Total: 1000- 100+1000
  - 10+100- 1+5 = 1994.

// intToRoman:
// Input: num = 3
// Output: "III"
// Explanation: 3 >= 1? yes, append "I", num=2. 2 >= 1? yes, append "I", num=1. 1 >= 1? yes, append "I", num=0. Result: "III".

// Input: num = 58
// Output: "LVIII"
// Explanation: 58 >= 50? yes, append "L", num=8. 8 >= 5? yes, append "V", num=3. 3 >= 1? yes, append "I", num=2. 2 >= 1? yes, append "I", num=1. 1 >= 1? yes, append "I", num=0. Result: "LVIII".

// Input: num = 1994
// Output: "MCMXCIV"
// Explanation: 1994 >= 1000? yes, append "M", num=994. 994 >= 900? yes, append "CM", num=94. 94 >= 90? yes, append "XC", num=4. 4 >= 4? yes, append "IV", num=0. Result: "MCMXCIV".
```

**Time Complexity:** romanToInt: O(n), intToRoman: O(1) -Both process fixed number of symbols  
**Space Complexity:** O(1) - Only using constant extra variables

Deep Insights:
  - Rule: Algorithm and complexity
  - Real-world: Application use cases
  - Common mistake: Common errors
  - Optimization: Optimization techniques
  - Interview tip: Interview strategy
  -  Greedy approach works perfectly for intToRoman conversion—always use largest possible value- symbol pair first (starting from 1000, then 900, etc.), subtract from number, then recurse on remainder, ensuring optimal minimal-length representation.
- Inputs are guaranteed within constraints (1 to 3999)—standard Roman numeral range where largest representable is MMMCMXCIX (3999), so no need to handle numbers beyond this range or negative numbers. -Interview tip: Explain why IV = 4 but VI = 6 clearly—subtractive notation (smaller before larger) only applies when reading left- to-right; IV means "one before five" = 5- 1 = 4, while VI means "five plus one" = 5+1 = 6; subtractive notation is exception, not the rule.

## Q28. Longest Common Prefix

Concept:
Find longest common prefix by trimming first string until it matches start of all subsequent strings.

Example:
```javascript
function longestCommonPrefix(strs) {
  if (!strs.length) return '';
  let pre = strs[0];
  for (let i = 1; i < strs.length; i++) {
    while (strs[i].indexOf(pre) !== 0) {
      pre = pre.slice(0, -1);
      if (!pre) return '';
    }
  }
  return pre;
}

// Input: strs = ["flower","flow","flight"]
// Output: "fl"
// Explanation: Start with prefix="flower". Compare with "flow": "flower".indexOf("flower")≠0, trim to "flowe" → "flowe".indexOf("flow")≠0 → continue trimming → "flo".indexOf("flow")≠0 → "fl".indexOf("flow")=0 ✓. Compare with "flight": "fl".indexOf("flight")≠0, but "fl" is prefix of "flight" ✓. Final: "fl".

// Input: strs = ["dog","racecar","car"]
// Output: ""
// Explanation: Start with prefix="dog". Compare with "racecar": "dog".indexOf("racecar")≠0, trim → "do" → "d" → "" (no match). Empty prefix → no common prefix exists.

// Input: strs = ["ab","a"]
// Output: "a"
// Explanation: Start with prefix="ab". Compare with "a": "a".indexOf("ab")≠0 (second string is shorter), so trim prefix to "a". Now "a".indexOf("a")=0 ✓. Final common prefix is "a".
```

**Time Complexity:** O(nk) - n strings, each compared with prefix where k is average string length  
**Space Complexity:** O(1) -Only using constant extra variables (excluding input)

Deep Insights:
  - Rule: Compare prefix character-by-character across strings; trim prefix when mismatch found; O(nk) time.
  - Real-world: Prefix matching in autocomplete, URL routing, command-line tools, file path processing.
  - Common mistake: Not handling empty strings correctly; case sensitivity issues; forgetting to trim prefix on mismatch.
  - Optimization: Trie for many queries; binary search on prefix length for long strings; indexOf trimming is straightforward.
  - Interview tip: Ask about case sensitivity first; mention trie alternative; explain why character-by-character works.

## Q29. Length of Last Word

Concept:
Find length of last word in string; trim trailing spaces, then count characters until space or end.

Example:
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

Deep Insights:
- Traverse from end; skip trailing spaces; count characters until space; O(n) time, O(1) space.
- Handle trailing spaces first; then count word characters.
- Edge case: All spaces returns 0; single word returns word length.
- Interview tip: Explain two-pass from end; mention trailing space handling.

## Q30. Zigzag Conversion

Concept:
Arrange string in zigzag pattern across numRows rows; read row by row from left to right.

Example:
```javascript
function convert(s, numRows) {
  if (numRows === 1) return s;
  
  const rows = Array(numRows).fill('');
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
```

**Time Complexity:** O(n) - Single pass through string  
**Space Complexity:** O(n) - Storage for all rows

Deep Insights:
- Simulate zigzag movement; track direction (up/down); append to appropriate row; O(n) time, O(n) space.
- Change direction at top (row 0) and bottom (row numRows-1).
- Edge case: numRows = 1 returns original string; numRows >= length returns original.
- Interview tip: Explain direction change logic; mention row tracking strategy.

## Q31. Find the Index of the First Occurrence in a String

Concept:
Find first occurrence of needle in haystack using KMP algorithm or simple iteration.

Example:
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

**Time Complexity:** O(m×n) - For each position check needle; can be O(m+n) with KMP  
**Space Complexity:** O(1) - Constant extra space

Deep Insights:
- Simple approach: check each starting position; O(m×n) time worst case.
- KMP algorithm optimizes to O(m+n) using failure function.
- Edge case: Empty needle returns 0; needle longer than haystack returns -1.
- Interview tip: Mention KMP optimization; explain brute force first; ask about performance.

## Q32. Text Justification

Concept:
Distribute words across lines with maxWidth; left-justify last line; distribute spaces evenly in middle lines.

Example:
```javascript
function fullJustify(words, maxWidth) {
  const result = [];
  let currentLine = [];
  let currentLength = 0;
  
  for (const word of words) {
    if (currentLength + currentLine.length + word.length > maxWidth) {
      // Format current line
      if (currentLine.length === 1) {
        result.push(currentLine[0] + ' '.repeat(maxWidth - currentLength));
      } else {
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

// Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
// Output: [
//   "This    is    an",
//   "example  of text",
//   "justification.  "
// ]

// Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
// Output: [
//   "What   must   be",
//   "acknowledgment  ",
//   "shall be        "
// ]
```

**Time Complexity:** O(n×maxWidth) - Process each word and format lines  
**Space Complexity:** O(n×maxWidth) - Result array storage

Deep Insights:
- Group words into lines; distribute spaces evenly; left-justify last line; O(n×maxWidth) time.
- Calculate spaces per gap; distribute extra spaces to left gaps.
- Last line handled separately: join with single space, pad to maxWidth.
- Edge case: Single word per line; last line formatting differs.
- Interview tip: Explain space distribution logic; mention last line special handling.

## Q33. Ransom Note

Concept:
Check if ransom note can be constructed from magazine using character frequency counts.

Example:
```javascript
function canConstruct(ransomNote, magazine) {
  const freq = new Map();
  
  // Count characters in magazine
  for (const char of magazine) {
    freq.set(char, (freq.get(char) || 0) + 1);
  }
  
  // Check ransom note
  for (const char of ransomNote) {
    const count = freq.get(char) || 0;
    if (count === 0) return false;
    freq.set(char, count - 1);
  }
  
  return true;
}

// Input: ransomNote = "a", magazine = "b"
// Output: false
// Explanation: Missing character 'a' in magazine

// Input: ransomNote = "aa", magazine = "ab"
// Output: false
// Explanation: Only one 'a' in magazine

// Input: ransomNote = "aa", magazine = "aab"
// Output: true
// Explanation: Two 'a's in magazine
```

**Time Complexity:** O(m + n) - Pass through both strings  
**Space Complexity:** O(m) - Frequency map storage

Deep Insights:
- Count characters in magazine; check ransom note characters; O(m + n) time, O(m) space.
- Hash map for character frequency; decrement when used.
- Return false if character not available or count becomes zero.
- Edge case: Empty ransom note returns true; empty magazine with non-empty note returns false.
- Interview tip: Explain frequency counting; mention hash map usage.

## Q34. Word Pattern

Concept:
Check if string follows pattern using bidirectional mapping between pattern characters and words.

Example:
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

// Input: pattern = "abba", s = "dog cat cat dog"
// Output: true
// Explanation: a -> dog, b -> cat

// Input: pattern = "abba", s = "dog cat cat fish"
// Output: false
// Explanation: a -> dog, b -> cat, but b should map to fish

// Input: pattern = "aaaa", s = "dog cat cat dog"
// Output: false
// Explanation: a should map to same word always
```

**Time Complexity:** O(n) - Single pass through pattern and words  
**Space Complexity:** O(n) - Map storage

Deep Insights:
- Maintain bidirectional mapping; check consistency in both directions; O(n) time, O(n) space.
- Two maps: pattern→word and word→pattern for bidirectional check.
- Return false if mapping conflicts in either direction.
- Edge case: Different lengths return false; empty pattern and string return true.
- Interview tip: Explain bidirectional mapping necessity; mention consistency check.

## Q35. Happy Number

Concept:
Check if number is happy (sum of squares of digits eventually equals 1); use Floyd's cycle detection.

Example:
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
  
  while (fast !== 1 && slow !== fast) {
    slow = getNext(slow);
    fast = getNext(getNext(fast));
  }
  
  return fast === 1;
}

// Input: n = 19
// Output: true
// Explanation: 19 -> 82 -> 68 -> 100 -> 1

// Input: n = 2
// Output: false
// Explanation: Enters cycle: 2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4

// Input: n = 1
// Output: true
```

**Time Complexity:** O(log n) - Digits in number  
**Space Complexity:** O(1) - Constant extra space

Deep Insights:
- Use Floyd's cycle detection; calculate sum of digit squares; O(log n) time, O(1) space.
- Fast/slow pointers detect cycle; if cycle contains 1, number is happy.
- Alternative: use hash set to detect cycle (O(log n) space).
- Edge case: Number 1 is happy; numbers entering cycle without 1 are not happy.
- Interview tip: Explain cycle detection; mention Floyd's algorithm; ask about alternative approaches.

## Q36. Contains Duplicate II

Concept:
Check if array has duplicate values within k distance using sliding window with hash map.

Example:
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
    seen.set(nums[i], i);
  }
  
  return false;
}

// Input: nums = [1,2,3,1], k = 3
// Output: true
// Explanation: nums[0] = nums[3] = 1, distance = 3

// Input: nums = [1,0,1,1], k = 1
// Output: true
// Explanation: nums[2] = nums[3] = 1, distance = 1

// Input: nums = [1,2,3,1,2,3], k = 2
// Output: false
// Explanation: Duplicates exist but distance > 2
```

**Time Complexity:** O(n) - Single pass through array  
**Space Complexity:** O(min(n,k)) - Map storage

Deep Insights:
- Use hash map to track last index of each value; check distance constraint; O(n) time, O(min(n,k)) space.
- Sliding window approach: maintain indices within k distance.
- Update map with current index; check if previous index within k.
- Edge case: k = 0 returns false (no duplicates possible); k >= n checks all array.
- Interview tip: Explain sliding window technique; mention distance constraint.

## Q37. Substring with Concatenation of All Words

Concept:
Find all starting indices of substrings that are concatenation of all words in any order.

Example:
```javascript
function findSubstring(s, words) {
  const wordLength = words[0].length;
  const totalLength = words.length * wordLength;
  const wordCount = new Map();
  
  // Count words
  for (const word of words) {
    wordCount.set(word, (wordCount.get(word) || 0) + 1);
  }
  
  const result = [];
  
  for (let i = 0; i <= s.length - totalLength; i++) {
    const seen = new Map();
    let j = 0;
    
    while (j < words.length) {
      const start = i + j * wordLength;
      const word = s.substring(start, start + wordLength);
      
      if (!wordCount.has(word)) break;
      
      seen.set(word, (seen.get(word) || 0) + 1);
      
      if (seen.get(word) > wordCount.get(word)) break;
      
      j++;
    }
    
    if (j === words.length) {
      result.push(i);
    }
  }
  
  return result;
}

// Input: s = "barfoothefoobarman", words = ["foo","bar"]
// Output: [0,9]
// Explanation: "barfoo" at index 0, "foobar" at index 9

// Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
// Output: []
// Explanation: No valid concatenation

// Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
// Output: [6,9,12]
```

**Time Complexity:** O(n×m×k) - n positions, m words, k word length  
**Space Complexity:** O(m) - Word count maps

Deep Insights:
- Check each starting position; use sliding window for words; O(n×m×k) time.
- Count words in input; check if substring matches word count.
- Use hash map to track seen words; break if count exceeds expected.
- Edge case: Empty string or words returns empty; no match returns empty.
- Interview tip: Explain sliding window approach; mention word counting; ask about optimization.
