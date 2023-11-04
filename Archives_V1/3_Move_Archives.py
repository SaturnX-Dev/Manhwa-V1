import os
import shutil
import re

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

# Función para crear una carpeta con un nombre común
def crear_carpeta(nombre_comun, intento=1):
    if intento > 1:
        nuevo_nombre = f"{nombre_comun} {intento}"
        nueva_ruta_carpeta = os.path.join(source_directory_folders, nuevo_nombre)
    else:
        nueva_ruta_carpeta = os.path.join(source_directory_folders, nombre_comun)

    try:
        os.makedirs(nueva_ruta_carpeta)
        return nueva_ruta_carpeta
    except FileExistsError:
        return crear_carpeta(nombre_comun, intento + 1)

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
            # Extraer palabras del nombre del archivo
            palabras = re.findall(r'\b\w+\b', archivo)

            # Filtrar palabras que no son números
            palabras = [palabra for palabra in palabras if not palabra.isnumeric()]

            # Unir las palabras para crear el nombre común
            nombre_comun = ' '.join(palabras)

            # Verificar si existe una carpeta con un nombre similar
            carpeta_existente = next((carpeta for carpeta in carpetas_en_folders if nombre_comun in carpeta), None)

            if carpeta_existente:
                # Ruta completa del archivo y carpeta
                ruta_archivo = os.path.join(source_directory_archives, archivo)
                ruta_carpeta = os.path.join(source_directory_folders, carpeta_existente)

                # Mover el archivo a la carpeta correspondiente
                shutil.move(ruta_archivo, ruta_carpeta)
                print(f"El archivo '{archivo}' ha sido movido a la carpeta '{carpeta_existente}'.")
            else:
                # Crear una nueva carpeta con el nombre común
                nueva_ruta_carpeta = crear_carpeta(nombre_comun)

                # Mover el archivo a la carpeta nueva
                ruta_archivo = os.path.join(source_directory_archives, archivo)
                shutil.move(ruta_archivo, nueva_ruta_carpeta)
                print(f"El archivo '{archivo}' ha sido movido a la nueva carpeta '{nombre_comun}'.")

# Menú
while True:
    print("Menú:")
    print("1. Listar archivos en 'Z:\Library\Raw'")
    print("2. Listar carpetas en 'Z:\Library\Reader'")
    print("3. Mover archivos a carpetas")
    print("4. Salir")

    opcion = input("Selecciona una opción (1/2/3/4): ")

    if opcion == '1':
        print("Archivos en 'Z:\Library\Raw':")
        archivos_en_archives = listar_archivos_en_archives()
        for archivo in archivos_en_archives:
            print(archivo)
    elif opcion == '2':
        print("Carpetas en 'Z:\Library\Readers':")
        carpetas_en_folders = listar_carpetas_en_folders()
        for carpeta in carpetas_en_folders:
            print(carpeta)
    elif opcion == '3':
        print("Moviendo archivos a carpetas...")
        mover_archivos_a_carpetas()
        print("Archivos movidos.")
    elif opcion == '4':
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida (1/2/3/4).")