#
# @lc app=leetcode.cn id=299 lang=python3
#
# [299] 猜数字游戏
#

# @lc code=start
import collections
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        n = len(secret)
        alpha = collections.defaultdict(int)
        beta = collections.defaultdict(int)
        for i in range(n):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                alpha[secret[i]] += 1
                beta[guess[i]] += 1

        for key in alpha.keys():
            cows += min(alpha[key], beta[key])

        return f'{bulls}A{cows}B'
# @lc code=end

