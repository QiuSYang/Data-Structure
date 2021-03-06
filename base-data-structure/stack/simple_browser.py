"""
    a simple browser realize
    Author: zhenchao.zhu
    解答：我们使用两个栈，X 和 Y，我们把首次浏览的页面依次压入栈 X，当点击后退按钮时，再依次从栈 X 中出栈，
    并将出栈的数据依次放入栈 Y。当我们点击前进按钮时，我们依次从栈 Y 中取出数据，放入栈 X 中。
    当栈 X 中没有数据时，那就说明没有页面可以继续后退浏览了。当栈 Y 中没有数据，
    那就说明没有页面可以点击前进按钮浏览了。
"""
import os
import sys
import logging

work_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(work_path)
from linked_stack import LinkedStack

logger = logging.getLogger(__name__)


class NewLinkedStack(LinkedStack):
    def is_empty(self):
        return not self._top

    def clear(self):
        if self.is_empty():
            return
        else:
            while self._top:
                self._top = self._top._next

            return


class Browser(object):
    """实现浏览器的前进后退功能"""
    def __init__(self):
        self.forward_stack = NewLinkedStack()  # 存依次顺序点击页面
        self.back_stack = NewLinkedStack()  # 存放回退过的页面

    def can_forward(self):
        if self.back_stack.is_empty():
            logger.info("Don't have url to go forward.")
            return False

        return True

    def can_back(self):
        if self.forward_stack.is_empty():
            logger.info("Don't have url to go back.")
            return False

        return True

    def open(self, url):
        if not self.back_stack.is_empty():
            logger.info("Open new url, Previous forward url cannot be restored, Clear forward stack.")
            # 点击回退当前页面之后，再在当前页面点击新的页面，之前在当前页面之后点击页面将无法回退恢复，
            # 因此存在回退栈中的页面列表将全部被清理出栈
            self.back_stack.clear()
        logger.info("Open new url {}".format(url))
        self.forward_stack.push(url)

    def back(self):
        if self.forward_stack.is_empty():
            return

        top = self.forward_stack.pop()  # 出栈
        self.back_stack.push(top)  # 记录回退的页面
        logger.info("Back to {}".format(top))

    def forward(self):
        if self.back_stack.is_empty():
            return

        top = self.back_stack.pop()
        self.forward_stack.push(top)
        logger.info("Forword to {}".format(top))


if __name__ == '__main__':
    logging.basicConfig(format="[%(asctime)s %(filename)s:%(lineno)s] %(message)s",
                        level=logging.INFO,
                        filename=None,
                        filemode='a')
    browser = Browser()
    browser.open('a')
    browser.open('b')
    browser.open('c')
    if browser.can_back():
        browser.back()
        browser.open('d')
        browser.back()

    if browser.can_forward():
        browser.forward()

    browser.back()
    browser.back()
    browser.back()
