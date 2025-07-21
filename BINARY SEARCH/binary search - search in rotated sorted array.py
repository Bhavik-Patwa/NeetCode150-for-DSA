# Problem 4.5 - Search in Rotated Sorted Array
# Given a rotated sorted array with unique elements, return the index of the target, or -1 if not found.
# Rotated Sorted : 123456 -> 345612 (sorted on two sides of a drop/rotation point)


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Brute Force
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Linearly scan the array to find the target.
# Time  : O(n)
# Space : O(1)
class Solution1:
    def search(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:                   # Compare each element with target
                return i
        return -1                                   # Return -1 if target not found


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Binary Search (Pivot + Two Binary Searches)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Find rotation pivot, then binary search in both subarrays.
# Time  : O(log n)
# Space : O(1)
class Solution2:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1

        while l < r:                                # Finding the pivot (smallest element after drop)
            m = (l + r) // 2
            if nums[m] > nums[r]:                   # Pivot is in right (unsorted) half
                l = m + 1                           # Moving to check right half
            else:                                   # Pivot is in left (unsorted) half including mid
                r = m                               # Moving to check left half

        pivot = l                                   # Rotation point

        def binary_search(left, right):             # Performing standard binary search in both halves
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        result = binary_search(0, pivot - 1)        # Searching left half
        if result != -1:
            return result

        return binary_search(pivot, len(nums) - 1)  # If not in left, searching right half


# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. Binary Search (Two Pass with Pivot & Direct Range)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Find pivot, then restrict search range based on where target lies.
# Time  : O(log n)
# Space : O(1)
class Solution3:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1

        while l < r:                                        # Finding the pivot
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1                                   # Right side unsorted, pivot is there
            else:
                r = m                                       # Pivot is at or before mid

        pivot = l                                           # Index of smallest value
        l, r = 0, len(nums) - 1

        if target >= nums[pivot] and target <= nums[r]:     # Determining which side to search
            l = pivot                                       # Searching right side
        else:
            r = pivot - 1                                   # Searching left side

        while l <= r:                                       # Standard binary search
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1                                           # Target not found


# ---------------------------------------------------------------------------------------------------------------------------------------
# 4. Binary Search (One Pass)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Modified binary search accounting for rotation while identifying sorted halves.
# Time  : O(log n)
# Space : O(1)
class Solution4:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid                                  # Target found

            if nums[l] <= nums[mid]:                        # Left half is sorted
                if target < nums[l] or nums[mid] < target:  # Target not in left half
                    l = mid + 1                             # Moving to check in right half
                else:
                    r = mid - 1                             # Target in left half

            else:                                           # Right half is sorted
                if target < nums[mid] or target > nums[r]:  # Target not in right half
                    r = mid - 1                             # Moving to check in left half
                else:
                    l = mid + 1                             # Target in right half

        return -1                                           # Not found



def main():
    nums = [3,5,6,0,1,2]
    target = 0
    print(Solution1().search(nums, target))
    print(Solution2().search(nums, target))
    print(Solution3().search(nums, target))
    print(Solution4().search(nums, target))


if __name__ == '__main__':
    main()