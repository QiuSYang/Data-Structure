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

