#
# @lc app=leetcode.cn id=502 lang=python3
#
# [502] IPO
#

# @lc code=start
from typing import *
import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if w >= max(capital):
            return w + sum(heapq.nlargest(k, profits))
        
        n = len(profits)
        
        arr = [(profits[i], capital[i]) for i in range(n)]
        arr.sort(key=lambda x:x[1])

        hq = []
        for i in range(k):
            while arr and arr[0][1] <= w:
                pro, cap = arr.pop(0)
                heapq.heappush(hq, -pro)
            if hq:
                min_neg_pro = heapq.heappop(hq)
                w -= min_neg_pro
        return w
# @lc code=end

sol = Solution()
sol.findMaximizedCapital(2,
0,
[1,2,3],
[0,1,1])