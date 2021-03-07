"""
# 基于链表实现队列
"""
import os
import logging

logger = logging.getLogger(__name__)


class Node(object):
    """定义节点"""
    def __init__(self, data: str, next=None):
        self.data = data
        self.next = next


class QueueByLinked(object):
    """基于链表实现队列"""
    def __init__(self):
        self._head: Node = None
        self._tail: Node = None

    def enqueue(self, value: str):
        """入列"""
        new_node = Node(data=value)
        if self._tail:
            # tail 节点包含数据
            self._tail.next = new_node
        else:
            # 队列为空
            self._head = new_node
        self._tail = new_node  # 队列尾部指向当前节点

    def dequeue(self):
        """出列"""
        if self._head:
            curent_node = self._head  # 对头出栈
            self._head = curent_node.next  # 对头指向next node
            if not self._head:
                # 队列仅包含一个元素，当前元素已经被取出, 因此队尾置空
                self._tail = None

            return curent_node.data

    def __repr__(self) -> str:
        values = []
        current = self._head
        while current:
            values.append(current.data)
            current = current.next
        return "->".join(value for value in values)


if __name__ == '__main__':
    logging.basicConfig(format="[%(asctime)s %(filename)s:%(lineno)s] %(message)s",
                        level=logging.INFO,
                        filename=None,
                        filemode="a")

    q = QueueByLinked()
    for i in range(10):
        q.enqueue(str(i))
    logger.info(q)

    for _ in range(3):
        q.dequeue()
    logger.info(q)

    q.enqueue("7")
    q.enqueue("8")
    logger.info(q)
