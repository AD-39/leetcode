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
        #########平平无奇的双指针
        # def check(a, b):
        #     i = 0
        #     la = len(a)
        #     for ch in b:
        #         while i != la and a[i] != ch:
        #             i += 1
        #         if i != la:
        #             i += 1
        #         else:
        #             return False
        #     return True

        #######高端大气上档次的dp
        ls = len(s)
        s_next_word = [[-1]*26 for _ in range(ls+1)]
        for i in range(1, ls+1):
            ch = s[i-1]
            for j in range(i-1, -1, -1):
                if s_next_word[j][ord(ch) - ord('a')] == -1:
                    s_next_word[j][ord(ch) - ord('a')] = i
                else:
                    break

        def check(b):
            p = 0
            for ch in b:
                p = s_next_word[p][ord(ch) - ord('a')]
                if p == -1:
                    return False
            return True
        ans = ''
        for word in dictionary:
            if len(word) >= len(ans) and check(word):
                ans = min(ans, word) if len(word) == len(ans) else word 
        return ans

# @lc code=end

