# Problem 5.6 - Sliding Window Maximum
# Given an array nums and integer k, return a list of the maximum elements from every contiguous subarray of size k.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Brute Force
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Slide the window and compute max by scanning each subarray.
# Time  : O(n * k)
# Space : O(n)
class Solution1:
    def maxSlidingWindow(self, nums, k):
        output = []

        for i in range(len(nums) - k + 1):          # Window start = 0 to as long as window fits
            maxi = nums[i]
            for j in range(i, i + k):               # Checking each element of each window
                maxi = max(maxi, nums[j])           # Finding max in current window
            output.append(maxi)                     # List of window wise maximums

        return output


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Segment Tree
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use segment tree for fast range max queries.
# Time  : O(n + n log n)
# Space : O(n)
class SegmentTree:
    def __init__(self, N, A):
        self.n = N
        while (self.n & (self.n - 1)) != 0:
            self.n += 1
        self.build(N, A)

    def build(self, N, A):
        self.tree = [float('-inf')] * (2 * self.n)
        for i in range(N):
            self.tree[self.n + i] = A[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = max(self.tree[i << 1], self.tree[i << 1 | 1])

    def query(self, l, r):
        res = float('-inf')
        l += self.n
        r += self.n + 1
        while l < r:
            if l & 1:
                res = max(res, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res = max(res, self.tree[r])
            l >>= 1
            r >>= 1
        return res

class Solution2:
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        segTree = SegmentTree(n, nums)
        output = []
        for i in range(n - k + 1):
            output.append(segTree.query(i, i + k - 1))
        return output


# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. Heap
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Push into max-heap and remove out-of-bound values.
# Time  : O(n log k)
# Space : O(k)
import heapq
class Solution3:
    def maxSlidingWindow(self, nums, k):
        heap = []
        output = []

        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))         # Using negative for max-heap (parent <= binary children)

            if i >= k - 1:                              # Window size atleast k
                while heap[0][1] <= i - k:              # Top/Max index should be within current window [i - k], else pop
                    heapq.heappop(heap)                 
                output.append( - heap[0][0])            # Appending max value
        return output


# ---------------------------------------------------------------------------------------------------------------------------------------
# 4. Dynamic Programming
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Precompute max to the left and right in each block.
# Time  : O(n)
# Space : O(n)
class Solution4:
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        leftMax = [0] * n
        rightMax = [0] * n

        leftMax[0] = nums[0]                                    # First and Last are independent
        rightMax[n - 1] = nums[n - 1]

        for i in range(1, n):                                   # Comparing pairs from second element : i-1 ? i
            if i % k == 0:                                      # Index at window boundary (Start)
                leftMax[i] = nums[i]                            # independent of previous
            else:
                leftMax[i] = max(leftMax[i - 1], nums[i])       # Comparing with previous within window

            j = n - 1 - i                                       # Comparing pairs from second-last element : j ? j+1
            if j % k == (k - 1):                                # Index at window boundary (End)
                rightMax[j] = nums[j]                           # Independent of next
            else:
                rightMax[j] = max(rightMax[j + 1], nums[j])     # Comparing with next within window

        output = [0] * (n - k + 1)                              # Creating as many number of windows possible
        for i in range(n - k + 1):
            output[i] = max(rightMax[i], leftMax[i + k - 1])    # 253 -> 255 & 553 -> 555
        return output


# ---------------------------------------------------------------------------------------------------------------------------------------
# 5. Deque
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Maintain deque with useful indices for max, and slide window.
# Time  : O(n)
# Space : O(k)
from collections import deque
class Solution5:
    def maxSlidingWindow(self, nums, k):
        output = []
        q = deque()                                 # Stores indices in FIFO
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:      # Current greater -> removing all previous smaller
                q.pop()                             # Removing smaller elements from right/back
            q.append(r)                             # Adding current element to right

            if l > q[0]:                            # Element out-of-window (before window start/l)
                q.popleft()                         # Removing oldest elements out-of-window from left/front

            if (r + 1) >= k:                        # Minimum/higher index for required window size
                output.append(nums[q[0]])           # Front has index of max element for current window
                l += 1                              # Sliding window start ahead
            r += 1                                  # Extending window ahead

        return output



def main():
    nums = [1, 2, 1, 0, 4, 2, 6]
    k = 3
    print(nums)
    print(Solution1().maxSlidingWindow(nums, k))
    print(Solution2().maxSlidingWindow(nums, k))
    print(Solution3().maxSlidingWindow(nums, k))
    print(Solution4().maxSlidingWindow(nums, k))
    print(Solution5().maxSlidingWindow(nums, k))


if __name__ == '__main__':
    main()