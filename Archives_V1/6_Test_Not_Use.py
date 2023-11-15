import os
import re
import shutil

# Directorios de origen y destino
source_directory_archives = r'Z:\Library\Raw'
source_directory_folders = r'Z:\Library\Reader'

# Función para listar archivos en 'Z:\Library\Raw'
def listar_archivos_en_archives():
    archivos_en_archives = [filename for filename in os.listdir(source_directory_archives) if os.path.isfile(os.path.join(source_directory_archives, filename))]
    return archivos_en_archives

# Función para listar carpetas en 'Z:\Library\Reader'
def listar_carpetas_en_folders():
    carpetas_en_folders = [foldername for foldername in os.listdir(source_directory_folders) if os.path.isdir(os.path.join(source_directory_folders, foldername))]
    return carpetas_en_folders

# Función para mover archivos a las carpetas correspondientes
def mover_archivos_a_carpetas():
    archivos_en_archives = listar_archivos_en_archives()
    carpetas_en_folders = listar_carpetas_en_folders()

    for archivo in archivos_en_archives:
        nombre_comun = None

        # Encontrar un nombre común en las carpetas
        for carpeta in carpetas_en_folders:
            if carpeta in archivo:
                nombre_comun = carpeta
                break

        if nombre_comun:
            # Ruta completa del archivo y carpeta
            ruta_archivo = os.path.join(source_directory_archives, archivo)
            ruta_carpeta = os.path.join(source_directory_folders, nombre_comun)

            # Mover el archivo a la carpeta correspondiente
            shutil.move(ruta_archivo, ruta_carpeta)
            print(f"El archivo '{archivo}' ha sido movido a la carpeta '{nombre_comun}'.")
        else:
            print(f"El archivo '{archivo}' no tiene una carpeta correspondiente.")

# Menú
while True:
    print("Menú:")
    print("1. Listar archivos en Raw")
    print("2. Listar carpetas en Reader")
    print("3. Mover archivos a carpetas")
    print("4. Verificar archivos en carpetas y mover si es necesario")
    print("5. Salir")

    opcion = input("Selecciona una opción (1/2/3/4/5): ")

    if opcion == '1':
        print("Archivos en Raw:")
        archivos_en_archives = listar_archivos_en_archives()
        for archivo in archivos_en_archives:
            print(archivo)
    elif opcion == '2':
        print("Carpetas en Reader:")
        carpetas_en_folders = listar_carpetas_en_folders()
        for carpeta in carpetas_en_folders:
            print(carpeta)
    elif opcion == '3':
        print("Moviendo archivos a carpetas...")
        mover_archivos_a_carpetas()
        print("Archivos movidos.")
    elif opcion == '4':
        # Implementar la verificación de archivos en carpetas y mover si es necesario
        print("Verificando archivos en carpetas y moviendo si es necesario...")
        # Agregar código para esta opción
        print("Verificación completada.")
    elif opcion == '5':
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida (1/2/3/4/5).")