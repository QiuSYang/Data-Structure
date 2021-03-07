"""
# 基于链表实现循环链表
"""
import os
import logging

logger = logging.getLogger(__name__)


class Node(object):
    """创建链表节点数据结构"""
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Error(Exception):
    """异常处理"""
    def __init__(self, msg='empty'):
        super().__init__(self)
        self.msg = msg

    def __str__(self):
        return "ErrorMsg: ".format(self.msg)


class CircularQueueByLinked(object):
    """基于链表实现循环队列"""
    def __init__(self, capacity=3):
        self.tail: Node = None  # 循环队列只有一个哨兵, 链尾指向链头
        self.size = 0
        self.capacity = 3

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def enqueue(self, value):
        """入列"""
        if self.size > self.capacity:
            raise Error(msg="队列容量已满，不能插入新的元素。")

        new_node = Node(value)
        if self.is_empty():
            # 空队列
            new_node.next = new_node  # next指向自身
        else:
            # 队尾插入元素
            new_node.next = self.tail.next  # 新的元素指向对首(循环队列队尾永远指向队首)
            self.tail.next = new_node

        self.tail = new_node  # 队尾指向当前节点
        self.size += 1

    def dequeue(self):
        """出列"""
        if self.is_empty():
            raise Error(msg="队列没有数据。")

        head = self.tail.next

        if self.size == 1:
            self.tail = None  # 队列仅一个元素，取出元素之后队列为空
        else:
            sec_head = head.next
            self.tail.next = sec_head  # 队列尾部指向新的头部，即被取出元素的next

        self.size -= 1

        return head

    def get_head(self):
        if self.is_empty():
            raise Error()

        return self.tail.next  # tail next 即为 head


if __name__ == '__main__':
    logging.basicConfig(format="[%(asctime)s %(filename)s:%(lineno)s] %(message)s",
                        level=logging.INFO,
                        filename=None,
                        filemode="a")
    logger.info("Start")

    S = CircularQueueByLinked()

    S.enqueue(1)
    logger.info("{} - {} - {}".format(S.get_head(), len(S), S.size))
    logger.info(S.dequeue())
    S.enqueue(2)
    logger.info("{} - {}".format(S.get_head(), len(S)))
    logger.info(S.dequeue())
    S.enqueue(3)
    logger.info("{} - {}".format(S.get_head(), len(S)))
    logger.info(S.dequeue())
    S.enqueue(4)
    logger.info("{} - {}".format(S.get_head(), len(S)))
    S.enqueue(5)
    S.enqueue(6)
    logger.info('len: {}'.format(len(S)))
