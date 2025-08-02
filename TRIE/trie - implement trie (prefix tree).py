# Problem 8.1 - Implement Trie (Prefix Tree)
# Design a prefix tree data structure supporting insert, search and prefix matching.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Prefix Tree (Array)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use a fixed-size array of 26 slots (a-z) for each TrieNode to store children.
# Time  : O(n)
# Space : O(n)
class TrieNode1:
    def __init__(self):
        self.children = [None] * 26                 # Array of 26 slots for 'a' to 'z'
        self.endOfWord = False                      # True if node marks end of a word

class Solution1:
    def __init__(self):
        self.root = TrieNode1()

    def insert(self, word):
        cur = self.root
        for c in word:
            i = ord(c) - ord("a")                   # Mapping character to index 0–25 using ordinals
            if cur.children[i] == None:
                cur.children[i] = TrieNode1()       # Creating and Replacing None with new node if missing
            cur = cur.children[i]
        cur.endOfWord = True                        # Marking end of the word

    def search(self, word):
        cur = self.root
        for c in word:
            i = ord(c) - ord("a")                   # Identifying index 0–25 using ordinals
            if cur.children[i] == None:
                return False                        # Character not found
            cur = cur.children[i]                   # Traversing to next node using location at index
        return cur.endOfWord                        # Search must end exactly at a word node, else it fails

    def startsWith(self, prefix):
        cur = self.root
        for c in prefix:
            i = ord(c) - ord("a")                   # Identifying index 0–25 using ordinals
            if cur.children[i] == None:
                return False                        # Prefix path doesn't exist
            cur = cur.children[i]
        return True                                 # Prefix path is correct


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Prefix Tree (Hash Map)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use hash maps (dict) in each TrieNode for dynamic character indexing and space efficiency.
# Time  : O(n)
# Space : O(n)
class TrieNode2:
    def __init__(self):
        self.children = {}                              # Using Dictionary for character mapping
        self.endOfWord = False

class Solution2:
    def __init__(self):
        self.root = TrieNode2()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:                   # If character not in dictionary
                cur.children[c] = TrieNode2()           # Creating node with character as key
            cur = cur.children[c]                       # Traversing to new node
        cur.endOfWord = True                            # Marking end of the word

    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:                   # If character not in dictionary
                return False                            # Character not found
            cur = cur.children[c]                       # Traversing to next node
        return cur.endOfWord                            # Searching complete only if end of word reached

    def startsWith(self, prefix):
        cur = self.root
        for c in prefix:
            if c not in cur.children:                   # If character not in dictionary
                return False                            # Prefix path doesn't exist
            cur = cur.children[c]                       # Traversing to next node
        return True                                     # Prefix path is correct



def main():
    trie1 = Solution1()
    trie1.insert("apple")
    print(trie1.search("apple"))
    print(trie1.search("app"))
    print(trie1.startsWith("app"))

    trie2 = Solution2()
    trie2.insert("apple")
    print(trie2.search("apple"))
    print(trie2.search("app"))
    print(trie2.startsWith("app"))


if __name__ == '__main__':
    main()