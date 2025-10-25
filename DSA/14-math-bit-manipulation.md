# 🧩 DSA Interview Notes - LeetCode Top 150

## 💡 Section 14 — Math / Bit Manipulation — Q135-Q146

---

### 135. 💡 Palindrome Number

**🧠 Concept**

Check if integer is palindrome by reversing half of the number and comparing with other half.

**💻 Example**

```javascript
function isPalindrome(x) {
  if (x < 0 || (x % 10 === 0 && x !== 0)) return false;
  
  let reversed = 0;
  while (x > reversed) {
    reversed = reversed * 10 + x % 10;
    x = Math.floor(x / 10);
  }
  
  return x === reversed || x === Math.floor(reversed / 10);
}
```

**💬 Explanation + Insight**

- **Half Reversal** - Reverse only half of the number
- **Edge Cases** - Handle negative numbers and multiples of 10
- **Odd Length** - Handle middle digit for odd-length numbers
- **Time Complexity** - O(log n) where n is the number
- **Space Complexity** - O(1) constant space

---

### 136. 💡 Plus One

**🧠 Concept**

Add one to number represented as array of digits, handling carry propagation.

**💻 Example**

```javascript
function plusOne(digits) {
  for (let i = digits.length - 1; i >= 0; i--) {
    if (digits[i] < 9) {
      digits[i]++;
      return digits;
    }
    digits[i] = 0;
  }
  
  return [1, ...digits];
}
```

**💬 Explanation + Insight**

- **Carry Handling** - Set digit to 0 and continue if digit is 9
- **Early Return** - Return immediately when no carry needed
- **All Nines** - Add 1 at beginning if all digits were 9
- **Time Complexity** - O(n) worst case, O(1) best case
- **Space Complexity** - O(1) in-place modification

---

### 137. 💡 Add Binary

**🧠 Concept**

Add two binary strings by simulating binary addition with carry handling.

**💻 Example**

```javascript
function addBinary(a, b) {
  let result = '';
  let carry = 0;
  let i = a.length - 1;
  let j = b.length - 1;
  
  while (i >= 0 || j >= 0 || carry) {
    const digitA = i >= 0 ? parseInt(a[i]) : 0;
    const digitB = j >= 0 ? parseInt(b[j]) : 0;
    
    const sum = digitA + digitB + carry;
    result = (sum % 2) + result;
    carry = Math.floor(sum / 2);
    
    i--;
    j--;
  }
  
  return result;
}
```

**💬 Explanation + Insight**

- **Right to Left** - Process digits from right to left
- **Carry Propagation** - Handle carry from previous addition
- **Padding** - Handle strings of different lengths
- **Time Complexity** - O(max(m,n)) where m,n are string lengths
- **Space Complexity** - O(max(m,n)) for result string

---

### 138. 💡 Sqrt(x)

**🧠 Concept**

Find square root of integer using binary search to find largest integer whose square ≤ x.

**💻 Example**

```javascript
function mySqrt(x) {
  if (x < 2) return x;
  
  let left = 2;
  let right = Math.floor(x / 2);
  
  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    const square = mid * mid;
    
    if (square === x) return mid;
    if (square < x) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  
  return right;
}
```

**💬 Explanation + Insight**

- **Binary Search** - Search for largest valid square root
- **Range Optimization** - Search in [2, x/2] range
- **Integer Result** - Return largest integer square root
- **Time Complexity** - O(log x) binary search
- **Space Complexity** - O(1) constant space

---

### 139. 💡 Pow(x, n)

**🧠 Concept**

Calculate x raised to power n using binary exponentiation with recursive approach.

**💻 Example**

```javascript
function myPow(x, n) {
  if (n === 0) return 1;
  if (n < 0) {
    x = 1 / x;
    n = -n;
  }
  
  function power(x, n) {
    if (n === 0) return 1;
    if (n === 1) return x;
    
    const half = power(x, Math.floor(n / 2));
    if (n % 2 === 0) {
      return half * half;
    } else {
      return half * half * x;
    }
  }
  
  return power(x, n);
}
```

**💬 Explanation + Insight**

- **Binary Exponentiation** - Use divide and conquer approach
- **Negative Power** - Handle negative exponents
- **Even/Odd Cases** - Different handling for even and odd powers
- **Time Complexity** - O(log n) binary exponentiation
- **Space Complexity** - O(log n) recursion stack

---

### 140. 💡 Factorial Trailing Zeroes

**🧠 Concept**

Count trailing zeroes in factorial by counting factors of 5 (since 2s are more abundant).

**💻 Example**

```javascript
function trailingZeroes(n) {
  let count = 0;
  
  while (n > 0) {
    n = Math.floor(n / 5);
    count += n;
  }
  
  return count;
}
```

**💬 Explanation + Insight**

- **Factor of 5** - Count multiples of 5, 25, 125, etc.
- **Mathematical Insight** - Trailing zeroes = min(count of 2s, count of 5s)
- **Efficient Counting** - Count 5s by dividing by 5 repeatedly
- **Time Complexity** - O(log n) base 5
- **Space Complexity** - O(1) constant space

