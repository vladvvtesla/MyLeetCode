"""
101 Symmetric Tree

1. Пройтись по дереву и преобразовать его в массив по уровням [1,2,2,...]
2. разбить массив на подмассивы по уровням дерева [1], [2,2], [3,4,4,3]
3. разделить подмассив на две части: [3,4], [4,3]
4. выполнить реверс второй части: [3,4], [3,4]
5. если мы получили два одинаковых подмассива, [3,4] == [3,4], то возвращаем True
6. Повторить операцию до самого нижнего уровня дерева


"""

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

    def levelorderTraversalWithNones(self, x):
        """
        1) сначала посчитать глубину дерева
        2) составить список для всех возможных Node в вдоичном дереве такой глубины
        1 элемент этого цикла равен root.val
        Цикл по этому списку
        Если у родительской ноды есть левый потомок,
            то значение = parentnode.left.val      иначе None
        Если у родительской ноды есть правый потомок,
            то значение = parentnode.right.val      иначе None
                            1
                          /  \
                         4    2     ===>  [1,4,2,None,None,3,None]
                             /
                            3
        x is root
        """
        # Create an list of Nones for result  N = 2**h - 1
        h = self.height(x)
        res = [None] * (2**h - 1)

        # Create an empty queue for level order traversal
        queue = []

        # Enqueue Root and node index in res. For root index is 0
        queue.append((x, 0))

        while (len(queue) > 0):
            # Insert front of queue into res and remove it from queue
            p_idx = queue[0][1]
            res[p_idx] = queue[0][0].val
            node_tuple = queue.pop(0)
            node = node_tuple[0]

            # Enqueue left child
            if node.left is not None:
                l_idx = 2 * p_idx + 1              # Parent = N , left child = 2*N + 1
                queue.append((node.left, l_idx))

            # Enqueue right child
            if node.right is not None:
                r_idx = 2 * p_idx + 2            # Parent = N , right child = 2*N + 2
                queue.append((node.right, r_idx))

        return res


def test_height():
    t = TreeNode(1)
    t.left = TreeNode(4)
    t.right = TreeNode(2)
    t.right.left = TreeNode(3)

    sol = Solution()
    test_res = sol.height(t)
    print('test_res', test_res)
    print("Test", 2, ":", "OK\n" if test_res == 3 else "Failed\n")

def test_levelorderTraversalWithNones():
    t = TreeNode(1)
    t.left = TreeNode(4)
    t.right = TreeNode(2)
    t.right.left = TreeNode(3)

    sol = Solution()
    test_res = sol.levelorderTraversalWithNones(t)
    print('test_res', test_res)
    print("Test", 1, ":", "OK\n" if test_res == [1,4,2,None,None,3,None] else "Failed\n")


if __name__ == '__main__':
    test_height()
    test_levelorderTraversalWithNones()
