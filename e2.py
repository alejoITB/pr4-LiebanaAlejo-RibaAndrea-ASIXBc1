'''

Andrea Alejandro ASIXBc1 29-11-2023

Programa que mostra un triangle amb nombres a les cantonades.
Cal demanar quina alçada ha de tenir el triangle.
Els valors permesos per a l'alçada son entre 2 i 9. (ambdós inclosos)
INPUT
Alçada del triangle: 5
OUTPUT
1
2 2
3   3
4     4
5 5 5 5 5

'''

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

