import os
import shutil

# Directorio de archivos
source_directory_archives = r'Z:\Library\Raw'

# Función para listar y extraer archivos de carpetas
def extraer_archivos_de_carpetas():
    carpetas_en_archives = [foldername for foldername in os.listdir(source_directory_archives) if os.path.isdir(os.path.join(source_directory_archives, foldername))]

    if not carpetas_en_archives:
        print("No se encontraron carpetas en 'Z:\Library\Raw'.")
        return

    for carpeta in carpetas_en_archives:
        carpeta_completa = os.path.join(source_directory_archives, carpeta)
        archivos_en_carpeta = [filename for filename in os.listdir(carpeta_completa) if os.path.isfile(os.path.join(carpeta_completa, filename))]

        if archivos_en_carpeta:
            for archivo in archivos_en_carpeta:
                ruta_archivo = os.path.join(carpeta_completa, archivo)
                ruta_destino = os.path.join(source_directory_archives, archivo)

                # Verificar si el archivo ya existe en la raíz
                if not os.path.exists(ruta_destino):
                    # Mover el archivo desde la carpeta a la ruta principal
                    shutil.move(ruta_archivo, ruta_destino)
                    print(f"El archivo '{archivo}' ha sido movido a la ruta principal.")

            # Opcionalmente, puedes eliminar la carpeta vacía después de mover los archivos
            # Si no deseas eliminar las carpetas, simplemente comenta o elimina la siguiente línea
            # os.rmdir(carpeta_completa)
            # print(f"La carpeta '{carpeta}' ha sido eliminada.")

# Función para eliminar carpetas vacías en 'Z:\Library\Raw'
def eliminar_carpetas_vacias():
    carpetas_en_archives = [foldername for foldername in os.listdir(source_directory_archives) if os.path.isdir(os.path.join(source_directory_archives, foldername))]

    carpetas_eliminadas = 0

    for carpeta in carpetas_en_archives:
        carpeta_completa = os.path.join(source_directory_archives, carpeta)
        if not os.listdir(carpeta_completa):
            os.rmdir(carpeta_completa)
            print(f"La carpeta vacía '{carpeta}' ha sido eliminada.")
            carpetas_eliminadas += 1

    if carpetas_eliminadas == 0:
        print("No se encontraron carpetas vacías para eliminar en Raw.")

# Menú
while True:
    print("Menú:")
    print("1. Extraer archivos de carpetas en Raw")
    print("2. Eliminar carpetas vacías en Raw")
    print("3. Salir")

    opcion = input("Selecciona una opción (1/2/3): ")

    if opcion == '1':
        print("Extrayendo archivos de carpetas...")
        extraer_archivos_de_carpetas()
        print("Extracción de archivos completada.")
    elif opcion == '2':
        print("Eliminando carpetas vacías...")
        eliminar_carpetas_vacias()
        print("Eliminación de carpetas vacías completada.")
    elif opcion == '3':
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida (1/2/3).")