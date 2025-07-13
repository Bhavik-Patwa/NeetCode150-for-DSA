# Problem 2.3 - EVALUATE REVERSE POLISH NOTATION
# Evaluate the value of an arithmetic expression in Reverse Polish Notation (postfix).
# Valid operators : +, -, *, /. Each operand is an integer.

# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Brute Force
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Loop through tokens and evaluate expressions when operator is found. Shrink and replace the expression in-place.
# Time  : O(n²)     {List slicing and re-creating multiple times}
# Space : O(n)      {Temporary tokens list}
class Solution1:
    def evalRPN(self, tokens):
        while len(tokens) > 1:
            for i in range(len(tokens)):
                if tokens[i] in "+-*/":
                    a = int(tokens[i - 2])                  # Left operand
                    b = int(tokens[i - 1])                  # Right operand

                    if tokens[i] == '+':                    # Applying the operator
                        result = a + b
                    elif tokens[i] == '-':
                        result = a - b
                    elif tokens[i] == '*':
                        result = a * b
                    elif tokens[i] == '/':
                        result = int(a / b)                 # Truncating toward zero

                    tokens = tokens[ : i - 2] + [str(result)] + tokens[ i + 1 : ]    # Replacing operands and operator with the result
                    break
        return int(tokens[0])


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Doubly Linked List
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Build a doubly linked list and modify it in-place as you evaluate the expression.
# Time  : O(n²)     {Due to backtracking and modification}
# Space : O(n)      {Linked list storage}
class DoublyLinkedList:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution2:
    def evalRPN(self, tokens):
        head = DoublyLinkedList(tokens[0])              # Building doubly linked list object from tokens
        curr = head
        for i in range(1, len(tokens)):
            curr.next = DoublyLinkedList(tokens[i], prev = curr)
            curr = curr.next

        while head is not None:                         # Evaluating the expression
            if head.val in "+-*/":
                l = int(head.prev.prev.val)             # Left operand
                r = int(head.prev.val)                  # Right operand

                if head.val == '+':                     # Applying the operator
                    res = l + r
                elif head.val == '-':
                    res = l - r
                elif head.val == '*':
                    res = l * r
                else:
                    res = int(l / r)                    # Truncating toward zero

                head.val = str(res)                     # Replacing operator node with result, and update pointers
                head.prev = head.prev.prev.prev
                if head.prev:
                    head.prev.next = head

            ans = int(head.val)                         # Storing current result
            head = head.next

        return ans


# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. Recursion
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Recursively evaluate tokens from the end using DFS. For each operator, evaluate right and left subtrees.
# Time  : O(n)      {Each token processed once}
# Space : O(n)      {Call stack due to recursion}
class Solution3:
    def evalRPN(self, tokens):
        def dfs():
            token = tokens.pop()                        # Popping token from end
            if token not in "+-*/":
                return int(token)                       # return number

            right = dfs()                               # Right operand
            left = dfs()                                # Left operand

            if token == '+':                            # Applying the operator
                return left + right
            elif token == '-':
                return left - right
            elif token == '*':
                return left * right
            elif token == '/':
                return int(left / right)                # Truncating toward zero

        return dfs()                                    # call and return the result computed by dfs


# ---------------------------------------------------------------------------------------------------------------------------------------
# 4. Stack
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use a stack. Push operands. On operator, pop two values, evaluate, push result back.
# Time  : O(n)        {Each token processed once}
# Space : O(n)        {Stack size grows with operands}
class Solution4:
    def evalRPN(self, tokens):
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())             # Applying addition
            elif c == "-":
                stack.append(stack.pop() - stack.pop())             # Order matters
            elif c == "*":
                stack.append(stack.pop() * stack.pop())             # Applying multiplication
            elif c == "/":
                stack.append(int(float(stack.pop() / stack.pop()))) # Truncating toward zero
            else:
                stack.append(int(c))                                # Pushing number to stack

        return stack[0]


def main():
    tokens = ["2", "3", "+", "3", "*", "4", "-"]
    print(Solution1().evalRPN(tokens[ : ]))
    print(Solution2().evalRPN(tokens[ : ]))
    print(Solution3().evalRPN(tokens[ : ]))
    print(Solution4().evalRPN(tokens[ : ]))



if __name__ == "__main__":
    main()