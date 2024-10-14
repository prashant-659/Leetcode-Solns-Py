class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        trip=[0,0,0]
        
        for triplet in triplets:
            
            if(triplet[0]>target[0] or triplet[1]>target[1] or triplet[2]>target[2]):
                continue
            else:
                if(triplet[0]==target[0]):
                    trip[0]+=1
                if(triplet[1]==target[1]):
                    trip[1]+=1
                if(triplet[2]==target[2]):
                    trip[2]+=1
        
        if(trip[0]>0 and trip[1]>0 and trip[2]>0):
            return True
        else:
            return False