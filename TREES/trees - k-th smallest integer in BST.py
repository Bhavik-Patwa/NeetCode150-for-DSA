# Problem 7.12 - K-th Smallest Integer in BST
# Given the root of a BST and integer k, return the kth smallest value (1-indexed) in the tree.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Brute Force
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Traverse entire tree and collect all values, sort, and return the kth smallest.
# Time  : O(n log n)
# Space : O(n)
class TreeNode1:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def kthSmallest(self, root, k):
        arr = []                            # Collecting traversed nodes in DFS order

        def dfs(node):
            if not node:
                return
            arr.append(node.val)            # Collecting current node value
            dfs(node.left)                  # Traversing left subtree
            dfs(node.right)                 # Traversing right subtree

        dfs(root)
        arr.sort()                          # Sorting values to find k-th smallest
        return arr[k - 1]                   # Returning k-th smallest value


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Inorder Traversal
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use inorder traversal to collect values in sorted order and return the kth one.
# Time  : O(n)
# Space : O(n)
class TreeNode2:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution2:
    def kthSmallest(self, root, k):
        arr = []                            # Collecting nodes in-order (sorted)

        def dfs(node):
            if not node:
                return
            dfs(node.left)                  # Traversing left subtree first
            arr.append(node.val)            # Backtracking to current node
            dfs(node.right)                 # Traversing right subtree

        dfs(root)
        return arr[k - 1]                   # Returning k-th smallest value


# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. Recursive DFS (Optimal)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use recursive inorder traversal and stop once kth element is found.
# Time  : O(k)
# Space : O(k) for call stack
class TreeNode3:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution3:
    def kthSmallest(self, root, k):
        cnt = k
        res = root.val

        def dfs(node):
            nonlocal cnt, res               # global variables within multiple definitions of dfs()
            if not node:
                return
            dfs(node.left)                  # Traversing left subtree first (in-order/sorted order)
            cnt -= 1                        # Reducing count while k = 0
            if cnt == 0:                    # k-th element reached
                res = node.val              # Taking k-th smallest
                return
            dfs(node.right)                 # Traversing right subtree

        dfs(root)
        return res                          # Returning the k-th smallest element


# ---------------------------------------------------------------------------------------------------------------------------------------
# 4. Iterative DFS (Optimal)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use iterative inorder traversal with stack to avoid recursion.
# Time  : O(k)
# Space : O(h) where h is tree height
class TreeNode4:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution4:
    def kthSmallest(self, root, k):
        stack = []                      # Stacking nodes in in-order
        curr = root

        while stack or curr:
            while curr:                 # Traversing to the leftmost/deepest node
                stack.append(curr)      # Collecting in reverse in-order
                curr = curr.left
            curr = stack.pop()          # Selecting node next in in-order
            k -= 1                      # Reducing count
            if k == 0:
                return curr.val         # Found kth smallest
            curr = curr.right           # Traversing right subtree one node at a time (while prioritizing its left subtree)


# ---------------------------------------------------------------------------------------------------------------------------------------
# 5. Morris Traversal
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use Morris inorder traversal to achieve O(1) space by modifying the tree temporarily.
# Time  : O(k)
# Space : O(1)
class TreeNode5:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution5:
    def kthSmallest(self, root, k):
        curr = root

        while curr:
            if not curr.left:                               # Left child does not exist (no smaller)
                k -= 1                                      # Reducing count for leftmost or next right
                if k == 0:
                    return curr.val                         # k-th element found
                curr = curr.right                           # Checking next greater in right subtree
            else:
                pred = curr.left                            # Left child exists (finding smaller)
                while pred.right and pred.right != curr:    # Traversing to rightmost child (not threading/circling back to current)
                    pred = pred.right

                if not pred.right:                          # Rightmost (pointing to None) in subtree
                    pred.right = curr                       # Linking (thread) rightmost to current : O(1) traceback (eliminates backtracking)
                    curr = curr.left                        # Traversing to next left child
                else:                                       # Rightmost (pointing back to curr) in subtree
                    pred.right = None                       # Removing threaded (reversing to original structure) link
                    k -= 1                                  # Reducing count for rightmost
                    if k == 0:
                        return curr.val                     # k-th smallest found
                    curr = curr.right                       # Traversing up through thread to curr

        return -1                                           # Fallback (should not hit)



def main():
    # pre-order (root -> left -> right) input :
    #       5
    #      / \
    #     3   6
    #    / \
    #   2   4
    #  /
    # 1

    node1 = TreeNode1(5,
                      TreeNode1(3, 
                                TreeNode1(2, TreeNode1(1)), 
                                TreeNode1(4)),
                      TreeNode1(6))

    node2 = TreeNode2(5,
                      TreeNode2(3, 
                                TreeNode2(2, TreeNode2(1)), 
                                TreeNode2(4)),
                      TreeNode2(6))

    node3 = TreeNode3(5,
                      TreeNode3(3, 
                                TreeNode3(2, TreeNode3(1)), 
                                TreeNode3(4)),
                      TreeNode3(6))

    node4 = TreeNode4(5,
                      TreeNode4(3,
                                TreeNode4(2, TreeNode4(1)), 
                                TreeNode4(4)),
                      TreeNode4(6))

    node5 = TreeNode5(5,
                      TreeNode5(3, 
                                TreeNode5(2, TreeNode5(1)), 
                                TreeNode5(4)),
                      TreeNode5(6))

    print(Solution1().kthSmallest(node1, 3))
    print(Solution2().kthSmallest(node2, 3))
    print(Solution3().kthSmallest(node3, 3))
    print(Solution4().kthSmallest(node4, 3))
    print(Solution5().kthSmallest(node5, 3))


if __name__ == '__main__':
    main()