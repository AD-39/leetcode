#
# @lc app=leetcode.cn id=275 lang=python3
#
# [275] H 指数 II
#

# @lc code=start
from typing import *
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, n
        
        while l < r:
            mid = (l + r) >> 1
            if citations[mid] >= n - mid:
                r = mid
            else:
                l = mid + 1
        return n - l
# @lc code=end
sol = Solution()
sol.hIndex([0,0])

