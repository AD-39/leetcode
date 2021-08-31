#
# @lc app=leetcode.cn id=220 lang=python3
#
# [220] 存在重复元素 III
#
import bisect
from typing import *
# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        ################二分插入+二分查找
        # n = len(nums)
        # sorted_list = []

        # for i in range(n):
        #     if i - k - 1 >= 0:
        #         sorted_list.remove(nums[i-k-1])

        #     p = bisect.bisect_left(sorted_list, nums[i] - t)
        #     if p < len(sorted_list) and sorted_list[p] <= nums[i] + t:
        #         return True

        #     q = bisect.bisect_left(sorted_list, nums[i])
        #     sorted_list.insert(q, nums[i])            
        # return False

        #############桶排
        def get_idx(x, t):
            return x//(t+1)
        
        n = len(nums)
        bucket_dict = {}
        for i in range(n):
            if i - k - 1 >= 0:
                bucket_dict.pop(get_idx(nums[i-k-1], t))

            idx = get_idx(nums[i], t)
            if idx in bucket_dict:
                return True
            if idx + 1 in bucket_dict and \
                abs(nums[i] - bucket_dict[idx + 1]) <= t:
                return True
            if idx - 1 in bucket_dict and \
                abs(nums[i] - bucket_dict[idx - 1]) <= t:
                return True

            bucket_dict[idx] = nums[i]
        return False



# @lc code=end
sol = Solution()
print(sol.containsNearbyAlmostDuplicate([1,5,9,1,5,9],
2,
3)
)
