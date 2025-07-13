# Problem 1.7 : PRODUCT OF ARRAY EXCEPT SELF
# Given an integer array nums, return an array output such that output[i] is the product of all elements of nums except nums[i].

# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Sorting
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : For each index, multiply all other values by skipping the current index.
# Time  : O(n x n) = O(n²)
# Space : O(n)
class Solution1:
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [0] * n               # Initializing result array with zeros

        for i in range(n):
            prod = 1                # Starting fresh for each index, multiplying first element with 1
            for j in range(n):
                if i == j:
                    continue        # Skipping the current index
                prod *= nums[j]     # Multiplying all other elements
            res[i] = prod           # Storing result
        return res
    

# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Division
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Multiply all elements → divide by current index element. (Handle zeroes carefully)
# Time  : O(n)
# Space : O(n)
class Solution2:
    def productExceptSelf(self, nums):
        prod, zero_cnt = 1, 0

        for num in nums:                        # First pass : calculating total product and counting zeroes
            if num:
                prod *= num                     # Only multiply non-zero elements
            else:
                zero_cnt += 1                   # Counting how many zeroes

        if zero_cnt > 1:                        # More than one zero -> all outputs are zero
            return [0] * len(nums)

        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zero_cnt:
                res[i] = 0 if c else prod       # One zero -> only one non-zero result
            else:
                res[i] = prod // c              # Normal case -> divide total product by current element
        return res


# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. Prefix and Suffix
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  :  result[i] = PREFIX[i] × SUFFIX[i] = [product of all elements BEFORE i] x [product of all elements AFTER i]
# Time  : O(n)
# Space : O(n)
class Solution3:
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [0] * n                                   # Final result array
        pref = [0] * n                                  # Prefix product array
        suff = [0] * n                                  # Suffix product array

        pref[0] = 1                                     # Setting neutral values for first prefix and last suffix
        suff[n - 1] = 1

        for i in range(1, n):                           # Building prefix array (left to right) for elements 0 to n-1
            pref[i] = nums[i - 1] * pref[i - 1]

        for i in range(n - 2, -1, -1):                  # Building suffix array (right to left) for elements n-1 to -1
            suff[i] = nums[i + 1] * suff[i + 1]

        for i in range(n):                              # Multiplying prefix and suffix for result
            res[i] = pref[i] * suff[i]

        return res


# ---------------------------------------------------------------------------------------------------------------------------------------
# 4. Prefix and Suffix optimized
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use the output array itself to store prefix products, and then reverse iterate for suffixes.
# Time  : O(n)
# Space : O(1)
class Solution4:
    def productExceptSelf(self, nums):
        res = [1] * len(nums)

        prefix = 1                                      # First pass 0 to N-1 -> storing prefix products
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1                                      # Second pass N-1 to 0 -> multiplying with suffix products
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res



def main():
    nums = [1, 2 , 3, 3, 4, 5, 6]
    sln1 = Solution1()
    print(sln1.productExceptSelf(nums))
    sln2 = Solution2()
    print(sln2.productExceptSelf(nums))
    sln3 = Solution3()
    print(sln3.productExceptSelf(nums))
    sln4 = Solution4()
    print(sln4.productExceptSelf(nums))

if __name__ == "__main__":
    main()