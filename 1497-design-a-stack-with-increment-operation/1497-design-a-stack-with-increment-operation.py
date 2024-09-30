class CustomStack:

    def __init__(self, maxSize: int):
        self.stack=[]
        self.size=maxSize

    def push(self, x: int) -> None:
        if len(self.stack)<self.size:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        else:
            val =self.stack.pop()
            return val
        

    def increment(self, k: int, val: int) -> None:
        if len(self.stack)<k:
            for i in range(len(self.stack)):
                self.stack[i]+=val
        else:
            for i in range(k):
                self.stack[i]+=val





# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)