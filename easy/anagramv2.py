
s = "anagram"
s_counts = {}
t = "marganas"
t_counts = {}

for char in s:
    if char in s_counts:
        s_counts[char] += 1
    else:
        s_counts[char] = 1

for char in t:
    if char in t_counts:
        t_counts[char] += 1
    else:
        t_counts[char] = 1

print(s_counts == t_counts)
