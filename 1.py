paliwo = 100
paliwo_zużyte_na_s = 10
czas = 0

while paliwo > 0:
    print(f"Jednostki paliwa: {paliwo} L | Czas lotu: {czas} s")
    paliwo -= paliwo_zużyte_na_s
    czas += 1

print("Koniec lotu.")