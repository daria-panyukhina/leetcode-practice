def twoSum_1(nums, target):
    for i in range(len(nums) - 1):
        for j in range((i + 1), len(nums)):
            if nums[i] + nums[j] == target:
                return i, j


def twoSum_2(nums, target):
    nums_dict = dict()
    for i in range(len(nums)):
        x = nums[i]
        if target - x in nums_dict:
            return nums_dict[target - x], i
        nums_dict[x] = i
    return 'No sollution'


nums = [int(x) for x in input('Input numbers: ').split()]
target = int(input('Input target sum: '))

print(twoSum_1(nums, target))
print(twoSum_2(nums, target))
