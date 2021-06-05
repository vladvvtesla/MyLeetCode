"""
102. Binary Tree Level Order Traversal


Runtime: 40 ms, faster than 16.58% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 15 MB, less than 17.58% of Python3 online submissions for Binary Tree Level Order Traversal.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def height(self, x):
        if x is None:
            return 0
        else:
            return max(self.height(x.left), self.height(x.right)) + 1

    def levelOrder(self, x):
        """
        1) сначала посчитать глубину дерева
        2) составить список списков для всех уровней в вдоичном дереве такой глубины
        1-й элемент этого спискаравен [root.val]
        Добавить в очередь первую ноду и уровень, на котором она сидит
        Если очередь не пуста
            node.val добавить в результат, а ноду удалить из очереди
        Если у удаленной ноды есть левый потомок,
            то значение node.left.val добавить в результат, а ноду и номер уровня добавить в очередь
        Если у удаленной ноды есть правый потомок,
            то значение node.right.val добавить в результат, а ноду и номер уровня добавить в очередь
                            1
                          /  \
                         4    2     ===>  [[1],[4,2],[3]]
                             /
                            3
        x is root
        """

        # Create an list of Nones for result  N = 2**h - 1
        h = self.height(x)
        res = [[] for x in range(h)]   # [[], [], []]

        # Create an empty queue for level order traversal
        queue = []

        # Enqueue Root and node index in res. For root index is 0
        queue.append((x, 0))

        while (len(queue) > 0):
            # Spaceial case for test 4: root = []
            if queue[0][0].val is None:
                return [[]]
            # this is for Leetcode
            #  if queue[0][0] is None:
            #  return []

            # Insert front of queue into res and remove it from queue
            p_idx = queue[0][1]
            res[p_idx].append(queue[0][0].val)
            node_tuple = queue.pop(0)
            node = node_tuple[0]

            # Enqueue left child
            if node.left is not None:
                l_idx = p_idx + 1
                queue.append((node.left, l_idx))

            # Enqueue right child
            if node.right is not None:
                r_idx = p_idx + 1
                queue.append((node.right, r_idx))

        return res


def test_levelOrder():
    # Test 1
    t = TreeNode(1)
    t.left = TreeNode(4)
    t.right = TreeNode(2)
    t.right.left = TreeNode(3)

    sol = Solution()
    test_res = sol.levelOrder(t)
    print('test_res', test_res)
    print("Test", 1, ":", "OK\n" if test_res == [[1], [4, 2], [3]] else "Failed\n")

def test_levelOrder2():             # Test 2
    t = TreeNode(3)
    t.left = TreeNode(9)
    t.right = TreeNode(20)
    t.right.left = TreeNode(15)
    t.right.right = TreeNode(7)

    sol = Solution()
    test_res = sol.levelOrder(t)
    print('test_res', test_res)
    print("Test", 2, ":", "OK\n" if test_res == [[3],[9,20],[15,7]] else "Failed\n")

def test_levelOrder3():             # Test 3
    t = TreeNode(1)

    sol = Solution()
    test_res = sol.levelOrder(t)
    print('test_res', test_res)
    print("Test", 3, ":", "OK\n" if test_res == [[1]] else "Failed\n")

def test_levelOrder4():             # Test 4
    t = TreeNode(None)

    sol = Solution()
    test_res = sol.levelOrder(t)
    print('test_res', test_res)
    print("Test", 4, ":", "OK\n" if test_res == [[]] else "Failed\n")

if __name__ == '__main__':
    test_levelOrder()
    test_levelOrder2()
    test_levelOrder3()
    test_levelOrder4()