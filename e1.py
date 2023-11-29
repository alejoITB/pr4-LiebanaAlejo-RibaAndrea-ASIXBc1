"""
Andrea Alejandro ASIXBc1 29-11-2023

Programa que demana a l'usuari la introducció de 10 nombres sencers
(que també podrien ser 10000000 😱😳😈)
i ha de mostrar, al final i per pantalla, quants són positius, quants negatius i quants zero.
"""
count0 = 0
countPOS = 0
countNEG = 0
num = 0
try:
    for i in range(10):
        num = int(input("Dame un número: "))
        if num == 0:
            count0 +=1
        elif num >0:
            countPOS += 1
        else:
            countNEG +=1

    print(f" Hay {countPOS} números positivos, {countNEG} números negativos y {count0} zeros")
except:
    print("ERROR.")