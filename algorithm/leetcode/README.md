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
