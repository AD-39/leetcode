#
# @lc app=leetcode.cn id=1109 lang=python3
#
# [1109] 航班预订统计
#

# @lc code=start
import itertools
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        pre_sum = [0]*n
        for fp, tp, seat in bookings:
            pre_sum[fp-1]+=seat
            if tp != n:
                pre_sum[tp]-=seat
        
        return list(itertools.accumulate(pre_sum))
   
# @lc code=end

