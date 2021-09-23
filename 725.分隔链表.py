# @before-stub-for-debug-begin
from python3problem725 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=725 lang=python3
#
# [725] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        ans = []

        length = 0
        p = head
        while p:
            p = p.next
            length += 1
        
        per_len = length // k
        remain = length % k

        for i in range(k):
            now_len = per_len + 1 if i < remain else per_len
            p = head
            for _ in range(1, now_len):
                p = p.next

            ans.append(head)
            if p:
                head = p.next
                p.next = None
        return ans
# @lc code=end

