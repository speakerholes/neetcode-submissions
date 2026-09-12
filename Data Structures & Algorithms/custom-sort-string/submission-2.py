class Solution:
    def customSortString(self, order: str, s: str) -> str:
        total_chars = Counter(s)
        result = []
        for char in order: 
            if char in total_chars: 
                result += [char] * total_chars[char]
                del total_chars[char]
        
        #left overs
        for char, count in total_chars.items():
            result += [char] * count

        return "".join(result)