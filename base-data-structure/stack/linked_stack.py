"""
# 基于链表实现栈
"""
import os
import logging

logger = logging.getLogger(__name__)


class Node(object):
    """节点定义"""
    def __init__(self, data: int, next=None):
        self._data = data
        self._next = next


class LinkedStack(object):
    """A stack based upon singly-linked list"""
    def __init__(self):
        self._top: Node = None

    def push(self, value: int):
        """栈顶插入节点"""
        new_top = Node(value)
        new_top._next = self._top
        self._top = new_top

    def pop(self):
        """出栈"""
        if self._top:
            value = self._top._data
            self._top = self._top._next
            return value

    def __repr__(self):
        current = self._top
        nums = []
        while current:
            nums.append(current._data)
            current = current._next

        return "->".join(f"{num}" for num in nums)


if __name__ == '__main__':
    logging.basicConfig(format="[%(asctime)s %(filename)s:%(lineno)s] %(message)s",
                        level=logging.INFO,
                        filename=None,
                        filemode='a')
    stack = LinkedStack()
    for i in range(9):
        stack.push(i)
    logger.info(stack)
    for _ in range(3):
        stack.pop()
    logger.info(stack)
