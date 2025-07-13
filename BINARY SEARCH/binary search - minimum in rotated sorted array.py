# Problem 4.4 - Find Minimum in Rotated Sorted Array
# Given a rotated sorted array with unique elements, return the minimum element.
# Rotated Sorted : 123456 -> 345612 (sorted on two sides of a drop/rotation point)


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Brute Force
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use Python’s built-in min() function to find the minimum value.
# Time  : O(n)
# Space : O(1)
class Solution1:
    def findMin(self, nums):
        return min(nums)            # Linear scanning for minimum


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Binary Search
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use binary search to locate the unsorted (rotated) portion, where the minimum must lie.
# Time  : O(log n)
# Space : O(1)
class Solution2:
    def findMin(self, nums):
        res = nums[0]                           # Initializing result with first element
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:               # If current segment is sorted (there is no drop/rotation), the smallest is at the left end
                res = min(res, nums[l])
                break

            m = (l + r) // 2                    # Midpoint
            res = min(res, nums[m])             # Updating result with nums[m]

            if nums[l] <= nums[m]:              # l to m is sorted, hence drop is in right half
                l = m + 1                       # Searching right half
            else:                               # l to m is not sorted, hence drop is in left half
                r = m - 1                       # Searching left half

        return res                              # minimum would be the point after the drop 3456!12


# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. Binary Search (Lower Bound)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Apply lower-bound binary search to narrow down to the minimum element.
# Time  : O(log n)
# Space : O(1)
class Solution3:
    def findMin(self, nums):
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2    # Midpoint
            if nums[m] < nums[r]:   # m to r -> sorted, hence drop -> left half
                r = m               # Minimum is in left half including m
            else:                   # m to r is not sorted, hence l to m is sorted, and drop -> right half
                l = m + 1           # Minimum is in right half excluding m

        return nums[l]              # l == r at the end, pointing to min



def main():
    nums = [3, 4, 5, 6, 1, 2]
    print(nums)
    print(Solution1().findMin(nums))
    print(Solution2().findMin(nums))


if __name__ == '__main__':
    main()