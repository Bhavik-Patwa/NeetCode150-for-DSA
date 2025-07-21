# Problem 6.3 - Linked List Cycle Detection  
# Given the beginning of a singly linked list head, return True if there is a cycle in the linked list.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Hash Set
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use a set to store visited nodes; if we see a node again, there is a cycle.
# Time  : O(n)         
# Space : O(n)

class ListNode1:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution1:
    def hasCycle(self, head):
        seen = set()                        # Set to store visited nodes
        cur = head

        while cur:
            if cur in seen:                 # If node is already seen, cycle exists
                return True
            seen.add(cur)                   # Adding node to set
            cur = cur.next                  # Moving to next node

        return False                        # Reached end; no cycle


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Fast And Slow Pointers
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use two pointers moving at different speeds; if they meet, a cycle exists.
# Time  : O(n)         
# Space : O(1)

class ListNode2:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution2:
    def hasCycle(self, head):
        slow, fast = head, head             # Initializing two pointers

        while fast and fast.next:
            slow = slow.next                # Moving slow by 1 step
            fast = fast.next.next           # Moving fast by 2 steps

            if slow == fast:                # If they meet, there is a cycle
                return True

        return False                        # If fast reaches end, no cycle



def main():
    # 3 -> 2 -> 0 -> -4 ->cycle-> 2
    node1d = ListNode1(-4)
    node1c = ListNode1(0, node1d)
    node1b = ListNode1(2, node1c)
    node1a = ListNode1(3, node1b)
    node1d.next = node1b                    # Creating cycle
    head1 = node1a

    node2d = ListNode2(-4)
    node2c = ListNode2(0, node2d)
    node2b = ListNode2(2, node2c)
    node2a = ListNode2(3, node2b)
    node2d.next = node2b                    # Creating cycle
    head2 = node2a

    print(Solution1().hasCycle(head1))                
    print(Solution2().hasCycle(head2))                

if __name__ == '__main__':
    main()