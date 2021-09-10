#
# @lc app=leetcode.cn id=682 lang=python3
#
# [682] 棒球比赛
#

# @lc code=start
from typing import *
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for ch in ops:
            if ch == 'C':
                stack.pop()
            elif ch == 'D':
                stack.append(stack[-1]*2)
            elif ch == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(ch))
        return sum(stack)

# @lc code=end
sol = Solution()
sol.calPoints(["5","-2","4","C","D","9","+","+"])

