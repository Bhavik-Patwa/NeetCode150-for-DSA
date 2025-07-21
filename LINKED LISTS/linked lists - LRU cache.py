# Problem 6.9 – LRU Cache
# Design an LRU (Least Recently Used) cache of fixed capacity that supports :
# - get(key) -> value (or –1 if absent)  
# - put(key, value) -> insert/update, evicting the least-recently-used item when full  


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Brute Force (List)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Maintain a list ordered from least- to most-recent; scan for key on each access.
# Time  : O(n) per get/put
# Space : O(n)

class LRUCache1:
    def __init__(self, capacity):                       # LRU, MRU = Least/Most Recently Used item
        self.cap = capacity
        self.cache = []                                 # [[key, val], …]

    def get(self, key):
        for i, (k, v) in enumerate(self.cache):
            if k == key:                                # Found (now MRU)
                self.cache.append(self.cache.pop(i))    # Popping and Appending : Putting the key at end/Most Recent
                return v
        return -1

    def put(self, key, value):
        for i, (k, _) in enumerate(self.cache):
            if k == key:                                # Key already exists
                self.cache.pop(i)                       # Removing existing before appending new at end/MRU
                break
            elif len(self.cache) == self.cap:           # Evicting LRU before appending new at end/MRU
                self.cache.pop(0)
        self.cache.append([key, value])                 # Inserting MRU


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Doubly Linked List + Hash Map
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Hash-map key → node for O(1) lookup; doubly linked list keeps usage order for O(1) eviction.
# Time  : O(1) per get/put
# Space : O(n)

class _Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache2:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}                                     # key -> node
        self.left, self.right = _Node(0, 0), _Node(0, 0)    # Sentinels : left = LRU (start), right = MRU (end)
        self.left.next = self.right                         # Initially : left <- -> right
        self.right.prev = self.left                         # left.prev -> right ; left <- right.prev

    def _remove(self, node):                                # Unlinking a node
        p, n = node.prev, node.next                         # Getting current prev and next of node
        p.next, n.prev = n, p                               # Skipping the node (linking prev <- -> next)

    def _insert(self, node):                                # Inserting/Appending before right (MRU end)
        p, n = self.right.prev, self.right                  # Getting second last(before right) and last nodes (right)
        p.next = n.prev = node                              # Linking to node   : Second-last -> node <- Last/right
        node.prev, node.next = p, n                         # Linking node with : Second-last <- node -> Last/right

    def get(self, key):
        if key not in self.cache:                           # Node not present
            return -1
        node = self.cache[key]
        self._remove(node)                                  # Removing already existing node
        self._insert(node)                                  # Appending node newly to MRU/right end
        return node.val

    def put(self, key, value):
        if key in self.cache:                               # Removing already existing node
            self._remove(self.cache[key])
        self.cache[key] = _Node(key, value)                 
        self._insert(self.cache[key])                       # Appending node newly to MRU/right end

        if len(self.cache) > self.cap:                      # Capacity exceeded
            lru = self.left.next
            self._remove(lru)                               # Evicting LRU (first node after left)
            del self.cache[lru.key]


# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. Built-in OrderedDict
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use collections.OrderedDict which remembers insertion order; move_to_end gives O(1) updates.
# Time  : O(1) amortized per get/put
# Space : O(n)

from collections import OrderedDict

class LRUCache3:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = OrderedDict()              # key -> value; FIFO order preserved unless explicitly arranged

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)             # Moving the key to last/right end/MRU
        return self.cache[key]                  # Returning the value

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)         # Moving the key to last/right end/MRU, before over-writing
        self.cache[key] = value                         
        if len(self.cache) > self.cap:          # Capacity reached : Popping item at the front/first in FIFO
            self.cache.popitem(last = False)


def main():
    lru1 = LRUCache1(2)
    lru1.put('A', 1)
    lru1.put('B', 2)
    print(lru1.get('A'))  
    lru1.put('C', 3)
    print(lru1.get('B'))

    lru2 = LRUCache2(2)
    lru2.put('A', 1)
    lru2.put('B', 2)
    print(lru2.get('A'))
    lru2.put('C', 3)
    print(lru2.get('B'))

    lru3 = LRUCache3(2)
    lru3.put('A', 1)
    lru3.put('A', 2)
    print(lru3.get('A'))
    lru3.put('C', 3)
    print(lru3.get('B'))


if __name__ == '__main__':
    main()