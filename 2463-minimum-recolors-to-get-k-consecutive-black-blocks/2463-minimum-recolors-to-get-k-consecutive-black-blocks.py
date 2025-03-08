class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l=0
        cur=0
        ans=float("inf")
        for r in range(len(blocks)):
            if blocks[r]=="W":
                cur+=1
            
            while r-l+1>k:
                if blocks[l]=="W":
                    cur-=1
                l+=1
            if r-l+1==k:
                ans=min(ans, cur)
        return ans
