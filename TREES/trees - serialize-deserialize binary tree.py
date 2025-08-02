# Problem 7.15 - Serialize and Deserialize Binary Tree
# Implement an algorithm to convert a binary tree to a string (serialize) and back to the original tree (deserialize).


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Depth First Search
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use preorder DFS traversal to serialize with "N" as null marker, then recursively build during deserialization.
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
                result.append("N")
                return
            result.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(self)
        return " -> ".join(result)

class Solution1:
    def serialize(self, root):
        res = []

        def dfs(node):
            if not node:                                # Empty tree : Null node
                res.append("N")
                return                                  # Returning since no subtrees to check
            res.append(str(node.val))                   # Adding node value to result list
            dfs(node.left)                              # Checking left subtree recursively
            dfs(node.right)                             # Checking right subtree recursively

        dfs(root)
        return ",".join(res)                            # Returning comma separated string result 

    def deserialize(self, data):
        vals = data.split(",")                          # Separating node values
        self.i = 0                                      # For indexing input nodes

        def dfs():
            if vals[self.i] == "N":                     # Skipping Null nodes
                self.i += 1
                return None

            node = TreeNode1(int(vals[self.i]))         # Recreating current node
            self.i += 1
            node.left = dfs()                           # Building left subtree recursively
            node.right = dfs()                          # Building right subtree recrusively
            return node

        return dfs()                                    # Returning result of depth first traversal (root)


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Breadth First Search
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use level-order traversal to serialize tree. During deserialization, assign children using queue and markers.
# Time  : O(n)
# Space : O(n)
from collections import deque

class TreeNode2:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        result = []
        def preorder(node):
            if not node:
                result.append("N")
                return
            result.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(self)
        return " -> ".join(result)

class Solution2:
    def serialize(self, root):
        if not root:                                        # Null node : Empty tree
            return "N"
        res = []
        queue = deque([root])                               # FIFO/level-wise traversal 

        while queue:
            node = queue.popleft()                          # Level-wise left to right traversal
            if not node:                                    # Marking Null node
                res.append("N")
            else:
                res.append(str(node.val))                   # Adding node value to result list
                queue.append(node.left)                     # Collecting left child
                queue.append(node.right)                    # Collecting right child

        return ",".join(res)                                # Returning comma separated string result

    def deserialize(self, data):
        vals = data.split(",")                              # Separating input nodes using commas
        if vals[0] == "N":                                  # Empty tree : Null node
            return None

        root = TreeNode2(int(vals[0]))
        queue = deque([root])                               # FIFO/Level-wise tree building
        index = 1                                           # For indexing serialized input

        while queue:
            node = queue.popleft()                          # Level-wise left to right nodes
            if vals[index] != "N":                          # Adding first Non-Null node as left child / Skipping Null node
                node.left = TreeNode2(int(vals[index]))
                queue.append(node.left)                     # Collecting node to check its children
            index += 1
            if vals[index] != "N":                          # Adding second Non-Null node as left child / Skipping Null node
                node.right = TreeNode2(int(vals[index]))
                queue.append(node.right)                    # Collecting node to check its children
            index += 1

        return root



def main():
    #   1
    #  / \
    # 2   3
    #    / \
    #   4   5
    node1 = TreeNode1(1,
                      TreeNode1(2),
                      TreeNode1(3, 
                                TreeNode1(4), TreeNode1(5)))

    node2 = TreeNode2(1,
                      TreeNode2(2),
                      TreeNode2(3, 
                                TreeNode2(4), TreeNode2(5)))

    s1 = Solution1()
    s2 = Solution2()
    serialized1 = s1.serialize(node1)
    print(serialized1)
    print(s1.deserialize(serialized1))
    serialized2 = s2.serialize(node2)
    print(serialized2)
    print(s2.deserialize(serialized2))


if __name__ == '__main__':
    main()