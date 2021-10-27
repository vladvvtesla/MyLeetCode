"""
Medium - 106. Construct Binary Tree from Inorder and Postorder Traversal

Main Idea:  The task is similar to
            105. Construct Binary Tree from Inorder and Preorder Traversal
            1) Postoorder[-1] is always a root
            2) we can divide Inorder: [left subtree, root, right subtree]
            3) Recurcion using subarrays

Time complexity:

Space complexity:

Runtime: 196 ms, faster than 33.47% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
Memory Usage: 88.3 MB, less than 27.92% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder[-1])
        mid = inorder.index(root.val)
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid+1:], postorder[mid:-1])
        return root

def test_solution1():
    def _height(x):
        if x is None:
            return 0
        else:
            return max(_height(x.left), _height(x.right)) + 1

    def levelorderTraversalWithNones(x):
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
        h = _height(x)
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

    inp = [([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]),
           ([-1],[-1])
           ]
    out = [[3, 9, 20, None, None, 15, 7],
           [-1]]

    for i in range(len(inp)):
        sol = Solution()
        root = sol.buildTree(inp[i][0],inp[i][1])
        test_res = levelorderTraversalWithNones(root)
        print('test_res', test_res)
        print("Test", i + 1, ":", "OK\n" if test_res == out[i] else "Failed\n")


if __name__ == '__main__':
    test_solution1()
