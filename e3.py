#region Descripció
"""
Alejandro Liébana, Andrea Riba ASIXc1B
M03 UF1
29/11/23
Descripció:
Programa que mostra per pantalla la suma de tots els nombres senars
 i de tots els nombres parells inferiors a un número límit,
 que l’usuari introdueix per teclat.
Ex: 	si el límit és 31 sumaParells 240 i sumaSenars 225
si el límit és 54 sumaParells 702 i sumaSenars 729
"""
#endregion

numero = int(input("Dame un numero y te sumo los pares y los inpares: "))
pares = 0
inpares = 0
try:
    for i in range(numero):
        if i % 2 == 0:
            pares += i
        else:
            inpares += i
    print(f"Los numeros pares suman {pares}, los números inpares suman {inpares}, has introducido {numero}")

except:
    print("ERROR. Introduce un número válido.")


