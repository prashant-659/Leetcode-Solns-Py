class Solution:
    def countLargestGroup(self, n: int) -> int:
        res=[]
        def count(di):
            equals=0

            while di>0:
                equals+=di%10
                di=di//10
            return equals
        x=Counter()
        for i in range(1,n+1):
            j=count(i)
            x[j]+=1
        max_size=max(x.values())
        return list(x.values()).count(max_size)