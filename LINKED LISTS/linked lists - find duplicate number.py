# Problem 6.8 - Find the Duplicate Number
# Given an array nums containing n + 1 integers in the range [1, n], return the one number that appears more than once.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Sorting
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Sort the array and check adjacent elements for duplicates.
# Time  : O(n log n)
# Space : O(1) (ignoring sort space cost)

class Solution1:
    def findDuplicate(self, nums):
        nums.sort()                             # Tim sorting the array
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:          # If two adjacent are equal, it's the duplicate
                return nums[i]
        return -1


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Hash Set
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Track seen numbers using a set; return if already present.
# Time  : O(n)
# Space : O(n)

class Solution2:
    def findDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:                     # If already seen, it's a duplicate
                return num
            seen.add(num)
        return -1


# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. Array (Boolean Marker)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use an auxiliary array to track visits by index.
# Time  : O(n)
# Space : O(n)

class Solution3:
    def findDuplicate(self, nums):
        seen = [0] * len(nums)      # Each position represents an integer, not indices
        for num in nums:
            if seen[num - 1]:       # If already marked, it's a duplicate (all integers < n)
                return num
            seen[num - 1] = 1       # Marking as seen (4 marked at nums[3] even if 4 not at nums[3])
        return -1


# ---------------------------------------------------------------------------------------------------------------------------------------
# 4. Negative Marking
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use input array to mark visits by negating elements at target indices.
# Time  : O(n)
# Space : O(1)

class Solution4:
    def findDuplicate(self, nums):      # abs() is necessary, since num at idx is dynamically negated
        for num in nums:
            idx = abs(num) - 1          # Each position represents an integer, not indices
            if nums[idx] < 0:           # Already visited
                return abs(num)
            nums[idx] *= -1             # Marking as visited (negating whatever number present at idx)
        return -1


# ---------------------------------------------------------------------------------------------------------------------------------------
# 5. Binary Search
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Count elements ≤ mid; if count > mid, duplicate must be in left half.
# Time  : O(n log n)
# Space : O(1)

class Solution5:
    def findDuplicate(self, nums):
        low, high = 1, len(nums) - 1                # low/med/high are not pointers for nums like usual Binary Search
        while low < high:                           # Instead, they are pointers in n-integer serach space
            mid = (low + high) // 2
            count = sum(num <= mid for num in nums) # Count of all nums <= mid

            if count <= mid:                        # If duplicate is > mid, count <= mid
                low = mid + 1                       # duplicate > mid : Checking integers greater than mid
            else:                                   # If duplicate is <= mid, count > mid
                high = mid                          # duplicate <= mid : Checking integers smaller than mid

        return low      # low = mid + 1; If duplicate exists, all values > mid will have atleast (values + 1) numbers > value


# ---------------------------------------------------------------------------------------------------------------------------------------
# 6. Bit Manipulation
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : For each bit, count 1s in input and range [1, n]; if more in input, duplicate has that bit.
# Time  : O(n log n)
# Space : O(1)

class Solution6:
    def findDuplicate(self, nums):
        n = len(nums) - 1
        res = 0

        for b in range(32):
            bit_mask = 1 << b                   # Shifting 1 leftward by
            cnt_nums = sum(num & bit_mask != 0 for num in nums)         # Counting (summing Truths) all nums satisfying the bit-mask
            cnt_range = sum(i & bit_mask != 0 for i in range(1, n + 1)) # Counting (summing Truths) integers [1, n+1] usually satisfying bit-mask

            if cnt_nums > cnt_range:            # If duplicate exists, cnt_nums - cnt_range = No. of duplicates
                res |= bit_mask                 # Duplicate has this bit set

        return res


# ---------------------------------------------------------------------------------------------------------------------------------------
# 7. Fast And Slow Pointers (Floyd's Tortoise and Hare)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Treat values as next pointers in a cycle; find intersection, then entry.
# Time  : O(n)
# Space : O(1)

class Solution7:
    def findDuplicate(self, nums):      # Depends highly on the order of numbers, but still worst case O(n)
        slow = fast = 0

        while True:                     # Finding intersection point
            slow = nums[slow]           # Moving one number at a time : 1->3->8
            fast = nums[nums[fast]]     # Moving two numbers (skipping one) at a time : 1->8
            if slow == fast:            # Cycle starts as soon as second duplicate reached
                break                   # Hence, either slow or fast will lead to atleast 1 duplicate

        slow2 = 0
        while True:                     # slow == fast; Taking any, order remains same; slow is step by step
            slow = nums[slow]           # Taking care of duplicate 1 that triggered the cycle
            slow2 = nums[slow2]         # Checking from start if match found
            if slow == slow2:
                return slow



def main():
    nums = [1, 3, 4, 2, 2]
    print(nums)
    print(Solution1().findDuplicate(nums[ : ]))
    print(Solution2().findDuplicate(nums[ : ]))
    print(Solution3().findDuplicate(nums[ : ]))
    print(Solution4().findDuplicate(nums[ : ]))
    print(Solution5().findDuplicate(nums[ : ]))
    print(Solution6().findDuplicate(nums[ : ]))
    print(Solution7().findDuplicate(nums[ : ]))


if __name__ == '__main__':
    main()