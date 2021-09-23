#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        for _ in range(10):
            n = sum([int(ch)**2 for ch in str(n)])
        return n == 1
# @lc code=end

