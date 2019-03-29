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
        m = 0
        licznik = 0
        for i in range(1, len(tab)):
            if tab[i] == tab[i-1]:
                licznik += 1
                if licznik > m:
                    m = licznik
            else:
                licznik = 0
        m += 1
        print(m)
    else:
        print("Zla ilosc elementow lub nie odpowiednia liczba")
else:
    print("Zle n")

