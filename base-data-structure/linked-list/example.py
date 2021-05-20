"""
# Linked-list 实例
"""
import os


class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def rotate_right(head: Node, k: int) -> Node:
    """给定一个链表，循环向右移动k个节点。
    如给定链表1->2->3->4->5，k=2，则返回循环右移2个节点后的链表：4->5->1->2->3。
    思路：设置2个指针，前一个先向前移动k个节点，然后两个节点同步向前移，直到前一个指针到达链表末端，这时两个指针之间的部分就是需要循环移动到链表头的部分。
    注意：这里k可以是任何值，有可能会比整个链表长度还大，所以可能会出现循环好几次的情况。可以先计算出链表的长度l，然后取余 k%l 就是实际需要移动的节点。
    虽然计算链表长度需要多循环一次，但实际上，在k比较大时直接移动反而会循环更多次。
    例如: 1->2->3, k=5, 结果2->3->1
    """
    if head is None or head.next is None:
        return head

    temp = head
    count = 0
    # 计算链表的长度
    while temp:
        count += 1
        temp = temp.next

    k = k % count  # 当k>count, 实际只需要移动k%count个节点
    if k == 0:
        # 循环推移回到原点
        return head

    # 双指正记录移动位置, 快慢指正
    fast = head
    slow = head
    for i in range(k):
        fast = fast.next
    # fast移动到末尾, slow移动倒数第K个节点
    while fast.next:
        fast = fast.next
        slow = slow.next

    result = slow.next
    slow.next = None  # 节点断开
    fast.next = head

    return result


if __name__ == '__main__':
    head = Node(1)
    temp = head
    for i in range(2, 7):
        temp.next = Node(i)
        temp = temp.next

    result = rotate_right(head, 2)
    while result:
        print(result.value)
        result = result.next
