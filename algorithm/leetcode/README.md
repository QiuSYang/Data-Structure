# LeetCode顺序做题积累

## LeetCode-1. 两数之和

Linked: https://leetcode-cn.com/problems/two-sum/

代码实现: 

    class Solution:
        # def twoSum(self, nums: List[int], target: int) -> List[int]:
        #     """暴力搜索法"""
        #     arr_len = len(nums)
        #     if arr_len < 2:
        #         return [0, 0]
        #     for i in range(arr_len-1):
        #         for j in range(i+1, arr_len):
        #             if nums[i] + nums[j] == target:
        #                 return [i, j]
            
        #     return [0, 0]
    
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            """哈希表方式"""
            arr_len = len(nums)
            if arr_len < 2:
                return [0, 0]
            cache = {}  # 哈希表
            for i in range(arr_len):
                # target - nums[i] 存在哈希表中, 说明已经找到目标值
                if target - nums[i] in cache:
                    return [cache[target - nums[i]], i]
                cache[nums[i]] = i

## LeetCode-2. 两数相加

Linked: https://leetcode-cn.com/problems/add-two-numbers/

代码实现: 

    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    class Solution:
        def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
            """数字已经按链表反向存取，最低在链头"""
            result = temp = ListNode()  # 存储结果列表, 以及链表引用
            carry_value = 0  # 进位值 
            while l1 or l2:
                value1 = l1.val if l1 else 0  # 链表为空之后, 值设置为0 
                value2 = l2.val if l2 else 0 
                sum_value = value1 + value2 + carry_value 
                save_value = sum_value % 10  # 当前位置保留值
                carry_value = sum_value // 10 
                # temp.val = save_value
                temp.next = ListNode(save_value)  # 数据添加进链表
                temp = temp.next 
                if l1:
                    # 向下访问
                    l1 = l1.next 
                if l2:
                    # 向下访问
                    l2 = l2.next 
            
            if carry_value > 0:
                # 如果还存在进位值, 添加在末尾
                temp.next = ListNode(carry_value) 
    
            return result.next

## LeetCode-3. 无重复字符的最长子串

Linked: https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

代码实现:

    class Solution:
        def lengthOfLongestSubstring_(self, s: str) -> int:
            result = []
            max_value = -1
            for c in s:
                if c not in result:
                    # 没有重复的字符加入列表
                    result.append(c)
                else:
                    max_value = max(max_value, len(result))  # 获取当前最大子串
                    index = result.index(c)  # 获取子串当前元素的索引位置
                    result = result[index+1:]  # 去除索引之前的元素
                    result.append(c)  # 将新的元素插入列表
            max_value = max(max_value, len(result))
    
            return max_value
    
        def lengthOfLongestSubstring(self, s: str) -> int:
            """动态规划
            状态转移方程: 给出一个字符串Si，已知它的最长子串长度为Li，如果在Si的末尾追加一个字符C，
            即Si+1=Si+C，那么Si+1的最长子串是多少？
            即lengthOfLongestSubString(Si+1)=max(Li,len(C结尾的无重复子串))
            """
            def find_left(s):
                tmp_str = s[-1]
                j = len(s) - 2
                while j >= 0 and s[j] not in tmp_str:
                    tmp_str += s[j]
                    j -= 1
                return tmp_str 
    
            length = len(s) 
            dp = [0] * (length + 1)
            for i in range(1, length+1):
                sub_s = s[:i]
                # 以s[i-1]字符结尾的无重复子串
                max_c_end_sub_str = find_left(sub_s)
                dp[i] = max(dp[i-1], len(max_c_end_sub_str))
            
            return dp[length]

## LeetCode-剑指 Offer 14- I. 剪绳子

Linked: https://leetcode-cn.com/problems/jian-sheng-zi-lcof/

