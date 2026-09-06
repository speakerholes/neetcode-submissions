class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        curr_ones = 0

        for char in nums: 
            if char == 0: 
                curr_ones = 0
            else: 
                curr_ones += 1
            result = max(result, curr_ones)

        return result