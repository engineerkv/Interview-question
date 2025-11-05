# Math

## Q224. Palindrome Number

**Problem:** Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

**Approach:** Reverse half of the number and compare with remaining half. Stop when reversed >= original.

### Solution 1: Half Reversal (Optimal)
```javascript
function isPalindrome(x) {
  // Negative numbers and multiples of 10 (except 0) are not palindromes
  if (x < 0 || (x !== 0 && x % 10 === 0)) return false;
  
  let reversed = 0;
  
  // Reverse half of number
  while (x > reversed) {
    reversed = reversed * 10 + x % 10;
    x = Math.floor(x / 10);
  }
  
  // Compare: x === reversed (even digits) or x === reversed/10 (odd digits)
  return x === reversed || x === Math.floor(reversed / 10);
}

// Test Cases:
// Input: x = 121
// Output: true
// Explanation: Reads 121 from left to right and from right to left

// Input: x = -121
// Output: false
// Explanation: From left to right, it reads -121. From right to left, it becomes 121-

// Input: x = 10
// Output: false
// Explanation: Reads 01 from right to left

// Input: x = -101
// Output: false
```

**Time Complexity:** O(log n) - Number of digits  
**Space Complexity:** O(1) - Constant extra space

**Deep Insights:**
- **Optimal Approach:** Half reversal achieves O(log n) time, O(1) space—optimal for palindrome
- **Half Reversal:** Reverse only half of number—avoids full reversal and overflow
- **Key Insight:** Stop when reversed >= original—compares halves efficiently
- **Edge Case Handling:** Negative numbers and multiples of 10 (except 0) are not palindromes
- **Even/Odd Digits:** Handle both cases—x === reversed or x === reversed/10
- **Edge Cases:** Single digit returns true; 0 returns true; handles all cases
- **Interview Tip:** Explain half-reversal strategy clearly; emphasize edge cases; mention optimization

## Q225. Plus One

**Problem:** You are given a large integer represented as an integer array `digits`, where each `digits[i]` is the `i`th digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading zeros. Increment the large integer by one and return the resulting array of digits.

**Approach:** Add one from right to left. If digit < 9, increment and return. If digit = 9, set to 0 and continue. If all 9s, add new digit at front.

### Solution 1: Carry Propagation (Optimal)
```javascript
function plusOne(digits) {
  for (let i = digits.length - 1; i >= 0; i--) {
    if (digits[i] < 9) {
      digits[i]++;
      return digits;
    }
    digits[i] = 0;  // Carry propagation
  }
  
  // All 9s, need to add new digit at front
  digits.unshift(1);
  return digits;
}

// Test Cases:
// Input: digits = [1,2,3]
// Output: [1,2,4]
// Explanation: 123 + 1 = 124

// Input: digits = [4,3,2,1]
// Output: [4,3,2,2]
// Explanation: 4321 + 1 = 4322

// Input: digits = [9]
// Output: [1,0]
// Explanation: 9 + 1 = 10

// Input: digits = [9,9,9]
// Output: [1,0,0,0]
// Explanation: 999 + 1 = 1000
```

**Time Complexity:** O(n) - Worst case traverse all digits  
**Space Complexity:** O(1) - Excluding result array

**Deep Insights:**
- **Optimal Approach:** Carry propagation achieves O(n) time—optimal for plus one
- **Carry Handling:** Propagate carry from right to left—same as decimal addition
- **All 9s Case:** If all digits are 9, add new digit at front—handles overflow
- **Key Insight:** Early return when digit < 9—optimizes common case
- **Edge Cases:** Single digit handled; all 9s handled correctly; handles all cases
- **Interview Tip:** Explain carry propagation clearly; emphasize all 9s case; mention early return optimization

## Q226. Factorial Trailing Zeroes

**Problem:** Given an integer `n`, return the number of trailing zeroes in `n!`. Note that `n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1`.

**Approach:** Count factors of 5 in n!. Each 5 contributes a trailing zero (paired with a 2). Count powers of 5 repeatedly.

### Solution 1: Factor 5 Counting (Optimal)
```javascript
function trailingZeroes(n) {
  let count = 0;
  
  // Count factors of 5 (including powers: 25, 125, etc.)
  while (n >= 5) {
    count += Math.floor(n / 5);
    n = Math.floor(n / 5);
  }
  
  return count;
}

// Test Cases:
// Input: n = 3
// Output: 0
// Explanation: 3! = 6, no trailing zero

// Input: n = 5
// Output: 1
// Explanation: 5! = 120, one trailing zero

// Input: n = 0
// Output: 0

// Input: n = 25
// Output: 6
// Explanation: 25! has 6 trailing zeroes (5, 10, 15, 20, 25 contribute; 25 contributes 2)
```

**Time Complexity:** O(log n) - Base 5 logarithm  
**Space Complexity:** O(1) - Constant extra space

**Deep Insights:**
- **Optimal Approach:** Factor 5 counting achieves O(log n) time—optimal for trailing zeroes
- **Factor 5:** Each 5 contributes a trailing zero—paired with abundant 2s
- **Powers of 5:** Count 25, 125, etc. repeatedly—each contributes multiple zeroes
- **Key Insight:** Count factors of 5 repeatedly—handles all powers of 5
- **Edge Cases:** n=0 returns 0; n<5 returns 0; handles all cases
- **Interview Tip:** Explain factor 5 counting clearly; emphasize pairing with 2s; mention powers of 5

## Q227. Sqrt(x)

