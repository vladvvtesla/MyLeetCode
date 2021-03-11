"""
1021. Remove Outermost Parentheses (Easy, Stack)


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


class LinkedListQueue():
    def __init__(self):
        self.first = None
        self.last = None

    def isEmpty(self):
        """ Returns whether the queue is empty. """
        return self.first == None

    def enqueue(self, item):
        """ Push element x onto end of queue """
        oldlast = self.last
        self.last = Node(item)
        print(self.last.item)
        if self.isEmpty():                   # special case for empty queue
            self.first = self.last
        else:
            oldlast.next = self.last

    def dequeue(self):
        item = self.first.item
        self.first = self.first.next
        if self.isEmpty():                       # special case for empty queue
            self.last.next = None
        return item


class Solution:
    def __init__(self):
        self.inp = LinkedListStack()  # Stack for input sting
        self.res = LinkedListQueue()  # Queue for result
        self.sum = 0                  #  '(' is +1, ')' is -1.
        self.res_string = ''

    def removeOuterParentheses(self, s):
        """
        Removing the outermost parentheses
        :param s:     # input string
        :return:
        """
        for p in s:
            if p == '(':
                self.inp.push(p)
                self.sum += 1
                print('self.sum', self.sum)
            elif p == ')':
                self.inp.push(p)
                self.sum -= 1
                print('self.sum', self.sum)

            if self.sum == 0:
                print('self.sum again', self.sum)
                self.inp.pop()                    # delete last ')' from '(())'
                while not self.inp.isEmpty():     # replace all from inp to res queue'(()'
                    tmp = self.inp.pop()
                    print('tmp', tmp)
                    if not self.inp.isEmpty():    # don't enqueue last '('  from '(()' => res = '()'
                        self.res.enqueue(tmp)

        # We should reverse order, so lets replace all queue to stack
        tmp = LinkedListStack()
        while not self.res.isEmpty():
            tmp.push(self.res.dequeue())


        # Make string from res stack
        # while not self.res.isEmpty():
            # print('self.res.dequeue()', self.res.dequeue())
            # self.res_string += self.res.dequeue()

        while not tmp.isEmpty():
            # print('self.res.dequeue()', self.res.dequeue())
            self.res_string += tmp.pop()

        return self.res_string


def test_removeOuterParentheses():
    """
    test queue
    :return:
    """
    # print('start my test')

    # res = LinkedListQueue()
    # res.enqueue('(')
    # res.enqueue(')')
    # print('first dequeue', res.dequeue())
    # print('second dequeue', res.dequeue())


    # print('end my test')

    inp = ["(()())(())(()(()))"]
    out = ["()()()()(())"]

    #inp = ["(()())(())",
    #       "(()())(())(()(()))",
    #       "()()",
    #       "(())"]
    #out = ["()()()",
    #       "()()()()(())",
    #       "",
    #       "()"]
    for i in range(len(inp)):
        sol = Solution()
        test_res = sol.removeOuterParentheses(inp[i])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK" if test_res == out[i] else "Failed")
        print()


if __name__ == '__main__':
    test_removeOuterParentheses()
