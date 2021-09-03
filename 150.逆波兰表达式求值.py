#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

# @lc code=start
from typing import *
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if item == '+':
                stack.append(stack.pop()+stack.pop())
            elif item == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif item == '*':
                stack.append(stack.pop()*stack.pop())
            elif item == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(item))
        return stack[-1]
# @lc code=end
sol = Solution()
sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
)

