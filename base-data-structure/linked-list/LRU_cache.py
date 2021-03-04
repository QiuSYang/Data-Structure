"""
使用链表实现LRU缓存机制
"""
import os
import logging

logger = logging.getLogger(__name__)


if __name__ == '__main__':
    logging.basicConfig(format='[%(asctime)s %(filename)s:%(lineno)s] %(message)s',
                        level=logging.INFO,
                        filename=None,
                        filemode='a')
