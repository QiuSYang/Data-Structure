"""
# 霍夫曼编码
对于定长编码而言，会为每个字符赋予一个长度固定为 m(m≥log2n) 的位串，我们常用的标准 ASCII 码就是采用定长编码策略对字符集进行编码的。
长度各异的编码，其中出现频率较高的字符，采用长度较短的编码表示，出现频率较低的字符，采用长度较长的编码表示。
著名的摩尔斯电码就是采用这种策略进行编码的。

通常情况下，与定长编码相比，变长编码可以有效减少表示同一字符集所需的编码长度，提升编码效率。
但是，为了使用变长编码策略，需要解决在定长编码模式下不会遇到的一个问题，就是前缀码问题。
“对每一个字符规定一个 0-1 串作为其代码，并要求任一字符的代码都不是其他字符代码的前缀”，这种编码称为前缀码。

哈夫曼树
为了对某字母表构造一套二进制的前缀码，可以借助二叉树。将树中所有的左向边都标记为0，所有的右向边都标记为 1。
通过记录从根节点到字符所在的叶子节点的简单路径上的所有 0-1 标记来获得表示该字符的编码。

用于表示二进制前缀码的二叉树每个叶子节点对应一个字符，非叶子节点不对应任何字符。
由于二叉树叶子节点之间没有互联的简单路径，所以依据这种二叉树生成的编码序列为前缀码，即字符集中各个字符对应的前缀各不相同。

对于给定的字符集和字符表而言，每个字符的出现频率可以确定，我们怎么才能构造一棵二叉树，
将较短的编码分配给高频字符，将较长的编码分配给低频字符呢？用贪心算法可以实现这个目标。

这个算法由戴维·哈夫曼（David Huffman）发明，因此，能达到这个目标的二叉树称为哈夫曼树。

具体算法如下：
    1. 初始化 n 个单节点的树，并为它们标上字母表中的字符。把每个字符出现的频率记在其对应的根节点中，用来标记各个树的权重，即树的权重等于树中所有叶子节点的概率之和。
    2. 重复下面的步骤，直到只剩一颗单独的树。找到两棵权重最小的树，若两棵树权重相同，可任选其一，分别把它们作为新二叉树的左右子树，并把其权重之和作为新的权重记录在新树的根节点中。
"""
import os
import logging

logger = logging.getLogger(__name__)


class Node(object):
    """树节点定义"""
    def __init__(self,pro):
        self.left = None
        self.right = None
        self.parent = None
        self.pro = pro  # 记录当前节点的值

    def is_left(self):  # 判断左子树
        return self.parent.left == self


def create_nodes(pros: list):
    """create nodes创建叶子节点
       pros: 所有字符出现的概率"""
    return [Node(pro) for pro in pros]


def create_huffman_tree(nodes: list):
    """create Huffman-Tree创建Huffman树
       所有待编码字符全部位于叶子节点"""
    queue = nodes[:]  # 对象引用
    while len(queue) > 1:
        queue.sort(key=lambda item: item.pro)  # 按概率升序排列
        node_left = queue.pop(0)
        node_right = queue.pop(0)  # 获取队列中概率最下的节点
        node_parent = Node(node_left.pro + node_right.pro)
        node_parent.left = node_left  # 小的放左边
        node_parent.right = node_right  # 大的放右边
        node_left.parent = node_parent
        node_right.parent = node_parent
        queue.append(node_parent)  # 父节点加入队列
    queue[0].parent = None

    return queue[0]  # 返回树的根节点


def create_huffman_tree_x(nodes: list):
    """create Huffman-Tree创建Huffman树
           所有待编码字符全部位于叶子节点
           除树的最大深度左叶子为待编码字符, 其他层待编码字符全部位置右叶子节点"""
    queue = []  # 存储父节点
    index = 0  # 使用标志符记录nodes的访问位置
    nodes.sort(key=lambda item: item.pro)  # 按概率升序排列
    node_left = nodes[index]
    index += 1
    node_right = nodes[index]  # 获取队列中概率最下的节点
    index += 1
    node_parent = Node(node_left.pro + node_right.pro)
    node_parent.left = node_left  # 小的放左边
    node_parent.right = node_right  # 大的放右边
    node_left.parent = node_parent
    node_right.parent = node_parent
    queue.append(node_parent)
    while index < len(nodes):
        node_left = queue.pop(0)
        node_right = nodes[index]  # 所有字符节点放在右叶子
        index += 1
        node_parent = Node(node_left.pro + node_right.pro)
        node_parent.left = node_left  # 小的放左边
        node_parent.right = node_right  # 大的放右边
        node_left.parent = node_parent
        node_right.parent = node_parent
        queue.append(node_parent)

    queue[0].parent = None

    return queue[0]  # 返回根节点


def huffman_encoding(nodes, root):
    """huff-man编码"""
    codes = [str()] * len(nodes)
    for idx, node in enumerate(nodes):
        while node != root:
            if node.is_left():
                codes[idx] = "0" + codes[idx]  # 当前是否为左节点
            else:
                codes[idx] = "1" + codes[idx]

            node = node.parent  # 依次向上访问到根节点

    return codes


if __name__ == '__main__':
    logging.basicConfig(format="[%(asctime)s %(filename)s:%(lineno)s] %(message)s",
                        level=logging.INFO,
                        filemode="a",
                        filename=None)

    letters_pros = [('B', 10), ('E', 15), ('C', 20), ('D', 20), ('A', 35)]
    nodes = create_nodes([item[1] for item in letters_pros])
    root = create_huffman_tree_x(nodes)
    codes = huffman_encoding(nodes, root)
    for item in zip(letters_pros, codes):
        logger.info("Label: {} pro: {} Huffman Code: {}".format(item[0][0], item[0][1], item[1]))
