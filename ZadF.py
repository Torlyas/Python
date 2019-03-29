import math
a = input()
a = int(a)
b = math.sqrt(a)
#frac, whole = math.modf(b)
frac = math.modf(b)
print(frac)
if frac == 0:
    print("Liczba A jest kwadratowa a jej pierwiastek wynosi ", end = "")
    print(b)
else:
    print("A nie jest liczba kwadratowa")