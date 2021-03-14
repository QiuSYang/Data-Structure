"""
# 计数排序
"""
import os
import logging
import itertools

logger = logging.getLogger(__name__)


def counting_sort(arr: list):
    """计数排序"""
    counts = [0] * (max(arr) + 1)  # 0~max包含max+1个元素
    for element in arr:
        # 计数，统计每个元素出现的次数, counts的索引代表arr中的元素值
        counts[element] += 1

    counts = list(itertools.accumulate(counts))  # 统计arr中某个元素应该出现位置, 即统计arr有多少个比某个元素小

    new_arr = [0] * len(arr)
    for element in reversed(arr):
        # 数组反转，是为了保证数组中相同的元素先出现依然排在前面
        index = counts[element] - 1  # 获取当前元素在排序数组中位置，-1因为下标索引从0开始
        new_arr[index] = element
        counts[element] -= 1  # 取出一个元素之后那么比此元素小的数量就要-1了

    arr = new_arr

    return arr


if __name__ == '__main__':
    logging.basicConfig(format="[%(asctime)s %(filename)s: %(lineno)s] %(message)s",
                        level=logging.INFO,
                        filemode="a",
                        filename=None)
    logger.info("计数排序结果: {}".format(counting_sort([1, 3, 6, 2, 4, 7, 9, 5, 8])))
