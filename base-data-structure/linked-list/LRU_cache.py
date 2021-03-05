"""
使用链表实现LRU缓存机制
"""
import os
import logging

logger = logging.getLogger(__name__)


class DbListNode(object):
    """双向链表节点"""
    def __init__(self, x, y):
        self.key = x
        self.val = y
        self.prev = None
        self.next = None


class LRUCache(object):
    """leet code: 146
        运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。
        它应该支持以下操作： 获取数据 get 和 写入数据 put 。
        获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
        写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。
            当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间

    哈希表+双向链表
    哈希表: 查询 O(1)
    双向链表: 有序, 增删操作 O(1)"""

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hkeys = {}
        # self.top 和 self.tail 作为哨兵节点，避免越界
        self.top = DbListNode(None, -1)
        self.tail = DbListNode(None, -1)

        self.top.next = self.tail  # 前后两个节点的关系
        self.tail.prev = self.top

    def get(self, key: int):
        if key in self.hkeys.keys():
            # 更新节点顺序
            cur = self.hkeys[key]
            # 跳出原位置(将当前节点剔除出来)
            cur.next.prev = cur.prev
            cur.prev.next = cur.next
            # 最近使用过的置于链表首部
            top_node = self.top.next
            self.top.next = cur
            cur.prev = self.top
            cur.next = top_node  # 与原来top节点的next节点拼接
            top_node.prev = cur

            return self.hkeys[key].val
        return -1

    def put(self, key: int, value: int):
        if key in self.hkeys.keys():
            cur = self.hkeys[key]
            cur.val = value
            # 跳出原位置
            cur.prev.next = cur.next
            cur.next.prev = cur.prev

            # 最近用过的置于链表首部
            top_node = self.top.next
            self.top.next = cur
            cur.prev = self.top
            cur.next = top_node
            top_node.prev = cur
        else:
            # 增加新节点至首部
            cur = DbListNode(key, value)
            self.hkeys[key] = cur

            # 最近用过的置于链表首部
            top_node = self.top.next
            self.top.next = cur
            cur.prev = self.top
            cur.next = top_node
            top_node.prev = cur

            # 判断列表的容量
            if len(self.hkeys.keys()) > self.cap:
                self.hkeys.pop(self.tail.prev.key)
                # 去掉原尾节点的前一个节点
                self.tail.prev.prev.next = self.tail  # 前一个节点前一个节点next节点指向tail
                self.tail.prev = self.tail.prev.prev  # 尾部前一个节点指向前前一个节点(双向链表一定要双向指向)

    def __repr__(self):
        vals = []
        p = self.top.next
        while p.next:
            vals.append(str(p.val))
            p = p.next
        return '->'.join(vals)


if __name__ == '__main__':
    logging.basicConfig(format='[%(asctime)s %(filename)s:%(lineno)s] %(message)s',
                        level=logging.INFO,
                        filename=None,
                        filemode='a')

    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    logger.info(cache)
    logger.info("return value: {}".format(cache.get(1)))  # 返回  1
    cache.put(3, 3)  # 该操作会使得密钥 2 作废
    logger.info(cache)
    logger.info("return value: {}".format(cache.get(2)))  # 返回 -1 (未找到)
    cache.put(4, 4)  # 该操作会使得密钥 1 作废
    logger.info(cache)
    logger.info("return value: {}".format(cache.get(1)))  # 返回 -1 (未找到)
    logger.info("return value: {}".format(cache.get(3)))  # 返回  3
    logger.info(cache)
    logger.info("return value: {}".format(cache.get(4)))  # 返回  4
    logger.info(cache)
