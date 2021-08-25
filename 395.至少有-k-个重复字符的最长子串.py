#
# @lc app=leetcode.cn id=395 lang=python3
#
# [395] 至少有 K 个重复字符的最长子串
#

# @lc code=start
import collections
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        ans = 0

        alp_position = collections.defaultdict(list)
        for i, ch in enumerate(s):
            alp_position[ch].append(i)
        
        pos_list = []
        for value in alp_position.values():
            if len(value) < k:
                pos_list += value

        if not pos_list:
            return len(s)
        
        pos_list.append(len(s))
        pos_list.sort()

        pre_p = 0
        for p in pos_list:
            ans = max(ans, self.longestSubstring(s[pre_p:p], k))
            pre_p = p+1

        return ans


# @lc code=end

