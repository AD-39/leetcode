# @before-stub-for-debug-begin
from python3problem524 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=524 lang=python3
#
# [524] 通过删除字母匹配到字典里最长单词
#

# @lc code=start
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def check(a, b):
            i = 0
            la = len(a)
            for ch in b:
                while i != la and a[i] != ch:
                    i += 1
                if i != la:
                    i += 1
                else:
                    return False
            return True
        
        ans = ''
        for word in dictionary:
            if len(word) >= len(ans) and check(s, word):
                ans = min(ans, word) if len(word) == len(ans) else word 
        return ans

# @lc code=end

