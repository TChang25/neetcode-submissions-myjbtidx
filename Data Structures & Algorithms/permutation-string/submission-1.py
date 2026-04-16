class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        if len(s1) > len(s2):
            return False
        for i in range(0, len(s2) - len(s1)+1):
            substr = sorted(s2[i:i+len(s1)])
            if substr == s1:
                return True
        return False

            