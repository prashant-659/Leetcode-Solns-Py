class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        ct=Counter(s)
        max_heap=[(-ord(c), cnt) for c, cnt in ct.items()]
        heapq.heapify(max_heap)

        res=[]
        while max_heap:
            #state1
            char, cnt=heapq.heappop(max_heap)

            char=chr(-char)
            cur_cnt=min(repeatLimit, cnt)

            res.append(char*cur_cnt)

            if cnt-cur_cnt >0 and max_heap:
                nxt_char, nxt_cnt=heapq.heappop(max_heap)
                nxt_char=chr(-nxt_char)
                res.append(nxt_char)
                if nxt_cnt>1:
                    heapq.heappush(max_heap, (-ord(nxt_char), nxt_cnt-1))
                
                heapq.heappush(max_heap, (-ord(char), cnt-cur_cnt))

        return "".join(res)                

            