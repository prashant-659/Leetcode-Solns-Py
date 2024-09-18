class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        #not a solution yet I CODED IT.
        # num=[]
        
        # string=""
        # for n in nums:   
        #     if n > 9:
        #         while n:
        #             val=n%10
        #             num.append(val)
        #             n=n//10
        #     else:
        #         num.append(n)
        # res=""
        # num.sort()
        # for i in range(len(num)-1,-1,-1):
        #     res=res+str(num[i])
        # return res

        if max(nums)==0:
            return "0"
        for i , n in enumerate(nums):
            nums[i]=str(n)
        def compare(n1,n2):
            if n1+n2>n2+n1:
                return -1
            else:
                return 1
        nums=sorted(nums,key= cmp_to_key(compare))

        return "".join(nums)
