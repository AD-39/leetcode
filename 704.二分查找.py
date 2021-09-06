#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start
import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        p = bisect.bisect_left(nums, target)
        return p if p < len(nums) and nums[p] == target else -1
# @lc code=end

