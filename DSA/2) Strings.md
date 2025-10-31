# Strings

## Q16. Valid Anagram

- Concept: Count characters (hash map) and compare.

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
```

- Deep Insights:
  - Sorting works but is O(n log n); counting is O(n).
  - Use fixed array of size 26 for lowercase letters.
  - Unicode needs Map, not fixed array.
  - Early exit on length mismatch.

## Q17. Longest Substring Without Repeating Characters

- Concept: Sliding window with last seen index.

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
```

- Deep Insights:
  - O(n) with window; avoid O(n^2) checks.
  - Store rightmost positions to jump left pointer.
  - Works with any charset using Map.
  - Empty string returns 0.

## Q18. Palindrome Check

- Concept: Two pointers from ends; skip non-alnum if needed.

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
```

- Deep Insights:
  - Normalize case to compare.
  - Skip non-alphanumeric for phrase checks.
  - Single char and empty are palindromes.
  - For Unicode, use proper category checks.

## Q19. Longest Palindromic Substring

- Concept: Expand around centers (odd and even).

```javascript
function longestPalindrome(s) {
  if (s.length < 2) return s;
  let start = 0;
  let end = 0;

  const expand = (l, r) => {
    while (l >= 0 && r < s.length && s[l] === s[r]) { l--; r++; }
    return [l + 1, r - 1];
  };

  for (let i = 0; i < s.length; i++) {
    const [l1, r1] = expand(i, i);
    const [l2, r2] = expand(i, i + 1);
    if (r1 - l1 > end - start) { start = l1; end = r1; }
    if (r2 - l2 > end - start) { start = l2; end = r2; }
  }
  return s.slice(start, end + 1);
}
```

- Deep Insights:
  - O(n^2) time, O(1) space.
  - Manacher’s gives O(n) but is complex.
  - Track bounds, not strings, for speed.
  - Handle ties consistently (first longest).

## Q20. Group Anagrams

- Concept: Key by character frequency signature.

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
```

- Deep Insights:
  - Sorting key O(k log k) vs count key O(k).
  - Stable grouping across identical strings.
  - For unicode, use Map counts.
  - Avoid collisions by delimiter in key.

## Q21. String Rotation / Reverse Words

- Concept: Reverse words by splitting and reversing order; rotation via doubling.

```javascript
function reverseWords(s) {
  return s.trim().split(/\s+/).reverse().join(' ');
}
function isRotation(a, b) {
  return a.length === b.length && (a + a).includes(b);
}
```

- Deep Insights:
  - Use regex to collapse spaces.
  - Rotation requires equal lengths.
  - Doubling trick checks all rotations.
  - Watch for empty strings.

## Q22. Longest Repeating Character Replacement

