def containsDuplicate(nums):
    for i in range(0, len(nums)):
        for j in range(1, len(nums)):
            if nums[i+1] == nums[j]:
                return True
            else:
                return False
        return False
nums = [1,2,3,4]
print(containsDuplicate(nums))
