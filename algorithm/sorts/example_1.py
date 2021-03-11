"""
# 实现一些简单排序算法，例如冒泡、插入、选择排序
"""
import os
import logging

logger = logging.getLogger(__name__)


def bubble_sort(arr: list):
    """冒泡排序只会操作相邻的两个数据。每次冒泡操作都会对相邻的两个元素进行比较，看是否满足大小关系要求。
    如果不满足就让它俩互换。一次冒泡会让至少一个元素移动到它应该在的位置，重复n次，就完成了n个数据的排序工作。"""
    arr_len = len(arr)
    if arr_len <= 1:
        return arr

    for i in range(arr_len):
        made_swap = False
        for j in range(arr_len-i-1):  # 第一层循环结束，最大元素将置于末尾
            # 相邻两个元素比较
            if arr[j+1] < arr[j]:
                # 符合条件，交换
                a = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = a
                made_swap = True

        if not made_swap:
            # 证明所有元素都已经顺序排列
            break

    return arr


def insertion_sort(arr: list):
    """一个有序的数组，我们往里面添加一个新的数据后，如何继续保持数据有序呢？
    很简单，我们只要遍历数组，找到数据应该插入的位置将其插入即可。
    将数组中的数据分为两个区间， 已排序区间和未排序区间。初始已排序区间只有一个元素，就是数组的第一个元素。
    插入算法的核心思想是取未排序区间中的元素，在已排序区间中找到合适的插入位置将其插入，并保证已排序区间数据一直有序。
    重复这个过程，直到未排序区间中元素为空，算法结束。"""
    arr_len = len(arr)
    if arr_len <= 1:
        return arr

    for j in range(1, arr_len):
        current_value = arr[j]  # 当前元素
        i = j - 1
        while i >= 0 and arr[i] > current_value:
            # 当前元素依次与前j个已经排序元素比较(降序)
            arr[i+1] = arr[i]
            i -= 1

        arr[i+1] = current_value  # 空白位置填充当前元素

    return arr


def selection_sort(arr: list):
    """选择排序算法的实现思路有点类似插入排序，也分已排序区间和未排序区间。
    但是选择排序每次会从未排序区间中找到最小的元素，将其放到已排序区间的末尾。"""
    arr_len = len(arr)
    if arr_len <= 1:
        return arr

    for i in range(arr_len):
        min_index = i
        min_value = arr[i]
        for j in range(i, arr_len):
            if arr[j] < min_value:
                min_value = arr[j]
                min_index = j

        # 元素交换
        arr[min_index] = arr[i]  # 将最小元素位置变为i位置的值
        arr[i] = min_value

    return arr


if __name__ == '__main__':
    logging.basicConfig(format="[%(asctime)s %(filename)s:%(lineno)s] %(message)s",
                        level=logging.INFO,
                        filemode="a",
                        filename=None)
    logger.info("bubble sort result: {}".format(bubble_sort([1, 4, 7, 9, 10, 6, 4, 5])))
    logger.info("insertion sort result: {}".format(insertion_sort([1, 4, 7, 9, 10, 6, 4, 5])))
    logger.info("selection sort result: {}".format(selection_sort([1, 4, 7, 9, 10, 6, 4, 5])))
