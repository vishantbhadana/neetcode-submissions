class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        check = Counter(nums)
        buckets = [ [] for i in range(len(nums)+1)]
        for num, count in check.items():
            buckets[count].append(num)
        result = []

        for i in range(len(nums), 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result)==k:
                    return result

