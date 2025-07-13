# Problem 1.3 : SUM OF 2 NUMBERS == TARGET
# Given an array nums and a target, return indices of the two numbers that add up to the target.
# Exactly one solution exists. Cannot use the same element twice.

# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Brute Force
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Check all possible pairs (i, j)
# Time  : O(n x n) = O(n²)
# Space : O(1)
class Solution1:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):       # adding each number with each remaining number in array
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    

# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Sorting + Two Pointers
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Sort a copy of array with indices, use two pointers to find target sum and convert sorted indices back to original
# Time  : O(n log n) (due to sort)
# Space : O(n) (due to index copy)
class Solution2:
    def twoSum(self, nums, target):
        A = [[num, i] for i, num in enumerate(nums)]        # Pairing each number with its index, list of lists
        A.sort()                                            # Sorting by numbers

        i, j = 0, len(A) - 1                                # Using two pointers from both ends
        while i < j:
            cur = A[i][0] + A[j][0]                         # Sum of values at two ends; A[indexing][0->NUM,1->i]
            if cur == target:
                return [A[i][1], A[j][1]]                   # Returning the original indices (not the sorted ones)
            elif cur < target:
                i += 1                                      # Need a larger sum -> move left pointer right
            else:
                j -= 1                                      # Need a smaller sum -> move right pointer left


# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. Hash Map - 2 pass
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : First, map each number to its index, Second, check if the complement exists and isn’t the same element
# Time  : O(n)
# Space : O(n)
class Solution3:
    def twoSum(self, nums, target):
        indices = {}                                        # Creating a hash map storing value -> index
        for i, n in enumerate(nums):
            indices[n] = i                                  # If number is repeated, the latest key is overwritten (safe but not efficient)

        for i, n in enumerate(nums):                        # Iterate again to find if complement exists
            diff = target - n                               # Complement needed to reach target
            if diff in indices and i != indices[diff]:      # Check that we're not using the same element twice
                return [i, indices[diff]]
            
            
# ---------------------------------------------------------------------------------------------------------------------------------------
# 4. Hash Map - 1 pass
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : For each element n, check if target - n exists in hashmap
# Time  : O(n)
# Space : O(n)
class Solution4:
    def twoSum(self, nums, target):
        indices = {}                                # Hash map to store value -> index

        for i, n in enumerate(nums):
            diff = target - n                       # Finding the complement needed to reach target
            if diff in indices:
                return [indices[diff], i]           # Complement exists -> return stored index and current index
            
            indices[n] = i                          # Storing the current number and its index in the hash map
            


# ---------------------------------------------------------------------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------------------------------------------------------------------
def main():
    nums = list(map(int, input("Enter numbers : ").split(" ")))
    target = int(input("Enter target : "))
    print(nums)
    sln1 = Solution1()
    print(sln1.twoSum(nums, target))
    sln2 = Solution2()
    print(sln2.twoSum(nums, target))
    sln3 = Solution3()
    print(sln3.twoSum(nums, target))
    sln4 = Solution4()
    print(sln4.twoSum(nums, target))


if __name__ == "__main__":
    main()
