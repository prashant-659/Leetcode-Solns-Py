class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        ct=defaultdict(int)
        for i in dominoes:
            ct[tuple(sorted(i))]=1+ct.get(tuple(sorted(i)),0)
        c=0
        for n in ct.values():
            s=n*(n-1)//2
            c+=s
        return c