**Problem:** Given a non-negative integer `x`, return the square root of `x` rounded down to the nearest integer. The returned integer should be non-negative as well. You must not use any built-in exponent function or operator.

**Approach:** Use binary search to find largest number whose square <= x. Search in range [2, x/2].

### Solution 1: Binary Search (Optimal)
```javascript
function mySqrt(x) {
  if (x < 2) return x;
  
  let left = 2, right = Math.floor(x / 2);
  
  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    const square = mid * mid;
    
    if (square === x) {
      return mid;
    } else if (square < x) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  
  return right;  // Largest number whose square <= x
}

// Test Cases:
// Input: x = 4
// Output: 2

// Input: x = 8
// Output: 2
// Explanation: Square root of 8 is 2.82842..., and since 2^2 < 8 < 3^2, return 2

// Input: x = 0
// Output: 0

// Input: x = 1
// Output: 1
```

**Time Complexity:** O(log x) - Binary search  
**Space Complexity:** O(1) - Constant extra space

**Deep Insights:**
- **Optimal Approach:** Binary search achieves O(log x) time—optimal for square root
- **Binary Search:** Find largest number whose square <= x—efficient search
- **Key Insight:** Search in range [2, x/2]—optimizes bounds
- **Return Value:** Return right when not found—largest valid square root
- **Edge Cases:** x=0 returns 0; x=1 returns 1; handles all cases
- **Interview Tip:** Explain binary search strategy clearly; emphasize bounds optimization; mention precision

## Q228. Pow(x, n)

**Problem:** Implement `pow(x, n)`, which calculates `x` raised to the power `n` (i.e., `x^n`).

**Approach:** Use binary exponentiation. If n is odd, multiply result by x. Square x and halve n. Handle negative n by inverting x.

### Solution 1: Binary Exponentiation (Optimal)
```javascript
function myPow(x, n) {
  if (n === 0) return 1;
  if (n < 0) {
    x = 1 / x;
    n = -n;
  }
  
  let result = 1;
  
  while (n > 0) {
    // If n is odd, multiply result by x
    if (n % 2 === 1) {
      result *= x;
    }
    // Square x and halve n
    x *= x;
    n = Math.floor(n / 2);
  }
  
  return result;
}

// Test Cases:
// Input: x = 2.00000, n = 10
// Output: 1024.00000

// Input: x = 2.10000, n = 3
// Output: 9.26100

// Input: x = 2.00000, n = -2
// Output: 0.25000
// Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
```

**Time Complexity:** O(log n) - Binary exponentiation  
**Space Complexity:** O(1) - Constant extra space

**Deep Insights:**
- **Optimal Approach:** Binary exponentiation achieves O(log n) time—optimal for pow
- **Binary Exponentiation:** Square x and halve n—reduces operations exponentially
- **Odd n Handling:** Multiply result by x when n is odd—accumulates result
- **Key Insight:** x^n = (x^(n/2))^2 if n even, x * (x^((n-1)/2))^2 if n odd—divide and conquer
- **Negative n:** Invert x and make n positive—handles negative exponents
- **Edge Cases:** n=0 returns 1; x=0 returns 0; handles all cases
- **Interview Tip:** Explain binary exponentiation clearly; emphasize negative exponent handling; mention optimization

## Q229. Max Points on a Line

**Problem:** Given an array of `points` where `points[i] = [xi, yi]` represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

**Approach:** For each point, calculate slopes to all other points. Normalize slopes using GCD. Count points with same normalized slope. Handle duplicate points separately.

### Solution 1: Slope Normalization (Optimal)
```javascript
function maxPoints(points) {
  if (points.length <= 2) return points.length;
  
  let max = 2;
  
  for (let i = 0; i < points.length; i++) {
    const slopes = new Map();
    let same = 1;  // Count duplicate points
    
    for (let j = i + 1; j < points.length; j++) {
      const [x1, y1] = points[i];
      const [x2, y2] = points[j];
      
      // Handle duplicate points
      if (x1 === x2 && y1 === y2) {
        same++;
      } else {
        // Calculate slope and normalize using GCD
        const dx = x2 - x1;
        const dy = y2 - y1;
        const g = gcd(Math.abs(dx), Math.abs(dy));
        const key = `${dx / g},${dy / g}`;
        slopes.set(key, (slopes.get(key) || 0) + 1);
      }
    }
    
    // Find max points on same line
    let currentMax = same;
    for (const count of slopes.values()) {
      currentMax = Math.max(currentMax, same + count);
    }
    max = Math.max(max, currentMax);
  }
  
  return max;
}

function gcd(a, b) {
  while (b !== 0) {
    [a, b] = [b, a % b];
  }
  return a;
}

// Test Cases:
// Input: points = [[1,1],[2,2],[3,3]]
// Output: 3

// Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
// Output: 4
```

**Time Complexity:** O(n²) - For each point, check all other points  
**Space Complexity:** O(n) - Slope map per point

**Deep Insights:**
- **Optimal Approach:** Slope normalization achieves O(n²) time—optimal for max points on line
- **Slope Normalization:** Use GCD to normalize slopes—reduces fractions to simplest form
- **Duplicate Points:** Handle duplicate points separately—count them for all lines
- **Key Insight:** Normalize slopes using GCD—ensures same slope representation
- **Map Storage:** Use map to count points with same slope—efficient grouping
- **Edge Cases:** ≤2 points returns length; all points same returns length; handles all cases
- **Interview Tip:** Explain slope normalization clearly; emphasize GCD usage; mention duplicate point handling

