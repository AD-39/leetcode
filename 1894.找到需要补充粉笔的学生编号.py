#
# @lc app=leetcode.cn id=1894 lang=python3
#
# [1894] 找到需要补充粉笔的学生编号
#

# @lc code=start
import bisect
import itertools
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)
        accu = list(itertools.accumulate(chalk))
        return bisect.bisect_right(accu, k)
# @lc code=end

