#calculo por estudiante
Nombre = (input("Nombre del estudiante: "))
N1 = float(input("Ingresar la nota numero 1: "))
N2 = float(input("ingresar la nota numero 2: "))
N3 = float(input("ingresar la nota numero 3: "))

promedio = (N1 + N2 + N3) /3
print ("Nombre", Nombre)
print ("La nota final del estudiante es: ", round (promedio,1))

mpromedio = 3.0
resultado = "Aprobado" if promedio >= mpromedio else "Reprobado"
print("El eatudiante fue: ", resultado)