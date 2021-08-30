#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
from typing import *
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)

        ans = [[0,0,0,0] for i in range(n)]
        #偷0偷n 偷0不偷n 不偷0偷n 都不偷
        ans[0] = [nums[0], nums[0], 0, 0]
        ans[1] = [0, nums[0], nums[1], 0]

        for i in range(2, n):
            ans[i][0] = max([ans[i-1][1], ans[i-2][0], ans[i-2][1]]) + nums[i]
            ans[i][1] = max(ans[i - 1][0], ans[i - 2][0])
            ans[i][2] = max([ans[i-1][3], ans[i-2][2], ans[i-2][3]]) + nums[i]
            ans[i][3] = max(ans[i - 1][2], ans[i - 2][2])

        return max(ans[-1][1], ans[-1][2], ans[-1][3])

        

# @lc code=end
sol = Solution()
sol.rob([1,3,1,3,100])

