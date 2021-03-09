"""
# 递归的一些实例
"""
import os
import logging

logger = logging.getLogger(__name__)


def fibonacci(n):
    """斐波那契数列（Fibonacci sequence），又称黄金分割数列，
    因数学家莱昂纳多·斐波那契（Leonardoda Fibonacci）以兔子繁殖为例子而引入，
    故又称为“兔子数列”，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……在数学上这个数列从第3项开始，每一项都等于前两项之和，
    斐波那契数列以如下被以递推的方法定义：F(0)=0，F(1)=1, F(n)=F(n-1)+F(n-2)（n ≥ 2，n ∈ N*）

    1. 递归公式：F(n)=F(n-1)+F(n-2)  当前项等于前两项之和
    2. 边界条件：F(0) = 0, F(1) = 1
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)  # 等于前两项之和


def factorial(n):
    """一个正整数的阶乘（factorial）是所有小于及等于该数的正整数的积，并且0的阶乘为1。自然数n的阶乘写作n!。
    1808年，基斯顿·卡曼引进这个表示法。亦即n!=1×2×3×...×(n-1)×n。阶乘亦可以递归方式定义：0!=1，n!=(n-1)!×n

    1. 递归公式：N! = (N-1)! * N
    2. 边界条件：0! = 1
    """
    if n == 0:
        return 1
    return n * factorial(n-1)


def factorial_sum(n):
    """sum = n! + (n-1)! + ... + 2! + 1!"""
    sum = 0
    for i in range(1, n+1):
        sum += factorial(i)

    return sum


def perm(arr, start, size, answers=[]):
    """
    递归函数中含三个参数，arr：数组；start：起始索引；size：数组所含元素数（也可以理解为结束索引+1）；
    递归结束的条件，当start和end相同时候
    具体实现及讲解在代码及注释中
    """
    # 定义递归结束的条件，也是打印当前排列
    if start == size:
        logger.info(arr)
        answers.append(arr.copy())  # 结果保存在全局列表中
    else:
        # 对数组（start，end）部分第一位元素所有可能进行遍历
        for index in range(start, size):
            # 交换第一个元素和数组（start，end）部分的另一个元素
            arr[index], arr[start] = arr[start], arr[index]
            # 递归，对确定下一位元素
            perm(arr, start + 1, size, answers)
            # 将数组恢复成交换之前
            arr[index], arr[start] = arr[start], arr[index]


if __name__ == '__main__':
    logging.basicConfig(format="[%(asctime)s %(filename)s:%(lineno)s] %(message)s",
                        level=logging.INFO,
                        filemode="a",
                        filename=None)
    logger.info("斐波那契结果: {}".format(fibonacci(5)))
    logger.info("阶乘求解: {}".format(factorial(5)))
    logger.info("阶乘求和: {}".format(factorial_sum(5)))

    results = []
    perm([1, 2, 3], 0, 3, results)
    logger.info("集合全排列: {}".format(results))
