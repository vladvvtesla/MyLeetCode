"""



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
    def calculate(self, s: str) -> int:
        """
        Dijkstra's two-stack algorithm
        """
        ops = LinkedListStack()
        vals = LinkedListStack()
        op = ''                                  # operator
        prev_d = False                           # Previus is digit , For case '233'

        for l in s:
            if l == " ":
                pass
            elif l == "(":
                ops.push(l)
                prev_d = False
            elif l == "+":
                ops.push(l)
                prev_d = False
            elif l == "-":
                ops.push(l)
                prev_d = False
            elif l == ")":
                prev_d = False
                while op != '(':                  # for '(4+5+2)'
                    op = ops.pop()
                    if op == "+":
                        vals.push(vals.pop() + vals.pop())
                    elif op == "-":
                        vals.push((vals.pop() - vals.pop()) * (-1))    # change sign
                op = ""  # we reached "("  and we should set op = '' at the end of while-circle

            else:
                if prev_d:
                    vals.push(10*vals.pop() + int(l))  #   23 = 10*2 + 3
                else:
                    vals.push(int(l))
                prev_d = True

        if not ops.isEmpty():                         # vals = "14,9", ops = "+"
            op = ops.pop()
            if op == "+":
                vals.push(vals.pop() + vals.pop())
            elif op == "-":
                vals.push((vals.pop() - vals.pop()) * (-1))    # change sign

        return vals.pop()                      # vals = "23", ops is empty


def test_calculate():
    inp = ["(1 + 1)",
           " 2-1 + 2 ",
           "4+9",
           "4 - 9",
           "(4+5-2)",
           "4+(9-2)",
           "(1+(4+5+2)-3)+(6+8)",
           "2147483647",
           "4+(90-20)",
           "-2+ 1",
           "30 + (-20+ 1)"]
    out = [2, 3, 13, -5, 7, 11, 23, 2147483647, 74, -1, -19]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.calculate(inp[i])
        print("Test", i + 1, ":", "OK" if test_res == out[i] else "Failed")
        print()

if __name__ == '__main__':
    test_calculate()





