"""
99. Recover Binary Search Tree  (Medium)

Main Idea:
пройтись по дереву в 

1) Обойти дерево в Inorder Traversal получим неотсортированный список
2) Пройтись по этому списку,
     3) если элемент меньше предыдущего, то это первый элемент на замену
     предыдущий - это left, сам элемент mid
     4) Если еще элемент меньше предыдущего, это второй элемент на замену
     второй элемент - right
5) Если нет элемента right, то поменять местами mid и left
6) Если есть элемент right, то поменять местами right и left


Time Complexity: O(N)
1) Inorder Traversal O(N)
2) обойти список O(N)
3) поменять элементы местами O(1)

Space Complexity:
O(N) extra space foe aux list

Runtime: 113 ms, faster than 26.67% of Python3 online submissions for Recover Binary Search Tree.
Memory Usage: 14.4 MB, less than 25.02% of Python3 online submissions for Recover Binary Search Tree.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(root):
            cur = root
            if not cur:
                return []
            else:
                return [val for val in inorder(cur.left) if val] + \
                       [cur.val] + \
                       [val for val in inorder(cur.right) if val]

        aux = inorder(root)

        # Find left, mid, right
        left = mid = right = None
        for k in range(1, len(aux)):
            if aux[k] < aux[k-1] and mid is None:
                left = k-1
                mid = k
            elif aux[k] < aux[k-1] and mid is not None:
                right = k

        def replace(root, a, b):
            cur = root
            if not cur:
                return []
            else:
                if cur.val == a:
                    cur.val = b
                elif cur.val == b:
                    cur.val = a
                return [val for val in replace(cur.left, a, b) if val] + \
                       [cur.val] + \
                       [val for val in replace(cur.right, a, b) if val]

        # Replace
        if right is not None:
            replace(root, aux[left], aux[right])
        else:
            replace(root, aux[left], aux[mid])


def test_solution():
    treeA = TreeNode(val=1)
    treeA.left = TreeNode(val=3)
    treeA.left.right = TreeNode(val=2)

    treeB = TreeNode(val=3)
    treeB.left = TreeNode(val=1)
    treeB.right = TreeNode(val=4)
    treeB.right.left = TreeNode(val=2)

    def inorder(root):
        cur = root
        if not cur:
            return []
        else:
            return [val for val in inorder(cur.left) if val] + \
                   [cur.val] + \
                   [val for val in inorder(cur.right) if val]

    inp = [treeA, treeB]
    out = [[1,2,3], [1,2,3,4]]
    sol = Solution()
    for i in range(len(inp)):
        res = sol.recoverTree(inp[i])
        print('inorder(res)', inorder(inp[i]))
        print("Test", i + 1, ":", "OK\n" if inorder(inp[i]) == out[i] else "Failed\n")

if __name__ == '__main__':
    test_solution()

