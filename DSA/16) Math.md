# Math

## Q172. Palindrome Number

Concept: Check if integer is palindrome by reversing half and comparing with remaining half.

```javascript
function isPalindrome(x) {
  if (x < 0 || (x !== 0 && x % 10 === 0)) return false;
  
  let reversed = 0;
  let original = x;
  
  while (x > reversed) {
    reversed = reversed * 10 + x % 10;
    x = Math.floor(x / 10);
  }
  
  return x === reversed || x === Math.floor(reversed / 10);
}

// Test Cases:
//
// Example 1:
//   Input: x = 121
//   Output: true
//   Explanation: Reads 121 from left to right and from right to left
//
// Example 2:
//   Input: x = -121
//   Output: false
//   Explanation: From left to right, it reads -121. From right to left, it becomes 121-
//
// Example 3:
//   Input: x = 10
//   Output: false
//   Explanation: Reads 01 from right to left
//
// Example 4:
//   Input: x = -101
//   Output: false
```

Deep Insights:
  - Rule: Reverse half of number and compare; stop when reversed >= original; O(log n) time.
  - Real-world: Palindrome checking, number validation, string comparison.
  - Common mistake: Not handling negative numbers; not handling multiples of 10; wrong comparison.
  - Optimization: O(log n) time, O(1) space; reverse half only; compare with original half.
  - Interview tip: Explain half-reversal strategy clearly; mention edge cases; ask about optimization.

Time Complexity: O(log n) - Number of digits
Space Complexity: O(1) - Constant extra space

## Q173. Plus One

Concept: Add one to number represented as array of digits; handle carry from right to left.

```javascript
function plusOne(digits) {
  for (let i = digits.length - 1; i >= 0; i--) {
    if (digits[i] < 9) {
      digits[i]++;
      return digits;
    }
    digits[i] = 0;
  }
  
  // All 9s, need to add new digit at front
  digits.unshift(1);
  return digits;
}

// Test Cases:
//
// Example 1:
//   Input: digits = [1,2,3]
//   Output: [1,2,4]
//   Explanation: 123 + 1 = 124
//
// Example 2:
//   Input: digits = [4,3,2,1]
//   Output: [4,3,2,2]
//   Explanation: 4321 + 1 = 4322
//
// Example 3:
//   Input: digits = [9]
//   Output: [1,0]
//   Explanation: 9 + 1 = 10
//
// Example 4:
//   Input: digits = [9,9,9]
//   Output: [1,0,0,0]
//   Explanation: 999 + 1 = 1000
```

Deep Insights:
  - Rule: Add one from right to left; handle carry; if all 9s, add new digit at front; O(n) time.
  - Real-world: Arithmetic operations, big number addition, carry propagation.
  - Common mistake: Wrong carry handling; not handling all 9s case; wrong digit manipulation.
  - Optimization: O(n) time, O(1) space (excluding result); handle carry from right; unshift if all 9s.
  - Interview tip: Explain carry propagation clearly; mention all 9s case; ask about optimization.

Time Complexity: O(n) - Worst case traverse all digits
Space Complexity: O(1) - Excluding result array

## Q174. Factorial Trailing Zeroes

Concept: Count trailing zeroes in n! by counting factors of 5; each 5 contributes a zero (with 2).

```javascript
function trailingZeroes(n) {
  let count = 0;
  
  while (n >= 5) {
    count += Math.floor(n / 5);
    n = Math.floor(n / 5);
  }
  
  return count;
}

// Test Cases:
//
// Example 1:
//   Input: n = 3
//   Output: 0
//   Explanation: 3! = 6, no trailing zero
//
// Example 2:
//   Input: n = 5
//   Output: 1
//   Explanation: 5! = 120, one trailing zero
//
// Example 3:
//   Input: n = 0
//   Output: 0
//
// Example 4:
//   Input: n = 25
//   Output: 6
//   Explanation: 25! has 6 trailing zeroes (5, 10, 15, 20, 25 contribute; 25 contributes 2)
```

Deep Insights:
  - Rule: Count factors of 5 in n!; each 5 contributes a zero (paired with 2); O(log n) time.
  - Real-world: Factorial calculations, combinatorics, mathematical analysis.
  - Common mistake: Wrong factor counting; not handling powers of 5; wrong calculation.
  - Optimization: O(log n) time, O(1) space; count 5s repeatedly; powers of 5 contribute multiple zeroes.
  - Interview tip: Explain factor 5 counting clearly; mention pairing with 2s; ask about optimization.

