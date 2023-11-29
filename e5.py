'''
Alejandro Andrea 29-11-2023
Programa que realitza la multiplicació, de dos nombres sencers,  mitjançant sumes
'''
try:
    num1 = int(input("Dame el primer número: "))
    num2 = int(input("Dame el segundo número: "))
    resultado = 0
    for i in range(num2):
        resultado += num1

    print(f"Resultado: {resultado}")

except:
    print("ERROR, introduce un número válido")
