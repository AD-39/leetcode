# @before-stub-for-debug-begin
from python3problem371 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=371 lang=python3
#
# [371] 两整数之和
#

# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        ans = 0
        c = 0
        for i in range(11):
            a1 = a>>i & 1
            b1 = b>>i & 1
            ans += (a1 ^ b1 ^ c)<<i
            c = a1&b1 | b1&c | a1&c
        if ans >> 10:
            return -self.getSum(~ans, 1)
        else:
            return ans

# @lc code=end

