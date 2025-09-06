
input = [1,2,3,4]

def productExceptSelf(nums):
    answers = []
    for i in range(len(nums)):
        if i == 0: 
            answers.append(1)
        else:
            answers.append(nums[i-1]*answers[i-1])
    
    postfix = 1
    for i in range(len(nums)-1, -1, -1):
        answers[i] *= postfix
        postfix *= nums[i]
    return answers
print(productExceptSelf(input))
