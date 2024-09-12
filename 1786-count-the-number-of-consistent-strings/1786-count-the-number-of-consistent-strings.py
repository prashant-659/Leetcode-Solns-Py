class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # allowed=set(allowed)
        count=0
        
        # for word in words:
        #     for c in word:
        #         if c not in allowed:
        #             count+=1
        #             break
                
            
        # return len(words)-count

        count=0
        for word in words: 
            for c in word:
                if c in allowed:
                    hai=True
                else:
                    hai=False
                    break
            if hai==True:
                count+=1
        return count







