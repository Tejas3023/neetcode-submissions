class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = {}
        for i in range(len(nums)):
            counts[nums[i]] = 1+counts.get(nums[i],0)
            
        for value in counts.values():
            if value > 1:
                return True
        return False