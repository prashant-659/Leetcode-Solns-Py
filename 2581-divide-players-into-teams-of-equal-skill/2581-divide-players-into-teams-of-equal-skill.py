class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        s=0
        e=len(skill)-1
        ans=0
        total=skill[s]+skill[e]
        while s<=e:
            if skill[s]+skill[e]!=total:
                return -1
            ans+=skill[s]*skill[e]
            s+=1
            e-=1
        return ans
            



