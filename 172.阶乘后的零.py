# @before-stub-for-debug-begin
from python3problem172 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        now = 5
        while now <= n:
            ans += n // now
            now *= 5
        return ans
# @lc code=end

