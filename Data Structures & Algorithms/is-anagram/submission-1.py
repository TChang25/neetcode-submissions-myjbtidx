class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for s1, s2 in zip(sorted(s), sorted(t)):
            if (s1 != s2):
                return False
        return True