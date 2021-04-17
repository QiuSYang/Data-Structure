"""
# 索引从0开始的小顶堆, left = 2*root + 1, right = 2*root + 2
# 参考: https://github.com/python/cpython/blob/master/Lib/heapq.py
"""
import os
import logging

logger = logging.getLogger(__name__)


class MinHeap(object):
    """小顶堆"""
    def __init__(self, datas):
        self._heap = datas

    def _siftup(self, pos):
        """从上向下的堆化
           将pos节点的子节点中的最值提升到pos位置
        """
        start = pos
        start_value = self._heap[pos]
        n = len(self._heap)  # 堆容量
        # 完全二叉树特性
        child = pos * 2 + 1
        # 比较叶子节点
        while child < n:
            child_right = child + 1
            # 平衡二叉树的特性, 大的都在右边
            if child_right < n and not self._heap[child_right] > self._heap[child]:
                # 左值 > 右值
                child = child_right
            self._heap[pos] = self._heap[child]
            pos = child
            child = pos * 2 + 1
        self._heap[pos] = start_value

        # 此时只有pos是不确定的
        self._siftdown(start, pos)

    def _siftdown(self, start, pos):
        """
        最小堆: 大于start的节点, 除pos外已经是最小堆
        以pos为叶子节点, start为根节点之间的元素进行排序. 将pos叶子节点交换到正确的排序位置
        操作: 从叶子节点开始, 当父节点的值大于子节点时, 父节点的值降低到子节点
        """
        startval = self._heap[pos]
        while pos > start:
            parent = (pos - 1) >> 1
            parentval = self._heap[parent]
            if parentval > startval:
                self._heap[pos] = parentval
                pos = parent
                continue
            break
        self._heap[pos] = startval

    def heapify(self):
        """
        堆化: 从后向前(从下向上)的方式堆化, _siftup中pos节点的子树已经是有序的,
        这样要排序的节点在慢慢减少
        1. 因为n/2+1到n的节点是叶子节点(完全二叉树的特性), 它们没有子节点,
        所以, 只需要堆化n/2到0的节点, 以对应的父节点为根节点, 将最值向上筛选,
        然后交换对应的根节点和查找到的最值
        2. 因为开始时待排序树的根节点还没有排序, 为了保证根节点的有序,
        需要将子树中根节点交换到正确顺序
        """
        n = len(self._heap)
        for i in reversed(range(n // 2)):
            self._siftup(i)

    def heappop(self):
        """
        弹出堆首的最值 O(logn)
        """
        tail = self._heap.pop()
        # 为避免破环完全二叉树特性, 将堆尾元素填充到堆首
        # 此时, 只有堆首是未排序的, 只需要一次从上向下的堆化
        if self._heap:
            peak = self._heap[0]
            self._heap[0] = tail
            self._siftup(0)
            return peak
        return tail

    def heappush(self, val):
        """
        添加元素到堆尾 O(logn)
        """
        n = len(self._heap)
        self._heap.append(val)
        # 此时只有堆尾的节点是未排序的, 将添加的节点迭代到正确的位置
        self._siftdown(0, n)

    @property
    def heap_datas(self):
        return self._heap

    def __repr__(self):
        vals = [str(i) for i in self._heap]
        return '->'.join(vals)


def get_array_top_k():
    """获取数组 top k值"""
    arr = [0, 7, 3, 4, 2, 1, 5, 6]
    arr_length = len(arr)
    top_k = 3
    arr_heap = arr[:top_k]  # 取数组前三个元素建堆
    heap = MinHeap(arr_heap)
    heap.heapify()  # 初始建堆
    for val in arr[top_k:]:
        # 依次扫描后面的数据
        root_val = heap.heap_datas[0]
        if val > root_val:
            heap.heappop()  # 删除堆顶元素
            heap.heappush(val)  # 插入新元素
    logger.info(heap)
    arr.append(10)
    arr.append(-1)
    arr.append(11)
    if len(arr) > arr_length:
        for val in arr[arr_length:]:
            # 求取最新arr 的 top k
            root_val = heap.heap_datas[0]
            if val > root_val:
                heap.heappop()  # 删除堆顶元素
                heap.heappush(val)  # 插入新元素
        arr_length = len(arr)  # 更新数据长度
    logger.info(heap)


def merge_n_sort_array():
    """使用最小堆合并n个有序数组"""
    n_arr = [[1, 3, 4, 5, 8],
             [2, 4, 6, 7, 11],
             [8, 9, 10, 12, 15]]

    datas = []  # 获取初始堆的元素, 即所有数组的第一个元素
    for arr in n_arr:
        datas.append(arr.pop(0))

    index_datas = datas.copy()  # 用于存取每次堆顶元素属于哪个数组, index_datas元素的索引对应数组索引
    sort_big_arr = []
    # 建立最小堆
    min_heap = MinHeap(datas)
    min_heap.heapify()

    index, arr_num = 0, len(n_arr)
    while True:
        try:
            root_val = min_heap.heappop()  # 获取堆顶元素
            sort_big_arr.append(root_val)
            arr_index = index_datas.index(root_val)
            new_val = n_arr[arr_index].pop(0)  # 从堆顶元素对应的数组中取下一个元素, 数组越界跳转
            index_datas[arr_index] = new_val
            min_heap.heappush(new_val)  # 新元素入堆
        except IndexError as e:
            # 出现索引异常时, 说明数据已经访问完, 堆元素减小
            logger.info("Error info: {}".format(e))
            index += 1
            index_datas[arr_index] = None  # 当前数组数据已经访问完, 对应索引数组设置为None
            if index >= arr_num:
                # 数组已经全部访问完
                break

    logger.info(sort_big_arr)


if __name__ == '__main__':
    logging.basicConfig(format="[%(asctime)s %(filename)s: %(lineno)s]: %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S",
                        level=logging.INFO,
                        filename=None,
                        filemode="a")

    h = MinHeap([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    h.heapify()
    logger.info(h)
    # logger.info(h.heappop())
    # logger.info(h)
    # h.heappush(3.5)
    # logger.info(h)
    # h.heappush(0.1)
    # logger.info(h)
    # h.heappush(0.5)
    # logger.info(h)
    # logger.info(h.heappop())
    # logger.info(h)
    # get_array_top_k()
    merge_n_sort_array()
