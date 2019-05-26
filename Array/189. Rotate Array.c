

void rotate(int* nums, int numsSize, int k){
    k = k%numsSize;
    reverse(nums, 0, numsSize - k - 1);
    reverse(nums, numsSize - k, numsSize - 1);
    reverse(nums, 0, numsSize -1);

}

void reverse(int* nums, int start, int end){
    int temp;
    while(start < end){
        #nums[start], nums[end] = nums[end], nums[start];
        temp = nums[start];
        nums[start] = nums[end];
        nums[end] = temp;
        start = start + 1;
        end = end - 1;
    }
}
