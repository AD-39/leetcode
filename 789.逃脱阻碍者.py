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
    def __init__(self) -> None:
        pass

    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        self.map = [[4000 for i in range(2000)] for i in range(2000)]
        target[0] += 1000
        target[1] += 1000
        startx = starty = 1000  
        for i in range(len(ghosts)):
            ghosts[i][0] += 1000
            ghosts[i][1] += 1000

        self.tx = target[0]
        self.ty = target[1]
        
        self.mapMask(ghosts)

        return self.findPath(startx, starty, 0)
    
    def mapMask(self, ghosts):
        
        for i in range(2000):
            for j in range(2000):
                for x,y in ghosts:
                    self.map[i][j] = min(self.map[i][j], 
                                abs(i - x) + abs(j - y))

    def findPath(self, x, y, len):
        #被抓到
        if self.map[x][y] <= len:
            return False
        #到达终点
        if x == self.tx and y ==self.ty:
            return True

        dir = [[0,1],[0,-1],[1,0],[-1,0]]

        ans =False
        for dx,dy in dir:
            nx = x + dx
            ny = y + dy
            if 0<=nx<2000 and 0<=ny<2000:
                ans |= self.findPath(nx,ny,len+1)

        return ans
# @lc code=end

sol = Solution()
print(sol.escapeGhosts([[5,0],[-10,-2],[0,-5],[-2,-2],[-7,1]],[7,7]))