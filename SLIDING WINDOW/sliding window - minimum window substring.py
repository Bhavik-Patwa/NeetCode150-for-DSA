# Problem 5.5 - Minimum Window Substring
# Return the shortest substring of s that contains all characters of t (including duplicates), or "" if no such substring exists.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Brute Force
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Try all substrings and compare character counts with `t`.
# Time  : O(n² m)
# Space : O(n + m)
class Solution1:
    def minWindow(self, s, t):
        if t == "":
            return ""

        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)                # Frequency of each char in t

        res, resLen = [-1, -1], float("infinity")           
        for i in range(len(s)):                             # Checking all windows stating from current c
            countS = {}
            for j in range(i, len(s)):                      # Checking all window sizes possible
                countS[s[j]] = 1 + countS.get(s[j], 0)      # Building frequency for current substring

                flag = True
                for c in countT:
                    if countT[c] > countS.get(c, 0):        # c appears less than expected in t string
                        flag = False                        # Requirements not met (all expected characters not present)
                        break
               
                if flag and (j - i + 1) < resLen:           # Requirements met & current window length < res
                    resLen = j - i + 1                      # Updating minimum string length
                    res = [i, j]                            # Updating minimum string/window indices

        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""      # Returning minimum acceptable string if found


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Sliding Window
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use frequency maps to expand and contract a window that satisfies the requirements of `t`.
# Time  : O(n)
# Space : O(n + m)
class Solution2:
    def minWindow(self, s, t):
        if t == "":
            return ""

        countT, window = {}, {}                             # countT = expected characters, window = string characters
        for c in t:
            countT[c] = 1 + countT.get(c, 0)                # Frequency of chars in t

        have, need = 0, len(countT)                         
        res, resLen = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):                             # Checking each character in string
            c = s[r]
            window[c] = 1 + window.get(c, 0)                # Adding character to window count

            if c in countT and window[c] == countT[c]:      # If c in target and number of c in target == window
                have += 1                                   # Current character's requirements satisfied : increment have by +1

            while have == need:                             # All characters present
                if (r - l + 1) < resLen:                    # Updating result if smaller window found
                    res = [l, r]                            # Window size
                    resLen = r - l + 1                      # Length of window
                    
                window[s[l]] -= 1                           # Shrinking window from left
                if s[l] in countT and window[s[l]] < countT[s[l]]:      # Left char (being removed) in Target and new frequency less than requirement 
                    have -= 1                               # One required char lost
                l += 1                                      # Shifting window

        l, r = res                                          # Minimum window size
        return s[l : r + 1] if resLen != float("infinity") else ""      # Returning minimum window length if found



def main():
    s = "OUZODYXAZV"
    t = "XYZ"
    print(s)
    print(t)
    print(Solution1().minWindow(s, t))
    print(Solution2().minWindow(s, t))


if __name__ == '__main__':
    main()