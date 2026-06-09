class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for num in range(len(nums)):
            search = target - nums[num]
            if search in hash:
                return [hash[search],num]
            else:
                hash[nums[num]] = num
        
        