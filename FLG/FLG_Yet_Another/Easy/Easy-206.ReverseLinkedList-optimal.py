"""
206. Reverse Linked List(Top-Easy)

Main Idea.
1) cur указывает на  head
2) Prev указывает на None
3) Пройтись по Linked List от head до конца,
поочередно меняя указатели  cur.next, prev, cur
В конце prev будет указывать на посленюю ноду,
Поэтому  return  prev


Time complexity: O(N)
один раз Пройтись по Linked List

Space complexity: O(1)
Constant space for prev and cur

Runtime: 57 ms, faster than 36.13% of Python3 online submissions for Reverse Linked List.
Memory Usage: 15.4 MB, less than 97.86% of Python3 online submissions for Reverse Linked List.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        prev = None
        cur = head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev


def test_solution():
    headA = ListNode(1)
    headA.next = ListNode(2)
    headA.next.next = ListNode(3)
    headA.next.next.next = ListNode(4)
    headA.next.next.next.next = ListNode(5)

    headA1 = ListNode(5)
    headA1.next = ListNode(4)
    headA1.next.next = ListNode(3)
    headA1.next.next.next = ListNode(2)
    headA1.next.next.next.next = ListNode(1)

    inp = [ headA ]
    out = [ headA1 ]
    # inp = [[1,2,3,1]]
    # out = [True]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.reverseList(inp[i])
        print('test_res.val', test_res.val)
        print("Test", i + 1, ":", "OK\n" if test_res.val == out[i].val else "Failed\n")


if __name__ == '__main__':
    test_solution()
