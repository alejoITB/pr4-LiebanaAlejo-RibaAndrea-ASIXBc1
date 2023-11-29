'''
Andrea Alejandro ASIXBc1 29-11-2023

Programa que imprimeix un tauler d’escacs per pantalla.
Un taulell d’escacs comença amb la casella  Blanca i és de mida 8x8 sempre ;-)
Fer servir:
BLANC = "⬜"
NEGRE = "⬛"
BLANCO=" "
NEGRO="██"
'''

NEGRO = "  "
BLANCO = "██"

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print(BLANCO, end="")
        else:
            print(NEGRO, end="")
    if i <7:
        print()


