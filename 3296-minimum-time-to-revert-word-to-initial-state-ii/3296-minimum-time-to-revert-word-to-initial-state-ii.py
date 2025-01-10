class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        i=1
        n=len(word)
        lps=[0]*(n)
        length=0
        while i< n:
            if word[i]==word[length]:
                length+=1
                lps[i]=length
                i+=1
            else:
                if length!=0:
                    length=lps[length-1]
                else:
                    lps[i]=0
                    i+=1
        
        maxLps = lps[n - 1]

        while maxLps > 0 and (n - maxLps) % k != 0:
            maxLps = lps[maxLps - 1]

        if (n - maxLps) % k == 0:
            return (n - maxLps) // k

        return math.ceil(n / k)  # or, (n + k - 1) // k