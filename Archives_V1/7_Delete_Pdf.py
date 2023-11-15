import os

# Directorio de carpetas
source_directory_folders = r'Z:\Library\Reader'

# Función para listar carpetas en 'Z:\Library\Reader'
def listar_carpetas_en_folders():
    carpetas_en_folders = [foldername for foldername in os.listdir(source_directory_folders) if os.path.isdir(os.path.join(source_directory_folders, foldername))]
    return carpetas_en_folders

# Función para buscar archivos PDF con versiones CBR o CBZ y devolver una lista de ellos
def buscar_pdf_con_versiones_cbr_cbz():
    archivos_a_eliminar = []

    carpetas_en_folders = listar_carpetas_en_folders()

    for folder in carpetas_en_folders:
        folder_path = os.path.join(source_directory_folders, folder)

        for root, dirs, files in os.walk(folder_path):
            for file in files:
                # Ruta completa del archivo actual
                file_path = os.path.join(root, file)

                # Verificar si el archivo actual es un PDF
                if file.lower().endswith(".pdf"):
                    # Construir las rutas para CBR y CBZ con el mismo nombre
                    base_name = os.path.splitext(file)[0]
                    cbr_path = os.path.join(root, base_name + ".cbr")
                    cbz_path = os.path.join(root, base_name + ".cbz")

                    # Verificar si existen las versiones CBR o CBZ
                    if os.path.exists(cbr_path) or os.path.exists(cbz_path):
                        archivos_a_eliminar.append(file_path)

    return archivos_a_eliminar

# Función para eliminar archivos proporcionados
def eliminar_archivos(archivos):
    for archivo in archivos:
        print("Eliminando archivo: {}".format(archivo))
        os.remove(archivo)

# Función para imprimir las carpetas en 'Z:\Library\Reader'
def imprimir_carpetas_en_folders():
    carpetas_en_folders = listar_carpetas_en_folders()
    print("Carpetas en {}: {}".format(source_directory_folders, carpetas_en_folders))

# Función principal para mostrar el menú
def mostrar_menu():
    while True:
        print("Menú:")
        print("1. Listar carpetas en Reader")
        print("2. Eliminar archivos PDF con versiones CBR o CBZ")
        print("3. Salir")

        opcion = input("Selecciona una opción (1/2/3): ")

        if opcion == '1':
            imprimir_carpetas_en_folders()
        elif opcion == '2':
            print("Buscando y eliminando archivos PDF con versiones CBR o CBZ...")
            archivos_a_eliminar = buscar_pdf_con_versiones_cbr_cbz()
            eliminar_archivos(archivos_a_eliminar)
            print("Eliminación completada.")
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida (1/2/3).")

# Ejecutar el menú
if __name__ == "__main__":
    mostrar_menu()