#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start
from typing import *
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        pre_sum = [[0]*m for i in range(n)]

        ################前缀和 mnmin(m,n)
        # ans = 0
        # for i in range(n):
        #     for j in range(m):
        #         if i == 0 and j == 0:
        #             pre_sum[i][j] = int(matrix[i][j])
        #         elif i == 0:
        #             pre_sum[i][j] = int(matrix[i][j]) + pre_sum[i][j-1]
        #         elif j == 0:
        #             pre_sum[i][j] = int(matrix[i][j]) + pre_sum[i-1][j]
        #         else:
        #             pre_sum[i][j] = int(matrix[i][j]) + pre_sum[i-1][j] +\
        #                 pre_sum[i][j-1] - pre_sum[i-1][j-1]
                
        #         for k in range(1,min(i,j)+2):
        #             a, b, c, d = i-k, i, j-k, j
        #             if a < -1 or c < -1:
        #                 continue
        #             elif a == -1 and c == -1:
        #                 s = pre_sum[b][d]
        #             elif a == -1:
        #                 s = pre_sum[b][d] - pre_sum[b][c]
        #             elif c == -1:
        #                 s = pre_sum[b][d] - pre_sum[a][d]
        #             else:
        #                 s = pre_sum[b][d] - pre_sum[b][c] - \
        #                     pre_sum[a][d] + pre_sum[a][c]

        #             if s == k**2:
        #                 ans = max(ans,s)
        # return ans

        #############动态规划 mn
        ans = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '0':
                    continue
                if i == 0 or j == 0:
                    pre_sum[i][j] = 1
                else:
                    pre_sum[i][j] = 1 + min([pre_sum[i-1][j-1],
                        pre_sum[i-1][j], pre_sum[i][j-1]])
                ans = max(ans, pre_sum[i][j])
        return ans**2
# @lc code=end
sol = Solution()
sol.maximalSquare(
[["0","1"]]
)

