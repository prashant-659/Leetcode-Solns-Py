class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        RT = list(accumulate(skill, initial=0))
        N = len(skill)
        M = len(mana)

        start = [0] * M
        for j in range(1, M):
            for i in range(N):
                start[j] = max(start[j], start[j-1] + mana[j-1] * RT[i+1] - mana[j] * RT[i])

        return start[-1] + RT[-1] * mana[-1]