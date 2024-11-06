#planilla del empleado
nombre = (input("Nombre del empleado: "))
horas = int(input("Escribir cantidad de horas laboradas: "))
valor = int(input("Escribir el valor de la hora laboral: "))
PagoTotal = horas*valor

print("Nombre del empelados: ", nombre)
print("Total a pagar: ", PagoTotal)
