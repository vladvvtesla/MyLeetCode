# Main Idea
# This solution with bufer space for a new Linked List (Implemented)
# It is similar to merge action in merge sorting algorithm

# Runtime: 48 ms, faster than 10.23% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 14.3 MB, less than 63.51% of Python3 online submissions for Merge Two Sorted Lists.

# Main Idea
# inserting L2 data to L1   (Not implemented)
#
# for node in l2:
#     if end_of_l2:
#         return l1
#
#     if end_of_l1:
#         append_l2_to_l1
#         return l1
#
#     pop_node_from_l2
#     find_index_in_l1_to_insert_node
#     insert_node_into_l1_by_index
# return l1


# Implementation of Linked List
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

    # Returns the length (integer) of the linked list
    def length(self):
        """Assume the first position is "1"."""
        current = self.head
        total = 1
        while current.next:
            total += 1
            current = current.next
        return total

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next

    def printList(self):
        cur = self.head
        while (cur):
            print(cur.val, " -> ", end='')
            cur = cur.next
        print("")


# Definition for singly-linked list.
class ListNde:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = LinkedList()
        while l1 and l2:
            if l1.val <= l2.val:
                res.append(ListNode(l1.val))
                l1 = l1.next
            else:
                res.append(ListNode(l2.val))
                l2 = l2.next
        while l1:                        # append rest of nodes of l1
            res.append(ListNode(l1.val))
            l1 = l1.next
        while l2:                        # append rest of nodes of l2
            res.append(ListNode(l2.val))
            l2 = l2.next
        # res.printList()
        return res.head


l1 = [1,2,4]
l2 = [1,3,4]

# l1 = []
# l2 = [0]

# l1 = []
# l2 = []

ll1 = LinkedList(None)
[ll1.append(ListNode(i)) for i in l1]
ll1.printList()
print()

ll2 = LinkedList()
[ll2.append(ListNode(i)) for i in l2]
ll2.printList()
print()

s = Solution()
res = s.mergeTwoLists(ll1.head,ll2.head)

# res.printList()