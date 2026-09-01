
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_result = ""

        for word in strs: 

            encoded_result += f"{len(word)}#{word}"

        return encoded_result

    def decode(self, s: str) -> List[str]:
        i = 0
        curr_digit = 0
        result = []
        while i < len(s): 

            while s[i] != "#": 
                curr_digit = curr_digit * 10 + int(s[i])
                i += 1
            
            result.append(s[i + 1:i + curr_digit + 1])
            i += curr_digit + 1
            curr_digit = 0
    
        return result

            


