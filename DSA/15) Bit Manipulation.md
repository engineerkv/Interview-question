# Bit Manipulation

## Q166. Add Binary

Concept: Add binary strings from right to left with carry; use bit manipulation or string addition.

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

// Test Cases:
//
// Example 1:
//   Input: a = "11", b = "1"
//   Output: "100"
//   Explanation: 11 + 1 = 100 in binary
//
// Example 2:
//   Input: a = "1010", b = "1011"
//   Output: "10101"
//   Explanation: 10 + 11 = 21 in binary (10101)
//
// Example 3:
//   Input: a = "0", b = "0"
//   Output: "0"
```

Deep Insights:
  - Rule: Add from right to left with carry; sum%2 for result, sum/2 for carry; O(max(m,n)) time.
  - Real-world: Binary addition, arithmetic operations, carry propagation.
  - Common mistake: Wrong carry handling; not handling different lengths; forgetting final carry.
  - Optimization: O(max(m,n)) time optimal; carry propagation crucial; handle different string lengths.
  - Interview tip: Explain carry propagation clearly; mention string handling; ask about optimization.

Time Complexity: O(max(m,n)) - Traverse both strings
Space Complexity: O(max(m,n)) - Result string

## Q167. Reverse Bits

Concept: Reverse bits of 32-bit unsigned integer; extract bits from right and build result from left.

```javascript
function reverseBits(n) {
  let result = 0;
  let count = 32;

  while (count > 0) {
    result = (result << 1) | (n & 1);
    n = n >>> 1;
    count--;
  }

  return result >>> 0; // Convert to unsigned 32-bit
}

// Test Cases:
//
// Example 1:
//   Input: n = 0b00000010100101000001111010011100
//   Output: 964176192 (0b00111001011110000010100101000000)
//   Explanation: Reverse of 43261596
//
// Example 2:
//   Input: n = 0b11111111111111111111111111111101
//   Output: 3221225471 (0b10111111111111111111111111111111)
```

Deep Insights:
  - Rule: Extract bits from right (n&1), shift result left (result<<1), OR with extracted bit; O(32) time.
  - Real-world: Bit reversal, network protocols, binary manipulation.
  - Common mistake: Wrong bit extraction; not handling unsigned conversion; wrong shift operations.
  - Optimization: O(32) time optimal; bit extraction and shifting; unsigned 32-bit conversion.
  - Interview tip: Explain bit operations clearly; mention unsigned conversion; ask about optimization.

Time Complexity: O(32) - Fixed 32-bit integer
Space Complexity: O(1) - Constant extra space

## Q168. Number of 1 Bits

Concept: Count set bits in number using n&(n-1) trick (removes rightmost set bit) or shifting.

```javascript
function hammingWeight(n) {
  let count = 0;
  
  while (n !== 0) {
    n = n & (n - 1); // Remove rightmost set bit
    count++;
  }
  
  return count;
}

// Alternative: Shifting approach
// function hammingWeight(n) {
//   let count = 0;
//   while (n !== 0) {
//     if (n & 1) count++;
//     n = n >>> 1;
//   }
//   return count;
// }

// Test Cases:
//
// Example 1:
//   Input: n = 11 (0b00000000000000000000000000001011)
//   Output: 3
//   Explanation: 11 has 3 set bits
//
// Example 2:
//   Input: n = 128 (0b00000000000000000000000010000000)
//   Output: 1
//
// Example 3:
//   Input: n = 4294967293 (0b11111111111111111111111111111101)
//   Output: 31
```

Deep Insights:
  - Rule: Use n&(n-1) to remove rightmost set bit; count iterations; O(k) time where k is number of set bits.
  - Real-world: Bit counting, population count, parity checking.
  - Common mistake: Wrong bit manipulation; not handling negative numbers; wrong unsigned conversion.
  - Optimization: O(k) time where k is set bits (faster than O(32)); n&(n-1) removes rightmost set bit.
  - Interview tip: Explain n&(n-1) trick clearly; mention time complexity; ask about optimization.

Time Complexity: O(k) - k is number of set bits
Space Complexity: O(1) - Constant extra space

## Q169. Single Number

Concept: Find single non-duplicate number in array using XOR; XOR all numbers, duplicates cancel out.

```javascript
function singleNumber(nums) {
  let result = 0;
  for (const num of nums) {
    result ^= num;
  }
  return result;
}

