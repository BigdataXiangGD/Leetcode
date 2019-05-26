# 1.reverse the first n - k elements

# 2.reverse the rest of them

# 3.reverse the entire array


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k%length
        self.reverse(nums, 0, length - k -1)
        self.reverse(nums, length - k, length - 1)
        self.reverse(nums, 0, length - 1)
            
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
