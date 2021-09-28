# @before-stub-for-debug-begin
from python3problem437 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.target = targetSum
        return self.my_path_sum(root, [])


    def my_path_sum(self, now, pre):
        pre = pre.copy()
        if not now:
            return 0
        
        for i in range(len(pre)):
            pre[i] += now.val
        
        pre.append(now.val)
        return pre.count(self.target) + \
            self.my_path_sum(now.left, pre) +\
            self.my_path_sum(now.right, pre)
# @lc code=end

