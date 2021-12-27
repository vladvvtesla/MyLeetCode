"""
113. Path Sum II (Medium)


Main Idea:
В нодах есть отрицательные числа, поэтому нужно считать до конца, даже если достигли таргета
1) пройтись по дереву до самого низа
2) попутно запоминать пройденный путь
3) попутно считать промежуточные суммы
4) Если текущая сумма достигла 22 и у текущей ноды нет потомков, то текущий путь добавить в результат

Time complexity: В худшем случае нужно посетить все ноды. Поэтому O(N)

Space complexity: NlogN extraspace for all path

Runtime: 40 ms, faster than 90.42% of Python3 online submissions for Path Sum II.
Memory Usage: 15 MB, less than 99.18% of Python3 online submissions for Path Sum II.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root, targetSum):
        if not root: return []                               # edge Case

        res = []
        stack = [(root, [root.val], root.val)]

        while stack:
            cur_el = stack.pop()                              # O(1)
            if cur_el[2] == targetSum and not cur_el[0].left and not cur_el[0].right:
                res.append(cur_el[1])                     # O(1)
            else:
                node = cur_el[0]
                if node.left:
                    stack.append((node.left,                   # O(1)
                                  cur_el[1] + [node.left.val], # O(1)
                                  cur_el[2] + node.left.val)   # O(1)
                                 )
                if node.right:
                    stack.append((node.right,
                                  cur_el[1] + [node.right.val],
                                  cur_el[2] + node.right.val)
                                 )

        return res


def test_solution():
    rootA = TreeNode(5)
    rootA.left = TreeNode(4)
    rootA.right = TreeNode(8)
    rootA.left.left = TreeNode(11)
    rootA.left.left.left = TreeNode(7)
    rootA.left.left.right = TreeNode(2)
    rootA.right.left = TreeNode(13)
    rootA.right.right = TreeNode(4)
    rootA.right.right.left = TreeNode(5)
    rootA.right.right.right  = TreeNode(1)

    rootB = TreeNode(1)
    rootB.left = TreeNode(2)

    rootC = TreeNode(1)
    rootC.left = TreeNode(-2)
    rootC.right = TreeNode(-3)
    rootC.left.left = TreeNode(1)
    rootC.left.right = TreeNode(3)
    rootC.right.left = TreeNode(-2)
    rootC.left.left.left= TreeNode(-1)




    inp = [(rootA, 22), (rootB, 1),(rootC, -1),
           ]
    out = [[[5,8,4,5],[5,4,11,2]], [], [[1,-2,1,-1]], ]
    sol = Solution()
    for i in range(len(inp)):
        test_res = sol.pathSum(inp[i][0],inp[i][1])
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")


if __name__ == '__main__':
    test_solution()




