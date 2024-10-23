class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        # res=[]
        # n=0
        # for i in range(x+1):
        #     for j in range(y+1):
        #         n=x**i+y**j
        #         if n<=bound and n not in res:
        #             res.append(n)
        # for i in range(y+1):
        #     for j in range(x+1):
        #         n=x**i+y**j
        #         if n<=bound and n not in res:
        #             res.append(n)
        # return res
        pX=[1]
        pY=[1]
        powX=x
        powY=y
        if x!=1:
            while powX<bound:
                pX.append(powX)
                powX=powX*x
        if y!=1:
            while powY<bound:
                pY.append(powY)
                powY=powY*y
        res=set()
        for i in range(len(pX)):
            for j in range(len(pY)):
                if (pX[i]+pY[j])<=bound:
                    res.add(pX[i]+pY[j])
        return list(res)
