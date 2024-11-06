#promedio de los partidos
pGanado = int(input("Escribir cantidad de partidos ganados "))
pPerdido = int(input("Escribir cantidad de partidos perdidos "))
pEmpatado = int(input("Escribir cantidad de partifdos empatados "))

pGanado = pGanado*3
pPerdido = pPerdido*0
pEmpatado = pEmpatado*1
Promedio = pGanado + pPerdido + pEmpatado

print("Puntos por partidos ganados: ", pGanado)
print("puntos por partidos perdidos: ", pPerdido)
print("puntos por partidos empatados: ", pEmpatado)
print ("El puntaje por numero de partidos jugados es: ", Promedio)
