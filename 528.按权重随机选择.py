#
# @lc app=leetcode.cn id=528 lang=python3
#
# [528] 按权重随机选择
#

# @lc code=start
import random
class Solution:

    def __init__(self, w: List[int]):
        self.w = [[0, w[0]]]
        self.sum = sum(w)
        for i in range(1, len(w)):
            self.w.append([self.w[-1][1], self.w[-1][1] + w[i]])



    def pickIndex(self) -> int:
        p = random.randint(1, self.sum)

        l, r = 0, len(self.w) - 1
        while l < r:
            mid = (l+r)//2
            a, b = self.w[mid]
            if a <= p < b:
                return mid
            elif a > p:
                r = mid - 1
            else:
                l = mid + 1
        
        return r





# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end

