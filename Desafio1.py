"""
La matriz va a estar ordenada de la siguiente manera
["Alumno","Materia","Nota","Materia","Nota"...]
Donde:
Alumno es un numero aleatorio de 5 digitos
Materia es un numero creciente que arranca en 100
y nota es un numero aleatorio entre 1 y 10

Aclaración: No entendi bien si por materia va asignada una nota o varias notas. Asi que le asigno una nota como si fuese la nota final
"""
import random
def mostrar_matriz(matriz,estudiantes,materias):
    print("Estudiantes    ","Materia        Nota         "*materias)
    for fil in range(estudiantes):
        for col in range((materias*2)+1):
            print("%3d" % matriz[fil][col],end="           ")
        print()

    return 0

def calcular_promedio_estudiante(matriz):
    print("\nPromedio de estudiantes:\nEstudiantes     Promedio")
    estudiantes=len(matriz)
    materias=len(matriz[0])
    for fil in range(estudiantes):
        prom=0
        for col in range(materias):
            if col==0:
                print(matriz[fil][col],end="           ")
            elif col%2==0:
                prom=prom+matriz[fil][col]
        print("%.2f"%(prom/((materias-1)/2)))


    return 0

def calcular_promedio_materias(matriz):
    print("\nPromedio de materias:\nMateria     Promedio")
    estudiantes=len(matriz)
    materias=len(matriz[0])
    for col in range(materias):
        prom=0
        for fil in range(estudiantes):
            if fil==0 and col%2!=0:
                print(matriz[fil][col], end="         ")
            elif col!=0 and col%2==0:
                prom=prom+matriz[fil][col]
        if prom!=0:
            print("%.2f"%(prom/estudiantes))

n = int(input("Indique el numero de alumnos: "))
m = int(input("Indique el numero de materias: "))   
lista=[]
for fil in range(n):
    lista.append([])
    materia=100
    for col in range(m+1):
        if col==0:
            lista[fil].append(random.randint(10000,99999))
        else:
            lista[fil].append(materia)
            materia+=1
            lista[fil].append(random.randint(1,10))

mostrar_matriz(lista,n,m)
calcular_promedio_estudiante(lista)
calcular_promedio_materias(lista)