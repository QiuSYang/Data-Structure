"""
基于数组实现动态队列(即使用已经被释放的内存)
"""
import os
import logging

logger = logging.getLogger(__name__)


class DynamicQueueByArray(object):
    """基于数组实现动态队列"""
    def __init__(self, capacity=5):
        self._items = []
        self.capacity = capacity
        self._head = 0
        self._tail = 0

    def enqueue(self, item: str):
        """入列"""
        if self._tail == self.capacity:
            if self._head == 0:
                # 没有多余容量可以被清理出来存储新的数据
                return False

            # tail指向的位置是没有包含元素的
            self._items[:self._tail - self._head] = self._items[self._head:self._tail]
            self._tail -= self._head  # tail指针回退head个位置
            self._head = 0  # head回退到对头

        if self._tail == len(self._items):
            self._items.append(item)  # 没有任何元素出栈, 直接在list尾部插入元素
        else:
            self._items[self._tail] = item  # 容器已满之后，改变对应位置的值
        # self._items.insert(self._tail, item)  # 上面整段代码与此句任选其一

        self._tail += 1

        return True

    def dequeue(self):
        """出栈"""
        if self._tail != self._head:
            item = self._items[self._head]
            self._head += 1

            return item

    def __repr__(self) -> str:
        return "->".join(item for item in self._items[self._head:self._tail])


if __name__ == '__main__':
    logging.basicConfig(format="[%(asctime)s %(filename)s:%(lineno)s] %(message)s",
                        level=logging.INFO,
                        filename=None,
                        filemode="a")
    q = DynamicQueueByArray(10)
    for i in range(10):
        q.enqueue(str(i))
    logger.info(q)

    for _ in range(3):
        q.dequeue()
    logger.info(q)

    q.enqueue("7")
    q.enqueue("8")
    logger.info(q)
