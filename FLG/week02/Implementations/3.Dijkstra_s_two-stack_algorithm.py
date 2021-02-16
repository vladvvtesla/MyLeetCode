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


"""
Dijkstra's two-stack algorithm
"""

def evaluate(eval_string):
    ops = LinkedListStack()
    vals = LinkedListStack()

    for s in eval_string:
        if s == "(":
            pass
        elif s == "+":
            ops.push(s)
        elif s == "*":
            ops.push(s)
        elif s == ")":
            op = ops.pop()
            if op == "+":
                vals.push(int(vals.pop()) + int(vals.pop()))
            elif op == "*":
                    vals.push(int(vals.pop()) * int(vals.pop()))
        else:
            try:                           # push ints, but ignore spaces
                int(s)
                vals.push(s)
            except ValueError:
                pass
    return vals.pop()


def test_evaluate():
    inp = ["( 1 + ( ( 2 + 3 ) * ( 4 * 5 ) ) )"]
    out = [101]
    for i in range(len(inp)):
        test_res = evaluate(inp[i])
        print()
        print("Test", i + 1, ":", "OK" if test_res == out[i] else "Failed")

if __name__ == '__main__':
    test_evaluate()









