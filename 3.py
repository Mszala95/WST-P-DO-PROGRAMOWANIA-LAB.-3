ulice = ["Jagodowa", "Lipowa", "Kwiatowa", "Kasztanowa", "Polna"]

for ulica in ulice:
    for blok in range(1, 6):  # Bloki od 1 do 5
        for lokal in range(1, 11):  # Lokale od 1 do 10
            print(f"Ulica {ulica}, blok {blok}, lokal {lokal}")
