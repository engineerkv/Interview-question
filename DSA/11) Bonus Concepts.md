# Bonus: Important Concepts

## Sliding Window

- Concept: Maintain a moving subarray/substring satisfying a property; grow right, shrink left to restore validity.

```javascript
// Longest substring with at most k distinct characters
function lenAtMostK(s, k) {
  const freq = new Map();
  let left = 0;
  let best = 0;

  for (let right = 0; right < s.length; right++) {
    const char = s[right];
    freq.set(char, (freq.get(char) || 0) + 1);

    while (freq.size > k) {
      const drop = s[left++];
      const next = freq.get(drop) - 1;
      if (next === 0) freq.delete(drop);
      else freq.set(drop, next);
    }

    best = Math.max(best, right - left + 1);
  }
  return best;
}
```

- Deep Insights:
  - O(n) with amortized pointer moves.
  - Choose invariant (size, sum, distinct).
  - For fixed-size windows, no inner while.
  - Maps/arrays store window state.

## Two Pointer

- Concept: Use two indices to traverse from ends or sweep with relative motion to meet constraints.

```javascript
// Two-sum on a sorted array
function twoSumSorted(arr, target) {
  let left = 0;
  let right = arr.length - 1;

  while (left < right) {
    const sum = arr[left] + arr[right];
    if (sum === target) return [left, right];
    if (sum < target) left++;
    else right--;
  }
  return [-1, -1];
}
```

- Deep Insights:
  - Requires order or a monotonic property.
  - Beats nested loops to O(n).
  - Useful for partitioning/compaction.
  - Generalize to 3Sum with inner two-pointer.

## Prefix Sum

- Concept: Transform range queries to differences of cumulative sums; extend to 2D and counts maps.

```javascript
// Count subarrays with sum equal to k
function subarraySum(nums, k) {
  const count = new Map([[0, 1]]);
  let sum = 0;
  let ans = 0;

  for (const x of nums) {
    sum += x;
    ans += count.get(sum - k) || 0;
    count.set(sum, (count.get(sum) || 0) + 1);
  }
  return ans;
}
```

- Deep Insights:
  - O(n); handles negatives.
  - Pre-seed 0 -> 1 for exact hits.
  - 2D prefix for matrix ranges.
  - Works with XOR (replace + with ^).

## Bit Manipulation

- Concept: Use bitwise ops to encode sets, parity, and arithmetic tricks efficiently.

```javascript
// Single number where every other element appears twice
function singleNumber(arr) {
  let x = 0;
  for (const v of arr) x ^= v;
  return x;
}
```

- Deep Insights:
  - x^x=0, x^0=x; XOR cancels pairs.
  - Check bit: (x >> i) & 1; set/clear: x |= 1 << i, x &= ~(1 << i).
  - Lowbit: x & -x (Fenwick/BIT).
  - Use masks for subsets DP.

## Trie (Autocomplete / Word Dictionary)

- Concept: Prefix tree storing characters per edge; supports insert, search, prefix search in O(L).

```javascript
class Trie {
  constructor() {
    this.root = {};
  }

  insert(word) {
    let node = this.root;
    for (const ch of word) {
      node[ch] = node[ch] || {};
      node = node[ch];
    }
    node.$ = true; // end marker
  }

  search(word) {
    let node = this.root;
    for (const ch of word) {
      if (!node[ch]) return false;
      node = node[ch];
    }
    return !!node.$;
  }

  startsWith(prefix) {
    let node = this.root;
    for (const ch of prefix) {
      if (!node[ch]) return false;
      node = node[ch];
    }
    return true;
  }
}
```

- Deep Insights:
  - Use `$` (or boolean) to mark word end.
  - Memory heavy; compress with arrays or radix.
  - Great for prefix queries, autocomplete.
  - Wildcards require backtracking.
