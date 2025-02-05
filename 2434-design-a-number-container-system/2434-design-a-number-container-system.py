from sortedcontainers import SortedList
class NumberContainers:

    def __init__(self):
        self.iton={}
        self.i=defaultdict(lambda: SortedList())

    def change(self, index: int, number: int) -> None:
        if index in self.iton:
            prev=self.iton[index]
            self.i[prev].remove(index)
        
        self.iton[index]=number
        self.i[number].add(index)
      
        

    def find(self, number: int) -> int:
        if number not in self.i or len(self.i[number])==0:
            return -1
        return self.i[number][0]
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)