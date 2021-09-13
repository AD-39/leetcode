#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        p = 1
        sq_num = []
        while p**2 <= n:
            sq_num.append(p**2)
            p += 1

        ans = [float('inf')] * (n + 1)
        ans[0] = 0
        for i in range(n + 1):
            for j in sq_num:
                if i+j <= n:
                    ans[i+j] = min(ans[i+j], ans[i]+1)
        return ans[-1]

# @lc code=end
sol = Solution()
sol.numSquares(1)

