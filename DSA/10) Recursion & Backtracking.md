# Recursion & Backtracking

## Q141. N-Queens

- Concept: Place queens row by row, pruning columns and diagonals using sets.

```javascript
function solveNQueens(n){ const res=[], col=new Set(), d1=new Set(), d2=new Set(), board=Array.from({length:n},()=>'.'.repeat(n).split('')); function bt(r){ if(r===n){ res.push(board.map(x=>x.join(''))); return; } for(let c=0;c<n;c++){ if(col.has(c)||d1.has(r-c)||d2.has(r+c)) continue; col.add(c); d1.add(r-c); d2.add(r+c); board[r][c]='Q'; bt(r+1); board[r][c]='.'; col.delete(c); d1.delete(r-c); d2.delete(r+c); } } bt(0); return res; }
```

- Deep Insights:
  - O(n!) worst-case, pruning vital.
  - Diagonals tracked by r±c.
  - Return boards as strings.
  - Symmetry not exploited here.

## Q142. Sudoku Solver

- Concept: Backtrack cell by cell; maintain row/col/box availability.

```javascript
function solveSudoku(board){ const R=Array.from({length:9},()=>new Set()), C=Array.from({length:9},()=>new Set()), B=Array.from({length:9},()=>new Set()); const box=(r,c)=>Math.floor(r/3)*3+Math.floor(c/3); const empty=[]; for(let r=0;r<9;r++) for(let c=0;c<9;c++){ const ch=board[r][c]; if(ch==='.') empty.push([r,c]); else { R[r].add(ch); C[c].add(ch); B[box(r,c)].add(ch); } }
  function bt(i){ if(i===empty.length) return true; const [r,c]=empty[i]; for(let d=1; d<=9; d++){ const ch=String(d); const b=box(r,c); if(R[r].has(ch)||C[c].has(ch)||B[b].has(ch)) continue; board[r][c]=ch; R[r].add(ch); C[c].add(ch); B[b].add(ch); if(bt(i+1)) return true; board[r][c]='.'; R[r].delete(ch); C[c].delete(ch); B[b].delete(ch); } return false; }
  bt(0); return board;
}
```

- Deep Insights:
  - Choose next empty (MRV) for speed.
  - Sets track constraints.
  - Backtracks on dead ends.
  - Valid puzzle assumed.

## Q143. Permutations / Combinations

- Concept: Build paths; for combinations control start index; for permutations use used-set or swap.

```javascript
function permute(nums){ const res=[], used=new Array(nums.length).fill(false), cur=[]; (function bt(){ if(cur.length===nums.length){ res.push([...cur]); return;} for(let i=0;i<nums.length;i++){ if(used[i]) continue; used[i]=true; cur.push(nums[i]); bt(); cur.pop(); used[i]=false; } })(); return res; }
function combine(n,k){ const res=[], cur=[]; (function bt(s){ if(cur.length===k){ res.push([...cur]); return;} for(let i=s;i<=n;i++){ cur.push(i); bt(i+1); cur.pop(); } })(1); return res; }
```

- Deep Insights:
  - O(n!) permutations; O(n choose k) combos.
  - Prune with remaining count.
  - Avoid duplicates by sorting + skip equal.
  - Iterative variants exist.

## Q144. Subsets / Power Set

- Concept: Decide include/exclude per item or iterate size by size.

```javascript
function subsets(nums){ const res=[[]]; for(const x of nums){ const add=res.map(s=>[...s,x]); res.push(...add); } return res; }
```

- Deep Insights:
  - 2^n subsets.
  - Backtracking alternative.
  - For duplicates, sort and skip same-start.
  - Order not important.

## Q145. Generate Parentheses

- Concept: Backtrack ensuring open used <= n and close <= open.

```javascript
function generateParenthesis(n){ const res=[]; (function bt(o,c,str){ if(str.length===2*n){ res.push(str); return;} if(o<n) bt(o+1,c,str+'('); if(c<o) bt(o,c+1,str+')'); })(0,0,''); return res; }
```

