import math
print("Wpisz n")
n = input()
n = int(n)
if n <= 100 and n > 0:
    tab = []
    print("Wpisz tablice")
    l = input()
    tab = l.split()
    correct = True
    for el in tab:
        el = int(el)
        if el<0 or el>10:
            correct = False
    if len(tab) == n and correct:
        bloczek = []
        bloki = []
        index = 0
        while index < n-1:
            if tab[index] == tab[index + 1]:
                same = True
                while same:
                    bloczek.append(tab[index])
                    if index < n-1:
                        if tab[index] != tab[index+1]:
                            same = False
                        index+=1
                index+=1
            else:
                index+=1 #index = index+1
            if len(bloczek) != 0:
                bloki.append(bloczek)
                print(bloczek)
                print(bloki)
                bloczek.clear()
        print(bloki)
    else:
        print("Zla ilosc elementow lub nie odpowiednia liczba")
else:
    print("Zle n")

