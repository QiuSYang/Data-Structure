"""
# 单向链表实现
"""
import os
import logging

logger = logging.getLogger(__name__)


class Node(object):
    """链表结构的Node节点"""

    def __init__(self, data, next_node=None):
        """Node节点的初始化方法.
        参数:
            data:存储的数据
            next:下一个Node节点的引用地址
        """
        self.__data = data
        self.__next = next_node

    @property
    def data(self):
        """Node节点存储数据的获取.
        返回:
            当前Node节点存储的数据
        """
        return self.__data

    @data.setter
    def data(self, data):
        """Node节点存储数据的设置方法.
        参数:
            data:新的存储数据
        """
        self.__data = data

    @property
    def next_node(self):
        """获取Node节点的next指针值.
        返回:
            next指针数据
        """
        return self.__next

    @next_node.setter
    def next_node(self, next_node):
        """Node节点next指针的修改方法.
        参数:
            next:新的下一个Node节点的引用
        """
        self.__next = next_node


if __name__ == '__main__':
    logging.basicConfig(format='[%(asctime)s %(filename)s:%(lineno)s] %(message)s',
                        level=logging.INFO,
                        filename=None,
                        filemode='a')
