# Problem 4.1 - Binary Search
# Search for a target in a sorted array of distinct integers. Return its index or -1 if not found.

# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Recursive Binary Search
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use recursion to divide search range in half at each step.
# Time  : O(log n)
# Space : O(log n)      {Due to recursive call stack}
class Solution1:
    def binary_search(self, l, r, nums, target):
        if l > r:
            return -1                                           # Bad case : target not found

        m = l + (r - l) // 2                                    # Mid index (prevents overflow)

        if nums[m] == target:
            return m                                            # Target found

        if nums[m] < target:
            return self.binary_search(m + 1, r, nums, target)   # Searching right half

        return self.binary_search(l, m - 1, nums, target)       # Searching left half

    def search(self, nums, target):
        return self.binary_search(0, len(nums) - 1, nums, target)


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Iterative Binary Search
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use a loop to repeatedly divide the range in half.
# Time  : O(log n)
# Space : O(1)
class Solution2:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2                            # Mid index

            if nums[m] > target:
                r = m - 1                                   # Searching left
            elif nums[m] < target:
                l = m + 1                                   # Searching right
            else:
                return m                                    # Target found

        return -1                                           # Target not found


# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. Upper Bound Binary Search
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Find first element greater than target, then check element before it.
# Time  : O(log n)
# Space : O(1)
class Solution3:
    def search(self, nums, target):
        l, r = 0, len(nums)

        while l < r:
            m = l + ((r - l) // 2)

            if nums[m] > target:                            # Target is less than Mid
                r = m                                       # Upper bound = Mid : Searching left half
            else:
                l = m + 1                                   # Moving right

        return l - 1 if l and nums[l - 1] == target else -1 # After loop, l is upper bound index -> checking previous index nums[l - 1]


# ---------------------------------------------------------------------------------------------------------------------------------------
# 4. Lower Bound Binary Search
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Find first index where nums[i] >= target, then verify if it's a match.
# Time  : O(log n)
# Space : O(1)
class Solution4:
    def search(self, nums, target):
        l, r = 0, len(nums)

        while l < r:
            m = l + ((r - l) // 2)

            if nums[m] >= target:                               # Target is less than/equal to Mid
                r = m                                           # Upper bound = Mid : Searching left half
            else:
                l = m + 1                                       # Searching right

        return l if l < len(nums) and nums[l] == target else -1 # After loop, l is lower bound index -> checking if nums[l] is the target


# ---------------------------------------------------------------------------------------------------------------------------------------
# 5. Built-in Function (bisect)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use Python's bisect module to find insertion point, then check if it matches target.
# Time  : O(log n)
# Space : O(1)
import bisect                                       # Inserting or locating positions in a list so that the list would remain sorted
class Solution5:
    def search(self, nums, target):
        index = bisect.bisect_left(nums, target)    # bisect_left(arr, x) -> first index where x could go or already is/first occurrence
                                                    # bisect_right(arr, x) -> first index where x would go after existing x’s/last occurrence
        return index if index < len(nums) and nums[index] == target else -1


def main():
    nums = [-1, 0, 3, 4, 6, 8]
    target = 6

    print(Solution1().search(nums[ : ], target))
    print(Solution2().search(nums[ : ], target))
    print(Solution3().search(nums[ : ], target))
    print(Solution4().search(nums[ : ], target))
    print(Solution5().search(nums[ : ], target))

if __name__ == "__main__":
    main()