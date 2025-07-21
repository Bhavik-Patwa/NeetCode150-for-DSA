# Problem 6.7 - Add Two Numbers
# Given two non-empty linked lists l1 and l2 that represent non-negative integers in reverse order,
# return their sum as a linked list (also in reverse order).


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Recursion
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Recurse through both lists carrying the overflow; create nodes on the way back.
# Time  : O(max(m, n))          (m, n = lengths of l1, l2)
# Space : O(max(m, n))          (recursion stack)

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
    def _add(self, l1, l2, carry):
        if not l1 and not l2 and carry == 0:            # Base : Nothing left to add
            return None

        v1 = l1.val if l1 else 0                        # Current digit from l1
        v2 = l2.val if l2 else 0                        # Current digit from l2
        carry, val = divmod(v1 + v2 + carry, 10)        # Returning quotient(% = carry) and remainder(// = sum)

        next_node = self._add(                          # Recursing for next digits
            l1.next if l1 else None,
            l2.next if l2 else None,
            carry
        )
        return ListNode1(val, next_node)                # Building nodes in reverse

    def addTwoNumbers(self, l1, l2):
        return self._add(l1, l2, 0)


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Iteration
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Walk both lists with a running carry, appending digits to a dummy head.
# Time  : O(max(m, n))
# Space : O(1)                  (output list not counted)

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
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode2()                             # Dummy head to start
        cur = dummy
        carry = 0

        while l1 or l2 or carry:                        # Continuing while digits/carry remain
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            carry, val = divmod(v1 + v2 + carry, 10)    # Computing carry (quotient) and value (remainder)
            cur.next = ListNode2(val)                   # Appending value node to new linked list

            cur = cur.next                              # Advancing pointers
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next                               # Returning head of new linked list



def main():
    # 2->4->3 + 5->6->4 => 7->0->8
    a3 = ListNode1(3, None)
    a2 = ListNode1(4, a3)
    a1 = ListNode1(2, a2)

    b3 = ListNode1(4, None)
    b2 = ListNode1(6, b3)
    b1 = ListNode1(5, b2)

    # 2->4->3 + 5->6->4 => 7->0->8
    c3 = ListNode2(3, None)
    c2 = ListNode2(4, c3)
    c1 = ListNode2(2, c2)

    d3 = ListNode2(4, None)
    d2 = ListNode2(6, d3)
    d1 = ListNode2(5, d2)

    print(Solution1().addTwoNumbers(a1, b1))
    print(Solution2().addTwoNumbers(c1, d1))


if __name__ == '__main__':
    main()