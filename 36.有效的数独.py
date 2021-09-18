# @before-stub-for-debug-begin
from python3problem36 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        for line in board:
            num_save = []
            for ch in line:
                if ch.isdigit() and ch in num_save:
                    return False
                else:
                    num_save.append(ch)
        
        for i in range(n):
            num_save = []
            for j in range(n):
                ch = board[j][i]
                if ch.isdigit() and ch in num_save:
                    return False
                else:
                    num_save.append(ch)
        
        for i in range(0,n,3):
            for j in range(0,n,3):
                num_save = []
                for x in range(i,i+3):
                    for y in range(j,j+3):
                        ch = board[x][y]
                        if ch.isdigit() and ch in num_save:
                            return False
                        else:
                            num_save.append(ch)
        
        return True

# @lc code=end

