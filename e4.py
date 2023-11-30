#region Descripció
"""
Alejandro Liébana, Andrea Riba ASIXc1B
M03 UF1
29/11/23
Descripció:
Programa que imprimeix un tauler d’escacs per pantalla.
Un taulell d’escacs comença amb la casella  Blanca i és de mida 8x8 sempre ;-)
Fer servir:
BLANC = "⬜"
NEGRE = "⬛"
BLANCO=" "
NEGRO="██"
"""
#endregion


NEGRO = " "
BLANCO = "██"
MEDIDA = 8

for i in range(MEDIDA):
    for j in range(MEDIDA):
        if (i + j) % 2 == 0:
            print(BLANCO, end=" ")
        else:
            print(NEGRO, end=" ")
    if i <7:
        print()


