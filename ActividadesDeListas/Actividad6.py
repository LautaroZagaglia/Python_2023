"""Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
pregunte al usuario la nota que ha sacado en cada asignatura y elimine de 
la lista las asignaturas aprobadas. Al final el programa debe mostrar por 
pantalla las asignaturas que el usuario tiene que repetir."""

materias = ["Matematicas","Lengua","Historia","Quimica","Fisica"]
materias_Desaprobadas = []
for aux in materias:
    nota=int(input(f"Que nota sacaste en {aux}? "))
    if nota < 5:
        materias_Desaprobadas.append(aux)
        materias.remove(aux)
        print("la materia "+ aux +" se agrego a materias desaprobadas")
    else:
        print("Felicidades aprobaste "+ aux)
print("materias desaprobadas")
for aux in materias_Desaprobadas:
    print(aux , end=", ")
print(f"Lista de materias {materias}")


#solucion 2
subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for i in range(len(subjects)-1, -1, -1):
    score = float(input("¿Qué nota has sacado en " + subjects[i] + "?"))
    if score >= 5:
        subjects.pop(i)
print("Tienes que repetir " + str(subjects))