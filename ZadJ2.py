import math
p = input()
d = len(p)/2
d = int(d)
#print(d)
j = len(p)-1
j = int(j)
palindrom = True
for i in range(0, d):
    if p[i] != p[j]:
        palindrom = False
    j -= 1
print(palindrom)