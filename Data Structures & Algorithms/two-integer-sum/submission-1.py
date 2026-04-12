class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(0, len(nums)):
            if d.get(target - nums[i]) != None:
                return sorted([i, d.get(target - nums[i])])
            else:
                d[nums[i]] = i;
        return [0,0]
