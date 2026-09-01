class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_i, t_i = 0, 0
        left_over = len(t) 

        while s_i < len(s) and t_i < len(t): 
            if s[s_i] == t[t_i]: 
                s_i += 1
                t_i += 1
                left_over -= 1
            else: 
                s_i += 1
        
        return left_over 
            