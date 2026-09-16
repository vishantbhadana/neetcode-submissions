class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i in nums:
            if i in dict and dict[i] > 0:
                return True
            dict[i] = 1
        return False