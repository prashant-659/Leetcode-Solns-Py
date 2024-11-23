class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        orient=[["."]* len(box) for _ in range(len(box[0]))]
        for r in range(len(box)):
            i=len(box[0])-1
            for c in range(len(box[0])-1,-1,-1):
                if box[r][c]=="#":
                    box[r][c], box[r][i]=box[r][i], box[r][c]
                    i-=1
                elif box[r][c]=="*":
                    i=c-1
        res=[]
        for c in range(len(box[0])):
            col=[]
            for r in reversed(range(len(box))):
                col.append(box[r][c])
            
            res.append(col)
        return res