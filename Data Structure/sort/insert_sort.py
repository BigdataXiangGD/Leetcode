'''
直接插入排序的核心思想就是：将数组中的所有元素依次跟前面已经排好的元素相比较，如果选择的元素比已排序的元素小，则交换，直到全部元素都比较过。
因此，直接插入排序可以用两个循环完成：

第一层循环：遍历待比较的所有数组元素
第二层循环：交换


时间复杂度为O(n^2)    空间O(1)   稳定
'''









def insert_sort(array):
    for i in range(0,len(array)):
        key = array[i]
        j = i -1
        while j>= 0:
            if array[j] > key:
                array[j+1] = array[j]
                array[j] = key
            j -= 1
    return array

print(insert_sort(array = [3,4,6,2,54,77,24,56,545,56,4,7,8,67]))
