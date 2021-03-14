"""
# 归并排序
"""
import os
import logging

logger = logging.getLogger(__name__)


def _merge(arr: list, low: int, mid: int, high: int):
    """数组排序合并"""
    # arr[low:mid], arr[mid+1:high]进行排序
    i, j = low, mid + 1
    tmp = []
    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1

    # 上面两个数组元素依次比较, 剩下的元素处理, 剩下的元素肯定是已经排序好的，以及比tmp数组的元素都要大
    start = i if i <= mid else j
    end = mid if i <= mid else high
    tmp.extend(arr[start:end+1])

    arr[low:high+1] = tmp  # 将排序好的数组覆盖原有数组


def _merge_sort_sub(arr: list, low: int, high: int):
    if low < high:
        # 仅仅当数组最低位小于最高位才继续进行分解(其实分解最小单位为2, 当数组大小为2是不再被分解,
        # 例如0, 1两个索引数组为一组, 那么继续分解, low为0, mid(0+(1-0)//2)也为0, high为1。
        # 这样前半部分和后半部分都不能满足拆分条件了(low < high), 就不能再拆分了)
        mid = low + (high - low) // 2
        # 递归调用分解与合并
        _merge_sort_sub(arr, low, mid)  # 前半部分继续拆分
        _merge_sort_sub(arr, mid+1, high)  # 后半部分继续拆分

        _merge(arr, low, mid, high)  # 数组合并


def merge_sort(arr: list):
    """归并排序"""
    _merge_sort_sub(arr, low=0, high=len(arr)-1)

    return arr


if __name__ == '__main__':
    logging.basicConfig(format="[%(asctime)s %(filename)s:%(lineno)s] %(message)s",
                        level=logging.INFO,
                        filemode="a",
                        filename=None)
    logger.info("归并排序结果: {}".format(merge_sort([1, 3, 5, 8, 10, 23, 2, 7, 6, 2])))
