#
# @lc app=leetcode.cn id=229 lang=python3
#
# [229] 求众数 II
#

# @lc code=start
from typing import *
import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ########counter
        # n = len(nums)
        # cnter = collections.Counter(nums)

        # ans = []
        # for key, value in cnter.items():
        #     if value > n//3:
        #         ans.append(key)
        # return ans

        #######摩尔计数
        num1, cnt1 = nums[0], 0
        num2, cnt2 = nums[0], 0
        n = len(nums)
        
        for num in nums:
            if num1 == num:
                cnt1 += 1
            elif num2 == num:
                cnt2 += 1
            else:
                if cnt1 == 0:
                    num1, cnt1 = num, 1
                elif cnt2 == 0:
                    num2, cnt2 = num, 1
                else:
                    cnt1 -= 1
                    cnt2 -= 1

        ans = []
        if cnt1 and nums.count(num1) > n//3:
            ans.append(num1)
        if cnt2 and nums.count(num2) > n//3:
            ans.append(num2)

        return ans


# @lc code=end
sol = Solution()
sol.majorityElement([3,2,3])
