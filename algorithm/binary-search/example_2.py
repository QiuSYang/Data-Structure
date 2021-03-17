"""
# 二分查找变种(二分查找的基础：数组有序)
"""
import os
import logging

logger = logging.getLogger(__name__)


def binary_search_left(arr: list, target):
    """变种1 --- 查找第一个值等于给定值的元素"""
    low, high = 0, len(arr) - 1
    while low <= high:
        # 边界条件, low <= high
        mid = low + (high - low) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    if low < len(arr) and arr[low] == target:
        # 下边界为第一个目标元素
        return low

    return -1


def binary_search_left_1(arr: list, target):
    """变种1 --- 查找第一个值等于给定值的元素 --- 方法2"""
    low, high = 0, len(arr) - 1
    while low <= high:
        # 边界条件, low <= high
        mid = low + (high - low) // 2
        if arr[mid] < target:
            low = mid + 1  # 向上收缩
        elif arr[mid] > target:
            high = mid - 1  # 向下收缩
        else:
            # arr[mid] == target
            if mid == 0 or arr[mid - 1] != target:
                return mid
            else:
                high = mid - 1  # 说明当前位置不是第一出线, 因此high继续收缩


def binary_search_right(arr: list, target):
    """变种2 --- 查找最后一个值等于给定值的元素"""
    low, high = 0, len(arr) - 1
    while low <= high:
        # 边界条件, low <= high
        mid = low + (high - low) // 2
        if arr[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1

    if high >= 0 and arr[high] == target:
        # 上边界为最后一个目标元素
        return high

    return -1


def binary_search_right_1(arr: list, target):
    """变种2 --- 查找最后一个值等于给定值的元素"""
    # 方法二
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] > target:
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            # 当前元素等于目标值
            if mid == len(arr) - 1 or arr[mid + 1] != target:
                return mid
            else:
                # 如果mid + 1 位置元素值等target, 说明此处不是最右位置, 因此最低为mid + 1
                low = mid + 1

    return -1


def binary_search_left_not_less(arr: list, target):
    """变种3 --- 查找第一个大于等于给定值的元素"""
    low, high = 0, len(arr) - 1
    while low <= high:
        # 收缩到最后只剩一个元素数组, mid == low == high
        mid = low + (high - low) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    if low < len(arr) and arr[low] >= target:
        return low  # 收缩到low 与 high交叉相向驶过, 当前low位置就是第一个大于等于给定元素的位置

    return -1


def binary_search_right_not_greater(arr: list, target):
    """变种4 -- 查找最后一个小于等于给定值的元素"""
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1
    if high >= 0 and arr[high] <= target:
        # 收缩到low 与 high交叉相向驶过, 当前high位置就是最后一个小于等于给定元素的位置
        # 因为当前mid位置 > target, high会继续收缩
        return high

    return -1


if __name__ == '__main__':
    logging.basicConfig(format="[%(asctime)s %(filename)s:%(lineno)s] %(message)s",
                        level=logging.INFO,
                        filemode="a",
                        filename=None)

    arr = [1, 1, 2, 3, 4, 6, 7, 7, 7, 7, 10, 22]

    logger.info("第一次出现给定元素: {}".format(binary_search_left(arr, 7)))
    logger.info("第一次出现给定元素: {}".format(binary_search_left_1(arr, 7)))
    logger.info("最后一次出现给定元素：{}".format(binary_search_right(arr, 7)))
    logger.info("最后一次出现给定元素：{}".format(binary_search_right_1(arr, 7)))

    logger.info("第一个大于等于给定值的元素: {}".format(binary_search_left_not_less(arr, 7)))
    logger.info("第一个大于等于给定值的元素: {}".format(binary_search_left_not_less(arr, 5)))
    logger.info("后一个小于等于给定值的元素: {}".format(binary_search_right_not_greater(arr, 7)))
    logger.info("后一个小于等于给定值的元素: {}".format(binary_search_right_not_greater(arr, 5)))
