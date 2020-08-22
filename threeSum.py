# threeSum.py
nums = [0,0,0,0,0]
def threeSum(nums):
    nums.sort()
    ans=[]
    for fixed in range(len(nums) - 2):
        if nums[fixed] > 0:
            break
        if fixed > 0 and nums[fixed] == nums[fixed - 1]:
            continue
        left = fixed + 1
        right = len(nums) - 1
        while left < right:
            if nums[fixed] + nums[left] + nums[right] == 0:
                ans.append([nums[fixed],nums[left],nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
            if nums[fixed] + nums[left] + nums[right] > 0:
                right -= 1
            else:
                left += 1
    return ans