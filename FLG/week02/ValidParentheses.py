"""
Runtime: 32 ms, faster than 63.83% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14.3 MB, less than 66.52% of Python3 online submissions for Valid Parentheses.
"""

class Node(object):
    def __init__(self, item=None):
        self.item = item
        self.next = None

class LinkedListStack():
    """" Stack Implementation using Singly-Linked Lists.  Coursera Sedgewick 1 w2 """
    def __init__(self, first=None):
        self.first = first

    def isEmpty(self):
        """ Chek if the first node is Null"""
        return self.first == None

    def push(self, item):
        """ Push to the beginning of Linked List """
        oldfirst = self.first         # Save link to the old head into a tmp variable
        self.first = Node()           # new first node
        self.first.item = item        #
        self.first.next = oldfirst    # create link to the

    def pop(self):
        """ Pop from the beginning of Linked List"""
        item = self.first.item         # Save link to the old head into a tmp variable
        self.first = self.first.next   # new first node
        return item


class Solution:
    def isValid(self, s: str) -> bool:
        stack = LinkedListStack()  # Empty stack
        parens = {"(": ")",
                  "{": "}",
                  "[": "]"
                   }                  # Keys = Opening parenthesis, Values - slosing parenthesis

        for item in s:
            if item in parens.keys():
                stack.push(item)            # Push all opening parenthesis
                continue
            if stack.isEmpty():             # False because empty stask and closing parenthesis
                return False
            pop_item = stack.pop()
            if item != parens[pop_item]:    # if item == ")" pop_item must be "(", and not "["
                return False

        return stack.isEmpty()              # We should get an empty stack, and not "((((("

def test_isValid():
    inp = ["()","()[]{}","(]", "([])", "([)]","(", "(((", ")", ""]
    out = [True, True, False, True, False, False, False, False, True]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.isValid(inp[i])
        print()
        print("Test", i + 1, ":", "OK" if test_res == out[i] else "Failed")

if __name__ == '__main__':
    test_isValid()