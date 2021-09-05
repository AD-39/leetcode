#
# @lc app=leetcode.cn id=470 lang=python3
#
# [470] 用 Rand7() 实现 Rand10()
#

# @lc code=start
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        ans = 0
        for i in range(10):
            ans += rand7()+i*7
        return ans%10 + 1
        # 上文非正确解法
        # 两个rand7出1-49然后选择等概率的数字
        

        
# @lc code=end

