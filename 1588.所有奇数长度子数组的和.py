#
# @lc app=leetcode.cn id=1588 lang=python3
#
# [1588] 所有奇数长度子数组的和
#

# @lc code=start
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        t = n//2

        cnt = [0]*n
        d = n
        while d > 0:
            cnt[i] = cnt[n-1-i] = d

        ans = 0
        for i in range(n):
            ans += arr[i]*cnt[i]
        return ans + sum(arr)


# @lc code=end

