"""
83. Remove Duplicates from Sorted List (Easy, Linked List)

Runtime: 44 ms, faster than 58.34% of Python3 online submissions for Remove Duplicates from Sorted List.
Memory Usage: 14.2 MB, less than 85.07% of Python3 online submissions for Remove Duplicates from Sorted List.
"""

# Implementation of Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def add_first(self, node):
        """Inserting at the Beginning"""
        node.next = self.head
        self.head = node

    def append(self, new_element):
        current = self.head
        if current:
            while current.next:
                # print(current.val)
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def printList(self):
        cur = self.head
        while (cur):
            print(cur.val, " -> ", end='')
            cur = cur.next
        print("")

    def to_list(self):
        res = []
        cur = self.head
        while (cur):
            res.append(cur.val)
            cur = cur.next
        return res


class Solution:
    def __init__(self, head):
        self.ll = LinkedList()  # Stack for input sting
        self.head = head

    def deleteDuplicates(self, head) -> ListNode:
        cur = self.head
        if not cur:
            return self.head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return self.head


def test_removeOuterParentheses():

    inp = [[1, 1, 2], [1,1,2,3,3], []]
    out = [[1, 2], [1,2,3], []]
    for i in range(len(inp)):
        ll = LinkedList(None)
        [ll.append(ListNode(i)) for i in inp[i]]
        ll.printList()
        print()
        sol = Solution(ll.head)
        sol.deleteDuplicates(ll.head)
        test_res = ll.to_list()
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK" if test_res == out[i] else "Failed")
        print()


if __name__ == '__main__':
    test_removeOuterParentheses()