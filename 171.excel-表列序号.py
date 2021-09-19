# @before-stub-for-debug-begin
from python3problem171 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel 表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for ch in columnTitle:
            ans *= 26
            num = ord(ch) - 64
            ans += num
        return ans
# @lc code=end

