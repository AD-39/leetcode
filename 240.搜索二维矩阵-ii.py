#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
from typing import *
from bisect import bisect_left as bl
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])

        ###########伞兵二分O(nlogn)
        # x, y = bl([line[-1] for line in matrix], target), bl(matrix[-1], target)

        # for i in range(x, n):
        #     j = bl(matrix[i][y:m], target)
        #     if y + j != m and matrix[i][y + j] == target:
        #         return True
        # return False

        ##########高贵的O(m+n)
        i, j = n - 1, 0 
        while True:
            if matrix[i][j] == target:
                return True

            while i >= 0 and matrix[i][j] > target:
                i -= 1
            if i < 0:
                return False

            while j < m and matrix[i][j] < target:
                j += 1
            if j == m:
                return False
        

# @lc code=end

sol = Solution()
sol.searchMatrix([[-1,3]],
3
)