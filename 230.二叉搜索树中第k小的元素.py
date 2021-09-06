#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        #########中序遍历
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()

            if k == 1:
                return root.val
            k -= 1
            
            root = root.right

            

        ##########没哈卵用的方法，但是是自己写的，懒得删了
        # def cnt(node, k):
        #     node_sum = 0

        #     if node.left:
        #         flag, ans = cnt(node.left, k)
        #         if flag:
        #             return flag, ans
        #         else:
        #             node_sum += ans

        #     if k - node_sum == 1:
        #         return True, node.val
        #     node_sum += 1

        #     if node.right:
        #         flag, ans = cnt(node.right, k - node_sum)
        #         if flag:
        #             return flag, ans
        #         else:
        #             node_sum += ans

        #     return False, node_sum

        # flag, ans = cnt(root, k)
        # return ans         
        
# @lc code=end

