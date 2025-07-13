# Problem 5.4 - Permutation in String
# Return True if s2 contains any permutation of s1 as a substring; otherwise return False.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Brute Force
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Sort every substring and compare with sorted s1.
# Time  : O(n² log n)
# Space : O(n)
class Solution1:
    def checkInclusion(self, s1, s2):
        s1 = sorted(s1)                                 # Sorting s1

        for i in range(len(s2)):                        # Checking strings starting with each character
            for j in range(i, len(s2)):
                subStr = s2[i : j + 1]
                subStr = sorted(subStr)                 # Sorting the current substring from s2
                if subStr == s1:                        # Checking if sorted substring equals sorted s1
                    return True
        return False


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Hash Table
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use two hash maps to compare frequency of s1 and substrings of s2.
# Time  : O(n²)
# Space : O(n)
class Solution2:
    def checkInclusion(self, s1, s2):
        count1 = {}
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)        # Frequency map of s1
        
        need = len(count1)
        for i in range(len(s2)):
            count2, cur = {}, 0
            for j in range(i, len(s2)):
                count2[s2[j]] = 1 + count2.get(s2[j], 0)
                if count1.get(s2[j], 0) < count2[s2[j]]:    # Freq[c] in  s1 less than s2
                    break                                   # More c in s2 than s1, or no c in s1 at all
                if count1.get(s2[j], 0) == count2[s2[j]]:
                    cur += 1                                # One character’s frequency matched
                if cur == need:
                    return True                     # All characters matched
        return False


# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. Sliding Window
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use two frequency arrays and compare in-place using a match counter.
# Time  : O(n)
# Space : O(1)
class Solution3:
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):                           # s1 not substring of s2 : Invalid
            return False
        
        s1Count, s2Count = [0] * 26, [0] * 26

        for i in range(len(s1)):                        # Using s1-sized window for s2. Eliminates all other-sized permutations (unwanted)
            s1Count[ord(s1[i]) - ord('a')] += 1         # Frequency map of s1
            s2Count[ord(s2[i]) - ord('a')] += 1         # Frequency map of s1-sized initial window in s2
        
        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1                            # Counting matched character frequencies including 0/absence

        l = 0
        for r in range(len(s1), len(s2)):               # Extending window-end pointer
            if matches == 26:                           # False : 26 - matches = extra c in window + s1 expected c not in window
                return True                             # True : Window = s1
            
            index = ord(s2[r]) - ord('a')               # Checking new c from extension
            s2Count[index] += 1                         ### Adding new c to window
            if s1Count[index] == s2Count[index]:        # New c in window and in s1
                matches += 1                            # Matching
            elif s1Count[index] + 1 == s2Count[index]:  # (Extra present) New c in window but not in s1
                matches -= 1                            # Updating/Removing match count (earlier c in both was equal(0 or more), now +1 in window)

            index = ord(s2[l]) - ord('a')               # Checking/Removing first c in window to maintain window size = s1
            s2Count[index] -= 1                         ### Removing old c from window
            if s1Count[index] == s2Count[index]:        # Extra c from window removed -> equal in s1 and window both
                matches += 1                            # Matching
            elif s1Count[index] - 1 == s2Count[index]:  # (Essential absent) Old c in s1 but not in window
                matches -= 1                            # Updating/Removing match count (earlier c in both was equal(0 or more), now -1 in window) 
            l += 1                                      # Stepping window-start pointer

        return matches == 26                            # Final window check



def main():
    s1 = "abc"
    s2 = "lecabee"
    print(s1)
    print(s2)
    print(Solution1().checkInclusion(s1, s2))
    print(Solution2().checkInclusion(s1, s2))
    print(Solution3().checkInclusion(s1, s2))


if __name__ == '__main__':
    main()