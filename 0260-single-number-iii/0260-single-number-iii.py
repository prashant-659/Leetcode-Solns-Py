class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor=0
        for n in nums:
            xor^=n
        distbit=xor&(-xor)

        u1, u2=0,0
        for n in nums:
            if n & distbit:
                u1^=n
            else:
                u2^=n
        return [u1, u2]


           
