#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        #偷 不偷
        ans = [[nums[0],0] for i in range(n)]
        for i in range(1, n):
            ans[i][0] = ans[i-1][1] + nums[i]
            ans[i][1] = max(ans[i-1][0], ans[i-1][1])
        return max(ans[n-1])
# @lc code=end

