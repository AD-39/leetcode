# @before-stub-for-debug-begin
from python3problem212 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#

# @lc code=start
class Trie:
    def __init__(self) -> None:
        self.children = DefaultDict(Trie)
        self.word = ''

    def insert(self, word):
        cur = self
        for ch in word:
            cur = cur.children[ch]
        cur.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        for word in words:
            root.insert(word)
        
        dir = [[0,1],[0,-1],[1,0],[-1,0]]
        n = len(board)
        m = len(board[0])
        vis = [[0]*m for _ in range(n)]

        def dfs(x, y, now):
            if now.word:
                ans.add(now.word)

            vis[x][y] = 1
            for dx, dy in dir:
                nx = x + dx
                ny = y + dy
                if 0<=nx<n and 0<=ny<m and\
                    not vis[nx][ny] and board[nx][ny] in now.children:
                    dfs(nx, ny, now.children[board[nx][ny]])
            vis[x][y] = 0
            return 
        
        ans = set()
        for i in range(n):
            for j in range(m):
                if board[i][j] in root.children:
                    dfs(i,j,root.children[board[i][j]])
        return list(ans)


# @lc code=end


