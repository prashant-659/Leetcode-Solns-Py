class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        n = len(events)
        req_index = events[0][0]
        max_time = events[0][1]

        for i in range(1, n):
            cur_time = events[i][1] - events[i - 1][1]
            cur_index = events[i][0]
            # Update the req_index when cur_time > max_time
            # or when cur_time == max_time then check for smaller index 
            # among cur_index and req_index and update req_index and max_time.
            if cur_time > max_time or (cur_time == max_time and cur_index < req_index):
                max_time = cur_time
                req_index = cur_index
        
        return req_index