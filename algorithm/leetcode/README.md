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
