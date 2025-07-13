# Problem 1.2 : 2 STRINGS ANAGRAMS?
# Given two strings s and t, return True if t is an anagram of s, and False otherwise.

# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Hash Map Count (Dictionary)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Build character count/frequency maps for both strings and compare.
# Time  : O(n)
# Space : O(n)

class Solution1:
    def isAnagram(self, s, t):
        if len(s) != len(t):                            # if lengths don't match -> can't be anagrams
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)      # Counting character frequency in s
            countT[t[i]] = 1 + countT.get(t[i], 0)      # Counting character frequency in t

        return countS == countT                         # Comparing both hash maps -> True if identical
    

# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Array based Hash Table
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use an integer array of size 26 (for lowercase a-z) to count frequency differences.
# Time  : O(n)
# Space : O(1) (fixed array)
class Solution2:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        count = [0] * 26                            # Using a single array count of size 26 (for a to z) to track net character frequency.

        for i in range(len(s)):                     # ORDINAL ord(char) returns Unicode (ASCII) integer, e.g. c - a = 99 - 97 = index 2
            count[ord(s[i]) - ord('a')] += 1        # Incrementing for char in s
            count[ord(t[i]) - ord('a')] -= 1        # Decrementing for char in t

        for val in count:                           # If all values are zero, they are anagrams
            if val != 0:
                return False
        return True
    

# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. Sorting
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Sort both strings and compare.
# Time  : O(n log n)
# Space : O(1) or O(n+m) depending on the sorting algorithm.
class Solution3:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)       # Sort both strings -> anagrams if equal
    


# ---------------------------------------------------------------------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------------------------------------------------------------------
def main():
    print("Enter 2 strings : ")
    s = input("String 1 : ")
    t = input("String 2 : ")
    sln1 = Solution1()
    print(sln1.isAnagram(s, t))
    sln2 = Solution2()
    print(sln2.isAnagram(s, t))
    sln3 = Solution3()
    print(sln3.isAnagram(s, t))  


if __name__ == "__main__":
    main()