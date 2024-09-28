# class Node:
#     def __init__(self,val,next,prev):
#         self.data=val
#         self.next=next
#         self.prev=prev
    
# class MyCircularDeque:

#     def __init__(self, k: int):
#         self.size=0
#         self.space=k
#         self.left=Node(0,None,None)
#         self.right=Node(0,None,self.left)
#         self.left.next=self.right
        

#     def insertFront(self, value: int) -> bool:
#         if self.isFull():
#             return False
#         new_node=Node(value,None,None)
#         temp=self.left.prev
#         temp.prev=new_node
#         new_node.next=temp  

#         self.left.next=new_node
#         new_node.prev=self.left

#         self.size+=1
#         return True      
        

#     def insertLast(self, value: int) -> bool:
#         if self.isFull():
#             return False
#         new_node=Node(value,None,None)

#         temp=self.right.prev
#         temp.next=new_node
#         new_node.prev=temp

#         new_node.next=self.right
#         self.right.prev=new_node

#         self.size+=1
#         return True
        
#     def deleteFront(self) -> bool:
#         if self.isEmpty():
#             return False
        
#         temp = self.left.next
#         self.left.next = temp.next
#         temp.next.prev = self.left
#         del temp

#         self.size -= 1
#         return True

#     def deleteLast(self) -> bool:
#         if self.isEmpty():
#             return False
        
#         temp = self.right.prev
#         self.right.prev = temp.prev
#         temp.prev.next = self.right

#         self.size -= 1
#         return True

#     def getFront(self) -> int:
#         if self.isEmpty():
#             return -1
        
#         return self.left.next.val

#     def getRear(self) -> int:
#         if self.isEmpty():
#             return -1
        
#         return self.right.prev.val

#     def isEmpty(self) -> bool:
#         return self.size == 0

#     def isFull(self) -> bool:
#         return self.size == self.space


# # Your MyCircularDeque object will be instantiated and called as such:
# # obj = MyCircularDeque(k)
# # param_1 = obj.insertFront(value)
# # param_2 = obj.insertLast(value)
# # param_3 = obj.deleteFront()
# # param_4 = obj.deleteLast()
# # param_5 = obj.getFront()
# # param_6 = obj.getRear()
# # param_7 = obj.isEmpty()
# # param_8 = obj.isFull()

class Node:
    def __init__(self, val, nex, prev):
        self.val, self.nex, self.prev = val, nex, prev

class MyCircularDeque:

    def __init__(self, k: int):
        self.size = 0
        self.space = k
        self.left = Node(0, None, None)
        self.right = Node(0, None, self.left)
        self.left.nex = self.right

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        
        new_node = Node(value, None, None)
        
        temp = self.left.nex
        temp.prev = new_node
        new_node.nex = temp

        self.left.nex = new_node
        new_node.prev = self.left

        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        
        new_node = Node(value, None, None)

        temp = self.right.prev
        temp.nex = new_node
        new_node.prev = temp

        new_node.nex = self.right
        self.right.prev = new_node

        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        temp = self.left.nex
        self.left.nex = temp.nex
        temp.nex.prev = self.left
        del temp

        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        
        temp = self.right.prev
        self.right.prev = temp.prev
        temp.prev.nex = self.right

        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.left.nex.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.right.prev.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.space