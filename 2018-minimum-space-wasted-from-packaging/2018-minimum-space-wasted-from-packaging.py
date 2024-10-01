class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        packages.sort()
        prefix=[0]*(len(packages)+1)
        for i in range(1,len(packages)+1):
            prefix[i]=prefix[i-1]+packages[i-1]
        min_waste=float('inf')
        mod=10 ** 9 + 7
        for box in boxes:
            box.sort()
            if box[-1]<packages[-1]:
                continue
            curr_waste=0
            prev_idx=-1

            for b in box:
                idx=self.binary_search(packages,b)
                if idx==-1:
                    continue
                
                total_size=(idx-prev_idx)*b

                package_size=prefix[idx+1]-(prefix[prev_idx+1] if prev_idx!=-1 else 0)

                curr_waste+=(total_size-package_size)
                prev_idx=idx
            min_waste=min(min_waste,curr_waste)

        return -1 if min_waste == float('inf') else min_waste % mod


    def binary_search(self, nums, target):
        start, end = 0, len(nums) - 1
        ans = -1

        while start <= end:
            mid = start + (end - start) // 2
            if target >= nums[mid]:
                ans = mid
                start = mid + 1
            else:
                end = mid - 1

        return ans