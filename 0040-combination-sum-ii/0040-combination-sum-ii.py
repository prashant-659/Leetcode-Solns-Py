class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def dfs(i, cur, total):
            if total==target:
                res.append(cur.copy())
                return
            if i>=len(candidates) or total>target:
                return
            
            #i clude
            cur.append(candidates[i])
            dfs(i+1, cur, total+candidates[i])
            cur.pop()

            #skip
            while i<len(candidates)-1 and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1, cur, total)

        dfs(0,[],0)
        return res
            