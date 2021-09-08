#
# @lc app=leetcode.cn id=1221 lang=python3
#
# [1221] 分割平衡字符串
#

# @lc code=start
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cntL = cntR = 0
        ans = 0
        for ch in s:
            if ch == 'L':
                cntL += 1
            else:
                cntR += 1
            ans += 1 if cntL == cntR else 0
        return ans
# @lc code=end

