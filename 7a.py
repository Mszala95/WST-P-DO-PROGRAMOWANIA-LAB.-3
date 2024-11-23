n = int(input("Podaj liczbę studentów w grupie: "))

suma_punktow = 0
licznik_studentow = 0

while licznik_studentow < n:
    punkty = float(input(f"Podaj liczbę punktów dla studenta {licznik_studentow + 1}: "))
    if punkty < 0 or punkty > 100:
        print("Liczba punktów poza przedziałem 0-100. Pomijanie...")
        continue
    suma_punktow += punkty
    licznik_studentow += 1

srednia = suma_punktow / n
print(f"Średnia liczba punktów w grupie: {srednia:.2f}")
