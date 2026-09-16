class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = {}
        for i in strs:
            sorted_i = tuple(sorted(i))
            if sorted_i in check:
                check[sorted_i].append(i)
            else:
                check[sorted_i] = [i]
        return [val for val in check.values()]    