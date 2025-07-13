# Problem 3.1 : Valid Palindrome
# Given a string s, return True if it is a palindrome (reads the same backward and forward), 
# ignoring non-alphanumeric characters and case.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Reverse String
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Filter the string to include only lowercase alphanumerics, then compare it with its reversed version.
# Time  : O(n)
# Space : O(n)          {copy pasting new string for comparison}
class Solution1:
    def isPalindrome(self, s):
        newStr = ''
        for c in s:
            if c.isalnum():                     # Keeping only alphanumeric characters
                newStr += c.lower()             # Converting to lowercase and appending
        return newStr == newStr[ : : -1]        # Check if the cleaned string is same as its reverse
    

# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Two Pointers
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use two pointers from both ends, skipping non-alphanumerics and compare characters in-place.
# Time  : O(n)
# Space : O(1)          {inplace transformation and comparison}
class Solution2:
    def isPalindrome(self, s):
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):    # Skipping left non-alphanumeric
                l += 1
            while r > l and not self.alphaNum(s[r]):    # Skipping right non-alphanumeric
                r -= 1
            if s[l].lower() != s[r].lower():            # Comparing lowercase characters
                return False
            l, r = l + 1, r - 1                         # Moving pointers inward
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))



def main():
    s = "Was it a car or a cat I saw?"
    print(s)
    print(Solution1().isPalindrome(s))
    print(Solution2().isPalindrome(s))


if __name__ == '__main__':
    main()