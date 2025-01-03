class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        size=len(cardPoints)-k
        minSum=float("inf")
        l=cur=0

        for r, v in enumerate(cardPoints):
            cur+=v
            if r-l+1>size:
                cur-=cardPoints[l]
                l+=1
            if r-l+1==size:
                minSum=min(minSum, cur)
        return sum(cardPoints)-minSum