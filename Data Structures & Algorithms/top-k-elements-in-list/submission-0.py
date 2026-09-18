class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        check = {}
        for i in nums:
            check[i] = check.get(i, 0) + 1
        sorted_element = sorted(check, key= lambda num: check[num], reverse=True)
        return sorted_element[:k]

