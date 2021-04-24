"""
# 二叉树实例
"""
import os
import logging

logger = logging.getLogger(__name__)


class TreeNode(object):
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Node(object):
    """definition a tree node"""
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def invertTree(self, root: TreeNode) -> TreeNode:
        """前序遍历树"""
        if root is None:
            return None
        temp = root.left
        root.left = root.right
        root.right = temp  # 左右子树交换

        # 让左右子节点继续翻转它们的子节点
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        self.tow_node_connect(root.left, root.right)
        return root

    def tow_node_connect(self, node1: 'Node', node2: 'Node') -> 'Node':
        if node1 is None or node2 is None:
            return

        # 前序遍历
        node1.next = node2

        self.tow_node_connect(node1.left, node1.right)  # 左右节点连接
        self.tow_node_connect(node2.left, node2.right)

        self.tow_node_connect(node1.right, node2.left)  # 右节点与左节点相连

    def flatten(self, root: TreeNode) -> TreeNode:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return root
            # 后序遍历
        self.flatten(root.left)
        self.flatten(root.right)

        # 1、左右子树已经被拉平成一条链表
        left = root.left
        right = root.right

        # 2、将左子树作为右子树
        root.left = None  # 左节点置空
        root.right = left  # 右节点连接当前节点的左节点

        # 3、将原先的右子树接到当前右子树的末端
        temp = root
        while temp.right is not None:
            temp = temp.right  # 找到右节点为空的位置
        temp.right = right  # 左右节点连接

        return root


if __name__ == '__main__':
    logging.basicConfig(format="[%(asctime)s %(filename)s:%(lineno)s] %(message)s",
                        level=logging.INFO,
                        filemode="a",
                        filename=None)
