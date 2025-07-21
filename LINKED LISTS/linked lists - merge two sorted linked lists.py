# Problem 6.2 - Merge Two Sorted Linked Lists
# Given the heads of two sorted linked lists list1 and list2, merge them into a single sorted list
# consisting of the original nodes, and return the head of the merged list.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Recursion
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Pick the smaller head node, recurse on the rest, and stitch pointers on the way back.
# Time  : O(n + m)      {n = len(list1), m = len(list2)}
# Space : O(n + m)      {call-stack for all nodes}
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
    def mergeTwoLists(self, list1, list2):
        if list1 is None:                           # If either list is exhausted, returning the other
            return list2
        if list2 is None:
            return list1

        if list1.val <= list2.val:                  # Choosing the smaller node
            list1.next = self.mergeTwoLists(list1.next, list2)  # Comparing next two options and assigning next pointer
            return list1                            # Returning the chosen smaller node
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)  # Comparing next two options and assigning next pointer
            return list2                            # Returning the chosen smaller node


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Iteration
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Walk both lists with a pointer, always attaching the smaller current node to the tail.
# Time  : O(n + m)
# Space : O(1)          {in-place merge using existing nodes}
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
    def mergeTwoLists(self, list1, list2):
        dummy = tail = ListNode2()          # Dummy -> head (smallest), tail -> latest (largest) of new merged-list

        while list1 and list2:              # Until one list runs out
            if list1.val < list2.val:
                tail.next = list1           # Choosing smaller node from either lists
                list1 = list1.next          # Advancing in that list
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next                # Advancing the merged-list tail

        tail.next = list1 or list2          # Appending remaining nodes
        return dummy.next                   # Head of merged list (skipping dummy)



def main():
    # 1->2->4
    node1b = ListNode1(4, None)
    node1a = ListNode1(2, node1b)
    head1 = ListNode1(1, node1a)
    # 1->3->5
    node11b = ListNode1(5, None)
    node11a = ListNode1(3, node11b)
    head11 = ListNode1(1, node11a)
    
    # 1->2->4
    node2b = ListNode2(4, None)
    node2a = ListNode2(2, node2b)
    head2 = ListNode2(1, node2a)
    # 1->3->5
    node22b = ListNode2(5, None)
    node22a = ListNode2(3, node22b)
    head22 = ListNode2(1, node22a)
    
    print(Solution1().mergeTwoLists(head1, head11))
    print(Solution2().mergeTwoLists(head2, head22))


if __name__ == '__main__':
    main()