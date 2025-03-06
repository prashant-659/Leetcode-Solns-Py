class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        n=len(transactions)
        name=[""]*n
        amount=[0]*(n)
        city=[""]*n
        time=[0]*n
        for i,t in enumerate(transactions):
            cur=t.split(",")
            na,t,a,ci=cur[0],cur[1],cur[2],cur[3]
            name[i]=na
            time[i]=int(t)
            amount[i]=int(a)
            city[i]=ci
        index=set()
        for i in range(n):
            if amount[i]>1000:
                index.add(i)
            for j in range(i+1,n):
                # if i==j:
                #     continue
                if  name[i]==name[j] and city[i]!=city[j] and abs(time[i]-time[j])<=60:
                    index.add(j)
                    index.add(i)
        res=[transactions[i] for i in index]
        
        return res
                