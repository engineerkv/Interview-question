# Dynamic Programming

## Q116. Fibonacci (Memo & Tabulation)

- Concept: Overlapping subproblems; memo recursion or bottom-up table.

```javascript
function fib(n){ const dp=new Array(n+1).fill(0); dp[1]=1; for(let i=2;i<=n;i++) dp[i]=dp[i-1]+dp[i-2]; return dp[n]; }
```

- Deep Insights:
  - O(n) time, O(1) space with two vars.
  - Memoized recursion also O(n).
  - Base cases n=0,1.
  - Avoid exponential naive recursion.

## Q117. Climbing Stairs

- Concept: Ways(n)=Ways(n-1)+Ways(n-2) like Fibonacci.

```javascript
function climbStairs(n){ let a=1,b=1; while(n--) [a,b]=[b,a+b]; return a; }
```

- Deep Insights:
  - O(n), O(1) space.
  - Combinatorial view exists.
  - Simple fib variant.
  - Handle n=0.

## Q118. Coin Change

- Concept: Min coins to make amount; dp[a]=min(dp[a], dp[a-coin]+1).

```javascript
function coinChange(coins, amount){ const dp=new Array(amount+1).fill(Infinity); dp[0]=0; for(const c of coins) for(let a=c;a<=amount;a++) dp[a]=Math.min(dp[a], dp[a-c]+1); return dp[amount]===Infinity? -1 : dp[amount]; }
```

- Deep Insights:
  - Unbounded knapsack style.
  - Order of loops controls permutations vs combinations.
  - O(amount*coins).
  - -1 when impossible.

## Q119. 0-1 Knapsack

- Concept: Each item once; 1D dp backward loop on weight.

```javascript
function knap01(W, wt, val){ const dp=new Array(W+1).fill(0); for(let i=0;i<wt.length;i++) for(let w=W; w>=wt[i]; w--) dp[w]=Math.max(dp[w], dp[w-wt[i]]+val[i]); return dp[W]; }
```

- Deep Insights:
  - Backwards prevents reuse.
  - O(NW) time.
  - Weight bounded.
  - Value maximization.

## Q120. Longest Increasing Subsequence

- Concept: Patience sorting tails array; binary search replace.

```javascript
function lengthOfLIS(nums){ const t=[]; for(const x of nums){ let i=0,j=t.length; while(i<j){ const m=(i+j>>1); if(t[m]<x) i=m+1; else j=m; } t[i]=x; } return t.length; }
```

- Deep Insights:
  - O(n log n).
  - t[k] = min tail of len k+1.
  - Recover path by tracking prevs.
  - Strictly increasing; adjust for non-decreasing.

## Q121. Longest Common Subsequence

- Concept: dp[i][j] = 1+dp[i-1][j-1] if match else max(top,left).

```javascript
function lcs(a,b){ const m=a.length,n=b.length, dp=Array.from({length:m+1},()=>new Array(n+1).fill(0)); for(let i=1;i<=m;i++) for(let j=1;j<=n;j++) dp[i][j]=a[i-1]===b[j-1]? dp[i-1][j-1]+1 : Math.max(dp[i-1][j],dp[i][j-1]); return dp[m][n]; }
```

- Deep Insights:
  - O(mn).
  - Space optimize to 2 rows.
  - Not contiguous (that’s LCS vs LPS/LRS variants).
  - Backtrack to get sequence.

## Q122. Edit Distance

- Concept: Levenshtein: insert/delete/replace costs; classic 2D DP.

```javascript
function minDistance(a,b){ const m=a.length,n=b.length, dp=Array.from({length:m+1},()=>new Array(n+1).fill(0)); for(let i=0;i<=m;i++) dp[i][0]=i; for(let j=0;j<=n;j++) dp[0][j]=j; for(let i=1;i<=m;i++) for(let j=1;j<=n;j++) dp[i][j]=a[i-1]===b[j-1]? dp[i-1][j-1] : 1+Math.min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]); return dp[m][n]; }
```

