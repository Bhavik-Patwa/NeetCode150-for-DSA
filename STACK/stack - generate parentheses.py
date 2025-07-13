# Problem 2.4 - GENERATE PARENTHESES
# Generate all combinations of n pairs of well-formed parentheses.

# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Brute Force
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Generate all 2^(2n) combinations and filter only the valid ones.
# Time  : O(2^2n * n)   {Generating all combinations and validating each}
# Space : O(2^2n * n)   {Storing all valid combinations}
class Solution1:
    def generateParenthesis(self, n):
        res = []

        def valid(s):
            open = 0
            for c in s:
                open += 1 if c == '(' else -1       # '(' : open += 1 , ')' open -= 1
                if open < 0:
                    return False                    # More ')' than '(' at any point -> invalid
            return open == 0                        # Must end with balanced '(' and ')'

        def dfs(s):
            if len(s) == 2 * n:
                if valid(s):                        # Adding only if the string is valid
                    res.append(s)
                return
            
            dfs(s + '(')                            # Try adding '('
            dfs(s + ')')                            # Try adding ')'
        
        dfs("")
        return res


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Backtracking
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Build only valid strings using constraints : open < n and close < open.
# Time  : O(2^n)        {Efficient pruning of invalid paths}
# Space : O(n)          {Stack depth}
class Solution2:
    def generateParenthesis(self, n):
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))          # Valid string complete
                return

            if openN < n:
                stack.append("(")                   # Adding '(' and recurse
                backtrack(openN + 1, closedN)
                stack.pop()                         # Backtracking : important to ensure continued use of stack variable

            if closedN < openN:
                stack.append(")")                   # Adding ')' only if it's valid
                backtrack(openN, closedN + 1)
                stack.pop()                         # Backtracking

        backtrack(0, 0)
        return res


# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. Dynamic Programming
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use recursion + memoization. For each n, combine results of all i and (n-1-i) pairs.
# Time  : O(2^n * n)    {Similar to Catalan number recursion}
# Space : O(2^n * n)    {Memoized combinations}
class Solution3:
    def generateParenthesis(self, n):
        res = [[] for _ in range(n + 1)]    # res[k] stores all valid parentheses with k pairs
        res[0] = [""]                       # Base case

        for k in range(1, n + 1):           # k = number of pairs of brackets [1, n+1] currently being built.
            for i in range(k):              
                for left in res[i]:                 # i     = '(' number of known pairs inside the outer pair ')'
                    for right in res[k - i - 1]:    # k-i-1 = '(' ')' remaining number of known pairs outside the outer pair
                        res[k].append("(" + left + ")" + right)     # Combining and wrapping

        return res[n]


def main():
    n = 2
    print(n)
    print(Solution1().generateParenthesis(n))
    print(Solution2().generateParenthesis(n))
    print(Solution3().generateParenthesis(n))



if __name__ == "__main__":
    main()