

nums = [1,2,3,1]
def containsDuplicate(nums):
    s = sorted(nums)
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
        return False
print(containsDuplicate(nums))

            
