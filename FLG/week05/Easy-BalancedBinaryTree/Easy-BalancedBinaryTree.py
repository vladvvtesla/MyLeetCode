"""
110. Balanced Binary Tree - Easy

Main Idea
We should solve it using Dynamic Programming

1. Fore each node get its height recursively and put height into auxiliary array
2. for each node
    if x.left.height - x.right.height > 1 or x.left.height - x.right.height < -1
        return False

Leaf has height 1


Time complexity:  ~ O(N)
    get height for each node O(N)
    add height to auxiliary array O(1)
    check if nodes subtrees are balanced O(1)
    We don't check all subtrees

Space complexity: O(N)
    N for tree nodes plus extra array for auxiliary

Runtime: 56 ms, faster than 42.54% of Python3 online submissions for Balanced Binary Tree.
Memory Usage: 18.4 MB, less than 53.73% of Python3 online submissions for Balanced Binary Tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.count = 1  # number of nodes in subtree including itself

class Solution:
    def isBalanced(self, root):
        if not root:
            return True

        aux = [0]*5000

        def _height(x, k):
            """
            Calculate height of left and right subtree recursively
            Fill auxiliary array of subtrees height
            Raise Exception() if h_left and h_right difference is more than 1
            :param x:  binary tree node
            :return:   node's height
            """
            if not x.left and not x.right:                 # End of branch
                aux[k] = 1                                 # leaf's height is 1

            elif x.left and x.right:
                if aux[2*k] and aux[2*k+1]:
                    aux[k] = max(aux[2*k],aux[2*k+1]) + 1
                else:
                    aux[k] = max(_height(x.left, 2*k), _height(x.right, 2*k+1)) + 1

            elif x.left:
                if aux[2*k]:
                    aux[k] = aux[2*k] + 1
                else:
                    aux[k] = _height(x.left, 2*k) + 1
            else:                                          # x.right
                if aux[2*k]:
                    aux[k] = aux[2*k+1] + 1
                else:
                    aux[k] = _height(x.right, 2*k+1) + 1

            # Check if balanced
            if (aux[2*k] - aux[2*k + 1] > 1) or (aux[2*k] - aux[2*k + 1] < -1):
                raise Exception()

            return aux[k]

        # To break out of a recursive function in Python is to throw an exception
        try:
            _height(x=root, k=1)
            return True
        except:
            return False


def test_isBalanced():
    # Test 1 : [3,9,20,None,None,15,7]  Expected True
    root = Node(3,3)
    root.left = Node(9,9)
    root.right = Node(20,20)
    root.right.left = Node(15,15)
    root.right.right = Node(7,7)
    sol = Solution()
    test_res = sol.isBalanced(root)
    print('test_res', test_res)
    print("Test", 1, ":", "OK\n" if test_res == True else "Failed\n")

    # Test 2 : [1,2,2,3,3,None,None,4,4]  Expected False
    root = Node(1,1)
    root.left = Node(2,2)
    root.right = Node(2,2)
    root.left.left = Node(3,3)
    root.left.right = Node(3,3)
    root.left.left.left = Node(4,4)
    root.left.left.right = Node(4,4)
    sol = Solution()
    test_res = sol.isBalanced(root)
    print('test_res', test_res)
    print("Test", 2, ":", "OK\n" if test_res == False else "Failed\n")

    # Test 3 : []  Expected True
    root = None
    sol = Solution()
    test_res = sol.isBalanced(root)
    print('test_res', test_res)
    print("Test", 4, ":", "OK\n" if test_res == True else "Failed\n")

    # Test 5 : [1,1]  Expected True
    root = Node(1,1)
    root.left = Node(1,1)
    sol = Solution()
    test_res = sol.isBalanced(root)
    print('test_res', test_res)
    print("Test", 5, ":", "OK\n" if test_res == True else "Failed\n")

    # Test 6 : [1,none 1]  Expected True
    root = Node(1,1)
    root.right = Node(1,1)
    sol = Solution()
    test_res = sol.isBalanced(root)
    print('test_res', test_res)
    print("Test", 6, ":", "OK\n" if test_res == True else "Failed\n")

    # Test 7 : [5,4,3]  Expected False
    root = Node(5,5)
    root.left = Node(4,4)
    root.left.left = Node(3,3)
    sol = Solution()
    test_res = sol.isBalanced(root)
    print('test_res', test_res)
    print("Test", 7, ":", "OK\n" if test_res == False else "Failed\n")

    # Test 8 : [5,None,4,None,None,None,3]  Expected False
    root = Node(5,5)
    root.right = Node(4,4)
    root.right.right = Node(3,3)
    sol = Solution()
    test_res = sol.isBalanced(root)
    print('test_res', test_res)
    print("Test", 8, ":", "OK\n" if test_res == False else "Failed\n")


if __name__ == '__main__':
    test_isBalanced()