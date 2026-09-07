class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_dec = 1
        max_inc = 1
        dec_sub = 1
        inc_sub = 1

        for i in range(1, len(nums)): 
            
            if nums[i] > nums[i - 1]: # increasing
                inc_sub += 1
                dec_sub = 1
            elif nums[i] < nums[i - 1]: # decreasing
                dec_sub += 1
                inc_sub = 1
            else: 
                inc_sub = 1
                dec_sub = 1
            
            max_dec = max(dec_sub, max_dec)
            max_inc = max(inc_sub, max_inc)
        
        return max(max_dec, max_inc)