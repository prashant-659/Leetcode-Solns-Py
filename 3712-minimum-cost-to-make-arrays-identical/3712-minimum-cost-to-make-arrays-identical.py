class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        ans2=0
        for i in range(len(arr)):
            ans2+=abs(arr[i]-brr[i])

        arr.sort()
        brr.sort()
        ans1=k

        for i in range(len(arr)):
            ans1+=abs(arr[i]-brr[i])
        return min(ans1, ans2)
        
