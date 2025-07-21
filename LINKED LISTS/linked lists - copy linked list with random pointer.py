# Problem 6.6 - Deep Copy of Linked List with Random Pointer
# Given the beginning of a linked list where each node also has a random pointer, create a deep copy of the list.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Recursion + Hash Map
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use recursion with memoization to copy each node and avoid duplication.
# Time  : O(n)
# Space : O(n)

class ListNode1:                                          # Definition for a linked list node with random pointer.
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

    def __str__(self):
        result = []
        curr = self
        while curr:
            rand = curr.random.val if curr.random else "None"
            result.append(f"[{curr.val}, {rand}]")
            curr = curr.next
        return " -> ".join(result) + " -> None"

class Solution1:
    def __init__(self):
        self.map = {}                                  # Global map visible to all deeper function calls

    def copyRandomList(self, head):
        if head is None:
            return None
        if head in self.map:
            return self.map[head]

        copy = ListNode1(head.val, None, None)                      # Create copy
        self.map[head] = copy                          # Memoizing; map = { original_node : copied_node }
        copy.next = self.copyRandomList(head.next)     # Recurse for next
        copy.random = self.map.get(head.random)        # Get copied random
        return copy


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Hash Map (Two Pass)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : First pass to copy nodes, second to assign next and random.
# Time  : O(n)
# Space : O(n)

class ListNode2:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

    def __str__(self):
        result = []
        curr = self
        while curr:
            rand = curr.random.val if curr.random else "None"
            result.append(f"[{curr.val}, {rand}]")
            curr = curr.next
        return " -> ".join(result) + " -> None"

class Solution2:
    def copyRandomList(self, head):
        oldToCopy = {None : None}                               # Mapping original-node : copy-node

        cur = head
        while cur:                                              # Pass 1 : Creating new copies
            oldToCopy[cur] = ListNode2(cur.val, None, None)     # Creating new nodes and copying node values
            cur = cur.next

        cur = head
        while cur:                                              # Pass 2 : Assigning new next and random
            copy = oldToCopy[cur]                               # Copying new node of current node
            copy.next = oldToCopy[cur.next]                     # Copying new node of current's next node
            copy.random = oldToCopy[cur.random]                 # Copying new node of current's random node
            cur = cur.next

        return oldToCopy[head]


# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. Hash Map (One Pass)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use defaultdict to build all nodes and connections in one pass.
# Time  : O(n)
# Space : O(n)

import collections

class ListNode3:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

    def __str__(self):
        result = []
        curr = self
        while curr:
            rand = curr.random.val if curr.random else "None"
            result.append(f"[{curr.val}, {rand}]")
            curr = curr.next
        return " -> ".join(result) + " -> None"

class Solution3:
    def copyRandomList(self, head):
        oldToCopy = collections.defaultdict(lambda : ListNode3(0, None, None))  # Function : node missing -> [0, None, None] -> [val, None, None]; not key : value
        oldToCopy[None] = None                                                  # Handling null references

        cur = head
        while cur:
            oldToCopy[cur].val = cur.val                                        # Assigning value
            oldToCopy[cur].next = oldToCopy[cur.next]                           # Assigning next's new node
            oldToCopy[cur].random = oldToCopy[cur.random]                       # Assigning random's new node
            cur = cur.next

        return oldToCopy[head]


# ---------------------------------------------------------------------------------------------------------------------------------------
# 4. Space Optimized - I
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Interleave copied nodes with originals, fix randoms, then split them.
# Time  : O(n)
# Space : O(1)

class ListNode4:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

    def __str__(self):
        result = []
        curr = self
        while curr:
            rand = curr.random.val if curr.random else "None"
            result.append(f"[{curr.val}, {rand}]")
            curr = curr.next
        return " -> ".join(result) + " -> None"

class Solution4:
    def copyRandomList(self, head):
        if head is None:
            return None

        l1 = head                               # l1 = original nodes ; l2 = copy nodes
        while l1:                               # Creating + appending copies between originals A->A'->B->B', assigning NEXT
            l2 = ListNode4(l1.val, None, None)  # Creating copy of current node
            l2.next = l1.next                   # Current copy -> Next original     A' -> B
            l1.next = l2                        # Current original -> Current copy  A  -> A'
            l1 = l2.next                        # Current = Next of Current Copy A' = Next original B

        l1 = head                               # l1 = original nodes ; l2 = copy nodes
        while l1:                               # Assigning RANDOM
            if l1.random:                       # If original's random != None
                l1.next.random = l1.random.next # {Copy}'s random -> {Original's random}'s Copy ; A->[A'=]->B->B'->C->[=C']
            l1 = l1.next.next                   # Moving to Next original from Current original

        l1 = head
        newHead = head.next                     # head = New copy's head
        while l1:                               # Separating the original and copy flows
            l2 = l1.next                        # Copy = Original's next
            l1.next = l2.next                   # Original's next -> (Copy's next) Next original : A->A'->B => A->B
            if l2.next:                         # If Copy's next exists
                l2.next = l2.next.next          # Copy's next -> Next copy : A'->B->B' => A'->B'
            l1 = l1.next

        return newHead


