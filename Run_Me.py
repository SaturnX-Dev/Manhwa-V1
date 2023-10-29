import subprocess
import shutil

# Función para mostrar el menú
def show_menu():
    while True:
        # Leer el arte ASCII desde un archivo .ans llamado "visual"
        try:
            with open("visual.ans", "r") as file:
                ascii_art = file.read()
        except FileNotFoundError:
            print("Archivo 'visual.ans' no encontrado.")
            return

        # Muestra el arte ASCII centrado
        terminal_width = shutil.get_terminal_size().columns
        for line in ascii_art.splitlines():
            print(line.center(terminal_width))

        # Muestra el mensaje sin centrar
        print("Saturnx-Dev Presenta Script Master V1")
        print("1. Ejecutar 1_Rename_Archives.py")
        print("2. Ejecutar 2_Rename_Folders.py")
        print("3. Ejecutar 3_Move_Archives.py")
        print("4. Ejecutar 4_Mix_Folders.py")
        print("5. Ejecutar 5_Extract_Bad_Folders.py")
        print("6. Ejecutar 6_Test_Not_Use.py")
        print("q. Salir")

        choice = input("Elige una opción: ")
        if choice == 'q':
            break
        elif choice == '1':
            subprocess.Popen(["cmd", "/c", "start", "python", "Archives_V1/1_Rename_Archives.py"], shell=True)
        elif choice == '2':
            subprocess.Popen(["cmd", "/c", "start", "python", "Archives_V1/2_Rename_Folders.py"], shell=True)
        elif choice == '3':
            subprocess.Popen(["cmd", "/c", "start", "python", "Archives_V1/3_Move_Archives.py"], shell=True)
        elif choice == '4':
            subprocess.Popen(["cmd", "/c", "start", "python", "Archives_V1/4_Mix_Folders.py"], shell=True)
        elif choice == '5':
            subprocess.Popen(["cmd", "/c", "start", "python", "Archives_V1/5_Extract_Bad_Folders.py"], shell=True)
        elif choice == '6':
            subprocess.Popen(["cmd", "/c", "start", "python", "Archives_V1/6_Test_Not_Use.py"], shell=True)

if __name__ == "__main__":
    show_menu()