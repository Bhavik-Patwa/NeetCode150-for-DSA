# Problem 1.5 : TOP K FREQUENT ELEMENTS
# Given an integer array nums and an integer k, return the k most frequent elements.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Sorting
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Count elements, sort by frequency and return top k.
# Time  : O(n log n)
# Space : O(n)
class Solution1:
    def topKFrequent(self, nums, k):
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)          # Counting frequency of each element

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])                      # Storing frequency and number as pair (reversing {(n:freq)} -> [freq,n])

        arr.sort()                                      # Sorting by frequency

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])                    # Popping the top k frequent elements
        return res
    

# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Min - Heap
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use a heap to efficiently track and keep only the k most frequent values.
# Time  : O(n log k)
# Space : O(n + k)
import heapq

class Solution2:
    def topKFrequent(self, nums, k):
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)              # Counting frequency of each number

        hp = []
        for num in count.keys():
            heapq.heappush(hp, (count[num], num))           # Building heap of size k, by removing smallest number whenever size > k
            if len(hp) > k:
                heapq.heappop(hp)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(hp)[1])                # Extracting numbers from heap (freq, num)
        return res
    

# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. Bucket Sort
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Group elements by frequency using buckets, then collect top k from highest frequency.
# Time  : O(n)
# Space : O(n)
class Solution3:
    def topKFrequent(self, nums, k):
        count = {}                                      # HashMap of numbers-frequency
        freq = [[] for _ in range(len(nums) + 1)]       # List of lists [[], [], ...] from 0 to n+1 : for buckets of numbers with same frequencies
                                                        # freq : 0th [] will always remain empty, but is helpful for indexing
        for num in nums:
            count[num] = 1 + count.get(num, 0)          # Counting frequency of each number

        for num, cnt in count.items():
            freq[cnt].append(num)                       # Grouping numbers by frequency

        res = []
        for i in range(len(freq) - 1, 0, -1):           # Traversing from highest freq to lowest in descending order (start, stop, step)
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
                


def main():
    nums = [1, 45, 33, 2, 1, 50, 1, 33, 50]
    k = 2
    sln1 = Solution1()
    print(sln1.topKFrequent(nums, k))
    sln2 = Solution2()
    print(sln2.topKFrequent(nums, k))
    sln3 = Solution3()
    print(sln3.topKFrequent(nums, k))


if __name__ == "__main__":
    main()