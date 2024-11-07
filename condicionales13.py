#Nota final
N1 = float(input("Primera nota: "))
N2 = float(input("Segunda nota: "))
N3 = float(input("Tercera nota: "))

if N1 >= 100 and N2 >= 100 and N3 >= 100:
    print ("Aprobado")
elif N1 < 100 or N2 < 100 or N3 >= 100:
    print ("Reprobo")
elif N1 < 100 or N2 >= 100 or N3 < 100:
    print ("Reprobo")
else:
    print ("Reprobo")
    