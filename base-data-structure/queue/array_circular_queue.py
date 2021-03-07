"""
# 基于数组实现训练队列
"""
import os
import logging
from itertools import chain

logger = logging.getLogger(__name__)


class CircularQueueByArray(object):
    """基于数组实现循环队列"""
    def __init__(self, capacity=5):
        self._items = []
        self._capacity = capacity + 1  # 预留一个空位留给尾部指针指向
        self._head = 0
        self._tail = 0

    def enqueue(self, item: str):
        """入栈"""
        if (self._tail + 1) % self._capacity == self._head:
            # 循环对列存储空间已经被填满(尾部指针已经没有可以指向的位置)
            return False

        self._items.append(item)  # 尾部插入元素
        self._tail = (self._tail + 1) % self._capacity  # 尾部指针指向的位置

        return True

    def dequeue(self):
        """出栈"""
        if self._head != self._tail:
            # 如果self._head == self._tail，循环队列为空
            item = self._items[self._head]
            self._head = (self._head + 1) % self._capacity
            return item

    def __repr__(self) -> str:
        if self._tail >= self._head:
            return "->".join(item for item in self._items[self._head: self._tail])
        else:
            return "->".join(item for item in chain(self._items[self._head:], self._items[:self._tail]))


if __name__ == '__main__':
    logging.basicConfig(format="[%(asctime)s %(filename)s:%(lineno)s] %(message)s",
                        level=logging.INFO,
                        filename=None,
                        filemode="a")
    q = CircularQueueByArray(5)
    for i in range(5):
        q.enqueue(str(i))
    q.dequeue()
    q.dequeue()
    q.enqueue(str(5))
    logger.info(q)
