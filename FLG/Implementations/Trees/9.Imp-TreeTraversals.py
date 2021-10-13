class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class Tree:
    def __init__(self):
        self.root = None


    def inorder(self, root):
        current = root
        if current is None:
            return
        self.inorder(current.left)
        print(current.data)
        self.inorder(current.right)

    def preorder(self, root):
        current = root
        if current is None:
            return
        print(current.data)
        self.preorder(current.left)
        self.preorder(current.right)

    def postorder(self, root):
        current = root
        if current is None:
            return
        self.postorder(current.left)
        self.postorder(current.right)
        print(current.data)


    def level_order_traversal(self, root):    # breadth_first_traversal
        from collections import deque
        list_of_nodes = []
        traversal_queue = deque([root])

        while len(traversal_queue) > 0:
            node = traversal_queue.popleft()
            list_of_nodes.append(node.data)
            if node.left_child:
                traversal_queue.append(node.left)
            if node.right_child:
                traversal_queue.append(node.right)
        return list_of_nodes