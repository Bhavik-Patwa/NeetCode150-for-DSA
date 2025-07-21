# Problem 3.2 : Two Integer Sum II
# Given a sorted integer array, return the 1-based indices of two numbers that add up to a target.
# Use O(1) space and ensure index1 < index2.
# Exactly one solution is guaranteed.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Brute Force
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Try every pair of elements to check if their sum equals the target.
# Time  : O(n²)
# Space : O(1)
class Solution1:
    def twoSum(self, numbers, target):
        for i in range(len(numbers)):                       # Checking every pair of elements
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:       # If the pair adds up to the target, returning their 1-based indices
                    return [i + 1, j + 1]
        return []                                           # Bad case fallback


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Binary Search
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Fix one element and binary search for the complement.
# Time  : O(n log n)
# Space : O(1)
class Solution2:
    def twoSum(self, numbers, target):          # Numbers are already sorted
        for i in range(len(numbers)):
            l, r = i + 1, len(numbers) - 1      # Binary search between i + 1 and end
            tmp = target - numbers[i]           # We want numbers[l..r] to contain this value
            while l <= r:
                mid = l + (r - l) // 2          # Standard binary search
                if numbers[mid] == tmp:
                    return [i + 1, mid + 1]
                elif numbers[mid] < tmp:
                    l = mid + 1
                else:
                    r = mid - 1
        return []


# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. Hash Map
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use a dictionary to store previously seen numbers and their indices.
# Time  : O(n)
# Space : O(n)
from collections import defaultdict

class Solution3:
    def twoSum(self, numbers, target):
        mp = defaultdict(int)               # To store number and its 1-based index
        for i in range(len(numbers)):
            tmp = target - numbers[i]       # Complement needed to reach target
            if mp[tmp]:                     # If complement is already seen
                return [mp[tmp], i + 1]     # Returning its index and current index
            mp[numbers[i]] = i + 1          # Storing current number with 1-based index
        return []
    

# ---------------------------------------------------------------------------------------------------------------------------------------
# 4. Two Pointers
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Start with pointers at both ends and move inward based on sum comparison.
# Time  : O(n)
# Space : O(1)
class Solution4:
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1              # Initializing two pointers

        while l < r:
            curSum = numbers[l] + numbers[r]    # Calculating current sum

            if curSum > target:
                r -= 1                          # Sum too big -> move right pointer left to reduce sum
            elif curSum < target:
                l += 1                          # Sum too small -> move left pointer right to increase sum
            else:
                return [l + 1, r + 1]           # Found the correct pair (1-based index)
        return []
    


def main():
    numbers = [2, 3, 4, 6, 9]
    target = 10

    print(Solution1().twoSum(numbers, target))
    print(Solution2().twoSum(numbers, target))
    print(Solution3().twoSum(numbers, target))
    print(Solution4().twoSum(numbers, target))


if __name__ == '__main__':
    main()