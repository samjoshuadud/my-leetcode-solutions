
strs = ["eat","tea","tan","ate","nat","bat"]



def groupAnagrams(strs):
    strs_sorted = []
    strs_counted = {}

    output = []

    for i in strs:
        joined = ''.join(sorted(i))
        strs_sorted.append(joined)
        
        if joined not in strs_counted:
            strs_counted[joined] = [i]
        else:
            strs_counted[joined].append(i)


    for i in strs_counted:
        output.append(strs_counted[i])
    
    return output

print(groupAnagrams(strs))
