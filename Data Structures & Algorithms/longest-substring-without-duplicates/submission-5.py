class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        string_dict = {}
        maxlen = 0
        while r < len(s):
            if s[r] in string_dict and string_dict[s[r]] >= l:
                l = string_dict[s[r]] + 1
            string_dict[s[r]] = r
            maxlen = max(maxlen, r - l + 1)
            r += 1

        return(maxlen)