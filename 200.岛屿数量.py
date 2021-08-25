#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
from typing import *
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        self.grid = grid
        self.n = len(grid)
        self.m = len(grid[0])

        ans = 0
        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j] == '1':
                    ans += 1
                    self.render(i,j)
        
        return ans
    
    def render(self, x, y):
        dis = [[0,1],[0,-1],[1,0],[-1,0]]
        self.grid[x][y] = '0'
        for dx, dy in dis:
            nx = x + dx
            ny = y + dy
            if 0<=nx<self.n and 0<=ny<self.m\
                 and self.grid[nx][ny] == '1':
                self.render(nx, ny)
# @lc code=end

sol = Solution()
print(sol.numIslands([["1"],["1"]]
))