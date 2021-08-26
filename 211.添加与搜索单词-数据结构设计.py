#
# @lc app=leetcode.cn id=211 lang=python3
#
# [211] 添加与搜索单词 - 数据结构设计
#

# @lc code=start
from typing import *
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}


    def addWord(self, word: str) -> None:
        self.my_add(self.root, word)

    def my_add(self, root_node, s):
        if not s:
            root_node['-1'] = {}
            return
        if s[0] not in root_node:
            root_node[s[0]] = {}
        self.my_add(root_node[s[0]], s[1:])

    def search(self, word: str) -> bool:
        return self.my_search(self.root, word)

    def my_search(self, root_node, s):
        if not s:
            return '-1' in root_node

        nxt = []
        if s[0] == '.':
            nxt = root_node.keys()
        elif s[0] in root_node:
            nxt .append(s[0])

        ans = False
        for item in nxt:
            ans |= self.my_search(root_node[item], s[1:])

        return ans

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

sol = WordDictionary()
print(sol.addWord('add'))
print(sol.search('a'))