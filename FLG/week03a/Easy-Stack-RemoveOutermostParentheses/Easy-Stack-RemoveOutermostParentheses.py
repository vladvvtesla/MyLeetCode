"""
1021. Remove Outermost Parentheses (Easy, Stack)

Main idea: We use LinkedListQueue
1. Enqueue all parentheses to Queue
2. Calculate a summ:   '(' is +1, ')' is -1.
3. If summ == 0, dequeue all parentheses from Queue, and append them into List,
excluding the fist and the last parentheses. "(()())" => "()()"
4 continue for all parentheses in the input string

# With aux list
# Runtime: 104 ms, faster than 6.32% of Python3 online submissions for Remove Outermost Parentheses.
# Memory Usage: 14.3 MB, less than 64.17% of Python3 online submissions for Remove Outermost Parentheses.

"""

class Node(object):
    def __init__(self, item=None):
        self.item = item
        self.next = None

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

    def printList(self):
        cur = self.first
        while (cur):
            print(cur.val, " -> ", end='')
            cur = cur.next
        print("")

class Solution:
    def __init__(self):
        self.inp = LinkedListQueue()   # Queue for input sting
        self.sum = 0                   #  '(' is +1, ')' is -1.
        self.res_list = []

    def removeOuterParentheses(self, s):
        """
        Removing the outermost parentheses
        :param s:     input string
        :return:      string
        """
        for p in s:
            if p == '(':
                self.inp.enqueue(p)
                self.sum += 1
            elif p == ')':
                self.inp.enqueue(p)
                self.sum -= 1

            if self.sum == 0:
                self.inp.dequeue()                # delete ferst ')' from '(())'
                while not self.inp.isEmpty():     # replace all from inp to res list'()'
                    tmp = self.inp.dequeue()
                    if not self.inp.isEmpty():    # don't append last ')'  from '(())' => res = '()'
                        self.res_list.append(tmp)

        return ''.join(self.res_list)


def test_removeOuterParentheses():
    inp = ["(()())(())",
           "(()())(())(()(()))",
           "()()",
           "(())"]
    out = ["()()()",
           "()()()()(())",
           "",
           "()"]
    for i in range(len(inp)):
        sol = Solution()
        test_res = sol.removeOuterParentheses(inp[i])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK" if test_res == out[i] else "Failed")
        print()


if __name__ == '__main__':
    test_removeOuterParentheses()
