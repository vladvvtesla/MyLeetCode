"""
103. Binary Tree Zigzag Level Order Traversal


"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def zigzagLevelOrder(self, root):
    #     return [self.zigzagLevelOrder(root.left)] + [root.val] + [self.zigzagLevelOrder(root.right)] if root else None



    def zigzagLevelOrder(self, root):

        def _height(x):
            if x is None:
                return 0
            else:
                return max(_height(x.left), _height(x.right)) + 1

        def _reverse(x):
            n = len(x)
            for k in range(n//2):
                x[k],x[n-k-1] = x[n-k-1],x[k]


        # Create an list of Nones for result  N = 2**h - 1
        height = _height(root)
        levelorderlist = [None] * (2**height - 1)

        # Create an empty queue for level order traversal
        queue = []

        # Enqueue Root and node index in res. For root index is 0
        queue.append((root, 0))

        while (len(queue) > 0):
            # Insert front of queue into res and remove it from queue
            p_idx = queue[0][1]
            levelorderlist[p_idx] = queue[0][0].val
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


        # Make list of lists from levelorderlist
        #  [3, 9, 20, None, None, 15, 7] -> [[3], [9, 20], [None, None, 15, 7]]
        res = []
        tmp = []
        for h in range(1,height+1):
            print('h', h)
            if h == 1:
                res.append([levelorderlist[0]])
            else:
                tmp = levelorderlist[(2**(h-1)-1):(h**2)-1]
                res.append(tmp)

        # Del all Nones
        for i in res:
            i[:] = [k for k in i if k is not None]
        print('res', res)

        # Reverse odd level
        for k,v in enumerate(res):
            if k % 2 != 0:
                _reverse(v)
        print('res', res)

        return res

def test_Solution1():
    t = TreeNode(3)
    t.left = TreeNode(9)
    t.right = TreeNode(20)
    t.right.left = TreeNode(15)
    t.right.right = TreeNode(7)

    sol = Solution()
    test_res = sol.zigzagLevelOrder(t)
    print('test_res', test_res)
    print("Test", 1, ":", "OK\n" if test_res == [[3],[20,9],[15,7]] else "Failed\n")

def test_Solution2():
    t = TreeNode(1)

    sol = Solution()
    test_res = sol.zigzagLevelOrder(t)
    print('test_res', test_res)
    print("Test", 2, ":", "OK\n" if test_res == [[1]] else "Failed\n")

def test_Solution3():
    t = TreeNode(None)

    sol = Solution()
    test_res = sol.zigzagLevelOrder(t)
    print('test_res', test_res)
    print("Test", 3, ":", "OK\n" if test_res == [[]] else "Failed\n")

def test_Solution4():
    t = TreeNode(3)
    t.left = TreeNode(9)
    t.right = TreeNode(20)
    t.right.left = TreeNode(15)
    t.right.right = TreeNode(7)
    t.right.right.left = TreeNode(48)
    t.right.right.right = TreeNode(41)

    sol = Solution()
    test_res = sol.zigzagLevelOrder(t)
    print('test_res', test_res)
    print("Test", 4, ":", "OK\n" if test_res == [[3],[20,9],[15,7]] else "Failed\n")


if __name__ == '__main__':
    test_Solution1()
    test_Solution2()
    test_Solution3()
    test_Solution4()