- Concept: Sliding window tracking most frequent char count.

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

    while (right - left + 1 - maxF > k) {
      freq[s.charCodeAt(left) - 65]--;
      left++;
    }
    best = Math.max(best, right - left + 1);
  }
  return best;
}
```

- Deep Insights:
  - Window length minus max frequency <= k.
  - maxF may be stale, but ok for correctness.
  - O(n) time with fixed alphabet.
  - For general chars, use Map.

## Q23. Minimum Window Substring

- Concept: Expand to cover, contract to minimal.

```javascript
function minWindow(s, t) {
  if (t.length === 0) return '';
  const need = new Map();
  for (const c of t) need.set(c, (need.get(c) || 0) + 1);

  const window = new Map();
  let haveKinds = 0;
  const needKinds = need.size;
  let bestLen = Infinity;
  let best = [-1, -1];
  let left = 0;

  for (let right = 0; right < s.length; right++) {
    const c = s[right];
    window.set(c, (window.get(c) || 0) + 1);
    if (need.has(c) && window.get(c) === need.get(c)) haveKinds++;

    while (haveKinds === needKinds) {
      if (right - left + 1 < bestLen) {
        bestLen = right - left + 1;
        best = [left, right];
      }
      const d = s[left++];
      window.set(d, window.get(d) - 1);
      if (need.has(d) && window.get(d) < need.get(d)) haveKinds--;
    }
  }
  return bestLen === Infinity ? '' : s.slice(best[0], best[1] + 1);
}
```

- Deep Insights:
  - Two maps: need and window.
  - Only contract when valid.
  - Track best length and indices.
  - O(n) average with hash maps.

## Q24. Isomorphic Strings

- Concept: Bidirectional mapping between characters.

```javascript
function isIsomorphic(s, t) {
  if (s.length !== t.length) return false;
  const m1 = new Map();
  const m2 = new Map();

  for (let i = 0; i < s.length; i++) {
    const a = s[i];
    const b = t[i];
    if ((m1.has(a) && m1.get(a) !== b) || (m2.has(b) && m2.get(b) !== a)) return false;
    m1.set(a, b);
    m2.set(b, a);
  }
  return true;
}
```

- Deep Insights:
  - One-to-one mapping required both ways.
  - Length mismatch fails early.
  - Same char must map consistently.
  - Works for any charset.

## Q25. Count & Say

- Concept: Build next term by run-length encoding.

```javascript
function countAndSay(n) {
  let s = '1';
  while (n-- > 1) {
    let cur = '';
    let i = 0;
    while (i < s.length) {
      let j = i;
      while (j < s.length && s[j] === s[i]) j++;
      cur += (j - i) + s[i];
      i = j;
    }
    s = cur;
  }
  return s;
}
```

- Deep Insights:
  - O(total length) across iterations.
  - String concatenation can be costly; consider arrays.
  - Base case n=1 is '1'.
  - Not true RLE compression; just description.

## Q26. Rabin-Karp / KMP Pattern Match

- Concept: KMP failure function for O(n + m) worst-case.

```javascript
function strStr(h, p) {
  if (p === '') return 0;
  const lps = new Array(p.length).fill(0);

  // build LPS
  for (let i = 1, len = 0; i < p.length;) {
    if (p[i] === p[len]) lps[i++] = ++len;
    else if (len) len = lps[len - 1];
    else i++;
  }

  // search
  for (let i = 0, j = 0; i < h.length;) {
    if (h[i] === p[j]) { i++; j++; if (j === p.length) return i - j; }
    else if (j) j = lps[j - 1];
    else i++;
  }
  return -1;
}
```

- Deep Insights:
  - LPS array stores longest proper prefix which is also suffix.
  - Deterministic linear time.
  - Prefer KMP over RK for exact match without hashing.
  - RK useful for rolling hash multiple queries.

## Q27. Valid Parentheses

- Concept: Stack of opening brackets; match closers.

```javascript
function isValid(s) {
  const stack = [];
  const map = { ')': '(', ']': '[', '}': '{' };

  for (const c of s) {
    if (c in map) {
      if (stack.pop() !== map[c]) return false;
    } else {
      stack.push(c);
    }
  }
  return stack.length === 0;
}
```

- Deep Insights:
  - Early fail on mismatch.
  - Only three bracket types considered.
  - Empty string is valid.
  - Push only openers.

## Q28. Roman to Integer / Integer to Roman

- Concept: Aggregation with subtractive pairs.

```javascript
function romanToInt(s) {
  const val = new Map([
    ['I', 1], ['V', 5], ['X', 10], ['L', 50],
    ['C', 100], ['D', 500], ['M', 1000]
  ]);
  let ans = 0;
  for (let i = 0; i < s.length; i++) {
    const v = val.get(s[i]);
    const n = i + 1 < s.length ? val.get(s[i + 1]) : 0;
    ans += v < n ? -v : v;
  }
  return ans;
}

function intToRoman(num) {
  const pairs = [
    [1000,'M'],[900,'CM'],[500,'D'],[400,'CD'],
    [100,'C'],[90,'XC'],[50,'L'],[40,'XL'],
    [10,'X'],[9,'IX'],[5,'V'],[4,'IV'],[1,'I']
  ];
  let s = '';
  for (const [v, ch] of pairs) {
    while (num >= v) { s += ch; num -= v; }
  }
  return s;
}
```

- Deep Insights:
  - Subtractive cases: IV, IX, XL, XC, CD, CM.
  - Left-to-right scan with lookahead.
  - Greedy works for intToRoman.
  - Inputs are within constraints (1..3999).

## Q29. Longest Common Prefix

- Concept: Horizontal scan trimming the prefix.

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
```

- Deep Insights:
  - Early exit on empty.
  - Trie alternative when many queries.
  - Binary search on prefix length is viable.
  - Beware case sensitivity.

## Q30. Edit Distance (DP)

- Concept: Classic Levenshtein DP with insert/delete/replace.

```javascript
function minDistance(a, b) {
  const m = a.length;
  const n = b.length;
  const dp = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));

  for (let i = 0; i <= m; i++) dp[i][0] = i;
  for (let j = 0; j <= n; j++) dp[0][j] = j;

  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      if (a[i - 1] === b[j - 1]) dp[i][j] = dp[i - 1][j - 1];
      else dp[i][j] = 1 + Math.min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]);
    }
  }
  return dp[m][n];
}
```

- Deep Insights:
  - O(mn) time/space; optimize to O(min(m,n)) space.
  - Operations: insert, delete, replace.
  - Base cases are first row/column.
  - DP table traversal is row-major.
