# Problem 6.10 – Merge K Sorted Linked Lists
# Given an array of k sorted linked lists, merge them into one sorted list and return its head.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Brute Force
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Collect all node values, sort them, rebuild a list.
# Time  : O(N log N)               (N = total nodes)
# Space : O(N)
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
    def mergeKLists(self, lists):
        nodes = []
        for head in lists:                  # For each linekd-list, appending all nodes to the list
            while head:
                nodes.append(head.val)
                head = head.next
        nodes.sort()                        # Tim Sorting the list

        dummy = cur = ListNode1()           # Dummy node for pre-starting
        for v in nodes:                     # Creating the final linked list of sorted elements
            cur.next = ListNode1(v)
            cur = cur.next
        return dummy.next


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Iteration (Find-Min Each Round)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Repeatedly pick the smallest current node among k heads.
# Time  : O(k N)                    (worst-case)
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
    def mergeKLists(self, lists):                   # lists : Holding k (each linked list) unchecked nodes
        dummy = cur = ListNode2()
        while True:                                 # Until all nodes are checked
            min_i = -1                              # Index of the minimum of the k linked-list heads
            for i, node in enumerate(lists):
                if node and (min_i == -1 or node.val < lists[min_i].val):   # Finding the current minimum node
                    min_i = i
            if min_i == -1:                         # Empty/all nodes checked
                break
            cur.next = lists[min_i]                 # Appending minimum node to result linked-list
            lists[min_i] = lists[min_i].next        # Replacing minimum node by its next node
            cur = cur.next                          # Current node = Minimum node
        return dummy.next


# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. Merge Lists One-by-One
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Iteratively merge lists[i-1] with lists[i].
# Time  : O(k N)
# Space : O(1)
class ListNode3:
    def __init__(self, val = 0, next = None):
        self.val, self.next = val, next

    def __str__(self):
        out, cur = [], self
        while cur:
            out.append(str(cur.val))
            cur = cur.next
        return " -> ".join(out) + " -> None"

class Solution3:
    def mergeKLists(self, lists):
        if not lists: 
            return None
        for i in range(1, len(lists)):                      # Comparing two linked lists at a time
            lists[i] = self._merge(lists[i - 1], lists[i])  # Merging result into second list, comparing with next, and so on
        return lists[-1]                                    # Last item (head node) is combined result across all linked lists

    def _merge(self, a, b):
        dummy = tail = ListNode3()
        while a and b:
            if a.val <= b.val:                              # Comparing heads of both lists
                tail.next, a = a, a.next                    # Linking smaller to result's tail, and advancing in list 1
            else:
                tail.next, b = b, b.next                    # Linking smaller to result's tail, and advancing in list 2
            tail = tail.next                                # Marking the smaller as current tail
        tail.next = a or b                                  # Only one list has item to compare
        return dummy.next


# ---------------------------------------------------------------------------------------------------------------------------------------
# 4. Min-Heap
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Push first node of each list into a min-heap; pop-min & push its next.
# Time  : O(N log k)
# Space : O(k)
import heapq
class _Wrap:
    def __init__(self, node):                   # Creating an object compatible with heap comparison operations
        self.node = node

    def __lt__(self, other): 
        return self.node.val < other.node.val

class ListNode4:
    def __init__(self, val = 0, next = None):
        self.val, self.next = val, next

    def __str__(self):
        out, cur = [], self
        while cur:
            out.append(str(cur.val))
            cur = cur.next
        return " -> ".join(out) + " -> None"
    
class Solution4:
    def mergeKLists(self, lists):
        heap = [_Wrap(n) for n in lists if n]   # Head node (converting to _Wrap object) from each linked list into heap
        heapq.heapify(heap)                     # Min-Heap of current heap objects : minimum at head
        dummy = cur = ListNode4()
        while heap:                             # While all nodes are checked
            n = heapq.heappop(heap).node        # Getting minimum node and reverting _Wrap object to original node form
            cur.next, cur = n, n                # Appending minimum node to result linked list; Updating current tail node
            if n.next:                          # If next node in respective linked list present, pushing to heap
                heapq.heappush(heap, _Wrap(n.next))
        return dummy.next


# ---------------------------------------------------------------------------------------------------------------------------------------
# 5. Divide & Conquer (Recursion)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Recursively merge pairs of lists (like merge-sort).
# Time  : O(N log k)
# Space : O(log k)               (recursion stack)
class ListNode5:
    def __init__(self, val = 0, next = None):
        self.val, self.next = val, next

    def __str__(self):
        out, cur = [], self
        while cur:
            out.append(str(cur.val))
            cur = cur.next
        return " -> ".join(out) + " -> None"

