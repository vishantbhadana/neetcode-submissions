class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)

        if m>n:
            return ""
        
        need = {}
        
        for c in t:
            need[c] = need.get(c, 0) + 1
        
        unique_needed = len(need)
        unique_count = 0
        min_len = float("inf")
        window = {}
        left = 0
        start = 0

        for right in range(n):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                unique_count+=1

            
            while unique_count == unique_needed:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                left_char = s[left]
                window[left_char] -= 1

                if (left_char in need and
                    window[left_char] < need[left_char]):
                    unique_count -= 1

                left += 1

        if min_len == float("inf"):
            return ""

        return s[start:start + min_len]





        