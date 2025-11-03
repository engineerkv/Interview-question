# Trie

## Q156. Implement Trie (Prefix Tree)

Concept: Prefix tree storing words; each node has children map and isEnd flag; insert/search/startsWith operations.

```javascript
class Trie {
  constructor() {
    this.root = {};
  }

  insert(word) {
    let node = this.root;
    for (const char of word) {
      if (!node[char]) {
        node[char] = {};
      }
      node = node[char];
    }
    node.isEnd = true;
  }

  search(word) {
    let node = this.root;
    for (const char of word) {
      if (!node[char]) {
        return false;
      }
      node = node[char];
    }
    return node.isEnd === true;
  }

  startsWith(prefix) {
    let node = this.root;
    for (const char of prefix) {
      if (!node[char]) {
        return false;
      }
      node = node[char];
    }
    return true;
  }
}

// Test Cases:
//
// Example 1:
//   Input: ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
//          [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
//   Output: [null, null, true, false, true, null, true]
//   Explanation: 
//     Trie trie = new Trie();
//     trie.insert("apple");
//     trie.search("apple");   // returns true
//     trie.search("app");      // returns false
//     trie.startsWith("app");  // returns true
//     trie.insert("app");
//     trie.search("app");      // returns true
```

Deep Insights:
  - Rule: Prefix tree with children map and isEnd flag; insert/search/startsWith in O(m) time per operation.
  - Real-world: Autocomplete, spell checkers, prefix matching, word dictionaries.
  - Common mistake: Forgetting isEnd flag for word completion; not handling empty strings correctly.
  - Optimization: O(m) time per operation where m is word length; space O(n×m) for n words of avg length m.
  - Interview tip: Explain prefix tree structure clearly; mention isEnd flag; ask about space optimization.

Time Complexity: O(m) - Per insert/search/startsWith where m is word length
Space Complexity: O(n×m) - n words of average length m

## Q157. Design Add and Search Words Data Structure

Concept: Trie with wildcard '.' support; search recursively when encountering '.' by trying all children.

```javascript
class WordDictionary {
  constructor() {
    this.root = {};
  }

  addWord(word) {
    let node = this.root;
    for (const char of word) {
      if (!node[char]) {
        node[char] = {};
      }
      node = node[char];
    }
    node.isEnd = true;
  }

  search(word) {
    return this.dfs(word, 0, this.root);
  }

  dfs(word, index, node) {
    if (index === word.length) {
      return node.isEnd === true;
    }

    const char = word[index];
    
    if (char === '.') {
      // Try all children
      for (const key in node) {
        if (key !== 'isEnd' && this.dfs(word, index + 1, node[key])) {
          return true;
        }
      }
      return false;
    } else {
      if (!node[char]) {
        return false;
      }
      return this.dfs(word, index + 1, node[char]);
    }
  }
}

// Test Cases:
//
// Example 1:
//   Input: ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
//          [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
//   Output: [null,null,null,null,false,true,true,true]
//   Explanation: 
//     WordDictionary wordDictionary = new WordDictionary();
//     wordDictionary.addWord("bad");
//     wordDictionary.addWord("dad");
//     wordDictionary.addWord("mad");
//     wordDictionary.search("pad");  // returns false
//     wordDictionary.search("bad");  // returns true
//     wordDictionary.search(".ad");  // returns true ('.' matches 'b' or 'd' or 'm')
//     wordDictionary.search("b.."); // returns true ('.' matches any character)
```

Deep Insights:
  - Rule: Trie with wildcard '.' support; DFS search recursively when encountering '.'; O(26^m) worst case for m '.'.
  - Real-world: Pattern matching with wildcards, search with partial information, autocomplete with typos.
  - Common mistake: Not handling '.' correctly; wrong recursive search logic; not skipping 'isEnd' in children iteration.
  - Optimization: O(m) for exact match, O(26^m) worst case for m wildcards; skip 'isEnd' when iterating children.
  - Interview tip: Explain wildcard handling clearly; mention recursive DFS; ask about optimization.

Time Complexity: O(m) exact match, O(26^m) worst case for m wildcards
Space Complexity: O(n×m) - n words of average length m

## Q158. Word Search II

Concept: Build Trie from words; DFS on board with backtracking; mark visited cells; remove found words from Trie.

```javascript
function findWords(board, words) {
  const trie = new Trie();
  for (const word of words) {
    trie.insert(word);
  }

  const result = [];
  const m = board.length;
  const n = board[0].length;

  const dfs = (i, j, node, path) => {
    const char = board[i][j];
    const nextNode = node[char];
    
    if (!nextNode) return;

    path += char;
    
    if (nextNode.word) {
      result.push(nextNode.word);
      delete nextNode.word; // Avoid duplicates
    }

    const temp = board[i][j];
    board[i][j] = '#'; // Mark visited

    const directions = [[-1,0],[1,0],[0,-1],[0,1]];
    for (const [di, dj] of directions) {
      const ni = i + di, nj = j + dj;
      if (ni >= 0 && ni < m && nj >= 0 && nj < n && board[ni][nj] !== '#') {
        dfs(ni, nj, nextNode, path);
      }
    }

    board[i][j] = temp; // Backtrack
  };

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      dfs(i, j, trie.root, '');
    }
  }

  return result;
}

class Trie {
  constructor() {
    this.root = {};
  }

  insert(word) {
    let node = this.root;
    for (const char of word) {
      if (!node[char]) {
        node[char] = {};
      }
      node = node[char];
    }
    node.word = word; // Store word at end node
  }
}

// Test Cases:
//
// Example 1:
//   Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
//          words = ["oath","pea","eat","rain"]
//   Output: ["eat","oath"]
//
// Example 2:
//   Input: board = [["a","b"],["c","d"]], words = ["abcb"]
//   Output: []
```

Deep Insights:
  - Rule: Build Trie from words; DFS with backtracking; mark visited cells; remove found words; O(mn×4^L) time.
  - Real-world: Word search puzzles, pattern matching on grid, autocomplete suggestions.
  - Common mistake: Not backtracking visited cells; not removing found words; wrong DFS logic.
  - Optimization: O(mn×4^L) time where L is max word length; backtracking crucial; remove found words to avoid duplicates.
  - Interview tip: Explain Trie + DFS strategy clearly; mention backtracking; ask about optimization.

Time Complexity: O(mn×4^L) - L is max word length, 4 directions per cell
Space Complexity: O(n×m) - Trie for n words, DFS recursion depth up to m

