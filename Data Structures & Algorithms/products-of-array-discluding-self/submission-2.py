class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zerocnt = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zerocnt += 1
                if zerocnt == 2:
                    return [0] * len(nums)
                continue
            prod *= nums[i]
        
        res = [prod] * len(nums)
        for i in range(len(nums)):
            if zerocnt == 0:
                res[i] = int(res[i] / nums[i])
            elif nums[i] == 0:
                res[i] = prod
            else:
                res[i] = 0

        return res               
            