class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        is_increasing = True  # Indicates if the array is increasing.
        is_decreasing = True  # Indicates if the array is decreasing.

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                is_increasing = False

            elif nums[i] > nums[i - 1]:
                is_decreasing = False

            if not is_increasing and not is_decreasing:
                break

        return is_increasing or is_decreasing  # Return true if either condition is met.