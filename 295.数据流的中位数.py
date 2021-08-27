#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#

# @lc code=start
import collections
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.num_set = []


    def addNum(self, num: int) -> None:
        p, q = 0, len(self.num_set)

        if q == 0:
            self.num_set.append(num)
            return
        elif q == 1:
            self.num_set.append(num)
            self.num_set.sort()
            return 

        mid = (p + q)//2
        while p + 1 < q:
            if self.num_set[mid] > num:
                q = mid
                mid = (p + q)//2
            else:
                p = mid
                mid = (p + q)//2
        
        if num > self.num_set[p]:
            self.num_set.insert(q, num)
        else:
            self.num_set.insert(p, num)



    def findMedian(self) -> float:
        n = len(self.num_set)
        if n % 2 == 0:
            return (self.num_set[n//2 - 1] + self.num_set[n//2])/2
        else:
            return self.num_set[n//2]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

sol = MedianFinder()
sol.addNum(-1)
sol.addNum(-2)
sol.findMedian()
sol.addNum(-3)
sol.findMedian()

