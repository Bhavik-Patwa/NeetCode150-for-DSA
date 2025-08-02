# Problem 8.3 - Word Search II
# Given a board and a list of words, return all words that can be formed by navigating adjacent cells.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Backtracking
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Try to match each word from every cell using DFS and backtrack on invalid paths.
# Time  : O(n * m * l)
# Space : O(l)
class Solution1:
    def findWords(self, board, words):
        ROWS, COLS = len(board), len(board[0])
        res = []

        def backtrack(r, c, i):
            if i == len(word):                          # Length of word exceeded : word found fully
                return True
            if (r < 0 or c < 0 or r >= ROWS or          # Index out of bound or Character mismatch
                c >= COLS or board[r][c] != word[i]):
                return False

            board[r][c] = '*'                           # Marking index as visited (temporarily)
            ret = (backtrack(r + 1, c, i + 1) or        # Matching neighbours with next character; Below
                   backtrack(r - 1, c, i + 1) or        # Above
                   backtrack(r, c + 1, i + 1) or        # Right
                   backtrack(r, c - 1, i + 1))          # Left
            board[r][c] = word[i]                       # Restoring character while backtracking
            return ret                                  # Returning if neighbour's character matches

        for word in words:                              # Checking for each word one by one
            flag = False                                # New word
            for r in range(ROWS):                       # Checking each row and column
                if flag:
                    break
                for c in range(COLS):
                    if board[r][c] != word[0]:          # Matching word's 1st character with current character
                        continue
                    if backtrack(r, c, 0):              # Recursively checking neighbours and backtracking 
                        res.append(word)                # Word found
                        flag = True                     # Marking word as already found
                        break
        return res


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Backtracking (Trie + Hash Set)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Build a trie of words and DFS search from each cell, tracking visited positions.
# Time  : O(n * m * 4^l)
# Space : O(n + m + l)
class TrieNode2:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self                                      # Accessing TrieNode object
        for c in word:                                  # Adding word by characters
            if c not in cur.children:
                cur.children[c] = TrieNode2()           # Creating new character TrieNode
            cur = cur.children[c]
        cur.isWord = True

class Solution2:
    def findWords(self, board, words):
        root = TrieNode2()
        for w in words:                                 # Creating Trie for each word 
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()                       # res : storing found words (unique) ; visit : visited nodes

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or     # Index out of bounds or
                (r, c) in visit or                              # Node already visited or
                board[r][c] not in node.children):              # Character mismatch 
                return

            visit.add((r, c))                           # Marking current index as visited
            node = node.children[board[r][c]]           # Next node
            word += board[r][c]                         # Adding character to generated word
            if node.isWord:                             # End of word reached
                res.add(word)                           # Word found; adding to result list

            dfs(r + 1, c, node, word)                   # Recursively checking characters ; Below
            dfs(r - 1, c, node, word)                   # Above
            dfs(r, c + 1, node, word)                   # Right
            dfs(r, c - 1, node, word)                   # Left
            visit.remove((r, c))                        # Removing current index after visiting all neighbours

        for r in range(ROWS):                           # Checking each index/character in rows and columns
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)                                # Converting set to list and returning result


# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. Backtracking (Trie)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Build a trie using array nodes, use DFS to traverse and prune dead paths using reference counts.
# Time  : O(n * m * 4^l)
# Space : O(n + m + l)
class TrieNode3:
    def __init__(self):
        self.children = [None] * 26                 # Dictionary avoided to reduce performance load
        self.idx = -1                               # Initializing index as -1
        self.refs = 0                               # Counting references to the node (passed or end)

    def addWord(self, word, i):
        cur = self                                  # TrieNode object
        cur.refs += 1
        for c in word:                              # Adding by character
            index = ord(c) - ord('a')
            if not cur.children[index]:             # Adding new character node
                cur.children[index] = TrieNode3()
            cur = cur.children[index]
            cur.refs += 1                           # Incrementing the reference count
        cur.idx = i                                 # Storing start index of word at end+1 node (indicating end)

class Solution3:
    def findWords(self, board, words):
        root = TrieNode3()
        for i in range(len(words)):                 # Creating new Trie Node for each word
            root.addWord(words[i], i)

        ROWS, COLS = len(board), len(board[0])
        res = []

        def getIndex(c):                            # Getting ordinal index for each character
            return ord(c) - ord('a')

        def dfs(r, c, node):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS    # Index out of bounds
                or board[r][c] == '*' or not                # Character is already visited
                node.children[getIndex(board[r][c])]):      # Getting index of board character; Character mismatch
                return
            
            tmp = board[r][c]                               # Storing board character temporarily
            board[r][c] = '*'                               # Marking index visited
            prev = node                                     # Setting current node as previous
            node = node.children[getIndex(tmp)]             # Setting current's child node as current

            if node.idx != -1:                              # Node is word end node
                res.append(words[node.idx])                 # Adding word to result
                node.idx = -1                               # Removing end node status
                node.refs -= 1                              # Decrementing reference count
                if not node.refs:                           # If no other words pass through this node, pruning the branch
                    prev.children[getIndex(tmp)] = None     # Removing child reference to prune search space and reduce future DFS calls
                    board[r][c] = tmp                       # Reinstating character at the visited index
                    return

            dfs(r + 1, c, node)                     # Recursively checking neighbours; Below
            dfs(r - 1, c, node)                     # Above
            dfs(r, c + 1, node)                     # Right
            dfs(r, c - 1, node)                     # Left

            board[r][c] = tmp                       # Restoring while backtracking after checking all neighbours

        for r in range(ROWS):                       # Checking each character in rows/columns for each word
            for c in range(COLS):
                dfs(r, c, root)

        return res                                  # Returning result list



def main():
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"]
    ]
    words = ["oath", "pea", "eat", "rain"]

    print(Solution1().findWords(board, words))
    print(Solution2().findWords(board, words))
    print(Solution3().findWords(board, words))


if __name__ == '__main__':
    main()