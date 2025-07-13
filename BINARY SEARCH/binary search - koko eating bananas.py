# Problem 4.3 - Koko Eating Bananas
# Find the minimum eating speed k such that Koko can finish all banana piles within h hours.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Brute Force
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Try every possible eating speed starting from 1 until one satisfies the time constraint.
# Time  : O(n * max(piles))
# Space : O(1)
import math

class Solution1:
    def minEatingSpeed(self, piles, h):
        speed = 1                                       # Start from speed 1

        while True:
            totalTime = 0

            for pile in piles:                          # Time to eat each pile at current speed
                totalTime += math.ceil(pile / speed)    # Ceil division -> spending full hour on each pile

            if totalTime <= h:
                return speed                            # Returning speed if time constraint is met

            speed += 1                                  # Trying next higher speed


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Binary Search
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use binary search to find the minimum speed that allows Koko to eat all bananas in time.
# Time  : O(n * log max(piles))
# Space : O(1)
import math

class Solution2:
    def minEatingSpeed(self, piles, h):
        l, r = 1, max(piles)                        # Search range for speed: [1, max pile]
        speed = r                                   # Initializing speedult with the max possible speed

        while l <= r:
            k = (l + r) // 2                        # Trying middle speed

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p / k)       # Computing total time needed at speed k

            if totalTime <= h:
                speed = k                           # Found a valid speed, trying smaller
                r = k - 1
            else:
                l = k + 1                           # Need faster speed

        return speed                                # Returning minimum valid speed found



def main():
    piles = [25, 10, 23, 4]
    h = 4
    print(Solution1().minEatingSpeed(piles, h))
    print(Solution2().minEatingSpeed(piles, h))


if __name__ == '__main__':
    main()