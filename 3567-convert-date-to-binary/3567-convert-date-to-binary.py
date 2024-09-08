class Solution:
    def convertDateToBinary(self, date: str) -> str:
        y,m,d=map(int, date.split("-"))
        bi_y=bin(y)[2:]
        bi_m=bin(m)[2:]
        bi_d=bin(d)[2:]
        return bi_y+"-"+bi_m+"-"+bi_d