class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # left = 0
        # count = {}

        # for right in range(len(s2)):
        #     c = s2[right]
        #     count[c] = count.get(c, 0) + 1

        #     if right - left + 1 > len(s1):
        #         old = s2[left]
        #         count[old] -= 1
        #         if count[old] == 0:
        #             del count[old]
        #         left += 1

        #     if right - left + 1 == len(s1):
        #         if count == dict(Counter(s1)):
        #             return True

        # return False
        n, m = len(s1), len(s2)

        count1 = [0]*26
        count2 = [0]*26

        if n>m:
            return False

        for i in range(n):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
        
        if count1==count2:
            return True
        
        for right in range(n, m):
            count2[ord(s2[right]) - ord('a')] +=1
            count2[ord(s2[right-n]) - ord('a')] -=1

            if count1==count2:
                return True
        
        return False


        