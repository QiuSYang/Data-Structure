"""
# 二叉搜索树: 当前节点左子树的所有值都小于当前节点值, 右子树的所有值都大于当前节点值
"""
import os
import logging
import math
from queue import Queue

logger = logging.getLogger(__name__)


class TreeNode(object):
    """树节点"""
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class BinarySearchTree(object):
    """二叉搜索树"""
    def __init__(self, values: list = []):
        self.root = None  # 根节点
        for value in values:
            self.insert(value)

    def insert(self, data):
        """树节点插入"""
        assert isinstance(data, int)

        if self.root is None:
            self.root = TreeNode(val=data)
        else:
            current = self.root
            p = None
            while current:
                # 一直访问到current节点为空, 说明已经找到要插入位置
                p = current
                if data < current.val:
                    # 应该插入在左子树
                    current = current.left
                else:
                    # 应该插入在右子树
                    current = current.right

            new_node = TreeNode(data)
            new_node.parent = p

            if data < p.val:
                # 插入到父节点左子树
                p.left = new_node
            else:
                # 插入到父节点右子树
                p.right = new_node

        return True

    def search(self, data):
        """搜索, 范围树中所有为data值的节点列表"""
        assert isinstance(data, int)

        ret = []  # 存储搜索到的所有节点
        current = self.root
        while current:
            if data < current.val:
                # 小于data的值只存在于左子树中
                current = current.right
            else:
                # 大于等于data节点只存在于右子树中
                if data == current.val:
                    ret.append(current)
                current = current.right  # 继续向搜索, 直到current节点为None

        return ret

    def delete(self, data):
        """删除节点"""
        assert isinstance(data, int)

        # 通过搜素得到需要删除的节点
        del_list = self.search(data)
        for n in del_list:
            # 父节点为空，又不是根节点，已经不在树上，不用再删除
            if n.parent is None and n != self.root:
                continue
            else:
                self._del(n)

    def _del(self, node: TreeNode):
        """ 删除
        所删除的节点N存在以下情况：
        1. 没有子节点：直接删除N的父节点指针
        2. 有一个子节点：将N父节点指针指向N的子节点
        3. 有两个子节点：找到右子树的最小节点M，将值赋给N，然后删除M
        """
        # 1
        if node.left is None and node.right is None:
            # 当前节点左右子树都为空
            if node == self.root:
                self.root = None
            else:
                if node.val < node.parent.val:
                    # 当前节点存在于父节点左树
                    node.parent.left = None  # 指空
                else:
                    # 当前节点存在于父节点右树
                    node.parent.right = None
            node.parent = None  # 当前节点与父节点断开
        # 2
        elif node.left is None and node.right is not None:
            # 存在右子树
            if node == self.root:
                self.root = node.right
                self.root.parent = None  # 与父节点断开
                node.right = None  # 与当前节点右树断开
            else:
                if node.val < node.parent.val:
                    # 当前节点存在于父节点左树
                    node.parent.left = node.right
                else:
                    # 当前节点存在于父节点右树
                    node.parent.right = node.right
                node.right.parent = node.parent  # 新的两个节点相连
                node.right = None
                node.parent = None
        elif node.left is not None and node.right is None:
            if node == self.root:
                self.root = node.left
                self.root.parent = None
                node.right = None
            else:
                if node.val < node.parent.val:
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left
                node.left.parent = node.parent
                node.left = None
                node.parent = None
        # 3
        else:
            min_node = node.right
            # 找到右子树的最小值节点, 右树所有节点都大于左树节点
            while min_node.left:
                min_node = min_node.left
            if node.val != min_node.val:
                # 当前节点值替换为右树的最小节点, 继续保持当前节点的右数都大于该节点左树所有节点, 小于该节点右树所有节点
                node.val = min_node.val
                self._del(min_node)
            else:
                # 右子树的最小值节点与被删除节点的值相等，再次删除原节点
                self._del(min_node)  # 先删除最小节点
                self._del(node)  # 再重新删除该节点

    def get_min(self):
        """返回最小值"""
        if self.root is None:
            return None
        n = self.root
        while n.left:
            # 连续访问左树
            n = n.left

        return n.val

    def get_max(self):
        """返回最大值"""
        if self.root is None:
            return None

        n = self.root
        while n.right:
            # 连续访问右树
            n = n.right

        return n.val

    def order(self):
        """排序"""
        if self.root is None:
            return []

        return self._in_order(self.root)

    def _in_order(self, node):
        """中序遍历, 进行排序, 二叉查找树的特点决定"""
        if node is None:
            return []

        ret = []
        n = node
        ret.extend(self._in_order(n.left))
        ret.append(n.val)
        ret.extend(self._in_order(n.right))

        return ret

    def _draw_tree(self):
        """可视化"""
        nodes = self._bfs()

        if not nodes:
            print('This tree has no nodes.')
            return

        layer_num = int(math.log(nodes[-1][1], 2)) + 1

        prt_nums = []

        for i in range(layer_num):
            prt_nums.append([None] * 2 ** i)

        for v, p in nodes:
            row = int(math.log(p, 2))
            col = p % 2 ** row
            prt_nums[row][col] = v

        prt_str = ''
        for l in prt_nums:
            prt_str += str(l)[1:-1] + '\n'

        return prt_str

    def _bfs(self):
        """宽度优先搜索, 一层一层从左向右访问节点
           通过父子关系记录节点编号
        """
        if self.root is None:
            return []

        ret = []
        q = Queue()  # 先进先出
        # 队列[节点, 编号]
        q.put((self.root, 1))
        while not q.empty():
            n = q.get()  # 队列元素出列
            if n[0] is not None:
                ret.append((n[0].val, 1))
                q.put((n[0].left, n[1]*2))  # 当前节点左节点入列
                q.put((n[0].right, n[1]*2+1))  # 当前节点右节点入列

        return ret

    def __repr__(self):
        logger.info(str(self.order()))  # 中序遍历
        return self._draw_tree()


if __name__ == '__main__':
    logging.basicConfig(format="[%(asctime)s %(filename)s: %(lineno)s] %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S",
                        level=logging.INFO,
                        filename=None,
                        filemode="a")
    nums = [4, 2, 5, 6, 1, 7, 3]
    bst = BinarySearchTree(nums)
    logger.info(bst)

    # 插入
    bst.insert(1)
    bst.insert(4)
    logger.info(bst)

    # 搜索
    for n in bst.search(2):
        logger.info(n.parent.val, n.val)

    # 删除
    bst.insert(6)
    bst.insert(7)
    logger.info(bst)
    bst.delete(7)
    logger.info(bst)
    bst.delete(6)
    logger.info(bst)
    bst.delete(4)
    logger.info(bst)

    # min max
    logger.info(bst.get_max())
    logger.info(bst.get_min())
