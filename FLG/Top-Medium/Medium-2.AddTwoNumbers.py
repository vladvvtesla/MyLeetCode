"""
2. Add Two Numbers (Medium)

Main Idea:
1. Прообежаться по всему L1 и получить число    O(n)
2. Прообежаться по всему L2 и получить число    O(n)
2. Сложить                                      O(1)
3. Из полученных числа сделать LinkedList       O(n)

Time complexity: O(n)

Space Complexity:

Runtime: 80 ms, faster than 33.44% of Python3 online submissions for Add Two Numbers.
Memory Usage: 14.3 MB, less than 45.87% of Python3 online submissions for Add Two Numbers.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        def _getnumber(first_node):
            cur = first_node
            res_number = 0
            idx = 0

            while cur:
                res_number += cur.val * (10 ** idx)
                cur = cur.next
                idx += 1

            return res_number

        res_sum = _getnumber(l1) + _getnumber(l2)
        res_list = [int(d) for d in str(res_sum)]

        # Linked List from array
        first_node = ListNode(res_list[-1])
        cur = first_node
        for idx in range(len(res_list)-2, -1, -1):
            cur.next = ListNode(res_list[idx])
            cur = cur.next

        return first_node


def test_solution():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    l3 = ListNode(0)
    l4 = ListNode(0)

    l5 = ListNode(9)
    l5.next = ListNode(9)
    l5.next.next = ListNode(9)
    l5.next.next.next = ListNode(9)
    l5.next.next.next.next = ListNode(9)
    l5.next.next.next.next.next = ListNode(9)
    l5.next.next.next.next.next.next = ListNode(9)

    l6 = ListNode(9)
    l6.next = ListNode(9)
    l6.next.next = ListNode(9)
    l6.next.next.next = ListNode(9)

    inp = [(l1, l2), (l3, l4), (l5, l6)
          ]
    out = [[7,0,8],[0],[8,9,9,9,0,0,0,1]]
    sol = Solution()

    for i in range(len(inp)):
        test_root = sol.addTwoNumbers(inp[i][0],inp[i][1])

        res_list = []
        cur = test_root
        while cur:
            res_list.append(cur.val)
            cur = cur.next

        print('res_list', res_list)
        print("Test", i + 1, ":", "OK\n" if res_list == out[i] else "Failed\n")


if __name__ == '__main__':
    test_solution()
