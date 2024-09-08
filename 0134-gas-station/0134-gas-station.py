class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # start_index = []
        # for i in range(len(gas)):
        #     diff = gas[i] - cost[i]  # Access elements from both gas and cost
        #     if diff > 0:
        #         start_index.append(i)
        #     else:
        #         return -1
        # # return start_index[0] if start_index else -1  # Return -1 if start_index is empty
        # cost2=0
        # diff=[]
        # cycle=False
        # while start_index:
        #     i1=start_index.pop()
        #     j=i+1
        #     while j!=i1:
        #         if j1>len(gas)-1:
        #             j1=0
        #         cost2-=(gas[j]+cost[i1])
        #         if cost2>gas[i1]:
        #             return start_index
        #         j+=1
        # return -1

        
        # return -1
        # while start_index:
        #     i1 = start_index.pop()  # Get the last index in start_index
        #     j = i1 + 1  # Start checking from the next station
        #     total_gas = 0  # Reset total gas
           

        #     while j != i1:
        #         if j >= len(gas):  # Wrap around when reaching the end
        #             j = 0

        #         total_gas += gas[j] - cost[j]  # Add net gain/loss at this station

        #         if total_gas < 0:  # If we run out of gas, this index is not valid
        #             valid = False
        #             break

        #      j += 1  # Move to the next station

        # if valid:  # If the loop completes and the trip was valid, return the start index
        #     return i1

        # return -1  # If no valid start index was found
        # n,total_surplus, surplus, start=len(gas), 0, 0,0
        # for i in range(n):
        #     total_surplus+=gas[i]-cost[i]
        #     surplus+=gas[i]-cost[i]
        #     if surplus<0:
        #         surplus=0
        #         start=i+1
        # return -1 if (total_surplus<0) else start 
        if sum(gas)<sum(cost):
            return -1  
         
        total=0
        res=0
        
        for i in range(len(gas)):
            total+=(gas[i]-cost[i])
            if total<0:
                total=0
                res=i+1
        return res