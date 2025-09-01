

s = "racecar"
t = "carrace"


def anagram(s, t):
    return sorted(s) == sorted(t)

print(anagram(s,t))
   
