import os

#Definir variables
libros = {}
SKU = {}

titulo = ()
autor = ()
fecha = ()

#1.Registrar datos de libros
def registrar_libro():
    titulo = ("Ingrese el título del libro: ")
    autor = print("Ingrese el autor del libro: ")
    fecha = print("Ingrese el año de publicacción del libro: ")
    SKU = print("Ingrese el SKU del libro: ")

#2.Prestar libro
def prestar_libro():
    nombre_usuario = input("Ingrese el nombre del usuario: .")
    SKU = print("Ingrese el SKU del libro: .")

#Validar que el libro exista y que no este ya prestado
if prestar_libro in SKU:
    print("El libro se puede prestar")
else:
    print("El libro ya esta prestado")
    SKU = False
    exit

#3.Listar todos los libros
if titulo and autor and fecha and SKU:
    libros[registrar_libro]={"Titulo":titulo, "Autor":autor, "Año de publicación":fecha, "SKU":SKU}
    print("Libro registrado exitósamente.")
else:
    print("Por favor ingrese todos los datos.")

def listar_libros():
    print("Título\t Autor\t Fecha\t SKU")
    for titulo, datos in libros.items():
        print(f"{titulo}\t {datos['Autor']}\t {datos['Año de publicación']}\t {datos['SKU']}")

#4.Imprimir reporte de préstamos
def imprimir_reporte(titulo=None):
    if titulo:
        filtered_libros = {titulo: datos for titulo, datos in libros.items() if datos ["Título"]==titulo}
    else:
        filtered_libros = libros

#Pasar a un archivo de texto
    with open(f"planilla_{libros}.txt", "w") as file:
        file.write (f"Titulo\t Autor\t Año de publicación\t SKU\n")
        for libros, datos in filtered_libros.items():
            file.write(f"{titulo}\t {datos['Autor']}\t {datos['Año de publicación']}\t {datos['SKU']}")

#Menú principal 
def main():
    while True:
        print("\n 1.Registrar libro\n 2.Prestar libro\n 3.Listar todos los libros\n 4. Imprimir reporte de préstamos\n 5. Salir del programa ")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_libro()
        elif opcion == "2":
            prestar_libro()
        elif opcion == "3":
            listar_libros()
        elif opcion == "4":
            imprimir_reporte(libros)
        elif opcion == "5":
            print("Saliendo del programa...")
            exit

if __name__ == "__main__":
    main()
            
