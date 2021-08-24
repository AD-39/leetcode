# @before-stub-for-debug-begin
# from python3problem789 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=789 lang=python3
#
# [789] 逃脱阻碍者
#

# @lc code=start
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        tx = target[0]
        ty = target[1]
        dis = [abs(x-tx)+abs(y-ty) for x,y in ghosts]

        return min(dis)>abs(tx)+abs(ty)

# @lc code=end
