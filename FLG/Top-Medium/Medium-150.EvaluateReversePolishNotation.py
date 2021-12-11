"""
150. Evaluate Reverse Polish Notation (Top-Medium)

Main Idea:
Use Stack Append and Pop

Time Complexity: O(n)

Space Complexity: O(n)

Runtime: 64 ms, faster than 84.86% of Python3 online submissions for Evaluate Reverse Polish Notation.
Memory Usage: 14.5 MB, less than 71.65% of Python3 online submissions for Evaluate Reverse Polish Notation.
"""


class Solution:
    def evalRPN(self, tokens):
        from collections import deque
        stack = deque()

        for val in tokens:
            if val not in {"+", "-", "*", "/"}:
                stack.append(int(val))
            else:
                if val == "+":
                    stack.append(stack.pop() + stack.pop())
                elif val == "-":
                    previous = stack.pop()
                    stack.append(stack.pop() - previous)
                elif val == "*":
                    stack.append(stack.pop() * stack.pop())
                else:
                    previous = stack.pop()
                    stack.append(int(stack.pop() / previous))
        return stack.pop()


def test_solution():

    inp = [["2", "1", "+", "3", "*"],
           ["4", "13", "5", "/", "+"],
           ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
           ]
    out = [9, 6, 22]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.evalRPN(inp[i])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")


if __name__ == '__main__':
    test_solution()
