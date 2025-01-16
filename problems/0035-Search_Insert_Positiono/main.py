# Solution to problem Search_Insert_Positiono
# Problem ID: 0035

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        middle = 0
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle

            if target > nums[middle]:
                left = middle + 1
            else:
                right = middle - 1
        if target > nums[middle]:
            return middle + 1
        else:
            return middle
