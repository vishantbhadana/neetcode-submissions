class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1]*n
        right = [1]*n

        i = 0
        product_left=1  #[1,2,4,6]
        while i<n:
            left[i] = product_left
            product_left *= nums[i]
            i += 1
        product_right = 1
        i = i-1
        while i>=0:
            right[i] = product_right
            product_right *= nums[i]
            i-=1
        i=0
        result = []
        while i<n:
            result.append(left[i]*right[i])
            i+=1
        return result


