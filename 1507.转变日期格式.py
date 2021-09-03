#
# @lc app=leetcode.cn id=1507 lang=python3
#
# [1507] 转变日期格式
#

# @lc code=start
class Solution:
    def reformatDate(self, date: str) -> str:
        month_dict = {
            "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", 
            "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
        }

        day, month, year = date.split()
        
        month = month_dict[month]

        day = day[:-2].zfill(2)
        return '-'.join([year, month, day])

# @lc code=end

