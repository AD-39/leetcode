#
# @lc app=leetcode.cn id=1588 lang=python3
#
# [1588] 所有奇数长度子数组的和
#

# @lc code=start
from typing import *
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ################O(n^2)
        # n = len(arr)
        # t = n//2 + 1

        # cnt = [[0]*t for i in range(n)]

        # for i in range(n):
        #     #行限制
        #     row = min(i+1, n-i)
        #     for j in range(t):
        #         #列限制
        #         col = min(1+2*j, n-2*j)
        #         cnt[i][j] = min(row, col)

        # ans = 0
        # for i in range(n):
        #     ans += arr[i]*sum(cnt[i])
        # return ans

        ##############O(n)
        n = len(arr)
        ans = 0
        for i in range(n):
            leftCnt, rightCnt = i, n - i - 1
            #计算左右两边距离为奇数/偶数的下标数量（0算作偶数）
            lo, le = (leftCnt+1)//2, leftCnt//2+1
            ro, re = (rightCnt+1)//2, rightCnt//2+1
            ans += arr[i] * (lo*ro + le*re)
        return ans

# @lc code=end
sol = Solution()
sol.sumOddLengthSubarrays([1,4,2,5,3])


