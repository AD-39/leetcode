#
# @lc app=leetcode.cn id=600 lang=python3
#
# [600] 不含连续1的非负整数
#

# @lc code=start
class Solution:
    def findIntegers(self, n: int) -> int:
        cnt = [1] * 32

        for i in range(1, 32):
            cnt[i] = cnt[i-1] + cnt[i-2]
        
        p = 0
        ans = 0
        pre = 0
        for i in range(31, -1, -1):
            cur = (n >> i) & 1
            if cur == 1:
                ans += cnt[i]
            if pre == 1 and cur == 1:
                break

            pre = cur

            if i == 0:
                ans += 1


        return ans
# @lc code=end
sol = Solution()
sol.findIntegers(1000)

