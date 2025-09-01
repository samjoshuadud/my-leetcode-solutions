
nums = [3, 3, 11, 15]
target = 6

def twoSum(nums, target):
    seen = {}
    for i in range(len(nums)):
        # 3
        complacent = target - nums[i]
        if complacent not in seen:
            seen[nums[i]] = i
        else:
            return [seen[complacent], i]
        
print(twoSum(nums, target))
