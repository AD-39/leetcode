# @before-stub-for-debug-begin
from python3problem639 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=639 lang=python3
#
# [639] 解码方法 II
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        # 无前缀、1前缀、2前缀
        ans = [1,0,0]

        for ch in s:
            nxt = [0,0,0]
            if ch == '*':
                nxt[0] = (ans[0]+ans[1])*9 + ans[2]*6
                nxt[1] = ans[0]
                nxt[2] = ans[0]
            else:
                num = int(ch)
                if num == 0:
                    nxt[0] = ans[1] + ans[2]
                elif num == 1 or num == 2:
                    nxt[0] = sum(ans)
                    nxt[num] = ans[0]
                elif num <= 6:
                    nxt[0] = sum(ans)
                else:
                    nxt[0] = ans[0] + ans[1]
            nxt[0] %= 10**9 + 7
            ans = nxt
        return ans[0]

# @lc code=end

