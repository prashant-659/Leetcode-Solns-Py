class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # allowed=set(allowed)
        #count=0
        
        # for word in words:
        #     for c in word:
        #         if c not in allowed:
        #             count+=1
        #             break
        # return len(words)-count

        #BIT Masks
        bit_mask=0
        for c in allowed:
            bit=1<<(ord(c)-ord('a'))
            bit_mask=bit_mask | bit #0000 0101 = 0101
        res=len(words)
        for word in words:
            for c in word:
                bit=1<<(ord(c)-ord('a'))
                if bit & bit_mask==0:
                    res-=1
                    break
        return res