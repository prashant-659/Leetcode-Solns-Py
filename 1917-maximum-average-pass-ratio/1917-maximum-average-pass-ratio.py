# class Solution:
#     def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
#         maxHeap=[]
#         i=0
#         for no, total in classes:
#             perc=no/total
#             new_perc=no+1/total+1
#             delta=new_perc-perc
#             maxHeap.append((-delta,no, total ))
#             i+=1

#         heapify(maxHeap)
#         for i in range(extraStudents):
#             delta, no, total=heapq.heappop(maxHeap)
#             no+=1
#             total+=1
#             new_delta=(no+1)/(total+1)-no/total
#             heapq.heappush(maxHeap,(-new_delta, no, total))
#         ans=0
#         while maxHeap:
#             delta, no, total=heapq.heappop(maxHeap)
#             ans+=no/total
#         return round(ans/len(classes),5)
            
import heapq
from typing import List

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Max-heap where we store the negative of the improvement delta to simulate a max-heap
        perc = []
        
        # Calculate the initial improvement delta for each class
        for no, total in classes:
            delta = (no + 1) / (total + 1) - no / total  # How much the ratio improves if we add 1 student
            heapq.heappush(perc, (-delta, no, total))  # Use negative delta to simulate max-heap
        
        # Distribute extra students
        for _ in range(extraStudents):
            delta, no, total = heapq.heappop(perc)
            no += 1
            total += 1
            new_delta = (no + 1) / (total + 1) - no / total  # New improvement for the updated class
            heapq.heappush(perc, (-new_delta, no, total))
        
        # Calculate the total average pass ratio
        ans = 0
        while perc:
            _, no, total = heapq.heappop(perc)
            ans += no / total  # Use the updated no and total for each class
        
        return round(ans / len(classes), 5)



            