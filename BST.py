class TreeNode:

    def __init__(self, value):

        self.value = value

        self.left = None

        self.right = None

class BinarySearchTree:

    def __init__(self):

        self.root = None

    def insert(self, value):

        new_node = TreeNode(value)

        if not self.root:

            self.root = new_node

            return

        current = self.root

        while True:

            if value < current.value:

                if not current.left:

                    current.left = new_node

                    return

                current = current.left

            else:

                if not current.right:

                    current.right = new_node

                    return

                current = current.right

    def search(self, value):

        current = self.root

        while current:

            if value == current.value:

                return current

            elif value < current.value:

                current = current.left

            else:

                current = current.right

        return None
