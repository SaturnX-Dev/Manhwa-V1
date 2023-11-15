import os
import shutil
import re

# Directorios de origen y destino
source_directory_archives = r'Z:\\Library\Raw'
source_directory_folders = r'Z:\\Library\Reader'

# Función para listar archivos en 'Z:\\Library\Raw'
def listar_archivos_en_archives():
    archivos_en_archives = [filename for filename in os.listdir(source_directory_archives) if os.path.isfile(os.path.join(source_directory_archives, filename))]
    return archivos_en_archives

# Función para listar carpetas en 'Z:\\Library\Reader'
def listar_carpetas_en_folders():
    carpetas_en_folders = [foldername for foldername in os.listdir(source_directory_folders) if os.path.isdir(os.path.join(source_directory_folders, foldername))]
    return carpetas_en_folders

# Función para crear una carpeta con un nombre común
def crear_carpeta(nombre_comun):
    # Eliminar caracteres no alfanuméricos ni espacios
    nombre_comun = re.sub(r'[^\w\s]', '', nombre_comun)

    # Excluir nombres específicos como "CBR", "CBZ", "PDF"
    palabras_excluidas = ["CBR", "CBZ", "PDF"]
    nombre_comun = ' '.join([palabra for palabra in nombre_comun.split() if palabra.upper() not in palabras_excluidas])

    # Construir la ruta completa de la carpeta
    ruta_carpeta = os.path.join(source_directory_folders, nombre_comun)

    # Crear la carpeta si no existe
    if not os.path.exists(ruta_carpeta):
        try:
            os.makedirs(ruta_carpeta)
        except FileExistsError:
            pass

    return ruta_carpeta

# Nueva función para mover archivos de un tipo específico a carpetas
def mover_archivos_por_tipo(tipo_archivo):
    archivos_en_archives = listar_archivos_en_archives()
    carpetas_en_folders = listar_carpetas_en_folders()

    for archivo in archivos_en_archives:
        if archivo.lower().endswith(tipo_archivo):
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
                # Extraer palabras del nombre del archivo
                palabras = re.findall(r'\b\w+\b', archivo)

                # Filtrar palabras que no son números
                palabras = [palabra for palabra in palabras if not palabra.isnumeric()]

                # Unir las palabras para crear el nombre común
                nombre_comun = ' '.join(palabras)

                # Verificar si existe una carpeta con un nombre similar
                carpeta_existente = next((carpeta for carpeta in carpetas_en_folders if nombre_comun.lower() in carpeta.lower()), None)

                if carpeta_existente:
                    # Ruta completa del archivo y carpeta
                    ruta_archivo = os.path.join(source_directory_archives, archivo)
                    ruta_carpeta = os.path.join(source_directory_folders, carpeta_existente)

                    # Mover el archivo a la carpeta correspondiente
                    shutil.move(ruta_archivo, ruta_carpeta)
                    print(f"El archivo '{archivo}' ha sido movido a la carpeta '{carpeta_existente}'.")
                else:
                    # Mover el archivo a la carpeta nueva o existente con el nombre común
                    ruta_carpeta = crear_carpeta(nombre_comun)
                    shutil.move(os.path.join(source_directory_archives, archivo), ruta_carpeta)
                    print(f"El archivo '{archivo}' ha sido movido a la carpeta '{nombre_comun}'.")

# Menú principal
while True:
    print("Menú:")
    print("1. Listar archivos en Raw")
    print("2. Listar carpetas en Reader")
    print("3. Mover archivos a carpetas por tipo")
    print("4. Salir")

    opcion = input("Selecciona una opción (1/2/3/4): ")

    if opcion == '1':
        print("Archivos en Raw:")
        archivos_en_archives = listar_archivos_en_archives()
        for archivo in archivos_en_archives:
            print(archivo)
    elif opcion == '2':
        print("Carpetas en Readers:")
        carpetas_en_folders = listar_carpetas_en_folders()
        for carpeta in carpetas_en_folders:
            print(carpeta)
    elif opcion == '3':
        # Submenú para seleccionar el tipo de archivo
        while True:
            print("Submenú - Seleccionar tipo de archivo:")
            print("1. Archivos CBR")
            print("2. Archivos CBZ")
            print("3. Archivos PDF")
            print("4. Volver al menú principal")

            opcion_tipo_archivo = input("Selecciona un tipo de archivo (1/2/3/4): ")

            if opcion_tipo_archivo == '1':
                print("Moviendo archivos CBR a carpetas...")
                mover_archivos_por_tipo('.cbr')
                print("Archivos CBR movidos.")
            elif opcion_tipo_archivo == '2':
                print("Moviendo archivos CBZ a carpetas...")
                mover_archivos_por_tipo('.cbz')
                print("Archivos CBZ movidos.")
            elif opcion_tipo_archivo == '3':
                print("Moviendo archivos PDF a carpetas...")
                mover_archivos_por_tipo('.pdf')
                print("Archivos PDF movidos.")
            elif opcion_tipo_archivo == '4':
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción válida (1/2/3/4).")
    elif opcion == '4':
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida (1/2/3/4).")