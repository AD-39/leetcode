# @before-stub-for-debug-begin
from python3problem210 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] 课程表 II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre = DefaultDict(list)
        for a, b in prerequisites:
            pre[a].append(b)
        
        remain = set(range(numCourses))
        solved = set()
        ans = []
        while remain:
            for item in remain:
                flag = True
                for pre_c in pre[item]:
                    if pre_c not in solved:
                        flag = False
                        break
                if flag:
                    ans.append(item)
                    solved.add(item)
            pre_remain = remain.copy()
            remain -= solved
            if not (pre_remain - remain):
                return []
        return ans
# @lc code=end