# Bit Manipulation

---

## 📍 Navigation

<div align="center">

[← Previous: Binary Search](14%29%20Binary%20Search.md) • [Home: README](README.md) • [Next: Math →](16%29%20Math.md)

[📋 Cheatsheet](DSA%20Interview%20Cheatsheet.md)

</div>

---

## Q218. ➕ Add Binary

**Problem:** Given two binary strings `a` and `b`, return their sum as a binary string.

**Approach:** Add from right to left with carry propagation. Sum = a[i] + b[j] + carry. Result digit = sum % 2, carry = sum / 2.

### Solution 1: String Addition with Carry (Optimal)

```javascript
function addBinary(a, b) {
  let result = '';
  let carry = 0;
  let i = a.length - 1, j = b.length - 1;

  while (i >= 0 || j >= 0 || carry > 0) {
    const sum = (i >= 0 ? parseInt(a[i]) : 0) +
                (j >= 0 ? parseInt(b[j]) : 0) +
                carry;
    result = (sum % 2) + result;
    carry = Math.floor(sum / 2);
    i--;
    j--;
  }

  return result;
}

```

// Test Cases:
// Input: a = "11", b = "1"
// Output: "100"
// Explanation: 11 + 1 = 100 in binary

// Input: a = "1010", b = "1011"
// Output: "10101"
// Explanation: 10 + 11 = 21 in binary (10101)

// Input: a = "0", b = "0"
// Output: "0"

```

**Time Complexity:** O(max(m,n)) - Traverse both strings
**Space Complexity:** O(max(m,n)) - Result string

## Q219. 🔢 Reverse Bits

**Problem:** Reverse bits of a given 32 bits unsigned integer. Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as signed integers. They should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned. In Java, the compiler represents the signed integers using 2's complement notation.

**Approach:** Extract bits from right (n & 1), shift result left (result << 1), OR with extracted bit. Repeat for 32 bits.

### Solution 1: Bit Extraction and Shifting (Optimal)

```javascript

function reverseBits(n) {
  let result = 0;
  let count = 32;

  while (count > 0) {
    // Extract rightmost bit and shift result left
    result = (result << 1) | (n & 1);
    // Shift n right (unsigned)
    n = n >>> 1;
    count--;
  }

  // Convert to unsigned 32-bit
  return result >>> 0;
}

```

// Test Cases:
// Input: n = 0b00000010100101000001111010011100
// Output: 964176192 (0b00111001011110000010100101000000)
// Explanation: Reverse of 43261596

// Input: n = 0b11111111111111111111111111111101
// Output: 3221225471 (0b10111111111111111111111111111111)

```

**Time Complexity:** O(32) - Fixed 32-bit integer
**Space Complexity:** O(1) - Constant extra space

## Q220. 🔢 Number of 1 Bits

**Problem:** Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

**Approach:** Use n & (n-1) trick to remove rightmost set bit. Count iterations until n becomes 0.

### Solution 1: n & (n-1) Trick (Optimal)

```javascript
function hammingWeight(n) {
  let count = 0;

  while (n !== 0) {
    n = n & (n - 1); // Remove rightmost set bit
    count++;
  }

  return count;
}

```

### Solution 2: Shifting Approach

```javascript
function hammingWeight(n) {
  let count = 0;
  while (n !== 0) {
    if (n & 1) count++;  // Check if rightmost bit is set
    n = n >>> 1;         // Shift right (unsigned)
  }
  return count;
}

```

// Test Cases:
// Input: n = 11 (0b00000000000000000000000000001011)
// Output: 3
// Explanation: 11 has 3 set bits

// Input: n = 128 (0b00000000000000000000000010000000)
// Output: 1

// Input: n = 4294967293 (0b11111111111111111111111111111101)
// Output: 31

```

**Time Complexity:** O(k) - k is number of set bits (optimal), O(32) for shifting
**Space Complexity:** O(1) - Constant extra space

## Q221. 💡 Single Number

**Problem:** Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one. You must implement a solution with a linear runtime complexity and use only constant extra space.

**Approach:** Use XOR property. XOR all numbers. Duplicates cancel out (a^a=0), single number remains.

### Solution 1: XOR (Optimal)

```javascript

