class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0]*n
        right = [0]*n

        tallest = 0
        for i in range(n):
            tallest = max(tallest, height[i])   # [ 0,2,2,3,3,3,3,3,3,3]
            left[i] = tallest
        
        tallest = 0
        for i in range(n-1, -1, -1):        # [3,3,3,3,3,3,3,3,2,1]
            tallest = max(tallest, height[i])
            right[i] = tallest
        
        water_max=0

        for i in range(n):
            water = min(left[i], right[i]) - height[i]
            water_max+=water
        
        return water_max
        