Time Complexity: O(log n) - Base 5 logarithm
Space Complexity: O(1) - Constant extra space

## Q175. Sqrt(x)

Concept: Find integer square root using binary search; find largest number whose square <= x.

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
  
  return right;
}

// Test Cases:
//
// Example 1:
//   Input: x = 4
//   Output: 2
//
// Example 2:
//   Input: x = 8
//   Output: 2
//   Explanation: Square root of 8 is 2.82842..., and since 2^2 < 8 < 3^2, return 2
//
// Example 3:
//   Input: x = 0
//   Output: 0
//
// Example 4:
//   Input: x = 1
//   Output: 1
```

Deep Insights:
  - Rule: Binary search for largest number whose square <= x; O(log x) time.
  - Real-world: Square root calculation, mathematical functions, approximation.
  - Common mistake: Wrong binary search bounds; not handling edge cases; wrong return value.
  - Optimization: O(log x) time optimal; binary search on range [2, x/2]; return right when not found.
  - Interview tip: Explain binary search strategy clearly; mention bounds; ask about precision.

Time Complexity: O(log x) - Binary search
Space Complexity: O(1) - Constant extra space

## Q176. Pow(x, n)

Concept: Compute x^n using binary exponentiation; if n is even, x^n = (x^(n/2))^2; else x^n = x * (x^((n-1)/2))^2.

```javascript
function myPow(x, n) {
  if (n === 0) return 1;
  if (n < 0) {
    x = 1 / x;
    n = -n;
  }
  
  let result = 1;
  
  while (n > 0) {
    if (n % 2 === 1) {
      result *= x;
    }
    x *= x;
    n = Math.floor(n / 2);
  }
  
  return result;
}

// Test Cases:
//
// Example 1:
//   Input: x = 2.00000, n = 10
//   Output: 1024.00000
//
// Example 2:
//   Input: x = 2.10000, n = 3
//   Output: 9.26100
//
// Example 3:
//   Input: x = 2.00000, n = -2
//   Output: 0.25000
//   Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
```

Deep Insights:
  - Rule: Binary exponentiation; if n odd, multiply result; square x; halve n; O(log n) time.
  - Real-world: Exponentiation, mathematical computations, power calculations.
  - Common mistake: Wrong exponentiation logic; not handling negative exponents; wrong iteration.
  - Optimization: O(log n) time optimal; binary exponentiation; handle negative n by inverting x.
  - Interview tip: Explain binary exponentiation clearly; mention negative exponents; ask about optimization.

Time Complexity: O(log n) - Binary exponentiation
Space Complexity: O(1) - Constant extra space

## Q177. Max Points on a Line

Concept: Count points on same line using slope; track (dx,dy) pairs; reduce fractions using GCD.

```javascript
function maxPoints(points) {
  if (points.length <= 2) return points.length;
  
  let max = 2;
  
  for (let i = 0; i < points.length; i++) {
    const slopes = new Map();
    let same = 1;
    
    for (let j = i + 1; j < points.length; j++) {
      const [x1, y1] = points[i];
      const [x2, y2] = points[j];
      
      if (x1 === x2 && y1 === y2) {
        same++;
      } else {
        const dx = x2 - x1;
        const dy = y2 - y1;
        const g = gcd(Math.abs(dx), Math.abs(dy));
        const key = `${dx / g},${dy / g}`;
        slopes.set(key, (slopes.get(key) || 0) + 1);
      }
    }
    
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
//
// Example 1:
//   Input: points = [[1,1],[2,2],[3,3]]
//   Output: 3
//
// Example 2:
//   Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
//   Output: 4
```

Deep Insights:
  - Rule: Count points on same line using normalized slopes; use GCD to reduce fractions; O(n²) time.
  - Real-world: Geometry problems, line detection, point clustering.
  - Common mistake: Wrong slope calculation; not handling duplicate points; not normalizing slopes.
  - Optimization: O(n²) time, O(n) space; normalize slopes with GCD; handle duplicate points separately.
  - Interview tip: Explain slope normalization clearly; mention GCD; ask about edge cases.

Time Complexity: O(n²) - For each point, check all other points
Space Complexity: O(n) - Slope map per point

