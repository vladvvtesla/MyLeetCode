class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class Tree:
    def __init__(self):
        self.root = None

    def inorder(self, root):
        cur = root
        if cur is None:
            return
        self.inorder(cur.left)
        print(cur.data)
        self.inorder(cur.right)

    def preorder(self, root):
        cur = root
        if cur is None:
            return
        print(cur.data)
        self.preorder(cur.left)
        self.preorder(cur.right)

    def postorder(self, root):
        cur = root
        if cur is None:
            return
        self.postorder(cur.left)
        self.postorder(cur.right)
        print(cur.data)


    def levelorder(self, root):    # breadth_first_traversal
        from collections import deque
        list_of_nodes = []
        queue = deque([root])

        while len(queue) > 0:
            node = queue.popleft()
            list_of_nodes.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return list_of_nodes