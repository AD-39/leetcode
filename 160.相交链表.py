# @before-stub-for-debug-begin
from python3problem160 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ########平平无奇的hashmap
        # nodeA = []
        # nodeB = []
        # while headA:
        #     nodeA.append(headA)
        #     headA = headA.next
        # while headB:
        #     nodeB.append(headB)
        #     headB = headB.next

        # i = 1
        # while i <= min(len(nodeA), len(nodeB)) and nodeA[-i] == nodeB[-i]:
        #     i += 1
        # if i == 1:
        #     return None
        # return nodeA[-i+1]

        ######高端大气的双指针
        #链接链表A首尾
        p = headA
        while p.next:
            p = p.next
        p.next = headA
        #双指针
        slow, fast = 2, 1
        while slow and fast and slow != fast:
            if slow == 2:
                slow, fast = headB, headB
            slow = slow.next
            fast = fast.next.next if fast.next else fast.next
        #无交点
        if not slow or not fast:
            p.next = None
            return None
        slow = headB
        while slow != fast:
            slow = slow.next
            fast = fast.next
        p.next = None
        return slow
        

        
# @lc code=end

