#
# @lc app=leetcode.cn id=165 lang=python3
#
# [165] 比较版本号
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        num_list_1 = [int(i) for i in version1.split('.')]
        num_list_2 = [int(i) for i in version2.split('.')]

        length = max(len(num_list_1), len(num_list_2))

        num_list_1 += [0] * (length - len(num_list_1))
        num_list_2 += [0] * (length - len(num_list_2))

        for i in range(length):
            if num_list_1[i] > num_list_2[i]:
                return 1
            elif num_list_1[i] < num_list_2[i]:
                return -1

        return 0
# @lc code=end

