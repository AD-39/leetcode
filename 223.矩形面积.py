#
# @lc app=leetcode.cn id=223 lang=python3
#
# [223] 矩形面积
#

# @lc code=start
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        def get_s(x1,x2,y1,y2):
            return abs(x1-x2) * abs(y1-y2)

        s = get_s(ax1,ax2,ay1,ay2) + get_s(bx1,bx2,by1,by2)
        
        x = sorted([ax1,ax2,bx1,bx2])
        y = sorted([ay1,ay2,by1,by2])

        if not (sorted([ax1,ax2]) == x[0:2] or sorted([ax1,ax2]) == x[2:]\
            or sorted([ay1,ay2]) == y0[0:2] or sorted([ay1,ay2]) == y[2:]):
            s -= get_s(x[1],x[2],y[1],y[2])

        return s

# @lc code=end

