# Problem 7.13 - Construct Binary Tree from Preorder and Inorder Traversal
# Given preorder and inorder traversal of a tree with unique values, construct the original binary tree.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Depth First Search
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Recursively build the tree using the first value of preorder as root and its index in inorder to split subtrees.
# Time  : O(n²)
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
    def buildTree(self, preorder, inorder):                         # preorder : root[0]->left[1:mid+1]->right[mid+1:] ; inorder : left[:mid]->root[mid]->right[mid+1:]
        if not preorder or not inorder:                             # No node/children
            return None

        root = TreeNode1(preorder[0])                               # First element of preorder is root
        mid = inorder.index(preorder[0])                            # Finding root in inorder. root splits inorder into left/right subtrees
        root.left = self.buildTree(preorder[1 : mid + 1],           # Left subtree from preorder slice (just after root)
                                   inorder[ : mid])                 # Left subtree from inorder slice (before root)
        root.right = self.buildTree(preorder[mid + 1 : ],           # Right subtree from preorder slice (after root)
                                    inorder[mid + 1 : ])            # Right subtree from inorder slice (after root)

        return root                                                 # Returning current node with its subtrees


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Hash Map + Depth First Search
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use hashmap to store inorder indices for fast access and recursively build tree in O(n) time.
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
    def buildTree(self, preorder, inorder):
        indices = {val: idx for idx, val in enumerate(inorder)} # Map for quick index lookup
        self.pre_idx = 0

        def dfs(l, r):
            if l > r:                                           # Out of expected range : no node exists
                return None

            rval = preorder[self.pre_idx]                       # Current node value in preorder sequence (left subtree then right)
            self.pre_idx += 1                                   # Indexing to next node in preorder sequence
            root = TreeNode2(rval)                              # Creating current/root node
            mid = indices[rval]                                 # Inorder index of root : root separates left/right subtrees
            root.left = dfs(l, mid - 1)                         # Building left subtree : [start, root]
            root.right = dfs(mid + 1, r)                        # Building right subtree : [root, end]
            return root

        return dfs(0, len(inorder) - 1)


# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. Depth First Search (Optimal)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use a DFS with stopping condition tied to inorder traversal's next expected value.
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
    def buildTree(self, preorder, inorder):
        preIdx = inIdx = 0                          # preIdx : track order of next nodes to create 
                                                    # inIdx : cross-check next expected node/if subtree boundary reached
        def dfs(limit):                             # limit (parent node) is compared with the next inorder element
            nonlocal preIdx, inIdx                  # global-like variables within class, accessible across dfs() iterations
            if preIdx >= len(preorder):             # All elements in preorder covered
                return None
            if inorder[inIdx] == limit:             # Equal : the inorder element has not changed (still same parent node) : No Children
                inIdx += 1
                return None

            root = TreeNode3(preorder[preIdx])      # Creating new node from preorder
            preIdx += 1                             # Moving to next unseen preorder element
            root.left = dfs(root.val)               # Checking left subtree using current node as limit/parent
            root.right = dfs(limit)                 # Checking right subtree using current's parent node limit/parent
            return root

        return dfs(float('inf'))                    # Starting with Infinity to allow first inorder element as root



def main():
    preorder = [3, 9, 20, 15, 7]                        # root -> left -> right
    inorder = [9, 3, 15, 20, 7]                         # left -> root -> right

    tree1 = Solution1().buildTree(preorder, inorder)
    tree2 = Solution2().buildTree(preorder, inorder)
    tree3 = Solution3().buildTree(preorder, inorder)

    print(tree1)
    print(tree2)
    print(tree3)

    # Output
    #       3
    #      / \
    #     9   20
    #         / \
    #        15  7


if __name__ == '__main__':
    main()