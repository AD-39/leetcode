# @before-stub-for-debug-begin
from python3problem169 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = None
        cnt = 0
        for num in nums:
            if num != ans:
                if cnt == 0:
                    ans = num
                    cnt = 1
                else:
                    cnt -= 1
            else:
                cnt += 1

        return ans
# @lc code=end

