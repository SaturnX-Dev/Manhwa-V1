import subprocess
import shutil
import art

# Define la función para mostrar el menú con arte ASCII
def show_menu():
    while True:
        # Leer el arte ASCII desde un archivo .ans llamado "visual"
        try:
            with open("visual.ans", "r") as file:
                ascii_art = file.read()
        except FileNotFoundError:
            error_message = "Archivo 'visual.ans' no encontrado"
            terminal_width = shutil.get_terminal_size().columns
            # Centra el mensaje de error
            centered_error_message = error_message.center(terminal_width)
            print(centered_error_message)
            return

        # Centra el arte ASCII leído desde "visual.ans"
        terminal_width = shutil.get_terminal_size().columns
        max_art_length = max(len(line) for line in ascii_art.splitlines())
        for line in ascii_art.splitlines():
            centered_line = line.center(terminal_width)
            # Asegura que cada línea tenga la misma longitud que la más larga
            centered_line += " " * (terminal_width - len(centered_line))
            print(centered_line)

        # Genera el título "Script Master V1" y centra el texto
        title = art.text2art("Script Master V1")
        title_lines = title.splitlines()
        max_title_length = max(len(line) for line in title_lines)
        for line in title_lines:
            print(line.center(terminal_width))
        
        print("By SaturnX-Dev")   

        ascii_art_menu = """
        _________________________________________________
        |                                               |
        |    Script Master V1                           |
        |                                               |
        | 1. Ejecutar 1_Rename_Archives.py              |
        | 2. Ejecutar 2_Rename_Folders.py               |
        | 3. Ejecutar 3_Move_Archives.py                |
        | 4. Ejecutar 4_Mix_Folders.py                  |
        | 5. Ejecutar 5_Extract_Bad_Folders.py          |
        | 6. Ejecutar 6_Test_Not_Use.py                 |
        | Q. Salir                                      |
        |_______________________________________________|
        """

        # Ajusta la longitud de las líneas para que coincidan con el ancho de la terminal
        max_line_length = max(len(line) for line in ascii_art_menu.splitlines())
        for line in ascii_art_menu.splitlines():
            print(line.center(terminal_width))

        choice = input("Elige una opción: ").strip().lower()
        
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
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    show_menu()