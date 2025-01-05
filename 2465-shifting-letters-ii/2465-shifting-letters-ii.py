class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix=[0]*(len(s)+1)

        for start, end, dir in shifts:
            prefix[start]+=1 if dir else -1
            prefix[end+1]-=1 if dir else -1
        for i in range(1, len(prefix)):
            prefix[i]+=prefix[i-1]


        res=[]
        for i, cur in enumerate(s):
            new=chr(ord("a")+((ord(cur)-ord("a")+prefix[i])%26))
            res.append(new)
        return "".join(res)
            