class Solution:
    def maxScore(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]**2
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        def lcm(a,b):
            return (a*b)//gcd(a,b)
        
        n1=len(nums)
        total_gcd=nums[0]
        total_lcm=nums[0]
        for n in nums[1:]:
            total_gcd=gcd(total_gcd,n)
            total_lcm=lcm(total_lcm, n)
        max_score=total_gcd*total_lcm

        for i in range(n1):
            cur_gcd=0
            cur_lcm=1
            for j in range(n1):
                if i!=j:
                    cur_gcd=gcd(cur_gcd, nums[j])
                    cur_lcm = lcm(cur_lcm, nums[j])
            max_score = max(max_score, cur_gcd * cur_lcm)
        
        return max_score  