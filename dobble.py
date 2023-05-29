import sys
import itertools

def dobble_deckgen(n):
    """
    General egy dobble decket a megadott merettel
        n (int): Deck merete.
    Visszateresi ertek egz lista a legeneralt dobble deckkel
    """
    if n < 2:
        raise ValueError("A Dobble pakli legalább 2 különböző ábrát tartalmazhat.")

    symbol= list(range(1, n + 1))
    deck= []

    for i in range(n):
        card= [symbol[i]] + [symbol[j] + n for j in range(n - 1)]
        deck.append(card)

    for i in range(1, n):
        card= [symbol[0] + n * i] + [symbol[j] + n * (i - 1) for j in range(1, n)]
        deck.append(card)

    return deck

def dobble_deckpri(deck):
    for card in deck:
        print(" ".join(str(num) for num in card))

# Paraméter beolvasása
if len(sys.argv) != 2:
    print("Használat: python dobble.py <n>")
    print("Ahol <n> a Dobble pakli mérete.")
    sys.exit(1)

n= int(sys.argv[1])

# Dobble pakli generálása
try:
    deck= dobble_deckgen(n)
    dobble_deckpri(deck)
except ValueError as e:
    print(e)
    sys.exit(1)