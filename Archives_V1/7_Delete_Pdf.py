import os

# Solicitar al usuario que ingrese el directorio de origen
source_directory = input("Ingresa Directorio de Origen: ")

# Verificar si el directorio de origen existe
if not os.path.exists(source_directory):
    print("El directorio de origen ingresado no existe. Por favor, verifica la ruta.")
    exit()

# Solicitar al usuario que ingrese el directorio de destino
destination_directory = input("Ingresa Directorio de Destino: ")

# Verificar si el directorio de destino existe
if not os.path.exists(destination_directory):
    print("El directorio de destino ingresado no existe. Por favor, verifica la ruta.")
    exit()

# Función para listar carpetas en un directorio
def listar_carpetas_en_directorio(directorio):
    carpetas_en_directorio = [foldername for foldername in os.listdir(directorio) if os.path.isdir(os.path.join(directorio, foldername))]
    return carpetas_en_directorio

# Función para buscar archivos PDF con versiones CBR o CBZ y devolver una lista de ellos
def buscar_pdf_con_versiones_cbr_cbz(directorio):
    archivos_a_eliminar = []

    carpetas_en_directorio = listar_carpetas_en_directorio(directorio)

    # Buscar archivos en la carpeta principal del directorio
    for file in os.listdir(directorio):
        file_path = os.path.join(directorio, file)
        if os.path.isfile(file_path) and file.lower().endswith(".pdf"):
            base_name = os.path.splitext(file)[0]
            cbr_path = os.path.join(directorio, base_name + ".cbr")
            cbz_path = os.path.join(directorio, base_name + ".cbz")

            # Verificar si existen las versiones CBR o CBZ
            if os.path.exists(cbr_path) or os.path.exists(cbz_path):
                archivos_a_eliminar.append(file_path)

    # Buscar archivos en carpetas y subcarpetas
    for folder in carpetas_en_directorio:
        folder_path = os.path.join(directorio, folder)

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

# Función para imprimir las carpetas en un directorio
def imprimir_carpetas_en_directorio(directorio):
    carpetas_en_directorio = listar_carpetas_en_directorio(directorio)
    print("Carpetas en {}: {}".format(directorio, carpetas_en_directorio))

# Función para mostrar el menú de Trabajar en Reader
def menu_reader():
    while True:
        print("Menú Trabajar en Reader:")
        print("1. Listar carpetas en Reader")
        print("2. Eliminar archivos PDF con versiones CBR o CBZ en Reader")
        print("3. Volver al menú principal")

        opcion = input("Selecciona una opción (1/2/3): ")

        if opcion == '1':
            imprimir_carpetas_en_directorio(source_directory_folders)
        elif opcion == '2':
            print("Buscando y eliminando archivos PDF con versiones CBR o CBZ en Reader...")
            archivos_a_eliminar = buscar_pdf_con_versiones_cbr_cbz(source_directory_folders)
            eliminar_archivos(archivos_a_eliminar)
            print("Eliminación en Reader completada.")
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida (1/2/3).")

# Función para mostrar el menú de Trabajar en Raw
def menu_raw():
    while True:
        print("Menú Trabajar en Raw:")
        print("1. Listar carpetas en Raw")
        print("2. Eliminar archivos PDF con versiones CBR o CBZ en Raw")
        print("3. Volver al menú principal")

        opcion = input("Selecciona una opción (1/2/3): ")

        if opcion == '1':
            imprimir_carpetas_en_directorio(source_directory_archives)
        elif opcion == '2':
            print("Buscando y eliminando archivos PDF con versiones CBR o CBZ en Raw...")
            archivos_a_eliminar = buscar_pdf_con_versiones_cbr_cbz(source_directory_archives)
            eliminar_archivos(archivos_a_eliminar)
            print("Eliminación en Raw completada.")
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida (1/2/3).")

# Función principal para mostrar el menú principal
def mostrar_menu_principal():
    while True:
        print("Menú Principal:")
        print("1. Trabajar en Reader")
        print("2. Trabajar en Raw")
        print("3. Salir")

        opcion = input("Selecciona una opción (1/2/3): ")

        if opcion == '1':
            menu_reader()
        elif opcion == '2':
            menu_raw()
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida (1/2/3).")

# Ejecutar el menú principal
if __name__ == "__main__":
    mostrar_menu_principal()