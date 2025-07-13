# Problem 1.1 : DUPLICATES IN ARRAY  
# Given an integer array nums, return True if any value appears at least twice. Otherwise, return False.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Brute Force
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Comparing each element with every other element.
# Time  : O(n x n) = O(n²)
# Space : O(1)

class Solution1:
    def hasDuplicate(self, nums):
        for i in range(len(nums)):                  # Looping through each number
            for j in range(i + 1, len(nums)):       # Comparing it with all the numbers after it
                if nums[i] == nums[j]:
                    return True                     # Found a duplicate
        return False                                # No duplicates found


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Sorting
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Sorting the array — duplicates (if any) become adjacent.
# Time  : O(n log n)
# Space : O(1) if sorting in-place (else O(n))

class Solution2:
    def hasDuplicate(self, nums):
        nums.sort()                         # Sorting the list first, inplace
        for i in range(len(nums)):
            if nums[i] == nums[i + 1]:
                return True                 # Found a duplicate next to it
        return False


# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. HashSet
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Track seen elements in a set - if found again, return True.
# Time  : O(n)
# Space : O(n)

class Solution3:
    def hasDuplicate(self, nums):
        seen = set()                        # Create an empty set
        for num in nums:
            if num in seen:
                return True                 # Found a duplicate
            seen.add(num)                   # Adding the unseen number to the set
        return False                        # No duplicates


# ---------------------------------------------------------------------------------------------------------------------------------------
# 4. HashSet Length Comparison
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Sets only store unique values -> if duplicates exist, set size < list size
# Time  : O(n)
# Space : O(n)

class Solution4:
    def hasDuplicate(self, nums):
        return len(set(nums)) < len(nums)


# ---------------------------------------------------------------------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------------------------------------------------------------------
def main():
    print("Enter 5 numbers :")
    nums = [input("Enter number : ") for _ in range(5)]
    
    sln1 = Solution1()
    print(sln1.hasDuplicate(nums))
    sln2 = Solution2()
    print(sln2.hasDuplicate(nums))
    sln3 = Solution3()
    print(sln3.hasDuplicate(nums))
    sln4 = Solution4()
    print(sln4.hasDuplicate(nums))


if __name__ == "__main__":
    main()