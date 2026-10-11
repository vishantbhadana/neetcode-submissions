class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        count = {}

        for right in range(len(s2)):
            c = s2[right]
            count[c] = count.get(c, 0) + 1

            if right - left + 1 > len(s1):
                old = s2[left]
                count[old] -= 1
                if count[old] == 0:
                    del count[old]
                left += 1

            if right - left + 1 == len(s1):
                if count ==dict(Counter(s1)):
                    return True

        return False

        