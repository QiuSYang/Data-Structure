"""
# 基于数组实现队列 --- 先进先出
"""
import os
import logging

logger = logging.getLogger(__name__)


class QueueByArray(object):
    """基于数组实现队列"""
    def __init__(self, capacity: int = 5):
        self._items = []
        self._capacity = capacity
        # 设置两个哨兵记录队首和队尾位置
        self._head = 0
        self._tail = 0

    def enqueue(self, item: str):
        """入列"""
        if self._tail == self._capacity:
            # 整理队列空间
            if self._head == 0:
                logger.info("已经没有空间可以继续存储数据")
                return False  # 队列被全部填满
            else:
                logger.info("整理已经空闲的内存重新使用")
                for i in range(self._tail - self._head):
                    # self._head空间可以重新利用
                    self._items[i] = self._items[i + self._head]
                self._tail = self._tail - self._head  # 尾部被往后推移self._head个位置
                self._head = 0

        self._items.insert(self._tail, item)  # 队尾插入元素
        self._tail += 1

        return True

    def dequeue(self):
        """出列"""
        if self._head == self._tail:
            return None

        item = self._items[self._head]
        self._head += 1

        return item

    def __repr__(self) -> str:
        return "->".join(item for item in self._items[self._head: self._tail])


if __name__ == '__main__':
    logging.basicConfig(format="[%(asctime)s %(filename)s:%(lineno)s] %(message)s",
                        level=logging.INFO,
                        filename=None,
                        filemode="a")

    S = QueueByArray(5)

    for i in range(5):
        S.enqueue(str(i))
    logger.info(S)
    S.enqueue("a")
    S.dequeue()
    S.dequeue()
    logger.info(S)
    S.enqueue("b")
    logger.info(S)