# ---------------------------------------------------------------------------------------------------------------------------------------
# 5. Space Optimized - II
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Temporarily store copy nodes in original random pointer, then fix all links.
# Time  : O(n)
# Space : O(1)

class ListNode5:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

    def __str__(self):
        result = []
        curr = self
        while curr:
            rand = curr.random.val if curr.random else "None"
            result.append(f"[{curr.val}, {rand}]")
            curr = curr.next
        return " -> ".join(result) + " -> None"

class Solution5:
    def copyRandomList(self, head):
        if head is None:
            return None

        l1 = head
        while l1:                               # Creating copies and using next and random efficiently
            l2 = ListNode5(l1.val, None, None)
            l2.next = l1.random                 # 1. Copy's next -> Original's random : A'->next  ->C
            l1.random = l2                      # 2. Original's random -> it's Copy :   A ->random->A'
            l1 = l1.next                        # 3. Next original = original's next :  A ->next  ->B

        l1 = head
        newHead = head.random                   # Original's random = Copy (new copy's head)
        while l1:                               # Assigning RANDOM
            l2 = l1.random                      # Copy's next -> Original's random : A'->C
            l2.random = l2.next.random if l2.next else None # If RANDOM exists, Copy's random -> (Copy's next) Original's random's random (it's Copy) : A'->C'
            l1 = l1.next

        l1 = head
        while l1:                               # Separating Original and Copy RANDOMS, and assigning NEXT
            l2 = l1.random                      # Copy's next -> Original's random : A'->C
            l1.random = l2.next                 # Original's random -> Original's random's (it's Copy) next (Original random) : A->C
            l2.next = l1.next.random if l1.next else None   # If NEXT exists, Copy' next -> Original's next's (it's Next) random (Next's Copy) : A'->B'
            l1 = l1.next                        # A->B

        return newHead



def main():
    # Creating nodes with random pointers : [['2', None], ['7', 3], ['4', 0], ['5', 1]]
    # Indices : 0:2->None, 1:7->3 , 2:4->0, 3:5->1

    node1d = ListNode1(5, None, None)
    node1c = ListNode1(4, node1d, None)
    node1b = ListNode1(7, node1c, None)
    node1a = ListNode1(2, node1b, None)
    node1a.random = None
    node1b.random = node1d
    node1c.random = node1a
    node1d.random = node1b

    node2d = ListNode2(5, None, None)
    node2c = ListNode2(4, node2d, None)
    node2b = ListNode2(7, node2c, None)
    node2a = ListNode2(2, node2b, None)
    node2a.random = None
    node2b.random = node2d
    node2c.random = node2a
    node2d.random = node2b

    node3d = ListNode3(5, None, None)
    node3c = ListNode3(4, node3d, None)
    node3b = ListNode3(7, node3c, None)
    node3a = ListNode3(2, node3b, None)
    node3a.random = None
    node3b.random = node3d
    node3c.random = node3a
    node3d.random = node3b

    node4d = ListNode4(5, None, None)
    node4c = ListNode4(4, node4d, None)
    node4b = ListNode4(7, node4c, None)
    node4a = ListNode4(2, node4b, None)
    node4a.random = None
    node4b.random = node4d
    node4c.random = node4a
    node4d.random = node4b

    node5d = ListNode5(5, None, None)
    node5c = ListNode5(4, node5d, None)
    node5b = ListNode5(7, node5c, None)
    node5a = ListNode5(2, node5b, None)
    node5a.random = None
    node5b.random = node5d
    node5c.random = node5a
    node5d.random = node5b

    print(Solution1().copyRandomList(node1a))
    print(Solution2().copyRandomList(node2a))
    print(Solution3().copyRandomList(node3a))
    print(Solution4().copyRandomList(node4a))
    print(Solution5().copyRandomList(node5a))


if __name__ == '__main__':
    main()