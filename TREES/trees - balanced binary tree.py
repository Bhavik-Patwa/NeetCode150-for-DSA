# Problem 7.4 - Balanced Binary Tree
# Given a binary tree, return true if it is height-balanced and false otherwise.
# A height-balanced tree has left and right subtree heights differing by no more than 1 at every node.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Brute Force
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Check height difference at each node and verify recursively for all subtrees.
# Time  : O(n²)
# Space : O(n)
class TreeNode1:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def isBalanced(self, root):
        if not root:
            return True

        left = self.height(root.left)               # Height of left subtree
        right = self.height(root.right)             # Height of right subtree

        if abs(left - right) > 1:                   # If difference between heights exceeds 1 : unbalanced
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)   # Checking subtrees recursively

    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left),      # Height of current node = 1 + max(left subtree, right subtree)
                       self.height(root.right))


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Recursive DFS
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Bottom-up postorder traversal checking height and balance simultaneously.
# Time  : O(n)
# Space : O(n)
class TreeNode2:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution2:
    def isBalanced(self, root):
        def dfs(node):
            if not node:
                return [True, 0]                                # [isBalanced, height]

            left = dfs(node.left)                               # Checking left subtree recursively
            right = dfs(node.right)                             # Checking right subtree recursively
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1    # Checking if current node is balanced

            return [balanced, 1 + max(left[1], right[1])]       # Returning [isBalanced, height] for current node

        return dfs(root)[0]                                     # Returning [isBalanced, height] for tree


# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. Iterative DFS
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Simulate postorder traversal using stack and track subtree heights to validate balance.
# Time  : O(n)
# Space : O(n)
class TreeNode3:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution3:
    def isBalanced(self, root):
        stack = []
        node = root
        last = None                                             # Latest visited node (for backtracking)
        depths = {}                                             # Storing current node/subtree heights

        while stack or node:
            if node:
                stack.append(node)                              # Appending until leaf node in subtree
                node = node.left                                # Traversing left subtree
            else:
                node = stack[-1]
                if not node.right or last == node.right:        # Right subtree empty or backtracking (visited)
                    stack.pop()

                    left = depths.get(node.left, 0)             # Getting height of left subtree (if exists)
                    right = depths.get(node.right, 0)           # Getting height of right subtree (if exists)

                    if abs(left - right) > 1:
                        return False                            # Unbalanced found

                    depths[node] = 1 + max(left, right)         # Storing current node/subtree height
                    last = node                                 # Updating latest visited (for backtracking)
                    node = None                                 # Further nodes visited; backtracking
                else:
                    node = node.right                           # Traversing right subtree

        return True                                             # Balanced



def main():
    #       1
    #      / \
    #     2   2
    #    / 
    #   3  
    #  / 
    # 4

    node1 = TreeNode1(1,
                      TreeNode1(2,
                                TreeNode1(3, 
                                          TreeNode1(4))), 
                      TreeNode1(2))

    node2 = TreeNode2(1,
                      TreeNode2(2,
                                TreeNode2(3, 
                                          TreeNode2(4))), 
                      TreeNode2(2))

    node3 = TreeNode3(1,
                      TreeNode3(2,
                                TreeNode3(3, 
                                          TreeNode3(4))), 
                      TreeNode3(2))

    print(Solution1().isBalanced(node1))
    print(Solution2().isBalanced(node2))
    print(Solution3().isBalanced(node3))


if __name__ == '__main__':
    main()