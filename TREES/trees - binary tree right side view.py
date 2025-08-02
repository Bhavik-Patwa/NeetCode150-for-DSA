# Problem 7.9 - Binary Tree Right Side View
# Given the root of a binary tree, return the values of nodes visible from the right side (top to bottom).


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Depth First Search
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Traverse right before left and record the first node seen at each level.
# Time  : O(n)
# Space : O(n)
class TreeNode1:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def rightSideView(self, root):
        res = []

        def dfs(node, depth):
            if not node:
                return None
            if depth == len(res):           # Only one node per depth (starts at 0) 
                res.append(node.val)        # Adding first node seen at this depth

            dfs(node.right, depth + 1)      # Prioritizing right child
            dfs(node.left, depth + 1)       # Then left child

        dfs(root, 0)
        return res


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Breadth First Search
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Traverse level by level and record the last node seen at each level.
# Time  : O(n)
# Space : O(n)
from collections import deque

class TreeNode2:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution2:
    def rightSideView(self, root):
        res = []
        q = deque([root])

        while q:
            rightSide = None                    # Tag for current level right view node
            qLen = len(q)

            for _ in range(qLen):
                node = q.popleft()              # Traversing FIFO level wise (left to right)
                if node:
                    rightSide = node            # Tracking the last traversed node at this level
                    q.append(node.left)         # Adding left first
                    q.append(node.right)        # Then right

            if rightSide:
                res.append(rightSide.val)       # Adding the last node’s value to result

        return res



def main():
    #       1
    #    /     \
    #   2       3
    #    \     /
    #     5   4

    node1 = TreeNode1(1,
                      TreeNode1(2, None, TreeNode1(5)),
                      TreeNode1(3, TreeNode1(4), None))

    node2 = TreeNode2(1,
                      TreeNode2(2, None, TreeNode2(5)),
                      TreeNode2(3, TreeNode2(4), None))

    print(Solution1().rightSideView(node1))
    print(Solution2().rightSideView(node2))


if __name__ == '__main__':
    main()