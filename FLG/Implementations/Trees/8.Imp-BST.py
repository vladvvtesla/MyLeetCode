"""
There is a structure to a BST. For a given node with a value, all the nodes in the left sub-tree
are less than or equal to the value of that node. Also, all the nodes in the right sub-tree of
this node are greater than that of the parent node.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class Tree:
    def __init__(self):
        self.root = None

    def find_min(self):
        """
        It takes O(h) to find the minimum or maximum value in a BST,
        where h is the height of thetree.
        """
        curr = self.root
        while curr.left:
            curr = curr.left
        return curr

    def find_max(self):
        """
        It takes O(h) to find the minimum or maximum value in a BST,
        where h is the height of thetree.
        """
        curr = self.root
        while curr.right:
            curr = curr.right
        return curr

    def insert(self, data):
        """Insertion of a node in a BST takes O(h), where h is the height of the tree."""
        node = Node(data)
        if self.root is None:
            self.root = node     # Insert into empty tree
        else:
            curr = self.root
            parent = None
            while True:
                parent = curr
                if node.data < curr.data:
                    curr = curr.left
                    if curr is None:
                        parent.left = node
                        return
                else:
                    curr = curr.right
                    if curr is None:
                        parent.right = node
                        return

    def get_node_with_parent(self, data):
        """
        1) If the node about to be removed has no children,
        we simply detach it from its parent:
        2) When the node we want to remove has one child, the parent of that node
        is made to point to the child of that particular node:
        3) more complex scenario arises when the node we want to delete
        has two children:

        Our node class does not have reference to a parent. As such, we need
        to use a helper method to search for and return the node with its parent node.
        This method is similar to the search method:
        :param data:
        :return:
        """
        parent = None
        curr = self.root
        if curr is None:
            return (parent, None)
        while True:
            if curr.data == data:
                return (parent, curr)
            elif curr.data > data:
                parent = curr
                curr = curr.left
            else:
                parent = curr
                curr = curr.right
            return (parent, curr)

    def remove(self, data):
        """The remove operation takes O(h), where h is the height of the tree."""
        parent, node = self.get_node_with_parent(data)
        if parent is None and node is None:
            return False
        # Get children count
        children_count = 0
        if node.left and node.right:
            children_count = 2
        elif (node.left is None) and (node.right is None):
            children_count = 0
        else:
            children_count = 1

        # No children
        if children_count == 0:
            if parent:
                if parent.right is node:
                    parent.right = None
                else:
                    parent.left = None
            else:
                self.root = None

        # one child
        elif children_count == 1:
            next = None
            if node.left:
                next = node.left
            else:
                next = node.right
            if parent:
                if parent.left is node:
                    parent.left = next
                else:
                    parent.right = next
            else:
                self.root = next

        # two children
        else:
            parent_of_leftmost = node
            leftmost = node.right
            while leftmost.left:
                parent_of_leftmost = leftmost
                leftmost = leftmost.left
            node.data = leftmost.data

            if parent_of_leftmost.left == leftmost:
                parent_of_leftmost.left = leftmost.right
            else:
                parent_of_leftmost.right = leftmost.right

    def search(self, data):
        """In this implementation, we will simply return the data if it was
           found or None if the data wasn't found
        """
        curr = self.root
        while True:
            if curr is None:
                return None
            elif curr.data is data:
                return data
            elif curr.data > data:
                curr = curr.left
            else:
                curr = curr.right


if __name__ == '__main__':
    # Test 1
    n1 = Node("root node")
    n2 = Node("left child node")
    n3 = Node("right child node")
    n4 = Node("left grandchild node")

    n1.left_child = n2
    n1.right_child = n3
    n2.left_child = n4

    curr = n1
    # while curr:
    #     print(curr.data)
    # curr = curr.left

    # Test 1
    print()
    tree = Tree()
    tree.insert(5)
    tree.insert(2)
    tree.insert(7)
    tree.insert(9)
    tree.insert(1)

    for i in range(1, 10):
        found = tree.search(i)
        print("{}: {}".format(i, found))