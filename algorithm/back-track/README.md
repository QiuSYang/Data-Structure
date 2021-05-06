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
