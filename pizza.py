import re

# A választék
menu = {
    'pizzák': {
        'margherita': 1000,
        'sonkás': 1200,
        'gombás': 1100,
    },
    'plusz feltétek': {
        'kukorica': 100,
        'hagyma': 150,
        'olívabogyó': 200,
    },
    'italok': {
        'kóla': 300,
        'ásványvíz': 200,
        'narancslé': 250,
    }
}

# Rendelési állomány 
rendeles = {
    'pizzák': [],
    'plusz feltétek': [],
    'italok': [],
    'vegosszeg': 0
}

# Felhasználói interakció és rendelés felvétele
def rendfelvetel():
    print("Assistant: Üdvözlöm! Egy pizza rendelés felvevő Asszisztens vagyok. Mit szeretne rendelni?")

    # Pizza kiválasztása
    while True:
        user_in = input("User: ").lower()

        # Keresés a választékban
        for kategori, elemek in menu.items():
            for elem, ar in elemek.items():
                if re.search(fr'\b{elem}\b', user_in):
                    rendeles[kategori].append(elem)
                    rendeles['vegosszeg'] += ar
                    print(f"Assistant: Hozzáadva a rendeléshez: {elem}")
                    break
            else:
                continue  # Külső for ciklus következő iterációja
            break  # Belső for ciklus megszakítása

        if rendeles['pizzák']:  # Ellenőrizzük, hogy van-e kiválasztott pizza
            break  # Kilépünk a while ciklusból, ha van kiválasztott pizza

    # Feltét kiválasztása /ha van pizza kiválasztva/
    if rendeles['pizzák']:
        for pizza in rendeles['pizzák']:
            valaszt = input(
                f"Assistant: Szeretne plusz feltétet a(z) {pizza} pizzájára? (igen/nem): ").lower()
            if valaszt == "igen":
                print("Assistant: Milyen plusz feltétet szeretne?")
                user_in = input("User: ").lower()
                for elem, ar in menu['plusz feltétek'].items():
                    if re.search(fr'\b{elem}\b', user_in):
                        rendeles['plusz feltétek'].append(elem)
                        rendeles['vegosszeg'] += ar
                        print(f"Assistant: Hozzáadva a rendeléshez: {elem}")

    # Üdítő kiválasztása /ha van pizza kiválasztva/
    if rendeles['pizzák']:
        print("Assistant: Rendben, milyen üdítőt szeretne?")
        while True:
            user_in = input("User: ").lower()

            for elem, ar in menu['italok'].items():
                if re.search(fr'\b{elem}\b', user_in):
                    rendeles['italok'].append(elem)
                    rendeles['vegosszeg'] += ar
                    print(f"Assistant: Hozzáadva a rendeléshez: {elem}")
                    break
            else:
                print("Assistant: Sajnálom, de az adott üdítő nincs a választékban. Kérlek, válassz újat.")
                continue  # Kilépünk a while ciklus jelenlegi iterációjából és újra kérdezzük az üdítőt
            break  # Kilépünk a while ciklusból, ha sikerült választ adni az üdítőre

    # Rendelési állomány kiíratása
    print("Assistant: A rendelési állomány:")
    for kategori, elemek in rendeles.items():
        if kategori != 'vegosszeg' and elemek:
            print(kategori.capitalize() + ":")
            for elem in elemek:
                print(f"- {elem}")
    print("Végösszeg: " + str(rendeles['vegosszeg']) + " Ft")
    print("Assistant: Köszönjük a rendelést!")

    # További rendelés
    valaszt = input("Assistant: Szeretne még valamit rendelni? (igen/nem): ").lower()
    if valaszt == "igen":
        rendfelvetel()
    else:
        print("Rendben, köszönöm, hogy engem választott, ha megelégedett a szolgáltatással kérem alkalmazzon máskor is.")

# Rendelés felvétele
rendfelvetel()