liczba_gosci = int(input("Podaj liczbę gości (łącznie z Tobą): "))
liczba_potraw = int(input("Podaj liczbę zamówionych potraw: "))

suma_cen = 0
licznik = 0

while licznik < liczba_potraw:
    cena = float(input(f"Podaj cenę potrawy {licznik + 1}: "))
    suma_cen += cena
    licznik += 1

srednia_cena = suma_cen / liczba_potraw

koszt_na_osobe = suma_cen / liczba_gosci

print(f"\nŚrednia cena potrawy: {srednia_cena:.2f} zł")
print(f"Koszt na jednego gościa: {koszt_na_osobe:.2f} zł")
