class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n=len(word)
        count=1
        i=k
        
        def check(word, i):
            j=0
            while i<len(word):
                if word[j]==word[i]:
                    i+=1
                    j+=1
                else:
                    break
            return i==len(word)


        while i<n:
            # i to n-i temp (suffix)==prefix of original word of len n-i
            if check(word,i):
                break
            count+=1
            i+=k
        return count