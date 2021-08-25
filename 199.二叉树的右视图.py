#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        #root is null
        if not root:
            return []

        stack = [[root, 0]]
        ans = []

        while stack:
            now, length = stack.pop(0)
            if len(ans) == length:
                ans.append(now.val)
            else:
                ans[length] = now.val
            #judge childnodes not null
            if now.left:
                stack.append([now.left, length+1])
            if now.right:
                stack.append([now.right, length+1])

        return ans

# @lc code=end

