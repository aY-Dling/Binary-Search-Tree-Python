# 南華大學資料結構-第二次期中報告(ex-7題目)    11124209蔡岱伶
# 员工管控软件里的 Python 二叉搜索树算法，一文讲明白！
在现代企业管理里，员工管控软件可是提升管理效率、优化资源配置的关键工具。这类软件得高效处理大量员工数据，而数据结构和算法选得好不好，对它的性能影响特别大。这篇文章就来仔细讲讲 Python 里的二叉搜索树（Binary Search Tree，BST）算法，看看它在员工管控软件里是怎么用的，还会通过具体代码例子，让大家见识一下它有多厉害。
![期末截圖01](https://github.com/aY-Dling/REPORT_-Exam/blob/main/%E6%9C%9F%E6%9C%AB%E6%88%AA%E5%9C%9601.jpeg?raw=true)

### 二叉搜索树算法简介

二叉搜索树是一种特殊的二叉树结构，每个节点都有个特点：左边子树里所有节点的值，都比这个节点的值小；右边子树里所有节点的值，都比这个节点的值大。有了这个特点，二叉搜索树在查找、插入和删除数据的时候，效率就很高。在员工管控软件里，我们可以把员工的唯一标识，比如员工编号，当作节点的值，再把员工的详细信息，像部门、职位、工作绩效这些，存到节点里。这样一来，用二叉搜索树就能把员工数据管理得井井有条，不管是查找还是更新，都能很快完成。

### Python 中二叉搜索树的实现

在 Python 里，我们可以自己定义个类，来实现二叉搜索树。下面这段代码，就是一个简单的二叉搜索树节点类，还有基本操作的示例：

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
