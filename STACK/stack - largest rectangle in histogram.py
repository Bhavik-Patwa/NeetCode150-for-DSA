# Problem 2.7 - LARGEST RECTANGLE IN HISTOGRAM
# Given bar heights in a histogram, return the area of the largest rectangle.

# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Brute Force
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : For each bar, expand left and right to find the max width it can extend while keeping the height.
# Time  : O(n²)
# Space : O(1)
class Solution1:
    def largestRectangleArea(self, heights):
        n = len(heights)
        maxArea = 0

        for i in range(n):
            height = heights[i]                                         # Current bar height

            rightMost = i + 1
            while rightMost < n and heights[rightMost] >= height:       # Expanding right as long as bars are at least as tall
                rightMost += 1

            leftMost = i - 1
            while leftMost >= 0 and heights[leftMost] >= height:        # Expanding left as long as bars are at least as tall
                leftMost -= 1

            width = rightMost - leftMost - 1                            # Total width of rectangle
            area = height * width                                       # Area = height × width
            maxArea = max(maxArea, area)                                # Updating max area if needed

        return maxArea


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Divide and Conquer (Segment Tree)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Recursively calculate max area in subarrays using index of min bar in each range (via segment tree).
# Time  : O(n log n)
# Space : O(n)
class MinIdx_Segtree:
    def __init__(self, N, A):
        self.n = N
        self.INF = int(1e9)
        self.A = A

        while (self.n & (self.n - 1)) != 0:         # Extending list to nearest power of 2 for segment tree compatibility
            self.A.append(self.INF)
            self.n += 1

        self.tree = [0] * (2 * self.n)              # Segment tree array
        self.build()                                # Building segment tree

    def build(self):
        for i in range(self.n):                     # Filling leaves with indices
            self.tree[self.n + i] = i

        for j in range(self.n - 1, 0, -1):          # Building internal nodes
            a = self.tree[j << 1]
            b = self.tree[(j << 1) + 1]
            self.tree[j] = a if self.A[a] <= self.A[b] else b

    def query(self, ql, qh):
        return self._query(1, 0, self.n - 1, ql, qh)

    def _query(self, node, l, h, ql, qh):
        if ql > h or qh < l: return self.INF                    # No overlap
        if l >= ql and h <= qh: return self.tree[node]          # Full overlap

        a = self._query(node << 1, l, (l + h) >> 1, ql, qh)     # Partial overlap — query left and right children
        b = self._query((node << 1) + 1, ((l + h) >> 1) + 1, h, ql, qh)

        if a == self.INF: return b
        if b == self.INF: return a
        return a if self.A[a] <= self.A[b] else b

class Solution2:
    def getMaxArea(self, heights, l, r, st):
        if l > r: return 0                   # Empty range
        if l == r: return heights[l]         # Single bar → area is its height

        minIdx = st.query(l, r)              # Getting index of min height in range

        left = self.getMaxArea(heights, l, minIdx - 1, st)      # Dividing into left, right and center area
        right = self.getMaxArea(heights, minIdx + 1, r, st)
        mid = (r - l + 1) * heights[minIdx]  # Full range area using min height

        return max(left, right, mid)         # Returning the max of all three

    def largestRectangleArea(self, heights):
        st = MinIdx_Segtree(len(heights), heights[:])
        return self.getMaxArea(heights, 0, len(heights) - 1, st)


# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. Stack (Left & Right Boundaries)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : For each bar, find the closest smaller bar on both sides. Use this to compute width and area.
# Time  : O(n)
# Space : O(n)
class Solution3:
    def largestRectangleArea(self, heights):
        n = len(heights)
        leftMost = [-1] * n
        rightMost = [n] * n
        stack = []

        for i in range(n):                                      # Left boundary : Nearest smaller to left
            while stack and heights[stack[-1]] >= heights[i]:   # Ignoring equal or greater (can form rectangle)
                stack.pop()
            if stack:                                           # Remaining are smaller
                leftMost[i] = stack[-1]                         # Assigning until nearest/latest
            stack.append(i)

        stack.clear()

        for i in range(n - 1, -1, -1):                          # Right boundary : Nearest smaller to right
            while stack and heights[stack[-1]] >= heights[i]:   # Ignoring equal or greater (can form rectangle)
                stack.pop()
            if stack:                                           # Remaining are smaller
                rightMost[i] = stack[-1]                        # Assigning until nearest/latest
            stack.append(i)

        maxArea = 0

        for i in range(n):                                      # Calculating area using boundaries
            width = rightMost[i] - leftMost[i] - 1              # width = length - (length - rightMost) - (leftMost + 1) = rightMost - leftMost - 1
            area = heights[i] * width
            maxArea = max(maxArea, area)

        return maxArea


# ---------------------------------------------------------------------------------------------------------------------------------------
# 4. Stack (One Pass)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : As you iterate, pop from stack when you find a shorter bar and calculate area immediately.
# Time  : O(n)
# Space : O(n)
class Solution4:
    def largestRectangleArea(self, heights):
        maxArea = 0
        stack = []      # (start_index, height). Pushes current height, but holds previously unresolved (rightward possible) pairs
        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:       # Resolving previous and finding current start_index : while stack top (previous bar) is taller than current
                index, height = stack.pop()         # Popping last taller bar and resolve (cannot go further)
                area = height * (i - index)         # index = start_index (inclusive), i = current (exclusive)
                maxArea = max(maxArea, area)
                start = index                       # Assigning previous (may hold it's previous) bar's start_index to the current
            stack.append((start, h))                # start (current) = start (taller bars before current), h = current height

        for i, h in stack:                          # Processing remaining bars in stack (multiple for loops), with right boundary = end
            area = h * (len(heights) - i)           # width = end - start_index
            maxArea = max(maxArea, area)

        return maxArea


# ---------------------------------------------------------------------------------------------------------------------------------------
# 5. Stack (Optimal with Sentinel)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Push all bars and use a dummy bar (0) to flush the stack in one final pass.
# Time  : O(n)
# Space : O(n)
class Solution5:
    def largestRectangleArea(self, heights):
        heights.append(0)                   # Sentinel value to flush stack
        maxArea = 0
        stack = []                          # Stack stores indices

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:    # current bar smaller than previously unresolved bar = taller bar ends here
                height = heights[stack.pop()]                   # If current height < previously unresolved (taller) bar : resolve taller bar
                width = i if not stack else i - stack[-1] - 1   # width = rightMost - leftMost - 1
                area = height * width
                maxArea = max(maxArea, area)
            stack.append(i)
                                            # Flushing (single for loop) and processing remaining bars in stack, with right boundary = end
        return maxArea


def main():
    heights = [7, 1, 7, 2, 2, 4]
    print(heights)
    print(Solution1().largestRectangleArea(heights[ : ]))
    print(Solution2().largestRectangleArea(heights[ : ]))
    print(Solution3().largestRectangleArea(heights[ : ]))
    print(Solution4().largestRectangleArea(heights[ : ]))
    print(Solution5().largestRectangleArea(heights[ : ]))



if __name__ == "__main__":
    main()