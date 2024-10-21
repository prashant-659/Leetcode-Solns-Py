class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        answer = []
        # All k-long subarrays
        for i in range(len(nums) - k + 1):

            if k == x:
                answer.append(sum(nums[i:i+k]))
                continue
            
            # Count occurrences
            d = dict()
            for j in nums[i:i+k]:
                if j in d:
                    d[j] += 1
                else:
                    d[j] = 1
            
            # If an array has less than x distinct elements
            if len(d) <= x:
                sum1 = 0
                for m in d:
                    sum1 += m * d[m]
                answer.append(sum1)
                continue
            
            # Sort based on occurrence then value
            sort = sorted(d.items(), key=lambda item: (item[1], item[0]), reverse=True)
            
            # Sum of the resulting array
            sum1 = 0
            for m in range(x):
                sum1 += sort[m][0] * sort[m][1]
            answer.append(sum1)
        
        return answer
        # def xsum(arr,x):
            
        #     mp=Counter(arr)
        #     heap=[(-cnt,n) for n,cnt in mp.items() ]
        #     heapq.heapify(heap)
        #     total=0
        #     topX=[]
        #     while heap and len(topX) < x:
        #         count, num = heapq.heappop(heap)
        #         topX.append((num, -count))
        #         total += num  # Add the element value (since we are asked for x-sum)
        #     return total

        # res=[]
        # n=len(nums)
        # window_counter = Counter(nums[:k])
        # res.append(xsum(window_counter, x))
        # for i in range(1, n - k + 1):
        #     outgoing_element = nums[i - 1]
        #     window_counter[outgoing_element] -= 1
        #     if window_counter[outgoing_element] == 0:
        #         del window_counter[outgoing_element]  # Remove from counter if count is zero

        #     incoming_element = nums[i + k - 1]
        #     window_counter[incoming_element] += 1

        #     res.append(xsum(window_counter, x))

        # return res




        # # for j in range():
        # #     substr=nums[i:j+1]
        # #     res.append(xsum(substr,x))
        # #     i+=1
        # # return res
