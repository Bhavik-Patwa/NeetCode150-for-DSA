# Problem 7.14 - Binary Tree Maximum Path Sum
# Given a non-empty binary tree, return the maximum path sum of any non-empty path (can start and end at any node).


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Depth First Search
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : At each node, compute the max path through it by summing node + left + right. Traverse entire tree and store max.
# Time  : O(n²)
# Space : O(n)
class TreeNode1:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def maxPathSum(self, root):
        res = -float('inf')                             # Initializing negative Infinity result

        def dfs(node):
            nonlocal res                                # global-like class variable accessible across dfs() iterations
            if not node:                                # No node
                return

            left = self.getMax(node.left)               # Getting max gain from left and right subtrees
            right = self.getMax(node.right)

            res = max(res, node.val + left + right)     # Trying path through current node including both left and right

            dfs(node.left)                              # Checking for each node in the left/right subtrees
            dfs(node.right)

        dfs(root)
        return res                                      # Returning max path observed

    def getMax(self, node):
        if not node:                                    # No node : no path
            return 0
        left = self.getMax(node.left)                   # Calculating for left subtree recursively
        right = self.getMax(node.right)                 # Calculating for right subtree recursively
        path = node.val + max(left, right)              # Forming path with max path value
        return max(0, path)                             # Discarding negative paths


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Depth First Search (Optimal)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use bottom-up DFS to track max gain and update global max by trying left + node + right at every step.
# Time  : O(n)
# Space : O(n)
class TreeNode2:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution2:
    def maxPathSum(self, root):
        res = [root.val]                                        # mutable list[] to hold global max path

        def dfs(node):
            if not node:
                return 0

            leftMax = max(dfs(node.left), 0)                    # Recursively computing max path sum from left/right children
            rightMax = max(dfs(node.right), 0)                  # Only taking positive gains

            res[0] = max(res[0], node.val + leftMax + rightMax) # Updating global result with current root path sum
                                                                # If res was integer variable(not list) : every dfs() iteration creates new
            return node.val + max(leftMax, rightMax)            # Returning max path starting from current node

        dfs(root)
        return res[0]



def main():
    #       -10
    #       /  \
    #      9   20
    #         /  \
    #        15   7

    node1 = TreeNode1(-10, 
                      TreeNode1(9), 
                      TreeNode1(20, 
                                TreeNode1(15), TreeNode1(7)))
    node2 = TreeNode2(-10, 
                      TreeNode2(9), 
                      TreeNode2(20,
                                TreeNode2(15), TreeNode2(7)))
    
    print(Solution1().maxPathSum(node1))
    print(Solution2().maxPathSum(node2))


if __name__ == "__main__":
    main()