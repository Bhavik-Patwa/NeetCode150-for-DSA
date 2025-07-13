# Problem 4.7 - Median of Two Sorted Arrays
# Given two sorted arrays, return the median of the combined sorted array in O(log(min(m, n))) time if possible.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Brute Force
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Merge both arrays, sort the result, and return the median element(s).
# Time  : O((m + n) log(m + n))
# Space : O(m + n)
class Solution1:
    def findMedianSortedArrays(self, nums1, nums2):
        merged = nums1 + nums2                              # Merging arrays
        merged.sort()                                       # Sorting merged array : O(L(log L)) using TimSort
        totalLen = len(merged)

        if totalLen % 2 == 0:
            mid = totalLen // 2
            return (merged[mid - 1] + merged[mid]) / 2.0    # Average of two middle elements
        else:
            return merged[totalLen // 2]                    # Returning the middle element


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Two Pointers
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use two pointers to simulate merging up to the median position without full sort.
# Time  : O(m + n)
# Space : O(1)
class Solution2:
    def findMedianSortedArrays(self, nums1, nums2):
        i = j = 0
        median1 = median2 = 0                           # Storing previous value
        total = len(nums1) + len(nums2)

        for _ in range(total // 2 + 1):
            median2 = median1                           # Storing previous number
            if i < len(nums1) and (j >= len(nums2) or nums1[i] <= nums2[j]):
                median1 = nums1[i]                      # Picking from nums1
                i += 1
            else:
                median1 = nums2[j]                      # Picking from nums2
                j += 1

        if total % 2 == 0:
            return (median1 + median2) / 2.0            # Even length, returning average of two middles
        else:
            return float(median1)                       # Odd length, returning the middle


# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. Binary Search (Recursive K-th Element)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Instead of merged-sorting, focus directly on middle elements. Recursively eliminate k//2 elements (binary logic) until k-th is found.
# Time  : O(log(min(m, n)))
# Space : O(log(min(m, n)))     {Due to recursion}
class Solution3:
    def get_kth(self, a, m, b, n, k, a_start = 0, b_start = 0):         # Finding k-th element in A+B without actually sorting/combining
        if m > n:                                                       # Hypothetically : i eliminated from larger A correctly. j (remaining) referred to smaller B. B might overflow!
            return self.get_kth(b, n, a, m, k, b_start, a_start)        # Ensuring first array is smaller {overflow prevented using min(i, len(A)}. Remaining safely eliminated from larger B

        if m == 0:                                                      # A is empty
            return b[b_start + k - 1]                                   # k-th in B is the k-th element overall
        if k == 1:                                                      # Current smallest -> comparing current first elements of A and B
            return min(a[a_start], b[b_start])                          
                                                                        # k = i + j : eliminate (i) from A or (j) from B, whichever set smaller
        i = min(m, k // 2)                                              # Eliminating k//2 elements, unless len(A) insufficient : preventing overflow
        j = k - i                                                       # Eliminating remaining elements from B; B is larger and always contains atleast k elements

        if a[a_start + i - 1] < b[b_start + j - 1]:                     # If i-th element of A < j-th element of B : remove first i elements of A. Otherwise first j of B
            return self.get_kth(a, m - i, b, n, k - i, a_start + i, b_start)    # Discarding first i elements from A
        else:
            return self.get_kth(a, m, b, n - j, k - j, a_start, b_start + j)    # Discarding first j elements from B

    def findMedianSortedArrays(self, nums1, nums2):
        total = len(nums1) + len(nums2)
        left = (total + 1) // 2                                         # Left middle element
        right = (total + 2) // 2                                        # Right middle element (same if odd)
        return (self.get_kth(nums1, len(nums1), nums2, len(nums2), left) +
                self.get_kth(nums1, len(nums1), nums2, len(nums2), right)) / 2.0


# ---------------------------------------------------------------------------------------------------------------------------------------
# 4. Binary Search (Optimal Partitioning)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Partition arrays so left and right halves are properly balanced.
# Time  : O(log(min(m, n)))
# Space : O(1)
class Solution4:
    def findMedianSortedArrays(self, nums1, nums2):
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2               # Goal : Dividing A+B into 2 equal halves; left half = i + j = right half

        if len(B) < len(A):
            A, B = B, A                 # Ensuring first array is smaller {overflow prevented using min(i, len(A)}. Remaining safely eliminated from larger B

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2            # Partitioning A at i : indices 0 to i in A
            j = half - i - 2            # Partitioning B at j : indices 0 to j in B; remaining (half - i); -2 for zero-indexing

            Aleft = A[i] if i >= 0 else float("-inf")                   # Last element of A's left half. If empty, -oo or oo helps in comparisons later
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")     # First element of A's right half
            Bleft = B[j] if j >= 0 else float("-inf")                   # Last element of B's left half
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")     # First element of B's right half

            if Aleft <= Bright and Bleft <= Aright:                     # Correct Partition : Largest in LEFT half(Aleft, Bleft) <= Smallest in RIGHT half(Bright, Aright)
                if total % 2:                                           # Left half : smaller and equal, Right half : larger and equal
                    return min(Aright, Bright)                          # Odd length, returning middle element
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2    # Even length, returning average
            elif Aleft > Bright:                                        # Incorrect Partition (unsorted) : Reduce A i/left half size : [3,6][9] [1][4,5] -> [3][6,9] [1][4,5]
                r = i - 1                                               # Moving partition left
            else:                                                       # Incorrect Partition (unsorted) : Reduce B i/left half size : [1,4][5] [7][8,9] -> [1,4][5] [-oo][7,8,9]
                l = i + 1                                               # Moving partition right



def main():
    nums1 = [1, 2, 5]
    nums2 = [2, 4, 7]
    print(nums1, nums2)
    print(Solution1().findMedianSortedArrays(nums1, nums2))
    print(Solution2().findMedianSortedArrays(nums1, nums2))
    print(Solution3().findMedianSortedArrays(nums1, nums2))
    print(Solution4().findMedianSortedArrays(nums1, nums2))


if __name__ == '__main__':
    main()