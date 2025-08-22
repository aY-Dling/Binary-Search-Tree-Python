class TreeNode:

    def __init__(self, value):

        self.value = value

        self.left = None

        self.right = None

class BinarySearchTree:

    def __init__(self):

        self.root = None
    #插入
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
    #搜尋
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
    #刪除
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
            # 找到要刪的節點
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            # 兩邊都有子樹，找右子樹的最小值來替代
            temp = self.min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete_helper(node.right, temp.value)

        return node

    def min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

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

# 删除员工编号 1002
bst.delete(1002)

# 再次搜索
result = bst.search(1002)
if result:
    print("删除失败，仍然找到编号为1002的节点")
else:
    print("成功删除编号为1002的节点")
