liczby_pierwsze = []  #
liczba = 2

while len(liczby_pierwsze) < 10:

    czy_pierwsza = True
    for dzielnik in range(2, int(liczba ** 0.5) + 1):
        if liczba % dzielnik == 0:
            czy_pierwsza = False
            break

    if czy_pierwsza:
        liczby_pierwsze.append(liczba)

    liczba += 1

print(",".join(map(str, liczby_pierwsze)))
