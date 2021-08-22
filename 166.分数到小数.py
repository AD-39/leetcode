#
# @lc app=leetcode.cn id=166 lang=python3
#
# [166] 分数到小数
#

# @lc code=start
import decimal as dec
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator==0:
            return str(numerator//denominator)

        dec.getcontext().prec = 2000


        ans = str(dec.Decimal(numerator)/dec.Decimal(denominator))
        start = ans.find('.')

        #循环节长度
        K = 1
        remain = 10
        while True:
            if remain == 0:
                return ans[:start+K]
            if remain % denominator == 1:
                break
            else:
                remain = (remain % denominator) * 10
            K += 1
        
        for i in range(start+1, len(ans)):
            if ans[i:i+K] == ans[i+K:i+2*K]:
                return f'{ans[:i]}({ans[i:i+K]})'

# @lc code=end

