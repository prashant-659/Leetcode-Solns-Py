# # class SegTree:
# #     def __init__(self, data):
# #         self.n = len(data)
# #         self.tree = [0] * (4 * (self.n))
# #         self.build(data, 1, 0, self.n - 1)  # Fixed indices here
    
# #     def build(self, data, node, start, end):
# #         if start == end:
# #             self.tree[node] = data[start]
# #         else:
# #             m = (start + end) // 2
# #             self.build(data, 2 * node, start, m)
# #             self.build(data, 2 * node + 1, m + 1, end)  # Fixed the range
# #             self.tree[node] = self.tree[2 * node] & self.tree[2 * node + 1]
    
# #     def query(self, l, r):
# #         return self._query(1, 0, self.n - 1, l, r)

# #     def _query(self, node, start, end, l, r):
# #         if r < start or end < l:
# #             return (1 << 31) - 1  # return all bits set (neutral element for AND)
# #         if l <= start and end <= r:
# #             return self.tree[node]
# #         m = (start + end) // 2
# #         left = self._query(2 * node, start, m, l, r)
# #         right = self._query(2 * node + 1, m + 1, end, l, r)
# #         return left & right

# # # class SegmentTree:
# # #     def __init__(self, nums):
# # #         n = len(nums)
# # #         self.tree = [0] * (4 * n)
# # #         self.n = n
# # #         self.build(nums, 0, 0, n - 1)
        
# # #     def build(self, nums, node, start, end):
# # #         if start == end:
# # #             self.tree[node] = nums[start]
# # #         else:
# # #             mid = (start + end) // 2
# # #             left_child = 2 * node + 1
# # #             right_child = 2 * node + 2
# # #             self.build(nums, left_child, start, mid)
# # #             self.build(nums, right_child, mid + 1, end)
# # #             self.tree[node] = self.tree[left_child] & self.tree[right_child]
    
# # #     def query(self, node, start, end, L, R):
# # #         if R < start or end < L:
# # #             return (1 << 31) - 1
        
# # #         if L <= start and end <= R:
# # #             return self.tree[node]
        
# # #         mid = (start + end) // 2
# # #         left_child = 2 * node + 1
# # #         right_child = 2 * node + 2
# # #         left_result = self.query(left_child, start, mid, L, R)
# # #         right_result = self.query(right_child, mid + 1, end, L, R)
# # #         return left_result & right_result


# # class Solution:
    
# #     def countSubarrays(self, nums: List[int], k: int) -> int:
# #         st=SegTree(nums)
# #         ans=0
# #         n=len(nums)
# #         for i in range(n):
# #             l=i
# #             r=n-1
# #             st=-1
# #             end=-1
# #             while l<=r:
# #                 m=(l+r)>>1
# #                 val=st.query(i,m)

# #                 if val>k:
# #                     l=m+1
# #                 else:
# #                     if val==k:
# #                         st=m
# #                     r=m-1
# #                 if st==-1:
# #                     continue
# #                 l=i, r=n-1
# #                 while l<=r:
# #                     m=(l+r)>>1
# #                     val=st.query(i, m)
# #                     if val>=k:
# #                         if val==k:
# #                             ed=m
# #                         l=m+1
# #                     else:
# #                         r=m-1
# #                 if ed==-1:
# #                     continue
# #                 ans+=(ed-st)+1
# #         return ans
# class SegTree:
#     def __init__(self, data):
#         self.n = len(data)
#         self.tree = [0] * (4 * self.n)
#         self.build(data, 1, 0, self.n - 1)
    
#     def build(self, data, node, start, end):
#         if start == end:
#             self.tree[node] = data[start]
#         else:
#             m = (start + end) // 2
#             self.build(data, 2 * node, start, m)
#             self.build(data, 2 * node + 1, m + 1, end)
#             self.tree[node] = self.tree[2 * node] & self.tree[2 * node + 1]
    
#     def query(self, l, r):
#         return self._query(1, 0, self.n - 1, l, r)

#     def _query(self, node, start, end, l, r):
#         if r < start or end < l:
#             return (1 << 31) - 1  # Return all bits set (neutral element for AND)
#         if l <= start and end <= r:
#             return self.tree[node]
#         m = (start + end) // 2
#         left = self._query(2 * node, start, m, l, r)
#         right = self._query(2 * node + 1, m + 1, end, l, r)
#         return left & right

# class Solution:
#     def countSubarrays(self, nums, k):
#         return self.atLeastK(nums, k) - self.atLeastK(nums, k + 1)

#     def atLeastK(self, nums, k):
#         ans = 0
#         temp = [0] * 32  # Frequency array for bits
        
#         l = 0
#         for r in range(len(nums)):
#             for i in range(32):
#                 if (1 << i) & nums[r]:
#                     temp[i] += 1
            
#             while (r - l + 1) > 0 and self.calc(temp, r - l + 1) < k:
#                 for i in range(32):
#                     if (1 << i) & nums[l]:
#                         temp[i] -= 1
#                 l += 1
            
#             ans += (r - l + 1)

#         return ans

#     # Function to calculate the AND from frequency vector
#     def calc(self, temp, w):
#         ans = 0
#         for i in range(32):
#             if temp[i] == w:
#                 ans += (1 << i)
#         return ans

#         # st = SegTree(nums)  # Initialize the Segment Tree
#         # ans = 0
# #         n = len(nums)

# #         for i in range(n):
# #             l, r = i, n - 1
# #             valid_end = -1  # To store the valid end for the subarray
            
# #             while l <= r:
# #                 m = (l + r) // 2
# #                 val = st.query(i, m)
                
# #                 if val > k:
#                     l = m + 1
#                 else:
#                     if val == k:
#                         valid_end = m
#                     r = m - 1

#             if valid_end == -1:
#                 continue

#             # Now we need to find the farthest end index `ed` for the valid subarrays
#             l, r = i, n - 1
#             while l <= r:
#                 m = (l + r) // 2
#                 val = st.query(i, m)

#                 if val >= k:
#                     if val == k:
#                         ed = m
#                     l = m + 1
#                 else:
#                     r = m - 1

#             if valid_end != -1 and ed != -1:
#                 ans += (ed - valid_end + 1)
                
#         return ans
from collections import defaultdict

class Solution:
    def countSubarrays(self, nums, k):
        res = 0
        mp = defaultdict(int)
        for num in nums:
            temp = defaultdict(int)
            temp[num] += 1
            
            for key, value in mp.items():
                temp[key & num] += value

            res += temp[k]
            mp = temp
        
        return res
