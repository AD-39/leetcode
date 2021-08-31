#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
from typing import *
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l, r = 0, len(nums) - 1
        #随机选择一个数字，作为基准
        idx = random.randint(l, r)
        target = nums[idx]
        nums[0], nums[idx] = nums[idx], nums[0]

        #l停留在最后一个大于等于target的数字之后
        while l <= r:
            while l != len(nums) and nums[l] >= target:
                l += 1
            while r != 0 and nums[r] < target:
                r -= 1
            if l < r:
                nums[l], nums[r] = nums[r], nums[l]
        #将l-1的位置写为target，之前全部为大于等于，之后全部为小于
        nums[0], nums[l-1] = nums[l-1], nums[0]
        if l == k:
            return target
        elif l > k:
            return self.findKthLargest(nums[:l-1], k)
        else:
            return self.findKthLargest(nums[l:], k-l)
# @lc code=end

sol = Solution()
sol.findKthLargest([3,2,1,5,6,4],2)
