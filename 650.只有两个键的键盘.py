#
# @lc app=leetcode.cn id=650 lang=python3
#
# [650] 只有两个键的键盘
#

# @lc code=start
class Solution:
    def minSteps(self, n: int) -> int:
        ans = 0
        while n != 1:
            p = 2
            while n % p != 0:
                p += 1
            ans += p
            n //= p
        return ans
# @lc code=end

