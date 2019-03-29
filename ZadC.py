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
        #print(tab)
        index = 0
        k = 0 #liczba wystapien elementu najczesciej
        for element in tab:
            #zliczanie wystapien
            if tab.count(element) > k:
                k = tab.count(element)
                najwiekszy = element
        print("Najczestszy element")
        print("wartosc liczby: ", end = "")
        print(najwiekszy)
        print("ilosc wystapien: ", end = "")
        print(k)
    else:
        print("Zla ilosc elementow lub nie odpowiednia liczba")
else:
    print("Zle n")

