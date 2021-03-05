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


class SingleLinkedList(object):
    """单向链表"""
    def __init__(self):
        self.__head = None  # 初始化链表头

    def insert_to_head(self, value):
        """在链表的头部插入一个存储value数值的Node节点.
        参数:
            value:将要存储的数据
        """
        node = Node(value)
        node.next_node = self.__head
        self.__head = node  # 将当前节点copy给头节点

    def insert_after(self, node, value):
        """在链表的某个指定Node节点之后插入一个存储value数据的Node节点.
        参数:
            node:指定的一个Node节点
            value:将要存储在新Node节点中的数据
        """
        if node is None:
            # 如果指定在一个空节点之后插入数据节点，则什么都不做
            return

        new_node = Node(value)
        new_node.next_node = node.next_node
        node.next_node = new_node

    def insert_before(self, node, value):
        """在链表的某个指定Node节点之前插入一个存储value数据的Node节点.
        参数:
            node:指定的一个Node节点
            value:将要存储在新的Node节点中的数据
        """
        if (node is None) or (self.__head is None):
            # 如果指定在一个空节点之前或者空链表之前插入数据节点，则什么都不做
            return

        if node == self.__head:
            # 如果是在链表头之前插入数据节点，则直接插入
            self.insert_to_head(value)
            return

        new_node = Node(value)
        pre = self.__head
        not_found = False  # 如果在整个链表中都没有找到指定插入的Node节点，则该标记量设置为True
        while pre.next_node != node:
            # 寻找指定Node之前的一个Node
            if pre.next_node is None:
                # 如果已经到了链表的最后一个节点，则表明该链表中没有找到指定插入的Node节点
                not_found = True
                break
            else:
                pre = pre.next_node  # 继续向下寻找
        if not not_found:
            # 查询到node节点
            pre.next_node = new_node
            new_node.next_node = node

    def find_by_value(self, value):
        """按照数据值在单向列表中查找.
        参数:
            value:查找的数据
        返回:
            Node
        """
        node = self.__head
        while node is not None and node.data != value:
            node = node.next_node

        return node

    def find_by_index(self, index):
        """按照索引值在列表中查找.
        参数:
            index:索引值
        返回:
            Node
        """
        node = self.__head
        pos = 0
        while node is not None and pos != index:
            node = node.next_node
            pos += 1

        return Node

    def delete_by_node(self, node):
        """在链表中删除指定Node的节点.
        参数:
            node:指定的Node节点
        """
        if self.__head is None:  # 如果链表是空的，则什么都不做
            return

        if node == self.__head:  # 如果指定删除的Node节点是链表的头节点
            self.__head = node.next_node
            return

        pro = self.__head
        not_found = False  # 如果在整个链表中都没有找到指定删除的Node节点，则该标记量设置为True
        while pro.next_node != node:
            if pro.next_node is None:
                # 如果已经到链表的最后一个节点，则表明该链表中没有找到指定删除的Node节点
                not_found = True
                break
            else:
                pro = pro.next_node
        if not not_found:
            # 删除node节点
            pro.next_node = node.next_node

    def delete_by_value(self, value):
        """在链表中删除指定存储数据的Node节点.
        参数:
            value:指定的存储数据
        """
        if self.__head is None:  # 如果链表是空的，则什么都不做
            return

        if self.__head.data == value:  # 如果链表的头Node节点就是指定删除的Node节点
            self.__head = self.__head.next_node

        pro = self.__head
        node = self.__head.next_node
        not_found = False
        while node.data != value:
            if node.next_node is None:
                # 如果已经到链表的最后一个节点，则表明该链表中没有找到执行Value值的Node节点
                not_found = True
                break
            else:
                pro = node
                node = node.next_node
        if not_found is False:
            pro.next_node = node.next_node

    def delete_last_n_node(self, n):
        """删除链表中倒数第N个节点.
        主体思路：
            设置快、慢两个指针，快指针先行，慢指针不动；当快指针跨了N步以后，快、慢指针同时往链表尾部移动，
            当快指针到达链表尾部的时候，慢指针所指向的就是链表的倒数第N个节点
        参数:
            n:需要删除的倒数第N个序数
        """
        fast = self.__head
        slow = self.__head

        step = 1
        while step <= n:
            #
            fast = fast.next_node
            step += 1

        while fast.next_node is not None:
            tmp = slow
            fast = fast.next_node
            slow = slow.next_node

        tmp.next_node = slow.next_node

    def find_mid_node(self):
        """查找链表中的中间节点.
        主体思想:
            设置快、慢两种指针，快指针每次跨两步，慢指针每次跨一步，则当快指针到达链表尾部的时候，慢指针指向链表的中间节点
        返回:
            node:链表的中间节点
        """
        fast = self.__head
        slow = self.__head

        while fast.next_node is not None:
            fast = fast.next_node.next_node
            slow = slow.next_node

        return slow

    def create_node(self, value):
        """创建一个存储value值的Node节点.
        参数:
            value:将要存储在Node节点中的数据
        返回:
            一个新的Node节点
        """
        return Node(value)

    def print_all(self):
        """打印当前链表所有节点数据."""
        pos = self.__head
        if pos is None:
            logger.info("当前链表还没有数据")
            return
        while pos.next_node is not None:
            logger.info(str(pos.data) + " --> ", end="")
            pos = pos.next_node
        logger.info(str(pos.data))

    def reversed_self(self):
        """翻转链表自身."""
        if self.__head is None or self.__head.next is None:  # 如果链表为空，或者链表只有一个节点
            return

        pre = self.__head
        node = self.__head.next
        while node is not None:
            pre, node = self.__reversed_with_two_node(pre, node)

        self.__head.next = None
        self.__head = pre

    def __reversed_with_two_node(self, pre, node):
        """翻转相邻两个节点.
        参数:
            pre:前一个节点
            node:当前节点
        返回:
            (pre,node):下一个相邻节点的元组
        """
        tmp = node.next_node
        node.next_node = pre
        pre = node  # 这样写有点啰嗦，但是能让人更能看明白
        node = tmp
        return pre, node

    def has_ring(self):
        """检查链表中是否有环.
        主体思想：
            设置快、慢两种指针，快指针每次跨两步，慢指针每次跨一步，如果快指针没有与慢指针相遇而是顺利到达链表尾部
            说明没有环；否则，存在环
        返回:
            True:有环
            False:没有环
        """
        fast = self.__head
        slow = self.__head

        while (fast.next_node is not None) and (fast is not None):
            fast = fast.next_node.next_node  # 快指针每次跨越两步
            slow = slow.next_node
            if fast == slow:
                return True

        return False

    def __iter__(self):
        """重写__iter__方法，方便for关键字调用打印值"""
        node = self.__head
        while node:
            yield node.data
            node = node.next_node


def merge_sorted_list(l1: Node, l2: Node):
    # 有序链表合并
    if l1 and l2:
        p1, p2 = l1, l2
        fake_head = Node(None)  # 头结点(哨兵)
        current = fake_head
        while p1 and p2:
            if p1.data <= p2.data:
                current.next_node = p1
                p1 = p1.next_node
            else:
                current.next_node = p2
                p2 = p2.next_node
            current = current.next_node  # 节点后移

        current.next_node = p1 if p1 else p2  # 操作最一个包含数据节点

        return fake_head.next_node

    return l1 or l2


if __name__ == '__main__':
    logging.basicConfig(format='[%(asctime)s %(filename)s:%(lineno)s] %(message)s',
                        level=logging.INFO,
                        filename=None,
                        filemode='a')

    l = SingleLinkedList()
    for i in range(15):
        l.insert_to_head(i)
    node9 = l.find_by_value(9)
    l.insert_before(node9, 20)
    l.insert_before(node9, 16)
    l.insert_before(node9, 16)
    l.delete_by_value(16)
    node11 = l.find_by_index(3)
    l.delete_by_node(node11)
    l.delete_by_value(13)

    for value in l:
        logger.info("value: {}".format(value))
