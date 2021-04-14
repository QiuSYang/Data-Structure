"""
# 二叉树的特殊结构 --- 堆
    二叉树root index为1, 即索引从1开始排
"""
import os
import logging
from typing import Optional, List

logger = logging.getLogger(__name__)


class Heap(object):
    """堆"""
    def __init__(self, capacity: int):
        self._data = [0] * (capacity + 1)
        self._capacity = capacity
        self._count = 0

    @classmethod
    def _get_parent_index(cls, child_index: int) -> int:
        """get the parent index"""
        return child_index // 2

    @classmethod
    def _get_left_index(cls, parent_index: int) -> int:
        """get the left child index"""
        return 2 * parent_index

    @classmethod
    def _get_right_index(cls, parent_index: int) -> int:
        """get the right child index"""
        return 2 * parent_index + 1

    @classmethod
    def _siftdown(cls, data: List[int],
                  count: int, root_index: int = 1) -> None:
        """向下堆二叉树"""
        current_index = larger_child_index = root_index
        while True:
            left_index, right_index = cls._get_left_index(current_index), cls._get_right_index(current_index)
            # 获取父, 左, 右三个节点的最大值位置
            if left_index <= count and data[current_index] < data[left_index]:
                larger_child_index = left_index
            if right_index <= count and data[larger_child_index] < data[right_index]:
                larger_child_index = right_index
            if larger_child_index == current_index:
                break  # 当前相对最大值已经位于父节点

            data[current_index], data[larger_child_index] = data[larger_child_index], data[current_index]
            current_index = larger_child_index  # 三个节点最大值位于父节点

    def _siftup(self) -> None:
        """向上堆化"""
        current_index, parent_index = self._count, self._get_parent_index(self._count)
        while parent_index and self._data[current_index] > self._data[parent_index]:
            # 父索引没有越界, 父节点值大于当前节点值, 继续向上堆化
            self._data[current_index], self._data[parent_index] = self._data[parent_index], self._data[current_index]
            current_index, parent_index = parent_index, self._get_parent_index(parent_index)

    def insert(self, value: int) -> None:
        """insert tree node"""
        if self._count >= self._capacity:
            # 节点已经满
            return
        self._count += 1  # 索引从1开始建立
        self._data[self._count] = value
        self._siftup()  # 向上建堆

    def remove_max(self) -> Optional[int]:
        """获取堆的最大值, 根节点存储最大值"""
        if self._count:
            result = self._data[1]  # 0 discard, index start from 1
            self._data[1] = self._data[self._count]
            self._count -= 1
            self._siftdown(self._data, self._count)  # 重新堆化

            return result

    @classmethod
    def build_heap(cls, data: List[int]) -> None:
        """建堆"""
        for i in range((len(data) - 1)//2, 0, -1):
            # 仅仅需要从数组中间开始, 二叉树的父节点是整个节点的一半
            cls._siftdown(data, len(data)-1, i)

    @classmethod
    def sort(cls, data: List[int]) -> None:
        """使用堆对数组排序,
        Data in a needs to start from index 1"""
        cls.build_heap(data)
        k = len(data) - 1
        while k > 1:
            # 根和最后元素交换, 相当于将最大元素移动到最后
            data[1], data[k] = data[k], data[1]
            k -= 1  # 数组data长度缩减1
            cls._siftdown(data, k)

    def __repr__(self):
        return self._data[1:self._count+1].__repr__()


if __name__ == '__main__':
    logging.basicConfig(format="[%(asctime)s %(filename)s: %(lineno)s]: %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S",
                        level=logging.INFO,
                        filename=None,
                        filemode="a")
    hp = Heap(10)
    hp.insert(3)
    hp.insert(9)
    hp.insert(1)
    hp.insert(8)
    hp.insert(7)
    hp.insert(3)
    logger.info(hp)
    for _ in range(6):
        logger.info(hp.remove_max())
    data = [0, 6, 3, 4, 0, 9, 2, 7, 5, -2, 8, 1, 6, 10]
    Heap.sort(data)
    logger.info(data[1:])
