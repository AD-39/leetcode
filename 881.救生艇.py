#
# @lc app=leetcode.cn id=881 lang=python3
#
# [881] 救生艇
#

# @lc code=start
from typing import *
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        p, q = 0, len(people) - 1

        ans = 0
        while p <= q:
            if people[p] + people[q] <= limit:
                p += 1
            q -= 1
            ans += 1

        return ans

# @lc code=end
sol = Solution()
sol.numRescueBoats([2,4],
5)