- Deep Insights:
  - Catalan numbers count.
  - Prune invalid states early.
  - O(Cn) outputs.
  - Balanced by construction.

## Q146. Word Search

- Concept: DFS from each cell matching next character, mark visited and backtrack.

```javascript
function exist(board, word){ const m=board.length,n=board[0].length; const dirs=[[1,0],[-1,0],[0,1],[0,-1]]; const seen=Array.from({length:m},()=>Array(n).fill(false)); function dfs(r,c,i){ if(i===word.length) return true; if(r<0||c<0||r>=m||c>=n||seen[r][c]||board[r][c]!==word[i]) return false; seen[r][c]=true; for(const [dr,dc] of dirs) if(dfs(r+dr,c+dc,i+1)) return true; seen[r][c]=false; return false; }
  for(let i=0;i<m;i++) for(let j=0;j<n;j++) if(dfs(i,j,0)) return true; return false;
}
```

- Deep Insights:
  - O(mn·4^L) worst-case.
  - Early break when full match.
  - Mark/unmark visited.
  - Prune by first char counts.

## Q147. Rat in a Maze

- Concept: From start, move in allowed directions marking path; backtrack on walls.

```javascript
function ratMaze(maze){ const m=maze.length,n=maze[0].length, res=[]; const dirs=[[1,0,'D'],[0,1,'R'],[-1,0,'U'],[0,-1,'L']]; const seen=Array.from({length:m},()=>Array(n).fill(false)); function bt(r,c,path){ if(r===m-1&&c===n-1){ res.push(path); return; } seen[r][c]=true; for(const [dr,dc,ch] of dirs){ const nr=r+dr,nc=c+dc; if(nr>=0&&nc>=0&&nr<m&&nc<n && maze[nr][nc]===1 && !seen[nr][nc]) bt(nr,nc,path+ch); } seen[r][c]=false; }
  if(maze[0][0]===1) bt(0,0,''); return res;
}
```

- Deep Insights:
  - Variants restrict moves.
  - Track visited to avoid loops.
  - Multiple paths collected.
  - Grid of 0/1.

## Q148. Combination Sum

- Concept: Choose candidate multiple times; backtrack with start index to avoid permutations.

```javascript
function combinationSum(cands, target){ cands.sort((a,b)=>a-b); const res=[], cur=[]; (function bt(i,sum){ if(sum===target){ res.push([...cur]); return;} for(let k=i;k<cands.length;k++){ const x=cands[k]; if(sum+x>target) break; cur.push(x); bt(k,sum+x); cur.pop(); } })(0,0); return res; }
```

- Deep Insights:
  - Unbounded choices.
  - Sort + break for pruning.
  - No duplicates by non-decreasing picks.
  - Target sums only.

## Q149. Letter combinations of Phone Number

- Concept: Map digits to letters; backtrack by appending choices per digit.

```javascript
function letterCombinations(d){ if(!d) return []; const map={2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}; const res=[], cur=[]; (function bt(i){ if(i===d.length){ res.push(cur.join('')); return;} for(const ch of map[d[i]]){ cur.push(ch); bt(i+1); cur.pop(); } })(0); return res; }
```

- Deep Insights:
  - O(3^m 4^n).
  - Empty input yields [].
  - Order by digit mapping.
  - Iterative queue variant exists.

## Q150. Palindrome Partitioning

- Concept: Backtrack split string; add substring if palindrome.

```javascript
function partition(s){ const res=[], cur=[]; const isPal=(l,r)=>{ while(l<r) if(s[l++]!==s[r--]) return false; return true; }; (function bt(i){ if(i===s.length){ res.push([...cur]); return;} for(let j=i;j<s.length;j++){ if(isPal(i,j)){ cur.push(s.slice(i,j+1)); bt(j+1); cur.pop(); } } })(0); return res; }
```

- Deep Insights:
  - O(n·2^n) backtracking.
  - Precompute DP pal table to prune.
  - Output all partitions.
  - Useful for cut problems.
