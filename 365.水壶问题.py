# @before-stub-for-debug-begin
from python3problem365 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=365 lang=python3
#
# [365] 水壶问题
#

# @lc code=start
import math
class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        a, b, c = jug1Capacity, jug2Capacity, targetCapacity

        if (a == 0 or b == 0) and c != a+b:
            return False
        if c > a+b:
            return False
            

        return c % math.gcd(a,b) == 0


# @lc code=end