- Deep Insights:
  - O(mn) time/space.
  - Reduce to O(min(m,n)) space.
  - Operations symmetric except costs.
  - Base rows/cols are edits from/to empty.

## Q123. Rod Cutting

- Concept: Unbounded knapsack on length; best price per length.

```javascript
function rodCut(price, n){ const dp=new Array(n+1).fill(0); for(let i=1;i<=n;i++) for(let len=1;len<=i;len++) dp[i]=Math.max(dp[i], price[len-1]+dp[i-len]); return dp[n]; }
```

- Deep Insights:
  - O(n^2).
  - Pieces unlimited.
  - Similar to coin change max value.
  - Track cuts to reconstruct.

## Q124. Partition Equal Subset Sum

- Concept: Can we reach sum=total/2 via subset? 1D boolean DP.

```javascript
function canPartition(nums){ const s=nums.reduce((a,b)=>a+b,0); if(s%2) return false; const t=s>>1, dp=new Array(t+1).fill(false); dp[0]=true; for(const x of nums) for(let j=t;j>=x;j--) dp[j]=dp[j]||dp[j-x]; return dp[t]; }
```

- Deep Insights:
  - Backwards loop for 0-1.
  - Early pruning by big numbers.
  - O(n*sum/2).
  - Exact half only.

## Q125. House Robber

- Concept: dp[i] = max(dp[i-1], dp[i-2]+nums[i]).

```javascript
function rob(nums){ let take=0, skip=0; for(const x of nums){ [take,skip]=[skip+x, Math.max(take,skip)]; } return Math.max(take,skip); }
```

- Deep Insights:
  - O(n), O(1) space.
  - Track include/exclude.
  - Non-adjacent constraint.
  - Negative values unusual.

## Q126. House Robber II

- Concept: Circle -> rob max of linear(0..n-2) or linear(1..n-1).

```javascript
function rob2(nums){ if(nums.length===1) return nums[0]; const f=a=>{ let t=0,s=0; for(const x of a){ [t,s]=[s+x, Math.max(t,s)]; } return Math.max(t,s); }; return Math.max(f(nums.slice(0,-1)), f(nums.slice(1))); }
```

- Deep Insights:
  - Two runs cover exclusion of first/last.
  - O(n) time.
  - Edge: n=1.
  - Same recurrence as Rob I.

## Q127. Decode Ways

- Concept: dp[i]=ways up to i; use one/two-digit valid decodes.

```javascript
function numDecodings(s){ if(!s||s[0]==='0') return 0; let a=1,b=1; for(let i=1;i<s.length;i++){ const one=s[i]!=='0', two= s[i-1]!=='0' && Number(s.slice(i-1,i+1))<=26; const c=(one?b:0)+(two?a:0); a=b; b=c; if(b===0) return 0; } return b; }
```

- Deep Insights:
  - Handle zeros carefully.
  - O(n) time, O(1) space.
  - Two-digit check <=26 and not leading zero.
  - Early return when dead.

## Q128. DP on Grid — Min Path / Unique Paths

- Concept: Grid DP with from-top/from-left transitions (blockers optional).

```javascript
function minPathSum(g){ const m=g.length,n=g[0].length, dp=new Array(n).fill(0); for(let i=0;i<m;i++) for(let j=0;j<n;j++) dp[j]=g[i][j]+Math.min(j?dp[j-1]:Infinity, i?dp[j]:Infinity); return dp[n-1]; }
function uniquePaths(m,n){ const dp=new Array(n).fill(1); for(let i=1;i<m;i++) for(let j=1;j<n;j++) dp[j]+=dp[j-1]; return dp[n-1]; }
```

- Deep Insights:
  - 1D rolling arrays save space.
  - Obstacles require zeroing cells.
  - Right/down moves standard.
  - O(mn).

## Q129. Palindromic Substrings

- Concept: Expand around centers O(n^2) to count palindromes.

```javascript
function countSubstrings(s){ let ans=0; const go=(l,r)=>{ while(l>=0&&r<s.length&&s[l]===s[r]){ ans++; l--; r++; } }; for(let i=0;i<s.length;i++){ go(i,i); go(i,i+1); } return ans; }
```

