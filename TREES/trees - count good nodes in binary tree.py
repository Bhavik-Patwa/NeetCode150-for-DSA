# Problem 7.10 - Count Good Nodes in Binary Tree
# A node is good if no node on the path from root to it has a greater value. Return the number of good nodes in the tree.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Depth First Search
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use DFS to pass down the max value seen so far and count nodes meeting the good condition.
# Time  : O(n)
# Space : O(n)
class TreeNode1:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def goodNodes(self, root):
        def dfs(node, maxVal):
            if not node:
                return 0

            res = 1 if node.val >= maxVal else 0    # Counting node (+1) if it's good, else (+0)
            maxVal = max(maxVal, node.val)          # Updating max value seen so far

            res += dfs(node.left, maxVal)           # Traversing left subtree and updating res for current node as root
            res += dfs(node.right, maxVal)          # Traversing right subtree and updating res for current node as root
            return res                              # res/count = count(node) + count(left subtree) + count(right subtree)

        return dfs(root, root.val)


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Breadth First Search
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use BFS with a queue carrying each node and the max value seen so far along the path.
# Time  : O(n)
# Space : O(n)
from collections import deque

class TreeNode2:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution2:
    def goodNodes(self, root):
        res = 0
        q = deque()
        q.append((root, -float('inf')))                         # Starting with root and negative infinity (root always selected)

        while q:
            node, maxVal = q.popleft()                          # FIFO / level wise (left to right)
            if node.val >= maxVal:                              # Each node carries specific maxVal (not global)
                res += 1                                        # Counting (+1) since good node

            if node.left:
                q.append((node.left, max(maxVal, node.val)))    # Checking left subtree; assigning current maxVal
            if node.right:
                q.append((node.right, max(maxVal, node.val)))   # Checking right subtree; assigning current maxVal

        return res



def main():
    #       3
    #      / \
    #     1   4
    #    /     \
    #   3       5

    node1 = TreeNode1(3,
                      TreeNode1(1, 
                                TreeNode1(3)),
                      TreeNode1(4, 
                                None, TreeNode1(5)))

    node2 = TreeNode2(3,
                      TreeNode2(1, 
                                TreeNode2(3)),
                      TreeNode2(4, 
                                None, TreeNode2(5)))

    print(Solution1().goodNodes(node1))
    print(Solution2().goodNodes(node2))


if __name__ == '__main__':
    main()