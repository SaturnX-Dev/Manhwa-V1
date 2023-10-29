import subprocess
import os
from colorama import Fore, Back, Style, init
import time

# Inicializa colorama
init(autoreset=True)

# Función para cargar y mostrar la representación visual desde el archivo ANSI
def load_and_show_visual():
    visual_path = "visual.ans"  # Cambia esto al nombre y extensión de tu archivo ANSI
    if os.path.isfile(visual_path):
        with open(visual_path, "r", encoding="utf8") as visual_file:
            visual_content = visual_file.read()
            print(Back.BLACK + Fore.CYAN + visual_content)
    else:
        print("Archivo visual no encontrado.")

# Función para mostrar el menú con colores arcoíris
def show_menu():
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    while True:
        load_and_show_visual()  # Muestra la representación visual
        print(Back.BLACK + Fore.WHITE + Style.BRIGHT + "Menú:")
        print(Back.BLACK + Fore.WHITE + Style.BRIGHT + "1. Ejecutar 1_Rename_Archives.py")
        print(Back.BLACK + Fore.WHITE + Style.BRIGHT + "2. Ejecutar 2_Rename_Folders.py")
        print(Back.BLACK + Fore.WHITE + Style.BRIGHT + "3. Ejecutar 3_Move_Archives.py")
        print(Back.BLACK + Fore.WHITE + Style.BRIGHT + "4. Ejecutar 4_Mix_Folders.py")
        print(Back.BLACK + Fore.WHITE + Style.BRIGHT + "5. Ejecutar 5_Extract_Bad_Folders.py")
        print(Back.BLACK + Fore.WHITE + Style.BRIGHT + "6. Ejecutar 6_Test_Not_Use.py")
        print(Back.BLACK + Fore.WHITE + Style.BRIGHT + "q. Salir")

        choice = input("Elige una opción: ")
        if choice == 'q':
            break
        elif choice in ['1', '2', '3', '4', '5', '6']:
            execute_script(choice, colors[int(choice) - 1])

# Función para ejecutar un script
def execute_script(script_choice, color):
    script_name = f"{script_choice}_Rename_Archives.py"  # Reemplaza el nombre según la opción elegida
    print(color + f"Ejecutando {script_name}...")
    subprocess.Popen(["cmd", "/c", "start", "python", f"Archives_V1/{script_name}"], shell=True)

if __name__ == "__main__":
    show_menu()