# Problem 1.9 : Longest Consecutive Sequence of Integers
# Find the length of the longest sequence of consecutive integers in an unsorted array.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Brute Force
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : For each number, check how long the streak can go using a set.
# Time  : O(n²)
# Space : O(n)
class Solution1:
    def longestConsecutive(self, nums):
        longest = 0
        store = set(nums)                       # Storing all elements for fast lookup

        for num in nums:
            streak, curr = 0, num
            while curr in store:                # While the next consecutive number exists
                streak += 1
                curr += 1
            longest = max(longest, streak)      # Updating the longest streak found
        return longest
    

# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Sorting
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Sort the array and count the longest streak of consecutive increasing numbers (skip duplicates).
# Time  : O(nlogn)
# Space : O(n)
class Solution2:
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        
        longest = 0
        nums.sort()                                     # Sorting first to bring sequences together
        
        curr, streak = nums[0], 0
        i = 0
        
        while i < len(nums):
            if curr != nums[i]:                         # If gap or duplicate found, reset tracking
                curr = nums[i]
                streak = 0
            while i < len(nums) and nums[i] == curr:    # Skipping duplicates
                i += 1
            streak += 1                                 # Extending current streak
            curr += 1                                   # Moving to expected next number
            longest = max(longest, streak)              # Updating maximum streak length
        return longest
    

# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. Hash Set
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Only start sequences from numbers that do not have a left neighbor.
# Time  : O(n)
# Space : O(n)
class Solution3:
    def longestConsecutive(self, nums):
        numSet = set(nums)                          # Converting list -> set for fast lookup + remove duplicates
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:             # Checking if num is start of a sequence (no left neighbor)
                length = 1

                while (num + length) in numSet:     # Expanding the sequence to the right as far as possible
                    length += 1

                longest = max(length, longest)      # Updating maximum streak length

        return longest
    

# ---------------------------------------------------------------------------------------------------------------------------------------
# 4. Hash Map
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use a hashmap to track streak boundaries and merge them when new numbers are added.
# Time  : O(n)
# Space : O(n)
from collections import defaultdict

class Solution4:
    def longestConsecutive(self, nums):
        mp = defaultdict(int)                           # Mapping longest streak lengths for each number
        longest = 0

        for num in nums:
            if not mp[num]:                             # Processing only if num is not already seen

                left = mp[num - 1]                      # Getting lengths of sequences adjacent to current number
                right = mp[num + 1]

                mp[num] = left + 1 + right              # Merging sequences and including current number

                mp[num - left] = mp[num]                # Start of the sequence = new streak length (only stored at boundary)
                mp[num + right] = mp[num]               # End of the sequence = new streak length (only stored at boundary)

                longest = max(longest, mp[num])         # Updating longest streak

        return longest
    


def main():
    nums = [1, 4, 2, 100, 3, 200, 4, 150]
    print(nums)
    sln1 = Solution1()
    print(sln1.longestConsecutive(nums))
    sln2 = Solution2()
    print(sln2.longestConsecutive(nums))
    sln3 = Solution3()
    print(sln3.longestConsecutive(nums))
    sln4 = Solution4()
    print(sln4.longestConsecutive(nums))


if __name__ == "__main__":
    main()