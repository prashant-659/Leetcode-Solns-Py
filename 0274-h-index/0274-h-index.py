class Solution:
    def hIndex(self, citations: List[int]) -> int:
        size=len(citations)
        req=1
        rec_num=0
        citations.sort(reverse=True)
        for i in citations:
            if i>=req:
                rec_num+=1
                req+=1
        return rec_num

