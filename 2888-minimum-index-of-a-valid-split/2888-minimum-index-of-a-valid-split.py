class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        r=Counter(nums)
        l=defaultdict(int)

        for i in range(len(nums)):
            l[nums[i]]+=1
            r[nums[i]]-=1

            l_i=i+1
            r_i=len(nums)-i-1
            if 2*l[nums[i]]>l_i and 2*r[nums[i]]>r_i:
                return i
        return -1


#         store=[[val,key] for key, val in mp.items()]
#         store.sort(reverse=True)
#         major=store[0][1]
#         halfornot=store[0][0]
#         i=0
#         aagese=0
#         pichese=0
#         l=0
#         r=len(nums)-1
#         while l<r:
#             e1=nums[l]
#             e2=nums[r]
#             if e1==major:
#                 aagese+=1
#             if e2==major:
#                 pichese+=1
#             if aagese+pichese==halfornot and aagese>(l+1)//2 and pichese>(len(nums)-r+1)//2:
#                 return i-1
#             l+=1
#             r-=1
#         return -1








# #         ele=-1
# #         ct=0
# #         for i in range(len(nums)):
# #             if ct==0:
# #                 ele=nums[i]
# #                 ct=1
# #             else:
# #                 if nums[i]==ele:
# #                     ct+=1
# #                 else: 
# #                     ct-=1
# #         dom = ele
# #         pre=[0]*len(nums)
# #         pre[0]=1 if pre[0]==dom else 0
# #         for i in range(1,len(nums)):
# #             if nums[i]==dom:
# #                 pre[i]=pre[i-1]+1
# #             else:
#                 pre[i]=pre[i-1]
#         count=0
#         for i in range(len(nums)):
#             if nums[i]==dom:
#                 count+=1
#             if count*2>(i+1 ) and (ct-count)*2>(len(nums)-i-1):
#                 return i
#         return -1
