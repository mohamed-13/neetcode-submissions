class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        # s = s.lower()

        max_len = 0
        l, r = 0, 0
        current = ""

        while r < len(s):

            if s[r] not in current:
                current += s[r]
                max_len = max(max_len, len(current))
                r += 1

            else:
                # Remove characters from the left
                current = current[1:]
                l += 1

        return max_len