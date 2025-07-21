# Problem 3.5 : Trapping Rain Water
# Given an array of heights representing vertical bars [BLOCKS], 
# return the total amount of water that can be trapped over them after raining.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Brute Force
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : For each index, compute max height to the left and right, and use that to determine water trapped.
# Time  : O(n²)
# Space : O(1)
class Solution1:
    def trap(self, height):
        if not height:
            return 0

        n = len(height)
        res = 0

        for i in range(n):                                  # Looping through every position
            leftMax = height[i]                             # Initializing max to the left
            rightMax = height[i]                            # Initializing max to the right

            for j in range(i):                              # Finding tallest bar on the left (including current)
                leftMax = max(leftMax, height[j])

            for j in range(i + 1, n):                       # Finding tallest bar on the right (including current)
                rightMax = max(rightMax, height[j])

            trapped = min(leftMax, rightMax) - height[i]    # Water trapped at index i = min(left, right) - height[i]
            res += trapped

        return res


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Prefix & Suffix Arrays
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : For each index, compute max height to the left and right, and use that to determine water trapped.
# Time  : O(n)
# Space : O(n)
class Solution2:
    def trap(self, height):
        n = len(height)
        if n == 0:
            return 0

        leftMax = [0] * n                                       # Arrays to store max height to the left and right of each position
        rightMax = [0] * n

        leftMax[0] = height[0]                                  # Filling leftMax : max height from the left up to i
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax[n - 1] = height[n - 1]                         # Filling rightMax : max height from the right up to i
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        res = 0
        for i in range(n):                                      # Calculating trapped water at each index
            water = min(leftMax[i], rightMax[i]) - height[i]
            res += water

        return res


# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. Stack
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use a stack to keep track of decreasing bars. When a higher bar is found, pop and calculate trapped water.
# Time  : O(n)
# Space : O(n)
class Solution3:
    def trap(self, height):
        if not height:
            return 0

        stack = []
        res = 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:                  # While current bar is taller than the bar at the stack's top
                mid = stack.pop()                                           # The bar where water might get trapped

                if not stack:
                    break                                                   # No left boundary to trap water

                left = stack[-1]                                            # Index of left boundary
                width = i - left - 1                                        # Width between left and current bar
                bounded_height = min(height[i], height[left]) - height[mid]
                res += width * bounded_height

            stack.append(i)                                                 # Push current bar index onto stack

        return res
    

# ---------------------------------------------------------------------------------------------------------------------------------------
# 4. Two Pointers
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Move two pointers inward, always shifting the side with the smaller max height. Calculate trapped water in one pass.
# Time  : O(n)
# Space : O(1)
class Solution4:
    def trap(self, height):
        if not height:
            return 0

        l, r = 0, len(height) - 1                   # Initializing left and right pointers
        leftMax, rightMax = height[l], height[r]    # Tracking max heights on both sides
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])   # Updating left max
                res += leftMax - height[l]          # Water trapped at current l
            else:
                r -= 1
                rightMax = max(rightMax, height[r]) # Updating right max
                res += rightMax - height[r]         # Water trapped at current r

        return res



def main():
    height = [0,2,0,3,1,0,1,3,2,1]
    print(height)
    print(Solution1().trap(height))
    print(Solution2().trap(height))
    print(Solution3().trap(height))
    print(Solution4().trap(height))


if __name__ == '__main__':
    main()