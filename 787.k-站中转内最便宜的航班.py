from typing import *
#
# @lc app=leetcode.cn id=787 lang=python3
#
# [787] K 站中转内最便宜的航班
#

# @lc code=start
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        price = [[float('inf') for i in range(n)] for j in range(n)]
        for fp, tp, pr in flights:
            price[fp][tp] = pr
        
        #now, len, price
        stack = [[src, 0, 0]]

        dis = [float('inf') for i in range(n)]

        ans = float('inf')
        while stack:
            now, len, pr = stack.pop(0)
            #到达终点
            if now == dst:
                ans = min(ans, pr)
                continue
            #中转达最大次数/价格超当前最优解
            if len > k or pr > ans:
                continue
            #当前点限制剪枝
            if pr >= dis[now]:
                continue
            dis[now] = pr


            for i in range(n):
                if price[now][i] != float('inf'):
                    stack.append([i, len+1, pr+price[now][i]])



        return ans if ans != float('inf') else -1




# @lc code=end

sol = Solution()
print(sol.findCheapestPrice(3,
[[0,1,100],[1,2,100],[0,2,500]],
0,
2,
1))

