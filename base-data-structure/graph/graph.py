"""
# 图(Graph)数据结构
"""
import os
import logging
from collections import deque

logger = logging.getLogger(__name__)


class UndirectedGraph(object):
    """无向图, 相互连接"""
    def __init__(self, vertex_num):
        self.v_num = vertex_num  # 图的顶点数
        self.adj_tbl = []  # 邻接表
        for _ in range(self.v_num + 1):
            self.adj_tbl.append([])

    def add_edge(self, s, t):
        """添加s顶点与t顶点, 两个顶点互通"""
        if s > self.v_num or t > self.v_num:
            return False

        self.adj_tbl[s].append(t)  # s顶点连接t顶点
        self.adj_tbl[t].append(s)  # t顶点连接s顶点

        return True

    def __len__(self):
        return self.v_num

    def __getitem__(self, index):
        if index > self.v_num:
            raise IndexError("No Such Vertex!")

        return self.adj_tbl[index]  # 获取第index顶点的关系链表

    def __repr__(self):
        return str(self.adj_tbl)

    def __str__(self):
        return str(self.adj_tbl)


class DirectedGraph(object):
    """有向图, 构建两个顶点之间关系"""
    def __init__(self, vertex_num):
        self.v_num = vertex_num  # 图的顶点数
        self.adj_tbl = []  # 邻接表
        for _ in range(self.v_num + 1):
            self.adj_tbl.append([])

    def add_edge(self, frm, to):
        """构建有向图两个顶点之间的关系, 从frm顶点指向to顶点"""
        if frm > self.v_num or to > self.v_num:
            return False

        self.adj_tbl[frm].append(to)  # frm ---> to

    def __len__(self):
        return self.v_num

    def __getitem__(self, index):
        if index > self.v_num:
            raise IndexError("No Such Vertex!")

        return self.adj_tbl[index]  # 获取第index顶点的关系链表

    def __repr__(self):
        return str(self.adj_tbl)

    def __str__(self):
        return str(self.adj_tbl)


def find_vertex_by_degree(graph, start_vertex, degree):
    """通过度查顶点
       start_vertex: 起始顶点
    """
    if len(graph) <= 1:
        return []

    if degree == 0:
        return [start_vertex]

    d_vertices = []
    queue = deque()
    prev = [-1] * len(graph)
    visited = [False] * len(graph)
    visited[start_vertex] = True
    queue.append(start_vertex)
    while len(queue) > 0:
        sz = len(queue)
        for i in range(sz):
            v = queue.popleft()
            for adj_v in graph[v]:
                if not visited[adj_v]:
                    prev[adj_v] = v
                    visited[adj_v] = True
                    queue.append(adj_v)
        degree -= 1

        if degree == 0 and len(queue) != 0:
            return queue


if __name__ == '__main__':
    logging.basicConfig(format="[%(asctime)s %(filename)s: %(lineno)s]: %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S",
                        level=logging.INFO,
                        filename=None,
                        filemode="a")

    ug = UndirectedGraph(10)
    ug.add_edge(1, 9)
    ug.add_edge(1, 3)
    ug.add_edge(3, 2)
    logger.info("Print adjacency list: {}".format(ug))

    dg = DirectedGraph(10)
    dg.add_edge(1, 9)
    dg.add_edge(1, 3)
    dg.add_edge(3, 4)
    logger.info("Print adjacency list: {}".format(dg))

    g = UndirectedGraph(8)
    g.add_edge(0, 1)
    g.add_edge(0, 3)
    g.add_edge(1, 2)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.add_edge(4, 6)
    g.add_edge(5, 7)
    g.add_edge(6, 7)
    logger.info(g)
    logger.info(find_vertex_by_degree(g, 0, 4))
