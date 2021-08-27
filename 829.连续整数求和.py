#
# @lc app=leetcode.cn id=829 lang=python3
#
# [829] 连续整数求和
#

# @lc code=start
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        ans = 0
        cnt = 0
        sum = 0
        while sum + cnt <= n:
            cnt += 1
            sum += cnt
            if (n - sum) % cnt == 0:
                ans += 1
        return ans
# @lc code=end

sol = Solution()
print(sol.consecutiveNumbersSum(100))
