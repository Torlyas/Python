import math
n = input()
n = int(n)
if n <= 100 and n > 0:
    tab = []
    l = input()
    tab = l.split()
    correct = True
    for el in tab:
        el = int(el)
        if el<0 or el>10:
            correct = False
    przywilej = False
    if len(tab) == n and correct:
        for el in tab:
            x = tab.count(el)
            if x >= n/2+1:
                przywilej = True
        print(przywilej)
    else:
        print("Zla ilosc elementow lub nie odpowiednia liczba")
else:
    print("Zle n")

