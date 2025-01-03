# class Solution:
#     def resultsArray(self, nums: List[int], k: int) -> List[int]:
        # res=[]
        # for i in range(len(nums)-k+1):
        #     is_valid=True
        #     max_el=nums[i]
        #     for j in range(i,i+k-1):
        #         if nums[j]+1 != nums[j+1]:
        #             isvalid=False
        #             break
        #         max_ele=max(max_el,nums[j])
        #     if is_valid:
        #         res.append(max(max_el,nums[i-k+1]))
        #     else:
        #         res.append(-1)
        # return res

# class Solution:
#     def resultsArray(self, nums: List[int], k: int) -> List[int]:
#         i,j=0,0
#         max_ele=0
#         res=[]
#         while j<len(nums):
#             if nums[j]>max_ele:
#                 max_ele=nums[j]

#             if (j-i+1)<k:
#                 j+=1
#             elif (j-i+1)==k:
#                 res.append(max(max_ele, nums[i]))
            
#             i+=1
#             j+=1
#         return res








        # n = len(nums)
        # result = []
        # for i in range(n - k + 1):
        #     is_valid = True
        #     max_element = nums[i]
        #     for j in range(i, i + k - 1):
        #         if nums[j] + 1 != nums[j + 1]:
        #             is_valid = False
        #             break
        #         max_element = max(max_element, nums[j])
            
        #     if is_valid:
        #         result.append(max(max_element, nums[i + k - 1]))
        #     else:
        #         result.append(-1)
        
        # return result       
                

# class Solution:
#     def resultsArray(self, nums: List[int], k: int) -> List[int]:
        # res=[]
        # for i in range(len(nums)-k+1):
        #     is_valid=True
        #     max_el=nums[i]
        #     for j in range(i,i+k-1):
        #         if nums[j]+1 != nums[j+1]:
        #             isvalid=False
        #             break
        #         max_ele=max(max_el,nums[j])
        #     if is_valid:
        #         res.append(max(max_el,nums[i-k+1]))
        #     else:
        #         res.append(-1)
        # return res

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = []
        for i in range(n - k + 1):
            is_valid = True
            max_element = nums[i]
            for j in range(i, i + k - 1):
                if nums[j] + 1 != nums[j + 1]:
                    is_valid = False
                    break
                max_element = max(max_element, nums[j])
            
            if is_valid:
                result.append(max(max_element, nums[i + k - 1]))
            else:
                result.append(-1)
        
        return result       
