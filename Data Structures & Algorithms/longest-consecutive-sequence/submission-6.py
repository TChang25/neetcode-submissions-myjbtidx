class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxLen = 0
        for i in range(0, len(nums)):
            leng = 0
            dist = 0
            while nums[i] - dist in s:
                if nums[i] - dist in s: 
                    s.remove(nums[i]-dist)
                    leng += 1
                dist += 1
            dist = 1
            while nums[i] + dist in s:
                if nums[i] + dist in s:
                    s.remove(nums[i]+dist)
                    leng += 1
                dist += 1
                
            maxLen = max(maxLen, leng)

        return maxLen