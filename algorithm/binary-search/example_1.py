"""
# 二分查找实现
"""
import os
import logging

logger = logging.getLogger(__name__)


def binary_search(arr: list, target):
    """Binary search of a target in a sorted array without duplicates.
    If such a target does not exist, return -1, othewise, return its index."""
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            # 中间元素刚好等于
            return mid
        elif arr[mid] > target:
            # 被查找元素存在于low ~ mid-1中
            high = mid - 1
        else:
            # 被查找元素存在于mid+1 ~ high
            low = mid + 1

    return -1


def binary_search_internally(arr: list, low: int, high: int, target: int):
    """递归函数"""
    if low > high:
        # 最低位与最高位已经相遇驶过, 说明数组中没有目标元素
        return -1

    # mid = low + int((high - low) >> 2)
    mid = low + (high - low) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        # 被查找元素存在于low ~ mid-1中
        return binary_search_internally(arr, low, mid - 1, target)  # 递归调用
    else:
        # 被查找元素存在于mid+1 ~ high
        return binary_search_internally(arr, mid + 1, high, target)  # 递归调用


def binary_search_recursion(arr: list, target):
    """递归实现二分查找"""
    index = binary_search_internally(arr, 0, len(arr) - 1, target)
    return index


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    # dp = [0] * (n+1)
    #
    # dp[1] = 1
    pre, cur = 0, 1
    for i in range(2, n+1):
        # dp[i] = dp[i-1] + dp[i-2]
        sum = pre + cur
        pre = cur
        cur = sum

    return sum


def str2int(text: str):
    text = reversed(text)
    sum = 0
    for idx, char in enumerate(text):
        temp = ord(char) - ord("0")
        sum += 10**idx * temp

    return sum


def str2float(text: str):
    text_list = text.split(".")
    if len(text_list) < 2:
        return str2int("".join(text_list))
    int_arr, float_arr = text_list[0], text_list[1]

    total = 0
    for idx, char in enumerate(reversed(int_arr)):
        temp = ord(char) - ord("0")
        total += 10 ** idx * temp

    for idx, char in enumerate(float_arr):
        temp = ord(char) - ord("0")
        x = idx + 1
        total += 0.1**x * temp

    return total


if __name__ == '__main__':
    logging.basicConfig(format="[%(asctime)s %(filename)s:%(lineno)s] %(message)s",
                        level=logging.INFO,
                        filemode="a",
                        filename=None)
    # logger.info("二分查找结果：{}".format(binary_search([1, 2, 5, 7, 9, 10], 2)))
    # logger.info("二分查找结果(递归版)：{}".format(binary_search_recursion([1, 2, 5, 7, 9, 10], 2)))
    # for i in range(5):
    #     logger.info(fib(i))

    logger.info(str2float("12.999"))
