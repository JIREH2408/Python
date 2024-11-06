
Num1 = int(input("Escribir el primer numero: "))
Num2 = int(input("Escribir el segundo numero: "))
Num3 = int(input("Escrinir el tercer numero: "))

if Num1 > Num2 and Num1 < Num3:
    medio = Num1 
    print("Numero medio: ", medio)
elif Num2 > Num1 and Num2 < Num3:
    medio = Num2
    print ("Numero medio: ",medio)
else:
    medio = Num3
    print ("Numero medio: ", medio)