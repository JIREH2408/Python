#Mirar si es divisible
N1 = int(input("Primero numero: "))
N2 = int(input("Segundo numero: "))
N3 = int(input("Tercer numero"))

if N1 % N2 == 0 or N1 % N3 == 0:
    print (f"{N1} es divisible por {N2} o {N3}")
else:
    print (f"{N1} no es divisible por {N2} ni por {N3}")
