class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def back(i, path, total):
            nonlocal res
            if total==target:
                res.append(path.copy())
                return
            if i>=len(candidates) or total>target:
                return
           
            
           
            path.append(candidates[i])
            back(i, path, total+candidates[i])
            path.pop()
            back(i+1, path, total)
        back(0, [],0)
        return res