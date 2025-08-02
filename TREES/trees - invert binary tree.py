# Problem 7.1 - Invert Binary Tree
# You are given the root of a binary tree root. Invert the binary tree and return its root.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Breadth First Search
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use a queue to perform level-order traversal and swap left and right children at each node.
# Time  : O(n)
# Space : O(n)
from collections import deque

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
    def invertTree(self, root):
        if not root:
            return None

        queue = deque([root])                               # Initializing queue with root node; deque() requires an iterable hence using [].
        while queue:
            node = queue.popleft()                          # Popping the current (left) node
            node.left, node.right = node.right, node.left   # Swapping left and right children; Python uses temp object behind the scenes
            if node.left:
                queue.append(node.left)                     # Enqueueing left child
            if node.right:
                queue.append(node.right)                    # Enqueueing right child

        return root


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Depth First Search (Recursive)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Recursively swap left and right child nodes during traversal.
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
    def invertTree(self, root):
        if not root:
            return None

        root.left, root.right = root.right, root.left       # Swapping left and right children simultaneously

        self.invertTree(root.left)                          # Recursing on left subtree
        self.invertTree(root.right)                         # Recursing on right subtree

        return root


# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. Iterative DFS
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use a stack to traverse nodes in DFS manner and swap left and right children.
# Time  : O(n)
# Space : O(n)
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
    def invertTree(self, root):
        if not root:
            return None

        stack = [root]                                      # Initializing stack with root node
        while stack:
            node = stack.pop()                              # Popping current (right) node
            node.left, node.right = node.right, node.left   # Swapping left and right children
            if node.left:
                stack.append(node.left)                     # Pushing left child to stack
            if node.right:
                stack.append(node.right)                    # Pushing right child to stack

        return root



def main():
    #       4
    #     /   \
    #    2     7
    #   / \   / \
    #  1   3 6   9

    node1 = TreeNode1(4,
                      TreeNode1(2, 
                                TreeNode1(1), TreeNode1(3)),
                      TreeNode1(7, 
                                TreeNode1(6), TreeNode1(9)))

    node2 = TreeNode2(4,
                      TreeNode2(2, 
                                TreeNode2(1), TreeNode2(3)),
                      TreeNode2(7, 
                                TreeNode2(6), TreeNode2(9)))

    node3 = TreeNode3(4,
                      TreeNode3(2, 
                                TreeNode3(1), TreeNode3(3)),
                      TreeNode3(7, 
                                TreeNode3(6), TreeNode3(9)))

    print(Solution1().invertTree(node1))
    print(Solution2().invertTree(node2))
    print(Solution3().invertTree(node3))


if __name__ == '__main__':
    main()

    # pre-order (root -> left -> right) output
    #       4
    #     /   \
    #    7     2
    #   / \   / \
    #  9   6 3   1
    # 4 -> 7 -> 9 -> None -> None -> 6 -> None -> None -> 2 -> 3 -> None -> None -> 1 -> None -> None
