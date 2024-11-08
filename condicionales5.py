# escribir que numeros son mayores, menores o iguales
Num1 = float(input("Escribir el primer numero: "))
Num2 = float(input("Escribir el segundo numero: "))
Num3 = float(input("Escribir el tercer numero: "))

if Num1 > Num2 and Num1 > Num3:
    print (Num1, "es mayor que ", Num2, " y ", Num3)
elif Num1 < Num2 and Num1 > Num3:
    print (Num2, "es mayor que ", Num1, " y ", Num3)
else:
    print (Num3, "es mayor que ", Num1, " y ", Num2)

if Num1 < Num2 and Num1 < Num3:
    print (Num1, "es menor que ", Num2, " y ", Num3)
elif Num1 > Num2 and Num2 < Num3:
    print (Num2, "es menor que ", Num1, " y ", Num3)
else:
    print (Num3, "es menor que ", Num1, " y ", Num2)

if Num1 == Num2 and Num2 == Num3:
    print ("los 3 numeros son iguales")
elif Num1 == Num2 or Num1 == Num3 or Num2 == Num3:
    print ("solo dos numeros son iguales")
else:
    print ("Ningun numero es igual")
    