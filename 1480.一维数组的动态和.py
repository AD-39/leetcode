#
# @lc app=leetcode.cn id=1480 lang=python3
#
# [1480] 一维数组的动态和
#

# @lc code=start
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [0]
        for item in nums:
            ans.append(ans[-1] + item)
        return ans[1:]

# @lc code=end

