class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix=[0]*(len(nums))
        prefix[0]=nums[0]
        
        for i in range(1,len(nums)):
            prefix[i]=nums[i]+prefix[i-1]

        def  binary(arr, target):
            l=0
            r=len(arr)-1
            while l<=r:
                m=l+(r-l)//2
                if arr[m]==target:
                    return m
                elif arr[m]<target:
                    l=m+1
                else:
                    r=m-1
            return l
        n=len(nums)

        ans=[]
        for q in queries:
            summ=0
            index=binary(nums, q)
            if index==0:
                summ=prefix[-1]-(n*q)
            else:
                summ=(index*q)-(prefix[index-1])
                summ+=(prefix[-1]-prefix[index-1]-((n-index) *q))

            ans.append(summ)
        return ans

            