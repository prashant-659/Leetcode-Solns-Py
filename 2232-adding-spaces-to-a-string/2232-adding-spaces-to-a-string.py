class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # ind=set(spaces)
        # word=[]
        # for i in range(len(s)):
        #     if i in spaces:
        #         word.append(" ")
        #         word.append(s[i])
        #     else:
        #         word.append(s[i])

        # return "".join(word)

        res=[]
        l=0
        for r in spaces:
            res.append(s[l:r])
            l=r
        res.append(s[l:])

        return " ".join(res)
