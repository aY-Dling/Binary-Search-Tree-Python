# 定义个类，来实现二叉搜索树
class TreeNode:

    def __init__(self, value):

        self.value = value

        self.left = None

        self.right = None
# 实现了插入和搜索这两个操作
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
# 创建一个二叉搜索树对象

bst = BinarySearchTree()

# 插入一些员工编号

bst.insert(1001)

bst.insert(1002)

bst.insert(1003)

# 假设要查找编号为1002的员工节点

result = bst.search(1002)

if result:

    print("找到编号为1002的员工节点")

else:

    print("未找到编号为1002的员工节点")

# 假设要插入新员工编号1004

bst.insert(1004)

# 二叉搜索树在员工管控软件中的删除操作

def delete(self, value):

    self.root = self._delete_helper(self.root, value)

def _delete_helper(self, node, value):

    if not node:

        return node

    if value < node.value:

        node.left = self._delete_helper(node.left, value)

    elif value > node.value:

        node.right = self._delete_helper(node.right, value)

    else:

        if not node.left:

            return node.right

        elif not node.right:

            return node.left

        temp = self.min_value_node(node.right)

        node.value = temp.value

        node.right = self._delete_helper(node.right, temp.value)

    return node

def min_value_node(self, node):

    current = node

    while current.left:

        current = current.left

    return current
