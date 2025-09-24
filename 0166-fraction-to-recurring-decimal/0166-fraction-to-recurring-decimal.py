class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        num, denom = numerator, denominator
        if num == 0:
            return '0'
        res = []
        if (num > 0) != (denom > 0):
            res.append('-')
        num, denom = abs(num), abs(denom)
        quo, rem = divmod(num, denom)
        res.append(str(quo))
        if rem == 0:
            return ''.join(res)
        res.append('.')
        
        seen = {}
        while rem:
            if rem in seen:
                ind = seen[rem]
                return ''.join(res[:ind]) + '(' + ''.join(res[ind:]) + ')'
            seen[rem] = len(res)
            quo, rem = divmod(rem * 10, denom)
            res.append(str(quo))
        return ''.join(res)