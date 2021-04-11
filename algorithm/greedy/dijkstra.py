"""
# 最短路径问题的算法—戴克斯特拉算法
戴克斯特拉算法如下：
    1. 设来源节点的距离值为 0，其余节点的距离值为最大值；
    2. 选择并固定距离值最小的非固定节点；
    3. 依次松弛起点为当前节点的所有边，跳过终点已被固定的边；
    4. 重复（2）～（4）至所有节点都被固定。
"""
import os
import sys
import logging

logger = logging.getLogger(__name__)


class Graph(object):
    """使用图数据结构辅助进行Dijkstra算法实现"""
    def __init__(self):
        self.vertices = {}  # 顶点
        self.edges = []  # 边
        self.src = None

    def add_edge(self, start, end, dist, is_direct=True):
        """添加边(起点, 终点, 权值, 是否为双向)"""
        if is_direct:
            # 双向边
            self.edges.extend([(start, end, dist), (end, start, dist)])
        else:
            self.edges.append((start, end, dist))

    def get_vertices(self):
        """输出节点集合"""
        return set(sum(([edge[0], edge[1]] for edge in self.edges), []))

    def get_neighbours(self, vertice):
        """返回vertice节点的相邻节点集"""
        neighbours = []
        for edge in self.edges:
            if edge[0] == vertice:
                neighbours.append((edge[1], edge[2]))  # (节点, 权值)

        return neighbours

    def check_for_negative_weights(self):
        """输出图中是否有权重为负的边，没有返回False"""
        for edge in self.edges:
            if edge[2] < 0:
                return True
        return False

    def get_current_v(self, temp_vertices, dist):
        """输出temp_vertices中距离值最小的非固定节点"""
        if len(temp_vertices) == 0:
            return None
        return min(temp_vertices, key=lambda v: dist[v])  # 获取最小距离的固定点

    def print_solution(self, dist, predecessor):
        """输出所有节点的最短路径和路径距离"""
        for v in self.vertices:
            path = self.get_path(predecessor, v)
            # logger.info(self.src, "to ", v, " - Distance: ", dist[v], " Path :", path)
            logger.info("{} to {} - Distance {} Path {}".format(self.src, v, dist[v], path))

    def get_path(self, predecessor, v):
        """输出v节点的最短路径"""
        pred = predecessor[v]
        path = []
        path.append(v)
        while pred != None:
            path.append(pred)
            pred = predecessor[pred]

        path.reverse()

        return path

    def dijkstra(self, src):
        """最短路径算法，输出从src起始的，到所有节点的最短路线"""
        if self.check_for_negative_weights():
            logger.info("权重不能为负")
            return

        self.src = src  # 来源节点
        self.vertices = self.get_vertices()  # 节点集合
        dist = {v: sys.maxsize for v in self.vertices}  # 初始距离值为最大数
        dist[src] = 0
        predecessor = {
            v: None for v in self.vertices  # 初始前任节点为None
        }

        temp_vertices = self.vertices.copy()  # 未固定节点集合，初始为所有节点
        current_v = src
        while len(temp_vertices) > 0:
            neighbours = self.get_neighbours(current_v)
            for n in neighbours:
                if (n[0] in temp_vertices
                        and dist[current_v] + n[1] < dist[n[0]]):
                    dist[n[0]] = dist[current_v] + n[1]
                    predecessor[n[0]] = current_v

            temp_vertices.remove(current_v)
            current_v = self.get_current_v(temp_vertices, dist)  # 更新当前节点

        self.print_solution(dist, predecessor)


if __name__ == '__main__':
    logging.basicConfig(format="[%(asctime)s %(filename)s:%(lineno)s] %(message)s",
                        level=logging.INFO,
                        filemode="a",
                        filename=None)

    graph = Graph()  # 创建对象
    graph.add_edge("a", "b", 2, False)  # 单向边
    graph.add_edge("a", "c", 1, True)  # 双向边
    graph.add_edge("b", "d", 3, False)
    graph.add_edge("d", "f", 1, True)
    graph.add_edge("f", "e", 2, False)
    graph.add_edge("c", "e", 4, False)
    graph.add_edge("b", "c", 2, False)
    graph.add_edge("e", "b", 4, False)
    graph.add_edge("d", "e", 1, False)
    graph.add_edge("c", "d", 2, False)
    graph.dijkstra("a")  # 来源节点是a
