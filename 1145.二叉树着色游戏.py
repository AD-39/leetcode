#
# @lc app=leetcode.cn id=1145 lang=python3
#
# [1145] 二叉树着色游戏
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        def cnt_point(node):
            if not node:
                return 0
            cnt = 0
            x_child = [node]
            while x_child:
                cur = x_child.pop(0)
                cnt += 1
                if cur.left:
                    x_child.append(cur.left)
                if cur.right:
                    x_child.append(cur.right)
            return cnt
        
        stack = [root]
        while stack:
            now = stack.pop(0)
            if now.val == x:
                left_cnt = cnt_point(now.left)
                right_cnt = cnt_point(now.right)
                father_cnt = n - left_cnt - right_cnt - 1

                return father_cnt > n - father_cnt or\
                    left_cnt > n - left_cnt or\
                    right_cnt > n - right_cnt 
            else:
                if now.left:
                    stack.append(now.left)
                if now.right:
                    stack.append(now.right)

# @lc code=end

