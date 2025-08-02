# Problem 7.3 - Diameter of Binary Tree
# The diameter of a binary tree is the length of the longest path between any two nodes in the tree (measured in edges).


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Brute Force
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : At every node, compute the height of left and right subtrees and return the max diameter among all nodes.
# Time  : O(n²)
# Space : O(n)

class TreeNode1:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def diameterOfBinaryTree(self, root):   # Calculating heights and diameters at each node in top-down; maximum assigned to root/Tree
        if not root:
            return 0

        leftHeight = self.maxHeight(root.left)                  # Height of left subtree
        rightHeight = self.maxHeight(root.right)                # Height of right subtree
        diameter = leftHeight + rightHeight                     # Diameter at current node

        sub = max(self.diameterOfBinaryTree(root.left),         # Max diameter in left subtree
                  self.diameterOfBinaryTree(root.right))        # Max diameter in right subtree

        return max(diameter, sub)                               # Returning the overall maximum

    def maxHeight(self, root):
        if not root:
            return 0
        return 1 + max(self.maxHeight(root.left),               # Height = 1 + max(left, right)
                       self.maxHeight(root.right))


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Depth First Search
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Postorder traversal to get height at each node, and track max diameter using closure.
# Time  : O(n)
# Space : O(n)

class TreeNode2:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution2:
    def diameterOfBinaryTree(self, root):
        res = 0                                                 # Storing max diameter seen so far

        def dfs(node):
            nonlocal res    # Allowing inner dfs() to update and retain shared res across function calls
            if not node:
                return 0

            left = dfs(node.left)                               # Height of left subtree
            right = dfs(node.right)                             # Height of right subtree
            res = max(res, left + right)                        # Updating max diameter overall

            return 1 + max(left, right)                         # Returning height of current node

        dfs(root)
        return res


# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. Iterative DFS
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use stack and memoization to simulate postorder traversal and compute diameter bottom-up.
# Time  : O(n)
# Space : O(n)

class TreeNode3:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution3:
    def diameterOfBinaryTree(self, root):
        stack = [root]                                          # Stack for DFS
        mp = {None : (0, 0)}                                    # Map to store (height, diameter) for each node
                                                                # Height belongs to node, Diameter belongs to tree
        while stack:
            node = stack[-1]                                    # Traversing in DFS (left->right->root) order

            if node.left and node.left not in mp:
                stack.append(node.left)                         # Visiting left subtree first
            elif node.right and node.right not in mp:
                stack.append(node.right)                        # Visiting right subtree next
            else:
                node = stack.pop()                              # Visiting current root (no subtrees left)

                leftHeight, leftDiameter = mp[node.left]        # Getting height/diameter of left subtree
                rightHeight, rightDiameter = mp[node.right]     # Getting height/diameter of right subtree

                height = 1 + max(leftHeight, rightHeight)       # Current node max height
                diameter = max(leftHeight + rightHeight,        # Diameter via current node
                               leftDiameter, rightDiameter)     # Or diameter (longest path) from either subtrees

                mp[node] = (height, diameter)                   # Storing result for current node in map

        return mp[root][1]                                      # Returning only the diameter


def main():
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5

    node1 = TreeNode1(1,
                      TreeNode1(2, 
                                TreeNode1(4), TreeNode1(5)),
                      TreeNode1(3))

    node2 = TreeNode2(1,
                      TreeNode2(2, 
                                TreeNode2(4), TreeNode2(5)),
                      TreeNode2(3))

    node3 = TreeNode3(1,
                      TreeNode3(2, 
                                TreeNode3(4), TreeNode3(5)),
                      TreeNode3(3))

    print(Solution1().diameterOfBinaryTree(node1))
    print(Solution2().diameterOfBinaryTree(node2))
    print(Solution3().diameterOfBinaryTree(node3))


if __name__ == '__main__':
    main()