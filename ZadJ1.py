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
        if el<1 or el>9:
            correct = False
    if len(tab) == n and correct:
        minEl = 0
        minLiczba = 1000
        maxEl = 0
        maxLiczba = 0
        for el in tab:
            if tab.count(el) < minLiczba:
                minLiczba = tab.count(el)
                minEl = el
            if tab.count(el) > maxLiczba:
                maxLiczba = tab.count(el)
                maxEl = el
        print(minEl)
        print(maxEl)
    else:
        print("Zla ilosc elementow lub nie odpowiednia liczba")
else:
    print("Zle n")