class Solution5:
    def mergeKLists(self, lists):
        if not lists: 
            return None
        return self._divide(lists, 0, len(lists) - 1)   # Dividing the linked lists to form pairs and merging to get single result

    def _divide(self, lists, l, r):
        if l == r: return lists[l]                      # Single list
        m = (l + r)//2
        return self._merge(self._divide(lists, l, m), self._divide(lists, m + 1, r))    # Recursively dividing+merging to compare pairs, then final merging

    def _merge(self, a, b):
        dummy = tail = ListNode5()
        while a and b:                                  # While both lists have a head node (either not empty)
            if a.val <= b.val:                          # Picking the smaller head
                tail.next, a = a, a.next                # Appending smaller head to result linked list
            else:              
                tail.next, b = b, b.next
            tail = tail.next                            # Updating current tail node
        tail.next = a or b                              # One list is empty, picking head of another
        return dummy.next


# ---------------------------------------------------------------------------------------------------------------------------------------
# 6. Divide & Conquer (Iterative)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Iteratively merge in pairs until one list remains.
# Time  : O(N log k)
# Space : O(1)
class ListNode6:
    def __init__(self, val = 0, next = None):
        self.val, self.next = val, next

    def __str__(self):
        out, cur = [], self
        while cur:
            out.append(str(cur.val))
            cur = cur.next
        return " -> ".join(out) + " -> None"

class Solution6:
    def mergeKLists(self, lists):
        if not lists: 
            return None
        while len(lists) > 1:           # While atleast a pair of linked lists to compare
            merged = []
            for i in range(0, len(lists), 2):       # Comparing all pairs of consecutive linked lists, one at a time
                merged.append(self._merge(lists[i], lists[i + 1] if i + 1 < len(lists) else None))  # Merging pairs and appending result list until possible
            lists = merged                          # Iteratively merging pairs until single result linked list remains
        return lists[0]

    def _merge(self, a, b):
        dummy = tail = ListNode6()
        while a and b:                              # While both lists have a head node (either not empty)
            if a.val <= b.val:                      # Picking the smaller head
                tail.next, a = a, a.next            # Appending smaller head to result linked list
            else:              
                tail.next, b = b, b.next
            tail = tail.next                        # Updating current tail node
        tail.next = a or b                          # One list is empty, picking head of another
        return dummy.next



def main():
    # 1->4->5, 1->3->4, 2->6
    a12 = ListNode1(5)
    a11 = ListNode1(4, a12)
    a10 = ListNode1(1, a11)
    b12 = ListNode1(4)
    b11 = ListNode1(3, b12)
    b10 = ListNode1(1, b11)
    c11 = ListNode1(6)
    c10 = ListNode1(2, c11)
    lists1 = [a10, b10, c10]

    # 1->4->5, 1->3->4, 2->6
    a22 = ListNode1(5)
    a21 = ListNode1(4, a22)
    a20 = ListNode1(1, a21)
    b22 = ListNode1(4)
    b21 = ListNode1(3, b22)
    b20 = ListNode1(1, b21)
    c21 = ListNode1(6)
    c20 = ListNode1(2, c21)
    lists2 = [a20, b20, c20]

    # 1->4->5, 1->3->4, 2->6
    a32 = ListNode1(5)
    a31 = ListNode1(4, a32)
    a30 = ListNode1(1, a31)
    b32 = ListNode1(4)
    b31 = ListNode1(3, b32)
    b30 = ListNode1(1, b31)
    c31 = ListNode1(6)
    c30 = ListNode1(2, c31)
    lists3 = [a10, b10, c30]

    # 1->4->5, 1->3->4, 2->6
    a42 = ListNode1(5)
    a41 = ListNode1(4, a42)
    a40 = ListNode1(1, a41)
    b42 = ListNode1(4)
    b41 = ListNode1(3, b42)
    b40 = ListNode1(1, b41)
    c41 = ListNode1(6)
    c40 = ListNode1(2, c41)
    lists4 = [a40, b40, c40]

    # 1->4->5, 1->3->4, 2->6
    a52 = ListNode1(5)
    a51 = ListNode1(4, a52)
    a50 = ListNode1(1, a51)
    b52 = ListNode1(4)
    b51 = ListNode1(3, b52)
    b50 = ListNode1(1, b51)
    c51 = ListNode1(6)
    c50 = ListNode1(2, c51)
    lists5 = [a50, b50, c50]

    # 1->4->5, 1->3->4, 2->6
    a62 = ListNode1(5)
    a61 = ListNode1(4, a62)
    a60 = ListNode1(1, a61)
    b62 = ListNode1(4)
    b61 = ListNode1(3, b62)
    b60 = ListNode1(1, b61)
    c61 = ListNode1(6)
    c60 = ListNode1(2, c61)
    lists6 = [a60, b60, c60]

    print(Solution1().mergeKLists(lists1))
    print(Solution2().mergeKLists(lists2))
    print(Solution3().mergeKLists(lists3))
    print(Solution4().mergeKLists(lists4))
    print(Solution5().mergeKLists(lists5))
    print(Solution6().mergeKLists(lists6))


if __name__ == "__main__":
    main()