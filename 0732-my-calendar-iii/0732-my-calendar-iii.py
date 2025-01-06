class MyCalendarThree:

    def __init__(self):
        self.mp={}
        self.maxCount=0


    def book(self, startTime: int, endTime: int) -> int:
        self.mp[startTime]=1+self.mp.get(startTime,0)
        self.mp[endTime]=self.mp.get(endTime,0)-1
        count=0
        for time in sorted(self.mp):
            count+=self.mp[time]
            self.maxCount=max(self.maxCount, count)
        return self.maxCount

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)