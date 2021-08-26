#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
from typing import *
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        now_sum = 0
        pre_p = 0
        p = 0

        while p < len(nums):
            while p < len(nums) and now_sum < target:
                now_sum += nums[p]
                p += 1
            
            while target <= now_sum - nums[pre_p]:
                now_sum -= nums[pre_p]
                pre_p += 1
                
            if now_sum >= target:
                ans = min(ans, p - pre_p)
                now_sum -= nums[pre_p]
                pre_p += 1

        return ans if ans != float('inf') else 0

# @lc code=end

sol = Solution()
print(sol.minSubArrayLen(7,
[2,3,1,2,4,3]))

