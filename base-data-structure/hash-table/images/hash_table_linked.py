"""
# 哈希表的实现，使用链表解决冲突
"""
import os


class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Hashtable(object):
    def __init__(self, size):
        # 这种写法构建哈希表时需提供哈希表长度
        # 创建空列表作为哈希表，列表每个元素都是node类型
        self.data = [Node()] * size
        self.size = size

    def hash_function(self, key, size):
        """哈希函数使用除留余数法。数据除以哈希表长然后取余"""
        return key % size

    def put(self, key):
        """向哈希表中插入数据，通过逐一插入构建哈希表"""
        # 求待插数据的哈希值
        hash_value = self.hash_function(key, self.size)
        # 若链表中下标为哈希值的位置还没有被其他数据占据，就直接把待插数据(key)放到那个位置
        if self.data[hash_value].data == None:
            self.data[hash_value].data = key
        # 如果已被占据，就在以【哈希表中下标为哈希值的位置】为起点的链表中顺次检查，直到检查到空位置
        else:
            # 上面链表起点位置空的情况已经帮忙建立好了结点，把数据域改变成key就好了。
            # 链表起点已被占据时，需要新建一个结点存储数据
            temp = Node(key)
            # p指向以【哈希表中下标为哈希值的位置】为起点的链表的头节点。
            p = self.data[hash_value]
            # 向后逐个检查
            while p.next != None:
                p = p.next
            # 现在存p已经指向了链表的末尾，p的next连接上temp即可
            p.next = temp

    def get(self, key):
        """判断某值（key）是不是在该哈希表里的函数"""
        # 获得要判断元素的哈希值
        hash_value = self.hash_function(key, self.size)
        # 相同哈希值的元素在哈希表相应位置链表中的存储没有规律
        # 简单情况，该哈希值下的链表头等于key就说明找到
        if self.data[hash_value].data == key:
            return True
        # 哈希值对应的链表头存储的不是key时
        else:
            # p存储链表头
            p = self.data[hash_value]
            # 只要没有碰到key，也没有到链表末尾，就一直向后寻找
            while p != None and p.data != key:
                p = p.next
            # 退出了上方循环后，还没有到链表的末尾，说明已找到
            if p != None and p.data == key:
                return True
        # 整个链表都未找到，说明整个哈希表里没有存储key的节点
        return False

    def delete(self, key):
        """在哈希表中删除数据为key的节点"""
        # 如果输入的key在这个哈希表中根本没有，返回错误
        if not self.get(key):
            return 'Delete Error'
        # 否则，哈希表中有存储此数据的节点。先找该数据对应的哈希值。
        hash_value = self.hash_function(key, self.size)
        # 和get函数完全类似。若哈希表中对应哈希值的链表的头部数据就和要删除的数据相符合，直接将该节点(链表头)数据域改变为none。
        # 空间有浪费，但不影响插入查找。
        if self.data[hash_value].data == key:
            self.data[hash_value].data = None
        # 否则，要删除的数据就在那个对应的链表中
        else:
            # p先指向那个位置的链表的头节点
            p = self.data[hash_value]
            # pre储存该链表当前节点之前的节点。设置pre，为了删除目标后将它上一个节点和后一个节点连接。初始时p指向头，pre为空即可。
            pre = None
            # 找到要删除的位置，每一步更新p和pre
            while p != None and p.data != key:
                pre = p
                p = p.next
            # 如果到末尾仍未找到（这种情况也可以去掉）
            if p == None:
                return 'Delete Error'
            else:
                pre.next = p.next


if __name__ == "__main__":
    # 按照要求建表、插入、删除、查找。
    n = int(input())
    # 建表
    h = Hashtable(n)
    lst = list(set(input().split()))
    slst = [int(i) for i in lst]
    for i in slst:
        h.put(i)
    # 插入
    n = int(input())
    for i in range(n):
        tmp = int(input())
        h.put(tmp)
    # 删除
    n = int(input())
    for i in range(n):
        tmp = int(input())
        tmp1 = h.delete(tmp)
        if tmp1 == 'Delete Error':
            print('Delete Error')
    # 查找
    n = int(input())
    for i in range(n):
        tmp = int(input())
        print(h.get(tmp))
