class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # res=0
        # n=start^goal
        # while n:
        #     res+=n&1
        #     n=n>>1
        # return res

        #Brian kernighan's algo
        #donot touch zeroes in bits
        # by subtracting 1 from binary representation, we can get rid of ones
        # res=0
        # n=start^goal
        # while n:
        #     n=n&(n-1)
        #     res+=1
        # return res

        maxi=max(start, goal)
        res=0
        while maxi:
            if (start&1)!=(goal&1):
                res+=1
            start=start>>1
            goal=goal>>1
            maxi=maxi>>1

        return res


        