# @before-stub-for-debug-begin
from python3problem678 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=678 lang=python3
#
# [678] 有效的括号字符串
#

# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:
        left_max = 0
        left_min = 0
        for ch in s:
            if ch == ')':
                if not left_max:
                    return False
                left_max -= 1
                left_min = left_min - 1 if left_min != 0 else 0
            elif ch == '*':
                left_max += 1
                left_min = left_min - 1 if left_min != 0 else 0
            else:
                left_max += 1
                left_min += 1

        return left_min == 0
            
# @lc code=end

