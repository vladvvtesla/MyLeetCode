"""


Top-Medium  - 116. Populating Next Right Pointers in Each Node



Main Idea:

Сделать массив, у которого в ячейках Ноды
и

Time cmplexity:

Space complexity:

Runtime: 73 ms, faster than 28.49% of Python3 online submissions for Populating Next Right Pointers in Each Node.
Memory Usage: 15.7 MB, less than 33.19% of Python3 online submissions for Populating Next Right Pointers in Each Node.

"""



# Definition for a Node.
class Node:
    def __init__(self, val=0, left = None, right = None, next = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, x):
        print('x.val', x.val)
        if not x:                    # edge case
            return

        if x.left:
            x.left.next = x.right                    # 2 -> 3

            if x.left.right and x.right.left:
                x.left.right.next = x.right.left     # 5 -> 6

        if x.right:
            if x.next and x.next.left:
                x.right.next = x.next.left           # 9 -> 10

            self.connect(x.left)
            self.connect(x.right)

        return x


def _height(x):
    if x is None:
        return 0
    else:
        return max(_height(x.left), _height(x.right)) + 1

def levelorderTraversalWithNones(x):
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


def test_solution1():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)


    sol = Solution()
    new_root = sol.connect(root)
    test_res = levelorderTraversalWithNones(new_root)
    print('test_res', test_res)
    print("Test 1", ":", "OK\n" if test_res == [1, 2, 3, 4, 5, 6, 7] else "Failed\n")



if __name__ == '__main__':
    test_solution1()