"""
19. Remove Nth Node From End of List (Medium)

Main Idea:
1) Get a size of a Linked List
2) If n == size  we should delete the first node of a Linked List, so head = head.next
3) Elif n < size, we calculate the shift from the head to the previous node and
   prev_node.next = prev_node.next.next


Time complexity:  O(n)
O(n) for getting a size  +  O(n) for finding node + O(1) to deleting node

Space Complexity:O(n)

Runtime: 43 ms, faster than 18.76% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 14.4 MB, less than 15.11% of Python3 online submissions for Remove Nth Node From End of List.

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        def _size(node):
            count = 0
            while node:
                node = node.next
                count += 1
            return count

        sz = _size(head)

        if 1 <= n < sz:                     # 1) Delete Node in the middle AND the last Node of a Linked List
            shift = sz - n - 1
            cur = head
            while shift > 0:
                cur = cur.next
                shift -= 1
            cur.next = cur.next.next
        elif n == sz:                        # 2) Delete the first Node of a Linked List
            head = head.next

        return head


def test_solution():

    class SinglyLinkedList():
        def __init__(self, head=None):
            self.head = head

        def append(self, x):
            if not self.head:
                self.head = ListNode(x)
            else:
                cur = self.head
                while cur.next:
                    cur = cur.next
                cur.next = ListNode(x)

        def __str__(self):
            res = []
            if self.head:
                cur = self.head
                res.append(cur.val)
                while cur.next:
                    cur = cur.next
                    res.append(cur.val)

            return str(res)


    def toLinkedList(arr):
        ll = SinglyLinkedList()
        for k in arr:
            ll.append(k)
        return ll

    def toList(head):
        res = []
        if head:
            cur = head
            res.append(cur.val)
            while cur.next:
                cur = cur.next
                res.append(cur.val)
        return res



    llist1 = toLinkedList([1,2,3,4,5])
    llist2 = toLinkedList([1])
    llist3 = toLinkedList([])
    # print('llist1', llist1)
    # print('llist2', llist2)
    # print('llist3', llist3)
    # print('toList-llist1', toList(llist1.head))
    # print('toList-llist2', toList(llist2.head))
    # print('toList-llist3', toList(llist3.head))

    inp = [(toLinkedList([1,2,3,4,5]).head, 2),
           (toLinkedList([1]).head,  1),
           (toLinkedList([1,2]).head, 1),
           (toLinkedList([1,2,3,4,5]).head, 1),
           ]
    out = [[1,2,3,5], [], [1], [1,2,3,4]]
    sol = Solution()


    for i in range(len(inp)):
        test_head = sol.removeNthFromEnd(inp[i][0], inp[i][1])
        test_res = toList(test_head)
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")


if __name__ == '__main__':
    test_solution()