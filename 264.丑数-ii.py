#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#

# @lc code=start
import math
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans = [0, 1]
        p2 = p3 = p5 = 1
        while len(ans) < n + 1:
            tmp = min([ans[p2]*2, ans[p3]*3, ans[p5]*5])
            ans.append(tmp)
            ####用if而非elif可以避免重复
            if ans[p2]*2 == tmp:
                p2 += 1
            if ans[p3]*3 == tmp:
                p3 += 1
            if ans[p5]*5 == tmp:
                p5 += 1

        return ans[n]

# @lc code=end
sol = Solution()
sol.nthUglyNumber(1600)
