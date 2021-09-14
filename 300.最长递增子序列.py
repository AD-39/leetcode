# @before-stub-for-debug-begin
from python3problem300 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # #####平平无奇的dp
        # n = len(nums)
        # dp = [1]*n
        # for i in range(n):
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        # return max(dp)

        ##########高端大气的O(nlgn)
        d = [nums[0]]
        for num in nums[1:]:
            if num > d[-1]:
                d.append(num)
            else:
                p = bisect.bisect_left(d, num) 
                d[p] = num
        return len(d)
        
# @lc code=end

