class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        # counter1=Counter(s)
        # counter2=Counter(t)
        # return counter1==counter2
        arr=[0]*26
        
        for n in s:
            arr[ord(n)-ord("a")]+=1
        for n in t:
            arr[ord(n)-ord("a")]-=1
        return max(arr)==0


