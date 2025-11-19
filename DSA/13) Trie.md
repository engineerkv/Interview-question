# Trie

## Q208. Implement Trie (Prefix Tree)

**Problem:** A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker. Implement the Trie class:
- `Trie()` Initializes the trie object.
- `void insert(String word)` Inserts the string `word` into the trie.
- `boolean search(String word)` Returns `true` if the string `word` is in the trie (i.e., was inserted before), and `false` otherwise.
- `boolean startsWith(String prefix)` Returns `true` if there is a previously inserted string `word` that has the prefix `prefix`, and `false` otherwise.

**Approach:** Each node stores children in a map/dict and has an `isEnd` flag. Traverse character by character, creating nodes as needed.

### Solution 1: Trie Implementation (Optimal)
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
    node.isEnd = true;  // Mark end of word
  }

  search(word) {
    let node = this.root;
    for (const char of word) {
      if (!node[char]) {
        return false;
      }
      node = node[char];
    }
    return node.isEnd === true;  // Check if word ends here
  }

  startsWith(prefix) {
    let node = this.root;
    for (const char of prefix) {
      if (!node[char]) {
        return false;
      }
      node = node[char];
    }
    return true;  // Prefix exists
  }
}
```

// Test Cases:
// Input: ["Trie", "insert", "search", "search", "startsWith", "insert", "search"], [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
// Output: [null, null, true, false, true, null, true]
// Explanation: 
//   Trie trie = new Trie();
//   trie.insert("apple");
//   trie.search("apple");   // returns true
//   trie.search("app");      // returns false
//   trie.startsWith("app");  // returns true
//   trie.insert("app");
//   trie.search("app");      // returns true
```

**Time Complexity:** O(m) - Per insert/search/startsWith where m is word length  
**Space Complexity:** O(n × m) - n words of average length m


## Q209. Design Add and Search Words Data Structure

**Problem:** Design a data structure that supports adding new words and finding if a string matches any previously added string. Implement the `WordDictionary` class:
- `WordDictionary()` Initializes the object.
- `void addWord(word)` Adds `word` to the data structure, it can be matched later.
- `bool search(word)` Returns `true` if there is any string in the data structure that matches `word` or `false` otherwise. `word` may contain dots `'.'` where dots can be matched with any letter.

**Approach:** Use Trie structure. For wildcard `'.'`, recursively try all children. For regular characters, traverse normally.

### Solution 1: Trie with DFS (Optimal)
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
    // Base case: reached end of word
    if (index === word.length) {
      return node.isEnd === true;
    }

    const char = word[index];
    
    if (char === '.') {
      // Wildcard: try all children (skip 'isEnd')
      for (const key in node) {
        if (key !== 'isEnd' && this.dfs(word, index + 1, node[key])) {
          return true;
        }
      }
      return false;
    } else {
      // Regular character: traverse normally
      if (!node[char]) {
        return false;
      }
      return this.dfs(word, index + 1, node[char]);
    }
  }
}
```

// Test Cases:
// Input: ["WordDictionary","addWord","addWord","addWord","search","search","search","search"], [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
// Output: [null,null,null,null,false,true,true,true]
// Explanation: 
//   WordDictionary wordDictionary = new WordDictionary();
//   wordDictionary.addWord("bad");
//   wordDictionary.addWord("dad");
//   wordDictionary.addWord("mad");
//   wordDictionary.search("pad");  // returns false
//   wordDictionary.search("bad");  // returns true
//   wordDictionary.search(".ad");  // returns true ('.' matches 'b' or 'd' or 'm')
//   wordDictionary.search("b.."); // returns true ('.' matches any character)
```

**Time Complexity:** O(m) for exact match, O(26^m) worst case for m wildcards  
**Space Complexity:** O(n × m) - n words of average length m


## Q210. Word Search II

**Problem:** Given an `m x n` board of characters and a list of strings `words`, return all words on the board. Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

**Approach:** Build Trie from words. Use DFS with backtracking on board. Mark visited cells and remove found words from Trie to avoid duplicates.

### Solution 1: Trie + DFS (Optimal)
```javascript
function findWords(board, words) {
  const trie = new Trie();
  // Build Trie from words
  for (const word of words) {
    trie.insert(word);
  }

  const result = [];
  const m = board.length;
  const n = board[0].length;

  function dfs(i, j, node) {
    const char = board[i][j];
    const nextNode = node[char];
    
    // No path in Trie
    if (!nextNode) return;
    
    // Word found
    if (nextNode.word) {
      result.push(nextNode.word);
      delete nextNode.word; // Remove to avoid duplicates
    }

    // Mark visited
    const temp = board[i][j];
    board[i][j] = '#';

    // Explore 4 directions
    const directions = [[-1,0],[1,0],[0,-1],[0,1]];
    for (const [di, dj] of directions) {
      const ni = i + di, nj = j + dj;
      if (ni >= 0 && ni < m && nj >= 0 && nj < n && board[ni][nj] !== '#') {
        dfs(ni, nj, nextNode);
      }
    }

    // Backtrack
    board[i][j] = temp;
  }

  // Start DFS from each cell
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      dfs(i, j, trie.root);
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
```

// Test Cases:
// Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
// words = ["oath","pea","eat","rain"]
// Output: ["eat","oath"]

// Input: board = [["a","b"],["c","d"]], words = ["abcb"]
// Output: []
```

**Time Complexity:** O(mn × 4^L) - L is max word length, 4 directions per cell  
**Space Complexity:** O(n × m) - Trie for n words, DFS recursion depth up to m


---

## Bonus: Trie Fundamentals

**Concept:** Prefix tree storing characters per edge; supports insert, search, prefix search in O(L).

```javascript
class Trie {
  constructor() {
    this.root = {};
  }

  insert(word) {
    let node = this.root;
    for (const ch of word) {
      node[ch] = node[ch] || {};
      node = node[ch];
    }
    node.$ = true; // end marker
  }

  search(word) {
    let node = this.root;
    for (const ch of word) {
      if (!node[ch]) return false;
      node = node[ch];
    }
    return !!node.$;
  }

  startsWith(prefix) {
    let node = this.root;
    for (const ch of prefix) {
      if (!node[ch]) return false;
      node = node[ch];
    }
    return true;
  }
}

// Test Cases:
// Input:
// let trie = new Trie();
// trie.insert("apple");
// trie.search("apple");   // Output: true
// trie.search("app");     // Output: false
// trie.startsWith("app"); // Output: true
// trie.insert("app");
// trie.search("app");     // Output: true

// Input:
// let trie = new Trie();
// trie.insert("hello");
// trie.insert("world");
// trie.search("hell");     // Output: false
// trie.startsWith("hell"); // Output: true
// trie.search("hello");    // Output: true

// Input:
// let trie = new Trie();
// trie.insert("a");
// trie.search("a");        // Output: true
// trie.startsWith("a");    // Output: true
```

**Time Complexity:** O(L) - Each operation processes word length L  
**Space Complexity:** O(AL) - Storage for all words where A is alphabet size


