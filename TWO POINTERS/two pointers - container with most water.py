# Problem 3.4 : Container with Most Water
# Given an array heights, where heights[i] represents the height of a vertical line [WALL] at position i, 
# return the maximum area of water a container can store using any two lines.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Brute Force
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Try every pair of lines and calculate the area using the shorter height.
# Time  : O(n²)
# Space : O(1)
class Solution1:
    def maxArea(self, heights):
        res = 0                                         # Initializing max area as 0

        for i in range(len(heights)):                   # Trying every possible pair of lines
            for j in range(i + 1, len(heights)):
                height = min(heights[i], heights[j])    # Water level is restricted by the shorter height
                width = j - i                           # Distance between the two lines
                area = height * width                   # Area of container = height × width
                res = max(res, area)                    # Tracking the maximum area found

        return res


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Two Pointers
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use two pointers at the ends of the array and move the one with the shorter line inward.
# Time  : O(n)
# Space : O(1)
class Solution2:
    def maxArea(self, heights):
        l, r = 0, len(heights) - 1                  # Starting with the widest container
        res = 0

        while l < r:
            height = min(heights[l], heights[r])    # Using the shorter height (bottleneck)
            width = r - l                           # Width between the two pointers
            area = height * width
            res = max(res, area)

            if heights[l] <= heights[r]:            # Moving the pointer to the shorter line to try finding a taller one
                l += 1
            else:
                r -= 1

        return res
    


def main():
    heights = [1,7,2,5,4,7,3,6]
    print(heights)
    print(Solution1().maxArea(heights))
    print(Solution2().maxArea(heights))


if __name__ == '__main__':
    main()