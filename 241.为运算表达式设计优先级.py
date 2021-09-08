#
# @lc app=leetcode.cn id=241 lang=python3
#
# [241] 为运算表达式设计优先级
#

# @lc code=start
from typing import *
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]

        ans = []
        for i, ch in enumerate(expression):
            if not ch.isdigit():
                exp1 = self.diffWaysToCompute(expression[:i])
                exp2 = self.diffWaysToCompute(expression[i+1:])
                
                for l in exp1:
                    for r in exp2:
                        if ch == '+':
                            ans.append(l + r)
                        elif ch == '-':
                            ans.append(l - r)
                        else:
                            ans.append(l * r)
        return ans
# @lc code=end
sol = Solution()
sol.diffWaysToCompute("2*3-4*5")

