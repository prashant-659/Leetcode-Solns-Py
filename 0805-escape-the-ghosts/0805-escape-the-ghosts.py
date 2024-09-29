class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        d_ghost_to_target=[]
        for x,y in ghosts:
            d_ghost_to_target.append(abs(x-target[0])+abs(target[1]-y))
        
        me_to_target=abs(target[0]-0)+abs(target[1]-0)
        for dis in d_ghost_to_target:
            if dis<=me_to_target:
                return False
        return True
