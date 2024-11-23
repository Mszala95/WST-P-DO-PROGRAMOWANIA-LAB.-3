while True:
    liczba = int(input("Podaj liczbę całkowitą (liczba ujemna kończy działanie): "))
    if liczba < 0:
        print("Podano liczbę ujemną. Koniec pętli.")
        break
    print(f"Podano liczbę: {liczba}")
