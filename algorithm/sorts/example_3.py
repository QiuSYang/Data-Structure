"""
# 快速排序
"""
import os
import logging
import random

logger = logging.getLogger(__name__)


def _partition(arr: list, low: int, high: int):
    """数组按照arr[low]元素进行拆分，所有小于arr[low]的元素位于左边，大于arr[low]的元素位于右边"""
    pivot, index = arr[low], low
    # i按照数组扫描依次移动, index只有交换之前移动，找到被交换的位置，指向上一次被交换的下一个位置，index位置元素<=pivot
    for i in range(low+1, high+1):
        if arr[i] <= pivot:
            # 将所有比基元素pivot小的元素移动到左边
            index += 1
            arr[i], arr[index] = arr[index], arr[i]  # 元素交换

    arr[low], arr[index] = arr[index], arr[low]

    return index  # 返回pivot元素位置, 拆分点


def _quick_sort_sub(arr: list, low: int, high: int):
    """边界条件：low >= high, 即数组不能再被拆分(此时数组被拆解单个元素数组)"""
    if low < high:
        # get a random position as the pivot
        k = random.randint(low, high)
        arr[low], arr[k] = arr[k], arr[low]  # 将第K元素调整到数组头部

        m = _partition(arr, low, high)  # 数组被拆解为三个部分: arr[low:m-1], arr[m], arr[m+1:high]
        # 递归调用
        _quick_sort_sub(arr, low, m-1)
        _quick_sort_sub(arr, m+1, high)


def quick_sort(arr: list):
    """快速排序
    快排的思想是这样的：如果要排序数组中下标从p到r之间的一组数据，我们选择p到r之间的任意一个数据作为pivot（分区点）。
    我们遍历p到r之间的数据，将小于pivot的放到左边，将大于pivot的放到右边，将pivot放到中间。
    经过这一步骤之后，数组p到r之间的数据就被分成了三个部分，前面p到q-1之间都是小于pivot的，中间是pivot，
    后面的q+1到r之间是大于pivot的。"""
    if arr is None or len(arr) < 1:
        return arr

    _quick_sort_sub(arr, 0, len(arr)-1)

    return arr


if __name__ == '__main__':
    logging.basicConfig(format="[%(asctime)s %(filename)s: %(lineno)s] %(message)s",
                        level=logging.INFO,
                        filemode="a",
                        filename=None)

    logger.info("快速排序结果: {}".format(quick_sort([1, 5, 7, 2, 3, 4, 5, 10, 9])))
