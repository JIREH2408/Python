
Longitud = float(input("Longitud de la varilla: "))
Diametro = float(input("Diametro de la varilla: "))

Masa = (Diametro * Longitud) / 3.5
if Longitud > 7.5 and Longitud <= 9 and Diametro <= 0.5 and Diametro <= 1.3 and Masa <= 5.8:
    print ("Es valida")
elif Longitud > 7.5 and Longitud <= 9 and Diametro >= 0.5 and Diametro <= 1.3 and Masa > 5.8:
    print ("No es valida ya que tiene mas masa de la permitida")
elif Longitud <= 7.5 or Longitud > 9:
    print ("No es valida porque la longitud es incorrecta")
else:
    print ("No es valida ya que el diametro es incorrecto")
    