class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s=""

        for i in s:
            if i.isalnum():
                new_s += i.lower()

        ct = 0

        for i in range(len(new_s)-1,-1,-1):
            if new_s[i] != new_s[ct]:
                return False
            ct +=1

        return True
