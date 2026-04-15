class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = set()
        for i in range(len(nums) - 2):
            l =  i + 1
            r = len(nums)-1
            while l < r:
                SumOfThree = nums[l] + nums[r] + nums[i]
                if SumOfThree < 0:
                    l += 1
                elif SumOfThree > 0:
                    r -= 1
                else:
                    res.add(tuple(sorted([nums[l],nums[r],nums[i]])))
                    l += 1
                    r -= 1
        return list(res)
