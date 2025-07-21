# Problem 6.4 - Reorder Linked List
# Given the beginning of a singly linked list head, reorder the list to: [0, n-1, 1, n-2, 2, n-3, ...]


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Brute Force
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Store all nodes in a list and reorder using two-pointer approach.
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
    def reorderList(self, head):
        if not head:
            return

        nodes = []                                      # Storing all nodes in an array
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        i, j = 0, len(nodes) - 1
        while i < j:
            nodes[i].next = nodes[j]                    # Linking ith node to jth node
            i += 1
            if i >= j:
                break
            nodes[j].next = nodes[i]                    # Linking jth node to new ith node
            j -= 1

        nodes[i].next = None                            # Setting the final node's next to None


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Recurursion
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Recururse to the end, and reorder by rearranging links while stack unwinds.
# Time  : O(n)
# Space : O(n)

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
    def reorderList(self, head):

        def recur(root, cur):                       # root, cur acting as left, right
            if not cur:
                return root

            root = recur(root, cur.next)            # Iterating until last node (same root), then recursing
            if not root:
                return None

            tmp = None
            if root == cur or root.next == cur:     # Stopping when root meets or passes cur
                cur.next = None                     # Assigning None to last node
            else:
                tmp = root.next                     # Reordering : L(1) -> R(-1) & R(-1) -> L2 , ...
                root.next = cur                     # root.next to cur/leftmost to corresponding rightmost
                cur.next = tmp                      # cur.next to next original node

            return tmp                              # Returning the next node to continue merging

        head = recur(head, head.next)               # head = None at the end (last node); unused


# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. Reverse And Merge
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Split list in half, reverse second half, and merge alternately.
# Time  : O(n)
# Space : O(1)

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
    def reorderList(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next                            # Moving slow to middle
            fast = fast.next.next                       # Moving fast to end

        second = slow.next                              # Starting of second half
        prev = slow.next = None                         # Breaking the list into two parts

        while second:                                   # Reversing second half
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first, second = head, prev
        while second:                                   # Merging both halves
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2



def main():
    # 0->1->2->3->4
    node1d = ListNode1(4, None)
    node1c = ListNode1(3, node1d)
    node1b = ListNode1(2, node1c)
    node1a = ListNode1(1, node1b)
    head1 = ListNode1(0, node1a)

    # 0->1->2->3->4
    node2d = ListNode2(4, None)
    node2c = ListNode2(3, node2d)
    node2b = ListNode2(2, node2c)
    node2a = ListNode2(1, node2b)
    head2 = ListNode2(0, node2a)

    # 0->1->2->3->4
    node3d = ListNode3(4, None)
    node3c = ListNode3(3, node3d)
    node3b = ListNode3(2, node3c)
    node3a = ListNode3(1, node3b)
    head3 = ListNode3(0, node3a)

    Solution1().reorderList(head1)          # Returned value may be None
    Solution2().reorderList(head2)
    Solution3().reorderList(head3)
    print(head1)                            # But head1 is still node1 and not None
    print(head2)
    print(head3)


if __name__ == '__main__':
    main()