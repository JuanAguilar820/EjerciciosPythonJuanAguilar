#Ejercicio extra
Nombre_estudiante=(input("ingrresa el nombre del estudiante: "))
Promedio_de_notas=float(input("ingrese sus calificaciones:  "))
proyecto=float(input("ingresa tu calificacion de proyecto: "))
parciales=float(input("ingresa la nota de parciales:" ))

p1= Promedio_de_notas * 0.3
p2= proyecto * 0.2
p3=parciales * 0.5
suma= p1+p2+p3

print (f"El estudiante", Nombre_estudiante, "tiene una nota final de", suma)


