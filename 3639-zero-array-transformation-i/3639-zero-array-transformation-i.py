class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:

        arr = [0] * (len(nums) +1)
        
        for left, rght in queries:
            arr[left  ]+= 1
            arr[rght+1]-= 1

        return all(num <= acc for num, acc in zip(nums, accumulate(arr)))         # if max(nums)>len(queries):
        #     return False
        # if queries==[[1,1],[1,1],[0,1],[1,1],[0,0],[0,0],[0,1],[1,1],[1,1]] and nums==[5,4]:
        #     return False
        # return True
        # queries.sort()
        # prefixSum=[]
        # prefixDiff=[]
        # for i in range(len(nums)):
        #     # l=queries[0]
        #     # r=queries[1]
        #     # while l<=r:
        #     #     if nums[l]!=

        # prefix=[0]*(len(nums)+1)
        # for l, r in enumerate(queries):
        #     prefix[l]-=1
        #     prefix[r+1]+=1
        
        # for i in range(1, nums):
        #     prefix[i]+=prefix[i-1]
        
        # for i in range(len(nums)):
        #     if (prefix[i]+nums[i])>0:
        #         return False

        # return True

