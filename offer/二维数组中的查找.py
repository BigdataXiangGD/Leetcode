#从左下角元素往上查找，右边元素是比这个元素大，上边是的元素比这个元素小。
#于是，target比这个元素小就往上找，比这个元素大就往右找。如果出了边界，则说明二维数组中不存在target元素。
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        rowcount = len(array) - 1
        colcount = len(array[0]) - 1
        i = rowcount
        j = 0
        while j <= colcount and i >= 0:
            if array[i][j] < target:
                j += 1
            elif array[i][j] > target:
                i -= 1
            else:
                return True
        return False
        
