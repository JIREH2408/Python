#Sueldo de un trabajador
Salario = float(input("ingrese el sueldo del trabajador: "))

if 300000 > Salario:
    aumento = Salario * 0.15 
    Asueldo = Salario + aumento
    print ("El sueldo del trabajador con el aumento es: ", Asueldo)
else:
    print("El trabajador no tiene aumento de sueldo")
