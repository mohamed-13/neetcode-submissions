class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        # dict_t = {}

        for i in s:
            if i not in dict_s:
                dict_s[i] = 1
            else:
                dict_s[i] += 1 
        
        for i in t:
            if i in dict_s:
                dict_s[i] -= 1
            else:
                return False 
        
        for i in dict_s:
            if dict_s[i] !=0:
                return False

        return True