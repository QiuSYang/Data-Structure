"""
# 自定义数组
    包含增、删、改、查功能
"""
import os
import logging

logger = logging.getLogger(__name__)


class CustomArray(object):
    """数据结构---自定义数组"""
    def __init__(self, capacity: int):
        self._data = []
        self._capacity = capacity

    def __getitem__(self, index: int):
        # find(查)
        return self._data[index]

    def __setitem__(self, index: int, value: object):
        # set(改)
        self._data[index] = value

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        for item in self._data:
            yield item

    def find(self, value: object):
        # 查找元素索引号
        try:
            return self._data.index(value)
        except ValueError:
            return None

    def delete(self, index: int):
        try:
            self._data.pop(index)
            return True
        except IndexError:
            return False

    def insert(self, index: int, value: int):
        if len(self) >= self._capacity:
            return False
        else:
            return self._data.insert(index, value)

    def show(self):
        for item in self:
            logger.info("value: {}".format(item))


def main():
    arr = CustomArray(5)
    arr.insert(0, 3)
    arr.insert(0, 4)
    arr.insert(1, 5)
    arr.insert(3, 9)
    arr.insert(3, 10)
    assert arr.insert(0, 100) is False
    assert len(arr) == 5
    assert arr.find(5) == 1
    assert arr.delete(4) is True
    arr.show()


if __name__ == "__main__":
    logging.basicConfig(format='[%(asctime)s %(filename)s:%(lineno)s] %(message)s',
                        level=logging.INFO,
                        filename=None,
                        filemode='a')
    logger.info("Start.")
    main()
