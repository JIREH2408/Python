#formula cuadratica o general
V1 = int(input("Valor de A: "))
V2 = int(input("Valor de B: "))
V3 = int(input("Valor de C: "))

VF = (V2 * V2) - (4 * V1 * V3)
if VF < 0:
    print("la ecuacion no tiene solucion real")
else:
    P1 = (-V2 + math.sqrt (VF)) / (2 * V1)
    P2 = (-V2 - math.sqrt (VF)) / (2 * V1)
    print ("Las soluciones reales de la ecuación son: P1 = ", P1, "y P2 = ", P2)
    