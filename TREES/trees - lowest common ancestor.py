# Problem 7.7 - Lowest Common Ancestor in Binary Search Tree
# Given a BST and two nodes p and q, return their lowest common ancestor (LCA).


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Recursion
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Traverse down the tree using BST properties until you find the split point between p and q.
# Time  : O(log n) on average (balanced BST), O(n) worst-case (skewed)
# Space : O(n) due to recursive call stack
class TreeNode1:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def lowestCommonAncestor(self, root, p, q):
        if not root or not p or not q:
            return None

        if max(p.val, q.val) < root.val:                            # Say p > q, p < root : q < root.       p and q < root
            return self.lowestCommonAncestor(root.left, p, q)       # LCA lies in left subtree
        elif min(p.val, q.val) > root.val:                          # Say p > q, q < root : q < root.       p and q > root
            return self.lowestCommonAncestor(root.right, p, q)      # LCA lies in right subtree
        else:                                                       # Say p > q, but p > root, q < root.    p : right q : left
            return root                                             # Found the split point (LCA)


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Iteration
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use BST property to move left or right until the split point between p and q is found.
# Time  : O(log n) on average (balanced BST), O(n) worst-case (skewed)
# Space : O(1)
class TreeNode2:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution2:
    def lowestCommonAncestor(self, root, p, q):
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:         # p and q > root
                cur = cur.right                             # LCA lies in right subtree
            elif p.val < cur.val and q.val < cur.val:       # p and q < root
                cur = cur.left                              # LCA lies in left subtree
            else:                                           # p < root and q > root (or vice versa)
                return cur                                  # Found the split point (LCA)



def main():
    #         6
    #       /   \
    #      2     8
    #     / \   / \
    #    0*  4 7   9
    #       / \
    #      3   5*
    # p1 designed separately only for convenience of assigning the 2 intended nodes
    p1 = TreeNode1(2, 
                   TreeNode1(0), 
                   TreeNode1(4, 
                             TreeNode1(3), TreeNode1(5)))
    root1 = TreeNode1(6, 
                      p1, TreeNode1(8, 
                                    TreeNode1(7), TreeNode1(9)))
    nodeP1 = p1.left            # Arbitrary choices
    nodeQ1 = p1.right.right

    p2 = TreeNode2(2, 
                   TreeNode2(0), 
                   TreeNode2(4, 
                             TreeNode2(3), TreeNode2(5)))
    root2 = TreeNode2(6, 
                      p2, TreeNode2(8, 
                                    TreeNode2(7), TreeNode2(9)))
    nodeP2 = p2.left
    nodeQ2 = p2.right.right

    print(Solution1().lowestCommonAncestor(root1, nodeP1, nodeQ1).val)
    print(Solution2().lowestCommonAncestor(root2, nodeP2, nodeQ2).val)


if __name__ == '__main__':
    main()