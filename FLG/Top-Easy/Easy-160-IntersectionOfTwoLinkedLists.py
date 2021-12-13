"""
160. Intersection of Two Linked Lists (Easy)

Main Idea:
1. Пройтись до конца первого LinkedList1 и получить ссылку на Node1
2.  Пройтись до конца второго LinkedList2 и получить ссылку на Node2
3. Если Node1 и Node2  это не один и тот же объект, то пересечения нет. Вернуть None
4.  Если Node1 и Node2  один и тот же объект, то пересечение находится где-то в середине
Для того чтобы быстрее найти, можем запомнить длину  LinkedList1 Len1 и  LinkedList2 Len2
5. В том  LinkedList, который короче. дойти до ноды, которая отстоит на  Len / 2 переходов от конца
6   Во втором LinkedList,  дойти до ноды, которая отстоит на столько же переходов от конца
Если  Node1 и Node2  один и тот же объект,
то пересечение в первой половине короткого списка,
если разные объекты, то пересечение во второй половине короткого списка

Изначально mid = hi = shortSize
Постепенно mid сдвигается в начало короткого списка,
пока не дойдем до пересечения


Time Complexity: O(NlogN)

Space Complexity: O(N) No extra space

Runtime: 212 ms, faster than 15.53% of Python3 online submissions for Intersection of Two Linked Lists.
Memory Usage: 29.3 MB, less than 81.76% of Python3 online submissions for Intersection of Two Linked Lists.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):

        def _getNode(head, x):
            count = 1
            cur = head
            while count < x:
                cur = cur.next
                count += 1
            return cur

        def _size(node):
            count = 0
            cur = node
            while cur:
                cur = cur.next
                count += 1
            return count

        sizeA = _size(headA)
        sizeB = _size(headB)

        if sizeA < sizeB:
            shortSize,longSize = sizeA,sizeB
            shortHead, longHead = headA, headB
        else:
            shortSize,longSize = sizeB,sizeA
            shortHead, longHead = headB, headA

        resHead = None
        lo = 1
        mid = hi = shortSize

        while lo <= hi:
            shortMid = _getNode(shortHead, mid)
            longMid = _getNode(longHead, mid + (longSize - shortSize ))
            if shortMid is longMid:
                resHead = shortMid
                hi = mid
            else:
                lo = mid + 1
            mid = (lo + hi) // 2
            if lo == hi: break
        return resHead


def test_solution():
    headA = ListNode(4)
    headA.next = ListNode(1)
    headA.next.next = ListNode(8)
    headA.next.next.next = ListNode(4)
    headA.next.next.next.next = ListNode(5)

    headB = ListNode(5)
    headB.next = ListNode(6)
    headB.next.next = ListNode(1)
    headB.next.next.next = headA.next.next


    headC = ListNode(1)
    headC.next = ListNode(9)
    headC.next.next = ListNode(1)
    headC.next.next.next = ListNode(2)
    headC.next.next.next.next = ListNode(4)

    headE = ListNode(2)
    headE.next = ListNode(6)
    headE.next.next = ListNode(4)


    headF = ListNode(1)
    headF.next = ListNode(5)
    headD = ListNode(3)
    headD.next = headC.next.next.next

    headG = ListNode(1)
    headH = headG

    headI = ListNode(3)
    headJ = ListNode(2)
    headJ.next = headI

    inp = [(headA, headB),(headC, headD),(headE, headF),(headG, headH),(headI, headJ)]
    out = [headA.next.next, headC.next.next.next, None, headG, headI]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.getIntersectionNode(inp[i][0], inp[i][1])
        if test_res:
            print('test_res.val', test_res.val)
        else:
            print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res is out[i] else "Failed\n")


if __name__ == '__main__':
    test_solution()
