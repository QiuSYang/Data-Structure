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


if __name__ == '__main__':
    logging.basicConfig(format="[%(asctime)s %(filename)s:%(lineno)s] %(message)s",
                        level=logging.INFO,
                        filemode="a",
                        filename=None)
    logger.info("斐波那契结果: {}".format(fibonacci(5)))
    logger.info("阶乘求解: {}".format(factorial(5)))
    logger.info("阶乘求和: {}".format(factorial_sum(5)))
