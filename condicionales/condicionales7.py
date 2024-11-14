Nombre = (input("Nombre: "))
Edad = (input("Edad: "))
Sexo = (input("Sexo (Masculino/Femenino): "))
Estadocivil = (input("Estado civil (Soltero/Casado): "))

if Sexo == "Masculino" and Estadocivil == "casado" and Edad > 40:
    print (Nombre, "Hombre mayor de 40 años y casado")
elif Sexo == "Femenino" and Estadocivil == "soltero" and Edad < 50:
    print (Nombre, "mujer menor de 50 años soltera")
else:
    print (Nombre, "No esta en los seleccionados: ")

