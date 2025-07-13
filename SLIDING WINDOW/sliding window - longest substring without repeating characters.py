# Problem 5.2 - Longest Substring without Repeating Characters
# Find the length of the longest substring in a string s without any repeating characters.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Brute Force
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Try all substrings and check each for uniqueness using a set.
# Time  : O(n²)         
# Space : O(n)
class Solution1:
    def lengthOfLongestSubstring(self, s):
        res = 0
        for i in range(len(s)):                 # Starting with each character
            charSet = set()
            for j in range(i, len(s)):          # Adding for each character until duplicate found
                if s[j] in charSet:
                    break                       # Duplicate found; breaking inner loop
                charSet.add(s[j])
            res = max(res, len(charSet))        # Tracking max unique length
        return res


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Sliding Window
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use a window and a set to maintain unique characters; shrink window if duplicate found.
# Time  : O(n)         
# Space : O(n)
class Solution2:
    def lengthOfLongestSubstring(self, s):
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])        # Removing ALL characters from left until all duplicates removed
                l += 1
            charSet.add(s[r])               # Adding current character
            res = max(res, r - l + 1)       # Updating max length : longest or current window length
        return res


# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. Sliding Window (Optimal)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use a map to remember last seen indices; skip ahead instead of shrinking one-by-one.
# Time  : O(n)        
# Space : O(n)
class Solution3:
    def lengthOfLongestSubstring(self, s):
        mp = {}                             # Stores last seen index of characters
        l = 0                               # Stores window start point, past any duplicates
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(l, mp[s[r]] + 1)    # Moving left pointer past last duplicate index, only moving forward and not backward
            mp[s[r]] = r                    # Updating last seen index
            res = max(res, r - l + 1)       # Updating result with window size
        return res


def main():
    s = "zxyxyz"
    print(s)
    print(Solution1().lengthOfLongestSubstring(s))
    print(Solution2().lengthOfLongestSubstring(s))
    print(Solution3().lengthOfLongestSubstring(s))


if __name__ == '__main__':
    main()