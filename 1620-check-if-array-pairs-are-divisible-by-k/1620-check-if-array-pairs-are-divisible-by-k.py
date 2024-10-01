class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        dic=defaultdict(int)
        for num in arr:
            dic[(num+k)%k]=1+dic.get((num+k)%k,0)
        if dic[0]%2==1:
            return False
        for i in range(1,k):
            if dic[i]!=dic[k-i]:
                return False
        return True
        
        