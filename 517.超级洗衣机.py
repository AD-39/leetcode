#
# @lc app=leetcode.cn id=517 lang=python3
#
# [517] 超级洗衣机
#

# @lc code=start
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        if sum(machines) % len(machines) != 0:
            return -1
        
        target = sum(machines) // len(machines)

        ans = 0
        tmp = 0
        for num in machines:
            num -= target
            tmp += num
            ans = max([ans, abs(tmp), num])

        return ans

# @lc code=end

