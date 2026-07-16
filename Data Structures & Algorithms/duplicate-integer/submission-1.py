class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)

        for c in count.values():
            if c > 1:
                return True
        
        return False