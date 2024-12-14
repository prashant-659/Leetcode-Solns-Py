class Solution:
    def toHex(self, num: int) -> str:
        s, res, num = '0123456789abcdef', '', num & 0xFFFFFFFF        
        while num:
            res += s[num % 16]
            num >>= 4
        
        return res[::-1] or '0'