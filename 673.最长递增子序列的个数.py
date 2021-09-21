# @before-stub-for-debug-begin
from python3problem673 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=673 lang=python3
#
# [673] 最长递增子序列的个数
#

# @lc code=start
import bisect
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[nums[0]]]
        cnt = [[1]]

        for num in nums[1: n]:
            if num > dp[-1][-1]:
                p = bisect.bisect_left(list(reversed(dp[-1])), num)
                dp.append([num])
                cnt.append([sum(list(reversed(cnt[-1]))[:p])])
            else:
                p = bisect.bisect_left([line[-1] for line in dp], num)
                dp[p].append(num)
                if p != 0:
                    q = bisect.bisect_left(list(reversed(dp[p-1])), num)
                    cnt[p].append(sum(list(reversed(cnt[p-1]))[:q]))
                else:
                    cnt[p].append(1)
        return sum(cnt[-1])
# @lc code=end

