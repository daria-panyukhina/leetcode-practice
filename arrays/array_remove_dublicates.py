def removeDuplicates(nums):
    ptr = 1
    i = 1
    while i < len(nums):
        if nums[i] != nums[i - 1]:
            nums[ptr] = nums[i]
            ptr += 1
        i += 1
    print(nums)
    return ptr


def removeElement(nums, val):
    ptr = 0
    i = 0
    while i < len(nums):
        if nums[i] != val:
            nums[ptr] = nums[i]
            ptr += 1
        i += 1
    print(nums)
    return ptr


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# nums1 = [1, 1, 2]
nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
# print(removeDuplicates(nums))
print(removeElement(nums2, val))