- Deep Insights:
  - O(n^2) time, O(1) space.
  - Manacher gives O(n) but complex.
  - Count vs longest uses same expansion.
  - Works for empty as 0.

## Q130. Burst Balloons

- Concept: Interval DP; dp[l][r] = best bursting (l,r) with last balloon k.

```javascript
function maxCoins(nums){ const a=[1,...nums,1], n=a.length; const dp=Array.from({length:n},()=>Array(n).fill(0)); for(let len=2; len<n; len++) for(let l=0;l+len<n;l++){ const r=l+len; for(let k=l+1;k<r;k++) dp[l][r]=Math.max(dp[l][r], a[l]*a[k]*a[r]+dp[l][k]+dp[k][r]); } return dp[0][n-1]; }
```

- Deep Insights:
  - O(n^3).
  - Padding 1s simplifies edges.
  - Choose last to burst in subinterval.
  - Classic interval DP.

## Q131. Job Scheduling

- Concept: Sort by end time; dp[i]=max(profit up to i, profit[i]+dp[prevNonOverlap]).

```javascript
function jobScheduling(start, end, profit){ const n=start.length, jobs=[]; for(let i=0;i<n;i++) jobs.push([start[i],end[i],profit[i]]); jobs.sort((a,b)=>a[1]-b[1]); const ends=jobs.map(j=>j[1]); const dp=new Array(n).fill(0); for(let i=0;i<n;i++){ const [s,e,p]=jobs[i]; let l=0,r=i-1,pos=-1; while(l<=r){ const m=(l+r>>1); if(ends[m]<=s){ pos=m; l=m+1; } else r=m-1; } dp[i]=Math.max(i?dp[i-1]:0, p + (pos>=0?dp[pos]:0)); } return dp[n-1]; }
```

- Deep Insights:
  - O(n log n).
  - Binary search for previous non-overlap.
  - Weighted interval scheduling.
  - Sort by end time.

## Q132. Wildcard Matching

- Concept: DP over i,j with '*' matching any sequence and '?' any char.

```javascript
function isMatch(s,p){ const m=s.length,n=p.length, dp=Array.from({length:m+1},()=>Array(n+1).fill(false)); dp[0][0]=true; for(let j=1;j<=n;j++) if(p[j-1]==='*') dp[0][j]=dp[0][j-1]; for(let i=1;i<=m;i++) for(let j=1;j<=n;j++) dp[i][j]= p[j-1]==='*'? dp[i][j-1]||dp[i-1][j] : (p[j-1]==='?'||p[j-1]===s[i-1]) && dp[i-1][j-1]; return dp[m][n]; }
```

- Deep Insights:
  - O(mn) time/space.
  - Leading '*' can match empty.
  - Greedy two-pointer alternative exists.
  - Careful with multiple '*'.

## Q133. Subset Sum

- Concept: Classic boolean DP to target sum using 0-1 items.

```javascript
function subsetSum(nums, target){ const dp=new Array(target+1).fill(false); dp[0]=true; for(const x of nums) for(let t=target;t>=x;t--) dp[t]=dp[t]||dp[t-x]; return dp[target]; }
```

- Deep Insights:
  - Same as partition half.
  - Backwards loop for 0-1.
  - O(n*target).
  - Early break if dp[target] true.

## Q134. Unbounded Knapsack

- Concept: Items unlimited; forward loop on weight to allow reuse.

```javascript
function unboundedKnapsack(W, wt, val){ const dp=new Array(W+1).fill(0); for(let i=0;i<wt.length;i++) for(let w=wt[i]; w<=W; w++) dp[w]=Math.max(dp[w], dp[w-wt[i]]+val[i]); return dp[W]; }
```

- Deep Insights:
  - Forward loop enables reuse.
  - O(NW) time.
  - Similar to coin change max value.
  - Items infinite.

## Q135. Maximum Rectangle

- Concept: For each row as histogram, use largest-rectangle stack.