代码实现:

    class Solution:
        def cuttingRope_greedy(self, n: int) -> int:
            """ 贪心算法
            2 = 1 + 1 = 1 * 1
            3 = 2 + 1 = 2 * 1
            4 = 2 + 2 = 2 * 2 = 3^(4//3-1) * 4 , 4%3 = 1 
            5 = 3 + 2 = 3 * 2 = 3^(5//3) * 2, 5%3 = 2 
            6 = 3 + 3 = 3 * 3 = 3^(6//3), 6%3 = 0
            7 = 3 + 4 = 3 * 4 = 3^(7//3-1) * 4, 7%3 = 1
            8 = 3 + 3 + 2 = 3 * 3 * 2 = 3^(8//3) * 2, 8%3 = 2 
            9 = 3 + 3 + 3 = 3 * 3 * 3 = 3(9//3), 9% = 0
            """
            if n <= 3:
                return n - 1 
            a, b = n//3, n%3  # 均分为三等分乘积最大
            if b == 0:
                return 3 ** a 
            elif b == 1:
                return 3 **(a-1) * 4 
            
            return 3 ** a * 2 
    
        def cuttingRope(self, n: int) -> int:
            """动态规划
            状态: f(n), 代表长度为n的绳子的最大切分乘积
            转移方程: f(n) = max(f(n), f(i)*f(n-i)), 即当前切出的长度最大乘积*剩长度的最大乘积
            初始条件: 初始条件，就是 1，2，3。通过验证也确实说明了这点，1 就不用说了肯定不能剪了；
            2 的话如果剪得话只能是 1、1，由于 1×1<2 所以到 2 也不要再剪了；
            3 的话可以剪为 1、2，1×2<3, 所以到 3 的时候也不要再剪了；
            对于4，我们可以发现 2×2<=4， 这时候剪不剪都无所谓；
            对于5，2×3>5，这时候有必要剪一刀，而且从4开始之后的都有必要剪。
            """
            if n < 4:
                return n-1
            dp = [0]*(n+1)
            # base case, 剩下长度为这几种特殊case, 无需再剪切
            dp[1] = 1
            dp[2] = 2
            dp[3] = 3
            for i in range(4, n+1):
                # 从4开始依次计算每种绳长切分的最大乘积
                for j in range(1, i//2+1):  # i//2只有进行一半操作, i-j包含另一半
                    # 每次切出的绳子长度
                    dp[i] = max(dp[i], dp[j] * dp[i - j])  # 状态转移方程
            
            return dp[n]

## LeetCode-剑指 Offer 14- II. 剪绳子

Linked: https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof/

代码实现:

    class Solution:
        def cuttingRope(self, n: int) -> int:
            # 如果 n = 2, 则结果为 1 * 1 = 1
            # 如果 n = 3, 则结果为 1 * 2 = 2
            # 这里和dp[2], dp[3]不一样，因为题目要求至少要切一刀
            if n <= 3:
                return n - 1
    
            # dp[i] 表示 长度为 i 的绳子的最大乘积（包含切 0 刀的情况）
            dp = [0 for _ in range(n+1)]
    
            dp[0] = 0   # 绳长为0，怎么切都是0
            dp[1] = 1   # 绳长为1，一刀也不切乘积最大
            dp[2] = 2   # 绳长为2，一刀也不切乘积最大
            dp[3] = 3   # 绳长为3，一刀也不切乘积最大
    
            # 当 n >= 4 时，切一刀的乘积 不再小于 一刀也不切的，开始动态规划
    
            '''
            dp[i] = max(dp[j]*dp[i-j], dp[i]) 的意思是，选择是否要在j的位置切一刀。
                切完后，总乘积就变成了：j左边的最大乘积 * 右边的最大乘积 （dp[j-0]*dp[i-j]）
                不切的话，总乘积保持不变
    
            想要dp[n]，需要 {dp[i], i < n}, 所以正向计算dp
            对于每一个i，尝试所有的可以切的位置（0 ~ i-1），取他们中最大的那个
            '''
            for i in range(4, n+1):
                for j in range(1, i+1):
                    dp[i] = max(dp[i], dp[j]*dp[i-j])
            
            return dp[n] % 1000000007  # 取余避免越界
    
            def cuttingRope(self, n: int) -> int:
                """参考链接:https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof/solution/mian-shi-ti-14-ii-jian-sheng-zi-iitan-xin-er-fen-f/"""
                if n <= 3: return n - 1
                a, b, p, x, rem = n // 3 - 1, n % 3, 1000000007, 3 , 1
                while a > 0:
                    if a % 2: rem = (rem * x) % p
                    x = x ** 2 % p
                    a //= 2
                if b == 0: return (rem * 3) % p # = 3^(a+1) % p
                if b == 1: return (rem * 4) % p # = 3^a * 4 % p
                return (rem * 6) % p # = 3^(a+1) * 2  % p

## LeetCode-剑指 Offer 19. 正则表达式匹配

Linked: https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof/

解析: https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof/solution/zheng-ze-biao-da-shi-pi-pei-by-leetcode-s3jgn/

代码实现:
    
    class Solution:
        def isMatch(self, s: str, p: str) -> bool:
            """动态规划
            状态: f[i][j]表示 ss 的前 ii 个字符与 pp 中的前 jj 个字符是否能够匹配
            转移方程:                     |f[i-1]f[j-1], s[i] == p[j]
                      | if p[j] != '*' = |False, s[i] != p[j]  
            f[i][j] = |
                      |otherwise = |f[i-1][j] or f[i][j-2], s[i] == p[j-1]
                                   |f[i][j-2], s[i] != p[j]"""
            m, n = len(s), len(p)
    
            def match(i: int, j: int) -> bool:
                if i == 0:
                    return False
                if p[j - 1] == '.':
                    return True
                return s[i - 1] == p[j - 1]
    
            dp = [[False] * (n + 1) for _ in range(m + 1)]
            dp[0][0] = True
            for i in range(m+1):
                for j in range(1, n+1):
                    if p[j-1] == '*':
                        dp[i][j] |= dp[i][j-2]  # 抛弃p串*之前的字符和当前字符
                        if match(i, j-1):
                            dp[i][j] |= dp[i-1][j]  # s串存在连续多个与p[j-1]相同的字符
                    else:
                        if match(i, j):
                            dp[i][j] |= dp[i-1][j-1]
    
            return dp[m][n] 

## LeetCode-剑指 Offer 42. 连续子数组的最大和

Linked: https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/

代码实现:

    class Solution:
        def maxSubArray(self, nums: List[int]) -> int:
            """动态规划
               状态: dp[i], 代表以元素 nums[i]为结尾的连续子数组最大和
               转移方程: dp[i] = max(num[i], dp[i-1] + nums[i]), 
               即当前元素之与前i-1的最大数组和+nums[i]的最大值"""
            n = len(nums)   
            dp = [0] * n
            dp[0] = nums[0]  # base case 
            for i in range(1, n):
                dp[i] = max(nums[i], dp[i-1] + nums[i])
            
            # 求状态数组中的最大值
            result = float("-inf")
            for i in range(n):
                result = max(result, dp[i])
            
            return result

## LeetCode-4. 寻找两个正序数组的中位数

Linked: https://leetcode-cn.com/problems/median-of-two-sorted-arrays/

解析参考链接: https://leetcode-cn.com/problems/median-of-two-sorted-arrays/

代码实现: 

    class Solution:
        def findMedianSortedArrays__(self, nums1: List[int], nums2: List[int]) -> float:
            """常规方法 O(n)"""
            def merge(nums1, nums2):
                """合并数组"""
                n, m = len(nums1), len(nums2)
                i, j = 0, 0
                merge_num = []
                while i<n and j<m:
                    if nums1[i] < nums2[j]:
                        merge_num.append(nums1[i])
                        i += 1
                    else:
                        merge_num.append(nums2[j])
                        j += 1 
                start = i if i<n else j 
                end = n if i<n else m 
                temp_num = nums1 if i<n else nums2
                # 将剩余数据压入列表
                merge_num.extend(temp_num[start:end])
    
                # print(merge_num)
                return merge_num 
            merge_num = merge(nums1, nums2)
    
            length = len(merge_num)
    
            if length%2 == 0:
                index = length//2
                return (merge_num[index-1] + merge_num[index])/2.0
            else:
                index = length//2
                return merge_num[index]
    
        def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
            """二分查找法, O(log(n+m))"""
            def getKthElement(k):
                """
                - 主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
                - 这里的 "/" 表示整除
                - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
                - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
                - 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
                - 这样 pivot 本身最大也只能是第 k-1 小的元素
                - 如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
                - 如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
                - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
                """
                
                index1, index2 = 0, 0
                while True:
                    # 特殊情况
                    if index1 == m:
                        return nums2[index2 + k - 1]
                    if index2 == n:
                        return nums1[index1 + k - 1]
                    if k == 1:
                        return min(nums1[index1], nums2[index2])
    
                    # 正常情况
                    newIndex1 = min(index1 + k // 2 - 1, m - 1)
                    newIndex2 = min(index2 + k // 2 - 1, n - 1)
                    pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                    if pivot1 <= pivot2:
                        k -= newIndex1 - index1 + 1
                        index1 = newIndex1 + 1
                    else:
                        k -= newIndex2 - index2 + 1
                        index2 = newIndex2 + 1
            
            m, n = len(nums1), len(nums2)
            totalLength = m + n
            if totalLength % 2 == 1:
                # 奇数
                return getKthElement((totalLength + 1) // 2)
            else:
                # 偶数
                return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2

## LeetCode-5. 最长回文子串 

Linked: https://leetcode-cn.com/problems/longest-palindromic-substring/

代码实现: 

    class Solution:
        """测试用例："aacabdkacaa" 无法过"""
        def longestPalindrome(self, s: str) -> str:
            """动态规划, 将S字符串反转, 转化为求解最长子串
            状态: dp[i][j], 代表以s[i]字符结尾的最长子串
            转移方程: dp[i][j] = dp[i-1][j-1] + 1"""
            sr = s[::-1]
            n, m = len(s), len(sr)
            dp = [[0]*(m+1) for _ in range(n+1)]
    
            max_value = 0  # 最大公共子串长度
            end_index = 0
            for i in range(1, n+1):
                for j in range(1, m+1):
                    if s[i-1] == sr[j-1]:
                        dp[i][j] = dp[i-1][j-1] + 1 
                    if dp[i][j] > max_value:
                        max_value = dp[i][j]
                        end_index = i  # 以 i 位置结尾的字符
    
            sub_str = s[end_index-max_value:end_index]    
    
            return sub_str

## LeetCode-剑指 Offer 47. 礼物的最大价值

Linked: https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/

代码实现: 

    class Solution:
        def maxValue(self, grid: List[List[int]]) -> int:
            """动态规划
            状态: dp[i][j], 代表从(0,0)坐标到(i,j)坐标的最大路径和
            转移方程: dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j], 
            即左边最大路径与上方最大路径的最大值 + 当前坐标值"""
            n, m = len(grid), len(grid[0])
    
            dp = [[0]*(m+1) for _ in range(n+1)]  # base case 价值大于0 
            for i in range(1, n+1):
                for j in range(1, m+1):
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1] 
            
            return dp[n][m]

## LeetCode-剑指 Offer 63. 股票的最大利润

Linked: https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/

代码实现:

    class Solution:
        def maxProfit_dp(self, prices: List[int]) -> int:
            """动态规划, 类似于求解最长上升子序列
            状态: dp[i], 代表在i时刻可以获取的最大利润
            转移方程: dp[i] = max(prices[i]-min_prices, dp[i-1]), 
            即以prices[i]价格卖出, 当前可获取的价值与i-1时可获取的最大价值的最大值"""
            if not prices:
                return 0 
            n = len(prices)
            dp = [0] * (n+1)  # base case dp[0] = 0 
    
            min_i_value = prices[0] 
            for i in range(1, n):
                dp[i] = max(prices[i] - min_i_value, dp[i-1])
                min_i_value = min(min_i_value, prices[i])  # 求解以prices[i]结尾子串的最小值
            
            return dp[n-1]
        
        def maxProfit(self, prices: List[int]) -> int:
            """暴力遍历法"""
            if not prices:
                return 0 
            n = len(prices)
            max_value = 0
            pre_min_prices = prices[0]  # 当前点之前的最小值
            for i in range(n):
                # 当前点卖出的最大利润
                max_value = max(max_value, prices[i] - pre_min_prices)
                pre_min_prices = min(pre_min_prices, prices[i])
    
            return max_value

## LeetCode-6. Z 字形变换

Linked: https://leetcode-cn.com/problems/zigzag-conversion/

代码实现: 

    class Solution:
        def convert(self, s: str, numRows: int) -> str:
            """按列遍历，指针上下波动"""
            if numRows < 2:
                return s 
            
            results = ["" for _ in range(numRows)]  # 记录每一行的字符
            i = 0 
            flage = -1  # 初始设置为向上
            for c in s:
                if i == 0 or i == numRows - 1:
                    flage = -flage  # 调转方向 
                results[i] += str(c)
                i += flage 
            
            return "".join(results)

## LeetCode-7. 整数反转

Linked: https://leetcode-cn.com/problems/reverse-integer/

代码实现:

    class Solution:
        def reverse(self, x: int) -> int:
            """数学"""
            INT_MIN, INT_MAX = -2**31, 2**31 - 1
    
            rev = 0
            while x != 0:
                # INT_MIN 也是一个负数，不能写成 rev < INT_MIN // 10
                # -2147483648 // 10 = -214748365 可以发现向下多-1
                if rev < INT_MIN//10 + 1 or rev > INT_MAX // 10:
                    # 数组越界, 倒数第二次
                    return 0  
                digit = x % 10
                # Python3 的取模运算在 x 为负数时也会返回 [0, 9) 以内的结果，因此这里需要进行特殊判断
                if x < 0 and digit > 0:
                    digit -= 10
                # 同理，Python3 的整数除法在 x 为负数时会向下（更小的负数）取整，因此不能写成 x //= 10
                x = (x - digit) // 10 
    
                rev = rev*10 + digit 
            
            return rev 

## LeetCode-8. 字符串转换整数 (atoi)

Linked: https://leetcode-cn.com/problems/string-to-integer-atoi/

代码实现:

    class Automaton:
        """自动机"""
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        def __init__(self):
            self.state = 'start'
            self.sign = 1
            self.ans = 0
            self.table = {
                'start': ['start', 'signed', 'in_number', 'end'],
                'signed': ['end', 'end', 'in_number', 'end'],
                'in_number': ['end', 'end', 'in_number', 'end'],
                'end': ['end', 'end', 'end', 'end'],
            }  # 状态转移列表
    
        def get_col(self, c):
            if c.isspace():
                return 0 
            elif c in ['+', '-']:
                return 1
            elif c.isdigit():
                return 2
            return 3 
        
        def get(self, c):
            self.state = self.table[self.state][self.get_col(c)]  # 从一个状态转移到另一个状态
            if self.state == "in_number":
                self.ans = self.ans * 10 + int(c)
                self.ans = min(self.ans, self.INT_MAX) if self.sign == 1 else min(self.ans, -self.INT_MIN)
            elif self.state == "signed":
                self.sign = 1 if c == '+' else -1
    
    
    class Solution:
        def myAtoi(self, s: str) -> int:
            """自动机"""
            automaton = Automaton()
            for c in s:
                automaton.get(c)
            return automaton.sign * automaton.ans

## LeetCode-14. 最长公共前缀

Linked: https://leetcode-cn.com/problems/longest-common-prefix/

代码实现:

    class Solution:
        def longestCommonPrefix_(self, strs: List[str]) -> str:
            """横向扫描寻找最大前缀"""
            # 用 LCP(s1, s2, ..., sn)表示字符串s1, ... sn最长公共前缀
            # LCP(s1, s2, ..., sn) = LCP(LCP(LCP(S1, S2), S3), ... Sn)
            if not strs:
                return str()
            prefix, count = strs[0], len(strs)
            for i in range(1, count):
                prefix = self.lcp(prefix, strs[i])
                if not prefix:
                    # 没有交集, 直接退出返回
                    break
            return prefix 
        
        def lcp(self, str1, str2):
            """求解两个字符串的最大公共前缀"""
            min_len = min(len(str1), len(str2))
            index = 0
            while index < min_len:
                if str1[index] == str2[index]:
                    index += 1 
                else:
                    break 
            
            return str1[:index]
    
        def longestCommonPrefix(self, strs: List[str]) -> str:
            """纵向扫描寻找最大前缀"""
            if not strs:
                return ""
            
            length, count = len(strs[0]), len(strs)
            for i in range(length):
                c = strs[0][i]  # 依次扫描字符串1的每个字符
                if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
                    # 依次去每个字符串的第i个字符与字符串1的第i个字符比较, 
                    # 或者某个字符串已经访问到最后一个元素
                    return strs[0][:i]
            
            return strs[0]  # 第一个字符串为最长公共前缀

## LeetCode-15. 三数之和

Linked: https://leetcode-cn.com/problems/3sum/

代码实现:

    class Solution:
        def threeSum(self, nums: List[int]) -> List[List[int]]:
            """排序+双指针法，固定左边界记为k"""
            n = len(nums)
            if n < 3:
                return [] 
            nums = sorted(nums)  # 排序，所有负数都在左边
            # print(nums)
            
            res = []  # 存储结果列表
            k = 0  # 存储最左边元素的索引
            for k in range(n-2):  # 去除i(中间), j(右边)两个元素
                if nums[k] > 0:
                    break  # 没有满足条件子数组
                if k > 0 and nums[k] == nums[k-1]:
                    continue  # 连续相同元素
                i, j = k + 1, n - 1  # 双指针位置
                while i < j:
                    # 扫描到相同位置直接退出
                    s = nums[k] + nums[i] + nums[j]
                    if s < 0:
                        i += 1 
                        while i < j and nums[i] == nums[i-1]:
                            # 相同元素， 左边界持续移动
                            i += 1
                    elif s > 0:
                        j -= 1
                        while i < j and nums[j] == nums[j+1]:
                            # 相同元素， 右边界持续移动
                            j -= 1 
                    else:
                        res.append([nums[k], nums[i], nums[j]])
    
                        # 同时移动
                        i += 1
                        j -= 1
                        while i < j and nums[i] == nums[i - 1]: 
                            i += 1
                        while i < j and nums[j] == nums[j + 1]: 
                            j -= 1
            
            return res 
    
            
        