# 动态规划

## 动态规划特点与解题套路

![image](images/1.png)

首先，**动态规划问题的一般形式就是求最值**。动态规划其实是运筹学的一种最优化方法，只不过在计算机问题上应用比较多，比如说让你求**最长**递增子序列呀，**最小**编辑距离呀等等。

既然是要求最值，核心问题是什么呢？求解动态规划的核心问题是穷举。因为要求最值，肯定要把所有可行的答案穷举出来，然后在其中找最值呗。

首先，动态规划的穷举有点特别，因为这类问题**存在「重叠子问题**，如果暴力穷举的话效率会极其低下，所以需要「备忘录」或者「DP table」来优化穷举过程，避免不必要的计算。

而且，动态规划问题一定会**具备「最优子结构**，才能通过子问题的最值得到原问题的最值。

另外，虽然动态规划的核心思想就是穷举求最值，但是问题可以千变万化，穷举所有可行解其实并不是一件容易的事，只有列出**正确的「状态转移方程**，才能正确地穷举。

## 明确 base case -> 明确「状态」-> 明确「选择」 -> 定义 dp 数组/函数的含义。

按上面的套路走，最后的结果就可以套这个框架：

    # 初始化 base case
    dp[0][0][...] = base
    # 进行状态转移
    for 状态1 in 状态1的所有取值：
        for 状态2 in 状态2的所有取值：
            for ...
                dp[状态1][状态2][...] = 求最值(选择1，选择2...)

## LeetCode-322. 零钱兑换

给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

你可以认为每种硬币的数量是无限的。

示例 1：

    输入：coins = [1, 2, 5], amount = 11
    输出：3 
    解释：11 = 5 + 5 + 1

示例 2：

    输入：coins = [2], amount = 3
    输出：-1

示例 3：

    输入：coins = [1], amount = 0
    输出：0

示例 4：

    输入：coins = [1], amount = 1
    输出：1

示例 5：

    输入：coins = [1], amount = 2
    输出：2

Linked：https://leetcode-cn.com/problems/coin-change

代码实现:
    
    class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)  # 最小面值为1, 最大次数不会超过amount 
        # base case 
        dp[0] = 0  # 面值为0, 不需要凑钱
        # 外层 for 循环在遍历所有状态的所有取值
        for i in range(len(dp)):
            # 内层 for 循环在求所有选择的最小值
            for coin in coins:
                # 子问题无解，跳过
                if (i - coin < 0):
                    # 面值大于钱的总数, 舍弃此面值
                    continue 
                # 状态转移方程
                dp[i] = min(dp[i], 1+dp[i - coin])  # 当前钱所需的面值钱数=1+凑够(1 - coin)所需的钱数
        
        if dp[amount] == (amount + 1):
            return -1 
        
        return dp[amount] 
    
    # 方法二 --- 自顶而下的方法
    def coinChange(coins: List[int], amount: int):
        # 备忘录
        memo = dict()
        def dp(n):
            # 查备忘录，避免重复计算
            if n in memo: return memo[n]
            # base case
            if n == 0: return 0
            if n < 0: return -1
            res = float('INF')
            for coin in coins:
                subproblem = dp(n - coin)
                if subproblem == -1: continue
                res = min(res, 1 + subproblem)
    
            # 记入备忘录
            memo[n] = res if res != float('INF') else -1
            return memo[n]
    
        return dp(amount)

## 动态规划的本质

![image](images/2.png)

**解决两个字符串的动态规划问题，一般都是用两个指针 i,j 分别指向两个字符串的最后，然后一步步往前走，缩小问题的规模。**

## LeetCode-72. 编辑距离

Linked:https://leetcode-cn.com/problems/edit-distance/

代码实现:

    class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # base case 
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            dp[i][0] = i 
        for j in range(1, n+1):
            dp[0][j] = j 

        # 自底而上求解
        for i in range(1, m+1):
            for j in range(1, n+1):
                # 两种情况的状态转移方程
                if word1[i-1] == word2[j-1]:
                    # 当前字符不需要操作, 编辑次数等于上一次结果
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # 次数操作次数，等于上一次+1
                    # 理解哪个指针需要移动
                    dp[i][j] = min(
                        dp[i - 1][j] + 1,  # word1删除
                        dp[i][j - 1] + 1,  # word1插入
                        dp[i - 1][j - 1] + 1,  # word1替换
                    )

        # 储存着整个 s1 和 s2 的最小编辑距离
        return dp[m][n]
        
## 1143. 最长公共子序列

Linked：https://leetcode-cn.com/problems/longest-common-subsequence/
        
代码实现：

    class Solution:
        def longestCommonSubsequence(self, text1: str, text2: str) -> int:
            m, n = len(text1), len(text2)
            # base case 
            dp = [[0]*(n+1) for _ in range(m+1)]
    
            for i in range(1, m+1):
                for j in range(1, n+1):
                    if text1[i-1] == text2[j-1]:
                        # s1[i-1] 和 s2[j-1] 必然在 lcs 中, 上一次最大值+1
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        # s1[i-1] 和 s2[j-1] 至少有一个不在 lcs 中, 等于上一次最大值
                        dp[i][j] = max(
                            dp[i][j-1], 
                            dp[i-1][j], 
                        )
            
            return dp[m][n]

