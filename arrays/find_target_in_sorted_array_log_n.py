def searchPlace(nums, target, ptr, length):
    half1 = length // 2
    half2 = length - half1
    new_ptr = ptr + half1

    if length == 1:
        if nums[ptr] == target:
            return ptr
        elif nums[ptr] < target:
            return ptr + 1
        else:
            return ptr - 1

    if target < nums[new_ptr]:
        return searchPlace(nums, target, ptr, half1)
    else:
        return searchPlace(nums, target, new_ptr, half2)

def searchInsert(nums, target):
    return searchPlace(nums, target, 0, len(nums))


nums = [1, 3, 5, 6]
target = 7
print(searchInsert(nums, target))
