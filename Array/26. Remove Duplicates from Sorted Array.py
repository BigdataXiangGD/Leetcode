class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        j = 0 #下指针
        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                nums[j + 1] = nums[i]
                j += 1
        return j + 1

    
    
    #Time O（n）; Space O(1)
    #遍历列表，以nums[0]为基准，下标指针j为0，逐一与后面元素比较找出不等元素，将不等元素放到第二个元素的位置nums[1]，j+1
