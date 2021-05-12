# 回溯算法

回溯算法其实就是我们常说的 DFS 算法，本质上就是一种暴力穷举算法。

**解决一个回溯问题，实际上就是一个决策树的遍历过程。**你只需要思考 3 个问题：

    1、路径：也就是已经做出的选择。
    
    2、选择列表：也就是你当前可以做的选择。
    
    3、结束条件：也就是到达决策树底层，无法再做选择的条件。

回溯算法的框架：

    result = []
    def backtrack(路径, 选择列表):
        if 满足结束条件:
            result.add(路径)
            return
        
        for 选择 in 选择列表:
            做选择
            backtrack(路径, 选择列表)
            撤销选择
            
**其核心就是 for 循环里面的递归，在递归调用之前「做选择」，在递归调用之后「撤销选择」**，特别简单。

多叉树的遍历框架:
    
    void traverse(TreeNode root) {
        for (TreeNode child : root.childern)
            // 前序遍历需要的操作
            traverse(child);
            // 后序遍历需要的操作
            }

回溯算法的核心框架:

    for 选择 in 选择列表:
        # 做选择
        将该选择从选择列表移除
        路径.add(选择)
        backtrack(路径, 选择列表)
        # 撤销选择
        路径.remove(选择)
        将该选择再加入选择列表

**只要在递归之前做出选择，在递归之后撤销刚才的选择，**就能正确得到每个节点的选择列表和路径。

## LeetCode-46. 全排列

Linked: https://leetcode-cn.com/problems/permutations/

代码实现: 
    
    class Solution:
        def permute(self, nums: List[int]) -> List[List[int]]:
            result = [] 
            track = []  # 记录路径
            self.backtrack(nums, track, result)
    
            return result
    
        def backtrack(self, nums: List[int], track: List[int], result: List[List[int]]):
            """路径：记录在 track 中
               选择列表：nums 中不存在于 track 的那些元素
               结束条件：nums 中的元素全都在 track 中出现"""
            if len(track) == len(nums):
                # 触发结束条件, 所有元素都已经存入track中
                result.append(track.copy())  # 数据拷贝
                return  
    
            # 依次访问列表每个元素
            for i in range(len(nums)):
                # 排除不合法的选择
                if nums[i] in track:
                    continue  # 去除重复元素
    
                # 做选择
                track.append(nums[i])
                # 进入下一层决策树
                self.backtrack(nums, track, result)
                # 取消选择
                track.pop()  # 删除最近一次添加的元素, 从新选择一次
                
## LeetCode-51. N 皇后

Linked: https://leetcode-cn.com/problems/n-queens/

代码实现：

    class Solution:
        def solveNQueens(self, n: int) -> List[List[str]]:
            result = []
            board = [['.' for _ in range(n)] for _ in range(n)]
            # print(board)
            self.backtrack(board, 0, result)
    
            return result
        
        def backtrack(self, board: List[list], row: int, result: List[List[str]]):
            """路径：board 中小于 row 的那些行都已经成功放置了皇后
               选择列表：第 row 行的所有列都是放置皇后的选择
               结束条件：row 超过 board 的最后一行"""
                # 触发条件
            if row == len(board):
                result.append(["".join(value) for value in board.copy()])  # 已经扫描到最后一行
                return 
    
            cols = len(board[row])
            for col in range(cols):
                # 依次扫描每行
                if not self.is_valid(board, row, col):
                    continue 
    
                # 做选择
                # print(board[row])
                board[row][col] = 'Q'
                # 进入下一行决策
                self.backtrack(board, row+1, result)
                # 撤销选择, 从新选择一次
                board[row][col] = '.'
        
        def is_valid(self, board: List[str], row: int, col: int):
            """检查当前放置位置是否有效"""
            rows, cols = len(board), len(board[0])
            # 检查列是否有皇后互相冲突
            for i in range(cols):
                if board[i][col] == 'Q':
                    return False
            # 检查右上方是否有皇后互相冲突
            i, j = row - 1, col + 1
            while i >=0 and j < cols:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1 
            # 检查左上方是否有皇后互相冲突
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False 
                i -= 1 
                j -= 1 
            
            return True

# BFS --- 广度优先搜索

