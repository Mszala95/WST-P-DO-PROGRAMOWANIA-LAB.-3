#1
imie = input("Podaj swoje imię: ")
print(f"Witaj {imie}!")

#2
wiek = input("Podaj swój wiek: ")
print(f"Twój wiek to: {wiek}")

#3
nazwisko = input("Podaj swoje nazwisko: ")

inicjaly = f"{imie[0].upper()}.{nazwisko[0].upper()}."
print(f"Twoje inicjały to: {inicjaly}")

#4
lancuch = input("Napisz coś: ")

for _ in range(5):
    print(lancuch)

#5
lancuch1 = input("Podaj pierwszy tekst: ")
lancuch2 = input("Podaj drugi tekst: ")

polaczony = lancuch1 + lancuch2
print(f"Połączony tekst: {polaczony}")

#6
lancuch1 = input("Podaj pierwszy tekst: ")
lancuch2 = input("Podaj drugi tekst: ")

polowa1 = lancuch1[:len(lancuch1) // 2]
polowa2 = lancuch2[:len(lancuch2) // 2]

polaczony = polowa1 + polowa2
print(f"Połączony tekst z połówek: {polaczony}")


