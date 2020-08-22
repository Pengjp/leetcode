# rotate_array.py
def rotate(nums,k)
    """
    Do not return anything, modify nums in-place instead.
    """
    k = k % len(nums)
    if len(nums) > 1 and  k > 0:
        nums[:] = reversed(nums)
        nums[:k], nums[k:] = reversed(nums[:k]), reversed(nums[k:])