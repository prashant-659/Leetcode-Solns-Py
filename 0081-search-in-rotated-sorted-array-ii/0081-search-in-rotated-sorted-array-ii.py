class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l, end = 0, len(nums) - 1

        while l <= end:
            mid = (l + end) // 2
            if target == nums[mid]:
                return True

            if nums[l] == nums[mid]:
                l += 1
                continue
            elif nums[mid] <= nums[end]:
                if target >= nums[mid] and target <= nums[end]:
                    l = mid + 1
                else:
                    end = mid - 1
            else:
                if target >= nums[l] and target <= nums[mid]:
                    end = mid - 1
                else:
                    l = mid + 1

        return False