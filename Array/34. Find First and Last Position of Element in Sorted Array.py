class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = r = mid
                while l > 0 and nums[l] == nums[l - 1]:
                    l -= 1
                while r  < len(nums) - 1  and nums[r] == nums[r + 1]:
                    r += 1
                return [l,r]
        return [-1, -1]
