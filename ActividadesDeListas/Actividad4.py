#numeros de la loteria 3,9,12,14,26,45
loteria= []
for i in range(6):
    numero = int(input("ingrese los numeros de la loteria primitiva"))
    loteria.append(numero)
loteria.sort()
print(f"los numeros de la loteria son: {loteria}")


#Segunda solucion
#awarded = []
#for i in range(6):
#    awarded.append(int(input("Introduce un número ganador: ")))
#awarded.sort()
#print("Los números ganadores son " + str(awarded))