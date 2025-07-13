# Problem 1.6 : ENCODE DECODE STRINGS
# Design a stateless encoding/decoding mechanism to convert a list of strings into a single string and back.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Encoding - Decoding
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : ["abc","de"] -> ["3,2#abcde"] Store the sizes of all strings (separated by commas), followed by #, then concatenate all strings.
# Time  : O(n)
# Space : O(n)
class Solution1:
    def encode(self, strs):
        if not strs:
            return ""
        
        sizes, res = [], ""

        for s in strs:
            sizes.append(len(s))        # Storing lengths of each string in a list

        for sz in sizes:
            res += str(sz)              # Adding sizes to the result string, separated by commas
            res += ','
        res += '#'                      # Delimiter to separate size part from actual strings
        for s in strs:
            res += s                    # Adding all strings concatenated one after another

        return res

    def decode(self, s):
        if not s:
            return []

        sizes, res, i = [], [], 0

        while s[i] != '#':              # Extracting sizes before hitting the '#' character
            cur = ""
            while s[i] != ',':          # Reading one number (could be multi-digit)
                cur += s[i]
                i += 1
            sizes.append(int(cur))      # Converting size to integer
            i += 1                      # Skipping ','

        i += 1                          # Skipping '#'

        for sz in sizes:                # Using the sizes, extract substrings
            res.append(s[i : i + sz])   # Slicing the string by size
            i += sz                     # Moving pointer forward

        return res
    

# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Encoding - Decoding (Optimal)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : ["abc","de"] -> ["3#abc2#de"] Prefix each word with its length and a special delimiter (#) to track where the word starts and ends.
# Time  : O(n)
# Space : O(n)
class Solution2:
    def encode(self, strs):
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s        # For each string, store its length, followed by '#', followed by the string

        return res

    def decode(self, s):
        res = []
        i = 0

        while i < len(s):                       # Decoding by reading the length first, then extracting the word
            j = i

            while s[j] != '#':                  # Finding the next '#' — this separates length from the string
                j += 1

            length = int(s[i : j])              # Converting substring [i : j] to integer (this is the length)

            i = j + 1                           # Moving past '#', extracting [length] characters as a word 
            j = i + length

            res.append(s[i : j])                # Appending extracted word
            i = j                               # Moving pointer to next encoded word

        return res
    


def main():
    strs = ["neetcode", "course", "#150"]
    sln1 = Solution1()
    print(sln1.encode(strs))
    print(sln1.decode(sln1.encode(strs)))
    sln2 = Solution2()
    print(sln2.encode(strs))
    print(sln2.decode(sln2.encode(strs)))


if __name__ == "__main__":
    main()