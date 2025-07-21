# Problem 4.6 - Time Based Key-Value Store
# Design a data structure that supports storing and retrieving values by key and timestamp, 
# retrieving the most recent value before or at a given timestamp.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Brute Force
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Store a dictionary of timestamps for each key and iterate to find the max timestamp ≤ query time.
# Time  : set : O(1), get : O(n)
# Space : O(n)
class TimeMap:
    def __init__(self):
        self.keyStore = {}                                          # key : {timestamp : [values]}

    def set(self, key, value, timestamp):
        if key not in self.keyStore:                                # key does not exist; creating new
            self.keyStore[key] = {}
        if timestamp not in self.keyStore[key]:                     # key exists, timestamp does not exist; creating new
            self.keyStore[key][timestamp] = []
        self.keyStore[key][timestamp].append(value)                 # key and timestamp exist, appending value at timestamp

    def get(self, key, timestamp):
        if key not in self.keyStore:
            return ""                                               # key does not exist

        seen = 0
        for time in self.keyStore[key]:
            if time <= timestamp:
                seen = max(seen, time)                              # Tracking latest valid timestamp

        return "" if seen == 0 else self.keyStore[key][seen][-1]    # Returning most recent value


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Binary Search (Sorted Map)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use a SortedDict to keep timestamps ordered and apply binary search with bisect_right.
# Time  : set : O(log n), get : O(log n)
# Space : O(n)
from collections import defaultdict
from sortedcontainers import SortedDict

class TimeMap:
    def __init__(self):
        self.keyStore = defaultdict(SortedDict)             # key : SortedDict{timestamp : value}

    def set(self, key, value, timestamp):
        self.keyStore[key][timestamp] = value               # Inserting timestamp -> value

    def get(self, key, timestamp):
        if key not in self.keyStore:
            return ""                                       # Key not present

        timestamps = self.keyStore[key]
        idx = timestamps.bisect_right(timestamp) - 1        # arr.bisect_right(x) returns index after last occurrence of x
                                                            # or returns correct index in sorted arr if no prior existence
        if idx >= 0:
            closest_time = timestamps.iloc[idx]             # Indexing to the correct timestamp at idx
            return timestamps[closest_time]
        return ""                                           # No valid timestamp found


# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. Binary Search (List)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Store [value, timestamp] pairs in a list per key and use binary search over timestamps.
# Time  : set : O(1), get : O(log n)
# Space : O(n)
class TimeMap:
    def __init__(self):
        self.keyStore = {}                                  # key : [value, timestamp]

    def set(self, key, value, timestamp):
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])       # Appending value with timestamp

    def get(self, key, timestamp):
        res, values = "", self.keyStore.get(key, [])        # Getting lists[] of [value, timestamp] at key, else default : []
        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:                   # Checking second element (time) of index m in values[]
                res = values[m][0]                          # Storing first element (value) of index m
                l = m + 1                                   # Searching right half
            else:
                r = m - 1                                   # Searching left half

        return res                                          # Returning most recent valid value



def main():
    tmp = TimeMap()

    tmp.set("alice", "happy", 1)
    print(tmp.get("alice", 1))
    print(tmp.get("alice", 2))
    tmp.set("alice", "sad", 3)
    print(tmp.get("alice", 3))


if __name__ == "__main__":
    main()
