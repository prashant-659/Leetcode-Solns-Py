from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        m=len(matrix)
        n=len(matrix[0])

        result=0
        histogram=[0]*n

        for i in range(m):
            for j in range(n):
                if matrix[i][j]=="1":
                    histogram[j]+=1
                else:
                    histogram[j]=0
            
            result=max(result,self.largestRectangleArea(histogram))
        return result

    
    def largestRectangleArea(self, histogram: List[int]) -> int:
        def nsl(arr):
            stk = []
            ans = []
            
            for i in range(len(arr)):
                while stk and stk[-1][0] >= arr[i]:
                    stk.pop()
                if len(stk) == 0:
                    ans.append(-1)
                else:
                    ans.append(stk[-1][1])
                    
                stk.append([arr[i],i])
                
            return ans
            
            
        def nsr(arr):
            stk=[]
            ans=[]
            
            
            for i in range(len(arr)-1,-1,-1):
                
                while len(stk) and stk[-1][0]>=arr[i]:
                    stk.pop()
                    
                if len(stk)==0:
                    ans.append(len(arr))
                else:
                    ans.append(stk[-1][1])
                    
                stk.append([arr[i],i])
                
            return ans[::-1]
            
            
        
        right=nsr(histogram)
        left=nsl(histogram)
        
        width=[]
        
        for i in range(len(histogram)):
            width.append((right[i]-left[i]-1)*histogram[i])
            
            
        return max(width)