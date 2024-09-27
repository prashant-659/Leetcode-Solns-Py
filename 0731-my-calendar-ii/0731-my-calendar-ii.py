
class MyCalendarTwo:

    def __init__(self):
        # self.m=defaultdict()
        self.event=[]
        self.doublebooking=[]

    def book(self, start: int, end: int) -> bool:
        
        for booking in self.doublebooking:
            s,e=booking[:]
            if start<e and end>s:
                return False
        
        for booking in self.event:
            s,e =booking[:]
            if start<e and end>s:
                self.doublebooking.append((max(start,s),min(end,e)))
       

        self.event.append((start,end))
        return True
        
        # self.m[start]=1+self.m.get(start,0)
        # self.m[end]=self.m.get(end,0)-1
        # sum=0
        # for i in sorted(self.m):
        #     sum+=self.m[i]

        #     if sum>=3:
        #         self.m[start]-=1
        #         self.m[end]+=1
        #         return False
        # return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)