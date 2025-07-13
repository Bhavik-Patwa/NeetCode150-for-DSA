# Problem 2.6 - CAR FLEETS
# Return the number of car fleets that will arrive at the destination.

# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Stack
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Sort cars by position (furthest to closest). Use stack to track fleet arrival times.
#         A car forms a new fleet only if it arrives strictly later than the car ahead.
# Time  : O(n log n)    {Sorting}
# Space : O(n)          {Stack to track fleet times}
class Solution1:
    def carFleet(self, target, position, speed):
        pair = [(p, s) for p, s in zip(position, speed)]        # Pairing position with speed
        pair.sort(reverse = True)                               # Sorting in reverse by position 10, 7, 4, 1 (right to left)

        stack = []

        for p, s in pair:
            time = (target - p) / s                             # Time to reach destination
            stack.append(time)                                  # Pushing time to stack

            if len(stack) >= 2 and stack[-1] <= stack[-2]:      # Same fleet : time for current car[-1] <= car[-2] ahead
                stack.pop()                                      

        return len(stack)                                       # Number of fleets is stack size


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Iteration
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Track fleets using latest fleet time without using a stack.
# Time  : O(n log n)
# Space : O(1)
class Solution2:
    def carFleet(self, target, position, speed):
        pair = [(p, s) for p, s in zip(position, speed)]    # zipping 'each' element of 2 lists to generate tuple pairs
        pair.sort(reverse = True)

        fleets = 1                                          # At least one fleet exists (first car)
        prevTime = (target - pair[0][0]) / pair[0][1]       # Time = ([target - pos] / speed) for first car to reach destination

        for i in range(1, len(pair)):
            currP, currS = pair[i]
            currTime = (target - currP) / currS             # Time for current car

            if currTime > prevTime:                         # Car can't catch previous fleet -> new fleet
                fleets += 1
                prevTime = currTime                         # Updating reference time

        return fleets


def main():
    target = 10
    position = [4, 1, 0, 7]
    speed = [2, 2, 1, 1]

    print(Solution1().carFleet(target, position[ : ], speed[ : ]))
    print(Solution2().carFleet(target, position[ : ], speed[ : ]))



if __name__ == "__main__":
    main()