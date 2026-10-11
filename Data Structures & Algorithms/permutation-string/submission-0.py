class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2)<len(s1):
            return False

        s1_count = [0]*26
        s2_sub_count = [0]*26

        for i in s1:
            s1_count[ord(i) - 97] +=  1

        k = len(s1)

        for idx,c in enumerate(s2):
            s2_sub_count[ord(c) - 97] +=  1
            if idx>=k:
                s2_sub_count[ord(s2[idx - k]) - 97] -=1
            if s1_count == s2_sub_count:
                return True
        return False


