"""记录一些算法题"""

from typing import List
from queue import Queue


def numIslands(grid: List[List[str]]) -> int:
    """广度(宽度)优先搜索-bfs"""
    if not grid:
        return 0
    direct_coors = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # 四个方位offset

    index = 1  # 岛屿ID
    q = Queue()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                index += 1
                print("index value: {}".format(index))
                grid[i][j] = index  # 已经搜索过的位置置0

                q.put((i, j))  # 入列
                while True:
                    if q.empty():
                        break
                    cur = q.get()  # 元素出列
                    for offset in direct_coors:
                        # 四个方向广度优先搜索
                        row, col = cur[0] + offset[0], cur[1] + offset[1]
                        if (row < 0 or row >= len(grid)
                                or col < 0 or col >= len(grid[0])):
                            continue
                        if grid[row][col] == "1":
                            q.put((row, col))
                            grid[row][col] = str(index)  # 近邻周围值设置为index

    return index - 1


def numIslands_dfs(grid: List[List[str]]) -> int:
    """深度优先搜索---dfs"""
    if not grid:
        return 0
    index = 1
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                index += 1
                dfs(grid, i, j, index)

    return index - 1


def dfs(grid, row, col, index):
    """四个方向深度搜索---dfs"""
    if (row < 0 or row >= len(grid) or
            col < 0 or col >= len(grid[0]) or
            grid[row][col] != "1"):
        return

    grid[row][col] = str(index)  # 当前位置已经被访问, 置index

    # 四个方向DFS
    dfs(grid, row, col - 1, index)
    dfs(grid, row - 1, col, index)
    dfs(grid, row, col + 1, index)
    dfs(grid, row + 1, col, index)


if __name__ == '__main__':
    arr = [["1","1","0","0","0"],
           ["1","1","0","0","0"],
           ["0","0","1","0","0"],
           ["0","0","0","1","1"]]

    result = numIslands_dfs(arr)
    print(result)
