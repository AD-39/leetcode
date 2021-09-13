#
# @lc app=leetcode.cn id=289 lang=python3
#
# [289] 生命游戏
#

# @lc code=start
from typing import *
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        pre_board = [line.copy() for line in board]
        n = len(board)
        m = len(board[0])

        dir = [[0,1],[0,-1],[1,0],[1,1],[1,-1],[-1,1],[-1,0],[-1,-1]]
        for i in range(n):
            for j in range(m):
                cnt = 0
                for dx, dy in dir:
                    nx, ny = i+dx, j+dy
                    if 0<=nx<n and 0<=ny<m and pre_board[nx][ny]:
                        cnt += 1
                board[i][j] = 1 if cnt == 3 or cnt == 2 and pre_board[i][j] else 0

# @lc code=end
sol = Solution()
sol.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])

