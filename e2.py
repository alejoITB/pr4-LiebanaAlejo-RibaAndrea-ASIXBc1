#region Descripció
"""
Alejandro Liébana, Andrea Riba ASIXc1B
M03 UF1
29/11/23
Descripció:
Programa que mostra un triangle amb nombres a les cantonades.
Cal demanar quina alçada ha de tenir el triangle.
Els valors permesos per a l'alçada son entre 2 i 9. (ambdós inclosos)
"""
#endregion


try:
    altura = int(input("Qué altura tiene el triangulo? (Entre 2 y 9) "))
    if altura >= 2 and altura <= 9:
        for i in range(1, altura+1):
            for j in range(1, i+1):
                if j == 1 or j == i or i == altura:
                    print(i, end="")
                else:
                    print(" ", end="")
            print("")
    else:
        print("Tiene que estar entre 2 y 9")


except:
    print("ERROR.")

