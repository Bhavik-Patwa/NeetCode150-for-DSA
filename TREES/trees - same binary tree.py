# Problem 7.5 - Same Binary Tree
# Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Recursive DFS
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Recursively compare current node values and check left and right subtrees for structural and value equality.
# Time  : O(n)
# Space : O(n)
class TreeNode1:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def isSameTree(self, p, q):
        if not p and not q:                     # Both nodes None - Same
            return True
        if p and q and p.val == q.val:          # Both exist and values match - Same, recursing subtrees
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False                        # Structural or Value mismatch


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Iterative DFS
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use stack to iteratively compare pairs of corresponding nodes from both trees.
# Time  : O(n)
# Space : O(n)
class TreeNode2:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution2:
    def isSameTree(self, p, q):
        stack = [(p, q)]                                            # Stack holds pairs of corresponding nodes

        while stack:
            node1, node2 = stack.pop()

            if not node1 and not node2:                             # Both None - Same, moving on
                continue
            if not node1 or not node2 or node1.val != node2.val:    # Structural or Value mismatch
                return False

            stack.append((node1.right, node2.right))                # Pushing right children first
            stack.append((node1.left, node2.left))                  # Pushing left children (checked first)

        return True


# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. Breadth First Search
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use two queues for level-order traversal and compare corresponding nodes.
# Time  : O(n)
# Space : O(n)
from collections import deque

class TreeNode3:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution3:
    def isSameTree(self, p, q):
        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            for _ in range(len(q1)):                        # Checking all nodes at same level
                nodeP = q1.popleft()                        # Checking left to right
                nodeQ = q2.popleft()                        # Checking left to right

                if nodeP is None and nodeQ is None:         # Both None - Same, moving on
                    continue
                if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:
                    return False                            # Structural or Value mismatch

                q1.append(nodeP.left)                       # Enqueueing children (left first)
                q1.append(nodeP.right)
                q2.append(nodeQ.left)                       # Enqueueing children (left first)
                q2.append(nodeQ.right)

        return True



def main():
    # input 1:
    #       1
    #      / \
    #     2   3

    # input 2:
    #       1
    #      / \
    #     2   3

    p1 = TreeNode1(1, 
                   TreeNode1(2), TreeNode1(3))
    q1 = TreeNode1(1, 
                   TreeNode1(2), TreeNode1(3))

    p2 = TreeNode2(1, 
                   TreeNode2(2), TreeNode2(3))
    q2 = TreeNode2(1, 
                   TreeNode2(2), TreeNode2(3))

    p3 = TreeNode3(1, 
                   TreeNode3(2), TreeNode3(3))
    q3 = TreeNode3(1, 
                   TreeNode3(2), TreeNode3(3))

    print(Solution1().isSameTree(p1, q1))
    print(Solution2().isSameTree(p2, q2))
    print(Solution3().isSameTree(p3, q3))


if __name__ == '__main__':
    main()