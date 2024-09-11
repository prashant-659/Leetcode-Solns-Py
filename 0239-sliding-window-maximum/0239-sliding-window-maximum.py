class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        #Monotonically decreasing queue
        
        # output = []
        # q = collections.deque()  # index
        # l = r = 0
        # # O(n) O(n)
        # while r < len(nums):
        #     # pop smaller values from q
        #     while q and nums[q[-1]] < nums[r]:
        #         q.pop()
        #     q.append(r)

        #     # remove left val from window
        #     if l > q[0]:
        #         q.popleft()

        #     if (r + 1) >= k:
        #         output.append(nums[q[0]])
        #         l += 1
        #     r += 1

        # return output
        #Monotonically decreasing queue

        # out = []
        # r,l = 0,0
        # q = collections.deque()
        # while r < len(nums):
        #     while q and q[-1] < nums[r]:
        #         q.pop()
        #     q.append(nums[r])
        #     if r+1 >= k:
        #         out.append(q[0])
        #         if nums[l] == q[0]:
        #             q.popleft()
        #         l+=1
        #     r+=1
        # return out

        q=deque()
        output=[]
        maxi=-sys.maxsize
        curr_sum=0
        i,j=0,0
        while j<len(nums):
            while q and q[-1]<nums[j]:
                q.pop()
            q.append(nums[j])
            if (j-i+1)<k:
                j+=1
            elif (j-i+1)==k:
                output.append(q[0])

                if q[0]==nums[i]:
                    q.popleft()
                i+=1
                j+=1
        return output
                
              

