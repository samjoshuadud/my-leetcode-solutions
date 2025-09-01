
nums = [1,2,3,1]
def containsDuplicate(nums):
    s = set()
    for i in nums:
        s.add(i)

    return len(nums) != len(s)
