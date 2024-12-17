class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # uncovered=set(houses)-set(heaters)

        # ranges=[[heater, heater] for heater in heaters]
        # radius=0

        # while uncovered:
        #     radius+=1

        #     for rng in ranges:
        #         rng[0]-=1
        #         rng[1]+=1
        #         uncovered.discard(rng[0])
        #         uncovered.discard(rng[1])
        # return radius

        # distances=[]
        # for house in houses:
        #     min_dist=float('inf')
        #     for heater in heaters:
        #         min_dist=min(min_dist, abs(heater-house))
        #     distances.append(min_dist)
        # return max(distances)

        heaters.sort()
        def bin_Sort(heaters, house):
            l,r=0, len(heaters)-1

            min_dist=float("inf")
            while l<=r:
                m=(l+r)//2

                min_dist=min(min_dist, abs(heaters[m]-house))
                if heaters[m]<house:
                    l=m+1
                else:
                    r=m-1
            return min_dist
        
        radius=0
        for house in houses:
            radius=max(radius, bin_Sort(heaters, house))
        return radius


