#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        c, r = 0, 0
        s = '#'.join([''] + [ch for ch in s] + [''])

        n = len(s)
        p = [0] * n


        def get_len(s, l, r):
            ans = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return (r-l-2)//2

        pre_i = 0
        for i in range(n):
            if i >= r:
                p[i] = get_len(s, i, i)
                r = i + p[i]
                pre_i = i
            else:
                i_mirror = 2*pre_i - i
                if r-i > p[i_mirror]:
                    p[i] = p[i_mirror]
                else:
                    p[i] = get_len(s, 2*i-r, r)
                    r = i + p[i]
                    pre_i = i
        
        max_len, start = 0, 0
        for i in range(n):
            if p[i] > max_len:
                max_len = p[i]
                start = i - max_len
        return ''.join(s[start:start+1+2*max_len].split('#'))

# @lc code=end
sol = Solution()
print(sol.longestPalindrome("ccc"))

