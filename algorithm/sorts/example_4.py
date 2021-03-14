"""
# 快速排序 --- 方法2
"""
import os
import logging
import random

logger = logging.getLogger(__name__)


def quick_sort(arr: list):
    """快速排序
    快排的思想是这样的：如果要排序数组中下标从p到r之间的一组数据，我们选择p到r之间的任意一个数据作为pivot（分区点）。
    我们遍历p到r之间的数据，将小于pivot的放到左边，将大于pivot的放到右边，将pivot放到中间。
    经过这一步骤之后，数组p到r之间的数据就被分成了三个部分，前面p到q-1之间都是小于pivot的，中间是pivot，
    后面的q+1到r之间是大于pivot的。"""
    # 双向排序: 提高非随机输入的性能
    # 不需要额外的空间,在待排序数组本身内部进行排序
    # 基准值通过random随机选取
    # 入参: 待排序数组, 数组开始索引 0, 数组结束索引 len(array)-1
    if arr is None or len(arr) < 1:
        return arr

    def swap(arr, low, high):
        # 数组内元素交换
        tmp = arr[low]
        arr[low] = arr[high]
        arr[high] = tmp
        return arr

    def quick_sort_sub(arr, low, high):
        if low >= high:
            # 单元素数组(数组最小单位), 无须再进行排序
            return arr

        # 随机选取基准值pivot, 数组最低位即为基准元素
        swap(arr, low, int(random.uniform(low, high)))

        temp = arr[low]  # 基准元素
        # 缓存边界值, 从上下边界同时排序
        i, j = low, high
        while True:
            # 元素交换, 将小于基准元素的元素全部转移到左边, 大于基准源的元素全部转移到右边，
            # 数组被拆分三份：小于temp的数组，等于temp的数组，大于temp的数组
            i += 1  # 因为low为基准元素的索引, 因先+1；而后需要从交换元素的下一个元素继续扫描
            while i <= high and arr[i] <= temp:
                i += 1  # 说明当前元素小于等于基准元素，继续从前向后扫描, 直至扫描到最后一个元素
            while arr[j] > temp:
                j -= 1  # 说明从后向前扫描, 当前元素大于基准元素

            # 如果小索引大于等于大索引, 说明排序完成, 退出排序
            if i >= j:
                break

            swap(arr, i, j)  # 前后元素交换位置, 当前两个元素不符合条件, i位置元素大于基准元素, j位置的元素小于基准元素

        # 将基准值的索引从下边界调换到索引分割点
        swap(arr, low, j)  # j为分割点

        # 递归调用
        quick_sort_sub(arr, low, j - 1)
        quick_sort_sub(arr, j + 1, high)

        return arr

    quick_sort_sub(arr, 0, len(arr) - 1)

    return arr


if __name__ == '__main__':
    logging.basicConfig(format="[%(asctime)s %(filename)s: %(lineno)s] %(message)s",
                        level=logging.INFO,
                        filemode="a",
                        filename=None)

    logger.info("快速排序结果: {}".format(quick_sort([1, 5, 7, 2, 3, 4, 5, 10, 9])))