## 框架

    // 计算从起点 start 到终点 target 的最近距离
    int BFS(Node start, Node target) {
        Queue<Node> q; // 核心数据结构
        Set<Node> visited; // 避免走回头路
        
        q.offer(start); // 将起点加入队列
        visited.add(start);
        int step = 0; // 记录扩散的步数
    
        while (q not empty) {
            int sz = q.size();
            /* 将当前队列中的所有节点向四周扩散 */
            for (int i = 0; i < sz; i++) {
                Node cur = q.poll();
                /* 划重点：这里判断是否到达终点 */
                if (cur is target)
                    return step;
                /* 将 cur 的相邻节点加入队列 */
                for (Node x : cur.adj())
                    if (x not in visited) {
                        q.offer(x);
                        visited.add(x);
                    }
            }
            /* 划重点：更新步数在这里 */
            step++;
        }
    }

队列 q 就不说了，BFS 的核心数据结构；cur.adj() 泛指 cur 相邻的节点，比如说二维数组中，cur 上下左右四面的位置就是相邻节点；visited 的主要作用是防止走回头路，大部分时候都是必须的，但是像一般的二叉树结构，没有子节点到父节点的指针，不会走回头路就不需要 visited。
            
## LeetCode-111. 二叉树的最小深度

Linked: https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/

代码实现: 

    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def minDepth(self, root: TreeNode) -> int:
            """广度优先搜索"""
            if root is None:
                return 0
            depth = 1  # root 本来就是一层
    
            queue = []  # 头部插入数据，尾部取数据()
            queue.append(root)
            while queue:
                size = len(queue)
                for i in range(size):
                    # 依次访问当前层所有节点
                    current_node = queue.pop()
                    if current_node.left is None and current_node.right is None:
                        return depth
                    if current_node.left is not None:
                        queue.insert(0, current_node.left)
                    if current_node.right is not None:
                        queue.insert(0, current_node.right)
                
                depth += 1  # 单层访问完深度+1
            
            return depth

## LeetCode-752. 打开转盘锁 

Linked: https://leetcode-cn.com/problems/open-the-lock/

代码实现:
    
    class Solution:
        def openLock(self, deadends: List[str], target: str) -> int:
            """BFS"""
            visited = []  # 记录已经穷举过的密码，防止走回头路
            queue = [] 
            step = 0 
            # 从起点开始启动广度优先搜索
            queue.append("0000")
            visited.append("0000")
            while queue:
                size = len(queue)
                for i in range(size):
                    cur = queue.pop()  # 获取队头元素
    
                    # 判断是否到达终点
                    if cur in deadends:
                        continue 
                    if cur == target:
                        return step 
    
                    # 将一个节点的未遍历相邻节点加入队列
                    for j in range(4):
                        # 四个位置依次操作一遍
                        up = self.plus_one(cur, j)
                        if up not in visited:
                            queue.insert(0, up)
                            visited.append(up)
                        
                        down = self.minus_one(cur, j)
                        if down not in visited:
                            queue.insert(0, down)
                            visited.append(up)
                step += 1 
    
            return -1 
    
        def plus_one(self, s: str, j: int):
            """s[j], 向上拨动一次"""
            nums = list(s)
            if nums[j] == '9':
                nums[j] = '0'
            else:
                nums[j] = str(int(nums[j]) + 1)
            
            s = "".join(nums) 
            
            return s 
        
        def minus_one(self, s: str, j: int):
            """s[j], 向下拨动一次"""
            nums = list(s)
            if nums[j] == '0':
                nums[j] = '9'
            else:
                nums[j] = str(int(nums[j]) - 1)
            
            s = "".join(nums) 
            
            return s 

## LeetCode-22. 括号生成

Linked: https://leetcode-cn.com/problems/generate-parentheses/

代码实现: 

    class Solution:
        def generateParenthesis(self, n: int) -> List[str]:
            result = []
            def backtrack(single: list, left: int, right: int):
                """回溯算法---dfs"""
                if len(single) == 2 * n:
                    # 验证其合法性
                    result.append("".join(single))
                    return 
                if left < n:
                    single.append('(')  # 选择
                    backtrack(single, left+1, right)  # 递归
                    single.pop() # 撤销选择
                if right < left:
                    single.append(')')
                    backtrack(single, left, right+1)  # 递归
                    single.pop() 
            
            backtrack([], 0, 0)
    
            return result 
