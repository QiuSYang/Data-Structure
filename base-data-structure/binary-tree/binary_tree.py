"""
# 二叉树
"""
import os
import logging

logger = logging.getLogger(__name__)


class TreeNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def pre_order(root):
    """前序遍历二叉树, 借助迭代器+递归实现"""
    if root:
        yield root.val  # 访问根节点
        yield from pre_order(root.left)  # 访问左树
        yield from pre_order(root.right)  # 访问右树


def in_order(root):
    """中序遍历二叉树, 借助迭代器+递归实现"""
    if root:
        yield from pre_order(root.left)  # 访问左树
        yield root.val  # 访问根节点
        yield from pre_order(root.right)  # 访问右树


def post_order(root):
    """后序遍历二叉树, 借助迭代器+递归实现"""
    if root:
        yield from pre_order(root.left)  # 访问左树
        yield from pre_order(root.right)  # 访问右树
        yield root.val  # 访问根节点


if __name__ == '__main__':
    logging.basicConfig(format="[%(asctime)s %(filename)s: %(lineno)s] %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S",
                        level=logging.INFO,
                        filename=None,
                        filemode="a")

    logger.info("申请N个节点")
    singer = TreeNode("Taylor Swift")

    genre_country = TreeNode("Country")
    genre_pop = TreeNode("Pop")

    album_fearless = TreeNode("Fearless")
    album_red = TreeNode("Red")
    album_1989 = TreeNode("1989")
    album_reputation = TreeNode("Reputation")

    song_ls = TreeNode("Love Story")
    song_wh = TreeNode("White Horse")
    song_wanegbt = TreeNode("We Are Never Ever Getting Back Together")
    song_ikywt = TreeNode("I Knew You Were Trouble")
    song_sio = TreeNode("Shake It Off")
    song_bb = TreeNode("Bad Blood")
    song_lwymmd = TreeNode("Look What You Made Me Do")
    song_g = TreeNode("Gorgeous")

    logger.info("设置树节点之间的关系")
    singer.left, singer.right = genre_country, genre_pop
    genre_country.left, genre_country.right = album_fearless, album_red
    genre_pop.left, genre_pop.right = album_1989, album_reputation
    album_fearless.left, album_fearless.right = song_ls, song_wh
    album_red.left, album_red.right = song_wanegbt, song_ikywt
    album_1989.left, album_1989.right = song_sio, song_bb
    album_reputation.left, album_reputation.right = song_lwymmd, song_g

    logger.info("前序遍历: {}".format(list(pre_order(singer))))
    logger.info("中序遍历: {}".format(list(in_order(singer))))
    logger.info("后序遍历: {}".format(list(post_order(singer))))
