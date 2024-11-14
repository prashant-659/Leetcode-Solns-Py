class DetectSquares:

    def __init__(self):
        self.list1=[]
        self.mp=defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.list1.append(point)
        if tuple(point) not in self.mp:
            self.mp[tuple(point)]=1
        else:
            self.mp[tuple(point)]+=1


    def count(self, point: List[int]) -> int:
        res=0
        px,py=point
        for x,y in self.list1:
            if abs(px-x)!=abs(py-y) or px==x or py==y:
                continue
            res+=self.mp[(px,y)]*self.mp[(x,py)]
        return res
            


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)