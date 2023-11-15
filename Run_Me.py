import subprocess

def show_menu():
    while True:
        try:
            with open("menu.ans", "r") as file:
                ascii_art = file.read()
        except FileNotFoundError:
            print("Archivo 'menu.ans' no encontrado.")
            return
        print(ascii_art)
        print("Recuerda hacer un backup primero")
        print("Made with love <3")
        choice = input("┏━°⌜ どせい ⌟°━┓").strip().lower()
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
        elif choice == '7':
            subprocess.Popen(["cmd", "/c", "start", "python", "7_Delete_Pdf.py"], shell=True)
        else:
            print("\nOpción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    show_menu()