// Test Cases:
//
// Example 1:
//   Input: nums = [2,2,1]
//   Output: 1
//
// Example 2:
//   Input: nums = [4,1,2,1,2]
//   Output: 4
//
// Example 3:
//   Input: nums = [1]
//   Output: 1
```

Deep Insights:
  - Rule: XOR all numbers; duplicates cancel out (a^a=0); single number remains; O(n) time, O(1) space.
  - Real-world: Finding unique elements, duplicate detection, XOR properties.
  - Common mistake: Not understanding XOR properties; wrong implementation; edge cases.
  - Optimization: O(n) time, O(1) space optimal; XOR properties: a^a=0, a^0=a.
  - Interview tip: Explain XOR properties clearly; mention duplicate cancellation; ask about variants.

Time Complexity: O(n) - Single pass through array
Space Complexity: O(1) - Constant extra space

## Q170. Single Number II

Concept: Count set bits at each position modulo 3; single number's bits appear once; reconstruct from counts.

```javascript
function singleNumber(nums) {
  let result = 0;
  
  for (let i = 0; i < 32; i++) {
    let count = 0;
    const bit = 1 << i;
    
    for (const num of nums) {
      if (num & bit) {
        count++;
      }
    }
    
    if (count % 3 !== 0) {
      result |= bit;
    }
  }
  
  return result >>> 0; // Convert to signed 32-bit
}

// Test Cases:
//
// Example 1:
//   Input: nums = [2,2,3,2]
//   Output: 3
//
// Example 2:
//   Input: nums = [0,1,0,1,0,1,99]
//   Output: 99
```

Deep Insights:
  - Rule: Count set bits at each position modulo 3; single number's bits appear once; O(32n) time.
  - Real-world: Finding unique elements with duplicates, bit counting, modular arithmetic.
  - Common mistake: Wrong bit counting; not handling negative numbers; wrong modulo logic.
  - Optimization: O(32n) time, O(1) space; count bits modulo 3; reconstruct number from counts.
  - Interview tip: Explain bit counting strategy clearly; mention modulo 3; ask about optimization.

Time Complexity: O(32n) - 32 bits × n numbers
Space Complexity: O(1) - Constant extra space

## Q171. Bitwise AND of Numbers Range

Concept: Find AND of all numbers in range [m,n]; result is common prefix of m and n in binary.

```javascript
function rangeBitwiseAnd(m, n) {
  let shift = 0;
  
  while (m < n) {
    m = m >> 1;
    n = n >> 1;
    shift++;
  }
  
  return m << shift;
}

// Alternative: Remove rightmost different bits
// function rangeBitwiseAND(m, n) {
//   while (m < n) {
//     n = n & (n - 1); // Remove rightmost set bit
//   }
//   return m & n;
// }

// Test Cases:
//
// Example 1:
//   Input: left = 5, right = 7
//   Output: 4
//   Explanation: 5 AND 6 AND 7 = 4
//
// Example 2:
//   Input: left = 0, right = 0
//   Output: 0
//
// Example 3:
//   Input: left = 1, right = 2147483647
//   Output: 0
```

Deep Insights:
  - Rule: Find common prefix of m and n; shift right until equal, then shift left; O(log n) time.
  - Real-world: Range queries, bit manipulation, AND operations.
  - Common mistake: Wrong shift logic; not handling edge cases; wrong AND calculation.
  - Optimization: O(log n) time optimal; find common prefix by shifting; result is common prefix.
  - Interview tip: Explain common prefix strategy clearly; mention shifting approach; ask about optimization.

Time Complexity: O(log n) - Shifting until m equals n
Space Complexity: O(1) - Constant extra space

