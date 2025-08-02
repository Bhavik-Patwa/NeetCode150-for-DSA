# Problem 7.11 - Valid Binary Search Tree
# Return true if the given binary tree is a valid BST, otherwise false.
# A valid BST has all left < current < all right for every node.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Brute Force
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Check at every node if all children in left/right subtree satisfy BST rules using value constraints.
# Time  : O(n²)
# Space : O(n)
class TreeNode1:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    left_check = staticmethod(lambda val, limit : val < limit)              # static methods : global-like (within class) functions without needing class object
    right_check = staticmethod(lambda val, limit : val > limit)             # Lambda functions for BST properties : left < root < right

    def isValidBST(self, root):
        if not root:                                                        # No node : satisfies property
            return True

        if (not self.isValid(root.left, root.val, self.left_check) or       # Checking left and right subtrees 
            not self.isValid(root.right, root.val, self.right_check)):
            return False

        return self.isValidBST(root.left) and self.isValidBST(root.right)   # Checking for each child node, if respective children always satisfy property

    def isValid(self, root, limit, check):                                  # limit = separator value
        if not root:                                                        # No node : satisfies property
            return True
        if not check(root.val, limit):                                      # Checking if property is not satisfied
            return False
        return self.isValid(root.left, limit, check) and self.isValid(root.right, limit, check) # Checking all left and right subtrees


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Depth First Search
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Pass valid value range (left, right) down the tree recursively to ensure all node values are within bounds.
# Time  : O(n)
# Space : O(n)

class TreeNode2:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution2:
    def isValidBST(self, root):
        def valid(node, left, right):
            if not node:                            # No node : satisfies property
                return True
            if not (left < node.val < right):       # Checking if property not satisfied with updated boundaries
                return False

            return valid(node.left, left, node.val) and valid(node.right, node.val, right)  # Updating current node as left/right; Moving to left/right child

        return valid(root, float("-inf"), float("inf"))     # Starting with infinite boundaries


# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. Breadth First Search
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use queue to traverse level-order while carrying down valid value ranges.
# Time  : O(n)
# Space : O(n)
from collections import deque

class TreeNode3:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution3:
    def isValidBST(self, root):
        if not root:
            return True

        q = deque([(root, float("-inf"), float("inf"))])        # Initializing queue with root and infinite boundaries

        while q:
            node, left, right = q.popleft()                     # Checking level-order (left to right)
            if not (left < node.val < right):                   # Checking if property not satisfied with updated boundaries
                return False

            if node.left:
                q.append((node.left, left, node.val))           # Left must be < current
            if node.right:
                q.append((node.right, node.val, right))         # Right must be > current

        return True



def main():
    #       5
    #      / \
    #     3   7
    #    / \   \
    #   2   4   9

    node1 = TreeNode1(5,
                      TreeNode1(3, 
                                TreeNode1(2), TreeNode1(4)),
                      TreeNode1(7, 
                                None, TreeNode1(9)))

    node2 = TreeNode2(5,
                      TreeNode2(3, 
                        TreeNode2(2), TreeNode2(4)),
                      TreeNode2(7, 
                        None, TreeNode2(9)))

    node3 = TreeNode3(5,
                      TreeNode3(3, 
                        TreeNode3(2), TreeNode3(4)),
                      TreeNode3(7, 
                        None, TreeNode3(9)))

    print(Solution1().isValidBST(node1))
    print(Solution2().isValidBST(node2))
    print(Solution3().isValidBST(node3))


if __name__ == '__main__':
    main()