```javascript
function maximalRectangle(mat){ if(!mat.length) return 0; const m=mat.length,n=mat[0].length,h=new Array(n).fill(0); let best=0; const area=arr=>{ const st=[], a=[...arr,0]; let res=0; for(let i=0;i<a.length;i++){ while(st.length && a[i]<a[st[st.length-1]]){ const height=a[st.pop()], left=st.length? st[st.length-1]+1 : 0; res=Math.max(res, height*(i-left)); } st.push(i);} return res; }; for(let r=0;r<m;r++){ for(let c=0;c<n;c++) h[c]=mat[r][c]==='1'? h[c]+1 : 0; best=Math.max(best, area(h)); } return best; }
```

- Deep Insights:
  - O(mn).
  - Reuses histogram logic.
  - Binary matrix of '1'/'0'.
  - Stack pattern crucial.

## Q136. Rain Water with DP

- Concept: Precompute leftMax/rightMax arrays; water at i = min(L,R)-h[i].

```javascript
function trapDP(h){ const n=h.length,L=new Array(n),R=new Array(n); for(let i=0,m=0;i<n;i++){ m=Math.max(m,h[i]); L[i]=m; } for(let i=n-1,m=0;i>=0;i--){ m=Math.max(m,h[i]); R[i]=m; } let w=0; for(let i=0;i<n;i++) w+=Math.min(L[i],R[i])-h[i]; return w; }
```

- Deep Insights:
  - O(n) time, O(n) space.
  - Two-pointer reduces to O(1) space.
  - Non-negative heights.
  - Classic DP precompute.

## Q137. Egg Dropping

- Concept: dp[k][m]=max floors solvable with k eggs and m moves; increase m until >= N.

```javascript
function superEggDrop(k, n){ const dp=new Array(k+1).fill(0); let m=0; while(dp[k]<n){ m++; for(let e=k;e>=1;e--) dp[e]=dp[e]+dp[e-1]+1; } return m; }
```

- Deep Insights:
  - O(k log n) style with triangular sums.
  - dp[e] floors with e eggs, m moves.
  - Much faster than O(kn) DP.
  - Monotonic m increases.

## Q138. Matrix Chain Multiplication

- Concept: Interval DP; dp[i][j]=min over k of dp[i][k]+dp[k][j]+cost.

```javascript
function matrixChainOrder(p){ const n=p.length-1; const dp=Array.from({length:n},()=>Array(n).fill(0)); for(let len=2; len<=n; len++) for(let i=0;i+len-1<n;i++){ const j=i+len-1; dp[i][j]=Infinity; for(let k=i;k<j;k++) dp[i][j]=Math.min(dp[i][j], dp[i][k]+dp[k+1][j]+p[i]*p[k+1]*p[j+1]); } return dp[0][n-1]; }
```

- Deep Insights:
  - O(n^3) time.
  - p stores dims: p[i-1]x p[i].
  - Parenthesization optimization.
  - No actual multiplication.

## Q139. Min Cost Climbing Stairs

- Concept: dp[i]=cost[i]+min(dp[i-1], dp[i-2]); answer min of last two.

```javascript
function minCostClimbingStairs(cost){ let a=0,b=0; for(const c of cost){ [a,b]=[b, Math.min(a,b)+c]; } return Math.min(a,b); }
```

- Deep Insights:
  - O(n), O(1) space.
  - Start at 0 or 1 index.
  - Local choice optimal.
  - Similar to climb stairs.

## Q140. Buy & Sell Stock DP (multiple variants)

- Concept: Track states: hold/cash with constraints (k, cooldown, fee).

```javascript
function maxProfitCooldown(prices){ let hold=-Infinity, cash=0, prev=0; for(const p of prices){ const tmp=cash; cash=Math.max(cash, hold+p); hold=Math.max(hold, prev-p); prev=tmp; } return cash; }
```

- Deep Insights:
  - Variants: single, unlimited, k, fee, cooldown.
  - State machine DP.
  - O(n) time.
  - Initialize carefully per variant.
