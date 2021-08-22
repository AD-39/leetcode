#
# @lc app=leetcode.cn id=173 lang=python3
#
# [173] 二叉搜索树迭代器
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):

        def inorder(root):
            if root == None:
                return []
            return inorder(root.left)+[root.val]+inorder(root.right)
        self.stack = inorder(root)
        self.p = -1
        self.len = len(self.stack)


    def next(self) -> int:
        self.p += 1
        return self.stack[self.p]


    def hasNext(self) -> bool:
        return self.p != self.len - 1



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

