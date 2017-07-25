# Factorial

zmienna = input('podaj numer: ')
if zmienna != 0:
    for i in range(1, zmienna):
        zmienna *= i
else:
    zmienna = 0
print zmienna
