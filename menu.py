import subprocess

def mostrar_menu():
    print("Selecciona una opción:")
    print("1. Ejecutar voztexto.py")
    print("2. Ejecutar word.py")
    print("3. Ejecutar sentimientos.py")
    print("4. Ejecutar chunk_1.py")
    print("5. Ejecutar analisisword.py")
    print("6. Ejecutar  graba-audio-texto.py")
    print("7. para salir")

def ejecutar_programa(opcion):
    if opcion == 1:
        subprocess.run(["python", "vozytexto.py"])
    elif opcion == 2:
        subprocess.run(["python", "word.py"])
    elif opcion == 3:
        subprocess.run(["python", "sentimientos.py"])
    elif opcion == 4:
        subprocess.run(["python", "chunk_1.py"])
    elif opcion == 5:
        subprocess.run(["python", "analisisword.py"])
    elif opcion == 6:
        subprocess.run(["python", "graba-audio-texto.py"])
    elif opcion == 7:
        print("Saliendo...")
        exit()
    else:
        print("Opción no válida. Por favor, selecciona una opción del 1 al 7.")

def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Introduce el número de la opción deseada: "))
            ejecutar_programa(opcion)
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número.")

if __name__ == "__main__":
    main()
