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


