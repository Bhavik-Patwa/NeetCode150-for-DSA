# Problem 7.6 - Subtree of Another Tree
# Given the roots of two binary trees root and subRoot, return true if subRoot is a subtree of root, else return false.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Recursive DFS
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Recursively compare each node in root with subRoot and check if they form the same tree.
# Time  : O(m * n) where m = nodes in root, n = nodes in subRoot
# Space : O(n + m)

class TreeNode1:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def isSubtree(self, root, subRoot):
        if not subRoot:                                         # Empty tree is always a subtree
            return True
        if not root:                                            # Empty main tree - no subtree
            return False

        if self.sameTree(root, subRoot):                        # Checking if trees match at current node
            return True

        return (self.isSubtree(root.left, subRoot) or           # Recursing on left subtree
                self.isSubtree(root.right, subRoot))            # Recursing on right subtree

    def sameTree(self, root, subRoot):
        if not root and not subRoot:                            # Both are None - Same
            return True
        if root and subRoot and root.val == subRoot.val:        # Both exist and value is same
            return (self.sameTree(root.left, subRoot.left) and  # Checking subtrees
                    self.sameTree(root.right, subRoot.right))
        return False                                            # Structure or value mismatch


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Serialization And Pattern Matching
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Serialize both trees with marker symbols and use Z-algorithm to detect subRoot in root serialization.
# Time  : O(n + m)
# Space : O(n + m)

class TreeNode2:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution2:
    def serialize(self, root):
        if root == None:
            return "$#"                         # Using $ (not necessary) for end marker and # for null
        return "$" + str(root.val) + self.serialize(root.left) + self.serialize(root.right) # Recursively adding serialized subtrees

    def z_function(self, s):
        z = [0] * len(s)                        # Initializing 0 for z value of each character in serialized combined
        l, r = 0, 0
        for i in range(1, len(s)):              # Matching character pairs in combined; Starting at 1 : avoiding self-matching until '|'
            if i <= r:                          # Reusing z if i inside matched (current) window; else fresh matching
                z[i] = min(r - i + 1, z[i - l]) # Ideally should be count of [i, r] matches or 0 (ignore). [i-l] : index within subroot (self-matched implies minimum value like 0 or 1)
            while i + z[i] < len(s) and s[z[i]] == s[i + z[i]]:     # If previous step implemented : skipping re-matching by intentional mismatching. Else, fresh matching character pairs. 
                z[i] += 1                       # Increasing match count
            if i + z[i] - 1 > r:                # Updating window markers if latest window is larger
                l, r = i, i + z[i] - 1
        return z

    def isSubtree(self, root, subRoot):
        serialized_root = self.serialize(root)                  # Serializing main tree
        serialized_subRoot = self.serialize(subRoot)            # Serializing subtree
        combined = serialized_subRoot + "|" + serialized_root   # Combining serialized subtree and main tree with separator 

        z_values = self.z_function(combined)                    # Calculating z values across combined stream
        sub_len = len(serialized_subRoot)                       # Length of serialized subtree needs to be matched

        for i in range(sub_len + 1, len(combined)):             # Checking z values for main tree (skipping subtree)
            if z_values[i] == sub_len:                          # z value (largest window) at current index matches subtree 
                return True                                     # Match found
        return False                                            # Match not found


def main():
    # Tree:
    #       3
    #      / \
    #     4   5
    #    / \
    #   1   2

    # SubTree:
    #     4 
    #    / \
    #   1   2

    root1 = TreeNode1(3,
                      TreeNode1(4, 
                                TreeNode1(1), TreeNode1(2)),
                      TreeNode1(5))

    subRoot1 = TreeNode1(4,
                         TreeNode1(1), TreeNode1(2))

    root2 = TreeNode2(3,
                      TreeNode2(4, 
                                TreeNode2(1), TreeNode2(2)),
                      TreeNode2(5))

    subRoot2 = TreeNode2(4,
                         TreeNode2(1), TreeNode2(2))


    print(Solution1().isSubtree(root1, subRoot1))
    print(Solution2().isSubtree(root2, subRoot2))


if __name__ == '__main__':
    main()