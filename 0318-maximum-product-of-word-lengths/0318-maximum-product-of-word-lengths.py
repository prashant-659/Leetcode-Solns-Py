class Solution:
    def maxProduct(self, words: List[str]) -> int:
        prods = [0]
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                t = True
                for k in set(words[i]):
                    if k in words[j]:
                        t = False
                        break
                if t:
                    prods.append(len(words[i])*len(words[j]))
        return max(prods)
                    