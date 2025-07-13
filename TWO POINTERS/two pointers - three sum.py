# Problem 3.3 : Three Sum
# Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]] such that 
# i ≠ j ≠ k and nums[i] + nums[j] + nums[k] == 0.
# The output must not contain duplicate triplets.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Brute Force
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Try all triplet combinations and use a set to remove duplicates.
# Time  : O(n³)
# Space : O(n)
class Solution1:
    def threeSum(self, nums):
        res = set()                                         # Using a set to avoid duplicate triplets
        nums.sort()                                         # Sorting the input array

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        tmp = [nums[i], nums[j], nums[k]]
                        res.add(tuple(tmp))                 # Storing as tuple to insert in set

        return [list(t) for t in res]                       # Converting each tuple back to list
    

# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Hash Map + Frequency Count
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Fix the first two numbers and check if the third number exists using a count map.
# Time  : O(n²)
# Space : O(n)
from collections import defaultdict

class Solution2:
    def threeSum(self, nums):
        nums.sort()                                         # Sorting the input array
        count = defaultdict(int)

        for num in nums:                                    # Counting frequency of all numbers
            count[num] += 1

        res = []

        for i in range(len(nums)):                          # Fixing the 1st element
            count[nums[i]] -= 1                             # Using nums[i], so decrementing its count

            if i > 0 and nums[i] == nums[i - 1]:
                continue                                    # Skipping duplicate values

            for j in range(i + 1, len(nums)):               # Fixing the 2nd element
                count[nums[j]] -= 1                         # Using nums[j], so decrementing its count

                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue                                # Skipping duplicate values

                target = -(nums[i] + nums[j])               # Computing the required third value

                if count[target] > 0:                       # If the third value exists
                    res.append([nums[i], nums[j], target])

            for j in range(i + 1, len(nums)):               # Restoring the frequency map for next i
                count[nums[j]] += 1

        return res
    

# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. Two Pointers
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Sort the array and use a fixed element with two pointers to find valid triplets.
# Time  : O(n²)
# Space : O(1)      {ignoring output}
class Solution3:
    def threeSum(self, nums):
        res = []
        nums.sort()                             # Sorting the array to enable two-pointer technique

        for i, a in enumerate(nums):            # Iterating through each element to fix the first value
            if a > 0:
                break                           # Since array is sorted, no further triplets can sum to 0
            if i > 0 and a == nums[i - 1]:
                continue                        # Skipping duplicate values for the fixed element

            l, r = i + 1, len(nums) - 1         # Applying two-pointer approach for the remaining part

            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1                      # Decreasing the sum by moving the right pointer left
                elif threeSum < 0:
                    l += 1                      # Increasing the sum by moving the left pointer right
                else:
                    res.append([a, nums[l], nums[r]])           # Valid triplet found
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:     # Skipping duplicates on the left
                        l += 1

        return res



def main():
    nums = [-1,0,1,2,-1,-4]
    print(Solution1().threeSum(nums))
    print(Solution2().threeSum(nums))
    print(Solution3().threeSum(nums))
    

if __name__ == '__main__':
    main()