---

### 141. 💡 Max Points on a Line

**🧠 Concept**

Find maximum number of points on a straight line using slope calculation and hash map.

**💻 Example**

```javascript
function maxPoints(points) {
  if (points.length < 3) return points.length;
  
  let maxPoints = 0;
  
  for (let i = 0; i < points.length; i++) {
    const slopes = new Map();
    let duplicates = 0;
    let max = 0;
    
    for (let j = i + 1; j < points.length; j++) {
      const dx = points[j][0] - points[i][0];
      const dy = points[j][1] - points[i][1];
      
      if (dx === 0 && dy === 0) {
        duplicates++;
        continue;
      }
      
      const gcd = getGCD(dx, dy);
      const slope = `${dx / gcd}/${dy / gcd}`;
      slopes.set(slope, (slopes.get(slope) || 0) + 1);
      max = Math.max(max, slopes.get(slope));
    }
    
    maxPoints = Math.max(maxPoints, max + duplicates + 1);
  }
  
  return maxPoints;
}

function getGCD(a, b) {
  return b === 0 ? a : getGCD(b, a % b);
}
```

**💬 Explanation + Insight**

- **Slope Calculation** - Use reduced fractions to represent slopes
- **GCD Normalization** - Reduce slope to simplest form
- **Duplicate Handling** - Count duplicate points separately
- **Time Complexity** - O(n²) for each pair of points
- **Space Complexity** - O(n) for slope map

---

### 142. 💡 Single Number

**🧠 Concept**

Find single number that appears once while others appear twice using XOR operation.

**💻 Example**

```javascript
function singleNumber(nums) {
  let result = 0;
  for (const num of nums) {
    result ^= num;
  }
  return result;
}
```

**💬 Explanation + Insight**

- **XOR Property** - XOR of same numbers equals 0
- **Commutative Property** - Order of XOR operations doesn't matter
- **Single Pass** - Find result in one iteration
- **Time Complexity** - O(n) single pass through array
- **Space Complexity** - O(1) constant space

---

### 143. 💡 Single Number II

**🧠 Concept**

Find single number that appears once while others appear three times using bit manipulation.

**💻 Example**

```javascript
function singleNumber(nums) {
  let ones = 0, twos = 0;
  
  for (const num of nums) {
    ones = (ones ^ num) & ~twos;
    twos = (twos ^ num) & ~ones;
  }
  
  return ones;
}
```

**💬 Explanation + Insight**

- **State Machine** - Track count of 1s in each bit position
- **Three States** - 0, 1, 2 occurrences (3 becomes 0)
- **Bit Manipulation** - Use XOR and AND operations
- **Time Complexity** - O(n) single pass through array
- **Space Complexity** - O(1) constant space

---

### 144. 💡 Reverse Bits

**🧠 Concept**

Reverse bits of 32-bit unsigned integer using bit manipulation and shifting.

**💻 Example**

```javascript
function reverseBits(n) {
  let result = 0;
  
  for (let i = 0; i < 32; i++) {
    result = (result << 1) | (n & 1);
    n >>= 1;
  }
  
  return result;
}
```

**💬 Explanation + Insight**

- **Bit Extraction** - Extract least significant bit
- **Bit Shifting** - Shift result left and number right
- **32 Iterations** - Process all 32 bits
- **Time Complexity** - O(1) constant time (32 iterations)
- **Space Complexity** - O(1) constant space

---

### 145. 💡 Number of 1 Bits

**🧠 Concept**

Count number of 1 bits in binary representation using bit manipulation techniques.

**💻 Example**

```javascript
function hammingWeight(n) {
  let count = 0;
  
  while (n !== 0) {
    count++;
    n = n & (n - 1);
  }
  
  return count;
}
```

**💬 Explanation + Insight**

- **Brian Kernighan's Algorithm** - Remove rightmost 1 bit
- **n & (n-1)** - Clears rightmost set bit
- **Efficient Counting** - Only count actual 1 bits
- **Time Complexity** - O(k) where k is number of 1 bits
- **Space Complexity** - O(1) constant space

---

### 146. 💡 Bitwise AND of Numbers Range

**🧠 Concept**

Find bitwise AND of all numbers in range by finding common prefix of binary representations.

**💻 Example**

```javascript
function rangeBitwiseAnd(left, right) {
  let shift = 0;
  
  while (left < right) {
    left >>= 1;
    right >>= 1;
    shift++;
  }
  
  return left << shift;
}
```

**💬 Explanation + Insight**

- **Common Prefix** - Find common prefix of left and right
- **Right Shift** - Remove different bits from right
- **Left Shift** - Restore common prefix
- **Time Complexity** - O(log n) where n is the range
- **Space Complexity** - O(1) constant space

---

*This comprehensive math and bit manipulation section covers essential numerical algorithms including arithmetic operations, bitwise techniques, and mathematical optimizations for efficient computation.*