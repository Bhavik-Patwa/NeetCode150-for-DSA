# Problem 6.5 - Remove k-th Node From End of Linked List
# Given the beginning of a singly linked list head and integer n, remove the nth node from the end and return the head.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Brute Force
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Store all nodes in a list and delete the (len - n)th node.
# Time  : O(n)
# Space : O(n)

class ListNode1:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

    def __str__(self):
        result = []
        curr = self
        while curr:
            result.append(str(curr.val))
            curr = curr.next
        return " -> ".join(result) + " -> None"

class Solution1:
    def removeNthFromEnd(self, head, k):
        nodes = []                                      # Storing nodes in array
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        removeIndex = len(nodes) - k                    # Index of node to be removed from the end
        if removeIndex == 0:
            return head.next                            # Removing head

        nodes[removeIndex - 1].next = nodes[removeIndex].next       # Skipping and assigning new link
        return head


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Iteration (Two Pass)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : First pass to get length, second to remove (len - n)th node.
# Time  : O(n)
# Space : O(1)

class ListNode2:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

    def __str__(self):
        result = []
        curr = self
        while curr:
            result.append(str(curr.val))
            curr = curr.next
        return " -> ".join(result) + " -> None"

class Solution2:
    def removeNthFromEnd(self, head, k):
        N = 0
        cur = head
        while cur:                                      # First pass : Finding length
            N += 1
            cur = cur.next

        removeIndex = N - k                             # Index to be removed from end
        if removeIndex == 0:
            return head.next                            # Removing head

        cur = head
        for i in range(N - 1):                          # Second pass : Iterating and Deleting node
            if (i + 1) == removeIndex:
                cur.next = cur.next.next
                break
            cur = cur.next

        return head


# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. Recursion
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Recurse to the end and count back while unwinding to remove nth node.
# Time  : O(n)
# Space : O(n)

class ListNode3:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

    def __str__(self):
        result = []
        curr = self
        while curr:
            result.append(str(curr.val))
            curr = curr.next
        return " -> ".join(result) + " -> None"

class Solution3:
    def recur(self, head, k):
        if not head:
            return None

        head.next = self.recur(head.next, k)        # Iterating until last node, then recurring
        k[0] -= 1                                   # Counting till k-th index; k[0] = number in k[]
        if k[0] == 0:                               
            return head.next                        # Skipping the k-th node
        return head                                 # Returning current node as is

    def removeNthFromEnd(self, head, k):
        return self.recur(head, [k])                # Passing k as list element : same k across calls (mutable)
                                                    # Using k : each recursive call gets a new copy of k


# ---------------------------------------------------------------------------------------------------------------------------------------
# 4. Two Pointers
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use two pointers with gap of n nodes to find and remove the nth node from end.
# Time  : O(n)
# Space : O(1)

class ListNode4:                                        # Definition for singly-linked list.
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

    def __str__(self):
        result = []
        curr = self
        while curr:
            result.append(str(curr.val))
            curr = curr.next
        return " -> ".join(result) + " -> None"

class Solution4:
    def removeNthFromEnd(self, head, k):
        dummy = ListNode4(0, head)          # Dummy node pointing to head/start node
        left = dummy
        right = head

        while k > 0:                        # Moving right pointer k steps ahead, while left stays at 0
            right = right.next
            k -= 1

        while right:                        # Moving both pointers (n-k steps) until right reaches end
            left = left.next                # Left (starts at 0) reaches removeIndex - 1, when
            right = right.next              # Right (starts at k) reaches end

        left.next = left.next.next          # Deleting the kth node from end using re-linking
        return dummy.next                   # Returning new head



def main():
    k = 2
    # 0->1->2->3->4
    node1d = ListNode1(4, None)
    node1c = ListNode1(3, node1d)
    node1b = ListNode1(2, node1c)
    node1a = ListNode1(1, node1b)
    head1 = ListNode1(0, node1a)

    node2d = ListNode2(4, None)
    node2c = ListNode2(3, node2d)
    node2b = ListNode2(2, node2c)
    node2a = ListNode2(1, node2b)
    head2 = ListNode2(0, node2a)

    node3d = ListNode3(4, None)
    node3c = ListNode3(3, node3d)
    node3b = ListNode3(2, node3c)
    node3a = ListNode3(1, node3b)
    head3 = ListNode3(0, node3a)

    node4d = ListNode4(4, None)
    node4c = ListNode4(3, node4d)
    node4b = ListNode4(2, node4c)
    node4a = ListNode4(1, node4b)
    head4 = ListNode4(0, node4a)

    print(Solution1().removeNthFromEnd(head1, k))
    print(Solution2().removeNthFromEnd(head2, k))
    print(Solution3().removeNthFromEnd(head3, k))
    print(Solution4().removeNthFromEnd(head4, k))


if __name__ == '__main__':
    main()