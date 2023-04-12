numeros= []
for aux in range(10):
    numeros.append(int(input("ingrese numeros del 1 al 10: ")))
numeros.sort(reverse=True)
for i in range(1, 11):
    print(i , end=", ")

#otra solucion
#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#for i in range(1, 11):
#    print(numbers[-i], end=", ")


#otra solucion
#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#numbers.reverse()
#for number in numbers:
#    print(number, end=", ")
