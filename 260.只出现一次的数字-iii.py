#
# @lc app=leetcode.cn id=260 lang=python3
#
# [260] 只出现一次的数字 III
#

# @lc code=start
from typing import *
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num

        #依据sign位分组
        a = b = 0
        #sign为xor结果中倒数第一个1的位置
        sign = ((xor ^ (xor - 1)) + 1) >> 1
        for num in nums:
            #该位为1则为a组，该位为0则为b组
            if sign & num == 0:
                a ^= num
            else:
                b ^= num

        return [a, b]
# @lc code=end
sol = Solution()
sol.singleNumber([1,2,1,3,2,5])
