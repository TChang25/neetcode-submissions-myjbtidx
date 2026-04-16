class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr = [0] * 26
        for s in s1:
            arr[ord(s) - ord('a')] += 1
        orgFTuple = tuple(arr)        
        
        if len(s1) > len(s2):
            return False

        for i in range(0, len(s2) - len(s1)+1):
            arr = [0] * 26
            for j in range(i, i + len(s1)):
                arr[ord(s2[j]) - ord('a')] += 1
            if tuple(arr) == orgFTuple:
                return True
        return False

            