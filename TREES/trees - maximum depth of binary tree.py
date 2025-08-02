# Problem 7.2 - Maximum Depth of Binary Tree
# Given the root of a binary tree, return its depth. The depth is the number of nodes along the longest path from root to leaf.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Recursive DFS
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Recursively return max depth of left and right subtree, adding 1 at each level.
# Time  : O(n)
# Space : O(n)
class TreeNode1:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        result = []
        def preorder(node):
            if not node:
                result.append("None")
                return
            result.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(self)
        return " -> ".join(result)

class Solution1:
    def maxDepth(self, root):                                               # Finding depths recursively bottom-up
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) # Depth = 1 + max(left depth, right depth)


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Iterative DFS (Stack)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use a stack with (node, depth) pairs and track max depth manually.
# Time  : O(n)
# Space : O(n)
class TreeNode2:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        result = []
        def preorder(node):
            if not node:
                result.append("None")
                return
            result.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(self)
        return " -> ".join(result)

class Solution2:
    def maxDepth(self, root):                           # Finding depths top-down
        stack = [[root, 1]]                             # Stack stores pairs of (node, depth)
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)                   # Updating max depth
                stack.append([node.left, depth + 1])    # Pushing left child with updated depth
                stack.append([node.right, depth + 1])   # Pushing right child with updated depth

        return res


# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. Breadth First Search
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use level-order traversal and count how many levels exist in the tree.
# Space : O(n)
# Time  : O(n)
from collections import deque

class TreeNode3:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        result = []
        def preorder(node):
            if not node:
                result.append("None")
                return
            result.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(self)
        return " -> ".join(result)

class Solution3:
    def maxDepth(self, root):
        q = deque()
        if root:
            q.append(root)

        level = 0
        while q:                                # Getting children (next level) of all nodes of current level
            for _ in range(len(q)):             # Traversing current level
                node = q.popleft()
                if node.left:
                    q.append(node.left)         # Adding left child to queue
                if node.right:
                    q.append(node.right)        # Adding right child to queue
            level += 1                          # Incrementing depth counter for next level

        return level


def main():
    #       3
    #      / \
    #     9  20
    #        / \
    #       15  7

    node1 = TreeNode1(3,
                      TreeNode1(9),
                      TreeNode1(20, 
                                TreeNode1(15), TreeNode1(7)))

    node2 = TreeNode2(3,
                      TreeNode2(9),
                      TreeNode2(20, 
                                TreeNode2(15), TreeNode2(7)))

    node3 = TreeNode3(3,
                      TreeNode3(9),
                      TreeNode3(20, 
                                TreeNode3(15), TreeNode3(7)))

    print(Solution1().maxDepth(node1))
    print(Solution2().maxDepth(node2))
    print(Solution3().maxDepth(node3))


if __name__ == '__main__':
    main()