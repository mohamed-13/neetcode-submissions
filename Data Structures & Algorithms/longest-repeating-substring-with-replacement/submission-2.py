class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        max_freq = 0
        max_len = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            # Highest frequency character in the current window
            max_freq = max(max_freq, count[s[r]])

            # Number of characters we need to replace
            replacements = (r - l + 1) - max_freq

            # Window is invalid
            while replacements > k:
                count[s[l]] -= 1
                l += 1
                replacements = (r - l + 1) - max_freq

            max_len = max(max_len, r - l + 1)

        return max_len