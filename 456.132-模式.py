from typing import *
#
# @lc app=leetcode.cn id=456 lang=python3
#
# [456] 132 模式
#

# @lc code=start
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        left_min = [float('inf')]

        for item in nums:
            left_min.append(min(left_min[-1], item))

        #单调栈，上小下大
        stack = []
        for i in range(len(nums)-1, 0, -1):
            while stack and stack[-1] <= left_min[i]:
                stack.pop(-1)

            if stack and stack[-1] < nums[i]:
                return True
            else:
                stack.append(nums[i])
               
                
        return False

# @lc code=end

sol = Solution()
sol.find132pattern([-1,3,2,0])