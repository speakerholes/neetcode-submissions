class Solution:
    def maxDifference(self, s: str) -> int:
        counts = Counter(s)
        min_odd, max_odd = float("inf"), 0
        min_even, max_even = float("inf"), 0

        for key, count in counts.items():
            if count % 2 == 1: # is odd
                min_odd = min(min_odd, count)
                max_odd = max(max_odd, count)
            else: 
                min_even = min(min_even, count)
                max_even = max(max_even, count)
        
        return max(max_odd - min_even, min_odd - max_even)

