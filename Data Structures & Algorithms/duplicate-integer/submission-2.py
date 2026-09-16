class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #always remember while doing some duplicacy problem try to use set always
        check = set()
        for i in nums:
            if i in check:
                return True
            check.add(i)
        return False
