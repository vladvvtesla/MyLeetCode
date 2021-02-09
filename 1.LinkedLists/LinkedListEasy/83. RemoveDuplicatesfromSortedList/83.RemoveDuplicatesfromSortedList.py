# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Implementation of Linked List
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

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

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        if cur:
            while cur.next:
                print(cur.val)
                if cur.next.val > cur.val:
                    cur = cur.next
                else:
                    if cur.next.next:
                        cur = cur.next.next
                    else:
                        cur = cur.next
            return cur
        else:
            return head


l1 = [1,1,2]
l2 = [1,1,2,3,3]

ll1 = LinkedList(None)
[ll1.append(ListNode(i)) for i in l1]
ll1.printList()
print()

ll2 = LinkedList()
[ll2.append(ListNode(i)) for i in l2]
ll2.printList()
print()

s1 = Solution()
res1_head = s1.deleteDuplicates(ll1.head)
res1 = LinkedList(res1_head)
res1.printList()
print()

s2 = Solution()
res2_head = s1.deleteDuplicates(ll2.head)
res2 = LinkedList(res2_head)
res2.printList()
