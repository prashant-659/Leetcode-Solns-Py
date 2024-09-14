class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # ans=0
        # res=0

        # last=len(blocks)
        # for i in range(last-k+1):
        #     res=blocks.count('B',i,i+k)
        #     ans=max(res,ans)
        # ans=k-ans
        # return ans
        i=0
        j=0
        curr=0
        ans=sys.maxsize
        while j< len(blocks):
            if blocks[j]=='W':
                curr+=1
            if j-i+1<k:
                j+=1
            elif j-i+1==k:
                ans=min(ans,curr)
                if blocks[i]=='W':
                    curr-=1

                i+=1
                j+=1
        return ans