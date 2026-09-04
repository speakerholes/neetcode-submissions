# prefix sum 
[0]

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        pref_arr = [0]
        vowels = "aeiou"
        for i, word in enumerate(words): 
            if word[0] in vowels and word[-1] in vowels: 
                pref_arr.append(pref_arr[i] + 1)
            else: 
                pref_arr.append(pref_arr[i])
        
        result = []
   
        for query in queries: 

            result.append(pref_arr[query[-1] + 1] - pref_arr[query[0]])
        return result
        
        
