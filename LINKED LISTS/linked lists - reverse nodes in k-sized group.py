# Problem 6.11 – Reverse Nodes in K-sized Groups  
# Given the head of a linked list, reverse the nodes in groups of size k and return the modified list.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Recursion
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Recursively process the list in k-sized chunks and reverse each chunk.
# Time  : O(N)
# Space : O(N/k) -> due to recursive calls

class ListNode1:
    def __init__(self, val = 0, next = None):
        self.val, self.next = val, next

    def __str__(self):
        out, cur = [], self
        while cur:
            out.append(str(cur.val))
            cur = cur.next
        return " -> ".join(out) + " -> None"

class Solution1:
    def reverseKGroup(self, head, k):
        cur = head                              # Start node for the current group
        group = 0                               # Count of nodes in current group
        while cur and group < k:                # While node exists and number of nodes in group < k
            cur = cur.next
            group += 1

        if group == k:                          # Number of group nodes == k : adding group; else no reversal
            cur = self.reverseKGroup(cur, k)    # Recursing to identify end+1 nodes for all groups (starting node of next group), then reverse linking
            while group > 0:                    # Fixing the next group start node/cur, pre-pending k nodes in order; 1->2->3->4 : 3->2->1->4
                tmp = head.next                 # Setting all middle nodes (tmp is temporary head) aside
                head.next = cur                 # Pre-pending head to start of next group/latest pre-pended node in reverse order
                cur = head                      # Head becomes end of current group (cur)
                head = tmp                      # Preparing head of middle nodes to prepend next
                group -= 1                      # Until k nodes pre-pended to form a group
            head = cur                          # Last pre-pended is the new head of the group
        return head


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Iteration
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use dummy node, iteratively reverse each k-group using pointer manipulation.
# Time  : O(N)
# Space : O(1)

class ListNode2:
    def __init__(self, val = 0, next = None):
        self.val, self.next = val, next

    def __str__(self):
        out, cur = [], self
        while cur:
            out.append(str(cur.val))
            cur = cur.next
        return " -> ".join(out) + " -> None"

class Solution2:
    def reverseKGroup(self, head, k):
        dummy = ListNode2(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)         # Identifying k-th : each group's k-th node which will go as first/head (reversed)
            if not kth:                             # Group size not satisfied : not reversed
                break
            groupNext = kth.next                    # k+1 = end+1 : Start node of next group marking the end of current group

            prev, curr = kth.next, groupPrev.next   # Latest pre-pended node / start of resolved part, start+1 : first node of current group after end of previous group
            while curr != groupNext:                # Until end of group not reached
                tmp = curr.next                     # Temporary head for middle nodes where curr is the head being pre-pended
                curr.next = prev                    # Linking/pre-pending next unresolved head to the latest pre-pended resolved node
                prev = curr                         # Marking current head as the latest pre-pended node
                curr = tmp                          # Preparing temporary head to be pre-pended next

            tmp = groupPrev.next                    # (Unupdated) Pre-reversed head node of group
            groupPrev.next = kth                    # Updating the head node of group as the k-th node (reversed to form group)
            groupPrev = tmp                         # After reversing, new head node of group

        return dummy.next

    def getKth(self, curr, k):                      # Identifying k-th : each group's k-th node which will go as first/head (reversed)
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr



def main():
    k = 3
    # 1->2->3->4->5
    a4 = ListNode1(5)
    a3 = ListNode1(4, a4)
    a2 = ListNode1(3, a3)
    a1 = ListNode1(2, a2)
    a0 = ListNode1(1, a1)

    b4 = ListNode2(5)
    b3 = ListNode2(4, b4)
    b2 = ListNode2(3, b3)
    b1 = ListNode2(2, b2)
    b0 = ListNode2(1, b1)

    print(Solution1().reverseKGroup(a0, k))
    print(Solution2().reverseKGroup(b0, k))


if __name__ == "__main__":
    main()