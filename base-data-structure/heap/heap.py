"""
# 二叉树的特殊结构 --- 堆
"""
import os
import logging

logger = logging.getLogger(__name__)


class Heap(object):
    """堆, 二叉树root index为1, 即索引从1开始排"""
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


if __name__ == '__main__':
    logging.basicConfig(format="[%(asctime)s %(filename)s: %(lineno)s]: %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S",
                        level=logging.INFO,
                        filename=None,
                        filemode="a")
