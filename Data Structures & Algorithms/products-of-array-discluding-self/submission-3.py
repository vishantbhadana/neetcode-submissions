class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        product_left = 1
        i = 0

        while i < n:
            result[i] = product_left
            product_left *= nums[i]
            i += 1

        product_right = 1
        i = n - 1

        while i >= 0:
            result[i] *= product_right
            product_right *= nums[i]
            i -= 1

        return result


