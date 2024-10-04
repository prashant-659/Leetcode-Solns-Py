class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        #Greedy
        maxstr=[i for i in ("ab" if x>=y else "ba")]
        minstr=[i for i in ("ba" if x>=y else "ab")]

        maxX=max(x,y)
        minX=min(x,y)

        cost=0
        stack1=[]
        s=[i for i in s]

        for ch in s:
            if len(stack1)>0 and (stack1[-1]==maxstr[0] and ch==maxstr[1]):
                del stack1[-1]
                cost+=maxX
            else:
                stack1.append(ch)
            
        sb=""
        while len(stack1)>0:
            sb+=stack1[-1]
            del stack1[-1]
        sb=sb[::-1]
        remstr=sb
        for ch in remstr:
            if (len(stack1))>0 and (stack1[-1]==minstr[0] and ch==minstr[1]):
                del stack1[-1]
                cost+=minX
            else:
                stack1.append(ch)
        return cost