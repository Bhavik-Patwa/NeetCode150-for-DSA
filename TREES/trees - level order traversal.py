# Problem 7.8 - Binary Tree Level Order Traversal
# Given a binary tree root, return a nested list representing level order traversal from left to right.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Depth First Search
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use DFS with a depth counter to fill sublists at the corresponding level.
# Time  : O(n)
# Space : O(n)

class TreeNode1:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def levelOrder(self, root):
        res = []

        def dfs(node, depth):
            if not node:
                return None
            if len(res) == depth:
                res.append([])                  # New level, creating sublist

            res[depth].append(node.val)         # Adding current node value to its level
            dfs(node.left, depth + 1)           # Recursively traversing left child
            dfs(node.right, depth + 1)          # Recursively traversing right child

        dfs(root, 0)
        return res


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Breadth First Search
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use a queue to traverse each level and build level-wise lists.
# Time  : O(n)
# Space : O(n)

import collections

class TreeNode2:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution2:
    def levelOrder(self, root):
        res = []
        q = collections.deque()                         # FIFO queue for traversing nodes
        q.append(root)

        while q:
            qLen = len(q)
            level = []                                  # New level list
            for _ in range(qLen):
                node = q.popleft()                      # Checking first element
                if node:
                    level.append(node.val)              # Adding current node value to level
                    q.append(node.left)                 # Enqueueing left child (left to right)
                    q.append(node.right)                # Enqueueing right child
            if level:
                res.append(level)                       # Appending the current level

        return res



def main():
    #       1
    #      / \
    #     2   3
    #    /   / \
    #   4   5   6

    node1 = TreeNode1(1,
                      TreeNode1(2, TreeNode1(4)),
                      TreeNode1(3, TreeNode1(5), TreeNode1(6)))

    node2 = TreeNode2(1,
                      TreeNode2(2, TreeNode2(4)),
                      TreeNode2(3, TreeNode2(5), TreeNode2(6)))

    print(Solution1().levelOrder(node1))
    print(Solution2().levelOrder(node2))


if __name__ == '__main__':
    main()