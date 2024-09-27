class MyCalendarTwo:

    def __init__(self):
        self.m=defaultdict()

    def book(self, start: int, end: int) -> bool:
        
        
        self.m[start]=1+self.m.get(start,0)
        self.m[end]=self.m.get(end,0)-1
        sum=0
        for i in sorted(self.m):
            sum+=self.m[i]

            if sum>=3:
                self.m[start]-=1
                self.m[end]+=1
                return False
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)