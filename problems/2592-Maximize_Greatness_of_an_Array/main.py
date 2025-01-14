# Solution to problem Maximize_Greatness_of_an_Array
# Problem ID: 2592

class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        count = 0
        i_array = sorted(nums, reverse=True) # sorted nums asc
        j_array = sorted(nums) # sorted nums desc
        i_idx = len(nums) - 1
        j_idx = 0
        while True:
            if i_idx < 0:
                return count
            elif i_array[i_idx] > j_array[j_idx]:
                count += 1
                j_idx += 1
            i_idx -= 1
