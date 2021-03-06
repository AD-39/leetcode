#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.my_insert(self.root, word)
        
    def my_insert(self, root_node, word):
        if word:
            if word[0] not in root_node.keys():
                root_node[word[0]] = {}
            self.my_insert(root_node[word[0]], word[1:])
        else:
            root_node['-1'] = {}



    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """

        return self.my_search(self.root, word)

    def my_search(self, root_node, word):
        if not word:
            return '-1' in root_node
        if word[0] not in root_node:
            return False

        return self.my_search(root_node[word[0]], word[1:])

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.my_startsWith(self.root, prefix)

    def my_startsWith(self, root_node, word):
        if not word:
            return True
        if word[0] not in root_node:
            return False

        return self.my_startsWith(root_node[word[0]], word[1:])





# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

trie = Trie()
trie.insert('apple')
trie.search('applea')

