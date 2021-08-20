#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return 0
        if length == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1

        mid = length//2
        if nums[mid-1] > nums[mid]:
            return self.findPeakElement(nums[:mid])
        elif nums[mid] < nums[mid+1]:
            return mid + self.findPeakElement(nums[mid:])
        else:
            return mid

        
# @lc code=end

