# elabore un algoritmo que lea dos notas, les obtenga el promedio y si la nota es mayor o igual a 3.0 inidque si gano o si es mejor a 3.0 indique que perdio

# Inicio

# Declaracion de variables
nota1 = 0.0
nota2 = 0.0
promedio = 0.0

# Entrada de datos
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
promedio = (nota1 + nota2) / 2

# Proceso
if promedio >= 3.0:
    print("Gano")
else:
    print("Perdio") 