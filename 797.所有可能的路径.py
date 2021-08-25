#
# @lc app=leetcode.cn id=797 lang=python3
#
# [797] 所有可能的路径
#

# @lc code=start
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.graph = graph
        self.n = len(graph)
        self.vis = [False] * self.n

        return self.dfs(0)
    
    def dfs(self, now):
        if now == self.n - 1:
            return [[self.n - 1]]

        ans = []
        for nxt in self.graph[now]:
            for line in self.dfs(nxt):
                ans.append([now]+line)
        return ans
# @lc code=end

