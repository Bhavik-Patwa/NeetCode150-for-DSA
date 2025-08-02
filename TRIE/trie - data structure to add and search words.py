# Problem 8.2 - Design Add and Search Word Data Structure
# Implement a data structure that allows adding words and searching with support for '.' wildcard.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Brute Force
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Store all words and compare character by character during search allowing '.' to match any character.
# Time  : O(n * m)
# Space : O(n)
class Solution1:
    def __init__(self):
        self.store = []

    def addWord(self, word):
        self.store.append(word)                             # Appending word in list

    def search(self, word):
        for w in self.store:
            if len(w) != len(word):                         # Skipping words of different length
                continue
            i = 0
            while i < len(w):
                if w[i] == word[i] or word[i] == '.':       # Matching exact character or wildcard
                    i += 1                                  # Indexing to next character
                else:
                    break                                   # Character mismatch
            if i == len(w):
                return True                                 # All characters matched
        return False


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Depth First Search (Trie)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use a Trie and DFS to explore branches when encountering '.' during search.
# Time  : O(n)
# Space : O(n)
class TrieNode:
    def __init__(self):
        self.children = {}                                  # Dictionary to hold children
        self.wordEnd = False                                # True if word ends here

class Solution2:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        cur = self.root
        for c in word:                                      # Adding by character
            if c not in cur.children:                       # Character not found in dictionary
                cur.children[c] = TrieNode()                # Creating new node with character as key
            cur = cur.children[c]                           # Traversing to next node
        cur.wordEnd = True                                  # Marking end of word

    def search(self, word):
        def dfs(j, root):                                   # Recursively searching for each character
            cur = root
            for i in range(j, len(word)):                   # For each character, from start or continuing from latest
                c = word[i]                                 # Current character
                if c == ".":                                # Character is a wildcard (implicitly skipping)
                    for child in cur.children.values():     # Checking all children (all next character nodes) of current
                        if dfs(i + 1, child):               # Matching next character with each child
                            return True                     # If match found, recursing its children
                    return False
                else:
                    if c not in cur.children:               # Character is not wildcard. If character not in dictionary
                        return False                        # Character not in trie
                    cur = cur.children[c]                   # Character found, traversing to next node
            return cur.wordEnd                              # Searching fails if end of word not reached

        return dfs(0, self.root)



def main():
    obj1 = Solution1()
    obj1.addWord("bad")
    obj1.addWord("dad")
    obj1.addWord("mad")
    print(obj1.search("pad"))
    print(obj1.search("bad"))
    print(obj1.search(".ad"))
    print(obj1.search("b.."))

    obj2 = Solution2()
    obj2.addWord("bad")
    obj2.addWord("dad")
    obj2.addWord("mad")
    print(obj2.search("pad"))
    print(obj2.search("bad"))
    print(obj2.search(".ad"))
    print(obj2.search("b.."))


if __name__ == '__main__':
    main()