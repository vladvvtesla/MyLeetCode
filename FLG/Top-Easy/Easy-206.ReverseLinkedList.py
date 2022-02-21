"""
206. Reverse Linked List(Top-Easy)

1) Переделать все ссылки next
2) Не забыть ссылку head.next сделать None,
иначе получится зацикливание после реверса,
последняя нода будет ссылаться на предпоследнюю

Main Idea.

Time complexity: O(N)
Пройтись по LinkedList и создать q: O(N)
Пройтись по q и создать новый LinkedList: O(N)
O(N) + O(N) = O(N)

Space complexity: O(N)
Extra space O(N) for q

Runtime: 90 ms, faster than 5.33% of Python3 online submissions for Reverse Linked List.
Memory Usage: 15.4 MB, less than 80.23% of Python3 online submissions for Reverse Linked List.

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        q = []

        while head:
            q.append(head)
            head = head.next

        q[0].next = None
        head = q.pop()
        cur_node = head
        while q:
            cur_node.next = q.pop()
            cur_node = cur_node.next

        return head


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
