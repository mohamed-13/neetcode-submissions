class Solution:
    def isPalindrome(self, s: str) -> bool:
        lt =[]
        for i in s.lower():
            if i.isalnum():
                lt.append(i)
        
       
        rlt = lt[::-1]
        lt = "".join(lt)

        rlt = "".join(rlt)

        if rlt == lt:
            return True

        else:
            return False