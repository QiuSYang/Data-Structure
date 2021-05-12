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
            """暴力搜索法"""
            arr_len = len(nums)
            if arr_len < 2:
                return [0, 0]
            cache = {}  # 哈希表
            for i in range(arr_len):
                # target - nums[i] 存在哈希表中, 说明已经找到目标值
                if target - nums[i] in cache:
                    return [cache[target - nums[i]], i]
                cache[nums[i]] = i
