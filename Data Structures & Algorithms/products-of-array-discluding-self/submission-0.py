class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1] * len(nums)
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if i == j:
                    continue
                arr[i] *= nums[j]
        
        return arr
