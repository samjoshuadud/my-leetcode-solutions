
input = ["neet","code","love","you"]

def encode(strs):
    output = []
    for i in strs:
        length = len(i)
        output.append(f"{length}#{i}")
    return "".join(output)

def decode(strs):
    output = []
    indicator = '#'
    i = 0
    while i < len(strs):
        num = strs.find(indicator, i)
        dig = int(strs[i:num])
        sliced = strs[num+1:(num+1)+dig]
        
        output.append(sliced)
        i = num + 1 + dig
    return output
print(decode(encode(input)))
