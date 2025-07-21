# Problem 6.1 - Reverse Linked List
# Given the beginning of a singly linked list head, reverse the list and return the new head.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Recursion
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Recurse to the end and reverse pointers as the stack unwinds.
# Time  : O(n)         
# Space : O(n)
class ListNode1:                                    # Defining singly-linked list node.
    def __init__(self, val = 0, next = None):       # Initializing object of class = new node
        self.val = val
        self.next = next
    
    def __str__(self):                              # Printing an object of class
        result = []
        curr = self
        while curr:
            result.append(str(curr.val))            # Appending nodes to list one by one until next node is None
            curr = curr.next
        return " -> ".join(result) + " -> None"


class Solution1:
    def reverseList(self, head):
        if not head:                                # Empty list
            return None

        newHead = head                              # Processing new node (head)
        if head.next:                               # If there are more nodes
            newHead = self.reverseList(head.next)   # Iterating until no more nodes, then recursing to reverse the order
            head.next.next = head                   # Reversing the link : assigning current to next node 1<-2

        head.next = None                            # Disconnecting current node from next
        return newHead                              # Returning the new head from deepest call


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Iteration
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use two pointers and reverse links in a single pass.
# Time  : O(n)         
# Space : O(1)
class ListNode2:                                        # Defining singly-linked list node.
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
    def reverseList(self, head):
        prev, curr = None, head                         # Initializing previous and current pointers

        while curr:                                     # Traversing until end of list
            temp = curr.next                            # Storing next node
            curr.next = prev                            # Reversing link between next and current(previous) : (Connect+Disconnect)
            prev = curr                                 # Storing current as previous
            curr = temp                                 # Setting next node as new current

        return prev                                     # New head of reversed list



def main():
    # 0->1->2->3
    node1c = ListNode1(3, None)
    node1b = ListNode1(2, node1c)
    node1a = ListNode1(1, node1b)
    head1 = ListNode1(0, node1a)
    # 0->1->2->3
    node2c = ListNode2(3, None)
    node2b = ListNode2(2, node2c)
    node2a = ListNode2(1, node2b)
    head2 = ListNode2(0, node2a)
    print(Solution1().reverseList(head1))
    print(Solution2().reverseList(head2))


if __name__ == '__main__':
    main()