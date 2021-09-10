#
# @lc app=leetcode.cn id=274 lang=python3
#
# [274] H 指数
#

# @lc code=start
from typing import *
import bisect
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        citations.reverse()
        citations = [item - i - 1 for i, item in enumerate(citations)]
        citations.reverse()
        return len(citations) - bisect.bisect_left(citations, 0)
# @lc code=end
sol = Solution()
sol.hIndex([3,0,6,1,5])

