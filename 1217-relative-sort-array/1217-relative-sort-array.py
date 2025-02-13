class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ct=Counter(arr1)
        ans=[]
        for n in arr2:
            while ct[n]!=0:
                ans.append(n)
                ct[n]-=1
                if ct[n]==0:
                    del ct[n]
        arr=[]
        for n,ct in ct.items():
            while ct!=0:
                arr.append(n)
                ct-=1
        arr.sort()
                
        return ans+arr


