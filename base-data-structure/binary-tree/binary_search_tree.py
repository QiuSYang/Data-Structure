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


if __name__ == '__main__':
    logging.basicConfig(format="[%(asctime)s %(filename)s: %(lineno)s] %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S",
                        level=logging.INFO,
                        filename=None,
                        filemode="a")
