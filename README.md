# 南華大學資料結構-第二次期中報告(ex-7題目)    11124209蔡岱伶
# 员工管控软件里的 Python 二叉搜索树算法，一文讲明白！
在现代企业管理里，员工管控软件可是提升管理效率、优化资源配置的关键工具。这类软件得高效处理大量员工数据，而数据结构和算法选得好不好，对它的性能影响特别大。这篇文章就来仔细讲讲 Python 里的二叉搜索树（Binary Search Tree，BST）算法，看看它在员工管控软件里是怎么用的，还会通过具体代码例子，让大家见识一下它有多厉害。

![BST01](https://github.com/aY-Dling/Binary-Search-Tree-Python/blob/main/BST01.jpeg?raw=true)

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
在上面这段代码里，我们定义了TreeNode类，用来表示二叉搜索树的节点，每个节点都有一个值，还有指向左子节点和右子节点的引用。BinarySearchTree类实现了插入和搜索这两个操作。通过insert方法，我们能把员工编号插到二叉搜索树里，search方法则可以根据员工编号，找到对应的节点。

### 二叉搜索树在员工管控软件中的查找操作

查找，是员工管控软件里经常要用到的操作。比如说，企业想根据员工编号，快速查到这个员工的详细信息。在二叉搜索树里，查找操作的时间复杂度平均是 O (log n)，这里的 n 指的是节点数量。也就是说，员工数据特别多的时候，也能很快找到目标员工。

 #创建一个二叉搜索树对象
 
    bst = BinarySearchTree()

 #插入一些员工编号

    bst.insert(1001)

    bst.insert(1002)

    bst.insert(1003)

 #假设要查找编号为1002的员工节点

    result = bst.search(1002)

    if result:

        print("找到编号为1002的员工节点")

    else:

        print("未找到编号为1002的员工节点")
这段代码里，我们先创建了一个二叉搜索树对象，然后插进去几个员工编号。接着用search方法，去找编号是 1002 的员工节点，最后根据找到没找到，给出相应的提示。

### 二叉搜索树在员工管控软件中的插入操作

有新员工入职了，员工管控软件就得把新员工的信息插到数据结构里。在二叉搜索树里，插入操作和查找操作差不多，也是通过比较节点的值，来确定新节点该放在哪儿。

 #假设要插入新员工编号1004

    bst.insert(1004)

调用insert方法，新员工的编号就能插到二叉搜索树里，而且还能保证二叉搜索树的特性不变。

### 二叉搜索树在员工管控软件中的删除操作

员工离职了，或者因为别的原因，要从系统里删掉他们的信息，这时候二叉搜索树的删除操作就派上用场了。删除操作稍微复杂点，得考虑好几种情况，比如要删的节点是叶子节点，或者只有一个子节点，再或者有两个子节点。

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

上面这段代码里，delete方法是对外提供的删除接口，它会调用_delete_helper方法，真正去执行删除操作。这个方法会根据节点的不同情况，做相应处理，保证删掉节点后，二叉搜索树还是原来的样子。

在实际的员工管控软件里，二叉搜索树可能会和其他数据结构或者技术一起用。比如说，可以把二叉搜索树和数据库连起来，实现数据的持久化存储。另外，为了让性能更好，可能还得优化二叉搜索树，像平衡二叉搜索树（AVL 树或红黑树），这样就能避免树长得太高，影响性能。

![BST02](https://github.com/aY-Dling/Binary-Search-Tree-Python/blob/main/BST02.jpeg?raw=true)

员工管控软件可是企业管理的核心工具之一，要提升它的性能，就得深入理解和优化底层的数据结构和算法。Python 里的二叉搜索树算法，查找、插入和删除都很快，给员工管控软件的数据管理帮了大忙。合理用好二叉搜索树，就能快速处理员工信息，满足企业管理的各种需求。以后软件开发的时候，企业业务会不断拓展，数据量也会越来越大，对二叉搜索树这类数据结构的研究和改进，还会继续推动员工管控软件向前发展。
