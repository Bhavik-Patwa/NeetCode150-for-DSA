# Problem 5.3 - Longest Repeating Character Replacement
# Given a string s and integer k, return the length of the longest substring where you can replace up to k characters to make all characters the same.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Brute Force
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : For each substring, count frequencies and check if the rest can be changed within k replacements.
# Time  : O(n²)         
# Space : O(26) -> O(1)
class Solution1:
    def characterReplacement(self, s, k):               # Make all characters same : Converting all characters to Max Frequency Character
        res = 0
        for i in range(len(s)):                         # For each character i
            count, maxf = {}, 0
            for j in range(i, len(s)):                  # For each window size starting with the character i
                count[s[j]] = 1 + count.get(s[j], 0)    # Counting each char frequency
                maxf = max(maxf, count[s[j]])           # Tracking most frequent char
                if (j - i + 1) - maxf <= k:             # AAABA, 1 : 5 - 4 <= 1 : remaining = WINDOW SIZE - MAX FREQ CHARACTER <= k
                    res = max(res, j - i + 1)           # Updating max window length
        return res


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Sliding Window
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : For each character, expand/shrink window to keep ≤ k mismatches.
# Time  : O(26 * n)
# Space : O(1)
class Solution2:
    def characterReplacement(self, s, k):
        res = 0
        charSet = set(s)                            # Trying to make window all equal to each unique char

        for c in charSet:
            count = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1                      # Counting matching characters

                while (r - l + 1) - count > k:      # If more than k mismatches
                    if s[l] == c:
                        count -= 1
                    l += 1                          # Shrinking from left
                res = max(res, r - l + 1)           # Updating result
        return res


# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. Sliding Window (Optimal)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Track max frequency in window, and allow window size - maxFreq ≤ k.
# Time  : O(n)
# Space : O(1)
class Solution3:
    def characterReplacement(self, s, k):
        count = {}                                  # Frequency map of characters in window
        res = 0
        l = 0
        maxf = 0                                    # Max frequency of any character in current window

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:           # maxf never updated! To maintain O(n). This means invalid strings will also be allowed, but their size would remain small.
                count[s[l]] -= 1                    # Shrinking window from left
                l += 1
            res = max(res, r - l + 1)               # Updating max valid window length
        return res


def main():
    s = "AAABABB"
    k = 1
    print(Solution1().characterReplacement(s, k))
    print(Solution2().characterReplacement(s, k))
    print(Solution3().characterReplacement(s, k))


if __name__ == '__main__':
    main()