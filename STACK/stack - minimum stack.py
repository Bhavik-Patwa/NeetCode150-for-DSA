# Problem 2.2 - MINIMUM STACK
# Design a stack that supports push, pop, top and retrieving the minimum element in constant time.


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Brute Force
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : To get the minimum, traverse the stack each time using a temp stack to preserve order.
# Time  : O(n)      {For getMin – traversing the stack}
# Space : O(n)      {Temp stack used to restore elements}
class Solution1:
    def __init__(self):
        self.stack = []                             # list uses append(), pop() at same (right) end = stack

    def push(self, val):
        self.stack.append(val)                      # Pushing the value onto the stack

    def pop(self):
        self.stack.pop()                            # Popping the top element

    def top(self):
        return self.stack[-1]                       # Returning the top element

    def getMin(self):
        tmp = []
        mini = self.stack[-1]                       # Starting with the top as minimum

        while len(self.stack):
            mini = min(mini, self.stack[-1])        # Updating minimum
            tmp.append(self.stack.pop())            # Moving elements to temporary stack

        while len(tmp):
            self.stack.append(tmp.pop())            # Restoring original stack

        return mini                                 # Returning the minimum value


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Two Stacks
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Maintain an auxiliary minStack where each element is the minimum so far.
# Time  : O(1)      {All operations in constant time}
# Space : O(n)      {Extra minStack of same size as stack}
class Solution2:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val)                                      # Pushing actual value
        val = min(val, self.minStack[-1] if self.minStack else val) # Simultaneously checking if it is the minimum so far
        self.minStack.append(val)                                   # Pushing current min to minStack

    def pop(self):
        self.stack.pop()                                            # Popping from main stack
        self.minStack.pop()                                         # Popping corresponding min

    def top(self):
        return self.stack[-1]                                       # Returning top of main stack

    def getMin(self):
        return self.minStack[-1]                                    # Returning top of minStack (current min)


# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. One Stack (Encoded Difference)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Store differences instead of actual values to encode minimum without extra space.
#         If pushing a value less than current min, encode the difference and update min.
# Time  : O(1)        {All operations in constant time}
# Space : O(n)        {Only one stack used}
class Solution3:
    def __init__(self):
        self.min = float('inf')                 # Initializing min value to infinity
        self.stack = []                         # Storing the difference = actual value - min

    def push(self, val):
        if not self.stack:
            self.stack.append(0)                # Appending first value (difference = 0) into empty stack
            self.min = val                      # Setting min to the value
        else:
            self.stack.append(val - self.min)   # Storing difference from current min
            if val < self.min:
                self.min = val                  # Updating min if necessary

    def pop(self):
        if not self.stack:
            return
        
        pop = self.stack.pop()                  # min correct (need not be updated)
        if pop < 0:                             # popped diff for latest min, update current min
            self.min = self.min - pop           # old min = latest min - -diff = latest min + diff

    def top(self):
        top = self.stack[-1]
        if top > 0:                             # top/diff > 0 : min not updated
            return top + self.min               # Actual value = diff + min
        else:
            return self.min                     # top/diff < 0 : actual value = latest updated min

    def getMin(self):
        return self.min                         # Returning current min


def main():
    sln1 = Solution1()
    sln1.push(5)
    sln1.push(2)
    sln1.push(7)
    print(sln1.getMin()) 

    sln2 = Solution2()
    sln2.push(5)
    sln2.push(2)
    sln2.push(7)
    print(sln2.getMin())

    sln3 = Solution3()
    sln3.push(5)
    sln3.push(2)
    sln3.push(7)
    print(sln3.getMin())



if __name__ == "__main__":
    main()