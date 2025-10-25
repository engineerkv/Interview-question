# 🧩 DSA Interview Notes - LeetCode Top 150

## 🟩 Section 4 — Greedy — Q36-Q42

---

### 36. 🟩 Best Time to Buy and Sell Stock II

**🧠 Concept**

Maximize profit by buying and selling multiple times, buying before every price increase.

**💻 Example**

```javascript
function maxProfit(prices) {
  let profit = 0;
  
  for (let i = 1; i < prices.length; i++) {
    if (prices[i] > prices[i - 1]) {
      profit += prices[i] - prices[i - 1];
    }
  }
  
  return profit;
}
```

**💬 Explanation + Insight**

- **Greedy Strategy** - Buy before every price increase
- **Local Optimum** - Take profit at every opportunity
- **No Transaction Cost** - Assume no fees for buying/selling
- **Time Complexity** - O(n) single pass through prices
- **Space Complexity** - O(1) constant space

---

### 37. 🟩 Gas Station

**🧠 Concept**

Find starting gas station to complete circular route by tracking gas surplus and deficit.

**💻 Example**

```javascript
function canCompleteCircuit(gas, cost) {
  let totalTank = 0;
  let currentTank = 0;
  let startStation = 0;
  
  for (let i = 0; i < gas.length; i++) {
    totalTank += gas[i] - cost[i];
    currentTank += gas[i] - cost[i];
    
    if (currentTank < 0) {
      startStation = i + 1;
      currentTank = 0;
    }
  }
  
  return totalTank >= 0 ? startStation : -1;
}
```

**💬 Explanation + Insight**

- **Gas Surplus** - Track total gas available vs needed
- **Current Tank** - Track gas in current journey
- **Restart Strategy** - Restart from next station if tank goes negative
- **Time Complexity** - O(n) single pass through stations
- **Space Complexity** - O(1) constant space

---

### 38. 🟩 Candy

**🧠 Concept**

Distribute minimum candies satisfying rating constraints using two passes for left and right neighbors.

**💻 Example**

```javascript
function candy(ratings) {
  const n = ratings.length;
  const candies = new Array(n).fill(1);
  
  // Left to right pass
  for (let i = 1; i < n; i++) {
    if (ratings[i] > ratings[i - 1]) {
      candies[i] = candies[i - 1] + 1;
    }
  }
  
  // Right to left pass
  for (let i = n - 2; i >= 0; i--) {
    if (ratings[i] > ratings[i + 1]) {
      candies[i] = Math.max(candies[i], candies[i + 1] + 1);
    }
  }
  
  return candies.reduce((sum, candy) => sum + candy, 0);
}
```

**💬 Explanation + Insight**

- **Two Passes** - Left to right, then right to left
- **Constraint Satisfaction** - Satisfy both left and right neighbors
- **Minimum Candies** - Use Math.max to maintain constraints
- **Time Complexity** - O(n) two passes through array
- **Space Complexity** - O(n) for candies array

---

### 39. 🟩 Jump Game

**🧠 Concept**

Check if can reach last index by tracking maximum reachable position from current position.

**💻 Example**

```javascript
function canJump(nums) {
  let maxReach = 0;
  
  for (let i = 0; i < nums.length; i++) {
    if (i > maxReach) {
      return false;
    }
    maxReach = Math.max(maxReach, i + nums[i]);
  }
  
  return true;
}
```

**💬 Explanation + Insight**

- **Maximum Reach** - Track furthest position reachable
- **Early Termination** - Return false if current position unreachable
- **Greedy Update** - Update max reach at each position
- **Time Complexity** - O(n) single pass through array
- **Space Complexity** - O(1) constant space

---

### 40. 🟩 Jump Game II

**🧠 Concept**

Find minimum jumps to reach last index using greedy approach with current and next jump boundaries.

**💻 Example**

```javascript
function jump(nums) {
  let jumps = 0;
  let currentEnd = 0;
  let farthest = 0;
  
  for (let i = 0; i < nums.length - 1; i++) {
    farthest = Math.max(farthest, i + nums[i]);
    
    if (i === currentEnd) {
      jumps++;
      currentEnd = farthest;
    }
  }
  
  return jumps;
}
```

**💬 Explanation + Insight**

- **Jump Boundaries** - Track current and next jump limits
- **Greedy Choice** - Take maximum reach at each jump
- **Minimum Jumps** - Count jumps only when boundary reached
- **Time Complexity** - O(n) single pass through array
- **Space Complexity** - O(1) constant space

---

### 41. 🟩 Minimum Number of Arrows to Burst Balloons

**🧠 Concept**

Find minimum arrows to burst all balloons by sorting by end position and using greedy selection.

**💻 Example**

```javascript
function findMinArrowShots(points) {
  if (points.length === 0) return 0;
  
  points.sort((a, b) => a[1] - b[1]);
  
  let arrows = 1;
  let end = points[0][1];
  
  for (let i = 1; i < points.length; i++) {
    if (points[i][0] > end) {
      arrows++;
      end = points[i][1];
    }
  }
  
  return arrows;
}
```

**💬 Explanation + Insight**

- **Sort by End** - Sort balloons by end position
- **Greedy Selection** - Shoot arrow at earliest end position
- **Overlap Check** - Check if balloon starts after current end
- **Time Complexity** - O(n log n) due to sorting
- **Space Complexity** - O(1) constant space

---

### 42. 🟩 IPO

**🧠 Concept**

Maximize capital by selecting projects with maximum profit within capital constraints using priority queue.

**💻 Example**

```javascript
function findMaximizedCapital(k, w, profits, capital) {
  const n = profits.length;
  const projects = [];
  
  for (let i = 0; i < n; i++) {
    projects.push([capital[i], profits[i]]);
  }
  
  projects.sort((a, b) => a[0] - b[0]);
  
  const maxHeap = [];
  let projectIndex = 0;
  
  for (let i = 0; i < k; i++) {
    while (projectIndex < n && projects[projectIndex][0] <= w) {
      maxHeap.push(projects[projectIndex][1]);
      projectIndex++;
    }
    
    if (maxHeap.length === 0) break;
    
    maxHeap.sort((a, b) => b - a);
    w += maxHeap.shift();
  }
  
  return w;
}
```

**💬 Explanation + Insight**

- **Capital Constraint** - Only select projects within current capital
- **Greedy Selection** - Always select project with maximum profit
- **Priority Queue** - Use heap for efficient maximum selection
- **Time Complexity** - O(n log n) for sorting and heap operations
- **Space Complexity** - O(n) for projects array and heap

---

*This comprehensive greedy section covers essential patterns including stock trading, gas station problems, candy distribution, jump games, interval problems, and capital optimization for efficient problem solving.*