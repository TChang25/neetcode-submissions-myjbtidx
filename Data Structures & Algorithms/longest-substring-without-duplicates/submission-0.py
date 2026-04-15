class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        seen = set()
        maxLen = 0
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            r += 1
            maxLen = max(r - l, maxLen)
        return maxLen
            

            