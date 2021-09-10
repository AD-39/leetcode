#
# @lc app=leetcode.cn id=662 lang=python3
#
# [662] 二叉树最大宽度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        ans = 0
        pre_line = []
        now_line = [(1, root)]
        line_ans = 1
        while line_ans:
            line_ans = max_line_ans = 0
            pre_line = now_line.copy()
            now_line = []
            for num, node in pre_line:
                if not line_ans and node:
                        line_ans = 1
                        max_line_ans = max(max_line_ans, line_ans)
                        now_line.append((1, node.left))
                        now_line.append((1, node.right))
                elif line_ans:
                    line_ans += num
                    if node:
                        max_line_ans = max(max_line_ans, line_ans)
                        now_line.append((1, node.left))
                        now_line.append((1, node.right))
                    else:
                        now_line.append((num*2, None))

            ans = max(ans, max_line_ans)
        return ans

# @lc code=end

