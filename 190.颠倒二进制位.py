#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            num = n>>i & 1
            ans = ans * 2 + num
        return ans
# @lc code=end

