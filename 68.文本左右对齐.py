#
# @lc app=leetcode.cn id=68 lang=python3
#
# [68] 文本左右对齐
#

# @lc code=start
from typing import *
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        words_lines = [[]]
        now_len = 0
        for word in words:
            if now_len + len(words_lines[-1]) + len(word) > maxWidth:
                words_lines.append([word])
                now_len = len(word)
            else:
                words_lines[-1].append(word)
                now_len += len(word)
        
        ans = []
        for i, line in enumerate(words_lines):
            if i == len(words_lines) - 1:
                final_text = ' '.join(line)
                final_text += ' ' * (maxWidth - len(final_text))
                ans.append(final_text)
                return ans
            space_len = maxWidth - len(''.join(line))
            pos = len(line) - 1
            if pos == 0:
                ans.append(line[0] + ' '*space_len)
            else:
                base = space_len // pos
                remain = space_len % pos
                for i in range(remain):
                    line[i] += ' '
                ans.append((' '*base).join(line))
            
# @lc code=end
sol = Solution()
sol.fullJustify(["This", "is", "an", "example", "of", "text", "justification."]
,16)

