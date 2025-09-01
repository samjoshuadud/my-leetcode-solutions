
nums = [4,1,-1,2,-1,2,3]
k = 2

def topFrequent(nums,k):
    c = {}
    for i in sorted(nums):
        if i not in c:
            c[i] = 1
        else:
            c[i] += 1
    
    sorted_c = dict(sorted(c.items(), key=lambda x: x[1], reverse=True))
    
    output = list(sorted_c)[0:k]
    return output

print(topFrequent(nums,k))
