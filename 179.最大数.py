#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#

# @lc code=start
import functools
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(item) for item in nums]
        
        def my_compar(x, y):
            if x+y < y+x:
                return 1
            else:
                return -1

        ans = ''.join(sorted(nums, 
            key=functools.cmp_to_key(my_compar)))
        
        #前导零
        if ans[0] == '0':
            return '0'
        else:
            return ans

# @lc code=end

