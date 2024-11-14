#de menor a mayor
A = int(input("Pirmer numero: "))
B = int(input("Segundo numero: "))
C = int(input("Tercer numero: "))

if A > B and A > C:
    if B > C:
        print(C, B, A)
    else:
        print(B, C, A)
elif B > A and B > C:
    if A > C:
        print(C, A, B)
else:
    print(A, C, B)
    
    
