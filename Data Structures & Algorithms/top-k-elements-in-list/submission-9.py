
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        curr_k = k 
        result = []

        counts = Counter(nums)
        groups = defaultdict(list)
        for key, val in counts.items(): 
            groups[val].append(key)

        for val in range(len(nums), -1, -1):
            arr = groups[val]
            if curr_k > len(arr): 
                result += arr
                curr_k -= len(arr)
            else: 
                return result + arr[:curr_k]
            
        return result 