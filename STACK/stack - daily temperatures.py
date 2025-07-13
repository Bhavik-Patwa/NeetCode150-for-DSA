# Problem 2.5 - DAILY TEMPERATURES
# Given a list of daily temperatures, return a list that tells how many days to wait until a warmer temperature.

# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Brute Force
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : For each day, check all future days to find the next warmer temperature.
# Time  : O(n²)
# Space : O(n)
class Solution1:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        res = []

        for i in range(n):
            count = 1
            j = i + 1
            while j < n:
                if temperatures[j] > temperatures[i]:       # Found warmer day
                    break
                j += 1
                count += 1
            count = 0 if j == n else count                  # No warmer day found
            res.append(count)
        return res


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Stack
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use a monotonic decreasing stack to keep track of indices. When a warmer day is found, update the result.
# Time  : O(n)
# Space : O(n)
class Solution2:
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)                      
        stack = []                                          # Stack stores (temp, index)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:               # Current temp is warmer than stack top
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd                # Days to wait = current index - stack index
            stack.append((t, i))                            # Pushing current temp and index
        return res


# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. Dynamic Programming
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Start from the end. Use precomputed results to jump ahead instead of checking every day.
# Time  : O(n)
# Space : O(n)
class Solution3:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        res = [0] * n

        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:     # Jumping ahead using previously stored results
                if res[j] == 0:                                     # No warmer day exists for j
                    j = n
                    break
                j += res[j]                                         # Using already computed days from next day for current
            if j < n:
                res[i] = j - i                                      # Storing how many days to wait
        return res


def main():
    temperatures = [30,38,30,36,35,40,28]
    print(temperatures)
    print(Solution1().dailyTemperatures(temperatures[ : ]))
    print(Solution2().dailyTemperatures(temperatures[ : ]))
    print(Solution3().dailyTemperatures(temperatures[ : ]))

if __name__ == "__main__":
    main()