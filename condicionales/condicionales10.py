#Nota final del estudiante

N1 = float(input("Primera nota: "))
N2 = float(input("Segunda nota: "))
N3 = float(input("Tercera nota: "))

if N1 >= 3.0 and N2 >= 3.0 and N3 < 3.0:
    notamayor = (N1 + N2) / 2 
    print ("La nota final es: ", notamayor)
elif N1 >= 3.0 and N2 < 3.0 and N3 >= 3.0:
    notamayor = (N1 + N3) / 2
    print ("La nota final es: ", notamayor)
else:
    notamayor = (N2 + N3) / 2
    print ("La nota final es: ", notamayor)
    