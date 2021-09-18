#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ''
        while columnNumber:
            p = columnNumber % 26
            if p == 0:
                ans = 'Z' + ans
                columnNumber = columnNumber//26 - 1
            else:
                ans = chr(p + 64) + ans
                columnNumber //= 26
        return ans
# @lc code=end

