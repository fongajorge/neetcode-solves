class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()

        for k in range(len(nums)):
            if nums[k] in map:
                return [map[nums[k]], k]

            map[target - nums[k]] = k
        
        return []
        