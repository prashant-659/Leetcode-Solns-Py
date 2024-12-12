from sortedcontainers import SortedList
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        sh=[]
        for x, y, h in buildings:
            sh.append((x,h, 0))
            sh.append((y,h,1))
        sh.sort()


        active_heights=SortedList([0])
        ans=[]
        n=len(sh)
        i=0
        while i<n:
            cur_x=sh[i][0] 

            #process events with same x together
            while i<n and sh[i][0]==cur_x:
                x,h,t=sh[i]
                if t==0:
                    active_heights.add(h)
                else:
                    active_heights.remove(h)
                i+=1
        # check if heights has changed

            if not ans or ans[-1][1]!=active_heights[-1]:
                ans.append([cur_x, active_heights[-1]])
        return ans
