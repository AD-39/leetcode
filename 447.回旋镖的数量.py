#
# @lc app=leetcode.cn id=447 lang=python3
#
# [447] 回旋镖的数量
#

# @lc code=start
from typing import *

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = 0
        for i in range(n):
            ax, ay = points[i]
            len_cnt = DefaultDict(int)

            for j in range(n):
                bx, by = points[j]
                length = ((ax-bx)**2 + (ay-by)**2)**0.5
                len_cnt[length] += 1

            for val in len_cnt.values():
                ans += val*(val-1)
        return ans
                
# @lc code=end
sol = Solution()
sol.numberOfBoomerangs([[0,0],[1,0],[-1,0],[0,1],[0,-1]])

