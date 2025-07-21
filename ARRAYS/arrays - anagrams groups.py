# Problem 1.4 - GROUPING ANAGRAM STRINGS
# Given an array of strings, group all anagrams together.
# Two strings are anagrams if their characters can be rearranged to form each other.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Sorting
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Two anagrams have the same sorted form. Use the sorted version as the key in a hashmap.
# Time  : O(n log n)        {Sorting each string}
#		  O(m × n log n)    {For m strings}
# Space : O(m × n)
from collections import defaultdict

class Solution1:
    def groupAnagrams(self, strs):
        res = defaultdict(list)             # Allows directly appending values to dictionary (implicitly checks key exists? creates if not)
        
        for s in strs:
            sortedS = ''.join(sorted(s))    # Sorting the string (e.g. 'eat' -> 'a' 'e' 't' -> 'aet') and using it as a KEY

            res[sortedS].append(s)          # Appending the original string to the list mapped to the sorted key
            
        return list(res.values())           # Returning all grouped anagrams as a list of lists


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Hash Table using Character Count
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Count the frequency of each letter (a – z). Use this 26-length count as a tuple key.
# Time  : O(n)        {Counting each string}
#		  O(m × n)    {For m strings}
# Space : O(m × n)
class Solution2:
    def groupAnagrams(self, strs):
        res = defaultdict(list)                     # default dictionary = append values directly without checking if the key exists

        for s in strs:
            count = [0] * 26                        # Initializing a count array of size 26 for each lowercase letter

            for ch in s:
                count[ord(ch) - ord('a')] += 1      # Ordinal indexing (a = 0, b = 1, ...)

            res[tuple(count)].append(s)             # Converting count (list to tuple) so it can be used as a dict key
                                                    # Appending original string, hence grouping anagrams (same count tuples) strings together
        
        return list(res.values())                   # Returning all grouped anagrams as a list of lists



def main():
    strs = list(input("Enter strings using commas (no spaces/quotation marks) : ").split(","))
    sln1 = Solution1()
    print(sln1.groupAnagrams(strs))
    sln2 = Solution2()
    print(sln2.groupAnagrams(strs))

if __name__ == "__main__":
    main()