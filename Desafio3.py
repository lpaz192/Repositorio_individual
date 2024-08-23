"""
Manejo de matriz de libros
"Id" "Nombre" "Autor" "Genero" "Estado"

Id = numero de 5 digitos
Nombre = array de maximo 20 caracteres
Autor = array de maximo 20 caracteres
Genero = Array de maximo 20 caracteres
Estado = 1=disponible
         -1=alquilado
"""

# Funciones

# Funciones CRUD
def agregar(matriz):
    aux=0
    matriz.append([])
    for i in range(len(matriz[0])):
        aux=input()
        matriz[3].append(aux)
    return matriz

def leer(matriz):
    print(matriz)
"""
def modificar(matriz):

def eliminar(matriz):

"""




# Main
matriz = [
    [84325, "Harry Potter", "J. K. Rowling", "Fantasia", -1],
    [45742, "Habitos Atomicos", "James Clear", "Autoayuda", 1],
    [37483, "La Republica",    "Platon",      "Filosofia", 1]
]

menu=0
while menu!=-1:
    print("*************Menú******************\n")
    print("1. Para agregar datos")
    print("2. Para leer los datos")
    print("3. Para modificar los datos")
    print("4. Para eliminar datos\n")
    print("***********************************\n")
    menu=int(input("Ingrese el numero de la tarea deseada. En caso de querer finalizar ingrese -1: ")) 
    if menu==1:
        matriz = agregar(matriz)
    elif menu==2:
        leer(matriz)
    """
    elif menu == 3:
        modificar(matriz)
    elif menu==4:
        matriz = eliminar(matriz)
    """
    