#
# @lc app=leetcode.cn id=430 lang=python3
#
# [430] 扁平化多级双向链表
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def flat(now):
            p = now

            while p:
                nxt = p.next
                if p.child:
                    last = flat(p.child)

                    p.next = p.child
                    p.child.prev = p
                    p.child = None

                    if not nxt:
                        l = last
                    else:
                        last.next = nxt
                        nxt.prev = last
                elif not nxt:
                    l = p
                p = nxt

            return l
                
        if head:
            flat(head)
        return head

        
# @lc code=end

