"""
# 哈希表
    1. 使用链表解决哈希表的冲突
    2. 使用哈希表+链表实现LRU cache查询复杂度为O(1)

哈希表（Hash table，也叫散列表），是根据关键码值(Key value)而直接进行访问的数据结构。
也就是说，它通过把关键码值映射到表中一个位置来访问记录，以加快查找的速度。
这个映射函数叫做散列函数，存放记录的数组叫做散列表。
"""
import os
import logging

logger = logging.getLogger(__name__)


class Dict(object):
    """hash table --- 类似位于字典数据结构"""
    def __init__(self, num):
        self.__table__ = []  # 二维列表, 第一维代表哈希表, 第二维代表链表支持解决冲突(key转为哈希表索引重复时, 将数据添加到同一个位置的链表最后)
        self.num = num  # 哈希表的容量
        for _ in range(num):
            self.__table__.append([])  # 表每个位置都对应一个链表来支持解决冲突(支持扩容)

    def hash_function(self, key, num):
        """哈希函数, 负责key的映射, 将key映射为数组的索引号"""
        hash_val = 0
        x = key
        if x < 0:
            logger.info("the key is low")
            return
        # while x != 0:
        #     hash_val = (hash_val << 3) + x % 10
        #     x /= 10

        return hash_val % num  # 轮转到第几个索引号

    def put(self, key, value):
        """散列表中插入数据"""
        i = self.hash_function(key, self.num) % self.num  # 计算索引号
        for p, (k, v) in enumerate(self.__table__[i]):
            if k == key:
                # 当前位置已经存在元素了
                self.__table__[i][p] = (key, value)  # 更新已有(key, value)
                return

        self.__table__[i].append((key, value))  # 添加新的(key, value)

    def get(self, key):
        """获取对应key的值"""
        i = self.hash_function(key, self.num) % self.num  # 计算索引号
        for k, v in self.__table__[i]:  # 获取key对应散列表的位置
            if key == k:
                return v

        raise KeyError(key)

    def keys(self):
        ret = []
        for table in self.__table__:
            for k, v in table:
                ret.append(k)

        return ret

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.put(key, value)


class LRUCache(object):
    """借助哈希表和链表实现LRU"""
    def __init__(self, size=3):
        self.size = size
        self.cache = {}  # 存储元素
        self.keys = []  # 记录元素访问先后顺序

    def set(self, key, value):
        """插入元素"""
        if key in self.cache:
            self.keys.remove(key)  # 删除原来的元素
            self.keys.insert(0, key)  # 将其添加到链头
            self.cache[key] = value  # 更新缓存内容
        elif len(self.keys) == self.size:
            # 链满
            old = self.keys.pop()  # 取出最后元素，最长时间不被使用的缓存
            self.cache.pop(old)  # 从缓存清楚此元素
            self.keys.insert(0, key)  # 将新的内容入缓存
            self.cache[key] = value
        else:
            # 新内容插入链头
            self.keys.insert(0, key)
            self.cache[key] = value

    def get(self, key):
        """获取元素"""
        if key in self.cache:
            self.keys.remove(key)  # 将其从链表的原有位置删除
            self.keys.insert(0, key)  # 将其重新插入链头
            return self.cache[key]  # 取出元素
        else:
            return None  # 缓存中不存在此元素


if __name__ == '__main__':
    logging.basicConfig(format="[%(asctime)s %(filename)s: %(lineno)s] %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S",
                        level=logging.INFO,
                        filename=None,
                        filemode="a")

    obj = Dict(3)

    for i in range(5):
        obj[i] = i

    logger.info(obj[1])

    test = LRUCache()
    test.set('a', 2)
    test.set('b', 2)
    test.set('c', 2)
    test.set('d', 2)
    test.set('e', 2)
    test.set('f', 2)
    logger.info(test.get('c'))  # None
    logger.info(test.get('b'))  # None
    logger.info(test.get('a'))  # None
    logger.info(test.get('e'))  # 2
