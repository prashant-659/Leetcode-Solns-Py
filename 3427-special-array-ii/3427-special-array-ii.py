# class Solution:
#     def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
#         res=[]

#         for start, end in queries:
#             t=True
#             for i in range(start+1,end+1):
#                 if nums[i-1]%2==nums[i]%2:
#                     t=False
#                     break
            
#             res.append(t)
#         return res

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        lst = [1]
        ans = []
        s = 1
        for i in range(len(nums)-1):
            if nums[i]%2 == nums[i+1]%2:
                s += 0
            else:
                s += 1
            lst.append(s)
        for q in queries:
            if abs(q[0] - q[1]) == lst[q[1]] - lst[q[0]]:
                ans.append(True)
            else:
                ans.append(False)
        return ans