function singleNumber(nums) {
  let result = 0;
  for (const num of nums) {
    result ^= num;  // XOR all numbers
  }
  return result;
}

```

// Test Cases:
// Input: nums = [2,2,1]
// Output: 1

// Input: nums = [4,1,2,1,2]
// Output: 4

// Input: nums = [1]
// Output: 1

```

**Time Complexity:** O(n) - Single pass through array
**Space Complexity:** O(1) - Constant extra space

## Q222. 💡 Single Number II

**Problem:** Given an integer array `nums` where every element appears three times except for one, which appears exactly once. Find the single element and return it. You must implement a solution with a linear runtime complexity and use only constant extra space.

**Approach:** Count set bits at each position modulo 3. The single number's bits appear once (not multiple of 3). Reconstruct number from bit counts.

### Solution 1: Bit Counting (Optimal)

```javascript
function singleNumber(nums) {
  let result = 0;

  // Check each bit position
  for (let i = 0; i < 32; i++) {
    let count = 0;
    const bit = 1 << i;  // Bit mask for position i

    // Count set bits at position i
    for (const num of nums) {
      if (num & bit) {
        count++;
      }
    }

    // If count not multiple of 3, bit is set in result
    if (count % 3 !== 0) {
      result |= bit;
    }
  }

  // Convert to unsigned 32-bit
  return result >>> 0;
}

```

// Test Cases:
// Input: nums = [2,2,3,2]
// Output: 3

// Input: nums = [0,1,0,1,0,1,99]
// Output: 99

```

**Time Complexity:** O(32n) - 32 bits × n numbers
**Space Complexity:** O(1) - Constant extra space

## Q223. 🔢 Bitwise AND of Numbers Range

**Problem:** Given two integers `left` and `right` that represent the range `[left, right]`, return the bitwise AND of all numbers in this range, inclusive.

**Approach:** Find common prefix of left and right in binary. Shift right until equal, then shift left by same amount.

### Solution 1: Common Prefix (Optimal)

```javascript

function rangeBitwiseAnd(m, n) {
  let shift = 0;

  // Find common prefix by shifting right
  while (m < n) {
    m = m >> 1;
    n = n >> 1;
    shift++;
  }

  // Shift left to restore common prefix
  return m << shift;
}

// Alternative: Remove rightmost different bits
// function rangeBitwiseAND(m, n) {
// while (m < n) {
// n = n & (n - 1); // Remove rightmost set bit
// }
// return m & n;
// }

// Test Cases:
// Input: left = 5, right = 7
// Output: 4
// Explanation: 5 AND 6 AND 7 = 4

// Input: left = 0, right = 0
// Output: 0

// Input: left = 1, right = 2147483647
// Output: 0

```

**Time Complexity:** O(log n) - Shifting until m equals n
**Space Complexity:** O(1) - Constant extra space

---

## Bonus: Bit Manipulation Fundamentals

**Concept:** Use bitwise ops to encode sets, parity, and arithmetic tricks efficiently.

```javascript

// Single number where every other element appears twice
function singleNumber(arr) {
  let x = 0;
  for (const v of arr) {
    x ^= v;
  }
  return x;
}

// Test Cases:
// Input: arr = [2, 2, 1]
// Output: 1

// Input: arr = [4, 1, 2, 1, 2]
// Output: 4

// Input: arr = [1]
// Output: 1

// Input: arr = [1, 3, 1, 3, 5]
// Output: 5

// Input: arr = [-1, -2, -1, -2, 3]
// Output: 3

```

**Time Complexity:** O(n) - Single pass through array
**Space Complexity:** O(1) - Only using constant extra variables

---

## 📍 Navigation

<div align="center">

[← Previous: Binary Search](14%29%20Binary%20Search.md) • [Home: README](README.md) • [Next: Math →](16%29%20Math.md)

[📋 Cheatsheet](DSA%20Interview%20Cheatsheet.md)

</div>
