
input = ["neet","code","love","you"]

def encode(strs):
    output = []
    for i in strs:
        length = len(i)
        output.append(f"{length}#{i}")
    return "".join(output)

def decode(strs):
    output = []
    j = 0

    for i in range(len(strs)-1):
       pass
        # BUKAS NALANG
print(decode(encode(input)))
