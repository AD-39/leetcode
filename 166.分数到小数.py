#
# @lc app=leetcode.cn id=166 lang=python3
#
# [166] 分数到小数
#

# @lc code=start
import decimal as dec
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        #可整除
        if numerator % denominator==0:
            return str(numerator//denominator)

        #判断符号
        sign = ''
        if numerator < 0 and denominator > 0 or\
            numerator > 0 and denominator < 0:
            sign = '-'
        numerator = abs(numerator)
        denominator = abs(denominator)
        

        front = str(numerator//denominator)+'.'
        ans = ''
        remain = numerator % denominator
        remain_save = {}
        p = 0

        while remain not in remain_save:
            remain_save[remain] = p
            remain *= 10
            while remain < denominator:
                remain *= 10
                ans += '0'
                p += 1
            
            ans += str(remain//denominator)
            p += 1
            remain = remain % denominator
            #不循环
            if remain == 0:
                return sign + front + ans

        #循环加括号
        p = remain_save[remain]
        return sign + front + ans[:p] + '(' + ans[p:] + ')' 


# @lc code=end

